# Quadratic-gap upgrade workstream

Branch: `research/quadratic-gap-upgrade`
Date: 2026-09-06

This directory continues the all-even `C_N(1,s)` antipodal construction from
`../extension_20260905/`.

## Current results

1. `QUADRATIC_GAP_THEOREM.md`
   - upgrades the uniform lower bound from `Omega(s^-3)` to `Omega(s^-2)`;
   - proves
     `1/(6 s (s+2)) <= 8-R_s <= 4 sin^2(pi/(s+2))`;
   - therefore closes the exponent and establishes `8-R_s = Theta(s^-2)`.
2. `ENDPOINT_PI2_ASYMPTOTIC.md`
   - proves the sharp endpoint limit
     `s^2 (8-rho(H_s(1))^2) -> pi^2`;
   - identifies the limiting soft-channel Dirichlet--Robin equation;
   - improves the global statement to `limsup s^2(8-R_s) <= pi^2`.
3. `PHASE_SLIP_COUNTEREXAMPLE.md`
   - disproves the old phase-zero conjecture Q7;
   - gives an exact rational/Sturm certificate already at `s=10`.
4. `FINITE_COMPARISON_LINEAR_THRESHOLD.md`
   - combines the quadratic gap with the old alternating lower estimate;
   - improves the sufficient repetition threshold from `O(s^(3/2))` to
     `O(s)`.
5. `verify_quadratic_gap_upgrade.py`
   - exact symbolic checks for the new generating-function identities;
   - exact Sturm verification of the `s=10` phase-slip certificate.
6. `../../../formal/QuadraticGap/CoreInequalities.lean`
   - starts a separate Lean formalization track for the new proof;
   - leaves the frozen `formal/TargetA` kernel untouched.

## Research status

The exponent problem is closed for the explicit antipodal family, and the
endpoint has the conjectured `pi^2` constant.  The remaining sharp global
question is

` s^2 (8-R_s) -> pi^2 ? `

The former shortcut Q7 ("the maximizing phase is always zero") is false, so
the global proof must show that the phase slip only changes lower-order
terms.

The current rigorous asymptotic bracket is

`1/6 <= liminf s^2(8-R_s) <= limsup s^2(8-R_s) <= pi^2`.

## Next proof targets

- analyze the two near-degenerate endpoint branches under a small Bloch
  phase and obtain a two-mode effective equation;
- prove the optimizer satisfies `4-h^2 = O(r^-4)`;
- show the phase improvement is `o(r^-2)`, which would close the global
  `pi^2` limit;
- extract the first phase-slip correction after the leading constant;
- formalize the Pell-square kernel and coefficient-convolution argument in
  Lean;
- extend the literature audit to periodic/magnetic Jacobi-strip and
  defect-state formulations before any priority claim.

No claim of final publication priority is made here.  The nearby signed
circulant literature and periodic/magnetic operator literature still require
full comparison before a novelty statement is used in a manuscript.
