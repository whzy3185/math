# Analytic Proof First Program

The classification remains a target to be reproved. Existing certificates are backup evidence, not a constraint on the final proof method.

| Target theorem | Current proof | Computational component | Desired analytic replacement | Candidate method | Status |
|---|---|---|---|---|---|
| T1 switching/gauge | diagonal conjugacy and cycle coordinates | none | retain | direct linear algebra | ANALYTIC_PROVED |
| T2 twisted spectrum | Fourier two-plane reduction | none | retain | circulant/Fourier proof | ANALYTIC_PROVED |
| T3 period-eight bulk | symbolic fiber polynomial and positivity | CAS-generated polynomial audit | derive factorization and endpoint argument directly | Floquet plus polynomial positivity | ANALYTIC_WITH_FINITE_BASE_CASES |
| T4 phase-slip charge | endpoint-sector argument | none | retain | word/sector arithmetic | ANALYTIC_PROVED |
| T5 G6 spectral theorem | transfer/Evans/resultant/Sturm atlas | exact algebraic root and chart exclusions | one scalar Evans or Weyl equation | block-Jacobi / Birman--Schwinger | ANALYTIC_OPEN |
| T6 G6 localization | stable/unstable matching | exact multiplier enclosures | retain analytic reduction, isolate minimal algebra | transfer hyperbolicity | ANALYTIC_WITH_FINITE_BASE_CASES |
| T7 large-order failure | G6 cap plus IMS, `n>=240` | exact threshold arithmetic | lower threshold uniformly | transfer-power or optimized finite-dimensional trial space | ANALYTIC_OPEN |
| T8 equality `8..30` | exhaustive switching/orbit certificates | millions of representatives | small structural case theorem or small finite base set | moments, local obstruction, minimizer rigidity | ANALYTIC_OPEN |
| T9 equality `34,36,38,42,44,46` | exact local windows plus de Bruijn closure | 92--171 states and terminal records | forbidden-pattern rigidity | local obstruction plus symbolic dynamics | ANALYTIC_OPEN |
| T10 failures 32/40 | explicit exact LDL witnesses | rational LDL | period-eight reference family | finite Floquet and elementary cosine comparison | ANALYTIC_PROVED |
| T11 failures `48<=n<240` | 96 full-matrix LDL rows | one row per structured witness | periodic Floquet families plus three fixed-energy residue-cap theorems | periods 8,10,12,14,18,22 cover 55 rows; residue-specific IMS covers 16 more; block Riccati/Schur invariance targets the remaining 25 | ANALYTIC_OPEN with exact uniform-cap evidence |
| T12 complete classification | assembly of closed modules | finite certificates in several modules | derive from improved modules | disjoint order partition | ANALYTIC_WITH_FINITE_BASE_CASES |

## Priority rules

1. An exact finite check may discover a statement but never upgrades it to `ANALYTIC_PROVED`.
2. Any proposed uniform result must state its range, boundary conditions, and equality cases before it is used downstream.
3. The old enumeration, finite-state closure, and LDL bridge remain intact as fail-closed provenance until a replacement theorem is independently audited.
4. Lean formalization begins only after a human proof statement and its dependencies are frozen.
