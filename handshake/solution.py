# Conference in Kalingrad Problem
# Hunter Damron 2020

# Note: This problem is named after Euler's Bridges of Königsberg (now Kalingrad) which presented the Handshake Lemma

def solve(n, m):
    return 2*m/n  # By Handshake Lemma

def brute_force(n, m, edges):
    pass  # TODO

if __name__ == "__main__":
    n, m = (int(x) for x in input().split())

    print(solve(n, m))
