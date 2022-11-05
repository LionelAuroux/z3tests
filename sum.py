#!/usr/bin/env python3.8

from z3 import *

"""
We try to compute a subset of myset that sum is 0
"""

myset = [-7, -3, -2, 5, 8]
lmyset = len(myset)

v = [Int(f'vars_{i}') for i in range(lmyset)]

s = Solver()

rt = []

for i in range(lmyset):
    # compose constraint
    rt.append(v[i] * myset[i])
    s.add(Or(v[i] == 0, v[i] == 1)) # use it as boolean

s.add(sum(rt) == 0) # so sum of subset must be null
s.add(sum(v) >= 1) # but subset is not empty set

sat = s.check()
print(f"Is SAT? {sat}")
if not sat:
    exit(0)

m = s.model()
print(f"RES : {m}")
for i in range(lmyset):
    if m[v[i]].as_long() == 1:
        print(myset[i])
