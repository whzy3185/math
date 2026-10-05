# Independent audit of the two-residual unique-domination theorem

Date: 2026-10-05. General proof audit and independently coded exact checks: **PASS**.

## Audited theorem and boundaries

For every integer gamma>=2, among finite simple bipartite graphs without isolated vertices, of order n=3 gamma+2 and with a unique minimum-cardinality dominating set of size gamma, the maximum number of edges is

    ceil(gamma^2/2)+5 gamma.

Connected graphs attain this value. For every even gamma>=4, the displayed constructions give at least two nonisomorphic connected extremal graphs. No complete equality classification is established or claimed.

The reviewed source is ../CANDIDATE_BOUNDARY_THEOREM.md. Its upper bound is an elementary argument, not an inference from the bounded computations. The local-cell and construction checks are independent corroboration. No Lean formalization or publication-novelty claim is endorsed. The source's attribution of known low-order values and the prior q=1 construction remains essential.

## Private-neighbor reduction and the use of uniqueness

The reduction to gamma centers, two selected exterior private neighbors per center, and two residual vertices is legitimate. If a center has no exterior private neighbor, deletion or replacement gives a smaller or different dominating set. If it has exactly one, replacement by that neighbor preserves domination and cardinality. The no-isolate hypothesis supplies a replacement neighbor when needed. Thus each center has at least two such neighbors, and the selected pairs are disjoint.

The local-cell argument requires more than ordinary domination number: a different dominating set of size at most two in a cell, combined with retained outside centers, would yield either a smaller global dominating set or another one of cardinality gamma. Both are forbidden by the stated hypothesis. Every application in the reviewed proof explicitly preserves domination of both residual vertices. No residual obligation is silently discarded.

## The four local bounds

The optional edge bounds are correct:

    L(2,2)=2, L(2,3)=4, L(2,4)=6, L(3,3)=6.

For (2,2), two disjoint private-private edges give an alternative pair. With the center edge present, a two-edge star also gives an alternative pair. This proves the bound two.

For (2,s), s=3,4, at least 2s-1 private-private edges without the center edge force one full row and a nonempty second row. The full-row vertex and a neighbor of the other row dominate both centers and both private sets. With the center edge, a full column would give a different pair, so there is at most one edge per column and at most s+1 optional edges. The inequality s+1<=2s-2 is valid for both specified values.

For (3,3), seven optional edges without the center edge leave at most two missing entries, ensuring a full row and full column. Their vertices dominate the cell. With the center edge, at least six private-private edges either give a full row or column, or force every row and column degree to be two. In the latter case the missing entries form a perfect matching; the endpoints of a missing edge form a different dominating pair. Every claimed alternative covers both centers as well as all six private vertices.

The stated attaining local configurations do have the center pair as their unique minimum dominating pair. In particular, the (3,3) example consists of K_(2,3) and an unused third row, in addition to the fixed center edges. Its unused-row leaf forces a choice from its own closed neighborhood; a single additional private vertex cannot dominate the remaining same-side private vertices. Direct exact enumeration confirms the assertion, including all other attaining patterns.

## Same-side residual vertices

Orient both residuals into the side with p centers, leaving q>=1 opposite centers. Let S count singleton-dominated residuals and r_j count those owned by the j-th opposite center.

The cell for center pair (i,j) includes exactly the singleton residuals whose owner j is removed. Every other singleton keeps its owner. A residual with at least two center-neighbors keeps one because only one center on its side of adjacency is removed. Thus the (2,2+r_j) cells are all legitimate.

The optional cell-edge sets are disjoint. Fixed selected-private incidences contribute 2 gamma; singleton owner edges contribute S; the cells contribute at most 2pq+2pS; each of the other 2-S residuals contributes at most 2p+q edges. There is no residual-residual edge in this placement. Therefore

    e <= 2 gamma+2pq+4p+2q-S(q-1)
      <= 2pq+6p+4q.

The argument also covers p=0: the cell sum is empty, and the direct residual degree accounting remains valid.

With d=p-q, the last expression is

    gamma^2/2+5 gamma+1/2-(d-1)^2/2.

Parity of d agrees with gamma. For even gamma, (d-1)^2>=1; for odd gamma it is nonnegative. This proves the desired ceiling bound, including gamma=2 and gamma=3.

## Opposite-side residual vertices

Let z have a nonempty center-neighborhood in Y and w one in X. Hence p,q>=1. Their possible mutual edge is retained explicitly in every relevant count.

### Both have at least two center-neighbors

Every ordinary (2,2) cell is valid: removing one center from each side leaves both residuals dominated. The resulting bound is

    e <= 2pq+5 gamma+1.

For odd gamma it is already at most the target. For even gamma, an excess above the target would force the sole possible value target+1, balanced p=q, and saturation of every degree and cell bound. In particular z meets all Y and selected U vertices, while w meets all X and selected V vertices. Replacing any selected center pair x_i,y_j in D by z,w dominates the whole graph and gives a different gamma-set. This contradiction excludes the one-edge excess.

