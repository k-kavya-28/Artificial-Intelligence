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