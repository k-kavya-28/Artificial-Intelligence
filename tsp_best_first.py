from queue import PriorityQueue

def tsp_best_first_search(graph, start_node):
    min_path = []
    min_cost = float('inf')
    open_list = PriorityQueue()
    open_list.put((0, start_node, [start_node]))

    while not open_list.empty():
        _, current_node, path = open_list.get()
        if len(path) == len(graph) and graph[current_node][start_node] != 0:
            path.append(start_node)
            cost = sum(graph[path[i]][path[i+1]] for i in range(len(path)-1))
            if cost < min_cost:
                min_path = path
                min_cost = cost
        else:
            for next_node in range(len(graph)):
                if next_node not in path and graph[current_node][next_node] != 0:
                    new_path = path + [next_node]
                    priority = sum(graph[new_path[i]][new_path[i+1]] for i in range(len(new_path)-1))
                    open_list.put((priority, next_node, new_path))

    return min_path, min_cost

graph = [
    [0,10,15,20],
    [10,0,35,25],
    [15,35,0,30],
    [20,25,30,0]
]

start_node = 0

min_path, min_cost = tsp_best_first_search(graph, start_node)
print("Best-First Search Minimum path:", min_path)
print("Best-First Search Minimum cost:", min_cost)
