"""Independent exact graph and isolated-chain checks for unequal cells.
No imports from primary verifiers or prior audit modules.
"""
from fractions import Fraction as F
from pathlib import Path
from hashlib import sha256
import json,time
T=[1,1,-1,1,-1,-1,1,-1]

def block_data(cap):
    D=[[cap-4 if i==j else F(-1) if {i,j} in ({0,2},{1,3}) else F(0) for j in range(4)] for i in range(4)]
    E=[[-1,0,0,0],[0,1,0,0],[-1,2,1,0],[2,-1,0,-1]]
    Fm=[[-1,0,0,0],[0,1,0,0],[-1,-2,1,0],[-2,-1,0,-1]]
    R=[[-1,-2,1,0],[-2,-1,0,-1]]
    W=[[0,0,-1,0],[0,0,0,1],[0,0,0,0],[0,0,0,0]]
    C=[[-1,0,-1,0],[0,-1,0,-1]]
    B=[[F(0) for _ in range(6)] for _ in range(6)]
    for i in range(2):B[i][i]=cap-4
    for i in range(4):
        for j in range(4):B[i+2][j+2]=D[i][j]
    for i in range(2):
        for j in range(4):B[i][j+2]=B[j+2][i]=F(C[i][j])
    U=R+[list(row) for row in zip(*W)]
    V=[[0,0]+row for row in E]
    return D,E,Fm,B,U,V

def add(a,i,j,x):
    x=F(x)
    if not x:return
    a[i][j]=a[i].get(j,F(0))+x
    if not a[i][j]:del a[i][j]

def rect(a,rows,cols,M,sign=1):
    assert not(set(rows)&set(cols))
    for u,i in enumerate(rows):
        for v,j in enumerate(cols):add(a,i,j,sign*M[u][v]);add(a,j,i,sign*M[u][v])

def diag(a,ids,M):
    for u,i in enumerate(ids):
        for v,j in enumerate(ids):add(a,i,j,M[u][v])

def vertices(lengths):
    N=sum(lengths);starts=[];s=0;K=[];chains=[]
    for h in lengths:
        assert h>=10 and h%8==2
        starts.append(s);K.append([s,s+1]+[(s-d)%N for d in [4,3,2,1]])
        chains.append(list(range(s+2,s+h-4)));s+=h
    assert sorted(sum(K,[])+sum(chains,[]))==list(range(N))
    return K,chains

