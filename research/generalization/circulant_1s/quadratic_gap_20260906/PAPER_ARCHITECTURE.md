# Manuscript architecture: parity-resolved quadratic gaps in signed circulants

Date: 2026-09-06
Branch: `research/quadratic-gap-upgrade`

## Working title

**Parity-Resolved Quadratic Bloch Gaps in Periodic Signings of `C_N(1,s)`**

Alternative title if the even sharp limit is closed:

**Sharp Quadratic Bloch Gaps for Explicit Signings of `C_N(1,s)` for All Jumps**

## Intended contribution package

The paper should now be organized around the full jump parameter `s>=2`, not
only even jumps.  The parity split is mathematically meaningful:

- odd `s`: the alternating-flux word is exactly solvable and already has a
  strict interior Bloch edge below `8`;
- even `s`: the alternating word touches `8`, and an antipodal defect family
  is needed to open a gap.

Current rigorous package:

1. an explicit periodic sub-eight signing for every integer jump `s>=2`;
2. a parity-free quadratic envelope
   `1/(6s(s+2)) <= 8-Rhat_s <= 4 sin^2(pi/(s+2))`;
3. therefore `8-Rhat_s = Theta(s^-2)` for all jumps;
4. for odd `s`, a unique maximizing phase, algebraic Chebyshev equation and
   sharp asymptotic `s^2(8-M_s)->pi^2`;
5. for even `s`, the primitive antipodal construction and exact continuant
   determinant reduction;
6. for even `s`, the new two-sided quadratic gap and endpoint sharp
   `pi^2` asymptotic;
7. an exact `s=10` counterexample to phase-zero maximality;
8. finite odd-jump coverage for every admissible even order `N`;
9. the even finite comparison threshold improved from `O(s^(3/2))`
   repetitions to `O(s)`;
10. symbolic verification scripts and a separate Lean formalization track.

The strongest desired addition before submission remains the even global
sharp limit

` s^2(8-R_s) -> pi^2  (s even). `

Once this is closed, the parity-free explicit family will satisfy

` s^2(8-Rhat_s) -> pi^2 `

through all integer jumps.

## Proposed theorem hierarchy

### Theorem A — all-jump explicit sub-eight family

Define the parity-dependent construction:

- odd `s`: `tau_i=(-1)^i`, period two;
- even `s`: the primitive period-`4s` antipodal word.

Prove `Rhat_s<8` for every integer `s>=2` and the common estimate

`1/(6s(s+2)) <= 8-Rhat_s <= 4 sin^2(pi/(s+2))`.

This should be the headline theorem because it removes the jump-parity
restriction from the main existence statement.

### Theorem B — odd-jump exact model and sharp gap

For odd `s>=3`, prove

`M_s=max_theta [4+2 cos(2theta)-2 cos(2s theta)] < 8`

and

`8-M_s = 4 min_theta [sin^2 theta + cos^2(s theta)]`.

Show the unique minimizer `theta_s` lies in `(0,pi/(2s))` and satisfies

`s U_(s-1)(cos(2 theta_s))=1`.

Prove the quantitative localization

`0 < pi/(2s)-theta_s <= pi^2/(4s^3)`

and the sharp two-sided estimate

`4 sin^2(pi/(2s)-pi^2/(4s^3))
 <= 8-M_s <= 4 sin^2(pi/(2s))`.

Hence

` s^2(8-M_s) -> pi^2. `

This section supplies an exactly tractable reference model for the harder
even phase-slip analysis.

### Theorem C — all-even antipodal sub-eight family

State the primitive period-`4s` signing and prove `R_s<8` for every even
`s>=2` via chirality, the reduced threshold matrix and determinant positivity.

### Theorem D — even quadratic-order gap

State

`1/(6s(s+2)) <= 8-R_s <= 4 sin^2(pi/(s+2))`.

The proof should emphasize:

- factorization of the threshold denominator into two Chebyshev channels;
- two-point mixture/covariance inequality;
- Pell-square derivative kernel;
- exact coefficient convolution retaining the cancellation lost in the old
  cubic estimate;
- inverse-trace lower bound for the least threshold eigenvalue.

### Theorem E — even endpoint sharp constant

Prove

` s^2(8-rho(H_s(1))^2) -> pi^2. `

