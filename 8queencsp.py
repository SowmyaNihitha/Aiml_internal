def is_safe(assignment, row, col):
    for r in assignment:
        c = assignment[r]
        if c == col or abs(r - row) == abs(c - col):
            return False
    return True

def solve_n_queens(n, row=0, assignment={}):
    if row == n:
        return assignment

    for col in range(n):
        if is_safe(assignment, row, col):
            assignment[row] = col
            result = solve_n_queens(n, row + 1, assignment)
            if result:
                return result
            del assignment[row]
    return None

# Run for 8 queens
solution = solve_n_queens(8)
if solution:
    print("Solution (row: column):", solution)
else:
    print("No solution found")
