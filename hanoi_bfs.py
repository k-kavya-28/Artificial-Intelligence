from collections import deque

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


def hanoi_bfs(initial_state, final_state):
    queue = deque()
    visited = set()
    queue.append(initial_state)

    while queue:
        current_state = queue.popleft()
        if current_state == final_state:
            return current_state
        visited.add(current_state)
        for next_state in get_next_states(current_state):
            if next_state not in visited:
                queue.append(next_state)
    return None

if __name__ == '__main__':
    initial_state = ((1,1,2,3),(2,),(3,))
    final_state = ((1,),(2,),(3,1,2,3))
    result = hanoi_bfs(initial_state, final_state)
    if result:
        print("Solution found using BFS: ", result)
    else:
        print("No solution found using BFS")


    