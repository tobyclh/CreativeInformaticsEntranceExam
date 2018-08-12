import sys

import primefac

n = int(input())
factors = list( primefac.primefac(n) )
print(factors)