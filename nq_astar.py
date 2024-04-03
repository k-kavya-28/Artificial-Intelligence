from queue import PriorityQueue

class NQueensAStar:
    def __init__(self, n):
        self.n = n

    def heuristic(self, state):
        conflicts = 0
        for i in range(len(state)):
            for j in range(i + 1, len(state)):
                if state[i] == state[j] or abs(state[i] - state[j]) == j - i:
                    conflicts += 1
        return conflicts

    def is_goal(self, state):
        return self.heuristic(state) == 0

    def solve(self):
        priority_queue = PriorityQueue()
        initial_state = [-1] * self.n
        priority_queue.put((0, initial_state))

        while not priority_queue.empty():
            _, current_state = priority_queue.get()

            if self.is_goal(current_state):
                return current_state

            for col in range(self.n):
                new_state = current_state[:] + [-1] * (self.n - len(current_state))  # Initialize new_state with enough elements
                new_state[current_state.count(-1)] = col
                priority_queue.put((self.heuristic(new_state), new_state))

        return None


    def print_solution(self, solution):
        for row in solution:
            print(' '.join('Q' if col == i else '.' for i, col in enumerate(row)))

if __name__ == "__main__":
    n = 4
    solver = NQueensAStar(n)
    solution = solver.solve()
    if solution:
        print("Solution found:")
        solver.print_solution([[(i, col) for i, col in enumerate(solution)]])
    else:
        print("No solution found.")