def direct(lengths,alpha,cap,gauged=False):
    tau=sum([T*((h-2)//8)+[1,-1] for h in lengths],[]);N=len(tau)
    A=[{} for _ in range(N)]
    for i in range(N):
        for d in [1,2]:
            j=(i+d)%N;sgn=(1 if d==1 else tau[i])*(alpha if i+d>=N else 1)
            assert j not in A[i];A[i][j]=A[j][i]=sgn
    assert all(len(row)==4 for row in A)
    M=[{i:cap} for i in range(N)]
    for i,row in enumerate(A):
        for j,x in row.items():
            for k,y in A[j].items():add(M,i,k,-x*y)
    if gauged:
        K,_=vertices(lengths);sw=set(K[0][2:])
        for i,row in enumerate(M):
            for j in row:row[j]*=(alpha if i in sw else 1)*(alpha if j in sw else 1)
    return M

def template(lengths,alpha,cap):
    K,chains=vertices(lengths);D,E,Fm,B,U,V=block_data(cap);N=sum(lengths);a=[{} for _ in range(N)];r=len(K)
    for ids in K:diag(a,ids,B)
    for i,ids in enumerate(chains):
        blocks=[ids[j:j+4] for j in range(0,len(ids),4)]
        for b in blocks:diag(a,b,D)
        for j in range(len(blocks)-1):rect(a,blocks[j],blocks[j+1],E if j%2==0 else Fm)
        rect(a,K[i],blocks[0],U)
        rect(a,blocks[-1],K[(i+1)%r],V,alpha if i==r-1 else 1)
    return a

def eliminate(a,order,keep):
    # Upper-triangle scalar Schur algorithm, with explicit arbitrary ordering.
    permutation=order+keep;pos={v:i for i,v in enumerate(permutation)}
    A=[{pos[j]:F(x) for j,x in a[v].items() if pos[j]>=i} for i,v in enumerate(permutation)];piv=[]
    for k in range(len(order)):
        row=A[k];p=row.get(k,F(0));piv.append(p)
        if p<=0:return False,piv,None
        ns=sorted(j for j in row if j>k)
        for u,i in enumerate(ns):
            for j in ns[u:]:
                v=A[i].get(j,F(0))-row[i]*row[j]/p
                if v:A[i][j]=v
                else:A[i].pop(j,None)
        A[k]={}
    offset=len(order)
    core=[[A[min(i,j)].get(max(i,j),F(0)) for j in range(offset,len(A))] for i in range(offset,len(A))]
    return True,piv,core

def isolated_chain(h,omega,cap):
    # Build a separate path with distinct left/right six-dimensional boundaries.
    # Boundaries have zero diagonal here; the core records only Schur losses.
    D,E,Fm,_,U,V=block_data(cap);n=h-6;a=[{} for _ in range(n+12)]
    blocks=[list(range(j,j+4)) for j in range(0,n,4)]
    for b in blocks:diag(a,b,D)
    for j in range(len(blocks)-1):rect(a,blocks[j],blocks[j+1],E if j%2==0 else Fm)
    rect(a,list(range(n,n+6)),blocks[0],U)
    rect(a,blocks[-1],list(range(n+6,n+12)),V,omega)
    ok,piv,core=eliminate(a,list(range(n)),list(range(n,n+12)));assert ok
    return core

def assembled(lengths,alpha,cap):
    r=len(lengths);_,_,_,B,_,_=block_data(cap)
    out=[[F(0) for _ in range(6*r)] for _ in range(6*r)]
    for i in range(r):
        for u in range(6):
            for v in range(6):out[6*i+u][6*i+v]+=B[u][v]
    for i,h in enumerate(lengths):
        C=isolated_chain(h,alpha if i==r-1 else 1,cap)
        dest=list(range(6*i,6*i+6))+list(range(6*((i+1)%r),6*((i+1)%r)+6))
        for u in range(12):
            for v in range(12):out[dest[u]][dest[v]]+=C[u][v]
    return out

def run():
    start=time.time();checks={};cases=[]
    # Loops, two parallel chains, and genuinely unequal cycles with >=3 cells.
    shapes=[(10,),(18,),(106,),(202,),(10,10),(10,18),(18,26),(106,114),(202,210),(10,18,26),(18,10,34,26),(106,114,122)]
    for cap in [F(198,25),F(790537,100000)]:
        for lengths in shapes:
            for alpha in [-1,1]:
                M=direct(lengths,alpha,cap,True)
                label='_'.join(map(str,lengths))+'_'+str(alpha)+'_'+str(cap)
                checks['raw_template_'+label]=M==template(lengths,alpha,cap)
                K,chains=vertices(lengths)
                ok,piv,C=eliminate(M,sum(chains,[]),sum(K,[]));assert ok
                checks['isolated_chain_sum_'+label]=C==assembled(lengths,alpha,cap)
                cases.append({'lengths':lengths,'alpha':alpha,'cap':str(cap),'positive_bulk_pivots':len(piv),'template_equal':checks['raw_template_'+label],'schur_equal':checks['isolated_chain_sum_'+label]})
        print('assembly cap',cap,'complete',flush=True)
    finite=[]
    for k in range(6,26):
        lengths=[8*(k//2)+2,8*((k+1)//2)+2];n=sum(lengths)
        ok,piv,_=eliminate(direct(lengths,-1,F(198,25)),list(range(n)),[])
        finite.append({'k':k,'n':n,'lengths':lengths,'positive':ok,'natural_order_pivots':len(piv),'pivot_sha256':sha256('\n'.join(map(str,piv)).encode()).hexdigest()})
    obstructions=[]
    for lengths in [(26,34),(34,42)]:
        n=sum(lengths)
        ok,piv,_=eliminate(direct(lengths,-1,F(790537,100000)),list(range(n)),[])
        checks['changed_sharp_obstruction_'+str(n)]=(not ok and piv[-1]<0 and all(p>0 for p in piv[:-1]))
        obstructions.append({'n':n,'lengths':lengths,'cap':'790537/100000','positive_prefix_count':len(piv)-1,'first_negative_pivot':str(piv[-1]),'pivot_prefix':[str(p) for p in piv]})
    checks['all_twenty_bases_positive']=all(row['positive'] for row in finite)
    checks['coverage_52_through_204']=[row['n'] for row in finite]==list(range(52,205,8))
    checks['analytic_starts_212']=8*(26//2)+2==106 and 8*((26+1)//2)+2==106
    parameters=[]
    for cap,J,r0,q,a,gamma,eps in [(F(198,25),24,F(1,10**10),F(2,3),F(1,30000),F(1,50),F(1,500)),(F(790537,100000),48,F(1,10**18),F(3,4),F(1,9000000000),F(1,10**6),F(1,10**8))]:
        err=12*(12*a)**2/(1-q*q)+576*r0+32*a
        checks['uniform_degree_two_error_'+str(cap)]=err<eps
        checks['positive_two_error_margin_'+str(cap)]=gamma-2*eps>0
        parameters.append({'cap':str(cap),'entrance':J,'min_cell':4*(J+2)+2,'error':str(err),'epsilon':str(eps),'margin':str(gamma-2*eps)})
    checks['cross_constant']=9*28<16**2
    checks['benchmark_at_52']=F(198,25)<8-F(200,52**2)
    # Independent polynomial gap data confirms exactly one G6 per legal cell.
    for lengths in shapes:
        tau=sum([T*((h-2)//8)+[1,-1] for h in lengths],[]);n=len(tau)
        plus=[i for i in range(n) if tau[i]*tau[(i+1)%n]==1]
        gaps=[(plus[(i+1)%len(plus)]-v)%n for i,v in enumerate(plus)]
        checks['gap_count_'+str(lengths)]=gaps.count(6)==len(lengths) and all(g in [4,6] for g in gaps)
    assert all(checks.values()),[k for k,v in checks.items() if not v]
    out={'status':'PASS','check_count':len(checks),'checks':checks,'assembly_cases':cases,'finite_bases':finite,'sharp_obstructions':obstructions,'parameters':parameters,'seconds':time.time()-start,'method':'Independent edge graph, raw gauge/template comparison, scalar Schur elimination, separate isolated-chain Schur sums, and natural-order finite LDL. No primary imports.'}
    path=Path(__file__).with_name('independent_replay.json');path.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'status':out['status'],'check_count':len(checks),'assembly_cases':len(cases),'seconds':out['seconds']},indent=2),flush=True)
if __name__=='__main__':run()
