from solution import *

if __name__ == "__main__":
    k, b, n = input().split()
    k = int(k)
    b = int(b)
    gt = kaprekar_k(n, b, k, brute=True)
    r = kaprekar_k(n, b, k)

    if gt != r:
        print("ERROR kaprekar_k(%s, %d, %d) failed %s != %s" % (n, b, k, r, gt))
        exit(1)
