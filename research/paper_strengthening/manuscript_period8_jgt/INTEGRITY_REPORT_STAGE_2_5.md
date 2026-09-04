# Stage 2.5 Integrity Report

> Historical pre-rewrite gate.  The current gate is
> `INTEGRITY_REPORT_AUTHORIAL_REWRITE.md`; the bibliography was reduced from
> 15 to 14 functional citations during the narrative audit.

## Verdict

**PASS.**  The registered populations below are complete for the current
manuscript version.  This verdict covers reference existence/metadata,
citation-context alignment, registered mathematical claims, internal numeric
consistency, bilingual label/scope agreement, and figure/table fidelity.  It
does not certify literature-search exhaustiveness or substitute for peer
review of novelty and significance.

## Registered populations

| population | audited | total | result |
|---|---:|---:|---|
| bibliography entries | 15 | 15 | PASS |
| distinct citation contexts in English | 9 | 9 | PASS |
| corresponding Chinese citation contexts | 9 | 9 | PASS |
| registered principal mathematical claims | 14 | 14 | PASS |
| figures | 3 | 3 | PASS |
| mathematical tables | 2 | 2 | PASS |
| own empirical/statistical claims | 0 | 0 | not applicable |
| English/Chinese theorem and equation labels | 72 | 72 | identical |

## A. Reference existence and metadata audit

Each row records a query used during the live audit, a confirming source, and
the fields checked against `references.bib`.

| key | query | confirming source | fields confirmed | verdict |
|---|---|---|---|---|
| `Harary1953` | `Harary On the notion of balance signed graph DOI` | Project Euclid/Crossref DOI `10.1307/mmj/1028989917` | author, title, journal, vol. 2(2), 143--146, year | VERIFIED |
| `Zaslavsky1982` | `Zaslavsky Signed graphs Discrete Applied Mathematics 4 47 74 DOI` | author publication list and DOI `10.1016/0166-218X(82)90033-6` | author, title, journal, vol. 4(1), pages, year, DOI | VERIFIED |
| `BelardoEtAl2018` | `Open problems spectral theory signed graphs Belardo Cioaba Koolen Wang` | journal DOI `10.26493/2590-9770.1286.d7b` and arXiv `1907.04349` | four authors, title, journal, vol. 1(2), article P2.10 | VERIFIED |
| `BiluLinial2006` | `Bilu Linial lifts discrepancy nearly optimal spectral gap DOI` | Combinatorica/Weizmann record, DOI `10.1007/s00493-006-0029-7` | authors, title, vol. 26(5), 495--519, year, DOI | VERIFIED |
| `MarcusSpielmanSrivastava2015` | `Interlacing families I bipartite Ramanujan graphs Annals DOI` | Annals DOI `10.4007/annals.2015.182.1.7` and arXiv `1304.4132` | authors, title, vol. 182(1), 307--325 | VERIFIED |
| `Reff2012` | `Spectral properties complex unit gain graphs Reff` | ScienceDirect DOI `10.1016/j.laa.2011.10.021` and arXiv `1110.4554` | author, title, LAA 436(9), 3165--3176 | VERIFIED |
| `KorotyaevSaburova2017` | `Magnetic Schrodinger operators periodic discrete graphs JFA` | ScienceDirect DOI `10.1016/j.jfa.2016.12.015` | authors, title, JFA 272(4), 1625--1660 | VERIFIED |
| `KorotyaevSaburova2023` | `Trace formulas magnetic Schrodinger periodic graphs LAA` | ScienceDirect DOI `10.1016/j.laa.2023.07.025` and arXiv `2206.09663` | authors, title, LAA 676, 395--440 | VERIFIED |
| `Davis1979` | `Philip Davis Circulant Matrices Wiley 1979 ISBN` | WorldCat OCLC `4804321` and Google Books | author, title, publisher, place, year, ISBN | VERIFIED |
| `BrunettiStanic2022` | `Unbalanced signed graphs extremal spectral radius index` | Springer DOI `10.1007/s40314-022-01814-5` | authors, title, journal, vol. 41, article 118 | VERIFIED |
| `GhorbaniMajidi2024` | `Complete signed graphs largest maximum smallest minimum eigenvalue` | ScienceDirect DOI `10.1016/j.disc.2023.113860` | authors, title, Discrete Math. 347(4), article 113860 | VERIFIED |
| `HuLiu2025` | `Vertex isoperimetry signed graphs non-bipartite Cayley sum graphs` | ScienceDirect DOI `10.1016/j.ejc.2025.104200`, arXiv `2306.05306`, author CV | authors, published title, EJC 130, article 104200 | VERIFIED |
| `AtayHua2016` | `symmetry Laplacian spectra signed graphs Atay Hua` | ScienceDirect DOI `10.1016/j.laa.2016.01.027` and arXiv `1411.6113` | authors, title, LAA 495, 24--37 | VERIFIED |
| `CedzichEtAl2021` | `Chiral Floquet systems quantum walks half-period DOI` | Hannover research portal DOI `10.1007/s00023-020-00982-6` and arXiv `2006.04634` | four authors, title, AHP 22(2), 375--413 | VERIFIED |
| `Suvagiya2026` | `Signed circulants Ramanujan bound Suvagiya` | arXiv `2607.18334` and locally inspected v1 PDF | author, title, year, preprint status, exact conjecture context | VERIFIED |

Ghost-citation check: every bibliography entry is cited, and every citation key
resolves to one bibliography entry.

## B. Citation-context audit

