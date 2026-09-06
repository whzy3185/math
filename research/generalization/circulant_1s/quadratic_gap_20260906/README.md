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
2. `PHASE_SLIP_COUNTEREXAMPLE.md`
   - disproves the old phase-zero conjecture Q7;
   - gives an exact rational/Sturm certificate already at `s=10`.
3. `verify_quadratic_gap_upgrade.py`
   - exact symbolic checks for the new generating-function identities;
   - exact Sturm verification of the `s=10` phase-slip certificate.
4. `../../../formal/QuadraticGap/CoreInequalities.lean`
   - starts a separate Lean formalization track for the new proof;
   - leaves the frozen `formal/TargetA` kernel untouched.

## Research status

The exponent problem is now closed for the explicit antipodal family.
The sharp asymptotic problem remains open:

` s^2 (8-R_s) -> pi^2 ? `

The former shortcut Q7 ("the maximizing phase is always zero") is false, so
the sharp analysis must include a shrinking phase boundary layer.

## Next proof targets

- derive the asymptotic root equation of `q_r(y,h)` in the scaling
  `8-y = Theta(r^-2)` and `4-h^2 = O(r^-4)`;
- prove the optimizer lies in that phase window;
- identify the limiting Robin boundary condition in the soft Chebyshev
  channel;
- extract the constant `pi^2` and the first phase-slip correction;
- formalize the Pell-square kernel and coefficient-convolution argument in
  Lean;
- update the finite-`N` comparison threshold using the new quadratic lower
  gap.

No claim of final publication priority is made here.  The nearby signed
circulant literature and periodic/magnetic operator literature still require
full comparison before a novelty statement is used in a manuscript.
