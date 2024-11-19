import time
import heapq


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


def a_star(start, goal, maze):
    def manhattan_distance(x, y, goal):
        # Calculate Manhattan distance
        return abs(x - goal[0]) + abs(y - goal[1])
    
    # Priority queue (min-heap) stores tuples of (cost, (x, y))
    pq = []
    heapq.heappush(pq, (0 + manhattan_distance(start[0], start[1], goal), 0, start))
    g_costs = {start: 0}
    f_costs = {start: manhattan_distance(start[0], start[1], goal)}
    visited = set()
    
    # Routes: Down, Up, Right, Left
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    while pq:
        f_cost, g_cost, (x, y) = heapq.heappop(pq)

        if (x, y) == goal:
            break
        
        if (x, y) in visited:
            continue
        
        visited.add((x, y))

        for dx, dy in directions:
            # Neighboring position
            nx, ny = x + dx, y + dy

            if (0 <= nx < len(maze)
                and 0 <= ny < len(maze[0])
                    and maze[nx][ny] != '#'
                        and (nx, ny) not in visited):
                new_g_cost = g_cost + 1
                new_f_cost = new_g_cost + manhattan_distance(nx, ny, goal)

                if (nx, ny) not in g_costs or new_g_cost < g_costs[(nx, ny)]:
                    g_costs[(nx, ny)] = new_g_cost
                    f_costs[(nx, ny)] = new_f_cost
                    heapq.heappush(pq, (new_f_cost, new_g_cost, (nx, ny)))
                
                if maze[nx][ny] == " ":
                    maze[nx][ny] = "."
                
                # Can be removed cause visualization only
                print_maze(maze)
                print("\n")
                time.sleep(0.5)

    maze[start[0]][start[1]] = "O"
    maze[goal[0]][goal[1]] = "X"


maze_1 = mazecreate_1()
start_maze_index = find_index(maze_1, 'O')
end_maze_index = find_index(maze_1, 'X')
a_star(start_maze_index, end_maze_index, maze_1)
print("Maze 1 with path:")
print_maze(maze_1)

maze_2 = mazecreate_2()
start_maze_index = find_index(maze_2, 'O')
end_maze_index = find_index(maze_2, 'X')
a_star(start_maze_index, end_maze_index, maze_2)
print("\nMaze 2 with path:")
print_maze(maze_2)

maze_3 = mazecreate_3()
start_maze_index = find_index(maze_3, 'O')
end_maze_index = find_index(maze_3, 'X')
a_star(start_maze_index, end_maze_index, maze_3)
print("\nMaze 3 with path:")
print_maze(maze_3)
