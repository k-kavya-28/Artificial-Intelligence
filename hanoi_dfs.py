def get_next_states(state):
    next_states = []
    for i in range(3):
        if state[i]:    #peg not empty
            for j in range(3):
                if i!=j and (not state[j] or state[i][-1] <= state[j][-1]):
                    new_state = list(state)
                    new_state[j] = new_state[j] + (new_state[i][-1],)
                    new_state[i] = new_state[i][:-1]
                    next_states.append(tuple(new_state))
    return next_states


def hanoi_dfs(current_state, final_state, visited):
    if current_state == final_state:
        return current_state
    visited.add(current_state)
    for next_state in get_next_states(current_state):
        if next_state not in visited:
            result = hanoi_dfs(next_state, final_state, visited)
            if result:
                return result
    return None

# Initial and Final states
initial_state = ((1, 1, 2, 3), (2,), (3,))
final_state = ((1,), (2,), (3, 1, 2, 3))

# Solve using DFS
visited = set()
result = hanoi_dfs(initial_state, final_state, visited)
if result:
    print("Solution found using DFS:", result)
else:
    print("No solution found using DFS.")
