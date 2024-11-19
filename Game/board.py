import pygame

from setting import *


class Board:
    def __init__(self):
        
        self.game_state = "stage_0"
        
        # Board array 
        self.board = [
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],  # Exit is here
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
        ]
        
                
    def place_block(self, block):
        # Update the board array with the block's position and size
        for i in range(block.size):
            if block.orientation == 'h':
                self.board[block.position[1]][block.position[0] + i] = 1 if block.colour == Red else block.id
            else:
                self.board[block.position[1] + i][block.position[0]] = 1 if block.colour == Red else block.id
                
    def display(self):
        # Prints the board to the console
        for row in self.board:
            str_row=""
            for num in row:
                str_row+="%d "%num if num>=10 else " %d "%num
            print(str_row)
        print("============")
        
    
    def exit_check(self):
        # Exit check if the red block is in the array[5][3]
        exit_x = 6
        exit_y = 2
        return self.board[exit_y][exit_x] == 1
    
    def render(self, screen, tile_size):
        for y, row in enumerate(self.board):
            for x, cell in enumerate(row):
                # Set the color for the tile
                if cell == 0:
                    color = White
                elif cell == 1:
                    color = Red
                elif cell > 1:
                    color = Yellow 
                
                # Draw the rectangle for each tile
                pygame.draw.rect(screen, color, pygame.Rect(x * tile_size, y * tile_size, tile_size, tile_size))
                
                # Draw the grid lines
                pygame.draw.rect(screen, Black, pygame.Rect(x * tile_size, y * tile_size, tile_size, tile_size), 2)