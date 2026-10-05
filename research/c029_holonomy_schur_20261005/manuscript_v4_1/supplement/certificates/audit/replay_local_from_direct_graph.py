"""Independent local certificate replay from a full-graph scalar Schur complement.

The two-cell recurrence is not used to construct the entrance state. It is
extracted from the n=106 graph after 96 scalar eliminations. SymPy is used
for exact small-matrix operations only.
"""
from fractions import Fraction as F
from pathlib import Path
import json
import sympy as sp
from replay_direct_graph_seed import direct_core, positive


def pd(a):
    return positive([[F(v) for v in row] for row in a.tolist()])[0]


schur, pivots = direct_core(106, trailing_blocks=2)
s = sp.Matrix(schur)
assert len(pivots) == 96
D=sp.Matrix([[sp.Rational(98,25),0,-1,0],[0,sp.Rational(98,25),0,-1],[-1,0,sp.Rational(98,25),0],[0,-1,0,sp.Rational(98,25)]])
EP=sp.Matrix([[-1,0,0,0],[0,1,0,0],[-1,2,1,0],[2,-1,0,-1]])
EM=sp.Matrix([[-1,0,0,0],[0,1,0,0],[-1,-2,1,0],[-2,-1,0,-1]])
P=sp.Matrix([[10766,87,19,974],[87,12664,148,-2418],[19,148,10093,-25],[974,-2418,-25,14009]])/10000
Q=sp.Matrix([[11503,614,990,-1101],[614,10470,15,113],[990,15,12299,-2632],[-1101,113,-2632,13260]])/10000
X=s[2:6,2:6]
R=s[:2,2:6]
W=s[2:6,6:10]-EP
Y=D-EP.T*X.inv()*EP
Z=D-EM.T*Y.inv()*EM
L=X.inv()*EP*Y.inv()*EM
residual=Z-X
checks={
    'entrance_constructed_by_96_positive_scalar_graph_pivots': True,
    'P_gt_9over10':pd(P-sp.Rational(9,10)*sp.eye(4)),
    'P_lt_2':pd(2*sp.eye(4)-P),
    'Q_gt_9over10':pd(Q-sp.Rational(9,10)*sp.eye(4)),
    'Q_lt_2':pd(2*sp.eye(4)-Q),
    'X_gt_half_I':pd(X-sp.eye(4)/2),
    'Y_gt_half_I':pd(Y-sp.eye(4)/2),
    'P_transfer_bound':pd(sp.Rational(2,5)*P-L.T*P*L),
    'Q_transfer_bound':pd(sp.Rational(2,5)*Q-L*Q*L.T),
    'residual_frobenius_bound':sum(z*z for z in residual)<sp.Rational(1,400000000000)**2,
    'R_entrance_bound':pd(sp.eye(2)/10**10-R*Q*R.T),
    'W_entrance_bound':pd(sp.eye(4)/10**10-W.T*Q*W),
}
cert=json.loads((Path(__file__).parents[1]/'analytic/r2_exact_certificate.json').read_text())
checks['X_equals_analytic_center']=X==sp.Matrix([[sp.Rational(v) for v in row] for row in cert['certificates']['center']])
assert all(checks.values()),checks
checks={k:bool(v) for k,v in checks.items()}
result={'status':'PASS','method':'exact direct-graph entrance plus independent symbolic matrix arithmetic','checks':checks}
Path(__file__).with_name('direct_graph_local_replay.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