Interpret the limiting equation as a soft-channel Dirichlet--Robin boundary
condition becoming asymptotically Neumann at the far endpoint.

### Proposition F — phase-zero failure

Give the exact `s=10` Sturm certificate:

- endpoint parameter `h=2`;
- interior parameter `h=19997/10000`;
- separator `y=317/40`;
- zero roots above the separator at the endpoint and one root above it at
  the interior phase.

This should be presented as an exact algebraic certificate, not numerical
sampling.

### Theorem G — even global sharp limit (target)

Desired statement:

` s^2(8-R_s) -> pi^2  (s even). `

Sufficient route:

- identify the two near-degenerate endpoint soft modes;
- derive a two-mode effective matrix for phase `phi=O(r^-2)`;
- prove the optimizer remains in that window;
- show the phase improvement is `o(r^-2)`.

A stronger second-order theorem may record the scaling of the phase slip and
the `r^-4` correction.

### Corollary H — finite signed-circulant consequences

Odd `s`:

- every admissible even `N` is covered by the period-two word;
- both holonomy sectors satisfy `rho^2<=M_s<8`.

Even `s`:

- for `N=4sL`, the antipodal family gives `rho^2<=R_s<8`;
- the explicit sufficient comparison condition is
  `L > pi * sqrt(3 (s+2)(1+s^2)/(2s))`.

The remaining order-compatibility problem should be stated separately:
odd `N` for odd jumps and non-`4s`-divisible orders for even jumps.

## Section plan

1. **Introduction and positioning**
   - fixed-underlying-graph signing minimization;
   - signed circulants and the `C_n(1,2)` benchmark;
   - the parity mechanism for general `C_N(1,s)`;
   - statement of the all-jump explicit theorem;
   - precise boundary: no global minimizer classification is claimed.
2. **Gauge and universal squared-operator algebra**
3. **Odd jumps: exact Fourier model**
4. **Odd jumps: unique phase and sharp `pi^2` gap**
5. **Even jumps: antipodal chirality and reduced threshold matrix**
6. **Exact continuant determinant for even jumps**
7. **Positive generating functions and threshold positivity**
8. **Even quadratic gap via the Pell derivative kernel**
9. **Endpoint `pi^2` asymptotics and the limiting Robin condition**
10. **Exact phase-slip counterexample**
11. **Small-phase effective theory and even global sharp asymptotics**
12. **Finite-order consequences and compatibility obstructions**
13. **Formal verification and reproducibility boundary**
14. **Literature comparison and open problems**

## Publication-strength boundary

The paper should not claim:

- a closed formula for the global minimum `m(N,s)` over all signings;
- that either parity-dependent family is globally optimal;
- that phase zero is the maximizing Bloch phase for even jumps;
- coverage of every order `N`;
- novelty of general spectral-radius-two signed-graph theory;
- priority before the periodic/magnetic operator literature audit is
  completed.

The all-`s` theorem is already a coherent main result.  Closing Theorem G
would make the asymptotic story substantially stronger by giving a universal
sharp constant through both parity classes.

## Formalization plan

The new Lean development remains separate from frozen `formal/TargetA`.
Suggested dependency order:

1. `OddJumpCore.lean` — weighted-distance/Cauchy algebra for the odd coarse
   bound;
2. `OddJumpTrig.lean` — trigonometric variational identity and monotonicity of
   `sin(sx)/sin x` on the first cell;
3. `OddJumpSharp.lean` — unique critical point, phase localization and sharp
   odd asymptotic;
4. `CoreInequalities.lean` — even denominator factorization and two-point
   covariance;
5. `ChebyshevMixture.lean` — `B_i B_j <= 2 B_(i+j)` and mixture bound;
6. `PellKernel.lean` — Pell-square generating kernel and exponential bound;
7. `CoefficientConvolution.lean` — formal derivative coefficient estimate;
8. `TraceGap.lean` — abstract positive-definite inverse-trace bridge;
9. `QuadraticGapTheorem.lean` — assemble the even analytic inequality;
10. `AllSTheorem.lean` — combine parity cases once the analytic interfaces are
    formalized.

The exact Sturm `s=10` certificate can be formalized later by a verified
polynomial certificate; it should not block the analytic Lean track.
