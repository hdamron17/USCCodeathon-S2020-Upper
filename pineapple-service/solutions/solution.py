#!/usr/local/bin/python3

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
    q = [i for i in range(n)]
    dist = [INF for _ in range(n)]
    dist[source] = 0
    while False in q:
        # Get minimum dist source -> u
        min_ = INF
        u = -1
        for node in q:
            if dist[node] < min_:
                min_ = dist[node]
                u = node
        if u == -1: break # Dead path
        q.remove(u)
        for node in q:
            if graph[u][node] != None:
                alt = dist[u] + graph[u][node]
                if alt < dist[node]:
                    dist[node] = alt
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
    makeGraph(nodes, edges, graph)

    # Make precomputed Dijkstras Matrix
    efficientGraph = [dijkstras(graph, i) for i in range(n)]

    # Calculate Costs
    cost = 0

    prev = path[0]
    cost = 0
    for next_ in path:
        i = nodes.index(prev)
        j = nodes.index(next_)
        cost += efficientGraph[i][j]
        prev = next_
    print(cost)
