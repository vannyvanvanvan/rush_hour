from collections import deque
from copy import deepcopy
import heapq
from setting import *

# Breadth-First Search
def bfs(board, blocks):
    # Create deep copies of the board and blocks
    board = deepcopy(board)
    blocks = deepcopy(blocks)
    
    # Visited states
    visited = set()
    # [Current list of moves, current board state, and current block positions].
    queue = deque([[[], board, blocks]])
    
    while queue:
        moves, board, blocks = queue.popleft()
        
        # Check if the exit is reached
        if board.exit_check():
            return moves
        
        for i, block in enumerate(blocks):
            for direction in [1, -1]:
                # Calculate the neighboring position based on the block's orientation
                if block.orientation == "h":
                    neighbor = (block.position[0] + direction, block.position[1])
                elif block.orientation == "v":
                    neighbor = (block.position[0], block.position[1] + direction)
                # Skip invalid positions
                if neighbor[0] < 0 or neighbor[1] < 0:
                    continue
                # Check if the block can move to the neighboring position
                if block.is_move_valid(neighbor[0], neighbor[1], board):
                    # Create new copies of the board and blocks to check the move
                    new_board = deepcopy(board)
                    new_blocks = deepcopy(blocks)
                    new_blocks[i].dragging = True
                    new_blocks[i].update_position((neighbor[0] * tile_size, neighbor[1] * tile_size), new_board)
                    # Generate a hash of the new board state to check if it's been visited
                    if hash(str(new_board.board)) not in visited:
                        # If not visited, record the new move
                        new_move = deepcopy(moves)
                        new_move.append({
                            'block_id': block.id,
                            'orientation': block.orientation,
                            'size': block.size,
                            'original_position': block.position,
                            'current_position': new_blocks[i].position 
                        })
                        queue.append([new_move, new_board, new_blocks])
                        # Mark the new state as visited.
                        visited.add(hash(str(new_board.board)))
                        
def dfs(board, blocks):
    # Create deep copies of the board and blocks
    board = deepcopy(board)
    blocks = deepcopy(blocks)
    
    # Visited states
    visited = set()
    # [Current list of moves, current board state, and current block positions].
    queue = deque([[[], board, blocks]])
    
    while queue:
        moves, board, blocks = queue.pop()
        
        # Check if the exit is reached
        if board.exit_check():
            return moves
        
        for i, block in enumerate(blocks):
            for direction in [1, -1]:
                # Calculate the neighboring position based on the block's orientation
                if block.orientation == "h":
                    neighbor = (block.position[0] + direction, block.position[1])
                elif block.orientation == "v":
                    neighbor = (block.position[0], block.position[1] + direction)
                # Skip invalid positions
                if neighbor[0] < 0 or neighbor[1] < 0:
                    continue
                # Check if the block can move to the neighboring position
                if block.is_move_valid(neighbor[0], neighbor[1], board):
                    # Create new copies of the board and blocks to check the move
                    new_board = deepcopy(board)
                    new_blocks = deepcopy(blocks)
                    new_blocks[i].dragging = True
                    new_blocks[i].update_position((neighbor[0] * tile_size, neighbor[1] * tile_size), new_board)
                    # Generate a hash of the new board state to check if it's been visited
                    if hash(str(new_board.board)) not in visited:
                        # If not visited, record the new move
                        new_move = deepcopy(moves)
                        new_move.append({
                            'block_id': block.id,
                            'orientation': block.orientation,
                            'size': block.size,
                            'original_position': block.position,
                            'current_position': new_blocks[i].position 
                        })
                        queue.append([new_move, new_board, new_blocks])
                        # Mark the new state as visited.
                        visited.add(hash(str(new_board.board)))

def dijkstra(board, blocks):
    # Create deep copies of the board and blocks
    board = deepcopy(board)
    blocks = deepcopy(blocks)
    
    # Visited states
    visited = set()
    # [Current list of moves, current board state, and current block positions].
    queue = [(0, 0, [], board, blocks)]
    
    count = 0
    while queue:
        f, _, moves, board, blocks = heapq.heappop(queue)
        
        
        # Check if the exit is reached
        if board.exit_check():
            return moves
        
        for i, block in enumerate(blocks):
            for direction in [1, -1]:
                # Calculate the neighboring position based on the block's orientation
                if block.orientation == "h":
                    neighbor = (block.position[0] + direction, block.position[1])
                elif block.orientation == "v":
                    neighbor = (block.position[0], block.position[1] + direction)
                # Skip invalid positions
                if neighbor[0] < 0 or neighbor[1] < 0:
                    continue
                # Check if the block can move to the neighboring position
                if block.is_move_valid(neighbor[0], neighbor[1], board):
                    # Create new copies of the board and blocks to check the move
                    new_board = deepcopy(board)
                    new_blocks = deepcopy(blocks)
                    new_blocks[i].dragging = True
                    new_blocks[i].update_position((neighbor[0] * tile_size, neighbor[1] * tile_size), new_board)
                    # Generate a hash of the new board state to check if it's been visited
                    if hash(str(new_board.board)) not in visited:
                        # If not visited, record the new move
                        new_move = deepcopy(moves)
                        new_move.append({
                            'block_id': block.id,
                            'orientation': block.orientation,
                            'size': block.size,
                            'original_position': block.position,
                            'current_position': new_blocks[i].position 
                        })
                        count += 1
                        heapq.heappush(queue, (len(moves) + 1, count, new_move, new_board, new_blocks))
                        # Mark the new state as visited.
                        visited.add(hash(str(new_board.board)))
                        
