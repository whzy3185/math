# Target A Final English-Language Re-review

Date: 2026-08-21

Repository HEAD reviewed: `d4df8dfdd00493d8051577e4d42ce04cf55bb6df`

Role: final independent English-language and publication-style referee

Recommendation: **FINAL PASS**

Severity counts: **BLOCKER 0 / MAJOR 0 / MODERATE 0 / MINOR 0**

## Re-review Scope

This short re-review checks the disposition of all six MODERATE and seven MINOR
findings in the preceding language report. I inspected the revised English
sources under `research/paper/manuscript_tex_pub`, the four updated build
records, and the publication LaTeX gate. I did not modify the manuscript or
code and did not rerun the expensive `n=30` computation.

## Disposition of Moderate Findings

| Previous finding | Final status | Verification |
|:---|:---|:---|
| Low-period theorem grammar | **RESOLVED** | `sections/02_introduction.tex:179-184` now states a declarative optimization theorem: among the specified infinite operators, the target uniquely minimizes \(R\) under the stated equivalences. The primitive-period domain and theorem meaning are unchanged. |
| Dynamic-programming superscript | **RESOLVED** | `sections/08_general_period.tex:57` now uses \(W_{2k}^{(r)}(r)\), consistently with the recurrence. |
| Malformed orbit summation | **RESOLVED** | `appendices/12_appendix_orbit_completeness.tex:30` now uses the valid command `\sum_{\mathrm{orbits}}`. |
| Ambiguous order ranges | **RESOLVED** | `sections/10_computational_verification.tex:46-47` now lists \(8,10,\ldots,20\) and \(22,24,\ldots,30\), making the even-order domain explicit. |
| Empty Acknowledgments placeholder | **RESOLVED** | The empty Acknowledgments heading and `[ACKNOWLEDGMENTS]` placeholder have been removed from `sections/12_data_code_availability.tex`. The declared author, affiliation, funding, and DOI metadata placeholders remain outside this finding. |
| Bibliography year | **RESOLVED** | `references.bib:12-20` now records the Belardo--Cioabă--Koolen--Wang journal article as 2018. |

## Disposition of Minor Findings

| Previous finding | Final status | Verification |
|:---|:---|:---|
| Adjacency-sign indices | **RESOLVED** | `sections/03_preliminaries.tex:19-21` consistently uses `\sigma_{ij}`. |
| Polynomial placeholder notation | **RESOLVED** | `sections/06_period8_spectral_edge.tex:145` now uses \(P(\,\cdot\,,c_2)\). |
| Exponential operator | **RESOLVED** | `sections/06_period8_spectral_edge.tex:158` now uses `\exp`. |
| Squared-operator wording | **RESOLVED** | `sections/07_eight_barrier.tex:10-12` now says to compose \(A_\tau\) with itself and collect the two-step transitions. |
| Undefined “nearest competitor” claim | **RESOLVED** | `sections/09_low_period_frontier.tex:137-139` now states only the exact theorem comparison and expressly disclaims a numerical ordering claim. |
| “Closes that separation” wording | **RESOLVED** | `sections/10_computational_verification.tex:102-104` now identifies the gap between coverage verification and independent spectral-decision verification precisely. |
| Doubled sentence spaces | **RESOLVED** | The identified doubled spaces in the Introduction and Data and Code Availability section have been normalized; the old patterns no longer occur. |

## Build and Source Verification

The updated build audit has status `TARGET_A_PUBLICATION_BUILDS_PASS`.

| Variant | Pages | Overfull boxes | Undefined citations | Undefined references | Fatal errors |
|:---|---:|---:|---:|---:|---:|
| Generic | 35 | 0 | 0 | 0 | 0 |
| Anonymous | 35 | 0 | 0 | 0 | 0 |
| JGT wrapper | 35 | 0 | 0 | 0 | 0 |
| SIDMA wrapper | 37 | 0 | 0 | 0 | 0 |

The publication verifier passed all six gates:

- source structure;
- theorem/proof structure;
- reference and citation integrity;
- table and list structure;
- build-artifact integrity;
- final publication LaTeX gate.

A targeted residue scan found none of the former malformed commands, ambiguous
ranges, notation errors, wording fragments, doubled sentence spaces, or the
Acknowledgments placeholder.

## Theorem and Proof Integrity

The editorial corrections do not alter any mathematical statement, proof
dependency, equivalence relation, finite/infinite spectral domain, or
computer-assisted proof boundary. The low-period theorem remains restricted to
primitive Hamilton-gauge period at most 16; the periods 17--24 calculation
remains explicitly non-theorem evidence. No proof body is deferred to the
author, and no new placeholder or malformed prose was introduced by these
repairs.

## Final Verdict

All six former MODERATE findings and all seven former MINOR findings are closed.
The English manuscript is mathematically complete, internally consistent, and
publication-professional, subject only to the already declared submission
metadata boundary.

Final assessment: **BLOCKER 0 / MAJOR 0 / MODERATE 0 / MINOR 0**.

From the English-language and publication-style perspective, Target A is ready
for final submission preparation.
