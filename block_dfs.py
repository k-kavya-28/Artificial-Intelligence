import copy

def getNextStates(state):
    next_states = []
    for i in range(3):
        for j in range(3):
            if i==j or len(state[i])==0:
                continue
            
            next_state = copy.deepcopy(state)
            block = next_state[i].pop()
            next_state[j].append(block)
            next_states.append(next_state)
    return next_states

def block_dfs(initial, final):
    closed = []
    open = []
    open.append((initial, []))
    
    while open:
        state, path = open.pop()
        if state == final:
            return path
        elif str(state) not in closed:
            closed.append(str(state))
            for next_state in getNextStates(state):
                if next_state is not None:
                    open.append((next_state, path + [next_state]))
    return None

if __name__ == '__main__':
    initial = [[1],[2,3],[]]
    final = [[],[],[1,2,3]]
    result = block_dfs(initial, final)
    for i in result:
        print(i)