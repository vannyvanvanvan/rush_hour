import pygame
from setting import *

class Block:
    def __init__(self, position=[0, 0], orientation='h', colour=(255, 255, 255), size=2):
        self.position = position                        # Position in the array
        self.size = size                                # How long gonna be the block is, 2?3?
        self.orientation = orientation                  # Orientation in the array, horizontal or vertical
        self.colour = colour                            # Color in the block
        self.dragging = False                           # Dragging check

    def start_drag(self, mouse_pos):
        # Check if the mouse is over the block to start dragging
        grid_x = mouse_pos[0] // tile_size
        grid_y = mouse_pos[1] // tile_size
        if self.position[0] <= grid_x < self.position[0] + self.size and self.position[1] == grid_y:
            self.dragging = True

    def stop_drag(self):
        self.dragging = False

    # Function is for positioning and legal movement within the board
    def update_position(self, mouse_pos, board):
        if self.dragging:
            # Calculate grid position based on mouse position
            grid_x = mouse_pos[0] // tile_size
            grid_y = mouse_pos[1] // tile_size
            
            # Clear previous position from the board
            if self.orientation == 'h':
                for i in range(self.size):
                    board[self.position[1]][self.position[0] + i] = "X"
            elif self.orientation == 'v':
                for i in range(self.size):
                    board[self.position[1] + i][self.position[0]] = "X"

            # Ensure the block stays within the bounds of the board
            valid_move = False

            if self.orientation == 'h':
                # Horizontal blocks can only move horizontally
                if 0 <= grid_x <= len(board[0]) - self.size and grid_y == self.position[1]:
                    valid_move = True
            elif self.orientation == 'v':
                # Vertical blocks can only move vertically
                if self.position[0] == grid_x and 0 <= grid_y <= len(board) - self.size:
                    valid_move = True
                    
            
            # !Allow the red block to move to [6][2]!
            if self.colour == Red and self.orientation == 'h' and grid_y == 2 and grid_x == 5:
                valid_move = True

            # Additional validation to check for overlapping blocks
            if valid_move and self.is_move_valid(grid_x, grid_y, board):
                
                self.position = [grid_x, grid_y]
                # Place the block in the new position
                for i in range(self.size):
                    if self.colour == Red:
                        if self.orientation == 'h':
                            board[grid_y][grid_x + i] = "R"
                        elif self.orientation == 'v':
                            board[grid_y + i][grid_x] = "R"
                    elif self.colour == Yellow:
                        if self.orientation == 'h':
                            board[grid_y][grid_x + i] = "Y"
                        elif self.orientation == 'v':
                            board[grid_y + i][grid_x] = "Y"
            else:
                # If invalid, reset the position in the array to its original
                self.place_block(board)

    def is_move_valid(self, grid_x, grid_y, board):
        # Check for valid move within board limits and collision detection on
        if self.orientation == 'h':
            for i in range(self.size):
                if board[grid_y][grid_x + i] != "X":
                    return False
        elif self.orientation == 'v':
            for i in range(self.size):
                if board[grid_y + i][grid_x] != "X":
                    return False
        return True

    def place_block(self, board):
        # Reset the position in the array to its original
        for i in range(self.size):
            if self.colour == Red:
                if self.orientation == 'h':
                    board[self.position[1]][self.position[0] + i] = "R"
                elif self.orientation == 'v':
                    board[self.position[1] + i][self.position[0]] = "R"
            elif self.colour == Yellow:
                if self.orientation == 'h':
                    board[self.position[1]][self.position[0] + i] = "Y"
                elif self.orientation == 'v':
                    board[self.position[1] + i][self.position[0]] = "Y"
                        
    def render(self, screen):
        # Render the block based on its current position and size
        for i in range(self.size):
            if self.orientation == 'h':
                pygame.draw.rect(screen, self.colour, pygame.Rect((self.position[0] + i) * tile_size, self.position[1] * tile_size, tile_size, tile_size))
            elif self.orientation == 'v':
                pygame.draw.rect(screen, self.colour, pygame.Rect(self.position[0] * tile_size, (self.position[1] + i) * tile_size, tile_size, tile_size))