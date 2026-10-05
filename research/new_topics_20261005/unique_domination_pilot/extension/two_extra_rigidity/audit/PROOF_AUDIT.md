# Independent audit of equality two vertices above the threshold

Date: 2026-10-05. General equality proof and independent exact checks: **PASS**.

## Audited classification

Let G be finite, simple, bipartite and without isolated vertices. Assume |V(G)|=3 gamma+2, its unique minimum-cardinality dominating set has size gamma>=2, and its edge count attains the previously audited maximum ceil(gamma^2/2)+5 gamma.

The reviewed argument proves exactly these graph-isomorphism classes:

- gamma=2: H2(1,1), F0 and F1
- odd gamma=2k+1>=3: H2(k+1,k)
- even gamma=2k>=4: H2(k,k) and H2(k+1,k-1)

Hence the class counts are three, one and two, respectively, and every equality graph is connected. The result concerns complete graphs up to isomorphism, not counts of labelled private-neighbor decompositions. No publication-priority claim or statement about three residual vertices is endorsed.

The proof reviewed is ../RIGIDITY_THEOREM.md. Its sharp upper bound, exterior-private-neighbor reduction and H2 attainment theorem are the already audited dependencies. The present audit checks the additional equality deductions and their completeness.

## Equality arithmetic and residual placements

Choosing two exterior private neighbors per center leaves exactly two residual vertices. In the same-side placement, with p centers on their side and q opposite centers, the upper bound is

    e <= 2pq+6p+4q-S(q-1) <= ceil(gamma^2/2)+5 gamma,

where S is the number of singleton-dominated residuals and q>=1. Equality requires p-q=1 for odd gamma and p-q in {0,2} for even gamma. These conditions give exactly the stated H2 parameter splits; no p=0 equality case survives. At gamma=2, the putative q=0 split is impossible because the residual vertices must be dominated by an opposite-side center.

In opposite-side placement, each residual has a nonempty center-neighborhood on its opposite side. The division into two multiple-owner residuals, one singleton-owner residual, and two singleton-owner residuals is exhaustive. All equality deductions preserve the outside-cell domination conditions from the upper-bound proof.

### Two multiple-owner residuals

For odd gamma, equality forces balanced center sizes and full saturation of the residual incidence bounds. Replacing any opposite center pair by the two residuals dominates every vertex and contradicts uniqueness.

For even gamma, equality forces p=q=k>=2 and exactly one total deficit relative to the upper estimate 2pq+5 gamma+1. Deficits are nonnegative integers: each six-cell is bounded by two optional edges, each residual incidence block by its complete allowable degree, and the residual edge by one. Therefore at most one residual incidence is missing.

If the missing incidence belongs to an X-center or its private pair, choose a different X-center to remove; if it belongs to a Y-center or its pair, choose a different Y-center. Such a choice exists because k>=2. Missing incidences to retained centers or their pairs are harmless, while a deficit in an optional cell or the residual edge does not affect the replacement. The set (D minus the chosen center pair) union {z,w} therefore gives a distinct dominating gamma-set. This excludes equality, including the one-deficit case that was not excluded merely by the earlier strict upper-bound argument.

### One singleton-owner residual

The exact target-minus-bound difference is

    ceil(gamma^2/2)-2pq+q-2.

If q>=2 it can vanish only at p=q=2. For odd gamma the first two terms already contribute at least one. If q=1, the other residual's multiple-owner condition gives p>=2 and gamma>=3, and the difference vanishes only at gamma=3, p=2. Thus the only numerical candidates are (p,q)=(2,1) and (2,2).

Saturation gives the multiple-owner residual w all X-neighbors, all V-neighbors, and the edge wz. The two special seven-cells have complete U rows to two columns of the shared three-set W. Those two active-column pairs have a common member c. Then

    {w,c} union (Y minus {the owner of z})

has cardinality gamma-1 and dominates the whole graph. In particular, c covers both complete U pairs and the removed Y-center, w covers all X-centers, all V vertices and z, and the remaining Y-centers are selected. This works also when c=z. It contradicts the domination number, not merely uniqueness. Both mixed-owner exceptions are excluded.

### Two singleton-owner residuals

The audited bound 2pq+4 gamma+2 is strictly below the target for gamma>=3, with gap at least gamma-2. Thus no equality case is omitted here. At gamma=2 the whole graph becomes the balanced (3,3) cell and is treated separately below.

Consequently every equality graph with gamma>=3 has same-side residuals. The argument is valid for any selected exterior-private pairs, so the classification does not presume a special decomposition exists.

## Same-side rigidity

### q>=2

Equality forces S=0, complete residual incidences to every Y-center and every U vertex, and equality in every six-cell bound.

A center edge x_i y_j would permit replacing x_i by z; the other residual remains dominated by retained Y-centers. Thus all center edges are absent. Each six-cell is then a two-edge star. A row-centered star permits replacing x_i,y_j by its row vertex and z; the second residual retains another Y-neighbor because q>=2. Hence every block is a column star.

For a fixed Y-center, column choices cannot vary across X-centers. If both private columns occur, selecting z, one vertex from every U pair, and every other Y-center gives a different dominating gamma-set. The second residual again retains a Y-neighbor. Therefore each column choice is uniform, and relabelling each V pair gives exactly H2(p,q). The complete edge accounting leaves no other edges or components.

### q=1

The equality splits restrict p to 1, 2 or 3, corresponding to gamma=2,3,4. This restriction is essential to the next intersection argument.

