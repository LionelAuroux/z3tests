#!/usr/bin/env python3.8

from z3 import *


print("""
SAT/SMT as problem solver
""")

s = Optimize()

pieces_de_bois_total = Int('pieces_de_bois_total')

coupe_A, coupe_B, coupe_C, coupe_D = Ints('coupe_A coupe_B coupe_C coupe_D')

type_A, type_B = Ints('type_A type_B')

s.add(pieces_de_bois_total == coupe_A + coupe_B + coupe_C + coupe_D)

s.add(coupe_A >= 0)
s.add(coupe_B >= 0)
s.add(coupe_C >= 0)
s.add(coupe_D >= 0)

s.add(type_A == coupe_A*3 + coupe_B*2 + coupe_C)
s.add(type_B == coupe_A + coupe_B*6 + coupe_C*9 + coupe_D*13)

s.add(type_A == 800)
s.add(type_B == 400)

s.minimize(pieces_de_bois_total)

print(f"Is SAT? {s.check()}")
print(f"RES: {s.model()}")