def greedy(board, blocks):
    # Create deep copies of the board and blocks
    board = deepcopy(board)
    blocks = deepcopy(blocks)
    
    # Visited states
    visited = set()
    # [Current list of moves, current board state, and current block positions].
    queue = [(0, 0, [], board, blocks)]
    
    count = 0
    while queue:
        f, _, moves, board, blocks = heapq.heappop(queue)
        
        
        # Check if the exit is reached
        if board.exit_check():
            return moves
        
        for i, block in enumerate(blocks):
            for direction in [1, -1]:
                # Calculate the neighboring position based on the block's orientation
                if block.orientation == "h":
                    neighbor = (block.position[0] + direction, block.position[1])
                elif block.orientation == "v":
                    neighbor = (block.position[0], block.position[1] + direction)
                # Skip invalid positions
                if neighbor[0] < 0 or neighbor[1] < 0:
                    continue
                # Check if the block can move to the neighboring position
                if block.is_move_valid(neighbor[0], neighbor[1], board):
                    # Create new copies of the board and blocks to check the move
                    new_board = deepcopy(board)
                    new_blocks = deepcopy(blocks)
                    new_blocks[i].dragging = True
                    new_blocks[i].update_position((neighbor[0] * tile_size, neighbor[1] * tile_size), new_board)
                    # Generate a hash of the new board state to check if it's been visited
                    if hash(str(new_board.board)) not in visited:
                        # If not visited, record the new move
                        new_move = deepcopy(moves)
                        new_move.append({
                            'block_id': block.id,
                            'orientation': block.orientation,
                            'size': block.size,
                            'original_position': block.position,
                            'current_position': new_blocks[i].position 
                        })
                        count += 1
                        heapq.heappush(queue, (heuristic(new_board.board), count, new_move, new_board, new_blocks))
                        # Mark the new state as visited.
                        visited.add(hash(str(new_board.board)))
                        
def a_star(board, blocks):
    # Create deep copies of the board and blocks
    board = deepcopy(board)
    blocks = deepcopy(blocks)
    
    # Visited states
    visited = set()
    # [Current list of moves, current board state, and current block positions].
    queue = [(0, 0, [], board, blocks)]
    
    count = 0
    while queue:
        f, _, moves, board, blocks = heapq.heappop(queue)
        
        
        # Check if the exit is reached
        if board.exit_check():
            return moves
        
        for i, block in enumerate(blocks):
            for direction in [1, -1]:
                # Calculate the neighboring position based on the block's orientation
                if block.orientation == "h":
                    neighbor = (block.position[0] + direction, block.position[1])
                elif block.orientation == "v":
                    neighbor = (block.position[0], block.position[1] + direction)
                # Skip invalid positions
                if neighbor[0] < 0 or neighbor[1] < 0:
                    continue
                # Check if the block can move to the neighboring position
                if block.is_move_valid(neighbor[0], neighbor[1], board):
                    # Create new copies of the board and blocks to check the move
                    new_board = deepcopy(board)
                    new_blocks = deepcopy(blocks)
                    new_blocks[i].dragging = True
                    new_blocks[i].update_position((neighbor[0] * tile_size, neighbor[1] * tile_size), new_board)
                    # Generate a hash of the new board state to check if it's been visited
                    if hash(str(new_board.board)) not in visited:
                        # If not visited, record the new move
                        new_move = deepcopy(moves)
                        new_move.append({
                            'block_id': block.id,
                            'orientation': block.orientation,
                            'size': block.size,
                            'original_position': block.position,
                            'current_position': new_blocks[i].position 
                        })
                        count += 1
                        g = len(moves) + 1
                        h = heuristic(new_board.board)
                        f = g + h
                        heapq.heappush(queue, (f, count, new_move, new_board, new_blocks))
                        # Mark the new state as visited.
                        visited.add(hash(str(new_board.board)))

def heuristic(board):
    x = board[2].index(1)
    return abs(x - 5)