# Claim ledger

## D1 Counterexample family

Proved and independently audited: the explicitly defined connected bipartite H(p,q) has unique minimum domination number p+q and 2pq+4p+3q edges. With p=ceil(γ/2), q=floor(γ/2), it violates arXiv:2511.01719v1 Conjecture 1 at n=3γ+1 for every γ>=4, by floor(γ/2)-1 edges. The n13 witness is exactly checked. This is distinct from the separate distant-range cutoff discrepancy. The n13 counterexample and printed-cutoff issue have prior public reports by John Erlbacher, now explicitly cited and matched by an exact isomorphism check. No whole-domain minimality or priority claim.

## D2 Sharp boundary and rigidity

Proved by a complete elementary proof and independently audited: for every γ>=2 the sharp maximum at n=3γ+1 is γ(γ+7)/2, with the same maximum for connected graphs. For γ>=4 the equality graph is unique up to isomorphism, namely the balanced H construction. The two-private-neighbor reduction, six/seven-vertex replacement lemmas, complete edge accounting and three equality replacement arguments are analytic. Finite checks are supplementary; no induction from finite samples is used.

## M1 Hall ratio

Proved structurally and verified by exact finite certificates: Hall ratio(M6)=10/3 under M2=K2. Exact graph reconstruction, complete maximal-independent-set enumeration, a 20/6 witness and all 273 rational-certificate nodes have independent replays. Numerical discovery output supplies no accepted proof premise.

## Boundaries

The initial Mycielski pilot did not classify equality; the subsequent M2 supplement below now completes that finite classification. No asymptotic theorem is claimed. The initial domination paper states rigidity for γ>=4; the independently audited D3 supplement now completes γ=2,3. Neither topic has a Lean formalization here. Current-source searches are bounded and do not certify absolute novelty. These are research deliverables, not journal submissions or external peer-review claims.



## M2 Complete equality classification and general compression

Independently audited exact finite classification: all Hall maximizers in M6 have20 vertices, independence number6 and include the final apex. There are1,990 labelled subsets in199 orbits under the full ambient group D5, every orbit of size10. Layer types(13,6,1),(14,5,1),(15,4,1) have109,83,7 orbits. They are not claimed to be199 abstract induced-graph isomorphism types.

Twenty-two additional rational-certificate nodes force the equality size/apex conditions. Two structurally different complete integer algorithms produce the same199 canonical masks, and every one of1,990 labelled subsets is independently checked. The general theorem m(mu(G))=m(G)+#{N(I):I independent in G} holds for nonempty finite simple base graphs; the claimed work bound is parameterized by i(G), not polynomial-time Hall optimization in n. See mycielski_strengthening/ and the six-page note.

## Attribution and manuscript status

The seven-page domination article now credits the prior n13 counterexample in its abstract, introduction and bibliography. Its central all-γ sharp theorem and equality classification remain independently audited; broad publication priority is not certified. The six-page Mycielski note includes a Chinese abstract and explicitly identifies the computer-assisted finite boundary. Both PDFs were compiled, source-reviewed and visually checked; no author identity, journal submission or peer-review status is invented.


## D3 Complete low-γ equality cases

A complete elementary argument and separate exact audit prove that the extremal graphs at n=3γ+1 are H(1,1) and H(2,1) for γ=2 and3. Combined with D2, the equality classification is now valid for every γ>=2. The sharpened seven-vertex equality lemma forces a K(2,2) across two of three columns; inconsistent omitted columns in the γ=3 skeleton yield an alternative minimum dominating set.

The independent checker examines all128 seven-vertex and16,384 ten-vertex reduced skeletons, using16,384 and16,777,216 subset tests respectively. This is not an unrestricted census of all graphs of those orders. Small-case prior overlap is explicitly credited; no novelty or Lean claim is added. See unique_domination_pilot/extension/LOW_GAMMA_EQUALITY.md and its audit. The seven-page first paper remains unchanged; this is a separate completion.


## D4 Sharp second boundary and integrated revision

For every γ>=2, the sharp edge maximum at n=3γ+2 is ceil(γ²/2)+5γ for finite simple bipartite graphs without isolates and with a unique minimum dominating γ-set. A complete elementary argument and independent audit prove the upper bound; connected graphs attain it. For even γ>=4 at least two nonisomorphic connected extremals attain equality. A complete second-boundary equality classification is still open in this package.

The ten-page paper_v2 integrates D2–D4, completes first-boundary rigidity for all γ>=2, and preserves the previous seven-page article. The source's small finite cases, Erlbacher's n13/n14 counterexamples and shared-center construction mechanism are explicitly credited. The integrated proof and all ten rendered pages passed a separate review. No Lean, broad novelty or journal peer-review claim is added.
