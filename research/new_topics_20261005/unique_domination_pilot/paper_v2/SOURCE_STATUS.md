# Primary sources and contribution scope

Version 2, 5 October 2026. Source checks were performed on the same date, including the final targeted two-residual queries at 08:58 UTC. No further broad literature search is inferred from the manuscript integration.

## Koch and Narayan

Garrison Koch and Darren Narayan, *Maximal bipartite graphs with a unique minimum dominating set*, arXiv:2511.01719v1, 3 November 2025.

- [Current record](https://arxiv.org/abs/2511.01719)
- [Pinned PDF](https://arxiv.org/pdf/2511.01719v1)
- [Pinned HTML](https://arxiv.org/html/2511.01719v1)
- Conjecture 1: PDF page 2
- Theorem 11: sharp γ=2 bound for all admissible orders
- Theorem 12: the threshold n=3γ and its six-vertex replacement estimate
- Section 2.1, Figure 1 discussion: already identifies uniqueness of the n=10, γ=3, 15-edge extremal graph
- Retrieved PDF SHA256: 49a9327b22e6928b77e6bd01119179f5e4bd1cc851d3fc7f33a31c162642d43c

The retrieved arXiv record lists v1 only. No separate author erratum was located. That version status does not imply that the conjecture is still unresolved: the public counterexample package below already refutes it.

## Erlbacher

John Erlbacher, *Demonstrandum — wave-1 verified artifacts: Koch–Narayan counterexample package*, public research artifacts, 2026.

- [Pinned write-up](https://github.com/demonstrandum-research/artifacts/blob/94db9ed50d48a57aae5ccb72e6a95a2b8f8f39d3/problems/p2-factory/kills/koch-narayan/WRITEUP.md)
- Commit: 94db9ed50d48a57aae5ccb72e6a95a2b8f8f39d3; Git author/committer timestamp 13 June 2026
- Write-up blob: a19396ed57227850e87a6248b9a89269de08c734
- 13-vertex graph certificate blob: 9daa667811f7fc18fc9304c88f81cbf22cf1effe
- 14-vertex graph certificate blob: 68119109e82801cb23f9edfa42c78c9228ba02f1

The manuscript credits the prior 13-vertex counterexample, 14-vertex example, unbalanced construction and cutoff issue. Explicit new checks map H₁(2,2) and H₂(3,1) to the respective prior certificates. H₂(p,1) is the known two-residual unbalanced subfamily. The shared-center mechanism for q>1 already appears in the prior 13-vertex example. No construction-priority claim is made.

The inspected prior write-up reports global finite extrema at γ=4, n=13,14,15, with a single-implementation qualification. It does not give the two all-γ upper bounds proved here, nor their general equality analysis. This is a comparison of inspected sources, not an exhaustive novelty guarantee. Repository dates are Git provenance metadata rather than authenticated first-publication dates. The repository citation metadata provides Zenodo DOIs, but their landing pages and archive contents were not independently retrieved; the bibliography uses the directly verified pinned GitHub source.

## Scope of this manuscript

- All γ≥2: sharp n=3γ+1 maximum γ(γ+7)/2, with complete equality classification
- All γ≥2: sharp n=3γ+2 maximum ⌈γ²/2⌉+5γ, with connected attainment
- Even γ≥4: at least two nonisomorphic extremal graphs in the second regime
- No complete second-regime equality classification, general-residual theorem, global smallest-counterexample claim, or Lean formalization

Other primary references retained for historical context are Fischermann–Rautenbach–Volkmann, Discrete Mathematics 260 (2003), 197–203, and Fraboni–Shank, Australasian Journal of Combinatorics 46 (2010), 91–99, [journal PDF](https://ajc.maths.uq.edu.au/pdf/46/ajc_v46_p091.pdf).
