import math

def alphabeta(depth, index, is_max, values, alpha, beta):
    if depth == 3:
        return values[index]

    if is_max:
        best = -math.inf
        for i in range(2):
            val = alphabeta(depth + 1, index * 2 + i, False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                print(f"Pruned at depth {depth}, index {index * 2 + i} ❌")
                break
        return best
    else:
        best = math.inf
        for i in range(2):
            val = alphabeta(depth + 1, index * 2 + i, True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                print(f"Pruned at depth {depth}, index {index * 2 + i} ❌")
                break
        return best

# Leaf node values
values = [3, 5, 6, 9, 1, 2, 0, -1]

# Start the alpha-beta pruning
result = alphabeta(0, 0, True, values, -math.inf, math.inf)

print("\nOptimal value:", result)
