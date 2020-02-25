# Conference in Kalingrad Problem
# Hunter Damron 2020

# Obverse that all edges are unique because each quadratic residue up to p/2 is unique
# x^2 == 0 only for x=0
# Both x == 2x and x == 4x occur only at x=0
# Since there are m integers from 1 to m, there are exactly m edges
# We know the number of vertices so the handshake lemma says the sum of vertex degrees is 2m
# Then for an average degree, we get 2m/n

# Note: This problem is named after Euler's Bridges of Königsberg (now Kalingrad) which presented the Handshake Lemma

def solve(n, m):
    return 2*m/n

def brute_force(n, m):
    pass  #TODO

if __name__ == "__main__":
    n, m = (int(x) for x in input().split())

    print(solve(n, m))  # By Handshake Lemma
