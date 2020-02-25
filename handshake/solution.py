# Conference in Kalingrad Problem
# Hunter Damron 2020

# Note: This problem is named after Euler's Bridges of Königsberg (now Kalingrad) which presented the Handshake Lemma

def solve(n, m):
    return 2*m/n  # By Handshake Lemma

def brute_force(n, m, edges):
    adj = {}

    def set_adj(adj, p1, p2):
        if p1 not in adj:
            adj[p1] = [p2]
        else:
            adj[p1].append(p2)

    for p1, p2 in edges:
        set_adj(adj, p1, p2)
        set_adj(adj, p2, p1)
    degrees = map(len, adj.values())
    return sum(degrees) / n

if __name__ == "__main__":
    n, m = (int(x) for x in input().split())
    print(solve(n, m))

    # edges = [input().strip().split(" and ") for _ in range(m)]
    # print(brute_force(n, m, edges))
