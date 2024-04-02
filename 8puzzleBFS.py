import copy
from collections import deque

def getBlankSpaces(state):
    for i in range(3):
        for j in range(3):
            if state [i][j] == 0:
                return (i,j)
            
def getNextMove(state):
    blank = getBlankSpaces(state)
    next_state = []

    #left move allowed
    if blank[1]>0:
        new_state = copy.deepcopy(state)
        new_state[blank[0]][blank[1]] = new_state[blank[0]][blank[1]-1]
        new_state[blank[0]][blank[1]-1] = 0
        next_state.append(new_state)

    #right move allowed
    if blank[1]<2:
         new_state = copy.deepcopy(state)
         new_state[blank[0]][blank[1]] = new_state[blank[0]][blank[1]+1]
         new_state[blank[0]][blank[1]+1] = 0
         next_state.append(new_state)

    #up move allowed
    if blank[0]>0:
        new_state = copy.deepcopy(state)
        new_state[blank[0]][blank[1]] = new_state[blank[0]-1][blank[1]]
        new_state[blank[0]-1][blank[1]] = 0
        next_state.append(new_state)

    #down move allowed
    if blank[0]<2:
        new_state = copy.deepcopy(state)
        new_state[blank[0]][blank[1]] = new_state[blank[0]+1][blank[1]]
        new_state[blank[0]+1][blank[1]] = 0
        next_state.append(new_state)

    return next_state

def eightPuzzleBFS(initial, final):
    closed = []
    open = deque()
    open.append((initial, []))

    while open:
        state, path = open.popleft()
        if state == final:
            return path
        elif str(state) not in closed:
            closed.append(str(state))
            for next in getNextMove(state):
                if next is not None:
                    open.append((next, path + [next]))

if __name__ == '__main__':
    initial = [[2,0,3],[1,8,4],[7,6,5]]
    final = [[1,2,3],[8,0,4],[7,6,5]]

    result = eightPuzzleBFS(initial, final)

    for state in result:
        for i in state:
            print(i)
        print('\n\n')