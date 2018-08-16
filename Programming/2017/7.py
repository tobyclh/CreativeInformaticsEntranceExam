import numpy as np
from tqdm import tqdm
from collections import deque
rlu = deque()
def handle_input(_str, default=0):
    val = input(_str)
    if val is None or val == '' or not isinstance(int(val), int):
        return default
    else:
        return int(val)
m = handle_input('m? ')
n = handle_input('n? ')
s = handle_input('s? ')
_min, _max = min(m, n), max(m, n)
dividers = []
for q in range(_min, 0, -1):
    if _max%q == 0 and _min%q==0:
        dividers.append(q)
print(f'Dividers : {dividers}')
optimal_read = None
from numba import jit, int32
# @jit(int32(int32, int32, int32))#(nopython=True)
from joblib import Parallel, delayed
# @jit
def banana(q, m, n):
    rlu = deque()
    count = 0
    for u in range(0, m, q): 
        for v in range(0, m, q):
            for w in range(0, n, q):
                for i in range(u, u+q):
                    for j in range(v, v+q):
                        for k in range(w, w+q):
                            for symbol in [('A', i, k), ('B', k, j)]:
                                if symbol in rlu:
                                    rlu.remove(symbol)
                                else:  
                                    count += 1
                                    if len(rlu) > s:
                                        rlu.popleft()
                                rlu.append(symbol)
    return count
from time import time
def wrapper(q):
    print(f'started for {q}')
    start = time()
    count = banana(q, m, n)
    duration = time() - start
    print(f'took : {duration} cnt : {count}, q : {q}')
    # break
# for q in dividers:
#     wrapper(q)
Parallel(n_jobs=len(dividers))(delayed(wrapper)(q) for q in dividers)

    
    
# best_q = _max
# if optimal_read is None or optimal_read > count or (optimal_read == count and best_q < q):
#     optimal_read = count
#     best_q = q
    
# print(f'Optimal divider : {q}, count : {optimal_read}')