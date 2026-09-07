def dfs(graph, node, visited):
    visited.add(node)
    print(node, end=" ")

    for i in graph[node]:
        if i not in visited:
            dfs(graph, i, visited)

# Input
graph = {}
n = int(input("Enter number of vertices: "))

for i in range(n):
    v = input("Vertex: ")
    graph[v] = input("Neighbors: ").split()

start = input("Starting vertex: ")

print("DFS Traversal:")
dfs(graph, start, set())
