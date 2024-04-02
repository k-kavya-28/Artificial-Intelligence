import copy
import heapq

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

def heuristic(state, final):
    score = 0
    for peg in state:
        for i,block in enumerate(peg):
            if block in final[i]:
                score += i
            else:
                score -= i
    return score

def block_astar(initial, final):
    closed = set()
    open_list = []
    heapq.heappush(open_list, (heuristic(initial, final), initial, []))
    
    while open_list:
        _,state, path = heapq.heappop(open_list)
        if state == final:
            return path
        elif str(state) not in closed:
            closed.add(str(state))
            for next_state in getNextStates(state):
                if next_state is not None:
                    heapq.heappush(open_list, (heuristic(next_state, final), next_state, path + [next_state]))
    return None

if __name__ == '__main__':
    initial = [[1],[2,3],[]]
    final = [[],[],[1,2,3]]
    result = block_astar(initial, final)
    if result is not None:
        for i in result:
            print(i)
    else:
        print("No solution found")