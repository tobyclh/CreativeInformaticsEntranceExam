import numpy as np
import math
def A_r1(d):
    _R = [0, 0, 10, 10]
    _range = (np.asarray(_R)*d)
    print(f'Range : {_range}')
    _r = []
    for i, r in enumerate(_range):
        if float(r).is_integer():
            _r.append(int(r))
        else:
            j = int(r)
            if i > 1:
                j+=1
            _r.append(j)
    
    x_min, y_min, x_max, y_max = _r
    count = 0
    for i in range(x_min, x_max+1):
        for j in range(y_min, y_max+1):
            if (d*i - 5)**2 + (d*j - 5)**2 <= 25:
                    count += 1
    return count


def A_r0(d):
    R=[0,0,10,10]
    _range = (np.asarray(R)*d)
    print(f'Range : {_range}')
    _r = []
    for i, r in enumerate(_range):
        if float(r).is_integer():
            _r.append(int(r))
        else:
            j = int(r)
            if i > 1:
                j+=1
            _r.append(j)
    
    x_min, y_min, x_max, y_max = _r
    count = 0
    for i in range(x_min, x_max+1):
        for j in range(y_min, y_max+1):
            if d*i >= x_min and d*i < x_max:
                if d*j >= y_min and d*j < y_max:
                    count += 1

    return count


d = float(input())
result = A_r1(d) / A_r0(d) / 4
print(f'Result :{result}')


