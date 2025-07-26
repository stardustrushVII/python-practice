from collections import deque
def bfs(graph, start):
    visited = set() # tracker of the visited
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited: # only process where we ain't gone
            print("Visited", node)
            visited.add(node) # marks as visited
            # adds all unvisited to the Q
            for neighbour in graph [node]:
                if neighbour not in visited:
                    queue.append(neighbour)


# structure of graph as dictionary
graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C"]
}

# Run bfs starting from node A
bfs(graph, "A")