#!/usr/local/bin/python3
import random,string,sys
from solutions.solution import dijkstras, INF
from random import randint, random, shuffle
import random

def randString():
    l = 10
    return ''.join([random.choice(string.ascii_letters + string.digits) for n in range(l)])

def randWeight(min_, max_):
    k = 0.5
    if random.random() < k:
        return randint(min_, max_)
    return None

def completeDijkstras(graph, n):
    return [dijkstras(graph, i) for i in range(n)]


n = randint(150, 250) if len(sys.argv) < 2 else int(sys.argv[1])
k = randint(20000, 100000) if len(sys.argv) < 3 else int(sys.argv[2])

graph = [[randWeight(1, 100) if i != j else 0 for i in range(n)] for j in range(n)]

# merge with a tree
tree = [i for i in range(n)]
shuffle(tree)
tree = tree + [tree[0]]
prev = tree[0]
for next_ in tree:
    if not graph[prev][next_] == None:
        graph[prev][next_] = randint(50,100)
    if not graph[prev][next_] == None:
        graph[next_][prev] = randint(50,100)
    prev = next_

for i in range(n):
    graph[i][i] = 0

# print([dijkstras(graph, i) for i in range(n)])

nodes = [randString() for i in range(n)]

path = [randint(0,n-1) for _ in range(k)]

# print(graph)

edges = []
for i in range(n):
    for j in range(n):
        if graph[i][j] and graph[i][j] > 0:
            edges.append((nodes[i], nodes[j], graph[i][j]))

path = [nodes[randint(0,n-1)] for _ in range(k)]

print("{} {} {}".format(n, len(edges), k))
print(" ".join(nodes))
shuffle(edges)
for edge in edges:
    print("{} {} {}".format(edge[0], edge[1], edge[2]))
print(" ".join(path))
