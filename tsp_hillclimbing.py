def tsp_hill_climbing(graph,start_node):
    current_node = start_node
    path = [current_node]
    cost = 0

    while len(path) < len(graph):
        min_cost = float('inf')
        next_node = None

        for neighbor in range(len(graph)):
            if neighbor not in path and graph[current_node][neighbor] != 0:
                if graph[current_node][neighbor] < min_cost:
                    min_cost = graph[current_node][neighbor]
                    next_node = neighbor

        if next_node is None:
            break

        path.append(next_node)
        cost += min_cost
        current_node = next_node

    cost += graph[current_node][start_node]
    path.append(start_node)

    return path, cost

graph = [
    [0,10,15,20],
    [10,0,35,25],
    [15,35,0,30],
    [20,25,30,0]
]

start_node = 0
min_path, min_cost = tsp_hill_climbing(graph, start_node)
print("Hill Climbing Minimum path:", min_path)
print("Hill Climbing Minimum cost:", min_cost)