import numpy as np
start_side = 10
def tri_area(side):
    return (np.sqrt(side**2 - (side/2)**2))*side/2


def area_of_snow(K=1, start=start_side):
    side = start_side
    num_tri = 1
    area = tri_area(side)*num_tri 
    for i in range(K-1):
        side = side/3
        num_tri = num_tri *3
        area += tri_area(side)*num_tri 
    return area

print(area_of_snow(30))

import shapely