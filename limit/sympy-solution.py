#! /usr/bin/env python3

from sympy.solvers import solve
from sympy import Symbol, And, Or, Eq, diff, lambdify
from sympy.plotting import plot, plot_implicit

def max_interval(A, B, C, D, y, eps, show=False):
    x = Symbol('x', real=True)
    fx = A*x**3 + B*x**2 + C*x + D
    intervals = solve(abs(fx - y) < eps)

    xranges = []
    diffs = []
    for interval in intervals.args if type(intervals) is Or else [intervals]:
        lhs, rhs = interval.args
        lb = lhs.lts
        ub = rhs.gts
        xranges.append((lb, ub))
        diffs.append((ub - lb))
    maxdiff = max(diffs)

    if show:
        min_x = min(b[0] for b in xranges)
        max_x = max(b[1] for b in xranges)
        adj = 0.1 * (max_x - min_x)
        min_x = min_x - adj
        max_x = max_x + adj

        dfx = diff(fx, x)
        extrema = solve(dfx)
        x_candidates = [min_x, max_x] + list(filter(lambda x: min_x < x < max_x, extrema))
        y_candidates = list(map(lambdify(x, fx), x_candidates))
        min_y = min(y_candidates)
        max_y = max(y_candidates)
        adj = 0.1 * (max_y - min_y)
        min_y = min_y - adj
        max_y = max_y + adj
        xlim = (min_x, max_x)
        ylim = (min_y, max_y)

        p = plot(fx, show=False, xlim=xlim, ylim=ylim, adaptive=False, nb_of_points=1000)
        p.append(plot(y, show=False, xlim=xlim, ylim=ylim, line_color='r')[0])
        p.append(plot(y-eps, show=False, xlim=xlim, ylim=ylim, line_color='lightsalmon', markers=['.'])[0])
        p.append(plot(y+eps, show=False, xlim=xlim, ylim=ylim, line_color='lightsalmon', markers=['.'])[0])
        for d, (lb, ub) in zip(diffs, xranges):
            p.append(plot_implicit(Eq(x, lb), show=False, xlim=xlim, ylim=ylim)[0])
            p.append(plot_implicit(Eq(x, ub), show=False, xlim=xlim, ylim=ylim)[0])
        print("  ".join(str(x) for x in diffs))
        p.show()

    return maxdiff

if __name__ == "__main__":
    A, B, C, D, y, eps = map(float, input().split())
    print(max_interval(A, B, C, D, y, eps, show=False))
