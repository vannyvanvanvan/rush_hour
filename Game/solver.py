def path(block):
    moves = []
    
    # Only store original position once
    if not hasattr(block, 'original_position'):
        block.original_position = block.position
        
    current_position = block.position
    
    orientation = block.orientation
    block_id = block.id
    size = block.size
        
    moves.append({
        'block_id': block_id,
        'orientation': orientation,
        'size': size,
        'original_position': block.original_position,
        'current_position': current_position 
    })


    return moves