| context | cited sources | alignment result |
|---|---|---|
| balance, switching, and cycle signs | Harary; Zaslavsky | supported; historical role stated without priority inflation |
| signings and two-lifts | Bilu--Linial; MSS | supported; existence/control problem kept distinct from the fixed-graph minimum |
| signed spectral programme | Belardo et al. | supported; cited as programme/open-problem context |
| exact extrema for restricted signed families | Brunetti--Stanić; Ghorbani--Majidi | supported; no claim that they solve the present graph |
| scalar Fourier spectra of circulants | Davis | supported |
| neighboring signed Cayley context | Hu--Liu | supported; explicitly described as neighboring rather than direct predecessor |
| gain, magnetic, and periodic graph operators | Reff; Korotyaev--Saburova 2017/2023 | supported; gauge/flux/Floquet vocabulary only |
| spectral symmetry and half-period chiral systems | Atay--Hua; Cedzich et al. | supported; manuscript states that the present coefficient criterion is different |
| twisted candidate and conjecture | Suvagiya | supported by the locally inspected Conjecture 3 passage; preprint status explicit |

The Chinese contexts make the same bounded claims.  No citation is asked to
validate a calculation carried out in this paper.

## C. Registered mathematical claim audit

| ID | claim | proof/evidence pointer | verdict |
|---|---|---|---|
| C1 | switching is orthogonal conjugacy and `(tau,alpha)` are the gauge coordinates | Section 2.1; frozen analytic/Lean kernel | ALIGNED |
| C2 | lift, cyclic, reflection, and repetition invariance | Proposition 2.1 and zone folding; `symmetry_invariance_lemmas.md` | ALIGNED |
| C3 | finite direct sum over `z^L=alpha` | Proposition 2.2; finite cell-shift proof | ALIGNED |
| C4 | half-cell monomial anticommutation iff `tau_(i+m)=-tau_i` | Theorem 3.1; explicit anticommutator coefficients | ALIGNED |
| C5 | equivalent half-periodic negative-flux criterion | Theorem 3.2; ratio and telescoping proof | ALIGNED |
| C6 | chiral dimensions and `2m -> m` squared reduction | Section 3.3 | ALIGNED |
| C7 | displayed period-eight fiber and `4 -> 2` determinant identity | Sections 4.1--4.2; frozen Lean identities | ALIGNED |
| C8 | polynomial `P(y,c)` | Eq. (period-eight polynomial); exact symbolic verifier | ALIGNED |
| C9 | four branches, endpoint values, simplicity, and gaps | Section 4.3; full-dispersion verifier | ALIGNED |
| C10 | exact positive and negative finite radii | Section 4.4; exact-edge and dispersion verifiers | ALIGNED |
| C11 | twisted finite formula and strict comparison for `L>=4` | Section 4.5; full shifted-grid proof and exact separator; frozen Lean comparison | ALIGNED |
| C12 | `M1,M2,M3` formulas and necessary inequalities | local square Eq. (39), Sections 5.1/6; general-period moment verifier | ALIGNED |
| C13 | smallest primitive period eight | Section 5.2; nine exact survivors, zone folding, minimal-period verifier | ALIGNED |
| C14 | period-eight trichotomy and unique first orbit | Section 5.3; exact recurrence and structural verifier | ALIGNED |

Quantifier checks passed:

- exact positive-sector equality is `L>=1`;
- twisted strict comparison is only `L>=4`;
- the negative-sector formula is analytic, not called Lean-checked;
- uniqueness is restricted to legal primitive period-eight phases modulo the
  stated symmetries;
- no equality is asserted for the global minimum `m(C_(8L)(1,2))`;
- no all-even or all-period classification is asserted.

## D. Figures, table, and computation

| artifact | source and transformation | caption/claim fidelity | verdict |
|---|---|---|---|
| Figure 1 | Eq. (target words), manually encoded in `figures/period8_flux_cell.tex` | shows the cycle square, two half-cells, and antipodal positive `Q` sites; no spectral claim | PASS |
| Figure 2 | Proposition 2.2, manually encoded in `figures/finite_bloch_cells.tex` | shows cell shift, seam holonomy, and `z^L=alpha`; no proof delegated to the figure | PASS |
| Figure 3 | Theorems 3.1--3.2, manually encoded in `figures/halfcell_chiral.tex` | shows the two operator factors and negative half-cell flux equivalence; caption matches theorem scope | PASS |
| survivor display | exact legal/moment/dihedral reduction from `verify_minimal_period.py` | complete for displayed periods below eight | PASS |
| certificate table | eight stored exact Rayleigh products | all vectors and exact negative values reproduce | PASS |

The period-eight recurrence prints its initial convention, update rule, and the
three decisive integer excesses.  It is not described as numerical evidence or
as an exhaustive search over finite graph signings.

## E. Bilingual and build integrity

- English and Chinese sources contain the same 72 theorem/equation/section labels.
- Both have seven sections and the same theorem order.
- All 15 citation keys occur in each version.
- English abstract: 159 words; six keywords.
- English PDF: 17 pages after the final integrity repair.
- Chinese PDF: 16 pages after the final integrity repair.
- No unresolved citation or cross-reference, placeholder, overfull box, or
  underfull box remains after the final build.

The macOS CTeX build reports platform-font reproducibility warnings.  These do
not affect glyph rendering in the inspected PDF; a journal build should use the
publisher's TeX environment.

## Advisory items outside the PASS denominator

The corresponding author, final author-order confirmation, current
affiliations, funding, acknowledgements, conflicts, and contribution statement
remain author-owned submission facts.  They are isolated in
`AUTHOR_AND_SUBMISSION_QUESTIONS.md` and are not guessed.
