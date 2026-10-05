"""Exact small-graph verification of the standalone structural module."""
from pathlib import Path
from functools import lru_cache
from collections import Counter
import json
from mycielski_structure import (mycielski, independent_sets_with_neighborhood,
    maximal_independent_sets_mycielski, induced_independence,
    independence_polynomial_mycielski)
P=Path(__file__).resolve().parent
cases=graphs=0
for n in range(1,5):
    edges=[(i,j) for i in range(n) for j in range(i)]
    for mask in range(1<<len(edges)):
        graphs+=1
        adjacency=[0]*n
        for e,(i,j) in enumerate(edges):
            if mask>>e&1:adjacency[i]|=1<<j;adjacency[j]|=1<<i
        new=mycielski(adjacency);full=(1<<n)-1
        @lru_cache(None)
        def alpha(S):
            if not S:return 0
            bit=S&-S;v=bit.bit_length()-1;T=S^bit
            return max(alpha(T),1+alpha(T&~new[v]))
        maximal=[];counts=Counter()
        for S in range(1<<len(new)):
            A=S&full;B=(S>>n)&full;apex=bool(S>>(2*n)&1)
            assert induced_independence(adjacency,A,B,apex)==alpha(S)
            cases+=1
            if all(not(new[v]&S) for v in range(len(new)) if S>>v&1):
                counts[S.bit_count()]+=1
                if all(new[v]&S for v in range(len(new)) if not(S>>v&1)):
                    maximal.append(S)
        assert tuple(maximal)==maximal_independent_sets_mycielski(adjacency)
        assert tuple(counts[j] for j in range(len(new)+1))==independence_polynomial_mycielski(adjacency)
adjacency=(2,1)
for _ in range(3):adjacency=mycielski(adjacency)
base=list(independent_sets_with_neighborhood(adjacency))
mis=maximal_independent_sets_mycielski(adjacency)
stored=json.loads((P.parent/'mycielski_pilot/m6_candidates.json').read_text())
assert list(mis)==stored['candidate_masks']
result={'status':'PASS','base_graphs_checked':graphs,'induced_subsets_checked':cases,'m5_independent_sets':len(base),'m5_distinct_independent_neighborhoods':len({N for I,N in base}),'m6_maximal_independent_sets':len(mis),'m6_independent_sets_from_polynomial':sum(independence_polynomial_mycielski(adjacency))}
(P/'general_module_checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
