# Import necessary modules
def is_safe(board, row, col, N):
    # Check this row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check lower diagonal on the left side
    i, j = row, col
    while j >= 0 and i < N:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True

def solve_n_queens_util(board, col, N):
    # If all queens are placed, return True
    if col >= N:
        return True

    # Consider this column and try placing this queen in all rows one by one
    for i in range(N):
        if is_safe(board, i, col, N):
            # Place this queen in board[i][col]
            board[i][col] = 1

            # Recur to place the rest of the queens
            if solve_n_queens_util(board, col + 1, N):
                return True

            # If placing queen in board[i][col] doesn't lead to a solution, remove the queen (backtrack)
            board[i][col] = 0

    # If the queen cannot be placed in any row in this column, return False
    return False

def solve_n_queens(N):
    # Initialize the board
    board = [[0 for _ in range(N)] for _ in range(N)]

    if solve_n_queens_util(board, 0, N):
        # Print the solution
        for row in board:
            print(" ".join(str(x) for x in row))
    else:
        print("Solution does not exist.")

# Driver code
N = 8
solve_n_queens(N)
