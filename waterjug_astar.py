import heapq

def heuristic(state, aim):
    amt1, amt2 = state
    return abs(amt1-aim) + abs(amt2-aim)

def water_jug_astar(jug1, jug2, aim):
    start_state = (0,0)
    goal_state = (aim, aim)
    visited = set()
    open_list = [(heuristic(start_state, aim), start_state)]
    
    while open_list:
        _,current_state = heapq.heappop(open_list)
        visited.add(current_state)
        amt1, amt2 = current_state
        
        if current_state == goal_state:
            print("Solution found")
            print(f"Jug1: {current_state[0]}, Jug2: {current_state[1]}")
            return True
        
        next_moves = [
            (amt1, 0),
            (0, amt2),
            (jug1, amt2),
            (amt1, jug2),
            (amt1 + min(amt2, (jug1-amt1)), amt2-min(amt2, (jug1-amt1))),
            (amt1-min(amt1, (jug2-amt2)), amt2 + min(amt1, (jug2-amt2)))
        ]
        
        for move in next_moves:
            if move not in visited:
                heapq.heappush(open_list, (heuristic(move, aim), move))
    
    print("No solution found")
    return False

jug1, jug2, aim = 4,3,2
water_jug_astar(jug1, jug2, aim)
    