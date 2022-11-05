#!/usr/bin/env python3.8

from z3 import *

a, b, c, d, e, f = Ints('a b c d e f')

s = Solver()
s.add(a*215 + b*275 + c*335 + d*355 + e*420 + f*580 == 1505)
s.add(a <= 10)
s.add(b <= 10)
s.add(c <= 10)
s.add(d <= 10)
s.add(e <= 10)
s.add(f <= 10)

print(f"SAT/SMT for diophantine equation")
while s.check():
    print(f"Is SAT? {s.check()}")
    m = s.model()
    print(f"RES: {m}")
    s.add(Not(And(a == m['a'], b == m['b'], c == m['c'], d == m['d'], e == m['e'], f == m['f'])))
    # FIXME: pas compris comment obtenir la 2ieme solution
