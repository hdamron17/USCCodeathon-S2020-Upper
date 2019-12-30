# Lego Levels

You have come up with a design for the new dorms to be built at USC. However to save costs, the buildings will be made of legos. The issue they ran into, is it would take the student builders too long to get the correct lengths. So they asked you to write a program to solve it.

## Description

Given a length for a row of legos, solve how the minimum number of legos it will take to build this row of length n.

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

Print the minimum number of legos needed to create a length $n$ row of legos. If the combination is not possible print `-1`.

## Sample Input 1

```
16
1 3 5
```

### Explanation

In this example, we are trying to build a row of 16 legos with legos of lengths 1, 3, and 5. The minimum in this example is 16. The solution is `3 x 5 + 1 x 1`. 3 legos of length 5, and 1 lego of length 1.

## Sample Output 1

```
4
```

## Sample Input 2

```
30 2
4 25
```

### Explanation

In this example, we are trying to build a row of 30 with legos of length 4, and 25. There does not exist a combination of 4s and 25 that add up to 30, thus it is impossible, we ouput `-1`.

## Sample Output 2

```
-1
```
