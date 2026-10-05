"""Independent exact verifier for the C029 residue-two continuation.

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


D=mat([[F(98,25),0,-1,0],[0,F(98,25),0,-1],[-1,0,F(98,25),0],[0,-1,0,F(98,25)]])
EP=mat([[-1,0,0,0],[0,1,0,0],[-1,2,1,0],[2,-1,0,-1]])
EM=mat([[-1,0,0,0],[0,1,0,0],[-1,-2,1,0],[-2,-1,0,-1]])
P=scale(F(1,10000),mat([[10766,87,19,974],[87,12664,148,-2418],[19,148,10093,-25],[974,-2418,-25,14009]]))
Q=scale(F(1,10000),mat([[11503,614,990,-1101],[614,10470,15,113],[990,15,12299,-2632],[-1101,113,-2632,13260]]))
R0=mat([[-1,-2,1,0],[-2,-1,0,-1]])
W0=mat([[0,0,-1,0],[0,0,0,1],[0,0,0,0],[0,0,0,0]])
C0=mat([[-1,0,-1,0],[0,-1,0,-1]])
G0=scale(F(98,25),eye(2))


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
    return [[F(198,25)*(i==j)-sq[i][j] for j in range(n)] for i in range(n)]


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
    checks={}
    diagnostics={}
    for n in (50,58,66,410):
        checks[f"graph_block_template_n{n}"]=graph_matrix(n)==block_template(n)
    checks['EP_frobenius_squared_14']=sum(x*x for row in EP for x in row)==14
    checks['EM_frobenius_squared_14']=sum(x*x for row in EM for x in row)==14
    for name,weight in [('P',P),('Q',Q)]:
        checks[name+'_gt_9over10']=pd(sub(weight,scale(F(9,10),eye(4))))
        checks[name+'_lt_2']=pd(sub(scale(2,eye(4)),weight))
    x=D
    g,h,c,r,w=G0,D,C0,R0,W0
    finite=[]
    certificates={}
    for j in range(101):
        checks[f'pivot_positive_j{j}']=pd(x)
        if j==24:
            center=x
            mid=schur(center,EP)
            nxt=schur(mid,EM)
            residual=sub(nxt,center)
            checks['center_gt_half_I']=pd(sub(center,scale(F(1,2),eye(4))))
            checks['middle_gt_half_I']=pd(sub(mid,scale(F(1,2),eye(4))))
            checks['center_residual_frobenius_lt_1over400billion']=sum(v*v for row in residual for v in row)<F(1,400000000000)**2
            l=mm(mm(inv(center),EP),mm(inv(mid),EM))
            checks['P_center_transfer_lt_two_fifths']=pd(sub(scale(F(2,5),P),mm(transpose(l),mm(P,l))))
            checks['Q_center_transfer_lt_two_fifths']=pd(sub(scale(F(2,5),Q),mm(l,mm(Q,transpose(l)))))
            checks['R_entrance_Q_bound']=pd(sub(scale(F(1,10**10),eye(2)),mm(r,mm(Q,transpose(r)))))
            checks['W_entrance_Q_bound']=pd(sub(scale(F(1,10**10),eye(4)),mm(transpose(w),mm(Q,w))))
            certificates['center']=[[str(v) for v in row] for row in center]
        if j>=10 and j%2==0:
            n=4*(j+2)+2
            s=core(g,h,c,r,w,x)
            okay,pivs=ldl(s)
            finite.append({'n':n,'terminal_index':j,'positive':okay})
            if j==24:
                passed,p=ldl(sub(s,scale(F(1,50),eye(6))))
                checks['six_core_106_margin_1over50']=passed
                certificates['seed_106_pivots']=[str(v) for v in p]
                certificates['seed_106_core']=[[str(v) for v in row] for row in s]
            if j==100:
                for margin in (F(1,100),F(1,50),F(1,20),F(1,10),F(9,20)):
                    passed,p=ldl(sub(s,scale(margin,eye(6))))
                    diagnostics['six_core_410_margin_'+str(margin)]=passed
                    if passed:
                        certificates['seed_margin']=str(margin)
                        certificates['seed_pivots']=[str(v) for v in p]
                certificates['seed_6core']=[[str(v) for v in row] for row in s]
        a=inv(x)
        e=EP if j%2==0 else EM
        g=sub(g,mm(r,mm(a,transpose(r))))
        h=sub(h,mm(transpose(w),mm(a,w)))
        c=sub(c,mm(r,mm(a,w)))
        r=scale(-1,mm(r,mm(a,e)))
        w=scale(-1,mm(transpose(e),mm(a,w)))
        x=sub(D,mm(transpose(e),mm(a,e)))
    checks['finite_50_through_410_all_positive']=all(z['positive'] for z in finite)
    checks['local_L_variation_lt_1over10000']=F(3,2)*F(14364)*2*F(1,10**10) < F(1,10000)
    checks['sqrt_two_fifths_plus_1over10000_lt_two_thirds']=(F(2,3)-F(1,10000))**2>F(2,5)
    checks['P_ball_self_map']=F(1,36)+F(4,9)<1
    q=F(2,3); a=F(1,30000); b=F(1,2500); delta=F(4,10**10)
    bound=24*b*b/(1-q*q)+48*a+144*delta
    checks['uniform_core_tail_lt_1over500']=bound<F(1,500)
    certificates['uniform_core_tail_upper']=str(bound)
    certificates['tail_seed_transfer_margin']=str(F(1,50)-F(2,500))
    out={'status':'PASS' if all(checks.values()) else 'FAIL','checks':checks,'diagnostics':diagnostics,'finite':finite,'certificates':certificates,'method':'independent standard-library Fraction arithmetic; no historical repository code executed'}
    path=Path(__file__).with_name('r2_exact_certificate.json')
    path.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'status':out['status'],'checks':checks,'diagnostics':diagnostics,'finite':finite,'certificate_path':str(path),'certificate_sha256':hashlib.sha256(path.read_bytes()).hexdigest()},indent=2))
    assert all(checks.values()), 'Failed required exact check'


if __name__=='__main__':
    run()
