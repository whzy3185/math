# Current theorem / evidence index

Date: 2026-09-06
Branch: `research/quadratic-gap-upgrade`

This index supersedes the 2026-09-05 status **for this workstream only**.  The
older repository-wide index remains a historical snapshot and should not be
used to infer that Q6/Q7 are still open.

## Evidence labels

- **Analytic theorem** — a readable mathematical proof is present; not yet
  independently refereed.
- **Exact finite computer-assisted theorem** — a finite exhaustive step is
  certified by integer/rational identities; floating arithmetic may propose a
  witness but does not decide correctness.
- **Analytic + exact finite lemma** — structural proof with a bounded exact
  finite-state component.
- **Lean source, uncompiled here** — formalization source exists but the
  current environment has no Lean/Lake execution record.
- **Numerical exploration** — evidence only; never a theorem dependency.

## A. Periodic/Bloch results

| ID | Result | Entry | Evidence |
|---|---|---|---|
| B1 | even `s`: primitive period-`4s` antipodal family has `R_s<8` | `../extension_20260905/EVEN_JUMP_THEOREM_AND_PROOF.md` | Analytic theorem |
| B2 | even quadratic envelope `1/(6s(s+2)) <= 8-R_s <= 4 sin^2(pi/(s+2))` | `QUADRATIC_GAP_THEOREM.md` | Analytic theorem |
| B3 | odd `s`: exact alternating-flux optimizer and `s^2(8-M_s)->pi^2` | `ODD_JUMP_SHARP_GAP.md` | Analytic theorem |
| B4 | even phase-zero endpoint has sharp constant `pi^2` | `ENDPOINT_PI2_ASYMPTOTIC.md` | Analytic theorem |
| B5 | Q7 is false: exact interior phase beats zero phase at `s=10` | `PHASE_SLIP_COUNTEREXAMPLE.md` | Exact Sturm certificate |
| B6 | even global edge still satisfies `s^2(8-R_s)->pi^2` | `EVEN_GLOBAL_PI2_THEOREM.md` + `GLOBAL_PI2_LOCALIZATION_LEMMA.md` | Analytic theorem |
| B7 | all jumps: parity-dependent explicit family has `s^2(8-Rhat_s)->pi^2` | `ALL_S_UNIFIED_THEOREM.md` | Analytic theorem assembly |
| B8 | even phase slip: `r^2 phi_r->pi/(4sqrt2)` and `r^4(e_r-g_(2r))->pi^2/32` | `EVEN_SECOND_ORDER_PHASE_SLIP_THEOREM.md` + `SECOND_ORDER_LOCAL_IMPLICIT_LEMMA.md` | Analytic theorem |
| B9 | first correction: `phi_r=pi/(4sqrt2 r^2)-3pi/(16r^3)+o(r^-3)` and gain through `r^-5` | `EVEN_THIRD_ORDER_PHASE_SLIP_REFINEMENT.md` | Analytic theorem |

## B. Finite-order results

| ID | Result | Entry | Evidence |
|---|---|---|---|
| F1 | `C_21(1,7)`: every signing has `rho^2>=1066/131>8` | `C21_S7_GLOBAL_OBSTRUCTION.md`, `verify_c21_s7_all_signings.py` | Exact finite computer-assisted theorem |
| F2 | one-defect `C_(3s)(1,s)`, odd `s>=7`: `rho^2>=193/24` | `N3S_ONE_DEFECT_LOCAL_OBSTRUCTION.md`, `verify_n3s_one_defect_local_obstruction.py` | Analytic + four exact local witnesses |
| F3 | nine-column signed-triangle rule: violation of middle alternation gives `rho^2>=8+1/1038` | `verify_triangle_strip_local_rule.py` | Exact finite computer-assisted lemma |
| F4 | `C_27(1,9)`: every signing has `rho^2>=8+1/1038` | `verify_c27_s9_all_signings.py` | Exact prefix-pruned exhaustive theorem |
| F5 | all odd `s>=7`: every signing of `C_(3s)(1,s)` has `rho^2>=8+1/1038` | `N3S_GLOBAL_OBSTRUCTION.md` | Analytic + exact finite lemma, with exact base cases |
| F6 | odd `s`, even admissible `N`: period-two signing gives `rho^2<8` | Task60 + `ODD_JUMP_SHARP_GAP.md` | Analytic Fourier theorem |
| F7 | even `s`, `N=4sL`: antipodal family gives `rho^2<8`; comparison threshold is `O(s)` repetitions | `FINITE_COMPARISON_LINEAR_THRESHOLD.md` | Analytic theorem |

## C. Formalization status

| File | Scope | Status |
|---|---|---|
| `../../../formal/QuadraticGap/CoreInequalities.lean` | even factorization/covariance core | Lean source, uncompiled here |
| `../../../formal/QuadraticGap/OddJumpCore.lean` | odd algebraic core | Lean source, uncompiled here |
| `../../../formal/QuadraticGap/PhaseSlipConstants.lean` | exact `sqrt2`/Robin/phase-slip constants | Lean source, uncompiled here |
| `../../../formal/TargetA/` | frozen period-eight kernel | pre-existing; not modified by this branch |

No new file in `formal/QuadraticGap/` should be called kernel-checked until a
real `lake build` succeeds in an environment with the declared toolchain.

## D. Exploratory only

- `explore_even_phase_slip_second_order.py` — numerical phase-slip discovery.
- `verify_second_order_phase_slip.py` — numerical regression of analytic
  asymptotics; audit only.
- `explore_odd_order_resonances.py` and `ODD_ORDER_RESONANCE_MAP.md` — map
  other short chord-cycle lengths; not a theorem beyond separately cited
  exact results.

## E. Superseded conjecture status

The old 2026-09-05 entries should now be read as follows:

- old Q5 / cubic gap target — superseded by B2;
- old Q6 `s^2(8-R_s)->pi^2` — **proved** by B3/B6/B7;
- old Q7 phase-zero global maximizer — **disproved** by B5;
- second-order phase-slip constants — **proved** by B8 and refined by B9.

## F. Publication boundary

Proved results do **not** imply a closed formula for `m(N,s)` for arbitrary
pairs, nor global optimality of the periodic parity-dependent family on every
finite ring.  The only current infinite all-signing finite classification is
F5 (`N=3s`, odd `s>=7`), together with isolated exact statements such as F1
and F4.
