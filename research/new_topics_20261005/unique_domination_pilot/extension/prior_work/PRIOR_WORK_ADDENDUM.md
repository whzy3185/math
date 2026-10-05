# Prior public counterexample and the scope of the boundary theorem

Checked 5 October 2026, 08:40–08:42 UTC. This addendum records a source discovered after the first seven-page manuscript was frozen. It changes the attribution of the counterexample; it does not change any mathematical statement or proof in that manuscript.

## Main finding

John Erlbacher's public **Demonstrandum — wave-1 verified artifacts** already contains the same 13-vertex, 22-edge bipartite graph with a unique minimum dominating set of size four. The graph in `candidate13.json` is isomorphic to that prior graph. Thus this individual counterexample, its refutation of Koch–Narayan Conjecture 1, and the associated printed-formula issue should be explicitly credited as prior work.

The present boundary theorem determines the maximum for **every** domination number γ≥2 at order 3γ+1, and classifies equality for γ≥4. No theorem of that scope was located in the inspected prior write-up, its listed verification materials, the current repository index, or the narrowly targeted follow-up searches. This is a bounded comparison, not a proof of priority over all existing or unpublished work.

## Primary sources and dates

1. [Erlbacher, detailed Koch–Narayan write-up, pinned initial snapshot](https://github.com/demonstrandum-research/artifacts/blob/94db9ed50d48a57aae5ccb72e6a95a2b8f8f39d3/problems/p2-factory/kills/koch-narayan/WRITEUP.md). Git blob: `a19396ed57227850e87a6248b9a89269de08c734`. The document dates its verification to 11–12 June 2026.
2. [Initial repository commit](https://github.com/demonstrandum-research/artifacts/commit/94db9ed50d48a57aae5ccb72e6a95a2b8f8f39d3). GitHub author and committer timestamps: 13 June 2026, 01:23:03 UTC. The path-specific commit history contained this single entry. Git commit dates are provenance metadata, not an independently authenticated first-public-availability timestamp.
3. [Prior graph certificate](https://github.com/demonstrandum-research/artifacts/blob/94db9ed50d48a57aae5ccb72e6a95a2b8f8f39d3/problems/p2-factory/kills/koch-narayan/certificate_13_4.json). Git blob: `9daa667811f7fc18fc9304c88f81cbf22cf1effe`.
4. [Current repository citation metadata](https://github.com/demonstrandum-research/artifacts/blob/c03d9915394e6e4906f1447680ed62eda0a023b7/CITATION.cff) names John Erlbacher and records a release dated 8 July 2026. It supplies DOI `10.5281/zenodo.21269439` for that snapshot and concept DOI `10.5281/zenodo.20673864`. The DOI/Zenodo landing pages could not be read in this check, so their independent metadata and archive contents have **not** been verified here. The pinned GitHub file is the directly verified citation.
5. [Koch–Narayan v1, Section 2.1 and Figure 1](https://arxiv.org/html/2511.01719v1#S2.SS1) already states uniqueness of the extremal graph at n=10, γ=3, e=15. Their Theorem 11 proves the γ=2 bound for all admissible orders. Low-γ completion of the present proof therefore has direct prior overlap.

The repository's main branch resolved to `c03d9915394e6e4906f1447680ed62eda0a023b7`, whose commit date is 13 July 2026. Its recursive tree was complete, not truncated. No separate Koch–Narayan manuscript was listed under `papers/`; the result's table entry links only the artifact package.

## Exact mathematical overlap

Both works use finite simple bipartite graphs without isolated vertices, ordinary closed-neighbourhood domination, and uniqueness among minimum-cardinality dominating sets. Neither underlying extremal problem requires connectedness; the common 13-vertex example is connected.

The prior write-up supplies:

- the n=13, γ=4 graph with 22 edges, exceeding the conjectured 21;
- exact finite domination certificates for that graph and five larger examples;
- the distinction between the printed tail cutoff and the construction-consistent cutoff;
- an unbalanced-split construction with edge expression 2γ+2pq+(n−3γ)(2q+1), p+q=γ;
- reported exhaustive extremal values 22, 28, 35 at (n,γ)=(13,4),(14,4),(15,4), with a stated single-implementation qualification for those global sweep conclusions;
- finite tests and discussion of failures beyond the one-residual-vertex regime.

The inspected write-up does **not** give a general upper bound γ(γ+7)/2 at n=3γ+1, a general classification of its equality cases, or the six-/seven-cell reduction that proves those conclusions in the present manuscript. Its unbalanced family at n=3γ+1 has edge count 2γ+2pq+2q+1; the graph achieving the sharper boundary value is treated there as a finite example rather than an all-γ sharp theorem.

Consequently, the appropriate paper emphasis is the sharp boundary maximum and equality theorem. The finite n=13 consequence should be described as recovering a previously reported counterexample. A future n=3γ+2 project must also account for the prior n=14, γ=4, e=28 example and unbalanced construction from its outset.

## Exact isomorphism and independent recheck

The following bijection takes the local certificate's labels to Erlbacher's integer labels:

`x0→8, x1→9, y0→0, y1→1, b00→2, b01→3, b10→4, b11→5, a00→10, a01→6, a10→11, a11→7, z→12`.

The newly written `check_prior_isomorphism.py` checks this map against every edge, then tests all 8192 vertex subsets of the prior graph. It finds exactly one minimum dominating set, `{0,1,8,9}`, of size four. No external verification code is executed or reused. Results are recorded in `isomorphism_result.json`.

## Suggested manuscript attribution

“Erlbacher's public verification artifacts already contain a connected bipartite graph with 13 vertices and 22 edges whose unique minimum dominating set has cardinality four, together with further counterexamples and finite extremal computations. Theorem 1.1 recovers that example as the first member of the sharp boundary family and determines the maximum and equality structure for general domination number at order 3γ+1.”

Suggested bibliographic entry: John Erlbacher, *Demonstrandum — wave-1 verified artifacts: Koch–Narayan counterexample package*, public GitHub research artifacts, 2026; pinned commit `94db9ed50d48a57aae5ccb72e6a95a2b8f8f39d3`, `problems/p2-factory/kills/koch-narayan/WRITEUP.md`.

## Search boundary

This update inspected the full primary write-up, current README and citation metadata, the relevant path's commit history, the recursive repository tree, the explicit graph certificate, and focused searches for the boundary formula and Koch–Narayan follow-ups. ArXiv 2511.01719 remains v1 in the retrieved record. The repository-level counterexample is sufficient to retract any implication that this is a newly discovered refutation, regardless of arXiv revision status. No claim of exhaustive forward-citation coverage is made.
