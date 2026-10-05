"""Exact matrix construction and unequal one-G6 Schur assembly primitives."""
from fractions import Fraction as F
from pathlib import Path
import json

T=(1,1,-1,1,-1,-1,1,-1)
CAP=F(790537,100000)

def tr(a):return list(map(list,zip(*a)))
def mm(a,b):return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]
def add(a,b):return [[x+y for x,y in zip(row,s)] for row,s in zip(a,b)]
def neg(a):return [[-x for x in row] for row in a]
def sub(a,b):return add(a,neg(b))
def zero(m,n):return [[F(0) for j in range(n)] for i in range(m)]
def inv(a):
 n=len(a);b=[row[:]+[F(i==j) for j in range(n)] for i,row in enumerate(a)]
 for k in range(n):
  p=b[k][k];assert p!=0;b[k]=[x/p for x in b[k]]
  for i in range(n):
   if i!=k:
    q=b[i][k];b[i]=[x-q*y for x,y in zip(b[i],b[k])]
 return [row[n:] for row in b]

def mats(t):
 d=[[t-4 if i==j else F(-1) if {i,j} in ({0,2},{1,3}) else F(0) for j in range(4)] for i in range(4)]
 ep=[[F(x) for x in row] for row in [[-1,0,0,0],[0,1,0,0],[-1,2,1,0],[2,-1,0,-1]]]
 em=[[F(x) for x in row] for row in [[-1,0,0,0],[0,1,0,0],[-1,-2,1,0],[-2,-1,0,-1]]]
 rr=[[F(x) for x in row] for row in [[-1,-2,1,0],[-2,-1,0,-1]]]
 ww=[[F(x) for x in row] for row in [[0,0,-1,0],[0,0,0,1],[0,0,0,0],[0,0,0,0]]]
 cc=[[F(x) for x in row] for row in [[-1,0,-1,0],[0,-1,0,-1]]]
 gg=[[t-4 if i==j else F(0) for j in range(2)] for i in range(2)]
 b=[x+y for x,y in zip(gg,cc)]+[x+y for x,y in zip(tr(cc),d)]
 u=rr+tr(ww)
 v=[ [F(0),F(0)]+row for row in ep]
 return d,ep,em,b,u,v

def graph(lengths,alpha,t=CAP):
 tau=[];starts=[];pos=0
 for h in lengths:
  assert h>=10 and h%8==2
  starts.append(pos);pos+=h;tau+=list(T)*((h-2)//8)+[1,-1]
 n=len(tau);a=[1]*(n-1)+[alpha];adj=[{} for i in range(n)]
 for i in range(n):
  for step,s in [(1,a[i]),(2,tau[i]*a[i]*a[(i+1)%n])]:
   j=(i+step)%n;assert j not in adj[i];adj[i][j]=adj[j][i]=s
 out=[[t if i==j else F(0) for j in range(n)] for i in range(n)]
 for i in range(n):
  for j,s in adj[i].items():
   for k,v in adj[j].items():out[i][k]-=s*v
 keep=[];inside=[]
 for b,h in zip(starts,lengths):
  keep += [b,b+1]+[(b+i)%n for i in (-4,-3,-2,-1)]
  inside+=list(range(b+2,b+h-4))
 assert len(set(keep+inside))==n
 return out,keep,inside

def direct_core(lengths,alpha,t=CAP):
 m,keep,inside=graph(lengths,alpha,t);order=inside+keep
 a=[[m[i][j] for j in order] for i in order]
 piv=[]
 for k in range(len(inside)):
  p=a[k][k];piv.append(p);assert p>0
  for i in range(k+1,len(a)):
   for j in range(i,len(a)):
    a[i][j]=a[j][i]=a[i][j]-a[i][k]*a[k][j]/p
 a=[row[len(inside):] for row in a[len(inside):]]
 # Canonical gauge on the H slot of K_0 moves the global seam phase
 # onto the incoming chain's terminal coupling.
 factors=[1,1]+[alpha]*4+[1]*(len(a)-6)
 return [[a[i][j]*factors[i]*factors[j] for j in range(len(a))] for i in range(len(a))]

def assembled_core(lengths,alpha,t=CAP):
 d,ep,em,b,u0,v=mats(t);r=len(lengths);s=zero(6*r,6*r)
 def put(i,j,a):
  for x in range(6):
   for y in range(6):s[6*i+x][6*j+y]+=a[x][y]
 for i in range(r):put(i,i,b)
 for i,h in enumerate(lengths):
  p=(h-2)//4-2;x=d;u=u0;loss=zero(6,6)
  for j in range(p+1):
   xi=inv(x);loss=add(loss,mm(u,mm(xi,tr(u))))
   if j==p:
    right=mm(tr(v),mm(xi,v));cross=mm(u,mm(xi,v))
    omega=alpha if i==r-1 else 1
    put(i,i,neg(loss));put((i+1)%r,(i+1)%r,neg(right))
    cross=[[-omega*z for z in row] for row in cross]
    put(i,(i+1)%r,cross);put((i+1)%r,i,tr(cross))
   else:
    e=ep if j%2==0 else em
    u=neg(mm(u,mm(xi,e)));x=sub(d,mm(tr(e),mm(xi,e)))
 return s

if __name__=='__main__':
 rows=[]
 for lengths in [(10,18),(18,26),(10,18,26),(10,10),(10,), (18,)]:
  for alpha in (-1,1):
   rows.append({'lengths':lengths,'alpha':alpha,'exact_assembly_matches_direct':direct_core(lengths,alpha)==assembled_core(lengths,alpha)})
 out={'status':'PASS' if all(x['exact_assembly_matches_direct'] for x in rows) else 'FAIL','rows':rows}
 Path(__file__).with_name('first_assembly_checks.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
 assert out['status']=='PASS'
