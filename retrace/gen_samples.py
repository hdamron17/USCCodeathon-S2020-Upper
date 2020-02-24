#! /usr/bin/env python3

import random
import time
from solution import *

samples = ["fffrffllfflfrf",
           "frflffrrfflffrfrfff",
           "ffffffffrffffffrff"]

def randomturns(weight, n=4, straight=True):
    rturns = random.choices([0, random.randint(1,n)], [1,weight])[0]
    randomrl = random.getrandbits(1)
    startrl = 'r' if randomrl else 'l'
    endrl = ('l' if randomrl else 'r') if straight else ''
    return ''.join([startrl * rturns, endrl * (rturns % 4)])

reverse_dict = {'r': 'l', 'l': 'r', 'f': 'f'}

def swap_turns(path):
    l = list(path)
    for j, c in enumerate(l):
        if c in "rl" and random.choices([True, False], [1,2])[0]:
            l[j] = reverse_dict[c] * 3
    return ''.join(l)

if __name__ == "__main__":
    random.seed(42)
    for x in range(3,18):
        maxlen = 2<<x
        dir_weights = [random.randint(5,20), random.randint(1,10), random.randint(1,10)]
        baselen = random.randint(1,maxlen>>2)
        n = random.randint(1, baselen<<1)
        noffshoots = random.randint(1, min(baselen-1, (maxlen - baselen) // n))
        offshoots = random.sample(range(baselen), noffshoots)
        maxoffshoot = random.choice(offshoots)
        offshoots = set(offshoots)  # For optimized containment
        ds = []
        for i in range(baselen):
            if i in offshoots:
                offshootlen = n if i == maxoffshoot else random.randint(1, n)
                offshoot = []
                for _ in range(offshootlen):
                    offshoot.append('f')
                    offshoot.append(randomturns(3, 2, False))
                offshoot_str = ''.join(offshoot)
                retrace = list(map(lambda c: reverse_dict[c], reversed(offshoot_str)))
                offshoot_str = swap_turns(offshoot_str)
                retrace_str = swap_turns(''.join(retrace))

                ds.append(offshoot_str)
                ds.append(random.choice(["rr", "ll"]))
                ds.append(retrace_str)
            ds.append(random.choices("frl", dir_weights)[0])
            ds.append(randomturns(0.1, 8))
        samples.append(''.join(ds))

    assert len(samples) < 100, "Too many samples"
    print("Max length %d" % max(map(len, samples)))
    for i, sample in enumerate(samples):
        ifname = "testcases/input/input%02d.txt" % i
        ofname = "testcases/output/output%02d.txt" % i

        t0 = time.time()
        r = solve(sample)
        t1 = time.time()
        print("Sample %0d (length %d -> %d) in %.6f seconds" % (i, len(sample), r, t1 - t0))
        # TODO add brute force for small inputs

        with open(ifname, 'w+') as ifile, open(ofname, 'w+') as ofile:
            ifile.write("%d\n%s\n" % (len(sample), sample))
            ofile.write(str(r) + '\n')

    import os
    os.system("zip -r retrace-testcases.zip testcases")
