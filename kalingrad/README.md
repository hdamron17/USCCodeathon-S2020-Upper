Conference in Kalingrad
=======================

Determine the number of collaborations between researchers at the 2012 ICCS conference in Kalingrad, Russia.

## Problem Statement

In 2012, the International Conference on Cognitive Science was held in Kalingrad, Russia, and one researcher noticed that many researchers at the conference were authors on several papers, and he wants to know how many papers each researcher presented, on average. He observed the following:

* There were $n$ authors and $m$ papers.
* Every paper had exactly two authors present at the conference.
* Not all researchers presented papers.

## Input Format

The first line contains two space separated integers $n m$.
The following $m$ lines each contain a paper's author list: "(Person 1) and (Person 2)".

## Constraints

$0 < n,m < 2^{30}$.

$n$ is at least as large as the number of researchers presenting papers.

## Output Format

Output the average numbers of papers presented by each researcher. An error allowance will be made for floating point calculations.

## Sample 0 Explanation

Each author has exactly one paper so the average is 1

![image](https://s3.amazonaws.com/hr-assets/0/1582604423-9f23172ce3-input00.png)

## Sample 1 Explanation

The number of papers are as follows:

* Rekleitis: 1
* Cooper: 2
* Erdos: 3
* Czabarka: 2
* Szekely: 2
* (Unnamed): 0

The average is $$ \frac{1+2+3+2+2+0}{6} = \frac{10}{6} = \frac{5}{3} = 1.66\dots $$

![image](https://s3.amazonaws.com/hr-assets/0/1582604462-534c4de774-input01.png)

## Sample 2 Explanation

A large and not very informative graph of the collaborations:

![image](https://s3.amazonaws.com/hr-assets/0/1582604626-fe0624ba8b-input02.png)
