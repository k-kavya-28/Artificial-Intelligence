def water_jug_dfs(jug1, jug2, aim):
    stack = [(0,0)]
    visited = set()
    
    while stack:
        amt1, amt2 = stack.pop()
        if amt1 == aim or amt2 == aim:
            print("Soln found: ")
            print(f"Jug1: {amt1}, Jug2: {amt2}")
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
                visited.add(move)
                stack.append(move)
    
    print("No solution found")
    return False

jug1, jug2, aim = 4,3,2
water_jug_dfs(jug1, jug2, aim)
    