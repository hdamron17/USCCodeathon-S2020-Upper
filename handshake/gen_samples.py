#! /usr/bin/env python3

import random
import os
from solution import *

samples = ["4 2",
           "9 4"]

if __name__ == "__main__":
    random.seed(42)
    for i in range(20):
        m = random.choice(range(1,1<<(i+10)))
        # TODO if we can lower uppwer bound, then avg should be able to go above 1
        n = random.choices([m*2, random.randint(m*2, min(m*10, 10**12-1))], [1,20])[0]
        samples.append("%d %d" % (n, m))

    assert len(samples) < 100, "Too many samples"
    for i, sample in enumerate(samples):
        ifname = "testcases/input/input%02d.txt" % i
        ofname = "testcases/output/output%02d.txt" % i

        n, m = (int(x) for x in sample.split())
        r = solve(n, m)
        print("%d %d -> %s" % (n, m, r))
        # TODO add brute force for small inputs

        os.system("mkdir -p testcases/input testcases/output")
        with open(ifname, 'w+') as ifile, open(ofname, 'w+') as ofile:
            ifile.write("%s\n" % sample)
            ofile.write(str(r) + '\n')

    os.system("zip -r handshake-testcases.zip testcases")
