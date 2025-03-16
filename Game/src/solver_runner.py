from src import board
from src.solver import Solver
from src.setup import *
import time


class runner:
    @staticmethod
    def a_star_runner(checks):
        block_moved = False
        print("Solving level...")
        start = time.time()
        moves = Solver.a_star(board, blocks)
        end = time.time()
        for move in moves:
            for block in blocks:
                if block.id == move["block_id"]:
                    block.dragging = True
                    block.update_position(
                        (
                            move["current_position"][0] * tile_size,
                            move["current_position"][1] * tile_size,
                        ),
                        board,
                    )
                    block.dragging = False

                if block.position != block.initial_position:
                    block_moved = True
                    print(
                        f"Block moved from {block.initial_position} to {block.position}"
                    )

            if block_moved:
                move_counter.increment()
                print(f"Moves: {move_counter.get_count()}")
                screen.fill(DarkGrey)
                menu_button.render()
                # Render the move counter at the bottom of the screen
                move_text = blocky_font.render(
                    f"Moves: {move_counter.get_count()}", True, White
                )
                move_text_rect = move_text.get_rect(
                    center=(Screen_Width // 2, Screen_Height - 20)
                )
                screen.blit(move_text, move_text_rect)

            # Rerender the board and blocks after each move
            board.render(screen, tile_size)
            for block in blocks:
                block.render(screen)

            # Update the display
            # board.display()
            pygame.time.delay(60)
            block_moved = False

        print(
            f"Solved level in {round(end - start,3)} seconds using {len(moves)} moves"
        )
        checks["runner_finished"] = True
