"""Independent exact verifier for the strengthened uniform residue-two cap.

Authored for this audit. No repository modules or executable code are imported.
Only Python's standard library is needed. Every acceptance comparison is rational.
"""
from fractions import Fraction as F
from pathlib import Path
import json
import hashlib


def mat(rows):
    return [[F(x) for x in row] for row in rows]


def transpose(a):
    return list(map(list, zip(*a)))


def mm(a, b):
    return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]


def add(a,b):
    return [[x+y for x,y in zip(ra,rb)] for ra,rb in zip(a,b)]


def scale(s,a):
    return [[s*x for x in row] for row in a]


def sub(a,b):
    return add(a,scale(-1,b))


def eye(n):
    return [[F(i==j) for j in range(n)] for i in range(n)]


def inv(a):
    n=len(a)
    b=[row[:] + e for row,e in zip(a,eye(n))]
    for j in range(n):
        pivot=b[j][j]
        assert pivot != 0
        b[j]=[x/pivot for x in b[j]]
        for i in range(n):
            if i!=j:
                c=b[i][j]
                b[i]=[x-c*y for x,y in zip(b[i],b[j])]
    return [row[n:] for row in b]


def ldl(a):
    assert a == transpose(a)
    b=[row[:] for row in a]
    pivots=[]
    for k in range(len(b)):
        p=b[k][k]
        pivots.append(p)
        if p<=0:
            return False,pivots
        for i in range(k+1,len(b)):
            for j in range(i,len(b)):
                b[i][j]=b[j][i]=b[i][j]-b[i][k]*b[k][j]/p
    return True,pivots


def pd(a):
    return ldl(a)[0]


CAP=F(790537,100000)

D=mat([[(CAP-4),0,-1,0],[0,(CAP-4),0,-1],[-1,0,(CAP-4),0],[0,-1,0,(CAP-4)]])
EP=mat([[-1,0,0,0],[0,1,0,0],[-1,2,1,0],[2,-1,0,-1]])
EM=mat([[-1,0,0,0],[0,1,0,0],[-1,-2,1,0],[-2,-1,0,-1]])
P=scale(F(1,10000),mat([[10766,87,19,974],[87,12664,148,-2418],[19,148,10093,-25],[974,-2418,-25,14009]]))
Q=scale(F(1,10000),mat([[11503,614,990,-1101],[614,10470,15,113],[990,15,12299,-2632],[-1101,113,-2632,13260]]))
R0=mat([[-1,-2,1,0],[-2,-1,0,-1]])
W0=mat([[0,0,-1,0],[0,0,0,1],[0,0,0,0],[0,0,0,0]])
C0=mat([[-1,0,-1,0],[0,-1,0,-1]])
G0=scale((CAP-4),eye(2))


def schur(x,e):
    return sub(D,mm(transpose(e),mm(inv(x),e)))


def core(g,h,c,r,w,x):
    a=inv(x)
    w=add(w,EP)
    g=sub(g,mm(r,mm(a,transpose(r))))
    h=sub(h,mm(transpose(w),mm(a,w)))
    c=sub(c,mm(r,mm(a,w)))
    return [x+y for x,y in zip(g,c)] + [x+y for x,y in zip(transpose(c),h)]


def graph_matrix(n):
    """Directly square the explicit signed graph using integer two-hop walks."""
    pattern=(1,1,-1,1,-1,-1,1,-1)
    tau=[pattern[i%8] for i in range(n-1)]+[-1]
    adj=[{} for _ in range(n)]
    for i in range(n):
        for step,sgn in ((1,1),(2,tau[i])):
            j=(i+step)%n
            assert j not in adj[i]
            adj[i][j]=sgn
            adj[j][i]=sgn
    sq=[[0]*n for _ in range(n)]
    for i in range(n):
        for k,a in adj[i].items():
            for j,b in adj[k].items():
                sq[i][j]+=a*b
    return [[CAP*(i==j)-sq[i][j] for j in range(n)] for i in range(n)]


