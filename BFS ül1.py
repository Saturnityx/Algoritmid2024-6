from collections import deque

# Define the BFS function
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    order = []

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            order.append(vertex)
            queue.extend(neighbor for neighbor in graph[vertex] if neighbor not in visited)

    return order

# Define a sample graph as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Perform BFS on the graph starting from vertex 'A'
bfs_order = bfs(graph, 'A')

print(f"BFS traversal order starting from vertex 'A': {bfs_order}")

# Tipp 'A' on ühendatud tippudega 'B' ja 'C'.
# Tipp 'B' on ühendatud tippudega 'D' ja 'E'.
# Tipp 'C' on ühendatud tippuga 'F'.
# Tipud 'D' ja 'F' ei ole ühendatud teiste tippudega.
# Tipp 'E' on ühendatud tippuga 'F'.