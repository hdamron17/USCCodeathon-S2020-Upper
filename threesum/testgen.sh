SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd -P)"

mkdir -p $SCRIPT_DIR/input
mkdir -p $SCRIPT_DIR/output


pushd $SCRIPT_DIR

for i in {3..5}
do
  python3 ./mkin.py 10  > input/input$i.txt
  echo $i
  python3 ./solutions/solution.py < input/input$i.txt > output/output$i.txt
done


for i in {6..9}
do
  python3 ./mkin.py 20 > input/input$i.txt
  echo $i
  python3 ./solutions/solution.py < input/input$i.txt > output/output$i.txt
done

for i in {10..14}
do
  python3 ./mkin.py 40 > input/input$i.txt
  echo $i
  python3 ./solutions/solution.py < input/input$i.txt > output/output$i.txt
done

for i in {15..19}
do
  python3 ./mkin.py 80 > input/input$i.txt
  echo $i
  python3 ./solutions/solution.py < input/input$i.txt > output/output$i.txt
done

for i in {20..25}
do
  python3 ./mkin.py 200 > input/input$i.txt
  echo $i
  python3 ./solutions/solution.py < input/input$i.txt > output/output$i.txt
done

for i in {26..30}
do
  python3 ./mkin.py 400 > input/input$i.txt
  echo $i
  python3 ./solutions/solution.py < input/input$i.txt > output/output$i.txt
done

for i in {31..35}
do
  python3 ./mkin.py 1000 > input/input$i.txt
  echo $i
  python3 ./solutions/solution.py < input/input$i.txt > output/output$i.txt
done

python3 ./mkin.py 2000 > input/input36.txt
echo "36"
python3 ./solutions/solution.py < input/input36.txt > output/output36.txt

python3 ./mkin.py 3000 > input/input37.txt
echo "37"
python3 ./solutions/solution.py < input/input37.txt > output/output37.txt
popd

rm -rf cases.zip
zip -r cases input output
