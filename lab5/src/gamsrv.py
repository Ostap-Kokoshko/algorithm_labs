def get_neighbors(graph, vertex):
    return graph[vertex]


def dijkstra(start_node, graph):
    distances = {vertex: float('infinity') for vertex in graph.keys()}
    distances[start_node] = 0

    visited = set()
    queue = [(0, start_node)]

    while queue:
        queue.sort()
        current_distance, node = queue.pop(0)

        if node in visited:
            continue

        visited.add(node)

        for neighbor, weight in get_neighbors(graph, node):
            total_distance = current_distance + weight

            if total_distance < distances[neighbor]:
                distances[neighbor] = total_distance
                queue.append((total_distance, neighbor))

    return distances


def gamsrv(graph, client_list):
    result_list = []
    for node in graph:
        helper = dijkstra(node, graph)
        res = max(helper[client] for client in client_list)
        result_list.append(res)
    return min(result_list)


def read_input_file(file_path):
    with open(file_path, 'r') as file:
        verteces, edges = map(int, file.readline().split())
        clients = file.readline().split()
        graph = {str(i): [] for i in range(1, verteces + 1)}
        for _ in range(edges):
            start_node, end_node, latency = map(int, file.readline().split())
            graph[str(start_node)].append((str(end_node), latency))
            graph[str(end_node)].append((str(start_node), latency))

    return graph, clients


def write_output_file(file_path, result):
    with open(file_path, 'w') as file:
        file.write(str(result))


input_file_path = 'gamsrv.in'
output_file_path = 'gamsrv.out'

graph, client_list = read_input_file(input_file_path)
result = gamsrv(graph, client_list)
write_output_file(output_file_path, result)
