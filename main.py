
import pygame

from board import Board
from setting import *

# Set up display
pygame.init()
screen = pygame.display.set_mode((Screen_Width, Screen_Height))
pygame.display.set_caption(Title)
# pygame.time.Clock()
board = Board()


# Event for the game to close/quit when the window is closed
def events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit(0)
            
def draw():
    
    # Added a loop if the game start will be in stage_1
    if board.game_state == "stage_1":
        screen.fill(DarkGrey)
        # Can be removed
        board.display()  # Concole board
        
        # Render the board
        board.render(screen, tile_size)
        
        # Update the display
        pygame.display.flip()
        
    # Check if the red car has reached the exit if so stage_2
    # Console and game output

    if board.exit_check():
        board.game_state = "stage_2"
        screen.fill(DarkGrey)
        # Rendering the winning message
        font = pygame.font.Font(None, 36)
        text = font.render("You win", True, (255, 255, 255))
        text_rect = text.get_rect(center=(600 // 2, 600 // 2))
        screen.blit(text, text_rect)
        print("You win! Red car reached the exit!")
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