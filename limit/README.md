Take it to the Limit
====================

Maximize input range for cubic equation with given error.

## Problem Statement

Determine which values of $x$ satisfy the equation $y = Ax^3 + Bx^2 + Cx + D$ with error at most $\varepsilon$ (i.e. $\left| (Ax^3 + Bx^2 + Cx + D) - y \right| \leq \varepsilon$). Then calculate the length of the largest interval for which all $x$ in the interval satisfy the equation.

## Input Format

One line of input with space separated real numbers $A$, $B$, $C$, $D$, $y$, $\varepsilon$.

## Constraints

$0 < A \leq 100$

$0 \leq B, C, D \leq 100$

$0.001 \leq \varepsilon \leq 1$

The values $y -\varepsilon$ and $y +\varepsilon$ will not be near any local extrema of $f(x)$ (to avoid any precision errors).

## Output Format

Report the length of the largest interval such that every $x$ in the interval satisfies the equation with error at most $\varepsilon$. To account for floating point error, an error allowance of $10^{-6}$ is given.

## Sample 0 Explanation

![image](https://s3.amazonaws.com/hr-assets/0/1577727181-3a352d1496-sample00.png)

There are three intervals (blue) on the $x$-axis for which $f(x) \approx 1$ with error at most $0.5$. The longest of the intervals has length $0.214003$
