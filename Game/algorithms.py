from collections import deque
from copy import deepcopy
from setting import *


def bfs(board, blocks):
    board = deepcopy(board)
    blocks = deepcopy(blocks)
    visited = set()
    queue = deque([[[], board, blocks]])
    
    while queue:
        moves, board, blocks = queue.popleft()
        if board.exit_check():
            return moves
        
        for i, block in enumerate(blocks):
            for direction in [1, -1]:
                if block.orientation == "h":
                    neighbor = (block.position[0] + direction, block.position[1])
                elif block.orientation == "v":
                    neighbor = (block.position[0], block.position[1] + direction)
                if neighbor[0] < 0 or neighbor[1] < 0:
                    continue
                if block.is_move_valid(neighbor[0], neighbor[1], board):
                    new_board = deepcopy(board)
                    new_blocks = deepcopy(blocks)
                    new_blocks[i].dragging = True
                    new_blocks[i].update_position((neighbor[0] * tile_size, neighbor[1] * tile_size), new_board)
                    if hash(str(new_board.board)) not in visited:
                        new_move = deepcopy(moves)
                        new_move.append({
                            'block_id': block.id,
                            'orientation': block.orientation,
                            'size': block.size,
                            'original_position': block.position,
                            'current_position': new_blocks[i].position 
                        })
                        queue.append([new_move, new_board, new_blocks])
                        visited.add(hash(str(new_board.board)))
