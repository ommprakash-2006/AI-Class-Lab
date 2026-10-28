from collections import deque

def water_jug(a, b, target):
    q = deque([(0, 0)])
    visited = {(0, 0)}
    parent = {}

    while q:
        x, y = q.popleft()

        if x == target or y == target:
            path = []
            while (x, y) != (0, 0):
                path.append((x, y))
                x, y = parent[(x, y)]
            path.append((0, 0))
            return path[::-1]

        states = [
            (a, y), (x, b),       # Fill
            (0, y), (x, 0),       # Empty
            (max(0, x-(b-y)), min(b, x+y)),
            (min(a, x+y), max(0, y-(a-x)))
        ]

        for s in states:
            if s not in visited:
                visited.add(s)
                parent[s] = (x, y)
                q.append(s)

a = int(input("Capacity of Jug 1: "))
b = int(input("Capacity of Jug 2: "))
target = int(input("Target: "))

path = water_jug(a, b, target)

for step in path:
    print(step)
