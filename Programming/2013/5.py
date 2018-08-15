from numba import jit
import numpy as np
from shapely.geometry.polygon import Polygon
from shapely.geometry.point import Point
import matplotlib.pyplot as plt
@jit(nopython=True)
def ray_tracing(x,y,poly):
    n = len(poly)
    inside = False
    p2x = 0.0
    p2y = 0.0
    xints = 0.0
    p1x,p1y = poly[0]
    for i in range(n+1):
        p2x,p2y = poly[i % n]
        if y > min(p1y,p2y):
            if y <= max(p1y,p2y):
                if x <= max(p1x,p2x):
                    if p1y != p2y:
                        xints = (y-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
                    if p1x == p2x or x <= xints:
                        inside = not inside
        p1x,p1y = p2x,p2y
    return inside
class triangle:
    def __init__(self, vertices, parent=None):
        assert vertices.shape[0] == 3
        assert vertices.shape[1] == 2
        self.vertices = vertices
        self.parent = parent
        self.children = []
    
    @property
    def v0(self):
        return self.vertices[0]
    
    @property
    def v1(self):
        return self.vertices[1]

    @property
    def v2(self):
        return self.vertices[2]

    
    def get_child(self, v0, v1):
        if len(self.children) == 0:
            return None
        for _v0, _v1 in [[v0, v1], [v1, v0]]:
            if all(_v0 == self.v0) and all(_v1 == self.v2):
                return self.children[0]
            if all(_v0 == self.v1) and all(_v1 == self.v2):
                return self.children[1]
            if all(_v0 == self.v1) and all(_v1 == self.v0):
                if len(self.children) >= 3:
                    return self.children[2]
                else:
                    return None

    def make_kid(self):
        for p0, p1, p2 in [(self.v0,self.v2,self.v1), (self.v2,self.v1,self.v0), (self.v1,self.v0,self.v2)]:
            y0, x0  = p0
            y1, x1  = p1
            y2, x2  = p2
            new_x0, new_x1 = x1/3 + x0/3*2,  x1/3*2 + x0/3
            new_y0, new_y1 = y1/3 + y0/3*2,  y1/3*2 + y0/3
            median_x, median_y = (x1+x0)/2, (y1+y0)/2
            new_x2, new_y2 = (median_x-x2)/3 + median_x, (median_y-y2)/3 + median_y
            new_vertices = np.array([[new_y0, new_x0], [new_y1, new_x1], [new_y2, new_x2]])
            tri = triangle(new_vertices, parent=self)
            self.children.append(tri)
            
            
    def get_knok_vertices(self, vertex_pair):
        ordered_vertices = []
        p0, p1 = vertex_pair
        ordered_vertices.append(p0)
        child = self.get_child(p0, p1)
        if child is not None:
            ordered_vertices.extend(child.get_knok_vertices([child.v0, child.v2]))
            ordered_vertices.extend(child.get_knok_vertices([child.v2, child.v1]))
            # ordered_vertices.extend(child.get_knok_vertices([child.v1, child.v0]))
        # else:
        #     print('child is None')
        ordered_vertices.append(p1)
        return ordered_vertices

    

    def plot(self):
        vertices = self.get_knok_vertices([self.v0, self.v2])
        vertices.extend(self.get_knok_vertices([self.v2, self.v1]))
        vertices.extend(self.get_knok_vertices([self.v1, self.v0]))
        vertices = np.asarray(vertices)
        
        print(vertices)
        # knoc = Polygon(vertices)
        # x, y = knoc.xy
        fig = plt.figure(1, figsize=(10,10), dpi=90)
        ax = fig.add_subplot(111)
        ax.plot(vertices[:,0], vertices[:,1])
        ax.set_title('Polygon Edges')

        xrange = [-8, 15]
        yrange = [-8, 15]
        ax.set_xlim(*xrange)
        ax.set_xticks(list(range(*xrange)) + [xrange[-1]])
        ax.set_ylim(*yrange)
        ax.set_yticks(list(range(*yrange)) + [yrange[-1]])
        ax.set_aspect(1)
        plt.show()
        return vertices


    def make_family(self, K):
        # print(f'Make family : {K}')
        if K >= 1:
            self.make_kid()
        K -= 1
        if K <= 0: 
            return
        for c in self.children:
            c.make_family(K)

        
tri = triangle(np.array([[0, 0], [10, 0], [5, 5*np.sqrt(3)]]))
tri.make_family(int(input('K?')))

#after plotting the graph you can simply test it with point
vertices = tri.plot()
poly = Polygon(vertices)
pt = Point(9,5)
print(poly.contains(pt))










