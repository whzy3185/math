# Final independent review of the integrated unique-domination manuscript

Date: 2026-10-05. Verdict: **PASS. No mathematical, claim-scope, attribution, or rendering blocker found.**

Reviewed the complete 736-line TeX source and all ten rendered PDF pages. The source/PDF hashes in `checked_sources.json` identify the exact reviewed version. This final pass checks the integrated statements and written proofs against the previously audited components; it does not rerun the frozen exhaustive enumerations.

## Statements and assumptions

- Lines 50–82 explicitly use finite simple bipartite graphs without isolated vertices, ordinary domination, and uniqueness among minimum-cardinality dominating sets. Connectedness is not silently imposed on the upper-bound classes
- Theorem 1.1, lines 85–96: the maximum at n=3gamma+1 is gamma(gamma+7)/2 for every gamma>=2, with complete equality classification for every gamma>=2
- Theorem 1.2, lines 98–107: the maximum at n=3gamma+2 is ceil(gamma^2/2)+5gamma for every gamma>=2; connected attainment and at least two nonisomorphic connected extremizers for even gamma>=4 are proved, while complete equality classification is explicitly not claimed
- The abstract, theorems, later conclusions and open-question section agree on these scopes

## Construction and common reduction

Lines 136–190 correctly define H_r(p,q), r in {1,2}, and prove its unique minimum dominating set using pairwise disjoint forced closed neighborhoods. The edge count 2(p+q)+2pq+r(2p+q), both balanced specializations, and connectedness are correct.

The exterior-private-neighbor lemma at lines 209–224 handles zero and one private neighbor separately and uses the no-isolate hypothesis where required. The replacement principle at lines 226–234 explicitly requires all outside vertices to remain dominated. The four optional-edge bounds in lines 238–320 are valid: 2,4,6,6 for private sizes (2,2),(2,3),(2,4),(3,3). The proof of the (3,3) bound correctly handles the center edge and the missing-perfect-matching case.

## One residual vertex and all equality cases

Lines 324–416 retain all possible center edges and residual incidences. In the multiple-owner case the residual keeps a retained owner; in the single-owner case it is included in the special seven-cell. The residual owner edge is counted once, including p=0. Optimization by d=p-q and parity gives the stated balanced split.

The gamma>=4 equality proof in lines 422–464 correctly forces full residual incidence and then excludes center edges, row-stars, and inconsistent column choices by explicit alternative dominating sets.

The gamma=2,3 extension in lines 468–485 is complete. Here q=1 and p=1 or 2. Equality in the seven-cell bound gives two active columns out of three. For p=2, differing omitted columns yield the alternative triple consisting of one vertex from each U pair and their common active column. Thus both small equality cases are isomorphic to the stated H graph. This legitimately extends the earlier gamma>=4 classification to all gamma>=2.

## Two residual vertices: all cases checked

### Same bipartition side, lines 504–534

Every singleton-owned residual is included exactly in the cells whose removed center owns it. Multi-owned residuals retain a center because only one opposite-side center is removed. Optional cell edges, singleton owner edges and remaining residual degrees are disjointly accounted for. The bound

    2pq+6p+4q = gamma^2/2+5gamma+1/2-(p-q-1)^2/2

has the stated ceiling maximum by parity. The p=0 boundary is explicitly covered.

### Opposite sides, both multi-owned, lines 545–565

The bound 2pq+5gamma+1 is correct and counts zw once. For odd gamma it already gives the target. For even gamma, integrality makes any violation exactly target+1, forcing balanced p=q and saturation of both residual degree bounds. Replacing a center pair by the residual pair then dominates the graph, ruling out that excess. This is a valid saturation argument rather than an unsupported subtraction of one.

### Opposite sides, exactly one singleton-owned, lines 567–581

The special cells include the singleton residual, while the multi-owned residual retains an X-center. The owner edge and zw are separately counted once. The resulting bound is 2pq+5gamma+2-q. For q=1, the hypothesis forces p>=2 and gamma>=3; the remaining difference ceil(gamma^2/2)-2gamma+1 is zero at gamma=3 and positive thereafter. No gamma=2 exception is overlooked.

### Opposite sides, both singleton-owned, lines 583–602

The four cell types include each residual exactly when its owner is removed. The mutual edge zw occurs only in the special (3,3) optional block, and the two owner edges are fixed incidences. The expansion to 2pq+4gamma+2 and comparison with the target hold for all gamma>=2, including p=q=1.

These cases exhaust every placement and ownership pattern. The bound is attained by the displayed H_2 construction. Lines 606–610 correctly distinguish H_2(k,k) and H_2(k+1,k-1) by the unordered sizes of the bipartition classes of connected bipartite graphs.

## Source comparison and attribution

The Koch–Narayan primary HTML was checked directly, including Conjecture 1, its Figure 1 discussion at (n,gamma)=(10,3), and the stated gamma=2/the-threshold results.

The pinned Erlbacher write-up was retrieved directly through the GitHub connector at commit `94db9ed50d48a57aae5ccb72e6a95a2b8f8f39d3`; the returned blob was `a19396ed57227850e87a6248b9a89269de08c734`. Its primary example, supplementary family, and exhaustive-sweep sections support the manuscript's attribution.

- Lines 64–70 credit the prior 13-/14-vertex examples, unbalanced construction, finite computations and earlier low-gamma equality observation
- Lines 193–199 correctly identify H_2(p,1) with the earlier two-extra-vertex family after exchanging center-side names, and recognize the shared-center mechanism in the prior 13-vertex graph
- Lines 614–634 correctly specialize the source formulas, compute the excesses b-1 and 2(b-1), and compare the prior gamma=5 family value 36 with the new sharp value 38
- Neither the prose nor the bibliography claims priority for those examples/mechanisms, authenticated first-publication timing, a smallest counterexample, or exhaustive novelty coverage

The attribution is consistent with the directly inspected primary source. No further literature search is implied by this review.

## Evidence and rendering

The supplementary count table and its scope at lines 645–710 agree with the existing independent audit outputs. The reduced-skeleton enumerations are not mislabeled as unrestricted graph censuses; finite checks are not presented as substitutes for the elementary proofs. No Lean formalization is asserted.

All ten rendered pages were visually inspected, including the theorem statements, local-cell lemmas, the complete two-residual case split, source comparison and bibliography. Mathematical symbols and equations match the TeX. No clipping, overlapping text, broken references, missing glyphs or unreadable formulas were observed. The build log contains no overfull-box, undefined-reference or warning entries in the checked version.

No revision is required by this final review.
