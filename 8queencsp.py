def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True

def solve_n_queens(board, row, n):
    if row == n:
        return [board[:]]
    solutions = []
    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solutions += solve_n_queens(board, row + 1, n)
            board[row] = -1  # backtrack
    return solutions

def print_solutions(solutions, n):
    for sol in solutions:
        for row in sol:
            print(" ".join("Q" if i == row else "." for i in range(n)))
        print("--------------------------")
    print("Number of solutions:", len(solutions))

# Run
n = int(input("Enter number of queens: "))
board = [-1] * n
solutions = solve_n_queens(board, 0, n)
print_solutions(solutions, n)
