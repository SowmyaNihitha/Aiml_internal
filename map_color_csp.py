# Define map: who borders whom
neighbors = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'QLD'],
    'SA': ['WA', 'NT', 'QLD', 'NSW', 'VIC'],
    'QLD': ['NT', 'SA', 'NSW'],
    'NSW': ['QLD', 'SA', 'VIC'],
    'VIC': ['SA', 'NSW'],
    'TAS': []
}

# Possible colors
colors = ['Red', 'Green', 'Blue']

def is_valid(state, region, color):
    for neighbor in neighbors[region]:
        if neighbor in state and state[neighbor] == color:
            return False
    return True

def solve(state, regions):
    if len(state) == len(regions):
        return state

    region = [r for r in regions if r not in state][0]

    for color in colors:
        if is_valid(state, region, color):
            state[region] = color
            result = solve(state, regions)
            if result:
                return result
            del state[region]  # backtrack
    return None

# Run
regions = list(neighbors.keys())
solution = solve({}, regions)

if solution:
    print("Solution:", solution)
else:
    print("No solution found.")
