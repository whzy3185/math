"""Exact structural and finite-base checks for the balanced R4 pilot.

New standalone Python-standard-library code. Floating spectral routines are
not used for any acceptance test.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

CAP=F(790537,100000)
T=(1,1,-1,1,-1,-1,1,-1)
EP=[[-1,0,0,0],[0,1,0,0],[-1,2,1,0],[2,-1,0,-1]]
EM=[[-1,0,0,0],[0,1,0,0],[-1,-2,1,0],[-2,-1,0,-1]]
R0=[[-1,-2,1,0],[-2,-1,0,-1]]
C0=[[-1,0,-1,0],[0,-1,0,-1]]
W0=[[0,0,-1,0],[0,0,0,1],[0,0,0,0],[0,0,0,0]]


def signed_graph(tau,alpha):
    n=len(tau);a=[1]*(n-1)+[alpha];adj=[{} for _ in range(n)]
    for i in range(n):
        for step,sgn in ((1,a[i]),(2,tau[i]*a[i]*a[(i+1)%n])):
            j=(i+step)%n
            assert j not in adj[i]
            adj[i][j]=adj[j][i]=sgn
    return adj


def repeated_cell(h,r,alpha):
    assert h>=10 and h%8==2 and r>=1
    tau=list(T)*((h-2)//8)+[1,-1]
    return signed_graph(tau*r,alpha)


def balanced_r4(k):
    n=8*k+4;half=4*k+2;q=[-1]*n
    for i in range(k):q[4*i]=q[half+4*i]=1
    tau=[1]
    for i in range(n-1):tau.append(tau[-1]*q[i])
    assert tau[-1]*q[-1]==1
    return signed_graph(tau,-1)


def sparse_cap_matrix(adj,cap):
    n=len(adj);a=[]
    for i in range(n):
        row={i:cap.numerator}
        for j,x in adj[i].items():
            for k,y in adj[j].items():row[k]=row.get(k,0)-cap.denominator*x*y
        a.append({j:F(v) for j,v in row.items() if v})
    return a


def sparse_ldl(matrix):
    n=len(matrix)
    order=list(range(4,n-4))+list(range(4))+list(range(n-4,n))
    pos={old:new for new,old in enumerate(order)}
    a=[{pos[j]:x for j,x in matrix[i].items()} for i in order]
    piv=[]
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


def digest(piv):
    return hashlib.sha256('\n'.join(str(p) for p in piv).encode()).hexdigest()


def padd(a,b):
    out=a.copy()
    for k,x in b.items():out[k]=out.get(k,0)+x
    return {k:x for k,x in out.items() if x}


def pmul(a,b):
    out={}
    for i,x in a.items():
        for j,y in b.items():out[i+j]=out.get(i+j,0)+x*y
    return {k:x for k,x in out.items() if x}


def phased_adjacency(h):
    tau=list(T)*((h-2)//8)+[1,-1]
    rows=[{} for _ in range(h)]
    for i in range(h):
        for step,sgn in [(1,1),(-1,1),(2,tau[i]),(-2,tau[(i-2)%h])]:
            q,j=divmod(i+step,h)
            rows[i][j]=padd(rows[i].get(j,{}),{q:sgn})
    return rows


def laurent_template_check(h):
    A=phased_adjacency(h)
    M=[{i:{0:CAP}} for i in range(h)]
    for i,row in enumerate(A):
        for j,a in row.items():
            for k,b in A[j].items():
                term={p:-v for p,v in pmul(a,b).items()}
                M[i][k]=padd(M[i].get(k,{}),term)
    M=[{j:p for j,p in row.items() if p} for row in M]
    m=(h-2)//4
    blocks=[[0,1]]+[list(range(2+4*j,6+4*j)) for j in range(m)]
    E=[{} for _ in range(h)]
    def put(bi,bj,values,power=0):
        for ri,i in enumerate(blocks[bi]):
            for cj,j in enumerate(blocks[bj]):
                value=values[ri][cj]
                if value:
                    E[i][j]=padd(E[i].get(j,{}),{power:value})
                    if i!=j:E[j][i]=padd(E[j].get(i,{}),{-power:value})
    d=[[CAP-4 if i==j else -1 if {i,j} in [{0,2},{1,3}] else 0 for j in range(4)] for i in range(4)]
    # Diagonal blocks need only their upper triangles to avoid double insertion.
    for i in range(h):E[i][i]={0:CAP-4}
    for block in blocks[1:]:
        for i,j in [(block[0],block[2]),(block[1],block[3])]:E[i][j]=E[j][i]={0:-1}
    for j in range(1,m):put(j,j+1,EP if j%2 else EM)
    put(0,1,R0)
    put(0,m,C0,-1)
    put(1,m,W0,-1)
    return M==E


def gadd(a,b):return (a[0]+b[0],a[1]+b[1])
def gmul(a,b):return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def ipow(k):return [(1,0),(0,1),(-1,0),(0,-1)][k%4]


def fiber_check(h,phase):
    A=repeated_cell(h,2,-1);B=phased_adjacency(h)
    for i,row in enumerate(A):
        lhs={}
        for j,value in row.items():
            c,s=divmod(j,h)
            lhs[s]=gadd(lhs.get(s,(0,0)),gmul((value,0),ipow(phase*c)))
        c,s=divmod(i,h)
        rhs={}
        for j,pol in B[s].items():
            for power,value in pol.items():
                rhs[j]=gadd(rhs.get(j,(0,0)),gmul((value,0),ipow(phase*(c+power))))
        lhs={j:x for j,x in lhs.items() if x!=(0,0)}
        rhs={j:x for j,x in rhs.items() if x!=(0,0)}
        if lhs!=rhs:return False
    return True


def run():
    checks={}
    for h in (18,26,34,106,202):checks[f'laurent_block_template_h{h}']=laurent_template_check(h)
    for h in (10,18,26,34):
        checks[f'R4_repeated_cell_equals_balanced_h{h}']=repeated_cell(h,2,-1)==balanced_r4((h-2)//4)
        for phase in (1,-1):checks[f'exact_fiber_embedding_h{h}_phase{phase}']=fiber_check(h,phase)
    finite=[]
    for j in range(1,25):
        h=8*j+2;n=2*h
        positive,pivs=sparse_ldl(sparse_cap_matrix(repeated_cell(h,2,-1),CAP))
        finite.append({'j':j,'cell_order':h,'n':n,'positive':positive,'pivot_count':len(pivs),'pivot_sha256':digest(pivs)})
    checks['all_24_R4_bases_positive']=all(row['positive'] for row in finite)
    checks['complete_base_coverage']=[row['n'] for row in finite]==list(range(20,389,16))
    # A strict obstruction to accidentally extending the sharp cap to odd k.
    positive,pivs=sparse_ldl(sparse_cap_matrix(balanced_r4(7),CAP))
    checks['odd_k_n60_strict_obstruction']=(not positive and pivs[-1]<0 and all(p>0 for p in pivs[:-1]))
    out={'status':'PASS' if all(checks.values()) else 'FAIL','cap':str(CAP),'checks':checks,'finite':finite,'odd_k_obstruction':{'k':7,'n':60,'first_negative_pivot':str(pivs[-1]),'positive_predecessor_count':len(pivs)-1,'ldl_prefix':[str(p) for p in pivs]},'method':'exact Laurent-polynomial block identities; exact Gaussian-integer fiber embeddings; direct sparse rational LDL on full real graphs'}
    path=Path(__file__).with_name('r4_pilot_certificate.json');path.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'status':out['status'],'checks':checks,'finite':finite,'certificate_path':str(path),'certificate_sha256':hashlib.sha256(path.read_bytes()).hexdigest()},indent=2))
    assert all(checks.values())


if __name__=='__main__':run()
