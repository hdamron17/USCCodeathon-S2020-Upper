#!/usr/local/bin/python3

from random import randint

n = randint(50,1000)
k = randint(15, 25)
l = [randint(1,100) for i in range(k)]
print("{} {}".format(n, k))
print(" ".join(list(map(str, l))))
