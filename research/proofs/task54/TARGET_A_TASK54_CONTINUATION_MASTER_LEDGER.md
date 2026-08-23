# Target A Task 54 Continuation Master Ledger

> **Historical ledger.** Task 55 supersedes every `OPEN_PENDING_2R_REPAIR`
> entry below with an independently checked exact-`2r` theorem, the explicit
> bound `3505r(9/25)^ell`, and `N_exp=3120`. The falsified exact-`r` rows
> remain falsified. See `../task55/TARGET_A_TASK55_MASTER_LEDGER.md` for the
> current project state.

The reference anchor is `07a922ea9fc084f08dc48299dd4535c5a32bbf15`.
`pending integration commit` means the result is in the preserved central WIP
and will receive the final Task 54 continuation commit SHA.

| ID | Statement and scope | Lane | Evidence | Verification | Dependencies | Integrated | Paper value / caveat |
|---|---|---|---|---|---|---|---|
| T54-I1 | `c6` is the only physical G6 level value in `(eta,c6]`; rank two, `delta6=1/100`, both orientations | H / Task55 repair | COMPUTER_ASSISTED_PROVED | positive Evans chart plus exact `K^2=-I`, `KA=-AK` checker | Task 50 physical root and Task55 symmetry | yes | APPENDIX; squared multiplicity is two |
| T54-I2 | Reduced G6 resolvent constants `150,1200`, bulk constant `12`, decay `exp(-d/40000)` after removing full rank-two pole | H | COMPUTER_ASSISTED_PROVED | isolation and analytic spectral theorem | T54-I1 | yes | APPENDIX; conservative constants |
| T54-X1 | For separated legal `r=1,2,3` G6 rings, codimension-`r` complement is below `c6-1/200` | H / A | FALSIFIED_AS_STATED | second local mode remains in complement | T54-I1 | withdrawn | requires codimension `2r` |
| T54-X2 | Exactly `r` squared eigenvalues occur in the fixed near-`c6` window | A | FALSIFIED_AS_STATED | positive/negative `A` partners square to same level | T54-X1 | withdrawn | corrected exact-`2r` theorem subsequently proved in Task 55 |
| T54-X3 | Problem-specific `r x r` Feshbach cluster theorem | J | OPEN | abstract Schur identity survives; complement and dimension do not | corrected T54-X1/X2 | withdrawn | must use `2r x 2r` |
| T54-X4 | Geometric reduced-resolvent parametrix independently proves exact-`r` | H | FALSIFIED | nonvanishing `-chi P chi` defect | none | yes, as withdrawn route | DISCUSSION only |
| T54-A1 | `rho(A_ring)^2<=c6+C_r(9/25)^ell` for fixed `r=1,2,3` and sufficient separation | A | OPEN_PENDING_2R_REPAIR | old proof used invalid exact-`r` ownership | corrected T54-X1, T54-X2 | withdrawn pending repair | expected to survive with two modes per interface |
| T54-A2 | Numerical `C_1,C_2,C_3` and explicit `N_exp` | A | OPEN | normalized tail prefactors absent | T54-A1 | yes, as open status | FUTURE WORK; no fitted constants accepted |
| T54-B1 | Exact global tent IMS error `(240R-342)/(R(2R^2+1))<=120/R^2` | B | PROVED | independent symbolic/rational recomputation and focused tests PASS | Task 53 local patch theorem | yes | ESSENTIAL |
| T54-B2 | Every even `n>=240` has an explicit counterexample (`N_IMS=240`) | B | COMPUTER_ASSISTED_PROVED | endpoint checks and algebraic monotonicity PASS | T54-B1, certified G6 edge, residue separations | yes | ESSENTIAL |
| T54-C1 | Every even `48<=n<240` has a structured full-spectrum certificate | C | COMPUTER_ASSISTED_PROVED | independent natural-order exact LDL, reconstruction, hashes, tamper tests PASS | signing reconstruction | yes | ESSENTIAL/APPENDIX certificate |
| T54-C2 | Every even `n>=48` has an explicit certified counterexample (`N_star=48`) | B/C | COMPUTER_ASSISTED_PROVED | finite bridge plus analytic tail PASS | T54-B2, T54-C1 | yes | strongest new threshold; not globally sharp |
| T54-L1 | Pointed local compactness and `||H_inf||<=liminf rho(A_j)^2` | L | PROVED | independent finite-support derivation | finite alphabet, range four | yes | OPTIONAL MAIN TEXT |
| T54-L2 | Charge measure has tight/dichotomy/normalized-vanishing trichotomy | L | PROVED | combinatorial proof audit | gap charge and bad-window indicator | yes | FUTURE PAPER infrastructure |
| T54-K1 | Common-residue liminf for explicit dilute G6 families | K/L | PROVED | transferred truncated G6 mode | T54-L1, G6 edge | yes | DISCUSSION |
| T54-K2 | Unrestricted `liminf m_(8k+r)^2>=c6`, `r=2,4,6` | K | OPEN | tight, dichotomy, vanishing, and aperiodic blockers remain | D, E, F, L | yes, as open status | FUTURE PAPER |
| T54-D1 | Universal multi-gap `B0->B2` interface lower bound by `c6` | D | OPEN | bounded/structural exploration only | interface Weyl/DtN theory | pending lane synthesis | FUTURE PAPER |
| T54-E1 | Reference-relative excursion cost with exact insertion invariance and nonnegative composition | E | OPEN | raw edgewise coboundary remains FALSIFIED | symbolic grammar, relative Weyl data | pending lane synthesis | FUTURE PAPER |
| T54-F1 | Uniform single-gap `g->g+8` hierarchy | F | OPEN | recurrence mechanism incomplete | Task 51 exterior-square recurrence | pending lane synthesis | FUTURE PAPER |
| T54-G1 | Complete primitive periodic frontier beyond `p=24` | G | OPEN | complexity forecast/exploration only until complete closure | Task 53 orbit machinery | pending lane synthesis | APPENDIX or sequel |
| T54-J1 | Explicit universal interaction coefficients and global simplicity | J | OPEN | only invariant norm formulas are proved | T54-X3 | pending lane synthesis | OPTIONAL/FUTURE PAPER |

## Evidence inventory

- `PROVED`: analytic localization/min-max and Schur-complement implications,
  the exact IMS formula, limit-operator direction, charge trichotomy, and the
  restricted dilute-G6 transfer implication.
- `COMPUTER_ASSISTED_PROVED`: complete G6 isolation with rank-two correction,
  global IMS cap, finite bridge, and `N_star=48`.
- `EXACT_FINITE`: 96 structured finite-order rows and their rational LDL
  sandwiches.
- `HIGH_PRECISION`: no high-precision-only claim is integrated as a theorem.
- `EXPERIMENTAL`: bounded D/E/F/G/J continuation findings, where recorded.
- `FALSIFIED`: exact-`r` and codimension-`r` complement claims; the
  nonprojective geometric reduced-resolvent gluing argument; the old raw
  edgewise nonnegative coboundary route.
- `OPEN`: numerical exponential constants, explicit `N_exp`, universal
  interface/excursion/single-gap theorems, extended complete periodic
  frontier, explicit splitting coefficients, and unrestricted common liminf.