In the (2,4) local cell, six optional edges force no center edge and equal size-three row neighborhoods. A center edge would allow at most five optional edges. A full row or differing size-three rows would give an alternative pair, as checked in the proof. Thus each U_i is complete to all but one of four common W-columns.

If the omitted columns vary, their active sets cover W. Since p<=3<4, some column remains active in every block. That column together with one vertex from each U_i gives a distinct dominating gamma-set. The omitted columns must therefore coincide. The three active columns may be relabelled as the active V vertex and the two residuals, giving H2(p,1).

This completes the general same-side classification without assuming that the residual vertices were uniquely identifiable in the original decomposition.

## The gamma=2 balanced exceptions

Opposite-side residuals imply p=q=1 and make the whole graph a (3,3) private cell, with six fixed and six optional edges.

If the center edge is absent, the cross matrix has six entries. With no full row or column it has all row/column degrees two and gives an alternative pair at a missing entry. If a full row exists, no column may be full. The remaining three entries consequently occupy the three columns once. A (2,1) division between the other rows gives an alternative pair; the only possibility is a (3,0) division. This is K_(2,3) plus an unused row, giving F0, up to interchanging sides.

If the center edge is present, five cross edges have no full row or column. All row and column degrees are (2,2,1). A simple bipartite graph on these six private vertices, with maximum degree two, no isolates and five edges, is either P6 or C4 disjoint union K2. P6 has the explicit alternate pair given in the proof. The remaining type is F1.

The uniqueness checks for F0 and F1 are correct. In F0 the leaf/center forced-neighborhood argument leaves only {x,y}. In F1, an opposite-private pair could dominate only if both its cross-degrees were two and its endpoints were nonadjacent; every such pair lies in the complete C4 block and is adjacent. All other pair types miss a center or private vertex. Singletons cannot dominate the bipartite graph of part sizes four and four.

F0 and F1 have the stated distinct degree sequences. H2(1,1) has bipartition sizes three and five rather than four and four. These are complete-graph invariants, so they distinguish three isomorphism classes independently of private-pair labelling.

For even gamma>=4, the two H2 parameter splits have unordered connected bipartition sizes {3k,3k+2} and {3k+1,3k+1}. These prove nonisomorphism. Odd gamma has only one allowable split. Attainment and connectivity are inherited from the audited construction theorem.

## Independent exact verification

The standalone independent_rigidity.py imports no primary verifier. It independently regenerates the local maximum-pattern lists, same-side patterns, mixed-owner assemblies and sparse residual witnesses.

### Full-graph isomorphism

The checker uses exhaustive vertex-bijection backtracking with degree/color refinement and exact adjacency and nonadjacency checks. It does not fix the dominating centers, private blocks, or a supplied bipartition mapping. Refinement only discards impossible mappings; the remaining bijection search is complete.

- All 15 balanced gamma=2 patterns are regenerated and have exactly two full-graph classes: six F0 patterns and nine F1 patterns
- H2(1,1), F0 and F1 are pairwise nonisomorphic by this independent routine
- Every accepted same-side pattern is checked for an actual full-graph isomorphism to its designated H2 graph

### Reduced equality patterns

All 164 same-side patterns in the claimed bounded check were regenerated. Exactly four labelled patterns survive at each of (p,q)=(1,1),(2,1),(2,2),(3,1),(3,2), and every survivor maps to its H2 representative. All rejected patterns have a separately found dominating set of size at most gamma.

All nine gamma=3 and all 576 gamma=4 mixed-owner candidates were rebuilt using freshly generated local extremal cells. Each has the explicit smaller dominating set, and independent search confirms minimum size at most gamma-1. No candidate survives.

Sixty-four additional sparse residual checks cover the balanced one-deficit replacements at k=2,3,4 and several odd saturated splits. The witnesses hold already with no optional cell edges, so adding those edges cannot invalidate domination. These finite checks corroborate the general replacement proof; they do not replace its unbounded quantifiers.

### Broader gamma=2,3 equality catalog

A separate C++ program reruns the independent complete private-pair-skeleton sweep used for the prior upper-bound audit and now emits every equality graph. This search precedes the new star and coherence reductions.

It covers 1,197,626 valid reduced graph patterns for gamma=2,3. Every one of the 116,635 graphs at or above the extremal edge threshold is checked for a different dominating set of size at most gamma. It finds nineteen labelled gamma=2 equality representations and four gamma=3 representations, with no over-bound graph.

The new unrestricted graph-isomorphism checker classifies those full edge lists as:

    gamma=2: four H2(1,1), six F0, nine F1 representations
    gamma=3: four H2(2,1) representations.

These representation multiplicities are not claimed as counts of all labelled global graphs. They independently confirm that decomposition choices do not create additional small-order isomorphism classes.

## Reproduction and artifacts

From this audit directory:

    g++ -O3 -std=c++17 -Wall -Wextra boundary_catalog.cpp -o boundary_catalog
    ./boundary_catalog > boundary_catalog_stdout.txt
    python independent_rigidity.py > independent_stdout.json

Python requires only the standard library. The independent files are:

- boundary_catalog.cpp and boundary_equality_catalog.txt
- boundary_catalog_stdout.txt
- independent_rigidity.py and independent_result.json
- independent_stdout.json
- source_manifest.json and SHA256SUMS

No mathematical correction was required. The general equality theorem is supported at the stated scope; the earlier paper_v2 remains a separate frozen version.
