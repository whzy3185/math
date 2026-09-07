# Current theorem / evidence index

Current status date: 2026-09-07
Branch: `research/quadratic-gap-upgrade`

The current synthesis is `FINAL_THEOREM_PACKAGE_20260907.md`; the newer
one-defect resonance entries below extend the finite-order program beyond that
package without changing its proved statements.

## Evidence labels

- **Analytic theorem** — readable mathematical proof present; not yet independently refereed.
- **Exact finite computer-assisted theorem** — finite exhaustive/pruned step whose acceptance is decided by integer/rational identities; floating arithmetic may only propose witnesses.
- **Analytic + exact finite lemma** — structural infinite proof with a bounded exact finite-state component.
- **Exact finite positive certificate** — explicit matrix with exact positive-definiteness or algebraic certificate.
- **Exact family theorem with finite certificates** — finite exact positive side plus a bounded local exact obstruction valid for an infinite tail.
- **Lean source, uncompiled here** — source exists but no current successful `lake build` record.
- **Numerical exploration** — evidence only.

## A. Periodic/Bloch results

| ID | Result | Entry | Evidence |
|---|---|---|---|
| B1 | even `s`: primitive period-`4s` antipodal family has `R_s<8` | `../extension_20260905/EVEN_JUMP_THEOREM_AND_PROOF.md` | Analytic theorem |
| B2 | even quadratic envelope `1/(6s(s+2)) <= 8-R_s <= 4 sin^2(pi/(s+2))` | `QUADRATIC_GAP_THEOREM.md` | Analytic theorem |
| B3 | odd `s`: exact alternating-flux optimizer and `s^2(8-M_s)->pi^2` | `ODD_JUMP_SHARP_GAP.md` | Analytic theorem |
| B4 | even phase-zero endpoint has sharp constant `pi^2` | `ENDPOINT_PI2_ASYMPTOTIC.md` | Analytic theorem |
| B5 | Q7 false: exact interior phase beats zero phase at `s=10` | `PHASE_SLIP_COUNTEREXAMPLE.md` | Exact Sturm certificate |
| B6 | even global edge satisfies `s^2(8-R_s)->pi^2` | `EVEN_GLOBAL_PI2_THEOREM.md` + `GLOBAL_PI2_LOCALIZATION_LEMMA.md` | Analytic theorem |
| B7 | all jumps: parity-dependent explicit family has `s^2(8-Rhat_s)->pi^2` | `ALL_S_UNIFIED_THEOREM.md` | Analytic theorem assembly |
| B8 | even phase slip: `r^2 phi_r->pi/(4sqrt2)` and `r^4(e_r-g_(2r))->pi^2/32` | `EVEN_SECOND_ORDER_PHASE_SLIP_THEOREM.md` + `SECOND_ORDER_LOCAL_IMPLICIT_LEMMA.md` | Analytic theorem |
| B9 | proposed first correction through `r^-3` in phase / `r^-5` in gain | `EVEN_THIRD_ORDER_PHASE_SLIP_REFINEMENT.md` | Analytic refinement pending separate uniform-remainder hostile audit; not in final headline theorem |

## B. Finite-order results

| ID | Result | Entry | Evidence |
|---|---|---|---|
| F0 | all admissible pairs: `m(N,s)=2 iff N=2s+2`; otherwise `m(N,s)>=sqrt5` | `../extension_20260905/FLAT_MINIMUM_AND_CHIRAL_CRITERION.md` | Analytic theorem |
| F1 | `C_21(1,7)`: every signing has `rho^2>=1066/131>8` | `C21_S7_GLOBAL_OBSTRUCTION.md`, `verify_c21_s7_all_signings.py` | Exact finite computer-assisted theorem |
| F2 | one-defect `C_(3s)(1,s)`, odd `s>=7`: `rho^2>=193/24` | `N3S_ONE_DEFECT_LOCAL_OBSTRUCTION.md`, `verify_n3s_one_defect_local_obstruction.py` | Analytic + exact local witnesses |
| F3 | nine-column signed-triangle rule: violation of middle alternation gives `rho^2>=8+1/70` | `verify_triangle_strip_local_rule.py` | Exact finite computer-assisted lemma |
| F4 | `C_27(1,9)`: every signing has `rho^2>=8+1/70` | `C27_S9_GLOBAL_OBSTRUCTION.md`, `verify_c27_s9_all_signings.py` | Exact prefix-pruned exhaustive theorem |
| F5 | all odd `s>=7`: every signing of `C_(3s)(1,s)` has `rho^2>=8+1/70` | `N3S_GLOBAL_OBSTRUCTION.md` | Analytic + exact finite lemma/base cases |
| F6 | odd `s`, even admissible `N`: period-two signing gives `rho^2<8` | Task60 + `ODD_JUMP_SHARP_GAP.md` | Analytic Fourier theorem |
| F7 | even `s`, `N=4sL`: antipodal family gives `rho^2<8`; comparison threshold `O(s)` repetitions | `FINITE_COMPARISON_LINEAR_THRESHOLD.md` | Analytic theorem |
| F8 | `C_9(1,3)` and `C_15(1,5)` admit explicit `rho^2<8` signings | `N3S_THRESHOLD_CLASSIFICATION.md`, `verify_n3s_short_threshold.py` | Exact finite positive Sylvester certificates |
| F9 | complete resonance-line threshold: `m(3s,s)<sqrt8` iff `s` even or `s in {3,5}` | `N3S_THRESHOLD_CLASSIFICATION.md` | Analytic assembly of F3--F8 + exact short certificates |
| F10 | canonical one-defect family on `N=5s`: favorable anchor is sub-eight for `s=3,5,7,9`; every one-defect sector has `rho^2>=8+1/34` for odd `s>=11` | `L5_ONE_DEFECT_THRESHOLD.md`, `verify_l5_one_defect_threshold.py` | Exact family theorem with finite certificates |
| F11 | canonical one-defect family on `N=7s`: favorable anchor is sub-eight through `s=13`; every one-defect sector has `rho^2>=8+1/142` for odd `s>=15` | `L7_L9_ONE_DEFECT_THRESHOLDS.md`, `verify_l7_l9_one_defect_thresholds.py` | Exact family theorem with finite certificates |
| F12 | canonical one-defect family on `N=9s`: favorable anchor is sub-eight through `s=17`; every one-defect sector has `rho^2>=8+1/652` for odd `s>=19` | `L7_L9_ONE_DEFECT_THRESHOLDS.md`, `verify_l7_l9_one_defect_thresholds.py` | Exact family theorem with finite certificates |
| F13 | canonical one-defect family on `N=13s`: favorable anchor is sub-eight for every odd `s<=27`; every one-defect sector has `rho^2>=8+1/940` for odd `s>=29` | `L13_ONE_DEFECT_THRESHOLD_AND_STAIRCASE.md`, `verify_l13_one_defect_threshold.py` | Exact family theorem with endpoint LDL + fixed seam witnesses |
| F14 | canonical one-defect threshold matrix on odd `N=Ls` reduces exactly from `Ls` dimensions to a `4L` endpoint Schur matrix with identical negative inertia | `ONE_DEFECT_ENDPOINT_REDUCTION.md`, `verify_one_defect_endpoint_reduction.py` | Analytic Schur/continuant theorem + regression |

