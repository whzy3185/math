# Independent integration review of the third unique-domination manuscript

Date: 2026-10-05. Corrected source and complete rendered PDF: **PASS**.

Reviewed manuscript: *Sharp boundary bounds and edit instability in uniquely dominated bipartite graphs*, third version. The final PDF has 15 pages; the supplementary-check appendix was shortened to remove a nearly empty final page from the 16-page draft. The earlier paper_v2 remains separate and unchanged.

The reviewed PDF SHA-256 is

    0770d1fb9f1fcde75f645609b671b8ff05fc48b2f8f579eaff071f0fa5801039

The corresponding TeX SHA-256 is

    3251481ac7c0567a3c6586c77618f35e809c6da45dd378a669e0885892166453

The source manifest records the complete reviewed bytes. This review checks integration against the independently audited component proofs; it is not external peer review or a publication-priority certification.

## Theorem hypotheses and scopes

The final abstract, class definition and stability theorem explicitly require integer domination number gamma>=2. This restriction is essential: without it, the stability theorem would refer to the undefined H(1,0), and the displayed extremal formulas would not cover the gamma=1 star cases.

The graph classes consistently consist of finite simple bipartite graphs without isolated vertices and with a unique minimum-cardinality dominating set. Inclusion-minimality is explicitly distinguished. Connectedness is not assumed for either upper bound, either equality classification or the stability upper bound. The equality graphs and the obstruction examples are proved connected as conclusions.

The one-residual theorem includes all gamma>=2 equality cases. The two-residual theorem correctly states exactly three graph-isomorphism classes at gamma=2, one at odd gamma>=3, and two at even gamma>=4. These are full-graph classes, not counts of labelled private-neighbor decompositions.

## Boundary bounds and complete equality proofs

The H_r construction, edge counts and disjoint-neighborhood uniqueness proof agree with the audited sources. Both residual-placement cases and all singleton/multiple-owner subcases preserve the required outside-cell domination obligations. The residual edge in opposite-side two-residual cases is neither omitted nor counted twice.

The two-residual equality proof retains the important even-gamma one-deficit argument, the smaller dominating sets excluding the gamma=3 and gamma=4 mixed-owner cases, the second residual's domination in the same-side replacements, and the p<=3 restriction in the q=1 column-intersection argument.

The eight-vertex exceptions are explicitly reconstructible:

- F0 has fixed xU,yV edges, no center edge, and K_(2,3) on two U vertices and all V
- F1 has fixed xU,yV edges, the center edge, a K_(2,2) cross block and the remaining private matching edge

Their twelve-edge counts, unique minimum dominating pairs, degree sequences and balanced bipartitions agree with the independent catalog. The H2(1,1) row has the correct unequal bipartition sizes and degree sequence. The larger even-gamma H2 classes remain distinguished by connected bipartition sizes.

## Stability theorem

The edit metric is defined as the minimum edge symmetric-difference size over every vertex bijection. One addition or deletion costs one, and relabellings need not preserve the displayed bipartition or dominating set.

The nonnegative edge deficit is integral. The proof treats t=0 by the audited equality theorem and t>=1 by the repair argument or the singleton-owner fallback. The added trivial bound

    d_edit <= e(G)+e(H*) = gamma(gamma+7)-t

is valid, so taking its minimum with 12 gamma t in the theorem is justified.

The integrated proof preserves the exact slack identity B+L+R, good-row and good-column conditions, the three-center coherence replacement, the repair counts, the p=0 intermediate template, the h^2<=B imbalance estimate, and the moved-triple degree bound. The singleton-owner argument correctly includes gamma=2,3 and uses the separate deficit lower bound for larger gamma. No connectedness is introduced.

The constant 12 is an upper-bound constant; the paper does not claim it is optimal. The matching-order statement is confined to the stated lower-example regime, rather than asserting a matching lower bound for every possible deficit.

## Obstruction construction and asymptotic consequences

The modified row deletes the active-column incidences and the residual incidence at the same private vertex, thereby creating a leaf. The new center-center edges are therefore compatible with the disjoint forced-neighborhood proof of unique minimum domination.

The parameter range k>=2 and 1<=s<=k-1 is present. The graph has exact deficit s, and the sorted degree groups are correct, including endpoint ties. The lower bound s(k+1) applies to all vertex relabellings; the identity modification gives the separate upper bound s(2k+1).

The substitution k=s^2 correctly disproves a uniform O(gamma sqrt(t)+t) estimate. The choice s=floor(k/2) gives relative edge deficit tending to zero and normalized edit-distance liminf at least 1/72. These statements concern the first boundary only. No stability claim for the second boundary or for different distance metrics is introduced.

## Notation, verification summaries and attribution

The residual owner count in the earlier upper-bound sections is now ell, leaving t for the edge deficit in the stability result. Cross-references and theorem dependencies resolve consistently.

The finite-check appendix now correctly states that exactly twenty of the 164 same-side patterns survive, four at each tested split, and only those survivors map to the stated H2 graphs. The remaining patterns have alternative dominating sets. The local pattern totals, mixed-owner counts and graph-isomorphism distinctions match the independent audit records.

The manuscript explicitly credits the prior thirteen-/fourteen-vertex counterexamples, the q=1 subfamily and known low-order source results. It does not claim a smallest counterexample over all orders, literature-wide novelty, an optimal stability constant, or Lean formalization.

## Corrections resolved during integration review

- Added gamma>=2 to the abstract, class definition and stability theorem
- Replaced the conflicting residual-owner symbol t by ell
- Distinguished the twenty surviving same-side patterns from all 164 tested patterns

No unresolved statement-scope, proof-transcription or integration issue remains.

## PDF verification

All 15 final pages were visually inspected. The displayed bounds, ceiling/floor notation, graph definitions, equality table, degree lists, stability estimates and references are legible and unclipped. Page numbering and cross-references are complete. The final build log has no warnings or overfull/underfull boxes.

Only final pages 1 through 15 belong to this PDF; any older sixteenth QA image is an intermediate artifact and was excluded from this final review.

Final layout reconciliation: the uncrossing inequality is now kept together as a display, and the supplementary-check summary is shortened. The three affected pages (13--15) were re-inspected against the refreshed PDF; the inequality, twenty-of-164 qualifier, verification scopes and full references remain intact. The verdict remains PASS on the refreshed hashes above.
