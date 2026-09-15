#!/usr/bin/env python3
"""Exact audit for DDGG_DISLOCATION_ALGEBRAIC_LIMIT.md.

Reconstructs the elimination curve, stationary resultant factorization,
Sturm root counts, phase-boundary exclusions, and rational isolation boxes.
All acceptance tests use exact SymPy arithmetic.
"""
import sympy as sp

y,d=sp.symbols('y d')
A=y**2-8*y+10-d**2

alpha=(
 d**6-2*d**5*y+8*d**5-d**4*y**2+8*d**4*y-6*d**4
 +4*d**3*y**3-48*d**3*y**2+168*d**3*y-160*d**3
 -d**2*y**4+16*d**2*y**3-92*d**2*y**2+224*d**2*y-168*d**2
 -2*d*y**5+40*d*y**4-296*d*y**3+992*d*y**2-1476*d*y+788*d
 +y**6-24*y**5+226*y**4-1056*y**3+2544*y**2-2944*y+1272
)
beta=-(y-d-4)*(
 d**3-d**2*y+4*d**2-d*y**2+8*d*y-12*d
 +y**3-12*y**2+40*y-32
)
E=sp.expand(alpha**2+beta**2+A*alpha*beta)
Ed=sp.diff(E,d)

resy=sp.factor(sp.resultant(E,Ed,d))
fac=sp.factor_list(resy)[1]
bydeg={sp.degree(f,y):(f,m) for f,m in fac}
assert set(bydeg) >= {1,6,18}
P6=bydeg[6][0]
P18=bydeg[18][0]

assert sp.Poly(P6,y).count_roots(sp.Rational(77,10),sp.Rational(31,4)) == 0
assert sp.Poly(P18,y).count_roots(sp.Rational(77,10),sp.Rational(31,4)) == 1
assert sp.Poly(P18,y).count_roots(sp.Rational(77007,10000),sp.Rational(77008,10000)) == 1

for dv in (-2,2):
    assert sp.Poly(E.subs(d,dv),y).count_roots(sp.Rational(77,10),sp.Rational(31,4)) == 0

resd=sp.factor(sp.resultant(E,Ed,y))
facd=sp.factor_list(resd)[1]
Q18=[f for f,m in facd if sp.degree(f,d)==18][0]
assert sp.Poly(Q18,d).count_roots(sp.Rational(1992,1000),sp.Rational(1993,1000)) == 1

# Numerical output is orientation only, after exact certification above.
yroots=[r for r in sp.nroots(P18,n=40,maxsteps=300)
        if abs(sp.im(r))<sp.Rational(1,10)**30 and sp.Rational(77,10)<sp.re(r)<sp.Rational(31,4)]
droots=[r for r in sp.nroots(Q18,n=40,maxsteps=300)
        if abs(sp.im(r))<sp.Rational(1,10)**30 and sp.Rational(1992,1000)<sp.re(r)<sp.Rational(1993,1000)]
assert len(yroots)==1 and len(droots)==1
print('P18 top root:', yroots[0])
print('candidate d roots in isolation interval:', droots)
print('all exact root-count checks passed')