## C. Corrected one-defect resonance picture

For `L=3,5,7,9`, the canonical favorable one-defect family happens to cross
the `sqrt(8)` threshold between `s=2L-1` and `s=2L+1`.

That finite pattern **does not extend to all odd `L`**.  F13 gives an exact
counterexample:

`L=13, s=27=2L+1` is still strictly sub-eight, while the uniform one-defect
failure begins at `s=29=2L+3`.

Accordingly, the old general `s=2L` aspect-ratio conjecture is **disproved and
superseded**.  The exact `L=3,5,7,9` theorems remain valid.

Using F14, numerical scans show a staircase of first-failure integers as `L`
grows.  Interpolation of the endpoint smallest eigenvalue suggests a large-`L`
critical ratio near

` s_c(L)/L ~ 2.0974 `.

This value is **Observed only**.  No limiting ratio theorem or analytic
characterizing equation is yet claimed.

Only `L=3` is currently classified over **all signings**.  For `L=5,7,9,13`,
multi-defect repair beyond the canonical one-defect threshold remains open.

## D. Exact rerun / certification status on 2026-09-07

Independently reproduced in the current analysis environment:

- F3 survivor counts: `8,56,152,440,488,1016,656,1064,128`; all 128 final survivors obey the forced middle alternation;
- F4: all `17,024` final cyclic candidates certified after exact prefix pruning;
- F1: all `49,940` admissible necklaces / `199,760` Hamilton-gauge representatives certified; weakest generated exact excess `36/262=18/131`;
- F8: every leading principal minor in both short witnesses is a positive exact integer;
- F10 short LDL pivots are positive, and all four fixed 50-vertex seam witnesses satisfy `34 q >= ||w||^2` with `q=752`, `||w||^2=25532`;
- F11/F12 short exact LDL decompositions are positive; their fixed `2L`-column seam witnesses give exact margins `1/142` and `1/652`;
- F13: exact rational endpoint LDL is positive through `s=27`, while the `s=29` endpoint has one negative pivot; the fixed 364-vertex seam window gives exact `1/940` witnesses for every sector from `s=29` onward;
- F14: the full threshold block pattern agrees entry-by-entry with the analytic formula in representative cases, and full/endpoint negative inertia agrees across both sides of the threshold.

A stronger randomized/pair-flip search on `C_55(1,11)` has not found a
sub-eight signing; the best observed squared radius was about `8.1034` in
that search.  This remains **numerical exploration only** and is not evidence
for an all-signing obstruction theorem.

## E. Formalization status

| File | Scope | Status |
|---|---|---|
| `../../../formal/QuadraticGap/CoreInequalities.lean` | even factorization/covariance core | Lean source, uncompiled here |
| `../../../formal/QuadraticGap/OddJumpCore.lean` | odd algebraic core | Lean source, uncompiled here |
| `../../../formal/QuadraticGap/PhaseSlipConstants.lean` | exact `sqrt2`/Robin/phase-slip constants | Lean source, uncompiled here |
| `../../../formal/TargetA/` | frozen period-eight kernel | pre-existing; not modified |

No new file in `formal/QuadraticGap/` is called kernel-checked until a real `lake build` succeeds with the declared toolchain.

## F. Publication boundary

The project does **not** give a closed formula for `m(N,s)` for arbitrary
pairs.  The exact finite all-signing classification currently completed is
the `sqrt(8)` threshold on `N=3s`, plus the universal flat `m=2`
classification.  F10--F14 deepen the canonical one-defect resonance theory
and provide an exact finite-dimensional reduction, but they do not yet
classify all signings on `L>=5` resonance lines.
