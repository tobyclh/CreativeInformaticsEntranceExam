import numpy as np
rlu = []
m = int(input('m? '))
n = int(input('n? '))
s = int(input('s? '))
_min, _max = min(m, n), max(m, n)
for q in range(_min, 0, -1):
    if _max%q == 0 and _min%q==0:
        break
print(f'Q : {q}')

A = np.arange(m*n).reshape([m, n])
# print(f'A : {A}')
B = np.ones([m, n]).T# * 2
C = np.zeros([m, m])
count = 0
for u in range(0, m, q):
    for v in range(0, m, q):
        for w in range(0, n, q):
            for i in range(u, u+q):
                for j in range(v, v+q):
                    d = 0
                    for k in range(w, w+q):
                        d += A[i,k] * B[k, j]
                        for symbol in [f'A{i}{k}', f'B{k}{j}']:
                            if symbol in rlu:
                                rlu.remove(symbol)
                                rlu.append(symbol)
                            else:
                                if len(rlu) > s:
                                    rlu.pop(0)
                                rlu.append(symbol)
                                count += 1
                    C[i,j] += d
print(f'C : {C} \n cnt :{count}')
# print(f'A@B : {A@B}')
assert np.allclose(C, A@B)