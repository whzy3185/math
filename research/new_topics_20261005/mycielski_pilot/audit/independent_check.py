"""Independent exact checker for the claimed Hall ratio of the 47-vertex M6.

This checker imports no discovery or primary-checker code and no numerical
optimization library. It reconstructs the graph using edge sets, enumerates
maximal independent sets by set-based Bron-Kerbosch, and checks each branch
certificate using fractions.Fraction. Floating point and solver status play
no role in acceptance.
"""
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from hashlib import sha256
from pathlib import Path
import json

HERE=Path(__file__).resolve().parent
SOURCE=HERE.parent
WITNESS=107765098387711


def integer(x):
    assert type(x) is int,x
    return x


def rational(pair):
    assert len(pair)==2
    a,b=map(integer,pair)
    assert b>0
    return Fraction(a,b)


def next_graph(n,edges):
    out=set(edges)
    for u,v in edges:
        out.add(tuple(sorted((u,n+v))))
        out.add(tuple(sorted((v,n+u))))
    for v in range(n):
        out.add((n+v,2*n))
    return 2*n+1,out


def adjacency(n,edges):
    out=[set() for _ in range(n)]
    for u,v in edges:
        assert 0<=u<v<n
        out[u].add(v);out[v].add(u)
    return out


def mask(vertices):
    return sum(1<<v for v in vertices)


def all_independent_sets(adj):
    def visit(remaining,chosen):
        if not remaining:
            yield frozenset(chosen)
            return
        v=min(remaining)
        rest=remaining-{v}
        yield from visit(rest,chosen)
        yield from visit(rest-adj[v],chosen|{v})
    yield from visit(set(range(len(adj))),set())


def maximal_independent_sets(adj):
    vertices=set(range(len(adj)))
    complement=[vertices-{v}-adj[v] for v in range(len(adj))]
    out=[]
    def visit(chosen,available,excluded):
        if not available and not excluded:
            out.append(mask(chosen))
            return
        candidates=available|excluded
        pivot=max(candidates,key=lambda v:(len(available&complement[v]),-v))
        for v in sorted(available-complement[pivot]):
            visit(chosen|{v},available&complement[v],excluded&complement[v])
            available.remove(v)
            excluded.add(v)
    visit(set(),vertices,set())
    assert len(out)==len(set(out))
    return sorted(out)


