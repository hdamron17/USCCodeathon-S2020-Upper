#!/usr/local/bin/python3

def getLine(func):
    return list(map(func, input().split()))

def copyList(listy):
    return [listy[i] for i in range(len(listy))]

def getEdge():
    l = input().split()
    na = l[0]
    nb = l[1]
    dist = int(l[2])
    return (na, nb, dist)

def makeGraph(nodes, edges, graph):
    for edge in edges:
        na = nodes.index(edge[0])
        nb = nodes.index(edge[1])
        graph[na][nb] = edge[2]
    return

def dijkstras(visited, distance, start, current, goal):
    pass

line = getLine(int)
n = line[0]
m = line[1]
k = line[2]
nodes = getLine(str)
edges = [getEdge() for _ in range(m)]
path = getLine(str)


graph = [[None for _ in range(n)] for _ in range(n)]
makeGraph(nodes, edges, graph)
print(nodes)
print(edges)
print(path)
print(graph)
