from copy import deepcopy
from queue import PriorityQueue

initial_state = [
    [0, 3, 6],
    [1, 2, 0],
    [4, 5, 7]
]

goal = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 0, 0]
]

queue = PriorityQueue()

class statenode:
    def _init_(self, state, parent=None, step=0):
        self.state = state
        self.parent = parent
        self.step = step

    def _lt_(self, other):
        return heuristic(self.state) < heuristic(other.state)

    def getparent(self):
        return self.parent

def heuristic(state):
    distance = 0
    for i in range(len(state)):
        for j in range(len(state[i])):
            value = state[i][j]
            if value != 0:
                target_i, target_j = (value - 1) // len(state), (value - 1) % len(state[i])
                distance += abs(i - target_i) + abs(j - target_j)
    return distance

def findblank(state):
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] == 0:
                return i, j

def up(state):
    i, j = findblank(state)
    if i > 0:
        state[i][j], state[i - 1][j] = state[i - 1][j], state[i][j]
        return state, 1
    return state, 0

def down(state):
    i, j = findblank(state)
    if i < 2:
        state[i][j], state[i + 1][j] = state[i + 1][j], state[i][j]
        return state, 1
    return state, 0

def left(state):
    i, j = findblank(state)
    if j > 0:
        state[i][j], state[i][j - 1] = state[i][j - 1], state[i][j]
        return state, 1
    return state, 0

def right(state):
    i, j = findblank(state)
    if j < 2:
        state[i][j], state[i][j + 1] = state[i][j + 1], state[i][j]
        return state, 1
    return state, 0

def parent(state):
    q = []
    while state:
        q.append(state.state)
        state = state.getparent()
    return q

def printstate(state):
    for row in state:
        print(*row)
    print()

def bfs():
    queue.put(statenode(initial_state))
    visited = set()
    visited.add(tuple(map(tuple, initial_state)))
    while not queue.empty():
        currentstate = queue.get()
        if currentstate.state == goal:
            print(currentstate.step)
            k = parent(currentstate.getparent())
            while k:
                h = k.pop()
                print("Heuristic:", heuristic(h))
                printstate(h)
            printstate(currentstate.state)
            print("pass")
            return 1
        for movfun in [up, down, left, right]:
            next_state, m = movfun(deepcopy(currentstate.state))
            if m == 1:
                if tuple(map(tuple, next_state)) not in visited:
                    queue.put(statenode(next_state, currentstate, currentstate.step + 1))
                    visited.add(tuple(map(tuple, next_state)))
    return None

bfs()