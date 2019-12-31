# Lego Combinations

You are in charge of distributing legos for projects. However you need to know all the combinations of legos that can be made from a certain combination of lego lengths.

## Description

Given a length `n`, find the number of combinations of `l_0 l_1 l_2 ... l_k` that will combine to make length bricks of `n`.

## Input

You will be given a desired length, and the lengths of available legos. There is no maximum of legos you can use, as the supplies have not yet been bought.

```
n k
l_1 l_2 l_3 ... l_k
```

## Constraints

$$ 0 \leq n \leq 1000 $$
$$ 0 < l_i \leq 100 $$
$$ 0 < k \leq 25 $$

## Output

Print the total number of combinations of legos that create a length $n$ row of legos. It is guaranteed there is at least one combination that add up to n(the empty set is a combination).

## Sample Input 1

```
8 3
1 3 5
```

### Explanation

In this example, we are trying to build a row of 16 legos with legos of lengths 1, 3, and 5. The combinations that can be made are:  

```
{1,1,1,1,1,1,1,1}
{1,1,1,1,1,3}
{1,1,1,5}
{1,1,3,3}
{3,5}
```

## Sample Output 1

```
5
```
