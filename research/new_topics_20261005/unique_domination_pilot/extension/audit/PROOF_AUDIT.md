# Independent audit of the low-domination equality completion

Date: 2026-10-05. Elementary proof audit and independently coded exact verification: **PASS**.

## Scope and conclusion

Assume a finite simple bipartite graph has no isolated vertices, has n=3 gamma+1 vertices, and has exactly one minimum-cardinality dominating set D of size gamma. The already audited sharp-boundary theorem gives e<=gamma(gamma+7)/2.

For gamma=2 and gamma=3, equality occurs only, up to graph isomorphism, for H(1,1) and H(2,1), respectively. The reviewed extension completes the equality proof when combined with the previously audited gamma>=4 argument.

The proof requires uniqueness among minimum-cardinality dominating sets. Ordinary minimum domination or uniqueness of an inclusion-minimal set would not justify the replacement arguments. No unrestricted enumeration of all seven- or ten-vertex graphs is claimed. No publication-novelty claim is endorsed; the source already identifies the ten-vertex equality graph, and the extension correctly acknowledges this overlap.

## Seven-vertex equality lemma

The fixed cell has centers x,y, a two-set U adjacent to x, and a three-set W adjacent to y. The optional edges are xy and U-W.

If xy is present and there are four optional edges, no W-column can have two U-neighbors, since {y,w} would then dominate. Hence the three U-W edges occupy all columns once. If one row contains all three, {x,u} is an alternative dominating pair. Otherwise the row degrees are two and one, and the degree-two row vertex together with the other row's neighbor dominates the whole cell. These checks account for both centers, both U vertices and all W vertices.

If xy is absent, four U-W edges have row degrees (3,1) or (2,2). The first configuration has an alternative pair using the full row and a neighbor of the other row. If the two size-two row neighborhoods differ, choose one row vertex and the other row's neighbor outside its neighborhood. This again dominates every vertex. Thus equality and uniqueness force identical size-two row neighborhoods: a K_(2,2), one unused W-column and no xy.

Conversely, with unused column c, every dominating set must meet the disjoint closed neighborhoods N[x]={x,u0,u1} and N[c]={c,y}. A dominating pair chooses exactly one from each. Choosing a U vertex leaves the other U vertex undominated, so x must be selected. Choosing c then leaves the active W vertices undominated, so y must be selected. This proves both minimum size two and uniqueness, not merely that {x,y} is an inclusion-minimal dominating set.

## Global equality reduction at gamma=2,3

The previously audited private-neighbor reduction selects two exterior private neighbors for each member of D and leaves one vertex z. The numerical equality condition forces p=ceil(gamma/2), q=floor(gamma/2). For gamma=2,3, q=1. If y is the sole dominator on that side, domination of z forces zy. Its private pair and z form the three-set W.

The remaining edges partition into p disjoint optional blocks x_i y and U_i-W. Each induced seven-cell has {x_i,y} as its unique dominating set of size at most two: any different local set would extend with all other retained centers to a different global dominating set of size at most gamma. Every outside vertex has its own retained center, while the shared leftover z is inside the cell. Thus there is no uncovered residual-vertex obligation.

The edge count is at most 2p+3+4p. Equality forces four optional edges in every block, so the local lemma makes each U_i complete to exactly two W-columns and forbids x_i y.

For gamma=2, there is one block, directly giving H(1,1).

For gamma=3, let c1,c2 be the two omitted columns. If they differ, the two active-column pairs cover W and have a common member w. Choosing one u_i from each U_i gives the alternative dominating triple {u1,u2,w}. It dominates x1,x2 through the chosen u_i, all four U vertices and y through w, and every W vertex through the two active-column pairs. This is a genuinely different set of cardinality three, contradicting uniqueness. Hence the omitted columns coincide, giving H(2,1).

The converse for both cases follows from the already proved H(p,q) construction, or directly from the disjoint-neighborhood forcing argument. No new hypothesis on connectedness is needed; the equality graphs are connected.

## Independent finite verification

The new independent_low_gamma.py uses no primary code. It builds the reduced skeleton from symbolic labels and tests every graph pattern, including all patterns below the extremal threshold. For each graph it computes the dominated set of every vertex subset by an exact subset-union dynamic program, derives the minimum dominating cardinality, and separately counts all minimizers.

Results:

- gamma=2: all 128 skeleton graphs, all 128 vertex subsets per graph, 16,384 subset tests; 58 patterns have D as their unique minimum set; the maximum is nine edges
- gamma=3: all 16,384 skeleton graphs, all 1,024 vertex subsets per graph, 16,777,216 subset tests; 2,790 patterns have D as their unique minimum set; the maximum is fifteen edges

At or above the proposed equality counts, there are respectively 64 and 6,476 graph patterns. Exactly three labelled patterns survive in each case, and each has the same single omitted W-column across all blocks. Every accepted mask, edge list and omitted column agrees exactly with the primary certificate.

The complete equality-mask lists in the primary bit order are:

    gamma=2: 54, 90, 108
    gamma=3: 7020, 11700, 14040.

The exhaustive scope is the reduced skeleton proved above, not all labelled graphs of these orders. The elementary proof is independent of the enumeration.

## Files and reproduction

Run:

    python independent_low_gamma.py

Only the Python standard library is required. The output and actual stdout are independent_result.json and independent_stdout.json. Source hashes and artifact checksums accompany this report. The existing boundary theorem and earlier manuscript are unchanged.

No blocking mathematical discrepancy was found in LOW_GAMMA_EQUALITY.md.
