#!/usr/local/bin/python3
import random, string, sys


def randString():
    l = 10
    return ''.join([random.choice(string.ascii_letters + string.digits) for n in range(l)])

n = random.randint(5,150) if len(sys.argv) < 2 else int(sys.argv[1])
k = random.randint(2,100000) if len(sys.argv) < 3 else int(sys.argv[2])

graph = [[0 if i == j else None for i in range(n)] for j in range(n)]

def connected(graph, n):
    visited = [0]
    unvisited = [i for i in range(1, n)]
    while len(unvisited) > 0:
        for end in unvisited:
            found = False
            for start in visited:
                if graph[start][end] and graph[end][start]:
                    visited.append(end)
                    unvisited.remove(end)
                    found = True
                    break
            if not found:
                return False
            break
    return True

while not connected(graph, n):
    i = random.randint(0, n-1)
    j = i
    while j == i:
        j = random.randint(0, n-1)
    graph[i][j] = random.randint(0,100)
    graph[j][i] = random.randint(0,100)

nodes = [randString() for _ in range(n)]
path = [nodes[random.randint(0,n-1)] for _ in range(k)]

edges = []
for i in range(n):
    for j in range(n):
        if graph[i][j] and graph[i][j] > 0:
            edges.append((nodes[i], nodes[j], graph[i][j]))

print("{} {} {}".format(n, len(edges), k))
print(" ".join(nodes))
random.shuffle(edges)
for edge in edges:
    print("{} {} {}".format(edge[0], edge[1], edge[2]))
print(" ".join(path))
