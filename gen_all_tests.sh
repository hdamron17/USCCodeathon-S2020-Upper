#!/usr/bin/env bash

CASES=0

mkdir -p input

# boundary cases to make sure people have the right idea
for i in `seq 1 9`; do
	./gen_testcase.sh $CASES $i
	CASES=$((CASES + 1))
done

# make sure it's not hard-coded
for _ in `seq 1 10`; do
	# between 10 and 100
	./gen_testcase.sh $CASES $((RANDOM % 90 + 10))
	CASES=$((CASES + 1))
done

# at this point the slow solutions will start timing out
for _ in `seq 1 10`; do
	# between 100 and 10000
	./gen_testcase.sh $CASES $((RANDOM % 9900 + 100))
	CASES=$((CASES + 1))
done

# at this point you really do need a fast solution
for _ in `seq 1 10`; do
	# between 10000 and 50000
	./gen_testcase.sh $CASES $((RANDOM % 40000 + 10000))
	CASES=$((CASES + 1))
done

# even with a fast solution, this will take several seconds
./gen_testcase.sh $CASES 50000
