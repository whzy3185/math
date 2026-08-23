# Target A Task 55 Master Ledger

Reference checkpoint: `bd1934da29a2eb56cf2045554c00c104d79a7959`.
Formal English and Chinese manuscript trees remain frozen.

## Integrated Results

| ID | Statement | Evidence | Independent verification | Boundary |
|---|---|---|---|---|
| T55-A1 | `rank P_(H6,{c6})=2`; `K^2=-I`, `KA=-AK`, `KH=HK` | `COMPUTER_ASSISTED_PROVED` plus analytic coefficient identity | rank-correction checker and tests | corrects, rather than weakens, the single-G6 edge theorem |
| T55-A2 | For `r=1,2,3`, `D>=1040`, exactly `2r` finite-ring levels lie in `[c6-1/400,c6+1/400]` | `COMPUTER_ASSISTED_PROVED` | exact-2r checker, two mathematical audits, 29 tamper tests | multiplicity counted; individual simplicity not asserted |
| T55-A3 | Codimension-`2r` complement satisfies `QHQ<=c6-1/200` and admits a `2r x 2r` Feshbach reduction | `COMPUTER_ASSISTED_PROVED` | same exact-2r certificate/checker | no entrywise leading coefficient theorem |
| T55-A4 | `|lambda_j-c6|<3505 r(9/25)^ell` | `COMPUTER_ASSISTED_PROVED` | exact rational Floquet and constant reconstruction | `ell=floor((floor(D/4)-12)/8)`; constants are sufficient, not optimal |
| T55-A5 | Every even `n>=3120` is covered by the explicit exponential family | `COMPUTER_ASSISTED_PROVED` | endpoint and monotonicity checks in exact-2r checker | `N_exp=3120` is sufficient, not minimal; `N_star=48` is stronger |
| T55-B1 | No counterexample exists at `n=34,36,38,42,44,46` | `COMPUTER_ASSISTED_PROVED` | independent exact window/de Bruijn/terminal checker; 23 tests | complete for these six orders |
| T55-B2 | `n=40` has an explicit counterexample | `COMPUTER_ASSISTED_PROVED` | independent exact rational LDL reconstruction | does not classify all order-40 minimizers |
| T55-B3 | Failure occurs exactly at `n=32`, `n=40`, and every even `n>=48` | `COMPUTER_ASSISTED_PROVED` | exhaustive union of inherited and Task 55 checked intervals | truth-value classification, not optimizer classification |
| T55-C1 | All 31,008 canonical primitive multi-gap cores with support sum in `{2,6,10,14,18}` have an exact Rayleigh witness above `c6` | `COMPUTER_ASSISTED_PROVED` | primary and alternate independent checkers | finite support-sum class only |
| T55-C2 | Any finite core containing consecutive gaps `(3,3)` has `sup sigma(A^2)>=419/53>c6` | `PROVED` with finite exact case check | 32 local dependency cases checked, including both tau lifts | arbitrary total length, but only this motif subclass |
| T55-D1 | Gap-2/gap-6 Evans quotient involution and the order-five exterior-square recurrence | `COMPUTER_ASSISTED_PROVED` | independent symbolic checker and tests | exchanges stable/unstable sheets; no physical spectral ordering |
| T55-D2 | Abstract static simplicity and Feshbach derivative criteria | `PROVED` | direct finite-dimensional algebra | physical finite-ring simplicity remains open |
| T55-E1 | Common-residue `limsup<=c6` and dilute-G6 matching lower bound | `PROVED` | inherited localization and pointed-limit arguments | unrestricted common liminf is not included |

## Exact Finite Read-Only Evidence

| ID | Computation | Evidence | Why it is not promoted |
|---|---|---|---|
| T55-R1 | Reference-relative graph: 105 states/164 edges; four-phase lift: 420/656; no negative `F4/F5` cycle; only reference zero orbit | `EXACT_FINITE_READ_ONLY` | no serialized producer/checker and no spectral bridge |
| T55-R2 | Period 25: 337,594 canonical orbits and 58 survivors; period 26: 649,532 and 95; all survivors have exact Rayleigh witnesses above `c6` | `EXACT_FINITE_READ_ONLY` | no bound certificate or independent reconstruction; integrated frontier remains `p<=24` |

## High-Precision Evidence

Representative transfer/Evans calculations at 80, 120, and 160 digits
resolve finite-ring interface roots below double precision and agree with
reciprocal Floquet structure. They are discovery and cross-check evidence
only. No interaction coefficient, nonvanishing, simplicity, or many-body
statement is promoted from those decimals.

## Falsified Or Retracted

| ID | Claim | Final status | Reason |
|---|---|---|---|
| T55-X1 | one squared G6 mode per interface | `FALSIFIED` | the simple `+/-sqrt(c6)` modes both square to `c6` |
| T55-X2 | exact `r` cluster and codimension-`r` complement | `FALSIFIED_AS_STATED` | correct dimension and codimension are `2r` |
| T55-X3 | problem-specific `r x r` Feshbach model | `FALSIFIED_AS_STATED` | must be `2r x 2r`; old coordinate expression also mixed spaces |
| T55-X4 | geometric reduced-resolvent gluing as an independent exact-count proof | `REJECTED` | nonvanishing projection defect |
| T55-X5 | raw nonnegative `c6`-weighted coboundary and reference-cell spectral deletion | `FALSIFIED` / `REJECTED` | reference cycle sign and non-scalar bulk monodromy |

## Open Problems

1. Prove every finite-core `B0 -> B2` interface has spectral top at least
   `c6`; support sum above 18 without `(3,3)` is not classified.
2. Prove the physical all-single-gap hierarchy; the quotient recurrence alone
   does not select the stable Evans sheet.
3. Extract interval-certified interaction coefficients and prove or refute
   physical finite-ring level simplicity and genuine three-body effects.
4. Convert the reference-relative finite graph into a checked certificate and
   prove a coercive graph-cost-to-spectrum bridge.
5. Extend the certified primitive periodic frontier beyond period 24 by a
   producer/checker pair or a structural tail theorem.
6. Prove the unrestricted nonzero-residue common liminf, closing tight,
   dichotomy, vanishing, and aperiodic blockers.

## Strongest Status

```text
COMPLETE_EVEN_ORDER_TRUTH_VALUE_CLASSIFICATION_PROVED
EXACT_2R_R123_CLUSTER_AND_FESHBACH_PROVED
UNIVERSAL_INTERFACE_AND_COMMON_LIMINF_OPEN
```
