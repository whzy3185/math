"""Independent audit of the antiperiodic construction.

Construct the signing and Bloch matrix algorithmically, then use a scalar
Fraction LDL test and symbolic polynomial identities. No primary-verifier or repository
verification code is executed.
"""
from fractions import Fraction as F
from pathlib import Path
import json
import sympy as sp
from replay_direct_graph_seed import positive

pattern = [1,1,-1,1,-1,-1,1,-1]
n = 32
A = [[0]*n for _ in range(n)]
flipped = []
for i in range(n):
    for step in (1,2):
        j = i+step
        sign = 1 if step == 1 else pattern[i % 8]
        if j >= n:
            sign *= -1
            flipped.append([i,j % n])
        A[i][j % n] = A[j % n][i] = sign

checks = {}
checks['flip_exactly_three_cut_edges'] = sorted(flipped) == [[30,0],[31,0],[31,1]]
checks['all_triangles_preserved'] = all(A[i][(i+1)%n]*A[(i+1)%n][(i+2)%n]*A[(i+2)%n][i] == pattern[i%8] for i in range(n))
hol = 1
for i in range(n):
    hol *= A[i][(i+1)%n]
checks['hamilton_holonomy_negative'] = hol == -1
certs = {}
for sign in (-1,1):
    M = [[F(279 if i == j else 0) + sign*100*A[i][j] for j in range(n)] for i in range(n)]
    ok, pivots = positive(M)
    checks[f'279I_{"plus" if sign == 1 else "minus"}_100A_positive'] = ok
    certs[str(sign)] = [str(p) for p in pivots]

x,z,s,t = sp.symbols('x z s t')
H = sp.zeros(8)
for i in range(8):
    for step in (1,2):
        j=i+step
        sign=1 if step==1 else pattern[i]
        phase=z if j>=8 else sp.Integer(1)
        H[i,j%8]=sign*phase
        H[j%8,i]=sign/phase
P=x**8-16*x**6+80*x**4-128*x**2+38+s*(-2*x**4+16*x**2-13)+s**2
checks['algorithmic_Bloch_determinant'] = sp.cancel(H.charpoly(x).as_expr()-P.subs(s,z+1/z)) == 0
f=x**4-2*x**3-6*x**2+12*x-4
checks['endpoint_factorization'] = sp.expand(P.subs(s,2)-f*f.subs(x,-x)) == 0
shifted=sum(coef*(t+4)**(power[0]//2) for power,coef in sp.Poly(P,x).terms())
checks['radical_reduction'] = sp.expand(shifted-t**4+(16+2*s)*t**2-s**2-19*s-38) == 0
checks['f_279over100_negative'] = f.subs(x,sp.Rational(279,100)) < 0
checks['f_14over5_positive'] = f.subs(x,sp.Rational(14,5)) > 0
checks={k:bool(v) for k,v in checks.items()}
assert all(checks.values()),checks
out={'status':'PASS','checks':checks,'n32_fraction_LDL_pivots':certs,
     'method':'algorithmic full signed graph and Bloch construction; independent Fraction scalar LDL'}
Path(__file__).with_name('antiperiodic_independent_replay.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':out['status'],'checks':checks},indent=2))
