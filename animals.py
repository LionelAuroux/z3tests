#!/usr/bin/env python3.8

from z3 import *

cat, dog, rabbit = Ints('cat dog rabbit')
#total = Int('total')

#s = Optimize()
s = Solver()

s.add(cat >= 0)
s.add(dog >= 0)
s.add(rabbit >= 0)

s.add(cat + rabbit == 10)
s.add(dog + cat == 24)
s.add(dog + rabbit == 20)
#s.add(total == cat + dog + rabbit)

#s.minimize(total)

print(f"Is SAT? {s.check()}")
print(f"RES: {s.model()}")
