#! /usr/bin/env python3

import random
import os
from math import floor, ceil, sqrt
from solution import *

samples = [(4, ["J. Cooper and E. Czabarka", "L. Szekely and P. Erdos"]),
           (6, ["L. Szekely and E. Czabarka", "L. Szekely and P. Erdos", "J. Cooper and P. Erdos", "E. Czabarka and P. Erdos", "J. Cooper and I. Rekleitis"])]

def triangular_index(n, k):
    # https://stackoverflow.com/a/27088560
    i = n - 2 - floor(sqrt(-8*k + 4*n*(n-1)-7)/2.0 - 0.5)
    j = k + i + 1 - n*(n-1)//2 + (n-i)*((n-i)-1)//2
    return (i,j)

if __name__ == "__main__":
    random.seed(42)
    for i in range(5):
        if i == 0:
            m = random.randint(1,50)
        else:
            m = random.choice(range(1,1<<(i+20)))
        min_n = 1 + ceil(sqrt(2*m))
        n = random.randint(min_n, 10*m)
        max_i = n * (n-1) // 2
        edges_i = random.sample(range(max_i), m)
        ijs = [triangular_index(n, k) for k in edges_i]
        edges = ["%d Smith and %d Johnson" % ij for ij in ijs]
        samples.append((n, edges))

    assert len(samples) < 100, "Too many samples"
    for i, sample in enumerate(samples):
        ifname = "testcases/input/input%02d.txt" % i
        ofname = "testcases/output/output%02d.txt" % i

        n, edges = sample
        r = solve(n, len(edges))
        print("%d %d -> %s" % (n, len(edges), r))
        # TODO add brute force for small inputs

        os.system("mkdir -p testcases/input testcases/output")
        with open(ifname, 'w+') as ifile, open(ofname, 'w+') as ofile:
            ifile.write("%d %d\n%s\n" % (n, len(edges), "\n".join(edges)))
            ofile.write(str(r) + '\n')

    os.system("zip -r handshake-testcases.zip testcases")
