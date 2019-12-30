#!/usr/local/bin/python3

i = list(map(int, input().split(" ")))
n = i[0]
k = i[1]
l = list(map(int, input().split(" ")))

counts = [-1 for i in range(n + 1)]
counts[0] = 0

i = 1
while (i <= n):
    j = 0
    while (j < len(l)):
        useJ = i - l[j]
        if (useJ >= 0):
            if (counts[i] == -1 and counts[useJ] != -1):
                counts[i] = counts[useJ] + 1
            elif (counts[useJ] != -1):
                counts[i] = min(counts[useJ] + 1, counts[i])
        j += 1
    i += 1
print(counts[-1])
