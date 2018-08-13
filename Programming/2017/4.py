import numpy as np
rlu = []
m = int(input('m? '))
n = int(input('n? '))
s = int(input('s? '))
A = np.ones([m, n])
B = np.ones([m, n]).T * 2
C = np.zeros([m, m])
count = 0
for i in range(m):
    for j in range(m):
        d = 0
        for k in range(n):
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
        C[i,j] = d
assert np.all(C == A@B)
print(f'C : {C} \n cnt :{count}')