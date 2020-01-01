SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd -P)"

mkdir -p $SCRIPT_DIR/input
mkdir -p $SCRIPT_DIR/output


pushd $SCRIPT_DIR

  for i in {8..14} {16..35}
  do
    python3 ./mkin2.py > input/input$i.txt;
    echo $i
  done

  for i in {0..35}
  do
    echo $i
    python3 ./solutions/solution.py < input/input$i.txt > output/output$i.txt
  done
popd

rm -rf cases.zip
zip -r cases input output