This is a valid integrality-and-saturation argument, rather than an unsupported subtraction of one from the bound. The case requires p,q>=2, so there is no unhandled gamma=2 or gamma=3 exception.

### Exactly one is singleton-dominated

After interchanging sides, suppose z has sole owner y_j0 while w has at least two X-neighbors. The special cells include z precisely when y_j0 is removed. The other residual w always keeps an X-neighbor. Thus the mixed (2,2)/(2,3) cell count is valid.

The two separately counted terms are the edge z-y_j0 and the possible edge zw. The remaining incidences of w are at most 2q+p. This gives exactly

    e <= 2pq+5 gamma+2-q.

For q>=2, the target follows immediately. For q=1, the multi-neighbor condition gives p>=2 and gamma>=3. The difference from the target is

    ceil(gamma^2/2)-2 gamma+1,

which is zero at gamma=3 and strictly positive for gamma>=4. The invalid gamma=2 value is explicitly excluded by the hypothesis, not overlooked.

### Both are singleton-dominated

The four cell types (2,2), (3,2), (2,3), (3,3) include each residual exactly whenever its owner is removed. Every residual outside a cell keeps its owner; every outside selected private vertex keeps its center. The two owner edges are fixed incidences, and zw occurs only in the (3,3) optional block.

The resulting disjoint count is

    e <= 2pq+4 gamma+2
      <= floor(gamma^2/2)+4 gamma+2
      <= ceil(gamma^2/2)+5 gamma,

with the last inequality valid for every gamma>=2. This includes the tight gamma=2 boundary.

These three cases exhaust opposite-side residual placements. Together with the same-side case, they prove the general upper bound.

## Attainment and nonisomorphic extremals

The H2(p,q) edge list is bipartite and connected and has 3(p+q)+2 vertices and

    2pq+6p+4q

edges. Closed neighborhoods of each x_i and each designated private leaf v_j^1 form p+q pairwise disjoint forced sets. Hence every dominating set has size at least p+q, attained by the centers.

A set of that size has exactly one member of each forced set and no vertices elsewhere. Both residuals and all active v_j^0 are consequently absent. Choosing a private U vertex instead of x_i leaves its mate undominated. Choosing a private leaf instead of y_j then leaves the active V vertex undominated. Therefore the center set is uniquely minimum.

Taking p=ceil(gamma/2), q=floor(gamma/2) gives the target value for all gamma>=2. For even gamma=2k>=4, both (p,q)=(k,k) and (k+1,k-1) are valid and attain it. Their unordered connected bipartition sizes are {3k,3k+2} and {3k+1,3k+1}, so they cannot be isomorphic. The argument proves at least two examples, not a classification.

## Independent exact computations

The new independent_two_extra.py imports no primary code. It reconstructs all local cells and all ten H2(p,q) graphs with 2<=p+q<=5, and tests domination by requiring intersection with every closed neighborhood. This differs from the primary union-cover routine.

All 1,696 local patterns were checked. The respective admissible counts are 14, 58, 254 and 548, with maxima 2, 4, 6 and 6. Every local pattern's uniqueness flag, supplied alternative dominating set and extremal mask agrees with the primary file.

For all ten H2 graphs, every vertex subset was checked. The exact domination counts at every size, unique minimum set, edge set, connectivity and bipartition sizes agree. Balanced cases give edge values 12, 20, 28 and 38 at gamma=2,3,4,5. The supplied edge-level map from H2(3,1) to the quoted prior 14-vertex graph and its unique four-element dominating set also checks exactly. This verifies the mathematical identification against supplied edge data, not a new literature-priority search.

### Additional reduced-skeleton counterexample search

The independently written search_boundary_skeletons.cpp exhausts all valid private-pair skeletons for gamma=2 and gamma=3, with residuals on the same or opposite sides and every legal p,q split. It allows every bipartite edge except those forbidden by the selected exterior-private-neighbor labels. Each residual is required to have a center-neighbor, since D dominates it.

There are 1,197,626 valid reduced graph patterns. All 116,635 patterns whose edge count reaches or exceeds the proposed maximum are tested for a different dominating set of size at most gamma. A candidate is accepted only if no such set exists. No pattern exceeds the claimed bound while preserving unique minimum domination.

At gamma=2 the attained bound is 12; at gamma=3 it is 20. These exhaustive reduced searches stress the small boundary cases independently of the analytic partition argument. They are not counts of nonisomorphic global graphs, and repeated private-pair representations may describe isomorphic or identical graphs.

The run reports PASS COMPLETE and has no search time cutoff. The upper bound for arbitrary gamma remains the elementary proof audited above.

## Reproduction and artifacts

From this audit directory:

    python independent_two_extra.py
    g++ -O3 -std=c++17 -Wall -Wextra search_boundary_skeletons.cpp -o search_boundary_skeletons
    ./search_boundary_skeletons

Python uses only the standard library. The separate outputs are independent_results.json, independent_stdout.json and boundary_search_stdout.txt. Source hashes and artifact checksums accompany this report.

No blocking mathematical correction was required. All prior proof packages remain unchanged.
