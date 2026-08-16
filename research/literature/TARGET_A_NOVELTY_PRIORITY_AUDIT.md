# Target A Novelty and Priority Audit

Audit cutoff: **2026-08-16**  
Evidence-access window: **2026-08-16T05:19:35Z to 2026-08-16T05:49:16Z**  
Baseline: `c5cadf3ec7e160fc994453907fe83c579dc89646`  
Baseline repository: `/Users/muelsyse/Documents/Codex/2026-08-15/cha-k/work/math-slow-c5cadf3` (read-only)

## Conclusion

As of 16 August 2026, no direct public prior was found in the sources and queries recorded in this audit.

This is a bounded search conclusion, not a universal priority claim. It is subject to indexing delay, inaccessible services, non-public communications, unpublished work, and sources outside the recorded queries. The project's own public GitHub branch is recorded separately as a **project-origin public disclosure** and is not counted as independent prior art.

## Classification Rule

Each claim receives exactly one required label:

- `DIRECT_PRIOR_FOUND`: an independent public source predating the project's claim record states substantially the same result.
- `CLOSE_PRIOR_FOUND`: a predating independent source states a material part or a near-equivalent result, but not the complete claim.
- `RELATED_METHOD_ONLY`: predating independent sources disclose a relevant method or general framework, but not the claimed target-specific result.
- `NO_DIRECT_PUBLIC_PRIOR_FOUND`: no direct or materially close independent public result was found in the recorded search.
- `UNRESOLVED`: the search record is too incomplete or ambiguous for one of the preceding assessments.

Commit timestamps establish repository provenance, not authorship adjudication or a publication date. The exact time when the public branch first became anonymously visible could not be recovered; anonymous visibility was directly confirmed at `2026-08-16T05:33:13Z`.

## Claim Matrix

| ID | Claim | Assessment | Confidence | Principal evidence |
|---|---|---|---|---|
| N1 | Conjecture 3 of arXiv:2607.18334 is false. | `NO_DIRECT_PUBLIC_PRIOR_FOUND` | High within searched sources | arXiv v1 still states the conjecture; no author revision, follow-up, or independent disproof was found. |
| N2 | Smallest even counterexample is `n=32`. | `NO_DIRECT_PUBLIC_PRIOR_FOUND` | High within searched sources | Source paper verifies only `n=8,10,12,14,16,18`; author experiments at `n=32` report no counterexample and retain no signing. |
| N3 | Explicit counterexample family for every `n=8L`, `L>=4`. | `NO_DIRECT_PUBLIC_PRIOR_FOUND` | High within searched sources | Exact family/pattern and multiple-of-eight searches returned no independent public source. |
| N4 | Sharp period-8 squared radius `eta=4+sqrt(10+2sqrt(5))`. | `NO_DIRECT_PUBLIC_PRIOR_FOUND` | High within searched sources | Searches for the exact radical, decimal, polynomial, and period-8 context found no independent match. |
| N5 | Target `Q=(+---)^2` is the unique period-8 minimizer. | `NO_DIRECT_PUBLIC_PRIOR_FOUND` | High within searched sources | No public period-8 classification or uniqueness result was found. |
| N6 | `Q=(-)^8` is the unique period-8 runner-up with `R=8`. | `CLOSE_PRIOR_FOUND` | High | arXiv:2607.18334 Proposition 1 gives the all-unbalanced quadrilateral phase spectral radius `2sqrt(2)`, hence squared radius `8`; it does not state the period-8 runner-up or uniqueness classification. |
| N7 | Period-8 eight-barrier trichotomy. | `NO_DIRECT_PUBLIC_PRIOR_FOUND` | High within searched sources | Exact and mechanism-oriented searches found no independent trichotomy. |
| N8 | Closed-walk structural mechanism. | `RELATED_METHOD_ONLY` | High | arXiv:2607.17343 uses short even cycles/trace control in parity families; arXiv:2302.10496 studies signed-graph spectra via parity-closed walks. Neither gives the Target A period-8 mechanism. |
| N9 | Target anti-period-4 chiral mechanism / `4+4` reduction. | `RELATED_METHOD_ONLY` | Medium-high | arXiv:2607.18334 already uses Fourier-invariant traceless `2x2` blocks for its alternating-flux phase, and general Bloch/chiral reductions are established methods; no target anti-period-4 involution or `4+4` result was found. |
| N10 | For arbitrary periodic Hamilton-gauge signings, `M1=4p`, `M2=20p+16d`, and `M3=118p+168d+96a+48b` imply `R(Q)<=8 => d<=3p/4` and `40d+96a+48b<=42p`. | `RELATED_METHOD_ONLY` | High | Signed-graph closed-walk lower bounds, general moment-support inequalities, and periodic-operator Floquet theory predate the claim; no source containing the exact motif identities or necessary inequalities was found. |
| N11 | Among periodic Hamilton-gauge signings with primitive `tau` period at most 16, the Target A period-8 phase is the unique minimizer up to translation, reflection, global `tau` negation, and unit-cell repetition. | `NO_DIRECT_PUBLIC_PRIOR_FOUND` | High within searched sources | Exact theorem-language, period-bound, orbit-count, pattern, radical, periodic-signing, and bounded-period searches found no independent classification or equivalent uniqueness result. |

