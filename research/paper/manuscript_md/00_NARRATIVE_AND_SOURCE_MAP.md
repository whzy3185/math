# Narrative and Source Map

Status: **MANUSCRIPT_SOURCE_MAP_COMPLETE**

This document is an internal writing map. Engineering identifiers belong here,
not in the article prose.

## Narrative

The article follows one mathematical question through three increasingly
structural answers.

1. The source conjecture predicts that the alternating-flux twisted class
   minimizes spectral radius on every even `C_n(1,2)`.
2. Exact finite verification shows that the prediction is correct through
   `n=30`, but an explicit period-8 pattern gives the first failure at `n=32`.
3. Floquet analysis turns that pattern into an infinite family for every
   multiple of eight at least 32 and yields the sharp squared spectral edge
   `eta=4+sqrt(10+2sqrt(5))`.
4. Squaring the operator exposes defect cancellation. Closed-walk moments then
   prove a complete eight-barrier trichotomy and explain why antipodal defects
   are the unique sub-eight period-8 geometry.
5. The same local calculation gives arbitrary-period moment identities and
   two necessary obstructions.
6. Exact orbit enumeration and a compressed moment/certificate argument show
   that the target is the unique optimum among primitive Hamilton-gauge
   periods at most 16.

The article therefore moves from counterexample to mechanism. The finite
minimality and bounded frontier are explicitly computer-assisted; the Floquet,
sharp-edge, operator-equivalence, cancellation, and moment-implication cores
are presented as human proofs.

## Theorem Map

| Article result | Claims | Primary mathematical sources |
|---|---|---|
| Theorem A: smallest counterexample | C1-C3 | `TARGET_A_SMALLEST_COUNTEREXAMPLE.md`, `TARGET_A_SPEC.md`, n=32 reconstruction audit |
| Theorem B: infinite family | C4-C7 | period-8 family proof, independent Floquet audit, infinite-family audit |
| Theorem C: sharp edge | C5-C7 | `TARGET_A_PERIOD8_SHARP_CONSTANT.md`, Floquet audit |
| Theorem D: period-8 trichotomy | C8-C16 | structural-mechanism proof, period-8 classification |
| Theorem E: general-period obstruction | C11, C13, C17-C21 | general-period moment proof |
| Theorem F: low-period frontier | C7, C13, C22-C25 | low-period frontier, structural compression, operator equivalences |

## Section Sources

| Manuscript section | Proof and audit artifacts | Evidence role |
|---|---|---|
| Introduction | source-paper snapshot, current status check, novelty audit | problem, dated status, contribution boundaries |
| Preliminaries | Target A specification, notation freeze, operator equivalences | definitions, switching, flux coordinates, zone folding |
| Smallest counterexample | smallest-counterexample proof, minimality certificate, n=32 reconstruction | exact witness and complete finite exclusion |
| Periodic/Floquet | period-8 family, Floquet independent audit | block decomposition, determinant, finite holonomies |
| Sharp edge | sharp-constant proof, infinite-family audit | exact radical, positivity, uniqueness, threshold comparison |
| Eight barrier | structural mechanism, period-8 classification | local square, moments, defect geometry, chiral reduction |
| General period | general-period moment obstruction | closed-walk expansion and necessary conditions |
| Low-period frontier | spectral frontier, structural frontier, operator equivalences | 2626-orbit completeness and exact exclusions |
| Computational verification | proof classification, trust model, reproducibility statement | computer-assisted boundary and reproducibility |
| Discussion | architecture, novelty refresh plan | limitations and open problems |
| Appendix A | minimality sources, Burnside counts | quotient/orbit completeness |
| Appendix B | period-8 table, residual certificates | exact finite certificates |
| Appendix C | reproducibility package | execution and evidence model |

## Writing Constraints

- Every theorem used in the article receives either a complete proof in the
  body or a complete proof in an explicitly cited appendix.
- No proof body is replaced by a pointer to code, JSON, a repository path, or
  future author work.
- Computer-assisted theorems state the finite domain, enumeration quotient,
  certificate type, coverage argument, and independently checked conclusion.
- `R(Q)` always denotes squared infinite-volume spectral radius.
- The only moment implication used is `F_k(Q)>0 => R(Q)>8`.
- The low-period radical comparison states `r>4` before squaring.
- No statement asserts all-period, all-signings, or all-finite-order global
  optimality.
- The dated public-status sentence is bounded to the checked sources and never
  becomes an absolute priority claim.
