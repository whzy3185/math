"""Independent complete skeleton audit using all-subset domination DP.
No imports from primary code. Every graph pattern and every vertex subset
is tested, including patterns below the extremal edge threshold.
"""
from pathlib import Path
from collections import Counter
import json,hashlib,time
HERE=Path(__file__).resolve().parent

def skeleton(p):
    # Symbolic labels keep construction independent of the stored bit order.
    X=[f'x{i}' for i in range(p)];Y=['y'];U=[[f'u{i}_{j}' for j in range(2)] for i in range(p)];W=[f'w{j}' for j in range(3)]
    labels=X+Y+sum(U,[])+W;idx={v:i for i,v in enumerate(labels)}
    fixed={(x,u) for x,us in zip(X,U) for u in us}|{('y',w) for w in W}
    optional=[(x,'y') for x in X]+[(u,w) for us in U for u in us for w in W]
    conv=lambda edges:sorted(tuple(sorted((idx[u],idx[v]))) for u,v in edges)
    return labels,conv(fixed),[tuple(sorted((idx[u],idx[v]))) for u,v in optional]

def full_domination(n,edges):
    closed=[1<<v for v in range(n)]
    for u,v in edges:closed[u]|=1<<v;closed[v]|=1<<u
    full=(1<<n)-1;covered=[0]*(1<<n);best=n+1;winners=[]
    for S in range(1,1<<n):
        bit=S&-S;covered[S]=covered[S^bit]|closed[bit.bit_length()-1]
        if covered[S]==full:
            size=S.bit_count()
            if size<best:best=size;winners=[S]
            elif size==best:winners.append(S)
    return best,winners

def run():
    start=time.time();source=json.loads((HERE.parent/'low_gamma_certificate.json').read_text());reports=[]
    for p in [1,2]:
        labels,fixed,optional=skeleton(p);n=len(labels);gamma=p+1;D=(1<<gamma)-1;target=gamma*(gamma+7)//2
        hist=Counter();unique_edges=Counter();accepted=[];high=0;winner_list=[]
        for code in range(1<<len(optional)):
            edges=fixed+[e for i,e in enumerate(optional) if code>>i&1]
            g,sets=full_domination(n,edges);assert g<=gamma
            hist[(g,len(sets))]+=1
            if len(edges)>=target:high+=1
            if g==gamma and sets==[D]:
                unique_edges[len(edges)]+=1
                if len(edges)>=target:
                    assert len(edges)==target
                    omissions=[]
                    for i in range(p):
                        rows=[p+1+2*i,p+2+2*i];W=list(range(3*p+1,3*p+4))
                        missing=[w for w in W if all(tuple(sorted((u,w))) not in edges for u in rows)]
                        assert len(missing)==1
                        assert all(tuple(sorted((u,w))) in edges for u in rows for w in W if w!=missing[0])
                        omissions.extend(missing)
                    assert len(set(omissions))==1
                    accepted.append({'mask':code,'edge_count':len(edges),'edges':sorted(edges),'omitted_column':omissions[0],'minimum_domination':g,'unique_minimum_set':[v for v in range(n) if D>>v&1]})
            if len(edges)==target:winner_list.append((code,g,sets))
        stored=next(z for z in source['cases'] if z['gamma']==gamma)
        assert sorted(map(tuple,stored['fixed_edges']))==fixed
        assert list(map(tuple,stored['free_edges_in_bit_order']))==optional
        assert [z['mask'] for z in accepted]==[z['mask'] for z in stored['accepted_patterns']]
        for row,old in zip(accepted,stored['accepted_patterns']):
            assert row['edges']==sorted(map(tuple,old['edges'])) and row['omitted_column']==old['omitted_private_column']
        assert len(accepted)==3 and max(unique_edges)==target
        assert high==stored['patterns_at_or_above_target_exhaustively_checked']
        reports.append({'gamma':gamma,'vertices':n,'patterns':1<<len(optional),'vertex_subsets_per_pattern':1<<n,'total_vertex_subsets_checked':(1<<len(optional))*(1<<n),'high_edge_patterns':high,'unique_D_pattern_count':sum(unique_edges.values()),'unique_D_counts_by_edges':dict(sorted(unique_edges.items())),'maximum_edges':target,'equality_patterns':accepted,'minimum_domination_histogram':{str(k):v for k,v in sorted(hist.items())}})
    result={'status':'PASS','cases':reports,'seconds':time.time()-start,'method':'Fresh symbolic skeleton construction and exact closed-neighborhood subset-union dynamic programming over every vertex subset of every graph pattern. No primary imports; minimum cardinality and uniqueness tested separately.'}
    (HERE/'independent_result.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':result['status'],'seconds':result['seconds'],'cases':[{k:z[k] for k in ['gamma','patterns','total_vertex_subsets_checked','high_edge_patterns','unique_D_pattern_count','maximum_edges']} for z in reports]},indent=2))
if __name__=='__main__':run()
