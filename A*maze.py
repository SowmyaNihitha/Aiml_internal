import heapq

def heuristic(a, b):
    """Manhattan Distance heuristic"""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star_algorithm(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    open_list = []
    heapq.heappush(open_list, (0, start))  # (f-cost, position)

    came_from = {}  # Track path
    g_cost = {start: 0}  # Cost from start to node
    f_cost = {start: heuristic(start, goal)}  # Estimated total cost

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == goal:
            return reconstruct_path(came_from, current)

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # 4 directions
            neighbor = (current[0] + dx, current[1] + dy)

            if not (0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols):
                continue  # Out of bounds

            if grid[neighbor[0]][neighbor[1]] == 1:
                continue  # Wall/obstacle

            tentative_g = g_cost[current] + 1

            if neighbor not in g_cost or tentative_g < g_cost[neighbor]:
                g_cost[neighbor] = tentative_g
                f_cost[neighbor] = tentative_g + heuristic(neighbor, goal)
                heapq.heappush(open_list, (f_cost[neighbor], neighbor))
                came_from[neighbor] = current

    return None  # No path found

def reconstruct_path(came_from, current):
    """Reconstruct path from goal to start."""
    path = []
    while current in came_from:
        path.append(current)
        current = came_from[current]
    path.append(current)  # Append start position
    return path[::-1]  # Reverse path

# Example Grid (0 = open, 1 = obstacle)
grid = [
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 0],
    [0, 0, 0, 1, 0, 0],
    [0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 0]
]

start = (0, 0)
goal = (5, 5)

path = a_star_algorithm(grid, start, goal)

if path:
    print("Path found:", path)
else:
    print("No path found!")
