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

def blockDFS(initial, final, depth_limit):
    closed = []
    open = []
    open.append((initial, []))

    while open:
        state, path = open.pop()
        if state == final:
            return path
        elif str(state) not in closed and len(path) < depth_limit:
            closed.append(str(state))
            for next_state in reversed(getNextStates(state)):
                if next_state is not None:
                    open.append((next_state, path + [next_state]))
    return None

def blockDFS_ID(initial, final):
    depth_limit = 1
    while True:
        result = blockDFS(initial, final, depth_limit)
        if result is not None:
            return result
        depth_limit += 1

if __name__ == '__main__':

    initial = [ [ 1 ],[2,3],[ ] ]  
    final = [ [ ],[  ],[ 1,2,3 ] ] 

    result = blockDFS_ID(initial, final)

    if result is None:
        print("Not found")
    else:
        for i in result:
            print(i)