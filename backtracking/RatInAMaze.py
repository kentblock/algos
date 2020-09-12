# Problem: Given an NxN Matrix representing a maze (0's represent blocked path, 1's open path) find a solution if it exists
#   - Simple version where source and destination are (0, 0) and (n-1, n-1) respectively
# BUG random method seems to try too many moves on some unsolvable mazes

import heapq, random, math

def generate_random_maze(size):
    """
    Generate a random maze, which may or may not be solvable
    """
    maze = []
    for _ in range(size):
        row = []
        for _ in range(size):
            rand_int = random.randint(0, 2)
            if rand_int is 2:
                rand_int = 0
            row.append(rand_int)
        maze.append(row)
    maze[0][0] = 0
    maze[size - 1][size - 1] = 0
    return maze

def clear_maze(maze):
    """
    Clear the rat's path from the maze
    """
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] is -1:
                maze[i][j] = 0

def is_valid(maze, pos, move):
    """
    return True if move is valid for pos on maze
    """
    return in_bounds(pos, move) and is_open(maze, move_rat(pos, move))

def is_open(maze, pos):
    """
    return True if position is open
    """
    return maze[pos[0]][pos[1]] == 0

def in_bounds(pos, move):
    """
    return True if move from pos is still in the maze
    """
    return ((pos[0] + move[0]) >= 0 and (pos[1] + move[1]) >= 0 and 
        (pos[0] + move[0]) < MAZE_SIZE and (pos[1] + move[1]) < MAZE_SIZE)

def move_rat(pos, move):
    """
    return new position after making move
    """
    return (pos[0] + move[0], pos[1] + move[1])

def find_path(maze, position):
    """
    Find path in maze recursively if there is one, tries moving down and right first always
    """
    global iteration_counter
    iteration_counter += 1
    if position == DESTINATION:
        return True

    for m in rat_moves:
        if is_valid(maze, position, m):
            new_position = move_rat(position, m)
            maze[new_position[0]][new_position[1]] = -1
            path_found = find_path(maze, new_position)
            if path_found:
                return path_found
            maze[new_position[0]][new_position[1]] = 0

    return False

def find_path_random(maze, position):
    """
    Find path in maze recursively if there is one, tries moves in random order
    """
    global iteration_counter
    iteration_counter += 1
    if position == DESTINATION:
        return True
    moves = [m for m in rat_moves]
    random.shuffle(moves)

    for m in moves:
        if is_valid(maze, position, m):
            new_position = move_rat(position, m)
            maze[new_position[0]][new_position[1]] = -1
            path_found = find_path_random(maze, new_position)
            if path_found:
                return path_found
            maze[new_position[0]][new_position[1]] = 0

    return False

def print_formatted_maze(maze):
    """
    Print the maze in fairly readable format
    """
    for row in maze:
        for val in row:
            space = " "
            if val is -1:
                space = ""
            print(f"{space}{val}", end="")
        print("")

def solve_maze(func, maze):
    """
    Given a func to solve maze, find a solution if there is one
    and output the result
    """
    print("")
    maze[SOURCE[0]][SOURCE[1]] = -1
    result = func(maze, SOURCE)
    print(f"Number of moves tried: {iteration_counter}")
    if result:
        print_formatted_maze(maze)
        print("")
    else:
        print("No solution for the maze.\n")

if __name__ == "__main__":
    """
    TESTING
    """
    iteration_counter = 0
    rat_moves = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    MAZE_SIZE = 10
    SOURCE = (0, 0)
    DESTINATION = (MAZE_SIZE - 1, MAZE_SIZE - 1)
    random_total = 0
    down_right_total = 0
    for _ in range(10):
        maze = generate_random_maze(MAZE_SIZE)
        print_formatted_maze(maze)
        solve_maze(find_path, maze)
        down_right_total += iteration_counter
        iteration_counter = 0
        clear_maze(maze)
        solve_maze(find_path_random, maze)
        random_total += iteration_counter
    
    comparison_ratio = (down_right_total - random_total) / down_right_total * 100
    print(f"""Always moving down and right first performed on average 
        {comparison_ratio}% better than picking a direction at random""")