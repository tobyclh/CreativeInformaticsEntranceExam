import random as r
import math as m

# Number of darts that land inside.
inside = 0
# Total number of darts to throw.
total = 5000000

# Iterate for the number of darts.
for i in range(0, total):
    # Generate random x, y in [0, 1].
    x2 = r.random()**2
    y2 = r.random()**2
    # Increment if inside unit circle.
    if m.sqrt(x2 + y2) < 1.0:
      inside += 1

# inside / total = pi / 4
pi = (float(inside) / total) * 4

# It works!
print(pi)