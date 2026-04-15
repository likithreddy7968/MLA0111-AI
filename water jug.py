from collections import deque

def water_jug_problem(jug1_capacity, jug2_capacity, target):
    # Initial state: both jugs empty
    visited = set()
    queue = deque()
    queue.append((0, 0))  # (jug1, jug2)

    while queue:
        jug1, jug2 = queue.popleft()

        # If target is reached
        if jug1 == target or jug2 == target:
            print("Solution found:")
            print(jug1, jug2)
            return True

        if (jug1, jug2) in visited:
            continue
        visited.add((jug1, jug2))

        # Possible operations:
        states = []

        # Fill Jug1
        states.append((jug1_capacity, jug2))
        # Fill Jug2
        states.append((jug1, jug2_capacity))
        # Empty Jug1
        states.append((0, jug2))
        # Empty Jug2
        states.append((jug1, 0))
        # Pour Jug1 -> Jug2
        pour = min(jug1, jug2_capacity - jug2)
        states.append((jug1 - pour, jug2 + pour))
        # Pour Jug2 -> Jug1
        pour = min(jug2, jug1_capacity - jug1)
        states.append((jug1 + pour, jug2 - pour))

        for state in states:
            if state not in visited:
                queue.append(state)

    print("No solution possible.")
    return False

# Example usage:
jug1_capacity = 4
jug2_capacity = 3
target = 2

water_jug_problem(jug1_capacity, jug2_capacity, target)
