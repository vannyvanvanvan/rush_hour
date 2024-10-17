import pygame

from levels import *
from board import Board
from setting import *

# Set up display
pygame.init()
screen = pygame.display.set_mode((Screen_Width, Screen_Height))
pygame.display.set_caption(Title)

# Imported my own icon into the game
program_icon = pygame.image.load('./assets/icon.png')
pygame.display.set_icon(program_icon)
# pygame.time.Clock()
board = Board()


# Get levels
levels = get_levels()
# Load levels, will change later for menu select
current_level = levels[0]

blocks = []
for block_data in current_level['blocks']:
    block = block_data
    blocks.append(block)
    board.place_block(block)
    
# For level creation easier for myself to keep track of the location of each blocks array
def display_mouse_position():
    mouse_pos = pygame.mouse.get_pos()
    grid_x = mouse_pos[0] // tile_size
    grid_y = mouse_pos[1] // tile_size
    print(f"Mouse position in grid: ({grid_x}, {grid_y})")
    print(f"Array: ({grid_y}, {grid_x})")
    print("========================")

# Event for the game to close/quit when the window is closed


def events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit(0)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = event.pos
                for block in blocks:
                    block.start_drag(mouse_pos)
                    
        elif event.type == pygame.MOUSEMOTION:
            # Update the position of the block when dragging it
            for block in blocks:
                mouse_pos = pygame.mouse.get_pos()
                block.update_position(mouse_pos,  board.board) 

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                for block in blocks:
                    # Moved the display function to here, so it will be printed out
                    # Everytime player releases the mouse
                    board.display()
                    block.stop_drag()
      
        # When pressed "0" i can see where my pointer pointed to which array
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0:
                display_mouse_position()


def draw():

    # Added a loop, which is called game_state for soft locks
    # game start = stage_1
    # game, map finishes = stage_2
    if board.game_state == "stage_1":
        screen.fill(DarkGrey)

        board.render(screen, tile_size)
        # Render all blocks
        for block in blocks:
            block.render(screen)
        # Update display
        pygame.display.flip()

    # Check if the red car has reached the exit if so stage_2
    # Console and game output
    if board.exit_check():
        board.game_state = "stage_2"
        screen.fill(DarkGrey)
        # Rendering the winning message
        font = pygame.font.Font(None, 36)
        text = font.render("You win", True, (255, 255, 255))
        text_rect = text.get_rect(
            center=(Screen_Width // 2, Screen_Height // 2))
        screen.blit(text, text_rect)
        print("You win!")
        pygame.display.flip()


def run():
    game_running = True
    while game_running:
        events()
        draw()

        # if board.game_state == "stage_3":

        # game_running = False


if __name__ == "__main__":
    run()
