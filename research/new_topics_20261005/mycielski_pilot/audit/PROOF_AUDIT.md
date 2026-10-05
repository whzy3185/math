# Independent audit: Hall ratio of the 47-vertex Mycielski graph

Date: 2026-10-05. Status: **PASS, exact finite result**. Literature novelty is not assessed here.

Let M_2=K_2 and obtain each next graph by retaining the original vertices, adding one clone per original vertex adjacent to its original neighbors, and adding an apex adjacent to all clones. Thus M_6 has 47 vertices and 236 edges. For a graph G define its Hall ratio as the maximum of |S|/alpha(G[S]) over nonempty vertex sets S.

The independently verified conclusion is

    Hall ratio(M_6)=10/3.

## Graph and complete independent-set data

The checker reconstructs all four Mycielski steps using ordinary edge sets, independently of the supplied adjacency-bitmask generator. The reconstructed adjacency exactly equals the supplied data. The graph is triangle-free.

An include/exclude enumeration independently counts 7407 independent sets in M_5. A separate set-based Bron-Kerbosch enumeration on the complement of M_6 returns exactly the supplied 857 maximal independent sets, with no duplicates. Every returned set is explicitly checked for independence and maximality. Its maximum size is 23.

Bron-Kerbosch is exhaustive because at each state the available vertices are precisely the permitted extensions of the current clique, and excluded vertices record extensions already visited. Pivot branching covers every maximal extension, while the terminal condition that both available and excluded sets are empty is exactly maximality. Applying this to the complement enumerates every maximal independent set of the original graph.

For any S, one has

    alpha(G[S]) = max_I |I intersect S|,

where I ranges over all maximal independent sets of G. One direction follows because each intersection is independent; the other follows by extending an independent set of G[S] to a maximal independent set of G. Thus these 857 rows are a complete constraint system, not a sampled relaxation.

## Lower witness

In the recursive original/clone/apex labeling, the witness is

    {0,1,2,3,4,5,6,7,11,12,15,19,21,22,26,32,33,41,45,46}.

It has 20 vertices. Its maximum intersection with the complete maximal-independent-set list is six. An independent include/exclude recursion on the induced 20-vertex graph also computes independence number six. For example, {0,2,5,7,11,41} is an independent six-set. Hence the Hall ratio is at least 20/6=10/3.

## Exact upper certificate

For an integer k, impose sum_{v in I} x_v <= k for every maximal independent set I, with binary variables x_v indicating membership in S. This is exactly the condition alpha(G[S])<=k.

At a certificate node, let O be the vertices fixed to one and Z those fixed to zero. Every remaining variable is free. A dual leaf supplies nonnegative rational multipliers y_I for the independent-set inequalities and nonnegative rational multipliers z_v for the upper bounds x_v<=1. For every free vertex it verifies

    sum_{I containing v} y_I + z_v >= 1.

Since all free variables are nonnegative, the resulting rigorous upper bound is

    |S| <= |O| + sum_I y_I (k-|I intersect O|) + sum_v z_v.

The checker reconstructs this rational expression exactly, compares it with the encoded bound, and verifies that it is strictly below floor(10k/3)+1. This proves |S|<=floor(10k/3). No rounded numerical objective or optimization status enters the argument.

Each internal node fixes a previously free variable to zero in one child and one in the other. The checker verifies both children. These alternatives are exhaustive and disjoint for every binary assignment, so accepted leaves certify the root problem.

All 273 nodes pass: 130 binary splits and 143 rational dual leaves. The certificates cover k=1 and k=3,4,...,14. All branching occurs at k=5: its tree contains 261 nodes and 131 dual leaves, has depth 15, and every leaf has strict slack at least 1/213 below the forbidden size 17. Thus no 17-vertex induced subgraph has independence number at most five.

The remaining cases are rigorous elementary bounds:

- k=2: Every six-vertex triangle-free graph has an independent triple. If a vertex has three neighbors, those neighbors are independent. Otherwise it has at least three nonneighbors; they cannot form a triangle, so a nonadjacent pair among them together with the vertex is independent. Consequently alpha<=2 implies |S|<=5
- k>=15: |S|/k<=47/15<10/3

These cover every possible independence number 1 through 23. Combined with the lower witness, the Hall ratio is exactly 10/3.

## Additional simplification

The k=6 root certificate actually has sum y_I=29/10 and sum z_v=3. Its same coefficients prove |S|<=29k/10+3 for every k. At k=6 integrality gives |S|<=20; at every k>=7 this expression is at most 10k/3. Thus the larger-k certificates are redundant for the stated Hall-ratio theorem. They were nevertheless all checked independently as supplied.

## Reproduction and scope

Run `python independent_check.py` with Python 3. Only the standard library is used. The inputs are the sibling `m6_candidates.json` and `upper_certificates.json`; their SHA-256 hashes are recorded in `independent_check_result.json`. The checker imports no discovery or primary-checker code and no numerical optimization library. Fresh stdout is recorded separately.

This certifies the finite numerical invariant and the stated witness. It does not classify all equality witnesses, establish a complete induced-independence profile, prove an asymptotic result for all Mycielski graphs, or establish that the result is new to the literature.
