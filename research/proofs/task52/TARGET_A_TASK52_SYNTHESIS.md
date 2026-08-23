# Target A Task 52 Synthesis

## 1. Baseline

entry HEAD: `ac4c69b796c9dc14d1307a092d1e0faa093081f2`

final HEAD: recorded after final verification and push

branch: `agent/target-a-discovery-snapshot`

tests: baseline `373 passed, 3 skipped, 20 subtests`

manuscript freeze: English `59e3a8f...`; Chinese `57ae03f...`; unchanged

## 2. Translation-Sector Charge

bulk sectors: `B_s`, positive Q sites `s mod4`

charge transition law: `sigma(q)=q mod4`; proposed `q/2 mod4` falsified

Z4 interpretation: all charges map to Z4; even charges occupy `{0,2}`

composition law: additive modulo four

status: PROVED

## 3. Plus/Minus-Two Algebra

q=+2 level: unique `p(y)` root in the inherited c6 interval

q=-2 level: unique root in `[8080985802104273,8080985802104274]/10^15`

same degree-ten factor: YES

exact root intervals: stored in `plus_minus_two_algebra.json`

structural transformation: exact equality of the full stable-branch
elimination resultants; no unsquared constant conjugacy claimed

status: `PLUS_MINUS_TWO_COMMON_POLYNOMIAL_PROVED`

## 4. Single-Gap Charge Spectrum

q=-2: COMPUTER_ASSISTED_PROVED above 8

q=-1: COMPUTER_ASSISTED_PROVED above c6

q=+2: G6, COMPUTER_ASSISTED_PROVED and exact algebraic level

q=+4: COMPUTER_ASSISTED_PROVED above c6

q=+6: inherited G10 theorem, above c6

q=+8: COMPUTER_ASSISTED_PROVED above c6 and below 8

large-g behavior: no threat for gaps 13 through 76; limit/monotonicity OPEN

g->g+8 recurrence: exact residue-dependent exterior-square recurrence of
order at most six

status: competitive comparisons proved; general family OPEN

## 5. Primitive Charged Interfaces

definition: canonical finite non-4 gap word with no proper neutral subword

search scope: gaps 1..12 except 4, length <=4, charges -2,+2,+4,+6

best competitor: G6 remains best in +2; `[8]` and `[10]` best in +4,+6

any level <c6: no non-G6 candidate in scope

completeness achieved: NO

elementary-charge verdict: `PLUS_TWO_UNIQUE_ELEMENTARY_EVEN_CHARGE_STRONGLY_SUPPORTED`

## 6. Fixed-r Method Selection

primary formalism: piecewise Evans/exponential dichotomy on `Gr(2,4)`

secondary checker: finite-ring transfer Evans determinant

Jost/scattering: promising equivalent presentation, not selected

Weyl/DtN: local convergence derived; global chart OPEN

Pruefer/Maslov: not implemented

Grassmannian: used basis-free with the primary method

reason for selection: reuses exact 4x4 kernels and scales directly to r=3

## 7. Bulk Propagation

decay rate: stable multipliers at most `9/25` per bulk cell near c6

Green/Weyl estimate: local chart `O((9/25)^L)`; global resolvent OPEN

finite-segment error: exponential dichotomy PROVED with existential constant

holonomy treatment: cut placed outside truncated local modes; exact in
finite-ring transfer checks

status: `BULK_EXPONENTIAL_DICHOTOMY_PROVED_DTN_GLOBAL_CHART_OPEN`

## 8. r=2 Theorem

legal orientations: forward and reflection

holonomies: both

eigenvalue count: at least two near c6 PROVED; exactly two OPEN

cluster interval: `c6 +/- C_2(9/25)^L`

error bound: existential theorem-level constant

full spectral cap: OPEN

strong target achieved: NO

sufficient target achieved: NO

status: `FIXED_R_R23_CLUSTER_PROVED_GLOBAL_CAP_PARTIAL`

## 9. r=3 Theorem

legal orientations: forward and reflection

holonomies: both

eigenvalue count: at least three near c6 PROVED; exactly three OPEN

cluster interval: `c6 +/- C_3(9/25)^L`

error bound: existential theorem-level constant

full spectral cap: OPEN

strong target achieved: NO

sufficient target achieved: NO

status: `FIXED_R_R23_CLUSTER_PROVED_GLOBAL_CAP_PARTIAL`

## 10. r=4 Stress Test

result: all large-separation deterministic rings retain four cluster levels

formalism scalability: supported; exact count not proved

## 11. Effective Interaction

two-slip splitting: inherited 80/120/160-digit Evans resolution

pairwise coefficient: OPEN

three-body remainder: OPEN

holonomy dependence: visible in representative transfer roots

mod16 consequence: OPEN

status: HIGH_PRECISION representative evidence

## 12. Residue-2 Upper Theorem

construction: one legal G6 slip

bound: conditional on the missing r=1 finite-ring global cap

epsilon_2(k): candidate `O((9/25)^L)`

status: CONDITIONAL

## 13. Residue-4 Upper Theorem

construction: two balanced G6 slips

bound: conditional on the missing r=2 global cap

epsilon_4(k): candidate `O((9/25)^L)`

status: CONDITIONAL

## 14. Residue-6 Upper Theorem

construction: three balanced G6 slips

bound: conditional on the missing r=3 global cap

epsilon_6(k): candidate `O((9/25)^L)`

three-G6 vs G10: three-G6 wins in inherited deterministic large rings

status: CONDITIONAL

## 15. Unified Nonzero-Residue Result

limsup r=2: OPEN/CONDITIONAL

limsup r=4: OPEN/CONDITIONAL

limsup r=6: OPEN/CONDITIONAL