def block_template(n):
    m=(n-2)//4
    blocks=[[0,1]]+[list(range(2+4*j,6+4*j)) for j in range(m)]
    a=[[F(0) for _ in range(n)] for _ in range(n)]
    def put(i,j,x):
        for u,row in zip(blocks[i],x):
            for v,value in zip(blocks[j],row):
                a[u][v]=value
                a[v][u]=value
    put(0,0,G0)
    for j in range(1,m+1):
        put(j,j,D)
    for j in range(1,m):
        put(j,j+1,EP if j%2 else EM)
    put(0,1,R0)
    put(0,m,C0)
    put(1,m,W0)
    return a


def run():
    global CAP,D,G0
    original_cap=CAP
    checks={}
    certificates={}
    for n in (18,26,34,202):
        checks[f'graph_block_template_n{n}']=graph_matrix(n)==block_template(n)
    checks['direct_full_graph_n10_positive']=pd(graph_matrix(10))
    checks['EP_frobenius_squared_14']=sum(x*x for row in EP for x in row)==14
    checks['EM_frobenius_squared_14']=sum(x*x for row in EM for x in row)==14
    for name,weight in [('P',P),('Q',Q)]:
        checks[name+'_gt_9over10']=pd(sub(weight,scale(F(9,10),eye(4))))
        checks[name+'_lt_2']=pd(sub(scale(2,eye(4)),weight))
    radius=F(1,10**18)
    eta=F(1,10**20)
    J=48
    seed_margin=F(1,10**6)
    x=D
    g,h,c,r,w=G0,D,C0,R0,W0
    finite=[{'n':10,'positive':checks['direct_full_graph_n10_positive'],'method':'direct full-matrix rational LDL'}]
    for j in range(J+1):
        checks[f'pivot_positive_j{j}']=pd(x)
        if j>=2 and j%2==0:
            n=4*(j+2)+2
            s=core(g,h,c,r,w,x)
            okay,pivs=ldl(s)
            finite.append({'n':n,'terminal_index':j,'positive':okay,'method':'six-by-six exact response core'})
            if j==J:
                passed,p=ldl(sub(s,scale(seed_margin,eye(6))))
                checks['six_core_202_margin_1over_million']=passed
                certificates['seed_pivots']=[str(v) for v in p]
                certificates['seed_core']=[[str(v) for v in row] for row in s]
        if j==J:
            center=x
            mid=schur(center,EP)
            image=schur(mid,EM)
            residual=sub(image,center)
            checks['center_gt_half_I']=pd(sub(center,scale(F(1,2),eye(4))))
            checks['middle_gt_half_I']=pd(sub(mid,scale(F(1,2),eye(4))))
            checks['center_residual_lt_radius_over40']=sum(v*v for row in residual for v in row)<(radius/40)**2
            l=mm(mm(inv(center),EP),mm(inv(mid),EM))
            checks['P_center_transfer_lt_half']=pd(sub(scale(F(1,2),P),mm(transpose(l),mm(P,l))))
            checks['Q_center_transfer_lt_half']=pd(sub(scale(F(1,2),Q),mm(l,mm(Q,transpose(l)))))
            checks['R_entrance_Q_bound']=pd(sub(scale(eta,eye(2)),mm(r,mm(Q,transpose(r)))))
            checks['W_entrance_Q_bound']=pd(sub(scale(eta,eye(4)),mm(transpose(w),mm(Q,w))))
            certificates['center']=[[str(v) for v in row] for row in center]
            certificates['entrance_R']=[[str(v) for v in row] for row in r]
            certificates['entrance_W']=[[str(v) for v in row] for row in w]
        a=inv(x)
        e=EP if j%2==0 else EM
        g=sub(g,mm(r,mm(a,transpose(r))))
        h=sub(h,mm(transpose(w),mm(a,w)))
        c=sub(c,mm(r,mm(a,w)))
        r=scale(-1,mm(r,mm(a,e)))
        w=scale(-1,mm(transpose(e),mm(a,w)))
        x=sub(D,mm(transpose(e),mm(a,e)))
    checks['finite_10_through_202_all_positive']=all(z['positive'] for z in finite)
    checks['base_coverage']=[z['n'] for z in finite]==list(range(10,203,8))
    checks['local_L_variation_lt_1over10000']=F(3,2)*14364*2*radius<F(1,10000)
    checks['inverse_bootstrap']=84*2*radius<F(1,6)
    checks['sqrt_half_plus_1over10000_lt_three_quarters']=(F(3,4)-F(1,10000))**2>F(1,2)
    q=F(3,4)
    theta=q*q
    checks['P_ball_self_map']=F(1,36)+theta<1
    a=F(1,9_000_000_000)
    b=12*a
    delta=4*radius
    checks['response_norm_conversion']=F(10,9)*eta<a*a
    bound=24*b*b/(1-q*q)+48*a+144*delta
    eps=F(1,10**8)
    checks['uniform_core_tail_lt_1over100million']=bound<eps
    checks['two_error_seed_margin_positive']=seed_margin-2*eps>0
    certificates['uniform_core_tail_upper']=str(bound)
    certificates['tail_seed_transfer_margin']=str(seed_margin-2*eps)
    # Independent finite obstruction to lowering the cap below 7.905369.
    lower_cap=F(7905369,10**6)
    D=sub(D,scale(CAP-lower_cap,eye(4)))
    G0=scale(lower_cap-4,eye(2))
    x=D
    g,h,c,r,w=G0,D,C0,R0,W0
    lower_bulk=[]
    for j in range(J+1):
        lower_bulk.append(pd(x))
        if j==J:
            lower_core=core(g,h,c,r,w,x)
            positive,pivs=ldl(lower_core)
            certificates['lower_cap_core']=[[str(v) for v in row] for row in lower_core]
            certificates['lower_cap_first_nonpositive_pivot']=str(pivs[-1])
            certificates['lower_cap_ldl_prefix']=[str(v) for v in pivs]
            checks['lower_cap_n202_strict_negative_core_pivot']=(not positive and pivs[-1]<0 and all(z>0 for z in pivs[:-1]))
        a_inv=inv(x)
        e=EP if j%2==0 else EM
        g=sub(g,mm(r,mm(a_inv,transpose(r))))
        h=sub(h,mm(transpose(w),mm(a_inv,w)))
        c=sub(c,mm(r,mm(a_inv,w)))
        r=scale(-1,mm(r,mm(a_inv,e)))
        w=scale(-1,mm(transpose(e),mm(a_inv,w)))
        x=sub(D,mm(transpose(e),mm(a_inv,e)))
    checks['lower_cap_n202_all_bulk_pivots_positive']=all(lower_bulk)
    out={'status':'PASS' if all(checks.values()) else 'FAIL','parameters':{'cap':str(original_cap),'lower_obstruction_cap':str(lower_cap),'entrance_index':J,'seed_graph_order':202,'radius':str(radius),'response_quadratic_bound':str(eta),'response_contraction':str(q),'riccati_contraction':str(theta),'seed_margin':str(seed_margin),'tail_target':str(eps)},'checks':checks,'finite':finite,'certificates':certificates,'method':'new standard-library Fraction verifier, exact acceptance only; normalized six-by-six cores except the explicit full n10 check'}
    path=Path(__file__).with_name('uniform_cap_certificate.json')
    path.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'status':out['status'],'parameters':out['parameters'],'checks':checks,'finite':finite,'certificate_path':str(path),'certificate_sha256':hashlib.sha256(path.read_bytes()).hexdigest()},indent=2))
    assert all(checks.values()), 'Failed required exact check'


if __name__=='__main__':
    run()
