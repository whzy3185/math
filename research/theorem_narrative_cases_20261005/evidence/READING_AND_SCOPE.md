# Reading scope and claim checks

Date: 2026-10-05. The detailed study distinguishes the exact text read from later journal metadata. It does not claim seven line-by-line proof verifications or equivalence of the preprint and journal versions.

## Reading

The pages and sections actually revisited are listed per record in `source_catalog.json` and in each case note. Work included the abstract, the relevant introduction/theorem hierarchy, selected substantive proof passages, and the actual ending or limitations. S4/S5/S7 do not have separate closing-question sections; the analysis does not invent them. Institutional affiliations were checked on page1 of each exact PDF. Public author emails and funding details were not collected into this package.

All seven original corpus PDFs match the SHA256 and page counts recorded in the catalog. These identities distinguish the research texts; their copyrighted full texts and images are not reproduced here.

## DOI checks

Each arXiv DOI was checked against its versioned arXiv page, DataCite registration and a DOI resolver redirect. A subsequent direct HTTPS request reached the arXiv abstract page with HTTP200 for all seven. The DOI is unversioned; use the exact version URL to reproduce the reading.

Five journal counterparts are recorded: S1,S2,S6,S7 with matching title/author evidence (S1 title edited), and S5 with a substantially changed title but matching authors, objectives and distinctive theorem cases. S5's future issue date is kept separate from its unknown first-online date. S3/S4 journal status remains unverified after bounded title/author searches and Crossref candidate checks.

Registered publisher targets were independently checked through DOI redirects. Some full landing pages failed: Wiley returned403, and Elsevier gateways could return HTTP200 with a 195-byte Site Unavailable page. That is not successful full-text access. Crossref metadata and indexed primary publisher pages supplied the relevant bibliographic evidence. Details appear in `doi_checks.json`; full third-party HTML is not redistributed.

## C029: exact places supporting the narrative

Frozen version: [20-page v3](https://github.com/whzy3185/math/blob/8ce218113ed07e3879ddc8bc157c7d32e77ad206/research/c029_holonomy_schur_20261005/manuscript_v3/manuscript.pdf).

- [Introduction](https://github.com/whzy3185/math/blob/8ce218113ed07e3879ddc8bc157c7d32e77ad206/research/c029_holonomy_schur_20261005/manuscript_v3/sections/01_introduction.tex): prescribed words, canonical signing, both holonomies, strict caps, attribution of prior witness ranges, and separation from unrestricted minima
- [Section4](https://github.com/whzy3185/math/blob/8ce218113ed07e3879ddc8bc157c7d32e77ad206/research/c029_holonomy_schur_20261005/manuscript_v3/sections/04_chain_reduction.tex): cI−A² positivity criterion, four-site recurrence, finite rational premises
- [Section5](https://github.com/whzy3185/math/blob/8ce218113ed07e3879ddc8bc157c7d32e77ad206/research/c029_holonomy_schur_20261005/manuscript_v3/sections/05_uniform_estimates.tex): pivot contraction, separate endpoint responses, proved positive S∞(c), all-phase equal-cell conclusion
- [Section6](https://github.com/whzy3185/math/blob/8ce218113ed07e3879ddc8bc157c7d32e77ad206/research/c029_holonomy_schur_20261005/manuscript_v3/sections/06_cells.tex): exact additive unequal-cell assembly, loops/parallel contributions, two-incidence quadratic-form estimate and error independent of r

The manuscript-source reading for the principal application covers these TeX sections and the main abstract/bibliography. Narrative validation checks that the words accurately describe these arguments. It is not a fresh replay of all numerical certificates, a whole-paper theorem verification, or a new novelty search.

## Scope invariants retained in all drafts

1. “Unequal” means independently chosen prescribed w_j within one finite cyclic concatenation; not arbitrary disorder
2. The common positive six-dimensional object is a retained-junction core combining neighboring chain responses, at fixed c
3. The common-core positivity is proved in the existing argument, not an extra unverified premise
4. The two-incidence estimate bounds quadratic forms; it is not cancellation of signed errors
5. Positive eliminated pivots remain necessary; Schur congruence does not copy the retained-core Euclidean gap to the original matrix
6. Both holonomies are global ±1 choices; no new arbitrary seam-phase theorem is claimed
7. 106/202 are sufficient thresholds; 7.92/7.90537 are certified caps; no optimality is asserted
8. Recovering the full known witness range also uses the inherited period-eight track; one cell alone only gives the residue-two family
9. Mycielski bounds retain nonempty finite simple bases, ordinary iterations and strict coloring thresholds; census orbits are embedded subsets under the ambient group
10. Domination bounds retain no isolated vertices, uniqueness of a minimum-cardinality dominating set, γ≥2, unrestricted relabellings and the full equality family; matching-order lower bounds retain their parity/deficit ranges

## Source-specific cautions retained

- S1: feasible versus weakly feasible; all extremizers versus an attaining extremizer
- S2: clique versus general forbidden graph; Springer online date differs from HEP display
- S3: matching-based structural proximity; leading-order sharpness differs from additive-order sharpness for two colors
- S4: unbalanced signed K_{3,3} family, not an edge-deleted ordinary graph; index differs from spectral radius
- S5: triangles need not be disjoint; title changed in journal counterpart; future issue date
- S6: 83/41 signed limit differs from finite 2+2/25 arboricity example; preprint abstract is imprecise on the latter
- S7: four-graph equality classification requires connectedness

## Material deliberately not promoted to the deep corpus

Belardo–Brunetti, *Limit points for the spectral radii of signed graphs*, Discrete Mathematics347(2)(2024),113745, [DOI10.1016/j.disc.2023.113745](https://doi.org/10.1016/j.disc.2023.113745), has verified primary publication metadata. Its [institutional PDF](https://iris.unina.it/retrieve/7e3e590f-1ef8-4ae7-9eaa-1a08c2a7489d/Limit%20points%20for%20the%20spectral%20radii%20of%20signed%20graphs.pdf) was not successfully retrieved in this pass. It is discussed only at the level supported by C029's existing source comparison and publisher metadata, not counted as an eighth deep reading.

Kannan–Pragada, *Signed spectral Turán type theorems*, LAA663(2023),62–79, [DOI10.1016/j.laa.2023.01.002](https://doi.org/10.1016/j.laa.2023.01.002), [arXiv2204.09870v3](https://arxiv.org/abs/2204.09870v3), is an existing C029 comparator outside the prioritized three-year first-submission window. The draft's description follows C029's cited Theorem3.3: an index bound using edge count, frustration index and balanced clique number. It is not represented as a new complete reading here.
