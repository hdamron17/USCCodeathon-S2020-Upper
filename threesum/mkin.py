from random import randint
import sys
from math import sqrt

n = int(sys.argv[1])
n = randint(n-int(sqrt(n)), n + int(sqrt(n)))

s = [str(randint(- int(n), int(n))) for _ in range(n)]
x = int(randint(-int(sqrt(n)), int(sqrt(n))))

print(n)
print(x)
print(" ".join(s))

