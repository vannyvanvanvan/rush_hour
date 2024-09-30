import pygame

from block import Block
from board import Board
from setting import *

# Set up display
pygame.init()
screen = pygame.display.set_mode((Screen_Width, Screen_Height))
pygame.display.set_caption(Title)
# pygame.time.Clock()
board = Board()


# Test blocks will add a library to store game data later
red_block = Block(position=[3, 2], orientation='h', colour=Red, size=2)
#yellow_block = Block(position=[0, 0], orientation='h', colour=Yellow, size=2)
yellow_block = Block(position=[0, 3], orientation='v', colour=Yellow, size=3)

# Place the blocks on the board
board.place_block(red_block)
board.place_block(yellow_block)

# Display the initial board state
# Console output after placing blocks
board.display() 

# Event for the game to close/quit when the window is closed
def events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit(0)
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Left mouse button
            if event.button == 1:  
                mouse_pos = event.pos
                red_block.start_drag(mouse_pos)
                yellow_block.start_drag(mouse_pos)

        if event.type == pygame.MOUSEBUTTONUP:
            # Left mouse button
            if event.button == 1: 
                red_block.stop_drag()
                yellow_block.stop_drag()
                
        
        if red_block.dragging:
            mouse_pos = pygame.mouse.get_pos()
            red_block.update_position(mouse_pos, board.board)  # Pass the board array
        
        if yellow_block.dragging:
            mouse_pos = pygame.mouse.get_pos()
            yellow_block.update_position(mouse_pos, board.board)  # Pass the board array
            
def draw():
    
    # Added a loop, which is called game_state for soft locks
    # game start = stage_1
    # game, map finishes = stage_2
    if board.game_state == "stage_1":
        screen.fill(DarkGrey)
        
        # Can be removed
        board.display()                     # Concole board
        
        board.render(screen, tile_size)     # Render the board
        red_block.render(screen)            # Render the red block
        yellow_block.render(screen)            # Render the red block
        
        pygame.display.flip()               # Update the display
        
    # Check if the red car has reached the exit if so stage_2
    # Console and game output
    if board.exit_check():
        board.game_state = "stage_2"
        screen.fill(DarkGrey)
        # Rendering the winning message
        font = pygame.font.Font(None, 36)
        text = font.render("You win", True, (255, 255, 255))
        text_rect = text.get_rect(center=(Screen_Width  // 2, Screen_Height  // 2))
        screen.blit(text, text_rect)
        print("You win!")
        pygame.display.flip()
            
def run():
    game_running = True
    while game_running:
        events()
        draw()
        
        #if board.game_state == "stage_3":

            #game_running = False
            
if __name__ == "__main__":
    run()