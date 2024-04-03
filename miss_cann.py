from collections import deque

# State representation: (m_on_left, c_on_left, boat_side)
# where m_on_left is the number of missionaries on the left side,
# c_on_left is the number of cannibals on the left side,
# and boat_side indicates the side where the boat is located (0 for left, 1 for right)

def is_valid_state(state):
    m_on_left, c_on_left, _ = state
    m_on_right = 3 - m_on_left
    c_on_right = 3 - c_on_left
    
    if(m_on_left and m_on_left < c_on_left) or (m_on_right and m_on_right < c_on_right):
        return False
    return True

def getNextStates(state):
    next_states = []
    m_on_left, c_on_left, boat_side = state
    m_on_right = 3 - m_on_left
    c_on_right = 3 - c_on_left
    
    if boat_side == 0:
        for m in range(3):
            for c in range(3):
                if 1<=m+c<=2:
                    new_state = (m_on_left - m, c_on_left - c, 1)
                    if(0<=new_state[0]<=3 and 0<=new_state[1]<=3 and is_valid_state(new_state)):
                        next_states.append(new_state)
    else:
        for m in range(3):
            for c in range(3):
                if 1<=m+c<=2:
                    new_state = (m_on_left + m, c_on_left + c, 0)
                    if(0<=new_state[0]<=3 and 0<=new_state[1]<=3 and is_valid_state(new_state)):
                        next_states.append(new_state)
    return next_states
                        
def mc_bfs():
    start_state = (3,3,0)
    goal_state = (0,0,1)
    
    open = deque()
    close = set()
    open.append([start_state])
    
    while open:
        path = open.popleft()
        current_state = path[-1]
        if current_state == goal_state:
            return path
        close.add(current_state)
        for next_state in getNextStates(current_state):
            if next_state not in close:
                new_path = list(path)
                new_path.append(next_state)
                open.append(new_path)
                
def mc_dfs():
    start_state = (3,3,0)
    goal_state = (0,0,1)
    
    open = []
    close = set()
    open.append([start_state])
    
    while open:
        path = open.pop()
        current_state = path[-1]
        if current_state == goal_state:
            return path
        close.add(current_state)
        for next_state in getNextStates(current_state):
            if next_state not in close:
                new_path = list(path)
                new_path.append(next_state)
                open.append(new_path)
                
print("BFS solution: ")
bfs_sol = mc_bfs()
for i,state in enumerate(bfs_sol):
    print(f"Step{i}: {state}")
        
print("DFS solution")
dfs_sol = mc_dfs()
for i,state in enumerate(dfs_sol):
    print(f"Step{i}: {state}")