import pygame

from setting import *


class Board:
    def __init__(self):
        
        self.game_state = "stage_1"
        
        # Board array 
        self.board = [
            ["X", "X", "X", "X", "X", "X"],
             ["X", "X", "X", "X", "X", "X"],
              ["X", "X", "X", "X", "X", "X", "X"], # Exit is here
               ["X", "X", "X", "X", "X", "X"],
                ["X", "X", "X", "X", "X", "X"],
                 ["X", "X", "X", "X", "X", "X"],
        ]
        
    def place_block(self, block):
        # Update the board array with the block's position and size
        for i in range(block.size):
            if block.orientation == 'h':
                self.board[block.position[1]][block.position[0] + i] = "R" if block.colour == Red else "Y"
            else:
                self.board[block.position[1] + i][block.position[0]] = "R" if block.colour == Red else "Y"
                
    def display(self):
        #Prints the board to the console 
        for row in self.board:
            print(" ".join(row))
        print("============")
        
    
    def exit_check(self):
        # Exit check if the red block is in the array[5][3]
        exit_x = 6
        exit_y = 2
        return self.board[exit_y][exit_x] == "R"
    
    def render(self, screen, tile_size):

        for y, row in enumerate(self.board):
            for x, cell in enumerate(row):
                # Set the color for the tile
                if cell == "X":
                    color = White  
                elif cell == "R":
                    color = Red  
                elif cell == "Y":
                    color = Yellow 
                
                # Draw the rectangle for each tile
                pygame.draw.rect(screen, color, pygame.Rect(x * tile_size, y * tile_size, tile_size, tile_size))
                
                # Draw the grid lines
                pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(x * tile_size, y * tile_size, tile_size, tile_size), 2)