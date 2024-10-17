# Diary of my final years project

I will be documenting my own work in the following diary. I have also divided the thing that i did, in each commits to make it more clear.

## 4/10/2024
- Created the basic files for the rush_hour game.
- Created the base function of a windowed app. (Properly closing and opening the game)
- Added some setting for the app
- Added diary.md and I have created a introduction for my initial release.
- Added requirements.txt for the easy and simple download, wrote down the installation instructions for the future users.
#
- Implementation of the basic code for the pygame to run.
- Implementation of the basic code for the game to work in console first.
#
- Created the basic functions like grid rendering, and winning message for the game.
- Tested if the red car passed the exit and will it appear the winning message and update the game state act as a soft lock.
## 7/10/2024
- Created the function of the block.py, which contain drag function, their data 
position/orientation/colour/size and how they are being rendered

## 8/10/2024
- I figured that due to my function making the block can only move within 6x6 grid. And i needed my red block to move past the array [5][2] as right now when the red block moved to [5][2] it counts as victorious.
we doesnt want that to happened, so I recreated the array, making the red block accessible to [6][2] and fixed some code to expand the grid beyond 6x6, making it look more appealing.

- I thought of a way to make the game more interesting by adding multiple levels. It will also give the game a "Gameboy-like" appearance.

## 9/10/2024
- Added icon for the game which i created it in photoshop.
- Fixed some of the code's structures.


## 16/10/2024
- Added levels.py for the game. Now we can design and run different levels for the menu selection(WIP)
- In order to solve the confusion for each blocks, I added black margin outlines for each blocks. Changed the way how they being rendered out.
#
- Changed the way hows it going to be printed out in the board terminal
#
- I have found example levels on the internet from "https://www.reddit.com/r/puzzles/comments/17j3cpj/hardest_rush_hour_puzzle_for_every_possible/"
#
- Added array/coord checker for me to easier to manually adding the blocks for each levels
# 17/10/2024
- Yesterday, when i was trying different levels that i have built for the game, I figured there are some kind of collustions error that causing a block to "jump" through another block which was blocking the dragging one. 
- Example: From this dragging the red block("R R") to the array [2, 4].
``` 
=============
=X X Y Y Y Y=
=X X Y Y X X==
=X R R Y X X X
=Y Y Y Y X Y==
=Y Y Y Y Y Y=
=Y Y Y Y Y Y=
=============
```
- As you can see it "jumped" over the the yellow block.
``` 
=============
=X X Y Y Y Y=
=X X Y Y X X==
=X X X Y R R X
=Y Y Y Y X Y==
=Y Y Y Y Y Y=
=Y Y Y Y Y Y=
=============
```
- I was spending so much time in the wrong direction, at first i thought in the first check for the block to move around in their direction have the wrong logic 
```
if self.orientation == 'h':
                # Horizontal blocks can only move horizontally
                if 0 <= grid_x <= len(board[0]) - self.size and grid_y == self.position[1]:
                    if self.is_move_valid(grid_x, grid_y, board):
                        print("1")
                        valid_move = True
            elif self.orientation == 'v':
                # Vertical blocks can only move vertically
                if self.position[0] == grid_x and 0 <= grid_y <= len(board) - self.size:
                    if self.is_move_valid(grid_x, grid_y, board):
                        print("2")
                        valid_move = True
```

However, i later figure out the error is located in the 
```
    def is_move_valid(self, grid_x, grid_y, board):
        if self.orientation == 'h':
            for i in range(self.size):
                if board[grid_y][grid_x + i] != "X":
                    return False
        elif self.orientation == 'v':
            for i in range(self.size):
                if board[grid_y + i][grid_x] != "X":
                    return False
        return True
```
With the latest check logic the blocks can not be phasing through other blocks even there are spaces left for them to fit in.
