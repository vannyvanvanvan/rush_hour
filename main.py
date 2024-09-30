import pygame

from board import Board
from setting import *

# Set up display
pygame.init()
screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption(Title)
# pygame.time.Clock()
board = Board()


# Event for the game to close/quit when the window is closed
def events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit(0)
            
def run():
    game_running = True
    while game_running:
        events()
        
        board.display()  # Concole board
        
        # Check if the red car has reached the exit
        if board.exit_check():
            print("You win! Red car reached the exit!")
            game_running = False



if __name__ == "__main__":
    run()