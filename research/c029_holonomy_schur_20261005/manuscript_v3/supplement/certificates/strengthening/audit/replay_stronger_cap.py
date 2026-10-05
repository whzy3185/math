"""Independent exact full-graph audit of the stronger one-G6 uniform cap.

The entrance state and finite cores are extracted by scalar Schur elimination
on the original signed graph. No four-site recurrence is used to construct
these states. All acceptance tests are rational.
"""
from fractions import Fraction as F
from pathlib import Path
import json
import sympy as sp

CAP = F(790537,100000)
LOWER = F(7905369,1000000)
ENTRANCE = 48
SEED_N = 202
RADIUS = F(1,10**18)
ETA = F(1,10**20)
SEED_MARGIN = F(1,10**6)


def direct_core(n, cap=CAP, trailing_blocks=1):
    b = [1,1,-1,1,-1,-1,1,-1]
    adj = [dict() for _ in range(n)]
    for v in range(n):
        for d, sign in ((1,1),(2,-1 if v==n-1 else b[v%8])):
            w=(v+d)%n
            adj[v][w]=adj[w][v]=sign
    assert all(len(row)==4 for row in adj)
    keep=[0,1]+list(range(n-4*trailing_blocks,n))
    cut=n-len(keep)
    order=list(range(2,n-4*trailing_blocks))+keep
    pos={v:i for i,v in enumerate(order)}
    a=[dict() for _ in range(n)]
    for v in range(n):
        row={v:cap}
        for w,c in adj[v].items():
            for u,d in adj[w].items():
                row[u]=row.get(u,F(0))-c*d
        i=pos[v]
        a[i]={pos[u]:z for u,z in row.items() if pos[u]>=i and z}
    pivots=[]
    for i in range(cut):
        pivot=a[i].get(i,F(0))
        assert pivot>0,(n,str(cap),i,str(pivot))
        pivots.append(pivot)
        ns=sorted(j for j,value in a[i].items() if j>i and value)
        for jj,j in enumerate(ns):
            left=a[i][j]/pivot
            for k in ns[jj:]:
                value=a[j].get(k,F(0))-left*a[i][k]
                if value:
                    a[j][k]=value
                else:
                    a[j].pop(k,None)
        a[i].clear()
    core=[[a[min(i,j)].get(max(i,j),F(0)) for j in range(cut,n)] for i in range(cut,n)]
    return core,pivots


def positive(a):
    a=[list(row) for row in a]
    pivots=[]
    for i in range(len(a)):
        p=a[i][i]
        pivots.append(p)
        if p<=0:
            return False,pivots
        for j in range(i+1,len(a)):
            for k in range(j,len(a)):
                a[j][k]=a[k][j]=a[j][k]-a[i][j]*a[i][k]/p
    return True,pivots


def pd(a):
    return positive([[F(z) for z in row] for row in a.tolist()])[0]


