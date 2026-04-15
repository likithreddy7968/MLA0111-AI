import itertools

def travelling_salesman(distance_matrix):
    n = len(distance_matrix)
    cities = range(n)
    best_path = None
    best_cost = float("inf")

    for perm in itertools.permutations(cities):
        # must return to start
        cost = 0
        for i in range(n-1):
            cost += distance_matrix[perm[i]][perm[i+1]]
        cost += distance_matrix[perm[-1]][perm[0]]  # return to start

        if cost < best_cost:
            best_cost = cost
            best_path = perm

    return best_path, best_cost

# Example usage:
# Distance matrix for 4 cities
distance_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

path, cost = travelling_salesman(distance_matrix)
print("Best path:", path)
print("Minimum cost:", cost)
