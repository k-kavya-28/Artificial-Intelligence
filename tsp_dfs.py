def tsp_dsf(graph, start_node):
    min_path = []
    min_cost = float('inf')
    stack = [(start_node,[start_node],0)]

    while stack:
        current_node, path, cost = stack.pop()
        if len(path) == len(graph) and graph[current_node][start_node] != 0:
            path.append(start_node)
            cost += graph[current_node][start_node]
            if cost < min_cost:
                min_path = path
                min_cost = cost
        else:
            for next_node in range(len(graph)):
                if next_node not in path and graph[current_node][next_node] != 0:
                    new_path = path + [next_node]
                    new_cost = cost + graph[current_node][next_node]
                    stack.append((next_node,new_path,new_cost))

    return min_path, min_cost

graph = [
    [0,10,15,20],
    [10,0,35,25],
    [15,35,0,30],
    [20,25,30,0]
]

start_node = 0
min_path, min_cost = tsp_dsf(graph, start_node)
print("DFS Minimum path:", min_path)
print("DFS Minimum cost:", min_cost)