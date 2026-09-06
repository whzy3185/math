# All-`s` sharp quadratic-gap workstream

Branch: `research/quadratic-gap-upgrade`
Date: 2026-09-06

This directory treats the full jump parameter `s>=2` for explicit periodic
signings of `C_N(1,s)`.  The parity split is structural:

- even `s`: primitive period-`4s` antipodal defect family;
- odd `s`: period-two alternating-flux family.

The frozen period-eight manuscript and `formal/TargetA` remain unchanged.

## Headline Bloch results

For the parity-dependent explicit family, write `Rhat_s` for the continuous
squared Bloch radius and `ghat_s=8-Rhat_s`.  The workstream proves

\[
 \boxed{s^2\widehat g_s\to\pi^2}
\]

through **all integer jumps**.

For even `s=2r`, the phase slip is resolved beyond leading order.  If
`h_r=2 cos(phi_r)` is globally optimizing and `e_r` is the phase-zero gap,
then

\[
 \phi_r=
 \frac\pi{4\sqrt2\,r^2}
 -\frac{3\pi}{16r^3}
 +o(r^{-3}),
\]

and

\[
 e_r-g_{2r}
 =\frac{\pi^2}{32r^4}
 -\frac{3\pi^2}{32\sqrt2\,r^5}
 +o(r^{-5}).
\]

The lower soft branch has the avoided-crossing boundary-layer law

\[
 r^4\bigl(g_{2r}(z/r^2)-e_r\bigr)
 \to z^2-\frac\pi{2\sqrt2}z.
\]

## New finite-order obstruction

The finite-order problem is genuinely different from the Bloch problem.
`C21_S7_GLOBAL_OBSTRUCTION.md` proves by exhaustive exact certification that
for **every** signing of `C_21(1,7)`,

\[
 \boxed{
 \rho(A)^2\ge\frac{1066}{131}>8.}
\]

The exhaustive reduction contains `49,940` admissible cyclic `Q`-necklaces
and `199,760` Hamilton-gauge representatives after scanning both anchors and
both holonomies.  For every representative the verifier constructs an
integer vector `w` and checks the exact inequality

\[
 w^T(8I-A^2)w<0.
\]

Thus not every admissible finite pair `(N,s)` can inherit a sub-`sqrt(8)`
signing, even though every jump has a periodic Bloch construction below the
threshold.

## Current result map

1. `ALL_S_UNIFIED_THEOREM.md`
   - explicit parity-dependent family for every `s>=2`;
   - common quadratic envelope;
   - sharp parity-free `pi^2` limit;
   - second-order even phase-slip refinement.
2. `ODD_JUMP_SHARP_GAP.md`
   - exact odd dispersion, unique optimizer and sharp `pi^2` limit.
3. `QUADRATIC_GAP_THEOREM.md`
   - even lower bound upgraded from `Omega(s^-3)` to `Omega(s^-2)`.
4. `ENDPOINT_PI2_ASYMPTOTIC.md`
   - sharp even phase-zero endpoint limit.
5. `PHASE_SLIP_COUNTEREXAMPLE.md`
   - exact `s=10` Sturm certificate proving phase zero is not always global.
6. `EVEN_GLOBAL_PI2_THEOREM.md`
   - closes the global even sharp leading constant despite phase slip.
7. `GLOBAL_PI2_LOCALIZATION_LEMMA.md`
   - explicit hyperbolic localization with bounded RHS and factored
     coefficient.
8. `EVEN_SECOND_ORDER_PHASE_SLIP_THEOREM.md`
   - proves `r^2 phi_r -> pi/(4sqrt2)` and
     `r^4(e_r-g_(2r)) -> pi^2/32`.
9. `SECOND_ORDER_LOCAL_IMPLICIT_LEMMA.md`
   - bootstraps the phase mass to `mu=O(r^-4)` and extracts the exact cusp
     coefficient `1/(2sqrt2)`.
10. `EVEN_THIRD_ORDER_PHASE_SLIP_REFINEMENT.md`
    - proves the `-3pi/(16r^3)` phase correction and the
      `-3pi^2/(32sqrt2 r^5)` gain correction.
11. `FINITE_COMPARISON_LINEAR_THRESHOLD.md`
    - even finite comparison threshold improved to `O(s)` repetitions.
12. `ODD_ORDER_ONE_DEFECT_OBSTRUCTION.md`
    - exact one-defect failure certificate at `(21,7)`.
13. `C21_S7_GLOBAL_OBSTRUCTION.md`
    - exhaustive all-signing obstruction with uniform exact margin
      `rho^2>=1066/131`.
14. `verify_c21_s7_all_signings.py`
    - exact integer certificate stage for all `199,760` representatives.
15. `verify_quadratic_gap_upgrade.py`, `verify_odd_jump_gap.py`,
    `verify_odd_order_obstruction.py`, `verify_second_order_phase_slip.py`
    - declared-scope exact/symbolic/numerical audits.
16. `../../../formal/QuadraticGap/`
    - separate Lean track, now including `PhaseSlipConstants.lean`;
    - frozen `formal/TargetA` remains untouched.

## What remains mathematically

The main remaining directions are now:

- structural classification of finite obstructions, beginning with the
  resonance family `N=3s` for odd `s`;
- exact determination of `m(21,7)` rather than only a strict lower bound;
- construction/classification of odd orders that do admit sub-`sqrt(8)`
  signings;
- removal of the `4s | N` restriction for even jumps;
- higher corrections beyond the currently proved `r^-5` phase-slip gain;
- global minimization over all signings for general `(N,s)`;
- Lean formalization of the odd sharp theorem, global localization,
  boundary-layer bootstrap and finite certificate.

## Finite-order coverage

- odd `s`, even `N`: period-two word gives `rho^2<8` for every admissible
  pair;
- even `s`: current explicit finite theorem covers `N=4sL`;
- odd `N`: arithmetic obstructions occur; `C_21(1,7)` has no sub-`sqrt(8)`
  signing at all.

No general formula for `m(N,s)` and no final publication-priority claim are
made here.
