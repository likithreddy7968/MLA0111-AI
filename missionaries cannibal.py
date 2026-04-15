from collections import deque

def is_valid(state):
    M_left, C_left, M_right, C_right, boat = state
    # Missionaries eaten check
    if (M_left < C_left and M_left > 0) or (M_right < C_right and M_right > 0):
        return False
    return True

def get_successors(state):
    M_left, C_left, M_right, C_right, boat = state
    successors = []
    if boat == 'left':
        # Boat moves from left to right
        moves = [(1,0),(2,0),(0,1),(0,2),(1,1)]
        for m,c in moves:
            if M_left >= m and C_left >= c:
                new_state = (M_left-m, C_left-c, M_right+m, C_right+c, 'right')
                if is_valid(new_state):
                    successors.append(new_state)
    else:
        # Boat moves from right to left
        moves = [(1,0),(2,0),(0,1),(0,2),(1,1)]
        for m,c in moves:
            if M_right >= m and C_right >= c:
                new_state = (M_left+m, C_left+c, M_right-m, C_right-c, 'left')
                if is_valid(new_state):
                    successors.append(new_state)
    return successors

def missionaries_cannibals():
    start = (3,3,0,0,'left')
    goal = (0,0,3,3,'right')
    queue = deque()
    queue.append((start, [start]))
    visited = set()

    while queue:
        state, path = queue.popleft()
        if state == goal:
            return path
        if state in visited:
            continue
        visited.add(state)
        for succ in get_successors(state):
            queue.append((succ, path+[succ]))
    return None

solution = missionaries_cannibals()
if solution:
    print("Solution found in", len(solution)-1, "steps:")
    for step in solution:
        print(step)
else:
    print("No solution exists.")
