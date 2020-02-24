#! /usr/bin/env python3

from sys import argv
import os
from solution import *

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

def startnode(p, red=False):
    return r'''
      \node[fill,state,minimum size=0,accepting%s] (c0) at (%d,%d) {};
''' % (",red" if red else "", p[0], p[1])

def arrow(i, p, red_arrow=False, red_node=False):
    red = lambda b: ",red" if b else ""
    return r'''
      \node[fill,state,minimum size=0%s] (c%d) at (%d,%d) {};
      \draw[-stealth%s] (c%d) -- (c%d);
''' % (red(red_node), i, p[0], p[1], red(red_node), i-1, i)

def graphic(ds):
    path = ds2path(ds)
    xshift = -min(map(lambda xy: xy[0], path))
    yshift = -min(map(lambda xy: xy[1], path))
    xlen = max(map(lambda xy: xy[0], path)) + xshift
    ylen = max(map(lambda xy: xy[1], path)) + yshift

    _, start, end = findLongestPalindromicString(path, debug=True)

    arrows = []
    for i, p in enumerate(path):
        arrows.append(startnode(p, start == i) if i == 0 else arrow(i, p, start <= i < end, start < i <= end))

    return graphic_text(xlen, ylen, xshift, yshift, "\n".join(arrows))

def png_graphic(i):
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
    i = int(argv[1]) if len(argv) > 1 else 0  # Default to 0
    png_graphic(i)
