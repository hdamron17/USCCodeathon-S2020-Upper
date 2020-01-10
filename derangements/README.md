# Messy Papers

Dr. Girardi needs to grade her papers, but they keep ending up in the wrong order!
Help her give at least one student the right grade.

## Problem

Given a stack of $n$ papers, find the minimum number of tries Dr. Girardi will
need before she will be sure that at least one of the papers is in the proper
position in the stack.

## Input Format

The number of papers $n$.

## Output Format

The number of tries to be sure the papers are in the right order.

## Constraints

$1 \le n \le 50000$

### Sample Input 0
```
3
```

### Sample Output 0
```
3
```

### Explanation of Sample 0

If there are 3 papers, they can be in the following orders (assuming they are numbered from 0 to 2):
```
0 1 2
0 2 1
1 0 2
1 2 0
2 0 1
2 1 0
```

There are four orders with at least one paper in the correct place:
- 0 1 2: all the papers in the right place
- 0 2 1: 0 is in the right place
- 1 0 2: 2 is in the right place
- 2 1 0: 1 is in the right place

Since there are $6$ total orders, Dr. Girardi needs at most $6 - 4 + 1 = 3$ tries
to make sure at least one student gets the right grade.

### Sample Input 1
```
10
```

### Sample Output 1
```
1334962
```

### Explanation of Sample 1

There are $3628800$ possible orders for the papers and $2293839$ orders where at least
one of the papers is in the correct place,
so Dr. Girardi needs at most $3628800 - 2293839 + 1 = 1334962$ tries to make sure
at least one student gets the right grade.

### Sample Input 2
```
1
```

### Sample Output 2
```
1
```

### Explanation of Sample 2

If there is only 1 paper, Dr. Girardi will always give the right grade on the first try.

## Language Note

This problem requires arbitrary size integers.
In python or Haskell, these are built-in; in other languages
you may have to use libraries. See https://www.hackerrank.com/environment
for libraries available on hackerrank.

C and C++ do not have an arbitrary precision arithmetic available on Hackerrank
and has been disabled for this challenge. If you want to use a typed language
I recommend Java (using BigInteger) or Rust (using `num`).
