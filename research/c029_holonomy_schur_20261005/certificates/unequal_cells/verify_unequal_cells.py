"""Exact new checks for unequal one-G6 cell concatenations.

Requires only the sibling assembly.py and the Python standard library.
The upstream fixed-energy Riccati premises remain in the frozen R2 packages.
"""
from fractions import Fraction as F
from pathlib import Path
import json,hashlib
from assembly import graph,direct_core,assembled_core


def sparse_ldl(matrix):
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


def test_full(lengths,alpha,cap):
    M,_,_=graph(lengths,alpha,cap)
    return sparse_ldl([{j:x for j,x in enumerate(row) if x} for row in M])


def run():
    checks={};assembly_rows=[]
    for lengths in [(10,18),(18,26),(10,18,26),(10,10),(10,),(18,)]:
        for alpha in (-1,1):
            okay=direct_core(lengths,alpha)==assembled_core(lengths,alpha)
            name='assembly_'+'_'.join(map(str,lengths))+'_alpha'+str(alpha)
            checks[name]=okay
            assembly_rows.append({'lengths':lengths,'alpha':alpha,'exact':okay})
    parameters=[]
    for cap,J,radius,q,a,gamma,epsilon in [(F(198,25),24,F(1,10**10),F(2,3),F(1,30000),F(1,50),F(1,500)),(F(790537,100000),48,F(1,10**18),F(3,4),F(1,9000000000),F(1,10**6),F(1,10**8))]:
        b=12*a;theta=q*q
        error=12*b*b/(1-q*q)+576*radius+32*a
        checks['degree_two_error_'+str(cap)]=error<epsilon
        checks['positive_margin_'+str(cap)]=gamma-2*epsilon>0
        parameters.append({'cap':str(cap),'J':J,'minimum_cell_order':4*(J+2)+2,'radius':str(radius),'q':str(q),'theta':str(theta),'a':str(a),'b':str(b),'degree_two_error_at_zero':str(error),'epsilon':str(epsilon),'core_margin':str(gamma-2*epsilon)})
    checks['cross_edge_constant']=16**2>9*28
    finite=[]
    for k in range(6,26):
        js=[k//2,(k+1)//2];hs=[8*j+2 for j in js]
        okay,piv=test_full(hs,-1,F(198,25))
        finite.append({'k':k,'n':8*k+4,'j_values':js,'cell_orders':hs,'positive':okay,'pivot_count':len(piv),'pivot_sha256':hashlib.sha256('\n'.join(str(v) for v in piv).encode()).hexdigest()})
    checks['full_R4_finite_bases_positive']=all(row['positive'] for row in finite)
    checks['full_R4_complete_finite_coverage']=[r['n'] for r in finite]==list(range(52,205,8))
    checks['full_R4_endpoint_cap_strict']=F(198,25)<F(2679,338)
    checks['full_R4_endpoint_benchmark']=F(8)-F(200,52**2)==F(2679,338)
    obstructions=[]
    for lengths in [(10,18),(18,26),(26,34),(34,42)]:
        for cap in (F(198,25),F(790537,100000)):
            okay,piv=test_full(lengths,-1,cap)
            row={'lengths':lengths,'cap':str(cap),'positive':okay,'pivot_count':len(piv)}
            if not okay:row.update({'strict_negative_pivot':piv[-1]<0,'first_nonpositive_pivot':str(piv[-1]),'positive_predecessors':all(p>0 for p in piv[:-1])})
            obstructions.append(row)
    witness=next(row for row in obstructions if row['lengths']==(26,34) and row['cap']==str(F(790537,100000)))
    checks['nearbalanced_R4_n60_sharp_cap_fails']=not witness['positive'] and witness['strict_negative_pivot'] and witness['positive_predecessors']
    out={'status':'PASS' if all(checks.values()) else 'FAIL','checks':checks,'assembly_checks':assembly_rows,'uniform_parameters':parameters,'full_R4_finite_bases':finite,'short_cell_falsification':obstructions,'method':'exact full-graph scalar Schur equality, sparse rational LDL, and rational tail inequalities; upstream Riccati premises cited separately'}
    path=Path(__file__).with_name('unequal_cells_certificate.json');path.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'status':out['status'],'checks':checks,'uniform_parameters':parameters,'full_R4_finite_bases':finite,'short_cell_falsification':obstructions,'certificate_path':str(path),'certificate_sha256':hashlib.sha256(path.read_bytes()).hexdigest()},indent=2));assert all(checks.values())


if __name__=='__main__':run()
