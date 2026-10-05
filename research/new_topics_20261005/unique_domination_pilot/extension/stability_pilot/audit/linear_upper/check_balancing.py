"""Independent explicit template bijections for the upper stability proof."""
from pathlib import Path
import json
HERE=Path(__file__).resolve().parent

def template(g,p,selected):
    q=g-p;z=3*g;E=set()
    def put(u,v):E.add(tuple(sorted((u,v))))
    for d in range(g):put(d,g+2*d);put(d,g+2*d+1)
    for i in range(p):
        put(z,g+2*i);put(z,g+2*i+1)
        for j in range(q):
            for b in range(2):put(g+2*i+b,g+2*(p+j)+selected[j])
    for j in range(q):put(z,p+j)
    return E

def check(g,p):
    a=(g+1)//2;b=g//2;q=g-p;h=abs(p-a);selected=[j%2 for j in range(q)]
    E=template(g,p,selected);F=template(g,a,[0]*b);center={};moved=set()
    if p>=a:
        for i in range(a):center[i]=i
        for j in range(q):center[p+j]=a+j
        for i in range(a,p):center[i]=a+q+i-a;moved.add(i)
    else:
        for i in range(p):center[i]=i
        for j in range(b):center[p+j]=a+j
        for j in range(h):center[p+b+j]=p+j;moved.add(p+b+j)
    f={3*g:3*g}
    for d,dest in center.items():
        f[d]=dest
        swap=selected[d-p] if d>=p and d not in moved else 0
        for bit in range(2):f[g+2*d+bit]=g+2*dest+(bit^swap)
    assert sorted(f)==list(range(3*g+1)) and sorted(f.values())==list(range(3*g+1))
    image={tuple(sorted((f[u],f[v]))) for u,v in E};difference=image^F
    moved_vertices={f[v] for d in moved for v in [d,g+2*d,g+2*d+1]}
    assert all(u in moved_vertices or v in moved_vertices for u,v in difference)
    degE=[0]*(3*g+1);degF=[0]*(3*g+1)
    for u,v in E:degE[u]+=1;degE[v]+=1
    for u,v in F:degF[u]+=1;degF[v]+=1
    degree_bound=sum(degE[v]+degF[f[v]] for d in moved for v in [d,g+2*d,g+2*d+1])
    assert degree_bound==h*(2*g-2*h+11)
    assert len(difference)<=degree_bound
    exact=h*(2*g-2*h+3);assert len(difference)==exact
    imbalance=(2*p-g)*(2*p-g-1)//2
    assert h*h<=imbalance
    assert 6*g+12<=12*g
    if g>=4:assert g+7<=12*((g-2)//2)
    return {'gamma':g,'p':p,'q':q,'moved_triples':h,'imbalance':imbalance,'actual_edit_count':len(difference),'degree_upper':degree_bound}

rows=[check(g,p) for g in range(2,41) for p in range(g)]
assert len(rows)==819
out={'status':'PASS','splits':len(rows),'rows':rows,'scope':'Explicit free-vertex relabelling; residual and all unchanged triples retain roles; no primary imports.'}
(HERE/'balancing_result.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':'PASS','splits':len(rows),'all_degree_bounds_and_imbalance_inequalities':True},indent=2))
