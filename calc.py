#!/usr/bin/env python3.8

from z3 import *

x, y, z = Ints('x y z')

s = Solver()

s.add(x == 2)
s.add(y == 12)
s.add(z == x + y)

print(f"SMT/SAT is also calculator")

print(f"Is Sat? {s.check()}")
print(f"RES: {s.model()}")
