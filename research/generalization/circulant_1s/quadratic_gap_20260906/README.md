# All-`s` sharp quadratic-gap workstream

Branch: `research/quadratic-gap-upgrade`
Date: 2026-09-06

This directory treats the full jump parameter `s>=2` for explicit periodic
signings of `C_N(1,s)`.  The parity split is structural:

- even `s`: primitive period-`4s` antipodal defect family;
- odd `s`: period-two alternating-flux family.

The old frozen period-eight manuscript and `formal/TargetA` remain unchanged.

## Current headline result

For the parity-dependent explicit family, write `Rhat_s` for the continuous
squared Bloch radius and `ghat_s=8-Rhat_s`.  The workstream now proves

\[
 \boxed{s^2\,\widehat g_s\to\pi^2}
\]

through **all integer jumps `s>=2`**.

This sharp statement combines:

- odd `s`: exact alternating-flux model with a unique interior optimizer;
- even `s`: antipodal defect model, exact phase slip, and a new global
  phase-localization argument showing the slip is lower order.

## Current results

1. `ALL_S_UNIFIED_THEOREM.md`
   - parity-dependent explicit signing for every integer `s>=2`;
   - common quadratic envelope
     `1/(6s(s+2)) <= 8-Rhat_s <= 4 sin^2(pi/(s+2))`;
   - sharp parity-free limit `s^2(8-Rhat_s)->pi^2`.
2. `ODD_JUMP_SHARP_GAP.md`
   - unique odd-jump maximizing phase;
   - exact critical equation `s U_(s-1)(cos(2 theta_s))=1`;
   - `O(s^-3)` phase localization around `pi/(2s)`;
   - sharp odd limit `s^2(8-M_s)->pi^2`.
3. `QUADRATIC_GAP_THEOREM.md`
   - even-jump lower bound upgraded from `Omega(s^-3)` to `Omega(s^-2)`.
4. `ENDPOINT_PI2_ASYMPTOTIC.md`
   - sharp even phase-zero endpoint limit.
5. `PHASE_SLIP_COUNTEREXAMPLE.md`
   - exact `s=10` Sturm certificate showing the global even phase is not
     always zero.
6. `EVEN_GLOBAL_PI2_THEOREM.md`
   - closes the global even sharp limit despite phase slip;
   - proves `r^2(2-h_r)->0` for every global maximizing phase sequence.
7. `GLOBAL_PI2_LOCALIZATION_LEMMA.md`
   - makes the delicate hyperbolic localization step explicit;
   - gives the exact RHS bound `2 sqrt(11)`;
   - factors the left coefficient as
     `(p-lambda q)(p-lambda^(-1)q)/p`;
   - proves `2-h=O(r^-2)` before the limiting Robin argument.
8. `FINITE_COMPARISON_LINEAR_THRESHOLD.md`
   - even-jump sufficient repetition threshold improved from
     `O(s^(3/2))` to `O(s)`.
9. `ODD_ORDER_ONE_DEFECT_OBSTRUCTION.md`
   - exact integer Rayleigh certificates at `(N,s)=(21,7)`;
   - rules out the naive one-defect odd-order repair.
10. `verify_quadratic_gap_upgrade.py`, `verify_odd_jump_gap.py`,
    `verify_odd_order_obstruction.py`
   - exact/symbolic/numerical reproducibility checks with declared scope.
11. `../../../formal/QuadraticGap/`
   - separate Lean formalization track;
   - frozen `formal/TargetA` remains untouched.

## Even phase slip: what remains

The leading constant is closed.  Numerical diagonalization now points to a
second-order law rather than a leading-order uncertainty.  If
`h_r=2 cos(phi_r)` is globally optimizing and `e_r` is the phase-zero gap,
the current conjectural refinement is

\[
 r^2\phi_r\to\frac\pi{4\sqrt2},
 \qquad
 r^4(e_r-g_{2r})\to\frac{\pi^2}{32}.
\]

This is consistent with an effective two-mode expansion

\[
 g_{2r}(\phi)=e_r+\phi^2
 -\frac{\pi}{2\sqrt2}\frac{|\phi|}{r^2}+o(r^{-4}).
\]

These second-order constants are **not yet theorems**.

## Finite-order coverage

- odd `s`: every admissible even `N` is covered by the period-two word;
- even `s`: the current explicit theorem covers `N=4sL`.

The jump parameter is therefore fully covered, while finite-order
compatibility remains open.  The exact `(21,7)` obstruction shows that odd
orders require a multi-defect or genuinely odd-period construction.

## Next proof targets

- derive and prove the second-order even two-mode effective matrix;
- prove or disprove the constants `pi/(4sqrt2)` and `pi^2/32`;
- design balanced multi-defect/odd-period words for odd `N`;
- remove the `4s | N` restriction for even jumps;
- formalize the odd Chebyshev critical-point theorem and the even global
  localization lemma in Lean;
- extend the publication-priority audit to periodic/magnetic Jacobi-strip
  and defect-state literature.

No global optimality over all signings and no final priority claim are made.
