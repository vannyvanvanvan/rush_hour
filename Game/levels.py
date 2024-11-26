from block import Block
from setting import *


def get_levels():
    levels = []

    # Level 1
    level_1 = {
        "blocks": [
            Block(position=[0, 2], orientation='h', colour=Red, size=2, block_id=1),
            Block(position=[0, 3], orientation='h', colour=Yellow, size=2, block_id=2),
            Block(position=[0, 4], orientation='v', colour=Yellow, size=2, block_id=3),
            Block(position=[1, 4], orientation='v', colour=Yellow, size=2, block_id=4),
            Block(position=[2, 4], orientation='h', colour=Yellow, size=2, block_id=5),
            Block(position=[2, 5], orientation='h', colour=Yellow, size=2, block_id=6),
            Block(position=[2, 2], orientation='v', colour=Yellow, size=2, block_id=7),
            Block(position=[2, 0], orientation='v', colour=Yellow, size=2, block_id=8),
            Block(position=[3, 0], orientation='h', colour=Yellow, size=3, block_id=9),
            Block(position=[3, 1], orientation='v', colour=Yellow, size=2, block_id=10),
            Block(position=[3, 3], orientation='h', colour=Yellow, size=2, block_id=11),
            Block(position=[5, 2], orientation='v', colour=Yellow, size=3, block_id=12),
        ]
        
    }
    levels.append(level_1)

    # Level 2
    level_2 = {
        "blocks": [
            Block(position=[1, 2], orientation='h', colour=Red, size=2, block_id=1),
            Block(position=[4, 2], orientation='v', colour=Yellow, size=2, block_id=2)
        ]
    }
    levels.append(level_2)

    return levels