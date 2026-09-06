# All-`s` sharp quadratic-gap workstream

Branch: `research/quadratic-gap-upgrade`
Date: 2026-09-06

This directory treats the full jump parameter `s>=2` for explicit periodic
signings of `C_N(1,s)`.  The parity split is structural:

- even `s`: primitive period-`4s` antipodal defect family;
- odd `s`: period-two alternating-flux family.

The frozen period-eight manuscript and `formal/TargetA` remain unchanged.

## Headline results

For the parity-dependent explicit family, write `Rhat_s` for the continuous
squared Bloch radius and `ghat_s=8-Rhat_s`.  The workstream proves

\[
 \boxed{s^2\widehat g_s\to\pi^2}
\]

through **all integer jumps**.

For even `s=2r`, the phase slip is now also resolved to second order.  If
`h_r=2 cos(phi_r)` is globally optimizing and `e_r` is the phase-zero gap,
then

\[
 \boxed{r^2\phi_r\to\frac\pi{4\sqrt2}},
 \qquad
 \boxed{r^4(e_r-g_{2r})\to\frac{\pi^2}{32}}.
\]

Thus the global even edge has the expansion

\[
 g_{2r}=e_r-\frac{\pi^2}{32r^4}+o(r^{-4}),
\]

and the lower soft branch obeys the boundary-layer law

\[
 r^4\bigl(g_{2r}(z/r^2)-e_r\bigr)
 \to z^2-\frac\pi{2\sqrt2}z.
\]

## Current result map

1. `ALL_S_UNIFIED_THEOREM.md`
   - parity-dependent explicit signing for every integer `s>=2`;
   - common quadratic envelope;
   - sharp parity-free `pi^2` limit;
   - second-order even phase-slip refinement.
2. `ODD_JUMP_SHARP_GAP.md`
   - unique odd-jump maximizing phase;
   - exact Chebyshev critical equation;
   - `O(s^-3)` phase localization;
   - sharp odd `pi^2` limit.
3. `QUADRATIC_GAP_THEOREM.md`
   - even-jump lower bound upgraded from `Omega(s^-3)` to `Omega(s^-2)`.
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
   - proves `r^2 phi_r -> pi/(4sqrt2)`;
   - proves `r^4(e_r-g_(2r)) -> pi^2/32`;
   - derives the cusp/effective-parabola law.
9. `SECOND_ORDER_LOCAL_IMPLICIT_LEMMA.md`
   - bootstraps `mu=o(r^-2)` to `mu=O(r^-4)` from global optimality;
   - gives the sharp Robin-coordinate displacement coefficient
     `1/(2sqrt2)`.
10. `FINITE_COMPARISON_LINEAR_THRESHOLD.md`
    - even finite comparison threshold improved to `O(s)` repetitions.
11. `ODD_ORDER_ONE_DEFECT_OBSTRUCTION.md`
    - exact integer Rayleigh certificates at `(N,s)=(21,7)`;
    - rules out the naive one-defect odd-order repair.
12. `verify_quadratic_gap_upgrade.py`, `verify_odd_jump_gap.py`,
    `verify_odd_order_obstruction.py`, `verify_second_order_phase_slip.py`
    - declared-scope exact/symbolic/numerical audits.
13. `../../../formal/QuadraticGap/`
    - separate Lean formalization track; frozen `formal/TargetA` untouched.

## What remains mathematically

The leading and second-order Bloch asymptotics are now closed for the
explicit family.  The main remaining mathematical directions are:

- higher-order even phase-slip expansion beyond `r^-4`;
- odd-order finite-ring constructions using balanced multi-defect or
  genuinely odd-period words;
- removal of the `4s | N` restriction for even jumps;
- global minimization over all signings (`m(N,s)`), which is a different and
  substantially harder problem;
- Lean formalization of the odd sharp theorem, global localization and
  second-order bootstrap.

## Finite-order coverage

- odd `s`: every admissible even `N` is covered by the period-two word;
- even `s`: the current explicit theorem covers `N=4sL`.

The jump parameter is fully covered, while finite-order compatibility is not.
The exact `(21,7)` obstruction shows that odd orders require more than a
single alternating defect.

No global optimality over all signings and no final publication-priority
claim are made here.
