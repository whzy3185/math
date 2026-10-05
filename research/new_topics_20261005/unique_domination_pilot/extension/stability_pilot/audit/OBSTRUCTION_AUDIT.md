# Independent audit of the edge-edit stability obstruction

Date: 2026-10-05. Construction, domination proof and relabelling-invariant lower bound: **PASS**.

## Audited conclusion and metric

For k>=2 and 1<=s<=k-1, the graph G(k,s) in EDIT_STABILITY_OBSTRUCTION.md is connected, bipartite, has no isolated vertices, has n=6k+1 and a unique minimum-cardinality dominating set of size gamma=2k. Its edge deficit from the sharp n=3 gamma+1 maximum is exactly t=s.

For edge-edit distance defined as the minimum edge symmetric-difference size over every vertex bijection,

    s(k+1) <= dist(G(k,s),H(k,k)) <= s(2k+1).

The lower bound allows completely arbitrary relabelling, with no preservation of named centers, bipartition sides or private pairs. The upper bound here concerns this construction only. This audit does not establish or endorse the separate proposed universal upper bound.

The examples disprove a universal bound C(gamma sqrt(t)+t). They also have asymptotically optimal edge density while remaining a positive normalized edit distance from the extremal graph. These are mathematical obstruction statements, not publication-novelty claims.

## Construction and edge accounting

For each of s selected rows, the graph deletes all k edges from u_i^0 to the active private columns v_j^0, adds all k edges x_i y_j, and deletes z u_i^0. The final deletion is at the same private vertex as the removed column incidences, making u_i^0 a leaf at x_i.

The k deletions and k additions cancel in edge count. The one remaining deletion per row gives

    e(G)=2k^2+7k-s=M_1(2k)-s.

All altered edges respect the original bipartition. Connectivity is explicit: z retains all Y-neighbors and every u_i^1, each x_i meets u_i^1, each V vertex meets its Y-center, and every modified leaf meets its X-center. No isolated vertex is introduced.

The natural labelling uses s(k+1) deletions and sk additions, all on distinct edges, giving symmetric-difference size s(2k+1).

## Unique minimum domination despite center-center edges

The new center-center edges invalidate the old use of N[x_i] on modified rows. The proposed proof correctly replaces it there by the newly created leaf neighborhood.

Every dominating set must meet these mutually disjoint closed neighborhoods:

- {x_i,u_i^0} on a modified row
- {x_i,u_i^0,u_i^1} on an unmodified row
- {y_j,v_j^1} for every column

There are 2k such sets, so every dominating set has cardinality at least 2k. The center set D=X union Y dominates and has that cardinality.

Any set of size 2k must choose exactly one vertex from each forced set and nothing else. Thus z, every active column vertex v_j^0, and every modified-row mate u_i^1 are absent. If a private vertex is chosen instead of x_i, its mate is undominated: the mate's possible neighbors are x_i, z and the active columns, none selected. This applies to both modified and unmodified rows. Every x_i is consequently forced. With all U vertices now excluded, choosing v_j^1 instead of y_j leaves v_j^0 undominated. Hence every y_j is forced as well, and D is uniquely minimum.

This is a minimum-cardinality and uniqueness proof, not a test of inclusion-minimality. It handles the changed edges inside D directly rather than assuming that D stays independent.

## The optimal degree matching and edit lower bound

For every fixed vertex bijection phi,

    sum_v |deg_G(v)-deg_H(phi^-1(v))|
        <= 2 |E(G) symmetric_difference phi(E(H))|.

Each discrepant edge contributes at most one to each endpoint's degree discrepancy, proving the inequality.

The minimum L1 matching cost between two real sequences is attained by matching sorted sequences. Indeed, when a<=b and c<=d,

    |a-c|+|b-d| <= |a-d|+|b-c|.

Repeatedly uncrossing inverted matches proves the claim without imposing any graph-labelling restriction. Therefore half the sorted degree L1 distance is a valid lower bound for every graph relabelling.

The degree lists in the source are correct. In H(k,k), the groups are

    (1,k), (2,k), (3,k), (k+2,2k), (2k+1,k), (3k,1).

In G(k,s), they are

    (1,k+s), (2,k-s), (3+s,k),
    (k+2,2k), (2k+1-s,k), (3k-s,1).

For 1<=s<=k-1 these are nondecreasing, including the endpoint ties. In particular, the modified X-centers enter the degree-(k+2) group exactly as the modified private vertices leave it. Matching positions gives

    s+ks+ks+s=2s(k+1).

This proves the claimed lower bound s(k+1). The calculation is not a comparison under only the original vertex names or the original bipartition.

## Consequences

### Failure of a square-root-deficit estimate

Set k=s^2, s>=2. The legal parameter conditions hold, gamma=2s^2, t=s, and

    dist >= s(s^2+1),
    gamma sqrt(t)+t=2s^(5/2)+s.

Their ratio tends to infinity. More explicitly it is at least sqrt(s)/3 for s>=2, so no absolute constant C can make the proposed estimate true for every graph in this class.

The unique extremal isomorphism class at these n=3 gamma+1 parameters is H(k,k), by the previously audited equality theorem. Thus the obstruction applies to distance from the entire extremal class, not just from an arbitrarily chosen representative.

### Failure of dense normalized edit stability

Set s=floor(k/2). Then t=O(k)=o(k^2) and e(G)/M_1(2k) tends to one. Nevertheless the lower bound gives

    liminf dist(G,H(k,k))/(6k+1)^2 >= 1/72.

The limit constant is correct: s(k+1) is asymptotic to k^2/2 and (6k+1)^2 to 36k^2.

The conditional observation about an O(gamma t) universal upper estimate is logically correct, but that upper estimate is outside this obstruction audit. The examples do not exclude vertex-deletion stability or stability under additional hypotheses.

## Independent computations

Two separately written implementations import no primary code.

1. check_small_domination.cpp reconstructs the modified graph by direct edge rules and tests every vertex subset of size at most 2k for all 1<=s<k with k=2,3,4. Across the six graphs it checks 5,512,028 candidate subsets. Exactly the specified center set dominates at size at most 2k in every case.
2. check_degree_obstruction.py constructs H first and applies the specified edge modifications. It independently checks connectivity, bipartiteness, exact edge deficit, the forced-neighborhood structural identities, both degree multisets, the sorted L1 formula and the natural edit count for 786 parameter pairs. These include all 2<=k<=40, 1<=s<k, the tied-degree endpoints, and further k=s^2 examples through s=12.

At n=13 an unrestricted minimum-cost degree assignment is also solved by exact subset dynamic programming over all assignments. Its value is six, equal to the sorted L1 calculation, and therefore gives the three-edge lower bound in that smallest example.

The finite tests corroborate the general proof. The unbounded obstruction follows from the exact construction, forced-neighborhood argument and matching inequality, not from numerical extrapolation.

## Reproduction and status separation

Run in this audit directory:

    g++ -O3 -std=c++17 -Wall -Wextra check_small_domination.cpp -o check_small_domination
    ./check_small_domination
    python check_degree_obstruction.py

Outputs are small_domination_stdout.txt, independent_degree_results.json and degree_stdout.json. Source hashes and artifact checksums are recorded separately.

No blocking mathematical discrepancy was found in the obstruction note. The separate universal linear-deficit proposal has not been used as a premise and is not certified by this report.
