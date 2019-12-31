#! /usr/bin/env python3

import random
import string
from solution import *

samples = ["2 10 1015",
           "7 10 1015",
           "500 10 1015",
           "30 2 1111",
           "500 34 AARDVARK"]

if __name__ == "__main__":
    random.seed(42)
    for b in range(2,36):
        k = random.choice([random.randint(0, 100), int(10**random.uniform(0, 100))])
        choices = (string.digits + string.ascii_uppercase)[:b]
        n_str = "".join([random.choice(choices[1:])] + random.choices(choices, k=random.randint(1, 30)))
        samples.append("%s %s %s" % (k, b, n_str))

    assert len(samples) < 100, "Too many samples"
    for i, sample in enumerate(samples):
        ifname = "testcases/input/input%02d.txt" % i
        ofname = "testcases/output/output%02d.txt" % i

        k, b, n = sample.split()
        k = int(k)
        b = int(b)
        r = kaprekar_k(n, b, k)
        if k < 100:
            gt = kaprekar_k(n, b, k, brute=True)
            if r != gt:
                print("ERROR kaprekar_k(%s, %d, %d) failed %s != %s" % (n, b, k, r, gt))

        with open(ifname, 'w+') as ifile, open(ofname, 'w+') as ofile:
            ifile.write(sample + '\n')
            ofile.write(r + '\n')

    import os
    os.system("zip -r kaprekar-testcases.zip testcases")
