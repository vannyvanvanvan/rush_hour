import pygame, threading
from src.spec_check import get_system_specs, wrap_text
from src.beachmark import run_beachmark
from src.solver_runner import runner
from src.sleeper import sleeper
from src.setup import *


def level(index):
    # Load the selected level
    global blocks
    current_level = levels[index]
    board.reset()
    blocks.clear()
    for block_data in current_level["blocks"]:
        new_block = copy.deepcopy(block_data)
        blocks.append(new_block)
        board.place_block(new_block)


# For level creation easier for myself to keep track of the location of each blocks array
def display_mouse_position():
    mouse_pos = pygame.mouse.get_pos()
    grid_x = mouse_pos[0] // tile_size
    grid_y = mouse_pos[1] // tile_size
    print(f"Mouse position in grid: ({grid_x}, {grid_y})")
    print(f"Array: ({grid_y}, {grid_x})")
    print("========================")


# This is where the game elements are functioned 
def events(checks: dict, threads: dict):
    global current_level_index, blocks, game_running, current_beachmark_index, beachmark_results
    # Event for the game to close/quit when the window is closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            window_xp_logoff_sound.play()
            pygame.time.delay(2000)
            game_running = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = event.pos
            if board.game_state == "stage_0":
                # Reset counter for move
                move_counter.reset()
                if menu.play_button.collidepoint(mouse_pos):
                    # Transition to level selection
                    button_click_sound.play()
                    board.game_state = "stage_0_1"
                elif menu.beachmark_button.collidepoint(mouse_pos):
                    button_click_sound.play()
                    board.game_state = "stage_0_2"

            elif board.game_state == "stage_0_1":

                for index in range(len(levels)):
                    level_rect = pygame.Rect(
                        Screen_Width // 2 - 100,
                        Screen_Height // 4 + index * 50 - 20,
                        200,
                        40,
                    )
                    if level_rect.collidepoint(mouse_pos):
                        current_level_index = index
                        # Load the selected level
                        level(index)

                        # Starting the game by switching to stage_1
                        button_click_sound.play()
                        board.game_state = "stage_1"
                        
                        
            elif board.game_state == "stage_0_2":
                for index in range(len(levels)):
                    level_rect = pygame.Rect(
                        Screen_Width//2 - 100,
                        Screen_Height//4 + index*50 - 20,
                        200, 40
                    )
                    if level_rect.collidepoint(mouse_pos):
                        current_level_index = index
                        level(index)
                        # Reset benchmark state
                        beachmark_results.clear()
                        current_beachmark_index = 0
                        checks["beachmark_started"] = False
                        checks["beachmark_finished"] = False
                        board.game_state = "stage_1_2"
                        
                        # Start benchmarking thread
                        threads["beachmark"] = threading.Thread(target=run_beachmark, args=(checks,))
                        threads["beachmark"].start()
                        print("Benchmarking thread started")

            # Block dragging
            elif board.game_state == "stage_1":
                if menu_button.play_button.collidepoint(mouse_pos):
                    button_click_sound.play()
                    # Reset the board
                    board.reset()
                    board.game_state = "stage_0"

                # Undo button clicked
                elif menu_button.undo_button.collidepoint(mouse_pos):
                    # Check if there are moves to undo
                    if board.undo_stack:  
                        # Get last move from the stack
                        last_move = board.undo_stack.pop() 
                        for block in blocks:
                            if block.id == last_move["block_id"]:
                                # Save the current position
                                redo_move = {
                                    "block_id": block.id,
                                    "from": block.position.copy(),
                                    "to": last_move["from"].copy(),
                                }
                                board.redo_stack.append(redo_move)
                                board.clear_block(block)
                                block.position = last_move["from"].copy()
                                # Place the block in the new position
                                board.place_block(block)
                                block_move_sound.play()
                                move_counter.decrement()  

                # Redo button clicked
                elif menu_button.redo_button.collidepoint(mouse_pos):     
                    # Redo similar to undo
                    if board.redo_stack:
                        redo_move = board.redo_stack.pop()  
                        for block in blocks:
                            if block.id == redo_move["block_id"]:
                                undo_move = {
                                    "block_id": block.id,
                                    "from": block.position.copy(),
                                    "to": redo_move["from"].copy(),
                                }
                                board.undo_stack.append(undo_move)
                                board.clear_block(block)
                                block.position = redo_move["from"].copy()
                                board.place_block(block)
                                block_move_sound.play()
                                move_counter.increment()
                                
                for block in blocks:
                    # Saving up the initial position
                    block.initial_position = block.position[:]
                    block.start_drag(mouse_pos)
            
            elif board.game_state == "stage_1_3":
                back_button = pygame.Rect(20, Screen_Height-70, 100, 50)
                if back_button.collidepoint(mouse_pos):
                    button_click_sound.play()
                    board.game_state = "stage_0"
                    # Reset benchmark state
                    beachmark_results.clear()
                    current_beachmark_index = 0
                    checks["beachmark_started"] = False
                    checks["beachmark_finished"] = False

        elif event.type == pygame.MOUSEMOTION and board.game_state == "stage_1":
            # Moving the block
            for block in blocks:
                mouse_pos = pygame.mouse.get_pos()
                block.update_position(mouse_pos, board)

        elif board.game_state == "stage_1":

            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                # Create a loop for when the block is moved
                for block in blocks:
                    block.stop_drag()

                    # Check if the block moved
                    if block.position != block.initial_position:
                        block_move_sound.play()
                        move_counter.increment()
                        print(
                            f"Block moved from {block.initial_position} to {block.position}"
                        )
                        board.display()
                        move_details = {
                            "block_id": block.id,
                            "from": block.initial_position.copy(),
                            "to": block.position.copy(),
                        }
                        board.undo_stack.append(move_details)
                        
                        board.redo_stack = []  

            if event.type == pygame.KEYDOWN and event.key == pygame.K_0:
                # Excuse check mouse position
                display_mouse_position()

            elif (
                event.type == pygame.KEYDOWN
                and event.key == pygame.K_s
                and not checks["runner_started"]
            ):
                # Solver stage
                board.game_state = "stage_1_1"
                checks["runner_started"] = True
                threads["runner"] = threading.Thread(
                    target=runner.a_star_runner, args=(checks,)
                )
                threads["runner"].start()
                checks["runner_finished"] = False

    # End runner when done
    if checks["runner_started"] and checks["runner_finished"]:
        threads["runner"].join()
        checks["runner_started"] = False
        checks["runner_finished"] = True
        
    # Check if the red car has reached the exit if so stage_2
    if checks["runner_finished"] and not checks["sleep_started"] and board.exit_check():
        board.game_state = "stage_2"
        win_sound.play()
        checks["sleep_started"] = True
        threads["sleeper"] = threading.Thread(
            target=sleeper.sleep, args=(checks, 3,)
        )
        threads["sleeper"].start()
        checks["sleep_finished"] = False

    # End win sleep when done
    if checks["sleep_started"] and checks["sleep_finished"]:
        threads["sleeper"].join()
        checks["sleep_started"] = False
        checks["sleep_finished"] = True
        board.reset()
        board.game_state = "stage_0"
    
    # Check benchmarking status if thread exists
    if board.game_state == "stage_1_2" and checks["beachmark_started"]:
        if checks["beachmark_finished"]:
            print("Benchmark completed, showing results")
            board.game_state = "stage_1_3"
            if "beachmark" in threads:
                threads["beachmark"].join()

