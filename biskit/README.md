Biskit's Cornfield Catastrophe
==============================

Biskit keeps getting lost in a corn maze and sometimes has to retrace his steps. Determine the longest path he had to retrace.

## Problem Statement

You are given Biskit's path through the maze as described by the string $C$. Each character is an action taken by Biskit:

* 'f' moves Biskit forward one foot
* 'r' turns Biskit 90 degrees right (clockwise)
* 'l' turns Biskit 90 degrees left (counterclockwise)

If Biskit moves along a certain path (length $l$) then turns around and follows the same path back to his starting spot (considering positions only, not the rotations taken) at any point during his navigation of the maze, this is a retrace of length $l$.

Find the length of the longest path Biskit retraces while he is wandering through the cornfield.

## Input Format

The first line contains a single integer $n$. The second line contains an $n$-length string $C$ composed only of 'f', 'r', and 'l'.

## Constraints

$0 < n < 10^6$

## Output Format

Output a single integer, the length of the longest path retraced (including the position at which Biskit turns).

## Sample 0 Explanation

Starting at the double circle, this is the path taken by Biskit.

![image](https://s3.amazonaws.com/hr-assets/0/1582569829-cc7f844728-input00.png)

## Sample 1 Explanation

![image](https://s3.amazonaws.com/hr-assets/0/1582569879-8f4b912ca5-input01.png)

## Sample 2 Explanation

Biskit does not retrace his steps at all. Trivially, each step can be considered a retrace of length 1.

![image](https://s3.amazonaws.com/hr-assets/0/1582570020-b978695089-input02.png)
