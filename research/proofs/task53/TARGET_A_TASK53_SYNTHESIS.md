# Target A Task 53 Synthesis


## 1. Baseline

entry HEAD: `9b9c6c10c4b682ee39efbf6ec0b6a3bf0d8d1bdf`

entry remote equality: YES, ahead/behind `0/0`

baseline tests: Task 52 verifier PASS; final full suite `509 passed, 3 skipped, 20 subtests passed`

formal manuscript hashes: English `59e3a8f73a152ef06f994e979b7219a3365efeae`; Chinese `57ae03fb5b90866f84d0d72b414008678e8f5004`


## 2. Bulk Global Hyperbolicity

eta: `4+sqrt(10+2sqrt(5))`

proved energy domain: `[c6_upper,16]`

unit-circle exclusion: complete

stable dimension: 2

unstable dimension: 2

critical energies: `4+sqrt(627)/6`, repeated `w=95/12`

status: `GATE_A1_PASS` / PROVED


## 3. G6 Global Grassmannian Atlas

number of charts: 3

coverage: full closed interval, with two nonempty overlaps

uncovered points: none

orientation: forward and reflected G6

translated sectors: `B_0 -> B_2`; simultaneous translations unitary

status: `GATE_A2_PASS` / COMPUTER_ASSISTED_PROVED


## 4. G6 Physical Root Selection

c6: unique degree-ten root in `[7905369311620327,7905369311620328]/10^15`

physical matching condition: `(Lambda^2 D_6 U_L) wedge S_R=0`, unsquared

gap2 root exclusion: nonzero G6 Evans determinant near `8.080985802104273`

resultant boundary: candidate completeness only; two candidates classified

status: PROVED


## 5. Single-G6 Global Edge

strong theorem: `sigma(H6) intersect (c6,16]=empty`

sup sigma(H6)=c6:
YES

sub-eight theorem: yes

proved beta: `c6`

proof type: exact resultant/Sturm plus two independent unsquared interval charts

status: `GATE_A3_PASS_G6_GLOBAL_EDGE_PROVED`


## 6. Discrete IMS

exact identity: `H=sum chi H chi +(1/2)sum[chi,[chi,H]]`

range: 4

C_IMS: 576

error scaling: `576/R^2`

status: `GATE_B1_PASS` / PROVED


## 7. Fixed-r Patch Classification

r=1: bulk / forward G6 / reflected G6 complete

r=2: same

r=3: same

holonomies: `alpha=+1,-1`

orientations: both, via reflection and diagonal gauge

status: `GATE_B2_PASS` / PROVED


## 8. Fixed-r Global Cap

r=1 bound: `rho^2<=c6+576/R^2`

r=2 bound: same

r=3 bound: same

asymptotic error: at most `36864/D^2` for `D>=26`

status: `GATE_B3_PASS` / PROVED


## 9. Residue 2

construction: `[6,4^(2k-1)]`

legal charge: one `+2` slip; `2k` defects

bound: `c6+o(1)`

limsup: at most `c6`

status: PROVED


## 10. Residue 4

construction: `[6,4^(k-1),6,4^(k-1)]`

legal charge: two `+2` slips; `2k` defects

bound: `c6+o(1)`

limsup: at most `c6`

status: PROVED


## 11. Residue 6

construction: three gap-six slips with balanced exponents summing to `2k-3`

legal charge: three `+2` slips; `2k` defects

bound: `c6+o(1)`

limsup: at most `c6`

status: PROVED


## 12. Eventual All-Even

proved:
YES

explicit rigorous N: 2500

observed experimental onset: retained in inherited experiments, not used

dependencies: A3, IMS, patch classification, fixed-r cap, residue constructions

status: `EVENTUAL_ALL_EVEN_PROVED`


## 13. Charge Fractionalization

+4 composite level: `c_(+4)>c6`

two-G6 asymptotic level: limsup at most `c6`

+6 composite level: `c_(+6)=c10>c6`

three-G6 asymptotic level: limsup at most `c6`

proved comparison: strict for sufficiently large separation

status: PROVED construction comparison


## 14. Exact-r Localized Excitations

r=1 exact count: inherited single-interface level only

r=2 exact count: OPEN; at least two proved

r=3 exact count: OPEN; at least three proved

Riesz/Feshbach: complementary resolvent open

status: `D1_EXACT_R_OPEN`


## 15. Interaction Theory

two-slip leading term: HIGH_PRECISION only

three-body remainder: OPEN

holonomy: retained in numerical transfer evidence

status: `D2_NOT_TRIGGERED_BY_D1`


## 16. Plus/Minus-Two Structural Duality

common polynomial: exact common resultant

unsquared relation: not found

