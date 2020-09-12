import heapq

def is_valid(pos, move):
    return ((pos[0] + move[0]) < BOARD_SIZE and ((pos[1] + move[1]) < BOARD_SIZE) and
        (pos[0] + move[0]) >= 0 and (pos[1] + move[1]) >= 0)

def move(pos, move):
    return (pos[0] + move[0], pos[1] + move[1])

def knights_tour(board, knight_pos, move_number):

    global iteration_counter
    iteration_counter += 1
    if move_number is BOARD_SIZE * BOARD_SIZE + 1:
        print("solution found")
        return True

    for m in knight_moves:
        if is_valid(knight_pos, m):
            new_pos = move(knight_pos, m)
            if board[new_pos[0]][new_pos[1]] == 0:
                board[new_pos[0]][new_pos[1]] = move_number
                
                ret_val = knights_tour(board, new_pos, move_number + 1)
                if ret_val:
                    return ret_val
                board[new_pos[0]][new_pos[1]] = 0

def get_accessibility(board, pos):

    accessible_squares = 0
    for m in knight_moves:
        move_pos = move(m, pos)
        if is_valid(pos, m) and board[move_pos[0]][move_pos[1]] is 0:
            accessible_squares += 1
    return accessible_squares

def knights_tour_heuristic(board, knight_pos, move_number):
    global heuristic_iteration_counter
    heuristic_iteration_counter += 1
    if move_number is BOARD_SIZE * BOARD_SIZE + 1:
        print("solution found")
        return True

    accessible_knight_moves = []
    for m in knight_moves:
        if is_valid(knight_pos, m):
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


if __name__ == "__main__":

    iteration_counter = 0
    heuristic_iteration_counter = 0
    BOARD_SIZE = 6
    knight_moves = [(1, 2), (2, 1), (-1, 2), (1, -2), (-1, -2), (-2, 1), (2, -1), (-2, -1)]
    board = [[0 for _ in range(0, BOARD_SIZE)] for _ in range(0, BOARD_SIZE)]
    board_heuristic = [[0 for _ in range(0, BOARD_SIZE)] for _ in range(0, BOARD_SIZE)]
    initial_position = (0, 0)

    board[initial_position[0]][initial_position[1]] = 1
    result = knights_tour(board, initial_position, 2)
    print(f"Iterations with no heuristic: {iteration_counter}")
    print("solution: ")
    for row in board:
        print(row)

    board_heuristic[initial_position[0]][initial_position[1]] = 1
    result = knights_tour_heuristic(board_heuristic, initial_position, 2)
    print(f"Iterations with heuristic: {heuristic_iteration_counter}")
    print("solution: ")
    for row in board_heuristic:
        print(row)