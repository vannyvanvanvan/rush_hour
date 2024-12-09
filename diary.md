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

# 18/10/2024
- Create a menu for the game, now the game have a function basic menu for the level selection, still work in progress.
- Dynamic levels selections, not hard coded.
- Changed event() function for a more logical and better code structure.

#
- Commented the debug codes, will remove dead code later on.
- I have sampled afew founds for the game.

# 21/10/2024
- Supervisor has suggested the material related to my work https://aima.cs.berkeley.edu/

# 25/10/2024
- Conducting experment on DFS, array Maze solving is used to let me understand more about it.
- It is used data structures known as **"Stack"**.
- A "stack" is a data structure used for the collection of the objects and based on the principle of **"LIFO"** known as **Last In First Out**.
- Now in a maze there are North, East, South, West.
- Marking the inital point as visited.
- Push current position to the stack.
- Pop() last element from the stack out.
- Check each neighboring cell in the North, East, South, and West directions.
- If a neighboring cell is open and unvisited, mark it as visited, push it onto the stack, and continue.
- If the neighboring cell is the maze exit, the solution is found.
#
- In this case what is DFS
- If a path is blocked or no unvisited neighbors, DFS automatically backtracks by popping the stack, "reversing" the path and trying alternative routes until exit is find.

# 29/10/2024
- Conducting experment on BFS, array Maze solving is used to let me understand more about it.
- It is used data structures known as **"Queue"**.
- A "Quene" is a data structure used for the collection of the objects and based on the principle of **"FIFO"** known as **First In First Out**.
- Now in a maze there are North, East, South, West.
- Marking the inital point as visited.
- Push current position to the quene.
- Pop(0) first element from the quene out.
- Check each neighboring cell in the North, East, South, and West directions.
- If a neighboring cell is open and unvisited, mark it as visited, enqueue it, and continue.
- If the neighboring cell is the maze exit, the shortest solution path is found, as BFS explores layer-by-layer.
#
- Path tracing in BFS
- Ensuring the shortest path by exploring all possible nodes at the current "layer" before moving on to nodes at the next layer.
- Therefore, the first time the exit is reached, it will be by the shortest path.
#
- I will be using `collections` library for the `deque` in Python instead of **pop(0)**, they work the same way but **pop(0)** is inefficient because it requires shifting all remaining elements one position to the left, resulting in an **O(n)** time complexity. `Deque`, on the other hand, is more optimized for appending and popping from both ends with **O(1)** time complexity.

# 1/11/2024
- Dijkstra’s algorithm
- It ensures that the shortest path is found
- Dijkstra’s algorithm requires each cells act like "node" in a graph and it searches for the shortest path with the lowest costs
- **Priority Queue** implemented as a min-heap, keeps track of cells with the lowest accumulated costs. This allows the algorithm to expand the lowest-cost paths first.


# 8/11/2024
- Greedy search 
- `Manhattan distance` as the heuristic

# 9/11/2024
- Changed the whole grid from string format into integer format. It was suggested by the supervisor.
- Edited how the output in the terminal is shown.

# 10/11/2024
- Created `Greedy search` in maze format
- Just uses the heuristic function: `f(n) = h(n)`
- `Manhattan distance` estimates how far a point is from the goal, by summing the absolute differences in `row` and `column` indices
- Once again, `priority queue` (min-heap) to `store` and `retrieve positions` based on their heuristic values
- Going to do A* next

# 11/11/2024
- Creating the `A* search`
- Using the heuristic function: `f(n) = g(n) + h(n)`

# 16/11/2024
- Created the `A* search`
- Estimateing the distance between the current position x, y and the goal
- Then sum of the absolute differences of row and column indices
- Priority Queue is to maintain a min-heap based on `f_cost = g_cost + heuristic`
- g_cost means cost to reach the current node
- f_cost means the estimated total cost

# 17/11/2024
- I tried to create a "path" that stores every infomation for the algorithms to work

```
File "d:\projects\Year_3_Program\Final year assignment\project\rush_hour_final_year_project\PROJECT\Game\block.py", line 97, in is_move_valid
    if board[grid_y][i] != 0: 
       ~~~~~^^^^^^^^
TypeError: 'Board' object is not subscriptable 
```

- This error ocurred when I am trying to make the def path, later found out that i forgot to index into the board object like a list
- but the board object is not behaving like a list or array, hence it is not directly subscriptable
- from board to board.board it fixed the problem
- Now it can access the array

# 20/11/2024
- After i tired to make the path for the algorithms to work properly, i figured that saving everything within a block can not save resources and making it overcomplicated, instead i will be changing how the path work in my next commit, which is saving the grid as the path

# 25/11/2024
```  File "d:\projects\Year_3_Program\Final year assignment\project\rush_hour_final_year_project\PROJECT\Game\block.py", line 101, in is_move_valid
    if board.board[grid_y][i] != 0:
       ~~~~~~~~~~~~~~~~~~~^^^
IndexError: list index out of range" 
```

- This bug is encountered when i tried to make the solver for BFS. After fixing is_move_valid() function, making it unable to go out bounds the problem is fixed.

- Finished working on the BFS algothm solver.

# 27/11/2024
- Added visualization for the BFS solver, for now whenever pressed the "a" button, it will excuse the function.

# 29/11/2024
- Moved all of the functions other than the main.py to .Game/src files.
- Added a blocky font for the game, the font is found on google font. "https://fonts.google.com/specimen/Press+Start+2P"
- Added a counter for the game.


# 30/11/2024
- Added a menu button for the game
- Fixing smelly code
- Fixed render errors

# 12/1/2024
- Fixed an error where when it changes back to stage 0 from stage 1 after loading the level, it didn't reset the board state so it bugged the whole rendering and gameplay. Now when the user switches back to stage 0 using the menu button, it will use a deepcopy of the levels so it won't change the level.py block coordinates, ALSO I added a reset block function to ensure that the state is fully reset.
#
- I used Ableton, which is a music software from Germany, and Audacity, a free and open-source audio editing and recording tool, to create the game audio.
- Fixed a smelly code
#
- Sound Effects Attribution:
- The Windows XP login and logoff sound effects are used in this project for educational purposes only. These sound effects are copyrighted by Microsoft Corporation and are not intended for commercial use.
- Credits: Windows XP Login and Logoff Sound Effects – Courtesy of Microsoft Corporation.
# 12/5/2024
- Fixed more smelly codes