import heapq

class Graph:
    def __init__(self, vertices, edges):
        self.vertices = set(vertices)
        self.edges = edges

        # adjacency list
        self.adjacency_list = {}
        for vertex in vertices:
            self.adjacency_list[vertex] = []
            for edge in edges:
                if vertex in edge:
                    for v in edge:
                        if v != vertex:
                            self.adjacency_list[vertex].append(v)

        # incidence matrix
        self.incidence_matrix = {}
        for vertex in vertices:
            self.incidence_matrix[vertex] = {}
            for edge in edges:
                self.incidence_matrix[vertex][edge] = 1 if vertex in edge else 0

        
        self.adjacency_matrix = {}
        for vertex in vertices:
            self.adjacency_matrix[vertex] = {}
            for vertex2 in vertices:
                self.adjacency_matrix[vertex][vertex2] = 0
                for edge in edges:
                    if vertex != vertex2 and vertex in edge and vertex2 in edge:
                        self.adjacency_matrix[vertex][vertex2] = 1

    def walk(self, start, end):
        nodes = self.vertices
        distances = {node: float('inf') for node in nodes}
        distances[start] = 0

        previous = {node: None for node in nodes}
        visited = set()
        queue = [(0, start)]

        while queue:
            current_distance, current_node = heapq.heappop(queue)

            if current_node in visited:
                continue
            visited.add(current_node)

            if current_node == end:
                break

            for neighbour in self.adjacency_list.get(current_node, []):
                edge = tuple(sorted((current_node, neighbour)))
                weight = self.edges.get(edge, float('inf'))

                distance = current_distance + weight
                if distance < distances[neighbour]:
                    distances[neighbour] = distance
                    previous[neighbour] = current_node
                    heapq.heappush(queue, (distance, neighbour))

        # reconstruc path
        path = []
        current = end
        while current is not None:
            path.append(current)
            current = previous[current]
        path.reverse()

        return path if distances[end] != float('inf') else []
