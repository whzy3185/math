# Primary source status

Checked 5 October 2026, most recently 08:40–08:44 UTC.

Garrison Koch and Darren Narayan, Maximal bipartite graphs with a unique minimum dominating set, arXiv:2511.01719v1, submitted 3 November 2025.

- Canonical record: https://arxiv.org/abs/2511.01719
- Version-fixed PDF: https://arxiv.org/pdf/2511.01719v1
- Full-text HTML: https://arxiv.org/html/2511.01719v1
- Exact claim location: Conjecture 1, PDF page 2
- Retrieved PDF SHA-256: 49a9327b22e6928b77e6bd01119179f5e4bd1cc851d3fc7f33a31c162642d43c

The record checked lists v1 only, with no later version or withdrawal. A targeted search did not locate a separate author erratum. A subsequent primary-source search located an earlier public counterexample package by John Erlbacher, detailed below. ArXiv revision status alone does not establish that the conjecture remains open.

The paper compares only the n=3gamma+1 specialization. With a=ceil(gamma/2),b=floor(gamma/2), that expression is 2gamma+2ab+2a+1. Its summation tail is zero. The reverified, previously reported 13-vertex example has 22 edges and gamma 4, whereas this expression is 21. The comparison remains the same under the natural repair of the source's separate distant-range cutoff.

The six-vertex replacement estimate in the new paper explicitly credits the proof of Theorem 12 in the source. The theorem gives the next-order sharp bound and its equality rigidity. No publication priority or exhaustive novelty claim is inferred from this version check.

Other primary references used for context:

- Fischermann, Rautenbach, Volkmann, Maximum graphs with a unique minimum dominating set, Discrete Mathematics 260 (2003), 197–203
- Fraboni, Shank, Maximum graphs with unique minimum dominating set of size two, Australasian Journal of Combinatorics 46 (2010), 91–99; https://ajc.maths.uq.edu.au/pdf/46/ajc_v46_p091.pdf

## Prior public counterexample identified during the final source check

John Erlbacher, Demonstrandum — wave-1 verified artifacts: Koch–Narayan counterexample package:

https://github.com/demonstrandum-research/artifacts/blob/94db9ed50d48a57aae5ccb72e6a95a2b8f8f39d3/problems/p2-factory/kills/koch-narayan/WRITEUP.md

The path-specific Git history gives commit 94db9ed50d48a57aae5ccb72e6a95a2b8f8f39d3, dated 13 June 2026. These are Git provenance timestamps, not an independently authenticated first-public-availability date. The write-up's blob is a19396ed57227850e87a6248b9a89269de08c734.

The same 13-vertex graph, the printed-cutoff issue, larger counterexamples, and finite extremal values were already reported there. An explicit isomorphism and fresh all-subset recheck appear in ../extension/prior_work/. The manuscript now credits that work. No general sharp formula gamma(gamma+7)/2 at n=3gamma+1 or all-gamma equality theorem was located in the inspected package, current repository index, or targeted follow-up searches. This bounded comparison does not establish exhaustive novelty.

Koch–Narayan's Section 2.1, Figure 1 discussion, already states uniqueness of the n=10, gamma=3, 15-edge extremal graph. Any later low-gamma completion must acknowledge that overlap.
