from graphviz import Graph
from sys import argv
import os

# g = Graph()
# g.attr('node', shape='circle', fixedsize='true', width='0.5')
# g.node('1')
# g.node('2')
# g.edge('1','2')
# g.view()

p = 2**31-1

def graphic(i):
    os.system('mkdir -p fig')

    with open("testcases/input/input%02d.txt" % i) as f:
        n, m = (int(x) for x in next(f).split())

    g = Graph()
    g.attr('node', shape='circle', fixedsize='true', width='0.4')

    nodes = {x*x % p for x in range(1,m+1)}
    nodes.update({2*x % p for x in nodes})
    for node in sorted(nodes):
        g.node('%d' % node)

    for x in range(1,m+1):
        g.edge('%d' % (x*x % p), '%d' % (2*x*x % p))

    g.attr('node', shape='circle', fixedsize='true', width='0.1')
    print(n)
    for x in range(n - len(nodes)):
        g.node('u%d' % x, '')

    g.render("fig/input%02d" % i, format="pdf", cleanup=True)

if __name__ == "__main__":
    i = int(argv[1]) if len(argv) > 1 else 0  # Default to 0
    graphic(i)
