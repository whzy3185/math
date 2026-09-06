# All-`s` quadratic-gap workstream

Branch: `research/quadratic-gap-upgrade`
Date: 2026-09-06

This directory now treats the full jump parameter `s>=2` for explicit
periodic signings of `C_N(1,s)`.  The parity split is structural:

- even `s`: primitive period-`4s` antipodal defect family;
- odd `s`: period-two alternating-flux family.

The old frozen period-eight manuscript and `formal/TargetA` remain unchanged.

## Current results

1. `ALL_S_UNIFIED_THEOREM.md`
   - combines the even and odd constructions;
   - proves an explicit sub-eight family for every integer `s>=2`;
   - proves the parity-free envelope
     `1/(6 s (s+2)) <= 8-Rhat_s <= 4 sin^2(pi/(s+2))`;
   - hence `8-Rhat_s = Theta(s^-2)` for all jumps.
2. `ODD_JUMP_SHARP_GAP.md`
   - upgrades the old qualitative odd-jump threshold `M_s<8`;
   - proves a unique maximizing phase and the exact critical equation
     `s U_(s-1)(cos(2 theta_s))=1`;
   - localizes `theta_s` within `O(s^-3)` of `pi/(2s)`;
   - proves the sharp odd-subsequence limit
     `s^2 (8-M_s) -> pi^2`;
   - for every admissible even `N`, gives an explicit odd-jump finite signing
     with squared spectral radius below `8`.
3. `QUADRATIC_GAP_THEOREM.md`
   - upgrades the even-jump lower bound from `Omega(s^-3)` to `Omega(s^-2)`;
   - proves
     `1/(6 s (s+2)) <= 8-R_s <= 4 sin^2(pi/(s+2))`.
4. `ENDPOINT_PI2_ASYMPTOTIC.md`
   - proves the sharp even endpoint limit
     `s^2 (8-rho(H_s(1))^2) -> pi^2`;
   - identifies the limiting soft-channel Dirichlet--Robin equation.
5. `PHASE_SLIP_COUNTEREXAMPLE.md`
   - disproves the even-jump phase-zero conjecture Q7;
   - gives an exact rational/Sturm certificate at `s=10`.
6. `FINITE_COMPARISON_LINEAR_THRESHOLD.md`
   - improves the even-jump sufficient repetition threshold from
     `O(s^(3/2))` to `O(s)`.
7. `verify_quadratic_gap_upgrade.py`
   - exact symbolic checks for the even-jump generating-function identities;
   - exact Sturm verification of the `s=10` phase-slip certificate.
8. `verify_odd_jump_gap.py`
   - exact Chebyshev derivative identities for odd jumps;
   - numerical verification of the unique phase and sharp finite-`s` bounds;
   - symbolic verification of the first recorded asymptotic coefficients.
9. `../../../formal/QuadraticGap/CoreInequalities.lean`
   - separate Lean formalization track for the new proof;
   - leaves the frozen `formal/TargetA` kernel untouched.

## Current theorem picture

For the parity-dependent explicit family, write `Rhat_s` for the continuous
squared Bloch radius and `ghat_s=8-Rhat_s`.  We now know

`ghat_s = Theta(s^-2)`

for every integer jump `s>=2`.

On odd jumps the sharp result is complete:

` s^2 ghat_s -> pi^2  (s odd). `

On even jumps the endpoint has the same `pi^2` constant, but a small phase
slip can improve the spectral edge.  The remaining sharp global question is

` s^2 ghat_s -> pi^2  (s even) ? `

with rigorous bracket

`1/6 <= liminf s^2 ghat_s <= limsup s^2 ghat_s <= pi^2`.

Therefore the only obstruction to a parity-free sharp `pi^2` theorem is the
even phase-slip problem.

## Finite-order coverage

- odd `s`: every admissible even order `N` is covered by the period-two word;
- even `s`: the current explicit theorem covers `N=4sL`.

Thus the jump parameter has been extended to all `s`, but order-compatibility
has not yet been removed for every `N`.  Odd `N` and non-`4s`-divisible even
orders are separate finite-ring extension problems.

## Next proof targets

- close the even global sharp limit by a two-mode small-phase analysis;
- investigate near-alternating defect words for odd `N` to remove the
  period-two lift obstruction;
- investigate seam/phase interpolation for even `s` when `4s` does not divide
  `N`;
- formalize the odd Chebyshev critical-point lemmas in Lean;
- formalize the Pell-square kernel and coefficient-convolution argument for
  the even quadratic lower bound;
- extend the literature audit to periodic/magnetic Jacobi-strip and
  defect-state formulations before any priority claim.

No final publication-priority claim is made here.  The current arXiv signed
circulant benchmark found in the audit treats `C_n(1,2)`; the all-jump result
still needs broader operator-literature comparison before novelty language is
used in a manuscript.
