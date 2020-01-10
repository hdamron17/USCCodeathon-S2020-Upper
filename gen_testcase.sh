#!/bin/sh
# modified from Charles' generate_testcase.sh
# https://github.com/z2oh/usc_lowerdivision_spring2018/blob/master/image_rotate/testcases/generate_testcase.sh

set -eu

# make sure we are in the test case directory
cd "$(dirname "$0")"

if [ $# -ne 2 ] ; then
	echo "USAGE: $0 <test case number> <n>"
	exit 1
fi

is_number() {
	case "$1" in
		''|*[!0-9]*) return 1;;
		*) return 0;;
	esac
}

if ! is_number "$1" && is_number "$2"; then
	echo "test number and input must be integers"
	exit 2
fi

mkdir -p input output
INPUT_FILE="./input/input$1.txt"
OUTPUT_FILE="./output/output$1.txt"

if [ -e "$INPUT_FILE" ] || [ -e "$OUTPUT_FILE" ]; then
	echo "ERROR: '$INPUT_FILE' or '$OUTPUT_FILE' exists"
	printf "Overwrite? y/[n] "
	read -r force
	[ "$force" = y ] && rm -f "$INPUT_FILE" "$OUTPUT_FILE" || exit 1
fi

echo "$2" > "$INPUT_FILE"
solutions/solution < "$INPUT_FILE" > "$OUTPUT_FILE"
