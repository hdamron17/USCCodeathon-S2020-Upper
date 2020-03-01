# Three Parent Life

It is the year 2170, and humankind has now ventured all the way to the edges of the galaxy. One such planet only a few light minutes away from Betelgeuse, has a very different kind of life. This life has 3 parents.

## Description

Your mission will be to figure out how many unique combinations of parental DNA(not necessarily parents) are there that can result in this child's DNA. Scientists have come up with some fancy math. A child's DNA's xeno number is equal to the product of all 3 parents. The xeno number is the number of xenos in DNA. Let a child's xeno number be $X$, and the parents be $A$, $B$, $C$. Dealing with xenos numbers is extremely hard, luckily, in base $\chi$, they are always an integer.

$$\chi^X = \chi^A\cdot\chi^B\cdot\chi^C$$

You will be given only integers, calculate the number of unique combinations of $A,B,C$ that can be parents of the child.

$\chi$ is a number from the future, unfortunately you do not know this number, but fortunately you do remember some ancient algebra 2 trick.

## Input

You will be given the number of potential parents $n$, the child's xeno number $x$, and a list of $i$s that are xenos numbers of the parents.


```
n
x
i_1 i_2 i_3 \dots i_n
```

## Constraints

$$3 \leq n \leq 3000$$
$$-3000 \leq x, i \leq 3000$$

## Output

Print the number of unique combinations of xenos number that can result in the child's xeno number.

## Sample Input 1

```
7
0
-2 1 -1 2 0 1 -1
```

### Explanation

There are only 4 unique solutions\\
$$\chi^0=\chi^{-1}\cdot\chi^{2}\cdot\chi^{-1}$$
$$\chi^0=\chi^{-1}\cdot\chi^{1}\cdot\chi^{0}$$
$$\chi^0=\chi^{1}\cdot\chi^{1}\cdot\chi^{-2}$$
$$\chi^0=\chi^{0}\cdot\chi^{-2}\cdot\chi^{2}$$

## Sample Output 1

```
4
```
