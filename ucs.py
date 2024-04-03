from queue import PriorityQueue

def uniform_cost_search(graph, start, goal):
    frontier = PriorityQueue()
    frontier.put((0, start)) # enqueue the initial state with cost 0
    explored = set()
    
    while not frontier.empty():
        cost, node = frontier.get() # dequeue the node with lowest cost
        if node == goal:
            return cost # return the cost of the goal node
        explored.add(node)
        for neighbor, neighbor_cost in graph[node]:
            if neighbor not in explored:
                frontier.put((cost + neighbor_cost, neighbor)) # enqueue neighbor node with its cost
    return None # goal node not found

graph = {
    'S': [('A', 1), ('B', 5),('C', 10)],
    'A': [('G', 10)],
    'B': [('G', 5)],
    'C': [('G', 5)]
}

start = 'S'
goal = 'G'

cost = uniform_cost_search(graph, start, goal)

if cost is not None:
    print("Cost of solution:", cost)
else:
    print("Goal not achievable.")