# Two-residual-vertex source comparison

Checked 5 October 2026. The global two-residual bound has a complete analytic proof and passed independent mathematical review on 5 October 2026. The comparison below concerns only the primary sources actually inspected.

## Koch–Narayan

Garrison Koch and Darren Narayan, *Maximal bipartite graphs with a unique minimum dominating set*, [arXiv:2511.01719v1](https://arxiv.org/html/2511.01719v1), 3 November 2025. The current arXiv record retrieved on 5 October 2026 still lists only v1. Theorem 11 already gives the sharp γ=2 edge value n(n−2)/4 at even n, hence 12 at n=8. Theorem 12 addresses n=3γ, not the whole n=3γ+2 regime.

At n=3γ+2, with a=⌈γ/2⌉ and b=⌊γ/2⌋, their Conjecture 1 specializes to 2γ+2ab+4a+2. The tail is zero under both the printed and construction-consistent cutoff. The present balanced twin family has 2γ+2ab+4a+2b edges, an excess of 2(b−1). These refutations at γ≥4 should be discussed in the context of prior counterexamples, rather than as a previously unknown falsity of the conjecture.

## Erlbacher's public artifacts

John Erlbacher, *Demonstrandum — wave-1 verified artifacts*, [Koch–Narayan write-up at pinned commit](https://github.com/demonstrandum-research/artifacts/blob/94db9ed50d48a57aae5ccb72e6a95a2b8f8f39d3/problems/p2-factory/kills/koch-narayan/WRITEUP.md). The commit metadata are dated 13 June 2026; the write-up describes work dated 11–12 June. The directly checked write-up Git blob is `a19396ed57227850e87a6248b9a89269de08c734`.

That package gives:

- a [14-vertex, γ=4, 28-edge certificate](https://github.com/demonstrandum-research/artifacts/blob/94db9ed50d48a57aae5ccb72e6a95a2b8f8f39d3/problems/p2-factory/kills/koch-narayan/certificate_14_4.json), blob `68119109e82801cb23f9edfa42c78c9228ba02f1`;
- a reported exhaustive maximum of 28 for that parameter pair, explicitly qualified as a single-implementation global sweep;
- an unbalanced-split family whose formula is 2γ+2p′q′+r(2q′+1), p′+q′=γ, r=n−3γ;
- a 20-vertex, γ=6, 46-edge example at r=2, obtained with p′=2,q′=4.

The twin construction H₂(p,1) is exactly the published family after interchanging the center-side labels p′=1,q′=p. In particular, H₂(3,1) is the previously published n=14 certificate. `check_two_extra.py` verifies an explicit map of all 28 edges and the unique four-element dominating set. This lower-bound subfamily is credited as prior work.

For q>1 the formulas and adjacencies differ: each twin in H₂(p,q) meets q centers, whereas each published bulk vertex meets one. Under p′=q,q′=p, the twin construction has 2(q−1) additional edges. The shared-center mechanism itself was already present in the prior n=13 counterexample, so no independent priority claim is made for the construction idea.

For example, the candidate value at γ=5 is 38, attained by H₂(3,2). Maximizing the displayed prior unbalanced formula over all positive p′,q′ at γ=5,r=2 gives 36. This is a comparison with that explicit formula, not a claim that no other prior 38-edge construction exists.

No all-γ formula ⌈γ²/2⌉+5γ or general upper proof for n=3γ+2 was located in the full inspected write-up, its current result index, or the focused follow-up searches. The candidate theorem's principal point is this proposed upper bound and its structural case analysis. The prior isolated counterexamples and finite extremal values remain explicitly credited. The search is bounded and does not establish exhaustive literature novelty.
