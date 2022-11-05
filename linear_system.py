#!/usr/bin/env python3.8

from z3 import *

x = Real('x')
y = Real('y')
z = Real('z')

s = Solver()
print(
"""
    SAT/SMT compute linear system

    3x + 2y -  z = 1
    2x - 2y + 4z = -2
    -x + (1/2)y - z = 0
"""
)

s.add(3 * x + 2 * y - z == 1)
s.add(2 * x - 2 * y + 4 * z == -2)
s.add(-x + .5*y - z == 0)

print(f"Is SAT? {s.check()}")
print(f"{s.model()}")
