import pygame
from setting import *


class Block:
    
    def __init__(self, position=[0, 0], orientation='h', colour = White, size=2, block_id=2):
        """
        # corresponding to the below variables: 
        # Position in the array,
        # How long gonna be the block is, 2?3?,
        # Orientation in the array, horizontal or vertical,
        # Color in the block,
        # Dragging check,
        # Unique integer ID for the block
        """
        self.position = position
        self.size = size
        self.orientation = orientation
        self.colour = colour
        self.dragging = False
        self.id = block_id
        
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
                    board.board[self.position[1]][self.position[0] + i] = 0
            elif self.orientation == 'v':
                for i in range(self.size):
                    board.board[self.position[1] + i][self.position[0]] = 0

            # Ensure the block stays within the bounds of the board
            valid_move = False

            if self.orientation == 'h':
                # Horizontal blocks can only move horizontally
                if 0 <= grid_x <= len(board.board[0]) - self.size and grid_y == self.position[1]:
                    if self.is_move_valid(grid_x, grid_y, board):
                        valid_move = True
            elif self.orientation == 'v':
                # Vertical blocks can only move vertically
                if self.position[0] == grid_x and 0 <= grid_y <= len(board.board) - self.size:
                    if self.is_move_valid(grid_x, grid_y, board):
                        valid_move = True

            # Allow the red block to move to [6][2]
            # For the exit function to work
            if self.colour == Red and self.orientation == 'h' and grid_y == 2 and grid_x == 5:
                valid_move = True

            # Additional validation to check for overlapping blocks
            if valid_move and self.is_move_valid(grid_x, grid_y, board):

                self.position = [grid_x, grid_y]
                # Place the block in the new position
                for i in range(self.size):

                    if self.colour == Red:
                        if self.orientation == 'h':
                            board.board[grid_y][grid_x + i] = 1
                        elif self.orientation == 'v':
                            board.board[grid_y + i][grid_x] = 1
                    elif self.colour == Yellow:
                        if self.orientation == 'h':
                            board.board[grid_y][grid_x + i] = self.id
                        elif self.orientation == 'v':
                            board.board[grid_y + i][grid_x] = self.id
            else:
                # If invalid, reset the position in the array to its original
                self.place_block(board)

    def is_move_valid(self, grid_x, grid_y, board):
        # Check for valid move within board limits and collision detection on
        if self.orientation == 'h':
                # Moving horizontally, ensure no blocks are in the way along the entire path
                if grid_x < self.position[0]: 
                    for i in range(grid_x, self.position[0]):
                        # To check if theres any blocks in the way
                        if board.board[grid_y][i] != 0: 
                            return False
                else:
                    # Moving right
                    for i in range(self.position[0] + self.size, grid_x + self.size):
                        if i <= 5:
                            if board.board[grid_y][i] != 0:
                                return False
                        
        elif self.orientation == 'v':
            # Moving vertically, ensure no blocks are in the way along the entire path
            if grid_y < self.position[1]: 
                for i in range(grid_y, self.position[1]):
                    if board.board[i][grid_x] != 0:
                        return False
            else:
                for i in range(self.position[1] + self.size, grid_y + self.size):
                    if i <= 5:
                        if board.board[i][grid_x] != 0:
                            return False
        return True

    def place_block(self, board):
        # Reset the position in the array to its original
        for i in range(self.size):
            if self.colour == Red:
                if self.orientation == 'h':
                    board.board[self.position[1]][self.position[0] + i] = 1
                elif self.orientation == 'v':
                    board.board[self.position[1] + i][self.position[0]] = 1
            elif self.colour == Yellow:
                if self.orientation == 'h':
                    board.board[self.position[1]][self.position[0] + i] = self.id
                elif self.orientation == 'v':
                    board.board[self.position[1] + i][self.position[0]] = self.id

    def render(self, screen):
        # Render the block based on its current position and size
        if self.orientation == 'h':
            block_rect = pygame.Rect(
                self.position[0] * tile_size,
                self.position[1] * tile_size,
                self.size * tile_size,
                tile_size
            )
        elif self.orientation == 'v':
            block_rect = pygame.Rect(
                self.position[0] * tile_size,
                self.position[1] * tile_size,
                tile_size,
                self.size * tile_size
            )
        pygame.draw.rect(screen, Black, block_rect, 5)
        # Black margin outline
        pygame.draw.rect(screen, self.colour, block_rect.inflate(-10, -10))
