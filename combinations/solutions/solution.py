#!/usr/local/bin/python3

i = list(map(int, input().split(" ")))
n = i[0]
k = i[1]
c = list(map(int, input().split(" ")))

l = len(c)
count = [[0 for i in range(n+1)] for j in range(l)]
for i in range(l):
    count[i][0] = 1
for i in range(0, n+1, c[0]):
    count[0][i] = 1

for i in range(1, l):
    for j in range(1, n+1):
        useJ = j - c[i]
        x = 0 if (useJ < 0) else count[i][useJ]
        count[i][j] = x + count[i-1][j]
print(count[l-1][n])
