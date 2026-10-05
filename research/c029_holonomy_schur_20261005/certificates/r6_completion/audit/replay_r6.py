"""Independent exact R6 completion audit.
Graphs are reconstructed from quadrilateral-gap positions, then matched to
the stated triangle words. Exact natural-order LDL differs from the primary
interior-first implementation. No primary modules are imported.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json,time
HERE=Path(__file__).resolve().parent
T=[1,1,-1,1,-1,-1,1,-1]

def build(k):
    q,rem=divmod(k,3);js=[q]*(3-rem)+[q+1]*rem
    lengths=[8*j+2 for j in js];N=sum(lengths)
    Q=[-1]*N;s=0
    for j,h in zip(js,lengths):
        for u in range(0,8*j,4):Q[s+u]=1
        s+=h
    tau=[1]
    for x in Q[:-1]:tau.append(tau[-1]*x)
    assert tau[-1]*Q[-1]==tau[0]
    expected=sum([T*j+[1,-1] for j in js],[])
    assert tau==expected
    edges={}
    for v in range(N):
        for d in [1,2]:
            u=(v+d)%N;edge=tuple(sorted((u,v)));assert edge not in edges
            edges[edge]=1 if d==1 else tau[v]
    A=[{} for _ in range(N)]
    for (u,v),c in edges.items():A[u][v]=A[v][u]=c
    assert len(edges)==2*N and all(len(row)==4 for row in A)
    # Build only the upper triangle of the normalized cap matrix.
    M=[]
    for i in range(N):
        row={i:F(198,25)}
        for v,c in A[i].items():
            for j,d in A[v].items():
                if j>=i:row[j]=row.get(j,F(0))-c*d
        M.append({j:x for j,x in row.items() if x})
    positives=[i for i,x in enumerate(Q) if x==1]
    gaps=[(positives[(i+1)%len(positives)]-u)%N for i,u in enumerate(positives)]
    return js,lengths,tau,gaps,M

def ldl(A):
    A=[dict(row) for row in A];piv=[]
    for i,row in enumerate(A):
        d=row.get(i,F(0));piv.append(d)
        if d<=0:return False,piv
        neighbors=sorted(j for j in row if j>i)
        for pos,j in enumerate(neighbors):
            factor=row[j]/d
            for k in neighbors[pos:]:
                v=A[j].get(k,F(0))-factor*row[k]
                if v:A[j][k]=v
                else:A[j].pop(k,None)
        A[i]={}
    return True,piv

def run():
    start=time.time();source=json.loads((HERE.parent/'r6_completion_certificate.json').read_text())
    checks={};rows=[]
    for k in range(6,39):
        js,lengths,tau,gaps,M=build(k);n=len(tau);ok,piv=ldl(M)
        checks[f'n{n}_positive']=ok and len(piv)==n
        checks[f'n{n}_three_gaps']=gaps.count(6)==3 and all(g in [4,6] for g in gaps) and len(gaps)==2*k
        checks[f'n{n}_floor_formula']=js==[(k+i)//3 for i in range(3)] and sum(js)==k and n==8*k+6
        old=next(x for x in source['finite_rows'] if x['k']==k)
        checks[f'n{n}_construction_matches']=old['n']==n and old['j_values']==js and old['cell_orders']==lengths and old['gap_word']==gaps and old['holonomy']==1
        rows.append({'k':k,'n':n,'j_values':js,'cell_orders':lengths,'positive':ok,'positive_pivot_count':len(piv),'normalized_pivot_sha256':hashlib.sha256('\n'.join(map(str,piv)).encode()).hexdigest(),'pivot_first':str(piv[0]),'pivot_last':str(piv[-1])})
        print('natural LDL',n,ok,flush=True)
    checks['complete_base_orders']=[x['n'] for x in rows]==list(range(54,311,8))
    checks['tail_first_cells']=[8*((39+i)//3)+2 for i in range(3)]==[106]*3
    checks['tail_first_order']=3*106==318
    checks['endpoint']=8-F(200,54**2)==F(5782,729)
    checks['positive_endpoint_gap']=F(5782,729)-F(198,25)==F(208,18225)>0
    # Supplemental check for the stated all-even >=48 witness corollary:
    # sqrt(5)<5/2; sqrt(15)<39/10 imply period-eight radius squared <79/10.
    checks['period8_radical_bound']=F(5)<F(5,2)**2 and F(15)<F(39,10)**2
    checks['benchmark48_above_79over10']=8-F(200,48**2)>F(79,10)
    assert all(checks.values()),[k for k,v in checks.items() if not v]
    result={'status':'PASS','check_count':len(checks),'checks':checks,'finite_rows':rows,'finite_count':33,'tail':{'k_min':39,'n_min':318,'min_cell':106,'dependency':'unequal_cells/UNEQUAL_CELL_SCHUR_THEOREM.md'},'benchmark_lower_at54':'5782/729','endpoint_gap':'208/18225','seconds':time.time()-start,'method':'Independent quadrilateral-gap graph reconstruction and normalized natural-order rational LDL. Primary file read only to compare construction metadata; its positivity flags are not used.'}
    (HERE/'independent_replay.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':result['status'],'checks':len(checks),'finite_graphs':33,'seconds':result['seconds']},indent=2),flush=True)
if __name__=='__main__':run()
