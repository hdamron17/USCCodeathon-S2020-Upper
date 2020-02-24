#! /usr/bin/env python3

from solution import *
from sys import argv

def graphic_text(xmax, ymax, xshift, yshift, arrows, width=10):
    return r'''
\documentclass{standalone}
\usepackage{tikz}
\usetikzlibrary{automata,arrows}
\def\xmax{%s}
\def\ymax{%s}
\begin{document}
  \scalebox{%s}{\begin{tikzpicture}
    \foreach \x in {0,...,\xmax}
      \draw (\x,0) -- (\x,\ymax);
    \foreach \y in {0,...,\ymax}
      \draw (0,\y) -- (\xmax,\y);

    \begin{scope}[shift={(%s+0.5,%s+0.5)}]
      %s
    \end{scope}
  \end{tikzpicture}}
\end{document}
''' % (xmax+1, ymax+1, width/xmax, xshift, yshift, arrows)

def arrow(i, p1, p2, red=False, start=False):
    return r'''
      \node[fill,state,minimum size=0%s] (a%d) at (%d,%d) {};
      \node[fill,state,minimum size=0] (b%d) at (%d,%d) {};
      \draw[-stealth%s] (a%d) -- (b%d);
''' % (",accepting" if start else "", i, p1[0], p1[1], i, p2[0], p2[1], ",red" if red else "", i, i)

def graphic(ds):
    path = ds2path(ds)
    xshift = -min(map(lambda xy: xy[0], path))
    yshift = -min(map(lambda xy: xy[1], path))
    xmax = abs(max(map(lambda xy: xy[0], path)) + xshift)
    ymax = abs(max(map(lambda xy: xy[1], path)) + yshift)

    _, start, end = findLongestPalindromicString(path, debug=True)

    arrows = []
    for i, (p1, p2) in enumerate(zip(path, path[1:])):
        arrows.append(arrow(i, p1, p2, start <= i < end, i == 0))

    return graphic_text(xmax, ymax, xshift, yshift, "\n".join(arrows))

def png_graphic(i):
    import os
    os.system('mkdir -p tex fig')

    with open("testcases/input/input%02d.txt" % i) as f:
        _, ds = f
    tex = graphic(ds)
    ofname = "tex/input%02d.tex" % i
    with open(ofname, 'w+') as f:
        f.write(tex)

    os.system('latexmk -pdf --shell-escape -silent -synctex=1 -outdir=build "%s"' % ofname)
    os.system('convert -density 600 build/input%02d.pdf fig/input%02d.png' % (i, i))

if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: gen_graphic.py N")
        exit(1)
    i = int(argv[1])
    png_graphic(i)
