import pygame

from setting import *


class Board:
    def __init__(self):
        
        self.game_state = "stage_1"
        
        self.board = [
            ["X", "X", "X", "X", "X", "X"],
             ["X", "X", "X", "X", "X", "X"],
              ["X", "X", "X", "X", "X", "X"], # Exit is here
               ["X", "X", "X", "X", "X", "X"],
                ["X", "X", "X", "X", "X", "X"],
                 ["X", "X", "X", "X", "X", "X"],
        ]
        
    def display(self):
        #Prints the board to the console 
        for row in self.board:
            print(" ".join(row))
        print("============")
        
    
    def exit_check(self):
        # Exit check if the red car is in the array[5][3]
        exit_x = 5  
        exit_y = 2
        return self.board[exit_y][exit_x] == "R"
    
    def render(self, screen, tile_size):

        for y, row in enumerate(self.board):
            for x, cell in enumerate(row):
                # Set the color for the tile
                if cell == "X":
                    color = White  # White for empty spaces
                elif cell == "R":
                    color = Red  # Red for the red car
                
                # Draw the rectangle for each tile
                pygame.draw.rect(screen, color, pygame.Rect(x * tile_size, y * tile_size, tile_size, tile_size))
                
                # Draw the grid lines
                pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(x * tile_size, y * tile_size, tile_size, tile_size), 2)