import time
import pygame

from menu import Menu
from levels import *
from board import Board
from setting import *
from solver import * 

# Set up display
pygame.init()
screen = pygame.display.set_mode((Screen_Width, Screen_Height))
pygame.display.set_caption(Title)

# Imported my own icon into the game
program_icon = pygame.image.load('./assets/icon.png')
pygame.display.set_icon(program_icon)
# pygame.time.Clock()
board = Board()
current_level_index = 0
blocks = []
levels = get_levels() 
menu = Menu(screen)
# Main menu
game_state = "stage_0"

def level(index):
    # Load the selected level 
    global blocks
    current_level = levels[index]
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

def events():
    global game_state, current_level_index, blocks
    
    # Event for the game to close/quit when the window is closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit(0)
        
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = event.pos
            if game_state == "stage_0":
                if menu.play_button.collidepoint(mouse_pos):
                    # Transition to level selection
                    game_state = "stage_0_1"
            elif game_state == "stage_0_1":
                for index in range(len(levels)):
                    level_rect = pygame.Rect(Screen_Width // 2 - 100, Screen_Height // 4 + index * 50 - 20, 200, 40)
                    if level_rect.collidepoint(mouse_pos):
                        current_level_index = index
                        # Load the selected level
                        level(index) 
                        # Starting the game by switching to stage_1
                        board.game_state = "stage_1"
                        game_state = "stage_1"

            # Block dragging
            if board.game_state == "stage_1":
                for block in blocks:
                    block.start_drag(mouse_pos)

        elif event.type == pygame.MOUSEMOTION and board.game_state == "stage_1":
            for block in blocks:
                mouse_pos = pygame.mouse.get_pos()
                block.update_position(mouse_pos, board)

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            for block in blocks:
                board.display()
                block.stop_drag()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_0:
            display_mouse_position()
        
        if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
            for i in bfs(board, blocks):
                for block in blocks:
                    if block.id == i["block_id"]:
                        block.dragging = True
                        block.update_position((i["current_position"][0] * tile_size, i["current_position"][1] * tile_size), board)
                        block.dragging = False
                time.sleep(1)

def draw():
    """
    # Now stage_0 is the menu, 
    # stage_0_1 equals to the level selection, 
    # and stage_1 equals to the gameplay.
    # Lastly, stage_2 equals to the player won the level.
    
    # Future going to add other stages with differen functions
    """
    if game_state == "stage_0":
        menu.render()
    elif game_state == "stage_0_1":
        menu.render_level_selection(levels)  

        # Draw level buttons
        for index in range(len(levels)):
            level_rect = pygame.Rect(Screen_Width // 2 - 100, Screen_Height // 4 + index * 50 - 20, 200, 40)
            # Draw button background
            pygame.draw.rect(screen, LightGrey, level_rect)
            # Draw level text
            level_text = menu.button_font.render(f"Level {index + 1}", True, DarkGrey)
            level_text_rect = level_text.get_rect(center=level_rect.center)
            screen.blit(level_text, level_text_rect)
            
    if board.game_state == "stage_1":
        screen.fill(DarkGrey)
        board.render(screen, tile_size)
        for block in blocks:
            block.render(screen)
        pygame.display.flip()

    """
    # Check if the red car has reached the exit if so stage_2
    # Console and game output
    """
    if board.exit_check():
        board.game_state = "stage_2"
        screen.fill(DarkGrey)
        # Rendering the winning message
        font = pygame.font.Font(None, 36)
        text = font.render("You win", True, (255, 255, 255))
        text_rect = text.get_rect(
            center=(Screen_Width // 2, Screen_Height // 2))
        screen.blit(text, text_rect)
        #print("You win!")
        pygame.display.flip()


def run():
    game_running = True
    while game_running:
        events()
        draw()
        
if __name__ == "__main__":
    run()
