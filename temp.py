import copy
from queue import PriorityQueue

def heuristic(initial, final):
    count = 0
    for i in range(3):
        for j in range(3):
            if initial[i][j] != final[i][j]:
                count = count+1
    return count

def blankspaces(state):
    for i in range(3):
        for j in range(3):
            if state [i][j] == 0:
                return (i,j)
def getnextmove(state):
    blank = blankspaces(state)
    next_state = []
    
    if blank[1]>0:
        new_state = copy.deepcopy(state)
        new_state[blank[0]][blank[1]]= new_state[blank[0]][blank[1]-1]
        new_state[blank[0]][blank[1]-1]= 0
        next_state.append(new_state)
    
    if blank[1]<2:
        new_state = copy.deepcopy(state)
        new_state[blank[0]][blank[1]]= new_state[blank[0]][blank[1]+1]
        new_state[blank[0]][blank[1]+1]= 0
        next_state.append(new_state)
    
    if blank[0]>0:
        new_state = copy.deepcopy(state)
        new_state[blank[0]][blank[1]]= new_state[blank[0]-1][blank[1]]
        new_state[blank[0]-1][blank[1]]= 0
        next_state.append(new_state)
    
    if blank[0]<2:
        new_state = copy.deepcopy(state)
        new_state[blank[0]][blank[1]]= new_state[blank[0]+1][blank[1]]
        new_state[blank[0]+1][blank[1]]= 0
        next_state.append(new_state)
        
    return next_state

def eightpuzzle_bestfs(initial, final):
    closed=[]
    open=PriorityQueue()
    open.put((heuristic(initial, final), initial, []))
    
    while open:
        _,state,path = open.get()
        if state==final:
            return path
        elif str(state) not in closed:
            closed.append(state)
            for next_state in getnextmove(state):
                if next_state is not None:
                    open.put((heuristic(next_state,final), next_state, path+[next_state]))
    return None

if __name__ == '__main__':
    initial = [[2,0,3],[1,8,4],[7,6,5]]
    final = [[1,2,3],[8,0,4],[7,6,5]]
    
    result= eightpuzzle_bestfs(initial, final)
    
    for state in result:
        for i in state:
            print(i)
        print('\n\n')