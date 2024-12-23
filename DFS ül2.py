# Define the DFS function
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    order = [start]

    for neighbor in graph[start]:
        if neighbor not in visited:
            order.extend(dfs(graph, neighbor, visited))

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

# Perform DFS on the graph starting from vertex 'A'
dfs_order = dfs(graph, 'A')

print(f"DFS traversal order starting from vertex 'A': {dfs_order}")

# Time and Space Complexity Analysis
time_complexity = "O(V + E)"  # V is the number of vertices and E is the number of edges
space_complexity = "O(V)"  # V is the number of vertices

print(f"Time Complexity: {time_complexity}")
print(f"Space Complexity: {space_complexity}")