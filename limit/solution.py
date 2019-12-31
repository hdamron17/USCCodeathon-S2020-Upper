#! /usr/bin/env python3

from math import isclose
from cmath import sqrt

def max_interval(A, B, C, D, y, eps):
    f = lambda x: A*x*x*x + B*x*x + C*x + D
    critical_points = sorted(cubic_formula(A, B, C, D-y+eps) + cubic_formula(A, B, C, D-y-eps))
    interior_check_points = [(l+u)/2 for l, u in zip(critical_points, critical_points[1:])]
    check_points = [critical_points[0] - 1] + interior_check_points + [critical_points[-1] + 1]
    checks = [abs(f(x) - y) < eps for x in check_points]
    lbs = [x for i, x in enumerate(critical_points) if checks[i+1] and not checks[i]]
    ubs = [x for i, x in enumerate(critical_points) if checks[i] and not checks[i+1]]
    return max(ub - lb for lb, ub in zip(lbs, ubs))

def determinant(A, B, C, D):
    return 18*A*B*C*D - 4*B*B*B*D + B*B*C*C - 4*A*C*C*C - 27*A*A*D*D

def num_zeros(A, B, C, D):
    # Determines number of real zeros by looking at discriminant
    det = determinant(A, B, C, D)
    if isclose(D, 0):
        print("WARN: cubic with repeated solution")
        return 3
    elif det > 0:
        return 3
    else:
        return 1

def cubic_formula(A, B, C, D):
    # Cubic formula as stated by https://en.wikipedia.org/wiki/Cubic_equation
    D_0 = B*B - 3*A*C
    D_1 = 2*B*B*B - 9*A*B*C + 27*A*A*D
    sqrt_term = sqrt(D_1*D_1 - 4*D_0*D_0*D_0)
    c = ((D_1 + sqrt_term)/2)**(1./3)
    if isclose(c.real, 0) and isclose(c.imag, 0):
        c = ((D_1 - sqrt_term)/2)**(1./3)
    xi = (-1 + sqrt(-3)) / 2
    xs = [-1/(3*A) * (B + xi**k * c + D_0/(xi**k * c)) for k in range(3)]
    xs.sort(key=lambda c: abs(c.imag))
    n = num_zeros(A, B, C, D)
    xs = list(map(lambda c: c.real, xs[:n]))
    return xs

if __name__ == "__main__":
    A, B, C, D, y, eps = map(float, input().split())
    print(max_interval(A, B, C, D, y, eps))
