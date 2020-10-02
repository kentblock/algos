# Problem
# Solve travelling salesman problem with dynamic programming
import heapq


def precompute_distances(index):
    """
    Calculate distance from index to every tile in grid,
    use BFS
    """
    visited = [[False for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    
    inital_house_pos = house_positions[index]
    pq = [(0, inital_house_pos)]

    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if (i, j) != inital_house_pos:
                dist[i][j][index] = INFINITY
    while pq:
        dist_to_pos, current_position = heapq.heappop(pq)
        visited[current_position[0]][current_position[1]] = True
        dist[current_position[0]][current_position[1]][index] = dist_to_pos 
        for m in MOVES:
            new_position = move(current_position, m)
            if in_bounds(new_position) and not visited[new_position[0]][new_position[1]]: 
                if new_position not in blocked_positions:
                    heapq.heappush(pq, (dist_to_pos + 1, new_position))

def find_min_path(mask, index):
    """
    Find min path to each house and back using dynamic programming
    """
    if mask == all_mask:
        return dist[0][0][index]

    if dp[mask][index] != -1:
        return dp[mask][index]

    min_dist = INFINITY
    for new_index in unvisited_houses(mask):
        next_house_pos = house_positions[new_index]
        new_distance = find_min_path((mask | 2 ** new_index), new_index) + dist[next_house_pos[0]][next_house_pos[1]][index]
        if new_distance <= min_dist:
            min_dist = new_distance
    dp[mask][index] = min_dist
    return min_dist

def unvisited_houses(mask):
    """
    Helper returns unvisited houses from a mask
    """
    unvisited_houses = []
    for i in range(num_houses):
        if not mask & (2 ** i):
            unvisited_houses.append(i)
    return unvisited_houses

def move(pos, m):
    """
    Helper, returns new position after a move
    """
    return (pos[0] + m[0], pos[1] + m[1])

def in_bounds(pos):
    """
    Helper to check if a position is on the grid
    """    
    return pos[0] >= 0 and pos[0] < GRID_SIZE and pos[1] >=0 and pos[1] < GRID_SIZE

def safe_square(row, col):
    """
    Helper, return True iff a square is safe
    """
    return (row, col) in blocked_positions

if __name__ == "__main__":
    """
    TESTING
    """
    INFINITY = 1000
    GRID_SIZE = 7
    MOVES = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    house_positions = [(0, 0), (0, 5), (2, 1), (2, 5)]
    num_houses = len(house_positions)
    blocked_positions = [(1, 3), (2, 3)]
    all_mask = 2 ** num_houses - 1

    dist = [[[0 for _ in range(len(house_positions))] for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

    for index in range(len(house_positions)):
        precompute_distances(index)

    dp = [[-1 for _ in range(num_houses)] for _ in range(all_mask)]
    find_min_path(1, 0)
    print(f"The minimum distance is {dp[1][0]}") 
    