## Primary Sources

### arXiv:2607.18334

[`Signed circulants at the Ramanujan bound`](https://arxiv.org/abs/2607.18334) has only version 1, submitted `2026-07-19T17:33:48Z`. Its [HTML text](https://arxiv.org/html/2607.18334) states Conjecture 3 for every even `n>=8` and reports exhaustive verification only for `n in {8,10,12,14,16,18}` to `10^-9`. Remark 5 leaves the lower bound open and identifies reflection positivity as a natural route. No correction, counterexample remark, or expanded verified range appeared in the accessed version.

Proposition 1 proves spectral radius `2sqrt(2)` for the relevant all-unbalanced quadrilateral phase. This is close prior for the value component of N6 only; the source does not classify all legal period-8 phases or assert unique second place.

The official source archive SHA-256 was `fe460ca0420552f87a4c0649397f9a52543b3faff3e67b84ee7de7d83bd477ba`.

### arXiv:2607.17343

[`Parity families and a kernel-averaged L-function for near-Ramanujan signings`](https://arxiv.org/abs/2607.17343) has only version 1, submitted `2026-07-19T17:07:14Z`. It supplies general parity-family, kernel-averaging, and trace/cycle methodology, but no `n=32` counterexample, period-8 classification, sharp radical, trichotomy, or target chiral reduction was found.

The official source archive SHA-256 was `80fa7dc4475bb4d8ee23442213f129f568f2c6752fcadfbfa645e94966d8c20c`.

### Author Repository

The public repository [`Vaibhavs25/bilu-linial-parity`](https://github.com/Vaibhavs25/bilu-linial-parity) had eight commits, all dated 19 July 2026. Its latest commit was `312f0e2f0b4cdc588b3c06c4754f1df231d4da6a` at `2026-07-19T17:25:09Z`; no commits after 19 July, issues, pull requests, or alternate branches were found.

A repository-wide text scan of Markdown, TeX, Python, CSV, and shell files found none of the target-specific strings or results. Generic `closed walk` text occurs in the companion methodology. The public `campaign.csv` includes heuristic `C_32(1,2)` rows, but all reported values remain above the conjectured threshold; the closest listed family value is `2.794518`. The campaign code records scalar summaries and not a recoverable counterexample signing. This is negative experimental evidence, not a proof of absence.

The GitHub TeX blobs match the official arXiv source archives byte-for-byte by SHA-256.

## Broader Search

The recorded exact-title, identifier, formula, pattern, polynomial, period, and mechanism queries covered arXiv search/API, Crossref, DataCite, OpenAlex, Semantic Scholar, general web search, GitHub repository/history/content, author pages, and citation/follow-up endpoints. Notable outcomes:

- arXiv API query `all:"C_n(1,2)" AND all:signing` returned only arXiv:2607.18334.
- arXiv API query `all:"period-8" AND all:circulant` returned zero records.
- Crossref exact normalized-title queries returned no matching records for either primary title.
- OpenAlex records for both papers reported `cited_by_count=0`; duplicate arXiv/DOI records were present.
- DataCite reported version 1 for both DOIs and `citationCount=0` in the accessed metadata.
- Semantic Scholar showed each companion paper citing the other and no other citing paper in the accessed citation endpoints. Its aggregate author record reported two papers and zero citations, an internal indexing inconsistency noted in the snapshot.
- Exact pattern/formula searches for `00010001`, `10001000`, `1561/200`, `7.804226065`, `4+sqrt(10+2sqrt(5))`, and the characteristic-polynomial fragments found no relevant independent source.
- arXiv:2302.10496, [`Spectra of power hypergraphs and signed graphs via parity-closed walks`](https://arxiv.org/abs/2302.10496), is methodologically related to N8 but does not address the Target A claims.

### Synchronization-Gate Addendum: N10 and N11

Targeted exact-expression searches for `M_1=4p`, `M_2=20p+16d`, `M_3=118p+168d+96a+48b`, `40d+96a+48b<=42p`, and `d<=3p/4` found no relevant independent match. The arXiv API returned only arXiv:2302.10496 for `closed walk` + `signed graph` + `spectral radius`, and zero records for the queried combinations `periodic signing` + `spectral radius`, `signed circulant` + `periodic`, and `Floquet` + `signed graph` + `moment`.

For N10, Zoran Stanic's [`Walks and eigenvalues of signed graphs`](https://doi.org/10.1515/spma-2023-0104) derives spectral-radius lower bounds from walks or closed walks. Barreras, Hayhoe, Hassani, and Preciado's [`Measure-theoretic bounds on the spectral radius of graphs from walks`](https://doi.org/10.1016/j.laa.2021.04.023) gives general moment-sequence constraints and ratios for measures supported on a graph spectrum. Periodic-graph Floquet frameworks include [`Schrodinger operators on periodic discrete graphs`](https://arxiv.org/abs/1307.1841) and [`Floquet isospectrality for periodic graph operators`](https://arxiv.org/abs/2302.13103). These are method antecedents only: none states the N10 Hamilton-gauge motif formulas or the two displayed necessary inequalities.

For N11, searches covered `primitive tau period`, `period at most 16`, `bounded-period periodic signings`, `2626`, `0001000100010001`, the exact radical with `unique minimizer`, symmetry/repetition language, and GitHub-targeted variants. No relevant independent bounded-period phase classification or uniqueness theorem was found. Hits for the binary word and generic minimizer terminology were unrelated.

Crossref and OpenAlex close-variant queries returned generic signed-graph, circulant, Floquet, or minimization literature but no N10/N11 result. Semantic Scholar returned HTTP 429 for all four addendum queries. Both addendum Google Scholar exact searches timed out with HTTP status `000`; they are recorded as inaccessible, not negative findings.

The complete query-by-query record is in `target_a_search_query_ledger.json`.

## Public Project Disclosure

The repository [`whzy3185/math`](https://github.com/whzy3185/math) is public. Commit [`c5cadf3ec7e160fc994453907fe83c579dc89646`](https://github.com/whzy3185/math/commit/c5cadf3ec7e160fc994453907fe83c579dc89646) contains the baseline claim package. The addendum sources are descendant commits [`637de46394592f918f8e719c88648a46077f1214`](https://github.com/whzy3185/math/commit/637de46394592f918f8e719c88648a46077f1214) for N10 and [`d43046f86d6b9f9ddf9a38b9d63dae0d11a7178d`](https://github.com/whzy3185/math/commit/d43046f86d6b9f9ddf9a38b9d63dae0d11a7178d) for N11. Both proof files returned HTTP 200 through anonymous raw GitHub requests by `2026-08-16T05:45:32Z`. These are project-origin disclosures, not independent sources.

The first local claim-bearing commit was `21d5b848ec6222e9cca8b263dcc9cd397b86b236` at `2026-08-15T17:11:25+08:00`. The baseline structural commit was authored and committed at `2026-08-16T12:59:14+08:00`; N10's commit is timestamped `13:26:10+08:00`, and N11's commit `13:44:48+08:00`. These Git timestamps do not establish when GitHub first exposed the history; the audit establishes only anonymous accessibility by the recorded observation times.

## Limitations

- Google Scholar was inaccessible: command-line exact-title queries timed out, the in-app browser reset/timed out, and the arXiv Scholar link returned HTTP 403. This is recorded as inaccessible, not as a negative search result.
- Semantic Scholar began returning HTTP 429 after the paper/citation records were retrieved, limiting additional query variants.
- GitHub's unauthenticated REST quota was exhausted during part of the audit. Public HTML/raw access, repository history, and previously retrieved API records were used to complete the source snapshot.
- Citation indices can lag very recent July/August 2026 work.
- Search engines do not index every repository branch, preprint mirror, discussion, or personal page.
- No assessment here determines mathematical correctness, legal priority, authorship, or patent status.

## Artifact Map

- `target_a_novelty_priority_audit.json`: machine-readable claim assessments and evidence links.
- `target_a_search_query_ledger.json`: complete query and service-access ledger.
- `target_a_public_source_snapshot.json`: source versions, commits, identifiers, hashes, and observed states.
- `TARGET_A_PROVENANCE_TIMELINE.md`: public-source and project-origin chronology.
