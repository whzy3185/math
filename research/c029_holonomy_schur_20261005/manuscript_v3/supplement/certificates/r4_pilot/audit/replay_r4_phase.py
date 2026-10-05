"""Independent graph-level exact replay of balanced R4 and phase assembly.
No primary verifier imports. All acceptance checks are rational/Laurent exact.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json,time
C=F(790537,100000)
T=[1,1,-1,1,-1,-1,1,-1]

# Laurent polynomials in a unit complex phase; conjugation reverses powers.
def plus(a,b):
    d=a.copy()
    for k,v in b.items(): d[k]=d.get(k,F(0))+v
    return {k:v for k,v in d.items() if v}
def times(a,b):
    d={}
    for i,x in a.items():
        for j,y in b.items(): d[i+j]=d.get(i+j,F(0))+x*y
    return {k:v for k,v in d.items() if v}
def scale(a,c):return {k:v*c for k,v in a.items() if v*c}
def conj(a):return {-k:v for k,v in a.items()}
def shift(a,k):return {j+k:v for j,v in a.items()}
def evalone(a):return sum(a.values(),F(0))

def flux_from_gaps(k):
    n=8*k+4
    # Two identical blocks of cyclic square-flux data; spacing is 4,...,4,6.
    q=[-1]*n
    for i in range(0,4*k,4):q[i]=q[4*k+2+i]=1
    tau=[1]
    for v in q[:-1]:tau.append(tau[-1]*v)
    assert tau[-1]*q[-1]==tau[0]
    return tau

def graph(tau,alpha):
    n=len(tau);out=[{} for _ in range(n)]
    for v in range(n):
        for d in (1,2):
            w=(v+d)%n
            # Positive Hamilton signs away from one seam, with crossed-step2 correction.
            val=(1 if d==1 else tau[v])*(alpha if v+d>=n else 1)
            assert w not in out[v]
            out[v][w]=out[w][v]=val
    assert all(len(row)==4 for row in out)
    return out

def squarecap(adj):
    a=[]
    for i,row in enumerate(adj):
        r={i:C}
        for j,x in row.items():
            for k,y in adj[j].items():r[k]=r.get(k,F(0))-x*y
        a.append({k:v for k,v in r.items() if v})
    return a

def ldl(a):
    # Natural vertex order differs from the creator's interior-first order.
    a=[{j:F(v) for j,v in row.items() if j>=i} for i,row in enumerate(a)]
    piv=[]
    for k,row in enumerate(a):
        p=row.get(k,F(0));piv.append(p)
        if p<=0:return False,piv
        ns=sorted(j for j in row if j>k)
        for u,i in enumerate(ns):
            for j in ns[u:]:
                a[i][j]=a[i].get(j,F(0))-row[i]*row[j]/p
                if not a[i][j]:del a[i][j]
        a[k]={}
    return True,piv

def phasegraph(h):
    tau=T*((h-2)//8)+[1,-1]
    a=[{} for _ in range(h)]
    for i in range(h):
        for d in (1,2):
            e,j=divmod(i+d,h);sgn=1 if d==1 else tau[i]
            assert j not in a[i]
            a[i][j]={e:F(sgn)};a[j][i]={-e:F(sgn)}
    return a

def phasesquare(h):
    adj=phasegraph(h);a=[{i:{0:C}} for i in range(h)]
    for i,row in enumerate(adj):
        for j,x in row.items():
            for k,y in adj[j].items():a[i][k]=plus(a[i].get(k,{}),scale(times(x,y),-1))
    return [{j:v for j,v in row.items() if v} for row in a]

def open_phase_core(h):
    a=phasesquare(h)
    # Eliminate all but V0, penultimate block and last block, leaving 10 vertices.
    keep=[0,1]+list(range(h-8,h))
    positive=True
    for k in range(2,h-8):
        p=a[k].get(k,{})
        assert set(p)=={0},(h,k,'phase-dependent pivot',p)
        d=p[0];positive &= d>0
        assert d>0
        ns=sorted(j for j in a[k] if j!=k)
        for ii,i in enumerate(ns):
            for j in ns[ii:]:
                v=plus(a[i].get(j,{}),scale(times(a[i][k],a[k][j]),-1/d))
                if v:a[i][j]=v;a[j][i]=conj(v)
                else:a[i].pop(j,None);a[j].pop(i,None)
        for j in ns:a[j].pop(k,None)
        a[k]={}
    core=[[a[i].get(j,{}) for j in keep] for i in keep]
    assert all(core[i][j]==conj(core[j][i]) for i in range(10) for j in range(10))
    E=[[-1,0,0,0],[0,1,0,0],[-1,2,1,0],[2,-1,0,-1]]
    tests=[]
    for i in range(10):
        for j in range(10):
            v=core[i][j]
            # Reverse entries handled by Hermitian symmetry.
            if i>j:continue
            if i<2 and j>=6:
                tests.append(v==({-1:evalone(v)} if evalone(v) else {}))
            elif 2<=i<6 and j>=6:
                residual=plus(v,{0:F(-E[i-2][j-6])})
                tests.append(residual==({-1:evalone(residual)} if evalone(residual) else {}))
            else:tests.append(v==({0:evalone(v)} if evalone(v) else {}))
    return all(tests),h-10

def reduced(p,r,alpha):
    q,k=divmod(p,r)
    return k,(1 if alpha==1 or q%2==0 else -1)

def embedding(h,r,alpha):
    A=graph((T*((h-2)//8)+[1,-1])*r,alpha)
    H=phasegraph(h)
    for i,row in enumerate(A):
        ci,vi=divmod(i,h);left={};right={}
        for j,val in row.items():
            cj,vj=divmod(j,h);key=(vj,cj);left[key]=left.get(key,0)+val
        for vj,pol in H[vi].items():
            for p,val in pol.items():
                k,s=reduced(ci+p,r,alpha);key=(vj,k);right[key]=right.get(key,0)+val*s
        left={k:v for k,v in left.items() if v};right={k:v for k,v in right.items() if v}
        if left!=right:return False
    return True

def hashp(p):return hashlib.sha256('\n'.join(map(str,p)).encode()).hexdigest()

def run():
    start=time.time();checks={};finite=[]
    for j in range(1,25):
        tau=flux_from_gaps(2*j);h=8*j+2
        checks[f'word_j{j}']=tau==(T*j+[1,-1])*2
        ok,p=ldl(squarecap(graph(tau,-1)))
        finite.append({'j':j,'n':2*h,'positive':ok,'natural_order_pivots':len(p),'pivot_sha256':hashp(p)})
        print('base',2*h,ok,flush=True)
    checks['all_24_bases']=all(z['positive'] for z in finite)
    ok,p=ldl(squarecap(graph(flux_from_gaps(7),-1)))
    checks['odd_k60_strict_negative']=not ok and p[-1]<0 and all(x>0 for x in p[:-1])
    obstruction={'n':60,'first_negative_index':len(p)-1,'first_negative_pivot':str(p[-1]),'positive_prefix_count':len(p)-1,'pivot_prefix':[str(x) for x in p]}
    print('odd60',checks['odd_k60_strict_negative'],flush=True)
    for h in [18,26,34,202]:
        ok,count=open_phase_core(h);checks[f'allphase_open_core_h{h}']=ok
        print('Laurent core',h,ok,count,flush=True)
    for h in [10,18,26,202]:
        for r in [1,2,3,4,5]:
            for alpha in [-1,1]:checks[f'general_fiber_h{h}_r{r}_a{alpha}']=embedding(h,r,alpha)
    q=F(3,4);a=F(1,9000000000);b=12*a;r=F(1,10**18)
    tail=24*b*b/(1-q*q)+48*a+576*r
    checks['unchanged_tail_exact']=tail==F(583333407,109375000000000000)
    checks['two_error_seed_margin']=F(1,10**6)-2*tail>F(49,50000000)
    out={'status':'PASS' if all(checks.values()) else 'FAIL','checks':checks,'finite':finite,'obstruction':obstruction,'tail':str(tail),'seconds':time.time()-start,'method':'Independent direct graph reconstruction, natural-order exact LDL, symbolic Laurent scalar Schur elimination, exact quotient-ring Floquet embeddings. No primary-verifier imports.'}
    path=Path(__file__).with_name('independent_replay.json');path.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'status':out['status'],'check_count':len(checks),'seconds':out['seconds'],'path':str(path)},indent=2),flush=True)
    assert all(checks.values())
if __name__=='__main__':run()
