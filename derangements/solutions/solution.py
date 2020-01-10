#!/usr/bin/env python

def derangements(n):
    acc = 1
    correction = -1
    for i in range(1, n+1):
        acc = acc*i + correction
        correction = -correction
    return acc

def tries(n):
    if n == 0:
        return 0
    return derangements(n) + 1

if __name__ == '__main__':
    print(tries(int(input())))
