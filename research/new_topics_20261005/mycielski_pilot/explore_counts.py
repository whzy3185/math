from pathlib import Path
import json,time

def myc(adj):
 n=len(adj); out=[0]*(2*n+1)
 for i,a in enumerate(adj):
  out[i]=a|(a<<n);out[i+n]=a|(1<<(2*n))
 out[2*n]=((1<<n)-1)<<n
 return out

def independent_sets(adj):
 def rec(cand,chosen):
  yield chosen
  while cand:
   bit=cand&-cand; cand^=bit;v=bit.bit_length()-1
   yield from rec(cand&~adj[v],chosen|bit)
 return rec((1<<len(adj))-1,0)

def candidates(adj):
 n=len(adj);full=(1<<n)-1
 noapex=set();apex=set();count=0
 for I in independent_sets(adj):
  count+=1;N=0;t=I
  while t:
   b=t&-t;t^=b;N|=adj[b.bit_length()-1]
  C=full&~N
  # Complete the original part by every vertex whose neighbor set is in N.
  # These extra vertices have no neighbor in I or in one another.
  J=I
  for v in range(n):
   if adj[v]&~N==0: J|=1<<v
  assert J&N==0
  noapex.add(J|(C<<n))
  if I|N==full: apex.add(I|(1<<(2*n)))
 return count,sorted(noapex|apex)

if __name__=='__main__':
 a=[2,1]
 for r in range(2,6):
  t=time.monotonic();cnt,mis=candidates(a)
  print(r,len(a),'independent',cnt,'Mnext maximal candidate',len(mis),'time',time.monotonic()-t,flush=True)
  if r==5:
   out=Path(__file__).resolve().parent
   (out/'m6_candidates.json').write_text(json.dumps({'base_adj':a,'adj':myc(a),'candidate_masks':mis,'base_independent_sets':cnt}))
  a=myc(a)
