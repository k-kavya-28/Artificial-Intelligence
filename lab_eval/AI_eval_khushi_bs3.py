import heapq

class PuzzleState:
    def __init__(self, state, parent=None, move="Initial"):
        self.state = state
        self.parent = parent
        self.move = move
        self.cost = 0
        self.depth = 0
        self.calculate_cost()

    def calculate_cost(self):
        self.cost = self.manhattan_distance() + self.depth

    def manhattan_distance(self):
        distance = 0
        goal_state = [[1, 2, 3], [4, 5, 6], [7, 0, 0]]  
        for i in range(3):
            for j in range(3):
                if self.state[i][j] != 0:
                    row, col = divmod(self.state[i][j] - 1, 3)
                    distance += abs(row - i) + abs(col - j)
        return distance

    def get_children(self):
        children = []
        empty_blocks = [(i, j) for i in range(3) for j in range(3) if self.state[i][j] == 0]
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            for x, y in empty_blocks:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < 3 and 0 <= new_y < 3:
                    new_state = [row[:] for row in self.state]
                    new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
                    children.append(PuzzleState(new_state, parent=self, move=(x, y)))
        return children

    def __lt__(self, other):
        return self.cost < other.cost  

def best_first_search(initial_state, goal_state):  
    heap = []
    visited = set()
    heapq.heappush(heap, initial_state)
    
    while heap:
        current_state = heapq.heappop(heap)
        if current_state.state == goal_state:
            return current_state
        visited.add(tuple(map(tuple, current_state.state)))
        for child in current_state.get_children():
            if tuple(map(tuple, child.state)) not in visited:
                heapq.heappush(heap, child)

    return None

initial_state = [[0, 3, 6], [1, 2, 0], [4, 5, 7]]
goal_state = [[1, 2, 3], [4, 5, 6], [7, 0, 0]]

initial_puzzle_state = PuzzleState(initial_state)

result = best_first_search(initial_puzzle_state, goal_state)

if result is not None:
    path = []
    while result.parent:
        path.append(result.state)
        result = result.parent
    path.append(initial_state)
    path.reverse()
    print("Solution Path:")
    for state in path:
        for row in state:
            print(row)
        print()
else:
    print("No solution found.")
