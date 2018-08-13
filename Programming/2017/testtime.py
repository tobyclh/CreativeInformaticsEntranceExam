from collections import deque
from time import time
times = 5001

a = [0]*times
start = time()
for _ in range(times-1):
    a.pop(0)
duration = time() - start 
print(f'duration : {duration}')

a = [0]*times

start = time()
for _ in range(times-1):
    a = a[1:]
duration = time() - start 
print(f'duration : {duration}')


a = deque([0]*times)
start = time()
for _ in range(times-1):
    a.popleft()
duration = time() - start 
print(f'duration : {duration}')



a = [*range(times)]
start = time()
for i in range(times-1):
    a.remove(i)
    a.append(i)
duration = time() - start 
print(f'duration : {duration}')


a = [*range(times)]
start = time()
for i in range(times-1):
    idx = a.index(i)
    a[idx:-1] = a[idx+1:]
    a[-1] = i

duration = time() - start 
print(f'duration : {duration}')
