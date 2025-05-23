from collections import deque
from math import gcd

def water_jug(m, n, d):
    if d > max(m, n) or d % gcd(m, n) != 0:
        return "Not possible"

    visited = set()
    q = deque([((0, 0), [])])

    while q:
        (a, b), path = q.popleft()
        if a == d or b == d:
            path.append((a, b))
            for step in path:
                print(step)
            return f"Steps: {len(path) - 1}"

        if (a, b) in visited:
            continue
        visited.add((a, b))

        # Possible next moves
        moves = [
            (m, b), (a, n), (0, b), (a, 0),
            (a - min(a, n - b), b + min(a, n - b)),  # a → b
            (a + min(b, m - a), b - min(b, m - a))   # b → a
        ]

        for new_state in moves:
            q.append((new_state, path + [(a, b)]))

    return "No solution"

# Example usage
print(water_jug(4, 3, 2))