def run():
    n=2;edges={(0,1)};sizes=[n]
    base_count=None
    for _ in range(4):
        if n==23:
            base_sets=list(all_independent_sets(adjacency(n,edges)))
            assert len(base_sets)==len(set(base_sets))
            base_count=len(base_sets)
        n,edges=next_graph(n,edges)
        sizes.append(n)
    assert sizes==[2,5,11,23,47]
    adj=adjacency(n,edges)
    graph_masks=[mask(row) for row in adj]
    full=(1<<n)-1
    supplied=json.loads((SOURCE/'m6_candidates.json').read_text())
    assert supplied['adj']==graph_masks
    assert base_count==7407==supplied['base_independent_sets']
    assert all(not(adj[u]&adj[v]) for u,v in edges)
    mis=maximal_independent_sets(adj)
    assert len(mis)==857
    assert mis==supplied['candidate_masks']
    for I in mis:
        assert I and I&~full==0
        assert all(not(graph_masks[v]&I) for v in range(n) if I>>v&1)
        assert all(graph_masks[v]&I for v in range(n) if not(I>>v&1))
    alpha=max(I.bit_count() for I in mis)
    assert alpha==23

    @lru_cache(None)
    def direct_alpha(S):
        if not S:
            return 0
        v=(S&-S).bit_length()-1
        rest=S&~(1<<v)
        return max(direct_alpha(rest),1+direct_alpha(rest&~graph_masks[v]))
    witness_size=WITNESS.bit_count()
    witness_alpha=max((WITNESS&I).bit_count() for I in mis)
    assert witness_size==20 and witness_alpha==6
    assert direct_alpha(WITNESS)==6
    ratio=Fraction(witness_size,witness_alpha)
    assert ratio==Fraction(10,3)
    witness_independent=next(WITNESS&I for I in mis if (WITNESS&I).bit_count()==6)

    data=json.loads((SOURCE/'upper_certificates.json').read_text())
    assert rational(data['target_hall_ratio'])==ratio
    expected={1,3,4,5,6,7,8,9,10,11,12,13,14}
    assert set(map(int,data['certificates']))==expected
    report={}
    for k in sorted(expected):
        cert=data['certificates'][str(k)]
        target=integer(cert['forbidden_size'])
        assert target==(10*k)//3+1
        stats=Counter()
        leaf_bounds=[]
        max_depth=0
        def check(node,ones,zeros,depth):
            nonlocal max_depth
            assert not(ones&zeros)
            assert (ones|zeros)&~full==0
            free=[v for v in range(n) if not((ones|zeros)>>v&1)]
            stats['nodes']+=1
            max_depth=max(max_depth,depth)
            tag=node['type']
            if tag=='split':
                stats['split']+=1
                v=integer(node['vertex'])
                assert v in free
                assert 'zero' in node and 'one' in node
                check(node['zero'],ones,zeros|(1<<v),depth+1)
                check(node['one'],ones|(1<<v),zeros,depth+1)
                return
            stats[tag]+=1
            if tag=='conflict':
                row=integer(node['row'])
                assert 0<=row<len(mis)
                assert (mis[row]&ones).bit_count()>k
                return
            if tag=='trivial':
                assert not free
                assert integer(node['bound'])==ones.bit_count()<target
                leaf_bounds.append(Fraction(ones.bit_count()))
                return
            assert tag=='dual',tag
            y={};z={}
            for row,num,den in node['y']:
                row=integer(row)
                assert 0<=row<len(mis)
                assert row not in y
                weight=rational([num,den])
                assert weight>=0
                y[row]=weight
            for v,num,den in node['z']:
                v=integer(v)
                assert v in free and v not in z
                weight=rational([num,den])
                assert weight>=0
                z[v]=weight
            for v in free:
                covered=z.get(v,Fraction(0))+sum((weight for row,weight in y.items() if mis[row]>>v&1),Fraction(0))
                assert covered>=1,(k,depth,v,covered)
            bound=Fraction(ones.bit_count())
            for row,weight in y.items():
                rhs=k-(mis[row]&ones).bit_count()
                bound+=weight*rhs
            bound+=sum(z.values(),Fraction(0))
            assert bound==rational(node['bound'])
            assert bound<target,(k,depth,bound,target)
            leaf_bounds.append(bound)
        check(cert['tree'],0,0,0)
        assert stats['nodes']==2*stats['split']+1
        report[str(k)]={'forbidden_size':target,'node_counts':dict(stats),'max_depth':max_depth,
                        'largest_leaf_upper_bound':str(max(leaf_bounds)),
                        'minimum_strict_leaf_slack':str(min(Fraction(target)-b for b in leaf_bounds))}
    total=Counter()
    for row in report.values():
        total.update(row['node_counts'])
    assert total['nodes']==273 and total['split']==130 and total['dual']==143
    assert report['5']['node_counts']['nodes']==261

    # The one omitted small parameter is handled by R(3,3)<=6.
    # In a triangle-free six-vertex graph: if a vertex has >=3 neighbors,
    # three such neighbors are independent. Otherwise it has >=3 nonneighbors;
    # those cannot form a triangle, so a nonadjacent pair plus the vertex is
    # independent. Thus alpha<=2 forces at most five vertices.
    assert Fraction(5,2)<ratio
    # Every possible alpha>=15 has a trivial 47/alpha upper bound.
    assert Fraction(47,15)<ratio
    coverage={str(k):('exact rational binary-tree certificate' if k in expected else
                      'triangle-free six-vertex argument' if k==2 else
                      '47/k <= 47/15 < 10/3') for k in range(1,alpha+1)}
    result={
        'status':'PASS','graph':'M6, M2=K2, original/clone/apex recursive labeling',
        'vertex_count':n,'edge_count':len(edges),'triangle_free':True,
        'M5_independent_set_count':base_count,'maximal_independent_set_count':len(mis),
        'MIS_size_distribution':dict(sorted(Counter(I.bit_count() for I in mis).items())),
        'alpha_M6':alpha,'witness_mask':WITNESS,'witness_vertices':[v for v in range(n) if WITNESS>>v&1],
        'witness_order':witness_size,'witness_alpha':witness_alpha,'witness_direct_alpha_replay':True,
        'witness_independent_six':[v for v in range(n) if witness_independent>>v&1],
        'Hall_ratio':str(ratio),'branch_tree_totals':dict(total),'per_k_certificates':report,
        'coverage_all_alpha_1_through_23':coverage,
        'input_sha256':{name:sha256((SOURCE/name).read_bytes()).hexdigest() for name in ['m6_candidates.json','upper_certificates.json']},
        'evidence_scope':'Exact finite computation and rational certificate; no literature novelty assertion and no numerical solver premise',
    }
    (HERE/'independent_check_result.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ['per_k_certificates','coverage_all_alpha_1_through_23']},indent=2))


if __name__=='__main__':
    run()