structural explanation: equality after stable-branch elimination only

status: `PLUS_MINUS_TWO_ELIMINATION_EQUALITY_ONLY`


## 17. p<=24 c6 Frontier

completeness: all legal dihedral orbits through period 24 bound to exact closure data

number of residual certificates: 16 new/strengthened witnesses

any non-target below c6: no

status: `P24_C6_FRONTIER_PROVED`


## 18. Single-Gap Hierarchy

recurrence: exact `g -> g+8` exterior-square recurrence inherited

tail theorem: none

best global conclusion: no mechanism beyond certified finite comparisons

status: `RECURRENCE_ROUTE_WEAK`


## 19. c6 Low-Energy Pilot

LP/coboundary certificate: infeasible under the stated sign convention

exact reconstruction: reference-cycle negative-sum obstruction

zero cycles: not applicable

obstruction: period-eight cycle has every `F_k^(c6)<0`

status: `CURRENT_LOCAL_GRAMMAR_INSUFFICIENT`


## 20. Strongest New Theorems

Rank by:

novelty: eventual all-even theorem; global G6 edge; fixed-r cap; p<=24 c6 frontier

generality: eventual all-even; fixed-r cap; single-interface edge; bounded frontier

rigor: IMS/residue chain; exact bulk geometry; interval Evans; finite frontier

journal value: eventual all-even plus charge fractionalization form the main upgrade

computer dependence: IMS/residue proofs are analytic; G6 edge and p<=24 frontier are computer-assisted


## 21. Updated Candidate Phase Diagram

m_(8k)^2: period-eight exact family gives a PROVED UPPER approaching `eta`

proved status: no exact minimum limit asserted

m_(8k+2)^2: PROVED LIMSUP `<=c6`

PROVED UPPER / PROVED LIMSUP / PROVED LIMIT / OPEN

m_(8k+4)^2: PROVED LIMSUP `<=c6`

same.

m_(8k+6)^2: PROVED LIMSUP `<=c6`

same.


## 22. What Is Still Open

primitive-interface completeness: OPEN beyond the proved G6 and bounded searches

periodic non-target threshold: OPEN beyond period 24

finite-signing liminf: OPEN

common residue limit: OPEN

exact finite m_n: OPEN in general

other: exactly-r Riesz count, interaction coefficients, unsquared plus/minus duality


## 23. Evidence Inventory

PROVED: A1, IMS, patch classification, fixed-r cap, residue limsups, eventual all-even, fractionalization

COMPUTER_ASSISTED_PROVED: A2, A3, p<=24 c6 frontier

EXACT_FINITE: closure counts, Sturm factors, Gaussian witness arithmetic, automaton counts

HIGH_PRECISION: inherited representative multi-slip splitting ladders only

EXPERIMENTAL: observed smaller onset and interaction fits

FALSIFIED: stated-sign nonnegative c6 coboundary on the full reference-containing automaton

OPEN: D1/D2, all-period hierarchy, common residue limit


## 24. Reviewer Verdicts

spectral: accept core; do not conflate cap with exact-r count

Floquet/Evans: accept with full three-chart atlas and unsquared selection

algebra: accept A chain; structural duality remains elimination-only

combinatorics: accept legal residue constructions and scope

computer-assisted: accept with certificates, tamper tests, and frozen hashes

hostile editor: major mathematical reframe justified

narrative/scope: main chain in text; S1/S3/S4 and D1/D2 outside or discussion


## 25. Manuscript Readiness

Does Task53 justify a major manuscript reframe?
YES

Minimum theorem package available: global G6 edge + IMS + fixed-r cap + residue limsups + eventual all-even

recommended main-text additions: the minimum package and fractionalization corollary

recommended appendix additions: atlas, candidate classification, IMS constants, patch maps, p<=24 audit

results to keep discussion-only: elimination equality, recurrence weakness, grammar obstruction, D1/D2


## 26. Recommended Next Stage

Choose exactly one primary recommendation:

`TARGET_A_TASK54_MANUSCRIPT_INTEGRATION`


## 27. Verification

full tests: `509 passed, 3 skipped, 20 subtests passed`

Task53 tests: 72 passed

Task52: PASS

Task51: PASS

Task50: PASS

Task49: PASS

Task48A: PASS

Task47: PASS

minimality: PASS

computational evidence: PASS

submission artifact: PASS

manuscript hashes: PASS, both frozen tree hashes unchanged


## 28. Git

commits: PENDING FINALIZATION

local HEAD: PENDING FINALIZATION

remote HEAD: PENDING FINALIZATION

ahead/behind: PENDING FINALIZATION

working tree: PENDING FINALIZATION

PR: NO
