#!/usr/local/bin/python3
# Scores 23.53/100
INF = float('inf')
def getLine(func):
    return list(map(func, input().split()))

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

def dijkstras(graph, source):
    n = len(graph)
    visited = [False for i in range(n)]
    tovisit = [source]
    dist = [INF for i in range(n)]
    dist[source] = 0
    while len(tovisit) > 0:
        u = tovisit.pop()
        if (visited[u]):
            continue
        visited[u] = True
        for i in range(n):
            if graph[u][i]:
                tovisit.append(i)
                if dist[i] > graph[u][i] + dist[u]:
                    dist[i] = graph[u][i] + dist[u]
    return dist

if __name__ == "__main__":
    # Input problem
    line = getLine(int)
    n = line[0]
    m = line[1]
    k = line[2]
    nodes = getLine(str)
    edges = [getEdge() for _ in range(m)]
    path = getLine(str)


    # Make Adjacency Matrix
    graph = [[None for _ in range(n)] for _ in range(n)]
    for i in range(n):
        graph[i][i] = 0
    makeGraph(nodes, edges, graph)
    # print(graph)

    # Make precomputed Dijkstras Matrix
    #efficientGraph = [dijkstras(graph, i) for i in range(n)]
    # print(efficientGraph)

    # Calculate Costs
    cost = 0

    prev = path[0]
    cost = 0
    for next_ in path:
        i = nodes.index(prev)
        j = nodes.index(next_)
        cost += dijkstras(graph, i)[j]#efficientGraph[i][j]
        prev = next_
    print(cost)

