class Vertex:
    def __init__(self, label):
        self.label = label
        self.edges = {}

    def add_edge(self, neighbor, weight):
        self.edges[neighbor] = weight


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, label):
        if label not in self.vertices:
            vertex = Vertex(label)
            self.vertices[label] = vertex

    def add_edge(self, start, end, weight):
        self.add_vertex(start)
        self.add_vertex(end)
        self.vertices[start].add_edge(end, weight)
        self.vertices[end].add_edge(start, weight)

    def parse(self, lines):
        for line in lines:
            parts = list(map(int, line.split()))
            start_label = parts[0]
            for i in range(1, len(parts), 2):
                end_label = parts[i]
                weight = parts[i + 1]
                self.add_edge(start_label, end_label, weight)

    def dijkstra(self, start):
        distances = {vertex: float('infinity') for vertex in self.vertices}
        distances[start] = 0
        priority_queue = [(0, start)]
        visited = set()

        while priority_queue:
            priority_queue.sort()
            current_distance, current_vertex = priority_queue.pop(0)

            if current_vertex in visited:
                continue

            visited.add(current_vertex)

            for neighbor, weight in self.vertices[current_vertex].edges.items():
                distance = current_distance + weight

                if distance < distances.get(neighbor, float('infinity')):
                    distances[neighbor] = distance
                    priority_queue.append((distance, neighbor))

        return distances


def find_minimum_latency(lines):
    graph = Graph()

    client_vertices = list(map(int, lines[1].split()))

    graph.parse(lines[2:])

    minimum_latency = float('infinity')

    for current_vertex_label in graph.vertices:
        if current_vertex_label in client_vertices:
            continue

        roadmap = graph.dijkstra(current_vertex_label)
        current_maximum_latency = max(roadmap[client_vertex] for client_vertex in client_vertices)

        if current_maximum_latency < minimum_latency:
            minimum_latency = current_maximum_latency

    return minimum_latency


def run(input_file_name, output_file_name):
    try:
        with open(input_file_name, 'r') as file:
            lines = file.read().splitlines()

        minimum_latency = find_minimum_latency(lines)

        with open(output_file_name, 'w') as file:
            file.write(str(minimum_latency))

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    input_file_name = "gamsrv.in"
    output_file_name = "gamsrv.out"
    run(input_file_name, output_file_name)
