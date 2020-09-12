import heapq, random, math

# Problem: Given an NxN Matrix representing a maze (0's represent blocked path, 1's open path) find a solution if it exists
#   - Simple version where source and destination are (0, 0) and (n-1, n-1) respectively

# Approach 1: Basic Backtracking algorithm

# Approach 2: Backtracking with a heuristic

# Possible heuristics: 
#   - Euclidean Distance to destination (Doesn't work very well)
#   - Choose the next position with the 



def generate_random_maze(size):
    
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
    
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] is -1:
                maze[i][j] = 0


def is_valid(pos, move):
    return ((pos[0] + move[0]) >= 0 and (pos[1] + move[1]) >= 0 and 
        (pos[0] + move[0]) < MAZE_SIZE and (pos[1] + move[1]) < MAZE_SIZE)

def move(pos, move):
    return (pos[0] + move[0], pos[1] + move[1])

def find_path(maze, position):

    global iteration_counter
    iteration_counter += 1
    if position == DESTINATION:
        return True

    for m in rat_moves:
        if is_valid(position, m):
            new_position = move(position, m)
            if maze[new_position[0]][new_position[1]] == 0:
                maze[new_position[0]][new_position[1]] = -1
                path_found = find_path(maze, new_position)
                if path_found:
                    return path_found
                maze[new_position[0]][new_position[1]] = 0

    return False

def get_distance_to_destination(position, destination):
    return math.sqrt((destination[0] - position[0])^2 + (destination[1] - position[1])^2)

def find_path_heuristic(maze, position):
    
    global iteration_counter_1
    iteration_counter_1 += 1
    if position == DESTINATION:
        return True

    distance_pq = []
    for m in rat_moves:
        if is_valid(position, m):
            new_position = move(position, m)
            if maze[new_position[0]][new_position[1]] == 0:
                dist = get_distance_to_destination(position, DESTINATION)
                heapq.heappush(distance_pq, (dist, new_position))

    while distance_pq:
        new_position = heapq.heappop(distance_pq)[1]
        maze[new_position[0]][new_position[1]] = -1
        path_found = find_path_heuristic(maze, new_position)
        if path_found:
            return True
        maze[new_position[0]][new_position[1]] = 0

    return False

def print_formatted_maze(maze):

    for row in maze:
        for val in row:
            space = " "
            if val is -1:
                space = ""
            print(f"{space}{val}", end="")
        print("")

if __name__ == "__main__":

    iteration_counter = 0
    rat_moves = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    MAZE_SIZE = 10
    SOURCE = (0, 0)
    DESTINATION = (MAZE_SIZE - 1, MAZE_SIZE - 1)
    
    maze = generate_random_maze(MAZE_SIZE)
    print_formatted_maze(maze)
    print("")
    maze[SOURCE[0]][SOURCE[1]] = -1
    result = find_path(maze, SOURCE)
    print(f"Number of moves tried: {iteration_counter}")
    if result:
        print_formatted_maze(maze)
    else:
        print("No solution for the maze.")

    clear_maze(maze)
    print("")
    iteration_counter_1 = 0
    maze[SOURCE[0]][SOURCE[1]] = -1
    result = find_path_heuristic(maze, SOURCE)
    print(f"Number of moves tried: {iteration_counter_1}")
    if result:
        print_formatted_maze(maze)
    else:
        print("No solution for the maze.")