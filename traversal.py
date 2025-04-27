def bfs_iterative(graph, start_node):
    visited = [start_node]  # Set to track visited nodes
    queue = [start_node]  # Queue for BFS

    while queue:
        node = queue.pop(0)
        print(node, end=" ")
        # print(node," ->")
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)

# Run BFS
print("BFS Traversal:")
bfs_iterative(graph, list(graph.items())[0][0])
# without recursion
def dfs_iterative(graph, start_node):
    visited = []
    stack = [start_node]

    while stack:
        node = stack.pop()  # Remove last element (LIFO behavior)
        if node not in visited:
            print(node, end=" ")
            visited.append(node)
            stack.extend(reversed(graph[node]))  # Add neighbors (reversed for correct order)

# Run DFS
print("\nDFS Traversal (Iterative):")
dfs_iterative(graph, 'A')
