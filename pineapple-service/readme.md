# Kenny's Pineapple Delivery

Kenny has hired you to start a new exciting business, delivering pineapples across college campuses across the nation. However, you must do so using top secret bike routes.

## Description

Given a network of bike routes that Kenny likes, give the minimum distance between each of the deliveries in the order Kenny decided.

## Input

You will be given first the number of destinations, `n`, the number of roads connecting two destinations, `m`. The destinations will be given names listed after n and m. Following this, the roads will be listed by the two destinations it connects and its distance. Finally Kenny will give you the route he wants you to take, it is imperative you take the route in order, as Kenny will need you to pick up and drop off things in that order. The number of destinations Kenny wants you to go to is, `k`.

Note, it is not guaranteed that A->B will be the same time as B->A. Sometimes you have to get through an obstacle only one way such as a hill.

```
n m k
N_1 N_2 N_3 ... N_n
N_a N_b dist_ab
.
.
.
N_i N_j ...
```

## Constraints

$$ 2 \leq n \leq 250 $$
$$ 1 \leq m \leq 31250 $$
$$1\leq k \leq 1000000 $$ 
$$ 1 \leq dist_ij \leq 100 $$
## Output

Print the minimum distance you need to travel to go between all routes.

## Sample Input 1

```
3 3 3
Columbia_Hall Preston Rusell_House
Columbia_Hall Preston 11
Columbia_Hall Rusell_House 9
Preston Rusell_House 8
Columbia_Hall Preston Rusell_House
```

### Explanation

In this example, we are trying to go from Columbia Hall to Preston to Rusell House. In order we get 19. From Columbia Hall to Preston it is 11, from Preston to Rusell House it is 8. 

## Sample Output 1

```
19
```