status: no LIMSUP theorem claimed; certainly no LIMIT claim

## 16. Eventual All-Even

proved: NO

explicit N: none

proof dependencies: all three nonzero-residue global caps

status: CONDITIONAL OPEN

## 17. c6-Weighted Moment Theory

F_k^(c6): exact local forms for k=1,...,5 over Q(c6)

M4/M5/M6 use: 10/27/76 motif classes

best exact local constraint: 3768 of 4096 support-10 tau windows excluded

status: PROVED forms / EXACT_FINITE exclusions

## 18. c6 Low-Energy Symbolic Grammar

window threshold: rational upper endpoint for c6

survivor language: 164 length-11 Q windows

bulk+slip decomposition: OPEN

automaton: 105 nodes, 164 edges, 48 primitive cycles through period 16

status: `C6_LOW_ENERGY_GRAMMAR_EXACT_FINITE_PARTIAL`, classification WEAK

## 19. Dense-Sparse Rigidity

dense-defect result: OPEN

sparse-defect reduction: blueprint only

local-limit classification: OPEN

truncated G6 lower bound: PROVED with exponential error

future liminf status: OPEN

## 20. p<=24 Audit Relative to c6

period10: band edge strictly above c6 PROVED

other primitive sub-eight phases: 11 non-target numerical comparisons

any R<c6: none in the bounded atlas

status: period10 PROVED; remainder EXPERIMENTAL bounded

## 21. Order-Nine Insurance

Q1/Q2 sector ordering: OPEN

dominant mode: PROMISING inherited

uniform tail: OPEN

exact prefix: inherited through k=32 on y>=7.98

finite Evans/Rouche fallback: not implemented

status: `INSURANCE_ROUTE_PARTIAL`

## 22. c6 Polynomial Root Geometry

all real roots: eight, exactly isolated

physical roots: two proved

q=-2 root: largest real root, about 8.080985802104

other interpreted roots: none

discriminant: exact nonzero negative integer

status: PROVED

## 23. Adversarial Falsification

H1 result: no bounded primitive threat

H2 result: no gap 13..76 threat

H3 result: candidate rule falsified; corrected additive law proved

H4 result: no finite scanned hidden branch

H5 result: no finite scanned extra r=3 branch

H6 result: no inherited mixed-charge winner

H7 result: none through p<=24; only period10 exact

H8 result: not excluded; 48 grammar cycles survive

H9 result: OPEN

H10 result: exact finite prefix only; uniform OPEN

## 24. Completeness Audit

Can we say:

"q=+2 unique elementary charge PROVED"? NO

reason: bounded primitive search does not meet completeness option A or B

Can we say:

"fixed-r r=1,2,3 theorem PROVED"? NO for exact count/global cap; YES only
for at-least-r cluster existence

Can we say:

"common nonzero residue limit = c6"? NO

If NO: no limsup/upper theorem is proved either; only conditional families
and cluster existence are stated.

Can we say:

"eventual all-even"? NO

## 25. Evidence Inventory

PROVED: translation charge; exact resultant equality; gap-plus-eight
recurrence; bulk dichotomy; fixed-r cluster existence; c6 weighted forms;
truncated G6 lower bound; period10 above c6; root geometry

COMPUTER_ASSISTED_PROVED: gap2 and competitive single-gap Evans intervals;
inherited G6/G10 theorems

EXACT_FINITE: c6 grammar windows/cycles; order-nine prefix

HIGH_PRECISION: representative r=2/r=3 finite-ring Evans roots

EXPERIMENTAL: primitive and large-gap searches; 40 full-spectrum fixed-r
rings; non-period10 p<=24 comparisons

FALSIFIED: `sigma=q/2 mod4`; bare `M8 D_g` recurrence in the fixed cut

OPEN: primitive completeness; exact fixed-r count/global cap; residue
limsup; eventual all-even; dense/sparse liminf; order-nine uniform tail

## 26. Strongest New Theorems

1. Plus/minus-two common exact polynomial: highest novelty and algebraic value.
2. Corrected translation-sector charge: highest generality and low computer dependence.
3. Fixed-r cluster-existence theorem: broad mechanism, but one-sided.
4. Exact gap-plus-eight exterior recurrence: general structural reduction.
5. Truncated G6 lower bound and c6 weighted forms: future liminf infrastructure.

## 27. Current Candidate Phase Diagram

m_(8k)^2: inherited period-eight upper mechanism; global minimum status as before

status: inherited

m_(8k+2)^2: OPEN (candidate c6; no proved limsup)

m_(8k+4)^2: OPEN (candidate c6; no proved limsup)

m_(8k+6)^2: OPEN (candidate c6 via three G6; no proved limsup)

## 28. Reviewer Verdicts

spectral: cluster proof accepted; global counting blocker

Floquet/Evans: local exact work accepted; uniform finite ring open

algebra: common resultant/root selection accepted

combinatorics: corrected Z4 law accepted; uniqueness incomplete

computer-assisted: evidence labels and kernels accepted

hostile editor: no manuscript integration before fixed-r cap

## 29. Recommended Next Task

`TARGET_A_TASK53_FIXED_R_COMPLETION`

## 30. Verification

full tests: pending final run

Task52: pending final run

Task51: baseline PASS

Task50: baseline PASS

Task49: baseline PASS

Task48A: baseline PASS

Task47: baseline PASS

minimality: baseline PASS

computational evidence: baseline PASS

submission artifact: baseline PASS

manuscript freeze: PASS

## 31. Git

commits: pending final logical commits

remote HEAD: pending push

ahead/behind: target `0/0`

working tree: target clean

PR: NO

Final status: `TARGET_A_TASK52_PARTIAL_PROGRESS`.
