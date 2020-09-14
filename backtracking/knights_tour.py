import heapq
# Backtracking algorithm to solve knight's tour problem


def is_valid(board, pos, m):
    """
    Check if the move is on the board and to an
    open position
    """
    if in_bounds(pos, m):
        new_position = move(pos, m)
        if board[new_position[0]][new_position[1]] == 0:
            return True
    return False

def in_bounds(pos, m):
    """
    Check if a move is on the board
    """
    return ((pos[0] + m[0]) < BOARD_SIZE and ((pos[1] + m[1]) < BOARD_SIZE) and
        (pos[0] + m[0]) >= 0 and (pos[1] + m[1]) >= 0)

def move(pos, m):
    """
    return new position after making a move
    """
    return (pos[0] + m[0], pos[1] + m[1])

def knights_tour(board, knight_pos, move_number):
    """
    Brute force backtracking algorithm to find a knights tour on the board
    """
    global iteration_counter
    iteration_counter += 1
    if move_number is BOARD_SIZE * BOARD_SIZE + 1:
        return True

    for m in knight_moves:
        if is_valid(board, knight_pos, m):
            new_position = move(m, knight_pos)
            board[new_position[0]][new_position[1]] = move_number
            ret_val = knights_tour(board, new_position, move_number + 1)
            if ret_val:
                return ret_val
            board[new_position[0]][new_position[1]] = 0

    return False

def get_accessibility(board, pos):
    """
    Helper func returns the accessibility of a position
    """
    accessible_squares = 0
    for m in knight_moves:
        move_pos = move(m, pos)
        if is_valid(board, pos, m):
            accessible_squares += 1
    return accessible_squares

def knights_tour_heuristic(board, knight_pos, move_number):
    """
    Backtracking using accesssibility heuristic to find a knights tour on 
    the board
    """
    global iteration_counter
    iteration_counter += 1
    if move_number is BOARD_SIZE * BOARD_SIZE + 1:
        return True

    accessible_knight_moves = []
    for m in knight_moves:
        if is_valid(board, knight_pos, m):
            heapq.heappush(accessible_knight_moves, (get_accessibility(board, move(knight_pos, m)), m))
            
    for _ in range(len(accessible_knight_moves)):
        m = heapq.heappop(accessible_knight_moves)[1]
        new_pos = move(knight_pos, m)
        if board[new_pos[0]][new_pos[1]] == 0:
            board[new_pos[0]][new_pos[1]] = move_number
            ret_val = knights_tour_heuristic(board, new_pos, move_number + 1)
            if ret_val:
                return ret_val
            board[new_pos[0]][new_pos[1]] = 0

def solve_knights_tour(func, board, initial_position):
    """
    Uses func to find a knights tour solution on the board with
    initial_position
    """
    board[initial_position[0]][initial_position[1]] = 1
    result = func(board, initial_position, 2)
    print(f"Iterations: {iteration_counter}")
    print("Solution: ")
    for row in board:
        print(row)

if __name__ == "__main__":
    """
    TESTING
    """
    iteration_counter = 0
    BOARD_SIZE = 6
    knight_moves = [
        (1, 2), (2, 1), (-1, 2), (1, -2),
        (-1, -2), (-2, 1), (2, -1), (-2, -1)
    ]
    board1 = [[0 for _ in range(0, BOARD_SIZE)] for _ in range(0, BOARD_SIZE)]
    board2= [[0 for _ in range(0, BOARD_SIZE)] for _ in range(0, BOARD_SIZE)]
    initial_position = (0, 0)

    print("Trying brute force algorithm....")
    solve_knights_tour(knights_tour, board1, initial_position)
    iteration_counter = 0
    print("Now trying with a heuristic....")
    solve_knights_tour(knights_tour_heuristic, board2, initial_position)