def run():
    finite={}
    checks={}
    for n in range(10,SEED_N+1,8):
        c,p=direct_core(n)
        ok,cp=positive(c)
        assert ok,(n,cp)
        finite[str(n)]={'positive':ok,'interior_scalar_pivots':len(p),'core_scalar_pivots':len(cp)}
        if n==SEED_N:
            shifted=[[c[i][j]-(SEED_MARGIN if i==j else 0) for j in range(6)] for i in range(6)]
            ok,seed_pivots=positive(shifted)
            checks['seed_margin']=ok
    schur,p=direct_core(SEED_N,trailing_blocks=2)
    assert len(p)==4*ENTRANCE
    s=sp.Matrix(schur)
    X=s[2:6,2:6]
    R=s[:2,2:6]
    EP=sp.Matrix([[-1,0,0,0],[0,1,0,0],[-1,2,1,0],[2,-1,0,-1]])
    EM=sp.Matrix([[-1,0,0,0],[0,1,0,0],[-1,-2,1,0],[-2,-1,0,-1]])
    W=s[2:6,6:10]-EP
    diag=sp.Rational(CAP-4)
    D=sp.Matrix([[diag,0,-1,0],[0,diag,0,-1],[-1,0,diag,0],[0,-1,0,diag]])
    P=sp.Matrix([[10766,87,19,974],[87,12664,148,-2418],[19,148,10093,-25],[974,-2418,-25,14009]])/10000
    Q=sp.Matrix([[11503,614,990,-1101],[614,10470,15,113],[990,15,12299,-2632],[-1101,113,-2632,13260]])/10000
    Y=D-EP.T*X.inv()*EP
    residual=D-EM.T*Y.inv()*EM-X
    L=X.inv()*EP*Y.inv()*EM
    checks.update({
        'finite_orders_10_through_202_positive':all(z['positive'] for z in finite.values()),
        '192_scalar_entrance_pivots_positive':True,
        'P_gt_9over10':pd(P-sp.Rational(9,10)*sp.eye(4)),
        'P_lt_2':pd(2*sp.eye(4)-P),
        'Q_gt_9over10':pd(Q-sp.Rational(9,10)*sp.eye(4)),
        'Q_lt_2':pd(2*sp.eye(4)-Q),
        'X_gt_half_I':pd(X-sp.eye(4)/2),
        'Y_gt_half_I':pd(Y-sp.eye(4)/2),
        'P_transfer_below_half':pd(P/2-L.T*P*L),
        'Q_transfer_below_half':pd(Q/2-L*Q*L.T),
        'residual_frobenius_below_r_over_40':sum(z*z for z in residual)<sp.Rational(RADIUS/40)**2,
        'R_entrance_below_eta':pd(sp.Rational(ETA)*sp.eye(2)-R*Q*R.T),
        'W_entrance_below_eta':pd(sp.Rational(ETA)*sp.eye(4)-W.T*Q*W),
    })
    q=F(3,4); theta=q*q; a=F(1,9*10**9); b=12*a
    bound=24*b*b/(1-q*q)+48*a+576*RADIUS
    checks.update({
        'euclidean_response_bound':a*a>F(10,9)*ETA,
        'local_perturbation_below_1e_minus_4':43092*RADIUS<F(1,10000),
        'local_transfer_slack':(q-F(1,10000))**2>F(1,2),
        'local_self_map':F(1,36)+theta<1,
        'uniform_tail_below_1e_minus_8':bound<F(1,10**8),
        'positive_uniform_core_margin':SEED_MARGIN-2*F(1,10**8)==F(49,50000000),
    })
    low_core,low_interior=direct_core(SEED_N,cap=LOWER)
    low_ok,low_pivots=positive(low_core)
    checks['lower_cap_has_strictly_negative_core_pivot']=not low_ok and low_pivots[-1]<0
    checks['lower_cap_negative_pivot_has_positive_predecessors']=all(z>0 for z in low_pivots[:-1])
    checks={k:bool(v) for k,v in checks.items()}
    assert all(checks.values()),checks
    out={
        'status':'PASS','method':'full signed graph scalar-Schur construction; exact rational and symbolic arithmetic',
        'cap':str(CAP),'lower_cap':str(LOWER),'entrance_index':ENTRANCE,'seed_order':SEED_N,
        'radius':str(RADIUS),'response_entrance_eta':str(ETA),'response_q':str(q),'riccati_theta':str(theta),
        'response_a':str(a),'response_b':str(b),'tail_bound_B0':str(bound),
        'uniform_core_margin':str(F(49,50000000)),
        'checks':checks,'finite_graphs':finite,
        'seed_shifted_core_pivots':[str(z) for z in seed_pivots],
        'center':[[str(z) for z in row] for row in X.tolist()],
        'lower_cap_positive_interior_pivots':len(low_interior),
        'lower_cap_core_pivots':[str(z) for z in low_pivots],
    }
    here=Path(__file__).resolve().parent
    (here/'stronger_cap_independent_replay.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ['seed_shifted_core_pivots','center','lower_cap_core_pivots','finite_graphs']},indent=2))


if __name__=='__main__':
    run()
