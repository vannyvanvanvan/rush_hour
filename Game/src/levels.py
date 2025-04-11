from src.block import Block
from src.setting import *

def get_levels():
    levels = []

    # Level 1
    level_1 = {
        "blocks": [
            Block(position=[1, 2], orientation='h', colour=Red, size=2, block_id=1),
        ]
        
    }
    levels.append(level_1)

    # Level 2
    level_2 = {
        "blocks": [
            Block(position=[2, 2], orientation='h', colour=Red, size=2, block_id=1),
            Block(position=[3, 3], orientation='v', colour=Yellow, size=2, block_id=2),
            Block(position=[4, 4], orientation='h', colour=Yellow, size=2, block_id=3),
            Block(position=[5, 0], orientation='v', colour=Yellow, size=3, block_id=4)
        ]
    }
    levels.append(level_2)
    
    # Level 3
    level_3 = {
        "blocks": [
            Block(position=[0, 0], orientation='h', colour=Yellow, size=3, block_id=1),
            Block(position=[1, 1], orientation='v', colour=Yellow, size=2, block_id=2),
            Block(position=[2, 2], orientation='h', colour=Red, size=2, block_id=3),
            Block(position=[2, 3], orientation='v', colour=Yellow, size=2, block_id=4),
            
            Block(position=[3, 4], orientation='h', colour=Yellow, size=2, block_id=5),
            Block(position=[4, 0], orientation='v', colour=Yellow, size=2, block_id=6),
            Block(position=[4, 2], orientation='v', colour=Yellow, size=2, block_id=7),
        ]
    }
    levels.append(level_3)
    
    # Level 4
    level_4 = {
        "blocks": [
            Block(position=[1, 2], orientation='h', colour=Red, size=2, block_id=1),
            Block(position=[0, 3], orientation='h', colour=Yellow, size=2, block_id=2),
            Block(position=[1, 4], orientation='v', colour=Yellow, size=2, block_id=3),
            Block(position=[2, 3], orientation='v', colour=Yellow, size=2, block_id=4),
            Block(position=[2, 5], orientation='h', colour=Yellow, size=2, block_id=5),
            Block(position=[3, 1], orientation='v', colour=Yellow, size=3, block_id=6),
            Block(position=[5, 1], orientation='v', colour=Yellow, size=3, block_id=7)

        ]
        
    }
    levels.append(level_4)
    
    # Level 5
    level_5 = {
        "blocks": [
            Block(position=[0, 2], orientation='h', colour=Red, size=2, block_id=1),
            Block(position=[0, 3], orientation='v', colour=Yellow, size=2, block_id=2),
            Block(position=[1, 3], orientation='h', colour=Yellow, size=3, block_id=3),
            Block(position=[1, 4], orientation='h', colour=Yellow, size=2, block_id=4),
            Block(position=[3, 4], orientation='v', colour=Yellow, size=2, block_id=5),
            Block(position=[2, 0], orientation='v', colour=Yellow, size=3, block_id=6),
            Block(position=[3, 0], orientation='h', colour=Yellow, size=2, block_id=7),
            Block(position=[3, 1], orientation='v', colour=Yellow, size=2, block_id=8),
            Block(position=[5, 0], orientation='v', colour=Yellow, size=3, block_id=9)
        ]
        
    }
    levels.append(level_5)

    # Level 6
    level_6 = {
        "blocks": [
            Block(position=[0, 2], orientation='h', colour=Red, size=2, block_id=1),
            Block(position=[0, 3], orientation='h', colour=Yellow, size=2, block_id=2),
            Block(position=[1, 4], orientation='v', colour=Yellow, size=2, block_id=3),
            Block(position=[2, 0], orientation='v', colour=Yellow, size=2, block_id=4),
            Block(position=[2, 2], orientation='v', colour=Yellow, size=2, block_id=5),
            Block(position=[2, 4], orientation='h', colour=Yellow, size=2, block_id=6),
            Block(position=[3, 0], orientation='h', colour=Yellow, size=3, block_id=7),
            Block(position=[3, 1], orientation='v', colour=Yellow, size=2, block_id=8),
            Block(position=[3, 3], orientation='h', colour=Yellow, size=2, block_id=9),
            Block(position=[5, 2], orientation='v', colour=Yellow, size=3, block_id=10)
            
        ]
        
    }
    levels.append(level_6)
    
    
    # Level 7
    level_7 = {
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
            Block(position=[5, 2], orientation='v', colour=Yellow, size=3, block_id=12)
        ]
    }
    levels.append(level_7)
    
    # Level 8
    level_8 = {
        "blocks": [
            Block(position=[0, 2], orientation='h', colour=Red, size=2, block_id=1),
            Block(position=[0, 3], orientation='h', colour=Yellow, size=2, block_id=2),
            Block(position=[0, 4], orientation='v', colour=Yellow, size=2, block_id=3),
            Block(position=[1, 1], orientation='h', colour=Yellow, size=2, block_id=4),
            Block(position=[1, 4], orientation='h', colour=Yellow, size=3, block_id=5),
            Block(position=[2, 2], orientation='v', colour=Yellow, size=2, block_id=6),
            Block(position=[2, 5], orientation='h', colour=Yellow, size=2, block_id=7),
            Block(position=[3, 0], orientation='v', colour=Yellow, size=2, block_id=8),
            Block(position=[3, 2], orientation='v', colour=Yellow, size=2, block_id=9),
            Block(position=[4, 0], orientation='h', colour=Yellow, size=2, block_id=10),
            Block(position=[4, 1], orientation='v', colour=Yellow, size=2, block_id=11),
            Block(position=[4, 3], orientation='h', colour=Yellow, size=2, block_id=12),
            Block(position=[5, 4], orientation='v', colour=Yellow, size=2, block_id=13)
            
        ]
        
    }
    levels.append(level_8)
    
    # Level 9
    level_9 = {
        "blocks": [
            Block(position=[0, 2], orientation='h', colour=Red, size=2, block_id=1),
            Block(position=[0, 3], orientation='h', colour=Yellow, size=2, block_id=2),
            Block(position=[0, 4], orientation='v', colour=Yellow, size=2, block_id=3),
            Block(position=[1, 1], orientation='h', colour=Yellow, size=2, block_id=4),
            Block(position=[1, 4], orientation='h', colour=Yellow, size=3, block_id=5),
            Block(position=[2, 2], orientation='v', colour=Yellow, size=2, block_id=6),
            Block(position=[1, 5], orientation='h', colour=Yellow, size=3, block_id=7),
            Block(position=[3, 0], orientation='v', colour=Yellow, size=2, block_id=8),
            Block(position=[3, 2], orientation='v', colour=Yellow, size=2, block_id=9),
            Block(position=[4, 0], orientation='h', colour=Yellow, size=2, block_id=10),
            Block(position=[4, 1], orientation='v', colour=Yellow, size=2, block_id=11),
            Block(position=[4, 3], orientation='h', colour=Yellow, size=2, block_id=12),
            Block(position=[5, 4], orientation='v', colour=Yellow, size=2, block_id=13)
            
        ]
        
    }
    levels.append(level_9)
    
    # Level 10
    level_10 = {
        "blocks": [
            Block(position=[0, 0], orientation='h', colour=Yellow, size=2, block_id=1),
            Block(position=[0, 1], orientation='h', colour=Yellow, size=2, block_id=2),
            Block(position=[0, 2], orientation='v', colour=Yellow, size=2, block_id=3),
            Block(position=[1, 2], orientation='v', colour=Yellow, size=2, block_id=4),
            Block(position=[0, 4], orientation='v', colour=Yellow, size=2, block_id=5),
            Block(position=[2, 0], orientation='h', colour=Yellow, size=3, block_id=6),
            Block(position=[2, 1], orientation='h', colour=Yellow, size=3, block_id=7),
            Block(position=[2, 2], orientation='h', colour=Red, size=2, block_id=8),
            Block(position=[2, 3], orientation='v', colour=Yellow, size=3, block_id=9),
            Block(position=[3, 3], orientation='v', colour=Yellow, size=3, block_id=10),
            Block(position=[4, 2], orientation='v', colour=Yellow, size=3, block_id=11),
            Block(position=[4, 5], orientation='h', colour=Yellow, size=2, block_id=12),
            Block(position=[5, 0], orientation='v', colour=Yellow, size=2, block_id=13),
            Block(position=[5, 2], orientation='v', colour=Yellow, size=2, block_id=14)
            
            
        ]
        
    }
    levels.append(level_10)
    
    # Level 11
    level_11 = {
        "blocks": [
            Block(position=[0, 2], orientation='h', colour=Yellow, size=2, block_id=1),
            Block(position=[0, 1], orientation='v', colour=Yellow, size=2, block_id=2),
            Block(position=[0, 3], orientation='v', colour=Yellow, size=3, block_id=3),
            Block(position=[1, 2], orientation='v', colour=Yellow, size=3, block_id=4),
            Block(position=[1, 5], orientation='h', colour=Yellow, size=2, block_id=5),
            Block(position=[2, 0], orientation='v', colour=Yellow, size=2, block_id=6),
            Block(position=[2, 2], orientation='h', colour=Red, size=2, block_id=7),
            Block(position=[2, 3], orientation='h', colour=Yellow, size=2, block_id=8),
            Block(position=[2, 4], orientation='h', colour=Yellow, size=3, block_id=9),
            Block(position=[3, 1], orientation='h', colour=Yellow, size=3, block_id=10),
            Block(position=[3, 5], orientation='h', colour=Yellow, size=2, block_id=11),
            Block(position=[4, 0], orientation='h', colour=Yellow, size=2, block_id=12),
            Block(position=[4, 2], orientation='v', colour=Yellow, size=2, block_id=13),
            Block(position=[5, 2], orientation='v', colour=Yellow, size=2, block_id=14),
            Block(position=[5, 4], orientation='v', colour=Yellow, size=2, block_id=15)
            
            
            
            
        ]
        
    }
    levels.append(level_11)
    
    

    return levels

