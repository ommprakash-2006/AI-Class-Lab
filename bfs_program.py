from collections import deque

def bfs(graph, start):
    visited = {start}
    queue = deque([start])

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Input
graph = {}
n = int(input("Enter number of vertices: "))

for i in range(n):
    v = input("Vertex: ")
    graph[v] = input("Neighbors: ").split()

start = input("Starting vertex: ")

print("BFS Traversal:")
bfs(graph, start)
