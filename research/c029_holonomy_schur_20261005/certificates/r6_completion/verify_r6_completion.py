"""Exact finite completion of the near-balanced legal-cell R6 family.

Standalone standard-library code. Infinite-length coverage is supplied by
the previously proved unequal-cell Schur theorem, not inferred from tests.
"""
from fractions import Fraction as F
from pathlib import Path
import json,hashlib
T=(1,1,-1,1,-1,-1,1,-1)


def construct(k):
    js=[k//3,(k+1)//3,(k+2)//3]
    tau=[]
    for j in js:tau+=list(T)*j+[1,-1]
    n=len(tau);adj=[{} for _ in range(n)]
    for i in range(n):
        for step,sgn in [(1,1),(2,tau[i])]:
            j=(i+step)%n
            assert j not in adj[i]
            adj[i][j]=adj[j][i]=sgn
    q=[tau[i]*tau[(i+1)%n] for i in range(n)]
    positions=[i for i,x in enumerate(q) if x==1]
    gaps=[(positions[(i+1)%len(positions)]-positions[i])%n for i in range(len(positions))]
    matrix=[]
    for i in range(n):
        row={i:198}
        for j,x in adj[i].items():
            for l,y in adj[j].items():row[l]=row.get(l,0)-25*x*y
        matrix.append({j:F(v) for j,v in row.items() if v})
    return js,tau,q,gaps,matrix


def positive_ldl(matrix):
    n=len(matrix);order=list(range(4,n-4))+list(range(4))+list(range(n-4,n));pos={old:new for new,old in enumerate(order)}
    a=[{pos[j]:x for j,x in matrix[i].items()} for i in order];piv=[]
    for k in range(n):
        p=a[k].get(k,F(0));piv.append(p)
        if p<=0:return False,piv
        neighbors=sorted(j for j in a[k] if j>k)
        for ii,i in enumerate(neighbors):
            ai=a[i][k]
            for j in neighbors[ii:]:
                value=a[i].get(j,F(0))-ai*a[j][k]/p
                if value:a[i][j]=a[j][i]=value
                else:a[i].pop(j,None);a[j].pop(i,None)
        for i in neighbors:a[i].pop(k,None)
        a[k]={k:p}
    return True,piv


def run():
    checks={};rows=[]
    for k in range(6,39):
        js,tau,q,gaps,M=construct(k);n=len(tau)
        positive,piv=positive_ldl(M)
        checks[f'n{n}_parameter_sum']=sum(js)==k and n==8*k+6
        checks[f'n{n}_three_legal_cells']=min(js)>=1 and len(js)==3
        checks[f'n{n}_three_G6_gaps']=gaps.count(6)==3 and all(x in (4,6) for x in gaps) and q.count(1)==2*k
        checks[f'n{n}_positive_full_graph_LDL']=positive and len(piv)==n
        rows.append({'k':k,'n':n,'j_values':js,'cell_orders':[8*j+2 for j in js],'gap_word':gaps,'holonomy':1,'positive':positive,'pivot_count':len(piv),'pivot_sha256':hashlib.sha256('\n'.join(str(v) for v in piv).encode()).hexdigest()})
    checks['finite_coverage_k6_through38']=[r['k'] for r in rows]==list(range(6,39))
    checks['finite_coverage_n54_through310']=[r['n'] for r in rows]==list(range(54,311,8))
    checks['tail_start_k39_all_cells106']=[8*((39+i)//3)+2 for i in range(3)]==[106,106,106]
    checks['tail_start_order318']=8*39+6==318
    checks['benchmark_endpoint']=F(8)-F(200,54**2)==F(5782,729)
    checks['cap_below_endpoint']=F(198,25)<F(5782,729)
    checks['endpoint_strict_margin']=F(5782,729)-F(198,25)==F(208,18225)
    out={'status':'PASS' if all(checks.values()) else 'FAIL','cap':'198/25','checks':checks,'finite_rows':rows,'finite_count':len(rows),'analytic_tail':{'k_min':39,'n_min':318,'minimum_cell_order':106,'dependency':'../unequal_cells/UNEQUAL_CELL_SCHUR_THEOREM.md','logical_reason':'for k>=39 each floor((k+i)/3)>=13, so all three legal cells meet the established minimum-length hypothesis'},'method':'direct signed-graph construction and exact sparse rational LDL of198I-25A^2; no floating acceptance'}
    path=Path(__file__).with_name('r6_completion_certificate.json');path.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'status':out['status'],'required_checks':len(checks),'checks':checks,'finite_count':len(rows),'finite_orders':[r['n'] for r in rows],'certificate_path':str(path),'certificate_sha256':hashlib.sha256(path.read_bytes()).hexdigest()},indent=2));assert all(checks.values())


if __name__=='__main__':run()
