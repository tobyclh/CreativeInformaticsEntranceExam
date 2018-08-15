# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 18:51:08 2015

@author: Duncan

A simplified version of linearring.py, one of the shapely examples
"""

from matplotlib import pyplot as plt
from shapely.geometry.polygon import LinearRing, Polygon




ring = LinearRing([(0, 0), (0, 2), (1, 1), (2, 2), (2, 0), (1, 0.8), (0, 0)])
x, y = ring.xy

fig = plt.figure(1, figsize=(5,5), dpi=90)
ax = fig.add_subplot(111)
ax.plot(x, y)
ax.set_title('Polygon Edges')

xrange = [-1, 3]
yrange = [-1, 3]
ax.set_xlim(*xrange)
ax.set_xticks(list(range(*xrange)) + [xrange[-1]])
ax.set_ylim(*yrange)
ax.set_yticks(list(range(*yrange)) + [yrange[-1]])
ax.set_aspect(1)
plt.show()