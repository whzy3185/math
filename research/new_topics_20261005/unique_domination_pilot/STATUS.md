# Current mathematical status

Independent mathematical audit: PASS, 5 October 2026.

The theorem max e(G)=gamma(gamma+7)/2 for bipartite graphs without isolated vertices of order3gamma+1 and unique minimum dominating set sizegamma is supported by a complete elementary proof and the independent audit in audit/PROOF_AUDIT.md. Connectedness can be imposed without changing the maximum. Equality rigidity has been proved and audited for gamma>=4.

The connected13-vertex,22-edge example has a unique minimum dominating4-set and contradicts Conjecture1 of Koch–Narayan2511.01719v1, whose specialized bound is21. The comparison is unaffected by the separate tail-cutoff typo.

Finite checks are supplementary: they are not essential hypotheses of the analytic proof. No Lean formalization or journal peer review is claimed. No claim of complete literature novelty is made.

Earlier candidate status is superseded by this current status record and the independent audit.

## Prior-work attribution update, 5 October 2026

The 13-vertex, 22-edge example and the printed-cutoff issue were already reported in John Erlbacher's public [Demonstrandum counterexample package](https://github.com/demonstrandum-research/artifacts/blob/94db9ed50d48a57aae5ccb72e6a95a2b8f8f39d3/problems/p2-factory/kills/koch-narayan/WRITEUP.md), whose Git commit is dated 13 June 2026. An explicit isomorphism and fresh exhaustive check are in extension/prior_work/. The present contribution is framed as the all-gamma sharp boundary maximum and equality theorem; no proof of that general theorem was located in the inspected prior package. This is a bounded source comparison, not an exhaustive priority claim. Mathematical statements and audit conclusions are unchanged.