# This is where the game elements are rendered 
def draw(checks: dict):
    
    # """
    # stage_0 = menu,
    # stage_0_1 = level selection (play),
    # stage_0_2 = level selection (Beachmark),
    # stage_1 = gameplay,
    # stage_1_1 = solver stage,
    # stage_2 = player won,
    
    # stage_1_2 = beachmark running,
    # stage_1_3 = beachmark results,
    # stage_2 = player won
    # """
    
    screen.fill(DarkGrey)

    if board.game_state == "stage_0":
        menu.render()
    elif board.game_state == "stage_0_1":
        menu.render_level_selection(levels)

        # Draw level buttons
        for index in range(len(levels)):
            level_rect = pygame.Rect(
                Screen_Width // 2 - 100, Screen_Height // 4 + index * 50 - 20, 200, 40
            )
            # Draw button background
            pygame.draw.rect(screen, Silver, level_rect)
            # Draw level text
            level_text = blocky_font.render(f"Level {index + 1}", True, Black)
            screen.blit(level_text, level_text.get_rect(center=level_rect.center))
            
    elif board.game_state == "stage_0_2":
        menu.render_level_selection(levels)
        for index in range(len(levels)):
            level_rect = pygame.Rect(
                Screen_Width//2 - 100,
                Screen_Height//4 + index*50 - 20,
                200, 40
            )
            pygame.draw.rect(screen, Silver, level_rect)
            level_text = blocky_font.render(f"Level {index+1}", True, Black)
            screen.blit(level_text, level_text.get_rect(center=level_rect.center))

    elif board.game_state in ["stage_1", "stage_1_1"]:

        if board.game_state == "stage_1":
            menu_button.render()

        # Render the move counter at the bottom of the screen
        move_text = blocky_font.render(
            f"Moves: {move_counter.get_count()}", True, White
        )
        move_text_rect = move_text.get_rect(
            center=(Screen_Width // 2, Screen_Height - 20)
        )
        screen.blit(move_text, move_text_rect)

        # Render the board
        board.render(screen, tile_size)
        for block in blocks:
            block.render(screen)

    elif board.game_state == "stage_2":

        screen.fill(DarkGrey)
        
        # Rendering the winning message
        move_text = blocky_font.render(
            f"Moves: {move_counter.get_count()}", True, White
        )
        move_text_rect = move_text.get_rect(
            center=(Screen_Width // 2, Screen_Height // 2 - 40)
        )
        screen.blit(move_text, move_text_rect)

        winning_text = blocky_font.render("You win", True, White)
        winning_text_rect = winning_text.get_rect(
            center=(Screen_Width // 2, Screen_Height // 2)
        )
        screen.blit(winning_text, winning_text_rect)
        
    elif board.game_state == "stage_1_2":
        screen.fill(DarkGrey)
        # Showing the progress
        solving_rect = pygame.Rect(Screen_Width//2 - 150, Screen_Height//3, 300, 80)
        pygame.draw.rect(screen, Silver, solving_rect)
        solving_text = blocky_font.render("Benchmarking...", True, Black)
        screen.blit(solving_text, solving_text.get_rect(center=solving_rect.center))
        
        # Showing the current algorithm that is being tested and add a check for a valid index
        if 0 <= current_beachmark_index < len(algorithms):
            current_algo = algorithms[current_beachmark_index]
            algo_text = blocky_font.render(f"Running {current_algo}", True, White)
            screen.blit(algo_text, algo_text.get_rect(center=(Screen_Width//2, Screen_Height//2)))
        
    elif board.game_state == "stage_1_3":
        screen.fill(DarkGrey)
        title_text = blocky_font.render("Beachmark Results", True, White)
        screen.blit(title_text, title_text.get_rect(center=(Screen_Width//2, 50)))
        
        # Rendering system specs
        specs = get_system_specs()
        y_pos = 100
        max_text_width = Screen_Width - 40

        # Render each spec
        spec_lines = [
            f"CPU: {specs['CPU']}",
            f"Cores/Threads: {specs['Cores']}/{specs['Threads']}",
            f"RAM: {specs['RAM']}",
        ]

        for line in spec_lines:
            wrapped = wrap_text(line, blocky_font, max_text_width)
            for sub_line in wrapped:
                text_surface = blocky_font.render(sub_line, True, White)
                screen.blit(text_surface, (20, y_pos))
                y_pos += 30
        
        # First element of the solver results
        y_pos = 300
        for result in beachmark_results:
            result_str = f"{result['algorithm']}: {result['moves']} moves, {result['duration']}s"
            result_text = blocky_font.render(result_str, True, White)
            screen.blit(result_text, result_text.get_rect(center=(Screen_Width//2, y_pos)))
            y_pos += 70

        back_button = pygame.Rect(20, Screen_Height-70, 100, 50)
        pygame.draw.rect(screen, Silver, back_button)
        back_text = blocky_font.render("Back", True, Black)
        screen.blit(back_text, back_text.get_rect(center=back_button.center))
        
    # if True:
    if checks["runner_started"] and not checks["runner_finished"]:
        solving_rect = pygame.Rect(
            Screen_Width // 2 - 150, Screen_Height // 3, 300, 80
        )
        pygame.draw.rect(screen, Silver, solving_rect)
        # Draw solving text
        solving_text = blocky_font.render(f"Solving...", True, Black)
        solving_text_rect = solving_text.get_rect(center=solving_rect.center)
        screen.blit(solving_text, solving_text_rect)

    pygame.display.flip()
        
def run():
    global game_running
    game_running = True
    checks = {
        "runner_started": False,
        "runner_finished": True,
        "sleep_started": False,
        "sleep_finished": True,
        "beachmark_started": False,
        "beachmark_finished": False
    }
    threads = {}

    while game_running:
        events(checks, threads)
        draw(checks)
    
    pygame.quit()


if __name__ == "__main__":
    run()