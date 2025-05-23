graph = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'C', 'E'],
    'C': ['A', 'B', 'D', 'E'],
    'D': ['A', 'C', 'E'],
    'E': ['B', 'C', 'D']
}
# Available colors
colors = ['Red', 'Green', 'Blue']
# Store the color assigned to each region
assignment = {}

def is_safe(region, color):
    for neighbor in graph[region]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def backtrack(region_list, index=0):
    if index == len(region_list):
        return True  # All regions are assigned
    
    region = region_list[index]
    for color in colors:
        if is_safe(region, color):
            assignment[region] = color
            if backtrack(region_list, index + 1):
                return True
            del assignment[region]  # backtrack
    return False

# Run the algorithm
region_list = list(graph.keys())
if backtrack(region_list):
    print("Color assignment:", assignment)
else:
    print("No solution found.")
