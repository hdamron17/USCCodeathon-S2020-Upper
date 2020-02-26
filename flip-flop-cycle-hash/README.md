Charles's Flip-Flop Cycle Hash
==============================

Help Charles encode a secret message to James at Texas A&M.

## Problem Statement

Charles has a secret message he wants to send to James at Texas A&M but he doesn't want anyone to know. To encrypt an integer message $n$ in base $b$ he will use the following algorithm:

1. Sort the digits from least to greatest as $n_0$
2. Sort the digits from greatest to least as $n_1$
3. Output the integer $n_1 - n_0$ still in base $b$

However, he thinks this hash isn't strong enough so he will keep doing until he is satisfied, namely $k$ times.

## Input Format

Three space separated values $k$ $b$ $n$ where $k,n$ are integers and $b$ is an alphanumeric base from either $0-9$ or $A-Z$.

## Constraints

$0 \leq k \leq 10^{100}$

$0 \leq n \leq 10^{50}$ (in base $b$)

$b$ either in $0-9$ or $A-Z$

## Output Format

Give the output of the encryption still in base $b$.

## Sample 0 Explanation

For the first iteration, the steps would go as follows:

1. $n_0 = 0115$
2. $n_1 = 5110$
3. Output $n_1 - n_0 = 5110 - 0115 = 4995$

Then the second iteration yields the output of $5355$.
