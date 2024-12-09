import pygame
from src.setup import *

def level(index):
    # Load the selected level 
    global blocks
    current_level = levels[index]
    board.reset()
    blocks.clear()
    for block_data in current_level['blocks']:
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

def events():
    # All the events handlers
    global current_level_index, blocks    
    # Event for the game to close/quit when the window is closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            window_xp_logoff_sound.play()
            pygame.time.delay(2000) 
            pygame.quit()
            quit(1)
        
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = event.pos
            if board.game_state == "stage_0":
                # Reset counter for move
                move_counter.reset()
                if menu.play_button.collidepoint(mouse_pos):
                    # Transition to level selection
                    button_click_sound.play()
                    board.game_state = "stage_0_1"
                    
            elif board.game_state == "stage_0_1":
                
                for index in range(len(levels)):
                    level_rect = pygame.Rect(Screen_Width // 2 - 100, Screen_Height // 4 + index * 50 - 20, 200, 40)
                    if level_rect.collidepoint(mouse_pos):
                        current_level_index = index
                        # Load the selected level
                        level(index) 
                        
                        # Starting the game by switching to stage_1
                        button_click_sound.play()
                        board.game_state = "stage_1"
               
            # Block dragging
            if board.game_state == "stage_1":
                if menu_button.play_button.collidepoint(mouse_pos):
                    button_click_sound.play()
                    # Reset the board
                    board.reset()
                    board.game_state = "stage_0"
                    
                for block in blocks:
                    # Saving up the initial position
                    block.initial_position = block.position[:]
                    block.start_drag(mouse_pos)

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
                        print(f"Block moved from {block.initial_position} to {block.position}")
                        board.display()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_0:
                # Excuse check mouse position
                display_mouse_position()
            
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                # Solver stage
                board.game_state = "stage_1_1"

def draw():
    
    """
    # stage_0 = menu, 
    # stage_0_1 = level selection, 
    # stage_1 = gameplay,
    # stage_1_1 = solver stage,
    # stage_2 = player won.
    
    # Future going to add other stages with differen functions
    """
    screen.fill(DarkGrey)
    
    if board.game_state == "stage_0":
        menu.render()
    elif board.game_state == "stage_0_1":
        menu.render_level_selection(levels)  

        # Draw level buttons
        for index in range(len(levels)):
            level_rect = pygame.Rect(Screen_Width // 2 - 100, Screen_Height // 4 + index * 50 - 20, 200, 40)
            # Draw button background
            pygame.draw.rect(screen, Silver, level_rect)
            # Draw level text
            level_text = blocky_font.render(f"Level {index + 1}", True, Black)
            level_text_rect = level_text.get_rect(center=level_rect.center)
            screen.blit(level_text, level_text_rect)
            
    elif board.game_state == "stage_1":
        menu_button.render()
        
        # Render the move counter at the bottom of the screen
        move_text = blocky_font.render(f"Moves: {move_counter.get_count()}", True, White)
        move_text_rect = move_text.get_rect(center=(Screen_Width // 2, Screen_Height - 20))
        screen.blit(move_text, move_text_rect)
        
        # Render the board
        board.render(screen, tile_size)
        for block in blocks:
            block.render(screen)
            
    elif board.game_state == "stage_1_1":        
        block_moved = False
        # Excuse BFS function      
        for move in bfs(board, blocks):
            for block in blocks:
                if block.id == move["block_id"]:
                    block.dragging = True
                    block.update_position(
                        (move["current_position"][0] * tile_size, move["current_position"][1] * tile_size),
                        board
                    )
                    block.dragging = False
                    
                    
                if block.position != block.initial_position:
                    block_moved = True
                    print(f"Block moved from {block.initial_position} to {block.position}")
                    
            if block_moved:
                move_counter.increment()
                print(f"Moves: {move_counter.get_count()}")
                screen.fill(DarkGrey)
                menu_button.render()
                # Render the move counter at the bottom of the screen
                move_text = blocky_font.render(f"Moves: {move_counter.get_count()}", True, White)
                move_text_rect = move_text.get_rect(center=(Screen_Width // 2, Screen_Height - 20))
                screen.blit(move_text, move_text_rect)
                
            # Rerender the board and blocks after each move 
            board.render(screen, tile_size)
            for block in blocks:
                block.render(screen)

            # Update the display
            pygame.display.flip()
            board.display()
            pygame.time.delay(100) 
    """
    # Check if the red car has reached the exit if so stage_2
    # Console and game output
    """
    if board.exit_check():
        
        board.game_state = "stage_2"
        
        screen.fill(DarkGrey)
        # Rendering the winning message
            
        move_text = blocky_font.render(f"Moves: {move_counter.get_count()}", True, White)
        move_text_rect = move_text.get_rect(center=(Screen_Width // 2, Screen_Height // 2 - 40))
        screen.blit(move_text, move_text_rect)            
        
        winning_text = blocky_font.render("You win", True, White)
        winning_text_rect = winning_text.get_rect(center=(Screen_Width // 2, Screen_Height // 2))
        screen.blit(winning_text, winning_text_rect)
        
        board.reset()
        win_sound.play()
        pygame.display.flip()
        pygame.time.delay(3000)
        board.game_state = "stage_0"
        #print("You win!")
    pygame.display.flip()


def run():
    game_running = True
    while game_running:
        events()
        draw()
        
if __name__ == "__main__":
    run()
