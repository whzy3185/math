# Seed Literature Audit

Audit date: 2026-08-31. This is a relevance audit for the fixed-family,
two-sided signed spectral-radius minimization paper. It is not a ranking of
the cited papers' intrinsic quality.

Scores use high, medium, and low; the rank is an editorial decision for the
present manuscript.

| Paper | Year | Venue | Published? | Direct relevance | Structural relevance | Citation-chain role | Proposed use | Rank | Keep? |
|---|---:|---|---|---|---|---|---|---|---|
| Bilu--Linial, *Lifts, discrepancy and nearly optimal spectral gap* | 2006 | Combinatorica | Yes | Medium | Medium | Historical origin of signing/2-lift program | One sentence in broad motivation | Historical | Yes |
| Marcus--Spielman--Srivastava, *Interlacing Families I* | 2015 | Annals | Yes | Medium | Medium | Explains bipartite one-sided-to-two-sided contrast | Same motivation paragraph as Bilu--Linial | Historical | Yes |
| Suvagiya, *Signed circulants at the Ramanujan bound* | 2026 | arXiv | Preprint | Very high | Very high | Direct conjecture, coordinates, candidate | Introduce only after independent problem positioning | S-preprint | Yes, separately marked |
| Brunetti--Stanic, *Unbalanced signed graphs with extremal spectral radius or index* | 2022 | Comput. Appl. Math. | Yes | High | Medium | Published signed spectral-radius extremal classification | Related Work main body | S | Yes |
| Ghorbani--Majidi, *Complete signed graphs with largest maximum or smallest minimum eigenvalue* | 2024 | Discrete Math. | Yes | Medium | Medium | Fixed underlying graph-family extremal signed adjacency analogue | Related Work main body | A | Yes |
| Hu--Liu, *Vertex isoperimetry... non-bipartite Cayley...* | 2025 | European J. Combin. | Yes | Low | High | Modern signed/non-bipartite Cayley context | Context paragraph only | A | Yes |
| Belardo--Brunetti, *Limit points for the spectral radii of signed graphs* | 2024 | Discrete Math. | Yes | Medium | Medium | Published spectral-radius program for signed graphs | Related Work or Discussion | A | Yes |
| Brunetti--Trevisan, *Limit points for the spectral radii of unbalanced signed graphs* | 2026 | Discrete Math. | Yes | Medium | Medium | Recent unbalanced signed-graph spectral-radius continuation | Related Work update; no theorem overlap | A | Yes |
| Conde--Dratman--Grippo, *On the spectral radius of unbalanced signed bipartite graphs* | 2026 | Discrete Math. | Yes | Medium | Low | Restriction to a graph class, but maximization and bipartite setting | Optional note only | B | No |
| Kannan--Pragada, *Signed spectral Turan type theorems* | 2023 | LAA | Yes | Low | Low | Signed-walk / largest-index inequalities | Do not use for present minimization narrative | Reject | No |
| Wang--Hou--Li, *Extremal results for C_3^--free signed graphs* | 2024 | LAA | Verification incomplete | Low | Low | Forbidden-subgraph maximum-index line | Do not add without a direct need | Reject | No |
| Wang, *Spectral Turan problem for K_5^--free signed graphs* | 2024 | LAA / preprint trail | Publication status not confirmed here | Low | Low | Forbidden-subgraph maximum-index line | Do not add | Reject | No |
| Korotyaev--Saburova, *Trace formulas... periodic graphs* | 2023 | LAA | Yes | Low | Very high | Flux/Floquet periodic-operator method | Section 2/4 method background | S | Yes |

## Screening Decision

The core library contains 13 records: 3 published S-tier records, one
S-tier preprint kept only as the direct problem source, 7 A-tier records, and
2 historical records. The three Turan/forbidden-subgraph seeds and the
unbalanced-bipartite maximization paper are not carried into the core library:
they optimize a different quantity or use a graph-class restriction too far
from fixed C_n(1,2) signing minimization.

## Novelty Check

No audited published source studies the same optimization problem:

~~~
min over all edge signings of rho(A_sigma) on the fixed family C_n(1,2).
~~~

No published source found in this audit states the twisted candidate, the
exceptions 32,40, the onset 48, the period-eight reference edge, or the
G6 phase-slip mechanism. The direct source for the specific conjecture is
Suvagiya's 2026 preprint, which is retained as a preprint rather than treated
as a peer-reviewed main precedent.
