# Problem
# Solve travelling salesman problem with dynamic programming
import heapq


def precompute_distances(index):
    """
    Calculate distance from index to every tile in grid,
    use BFS
    """
    # BUG not yet working 
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
            if not visited[new_position[0]][new_position[1]]: 
                if new_position not in blocked_positions:
                    heapq.heappush(pq, (dist_to_pos + 1, new_position))
    

def find_min_path(mask, index):
    pass #TODO
    """
    Find min path to each house and back using dynamic programming
    """
    if mask == all_mask:
        return dist[0][0][index]

def move(pos, m):
    """
    Helper, returns new position after a move
    """
    return (pos[0] + m[0], pos[1], m[1])
    
def safe_square(row, col):
    """
    Helper, return True iff a square is safe
    """
    return test_grid[row][col] != BLOCKED

if __name__ == "__main__":
    """
    TESTING
    """
    INFINITY = 1000
    GRID_SIZE = 7
    MOVES = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    house_positions = [(0, 5), (2, 1), (2, 5)]
    num_houses = len(house_positions)
    blocked_positions = [(1, 3), (2, 3)]
    all_mask = 2 ** num_houses

    dist = [[[0 for _ in range(len(house_positions))] for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    precompute_distances(0)
    
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            print(f"{dist[i][j][0]} ", end="")
        print("")