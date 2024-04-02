import copy
import random

def getHeuristic(initial, final):
    count = 0
    for i in range(3):
        for j in range(3):
            if initial[i][j] == final[i][j]:
                count += 1
    return count

def getBlankSpaces(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return (i,j)
            
def getNextMove(state):
    blank = getBlankSpaces(state)
    next_state = []

    if blank[1] > 0:
        new_state = copy.deepcopy(state)
        new_state[blank[0]][blank[1]] = new_state[blank[0]][blank[1]-1]
        new_state[blank[0]][blank[1]-1] = 0
        next_state.append(new_state)

    if blank[1] < 2:
        new_state = copy.deepcopy(state)
        new_state[blank[0]][blank[1]] = new_state[blank[0]][blank[1]+1]
        new_state[blank[0]][blank[1]+1] = 0
        next_state.append(new_state)

    if blank[0] > 0:
        new_state = copy.deepcopy(state)
        new_state[blank[0]][blank[1]] = new_state[blank[0]-1][blank[1]]
        new_state[blank[0]-1][blank[1]] = 0
        next_state.append(new_state)

    if blank[0] < 2:
        new_state = copy.deepcopy(state)
        new_state[blank[0]][blank[1]] = new_state[blank[0]+1][blank[1]]
        new_state[blank[0]+1][blank[1]] = 0
        next_state.append(new_state)

    return next_state

def eightPuzzleHillClimb(initial, final):
    curr = initial
    path = [curr]

    while True:
        h = getHeuristic(curr, final)
        if h == 9:
            return path
        
        next_states = getNextMove(curr)
        h_next = [getHeuristic(next, final) for next in next_states]

        if max(h_next) < h:
            print("Stuck in local maxima")
            return path
        if next_states is None:
            print("Failed to find solution")
            return path
        
        indices = [i for i,j in enumerate(h_next) if j>h]
        choice_index = random.choice(indices)
        curr = next_states[choice_index]
        path.append(curr)
        
if __name__ == '__main__':
    initial = [[2,0,3],[1,8,4],[7,6,5]]
    final = [[1,2,3],[8,0,4],[7,6,5]]
    result = eightPuzzleHillClimb(initial, final)
    if result is None:
        print("Failed to find solution")
    else:
        for state in result:
            for i in state:
                print(i)
            print('\n\n')