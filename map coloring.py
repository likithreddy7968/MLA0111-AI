
neighbors = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q':  ['NT', 'SA', 'NSW'],
    'NSW':['SA', 'Q', 'V'],
    'V':  ['SA', 'NSW'],
    'T':  []
}

colors = ['Red', 'Green', 'Blue']

def is_valid(assignment, region, color):
    for neighbor in neighbors[region]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def backtrack(assignment):
    if len(assignment) == len(neighbors):
        return assignment

    # Select an unassigned region
    region = [r for r in neighbors if r not in assignment][0]

    for color in colors:
        if is_valid(assignment, region, color):
            assignment[region] = color
            result = backtrack(assignment)
            if result:
                return result
            assignment.pop(region)
    return None

solution = backtrack({})
print("Map Coloring Solution:")
for region, color in solution.items():
    print(region, "->", color)
