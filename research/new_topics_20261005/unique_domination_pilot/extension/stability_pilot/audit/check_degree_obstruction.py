"""Independent degree and forced-neighborhood checks for the stability obstruction.
No primary code imports. Edge distance means the symmetric-difference size.
"""
from pathlib import Path
from collections import Counter
import json,time
HERE=Path(__file__).resolve().parent

def construct(k,s):
    assert 1<=s<k
    X=list(range(k));Y=list(range(k,2*k));U=[(2*k+2*i,2*k+2*i+1) for i in range(k)];V=[(4*k+2*j,4*k+2*j+1) for j in range(k)];z=6*k;n=z+1
    norm=lambda E:{tuple(sorted(e)) for e in E}
    H=norm([(x,u) for x,us in zip(X,U) for u in us]+[(y,v) for y,vs in zip(Y,V) for v in vs]+[(u,vs[0]) for us in U for u in us for vs in V]+[(z,u) for us in U for u in us]+[(z,y) for y in Y])
    removed=norm([(U[i][0],V[j][0]) for i in range(s) for j in range(k)]+[(z,U[i][0]) for i in range(s)])
    added=norm([(X[i],y) for i in range(s) for y in Y])
    assert removed<=H and not(added&H)
    G=(H-removed)|added
    A=[set() for _ in range(n)];AH=[set() for _ in range(n)]
    for edges,out in [(G,A),(H,AH)]:
        for u,v in edges:out[u].add(v);out[v].add(u)
    L=set(X)|{v for vs in V for v in vs}|{z};R=set(Y)|{u for us in U for u in us}
    assert L|R==set(range(n)) and not L&R
    assert all((u in L)!=(v in L) for u,v in G) and all(A)
    seen={0};todo=[0]
    while todo:
        for w in A[todo.pop()]-seen:seen.add(w);todo.append(w)
    assert len(seen)==n
    D=set(X+Y);assert all(v in D or A[v]&D for v in range(n))
    forced=[]
    for i in range(k):
        forced.append({X[i],U[i][0]} if i<s else {X[i],*U[i]})
        owner=U[i][0] if i<s else X[i]
        assert forced[-1]==A[owner]|{owner}
    for j in range(k):forced.append({Y[j],V[j][1]});assert forced[-1]==A[V[j][1]]|{V[j][1]}
    assert sum(map(len,forced))==len(set().union(*forced))
    union=set().union(*forced)
    assert z not in union and all(vs[0] not in union for vs in V)
    for i,us in enumerate(U):
        for choice in forced[i]-{X[i]}:
            mate=us[1] if choice==us[0] else us[0]
            assert A[mate]&union=={X[i]}
    for j,vs in enumerate(V):assert A[vs[0]]<=({Y[j]}|set().union(*(set(us) for us in U)))
    hdeg=sorted(map(len,AH));gdeg=sorted(map(len,A))
    expected_h=sorted([1]*k+[2]*k+[3]*k+[k+2]*(2*k)+[2*k+1]*k+[3*k])
    expected_g=sorted([1]*(k+s)+[2]*(k-s)+[s+3]*k+[k+2]*(2*k)+[2*k-s+1]*k+[3*k-s])
    assert hdeg==expected_h and gdeg==expected_g
    l1=sum(abs(a-b) for a,b in zip(hdeg,gdeg))
    assert l1==2*s*(k+1)
    assert len(H)==2*k*k+7*k and len(H)-len(G)==s
    assert len(H^G)==s*(2*k+1)
    return {'k':k,'s':s,'n':n,'gamma':2*k,'edge_deficit':s,'extremal_edges':len(H),'modified_edges':len(G),'degree_l1':l1,'all_relabelings_edit_lower':l1//2,'identity_edit_upper':len(H^G),'connected':True,'forced_neighborhood_checks':True,'degree_hist_H':dict(sorted(Counter(hdeg).items())),'degree_hist_G':dict(sorted(Counter(gdeg).items()))},hdeg,gdeg

def minimum_assignment(a,b):
    n=len(a);dp=[10**9]*(1<<n);dp[0]=0
    for S in range(1<<n):
        i=S.bit_count()
        if i==n:continue
        for j in range(n):
            if not(S>>j&1):dp[S|1<<j]=min(dp[S|1<<j],dp[S]+abs(a[i]-b[j]))
    return dp[-1]

def run():
    start=time.time();pairs={(k,s) for k in range(2,41) for s in range(1,k)}|{(s*s,s) for s in range(2,13)}
    records=[]
    for k,s in sorted(pairs):r,a,b=construct(k,s);records.append(r)
    r,a,b=construct(2,1);assignment=minimum_assignment(a,b);assert assignment==r['degree_l1']==6
    out={'status':'PASS','cases':len(records),'records':records,'small_unrestricted_degree_assignment_minimum':assignment,'scope':'Checks actual degrees and structural uniqueness premises; general all-relabeling lower bound uses the sorted matching inequality. No universal upper stability bound is claimed.','seconds':time.time()-start}
    (HERE/'independent_degree_results.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'status':'PASS','parameter_pairs':len(records),'degree_assignment_n13':assignment,'seconds':out['seconds']},indent=2))
if __name__=='__main__':run()
