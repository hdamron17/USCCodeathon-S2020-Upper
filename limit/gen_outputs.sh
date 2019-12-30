#! /bin/bash
set -e

for ifile in testcases/input/input*.txt; do
  ofile="${ifile//input/output}"
  gt="$(python sympy-solution.py < $ifile)"
  r="$(python solution.py < $ifile)"
  success="$(python -c "print(int(abs($r - $gt) < 1e-6))")"
  if [ "$success" -eq 0 ]; then
    echo "ERROR in $(basename $ifile .txt): abs($gt - $r) >= 1e-6"
    continue
  fi
  echo "$gt" > $ofile
done

zip -r limit-testcases.zip testcases
