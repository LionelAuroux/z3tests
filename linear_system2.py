#!/usr/bin/env python3.8

from z3 import *

circle, square, triangle = Ints('circle square triangle')

s = Solver()

s.add(circle + circle == 10)
s.add(circle * square + square == 12)
s.add(circle * square - triangle * circle == circle)

print(f"SAT/SMT compute linear system with symbolic")

print(f"Is it SAT? {s.check()}")
print(f"RES: {s.model()}")
