import time


def mazecreate_1():
    maze_1_map = []
    maze_1_map.append(["#", "#", "#", "#", "O", "#"])
    maze_1_map.append(["X", " ", " ", "#", " ", "#"])
    maze_1_map.append(["#", " ", "#", "#", " ", "#"])
    maze_1_map.append(["#", " ", " ", " ", " ", "#"])
    maze_1_map.append(["#", "#", "#", "#", "#", "#"])

    return maze_1_map


def mazecreate_2():
    maze_2_map = []
    maze_2_map.append(["#", "X", "#", "#", "#", "#", "#", "#"])
    maze_2_map.append(["#", " ", " ", "#", " ", " ", " ", "#"])
    maze_2_map.append(["#", " ", "#", "#", " ", "#", "#", "#"])
    maze_2_map.append(["#", " ", "#", " ", " ", " ", " ", "O"])
    maze_2_map.append(["#", " ", "#", "#", "#", " ", "#", "#"])
    maze_2_map.append(["#", " ", " ", " ", " ", " ", " ", "#"])
    maze_2_map.append(["#", " ", "#", " ", "#", " ", "#", "#"])
    maze_2_map.append(["#", "#", "#", "#", "#", "#", "#", "#"])

    return maze_2_map


def mazecreate_3():
    maze_3_map = []
    maze_3_map.append(["#", "#", "#", "#", "#", "#", "#", "#"])
    maze_3_map.append(["#", "O", " ", " ", "#", " ", " ", "#"])
    maze_3_map.append(["#", "#", "#", " ", "#", " ", " ", "#"])
    maze_3_map.append(["#", " ", "#", " ", "#", " ", " ", "#"])
    maze_3_map.append(["#", " ", "#", " ", "#", "#", " ", "#"])
    maze_3_map.append(["#", " ", " ", " ", " ", " ", " ", "#"])
    maze_3_map.append(["#", " ", "#", " ", "#", " ", "X", "#"])
    maze_3_map.append(["#", "#", "#", "#", "#", "#", "#", "#"])

    return maze_3_map

# Maze printing definition


def print_maze(maze):
    for row in maze:
        for cell in row:
            print(cell, end=" ")

        print()


# Printing out the maze
maze_1 = mazecreate_1()
maze_2 = mazecreate_2()
maze_3 = mazecreate_3()
print_maze(maze_1)
print_maze(maze_2)
print_maze(maze_3)

# ===================================================================

# Finding the indices of 'X' and 'O'


def find_index(maze, char):
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            if cell == char:
                return i, j
    return None

# ===================================================================


def dfs(start, goal, maze):
    # Stack data structure for DFS
    stack = [start]
    # Track visited cells
    visited = set()
    # Track the path
    path = {}

    while stack:
        # popping current cell
        current = stack.pop()
        if current == goal:
            # Exit if goal
            break

        # Mark down the visited cell
        visited.add(current)

        # Routes: Down, Up, Right, Left
        for direction in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            neighbor = (current[0] + direction[0], current[1] + direction[1])

            # Valid move check
            if (0 <= neighbor[0] < len(maze) and
                0 <= neighbor[1] < len(maze[0]) and
                maze[neighbor[0]][neighbor[1]] != '#' and
                    neighbor not in visited):

                stack.append(neighbor)
                visited.add(neighbor)
                path[neighbor] = current

                # Mark the current cell on the maze to show it’s visited
                if maze[neighbor[0]][neighbor[1]] == " ":
                    maze[neighbor[0]][neighbor[1]] = "."
                
                # Can be removed cause visualization only
                print_maze(maze)
                print("\n")
                time.sleep(0.5)

    maze[start[0]][start[1]] = "O"
    maze[goal[0]][goal[1]] = "X"


maze_1 = mazecreate_1()
start_maze_index = find_index(maze_1, 'O')
end_maze_index = find_index(maze_1, 'X')
dfs(start_maze_index, end_maze_index, maze_1)
print("Maze 1 with path:")
print_maze(maze_1)


maze_2 = mazecreate_2()
start_maze_index = find_index(maze_2, 'O')
end_maze_index = find_index(maze_2, 'X')
dfs(start_maze_index, end_maze_index, maze_2)
print("\nMaze 2 with path:")
print_maze(maze_2)


maze_3 = mazecreate_3()
start_maze_index = find_index(maze_3, 'O')
end_maze_index = find_index(maze_3, 'X')
dfs(start_maze_index, end_maze_index, maze_3)
print("\nMaze 3 with path:")
print_maze(maze_3)
