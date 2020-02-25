from graphviz import Graph
from sys import argv
import os

def graphic(i):
    os.system('mkdir -p fig')

    with open("testcases/input/input%02d.txt" % i) as f:
        n, m = (int(x) for x in next(f).split())
        edges = [next(f).strip().split(" and ") for _ in range(m)]

    g = Graph()

    nodes = {e[0] for e in edges}.union({e[1] for e in edges})
    for node in sorted(nodes):
        g.node(node)

    for p1, p2 in edges:
        g.edge(p1, p2)

    g.attr('node', shape='circle', fixedsize='true', width='0.3')
    for x in range(n - len(nodes)):
        g.node('_%d' % x, '')

    g.render('build/input%02d' % i, format='pdf', cleanup=True)
    os.system('convert -density 600 build/input%02d.pdf fig/input%02d.png' % (i, i))

if __name__ == "__main__":
    i = int(argv[1]) if len(argv) > 1 else 0  # Default to 0
    graphic(i)
