import heapq

class PuzzleState:
    def __init__(self, board, moves=0, previous=None):
        self.board = board
        self.moves = moves
        self.previous = previous
        self.empty = board.index(0)  # position of the empty tile (0)

    def __lt__(self, other):
        return (self.moves + self.heuristic()) < (other.moves + other.heuristic())

    def heuristic(self):
        """Manhattan distance heuristic"""
        distance = 0
        for i, tile in enumerate(self.board):
            if tile == 0: 
                continue
            x, y = divmod(i, 3)
            goal_x, goal_y = divmod(tile - 1, 3)
            distance += abs(x - goal_x) + abs(y - goal_y)
        return distance

    def neighbors(self):
        """Generate possible moves"""
        results = []
        x, y = divmod(self.empty, 3)
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                new_empty = nx * 3 + ny
                new_board = list(self.board)
                new_board[self.empty], new_board[new_empty] = new_board[new_empty], new_board[self.empty]
                results.append(PuzzleState(new_board, self.moves + 1, self))
        return results

def solve_puzzle(start, goal):
    """A* search to solve the 8 puzzle"""
    start_state = PuzzleState(start)
    goal_state = goal

    frontier = []
    heapq.heappush(frontier, start_state)
    explored = set()

    while frontier:
        current = heapq.heappop(frontier)
        if current.board == goal_state:
            path = []
            while current:
                path.append(current.board)
                current = current.previous
            return path[::-1]  # reverse path
        explored.add(tuple(current.board))
        for neighbor in current.neighbors():
            if tuple(neighbor.board) not in explored:
                heapq.heappush(frontier, neighbor)
    return None

# Example usage:
start = [1,2,3,
         4,0,6,
         7,5,8]

goal = [1,2,3,
        4,5,6,
        7,8,0]

solution = solve_puzzle(start, goal)
if solution:
    print("Solution found in", len(solution)-1, "moves:")
    for step in solution:
        print(step[0:3])
        print(step[3:6])
        print(step[6:9])
        print()
else:
    print("No solution exists.")
