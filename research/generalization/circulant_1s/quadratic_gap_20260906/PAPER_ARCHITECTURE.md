# Manuscript architecture: quadratic gap and phase slip in signed circulants

Date: 2026-09-06
Branch: `research/quadratic-gap-upgrade`

## Working title

**Quadratic Bloch Gaps and Phase Slip in Periodic Signings of `C_N(1,s)`**

Alternative title if the global sharp limit is closed:

**Sharp Quadratic Bloch Gaps for an Antipodal Family of Signed Circulants**

## Intended contribution package

The paper should be organized around one explicit primitive period-`4s`
family for every even jump `s`, rather than around the older period-eight
case.

Current rigorous package:

1. all-even primitive antipodal construction with `R_s<8`;
2. exact continuant/characteristic-polynomial reduction;
3. new two-sided quadratic gap
   `1/(6s(s+2)) <= 8-R_s <= 4 sin^2(pi/(s+2))`;
4. endpoint sharp asymptotic
   `s^2(8-rho(H_s(1))^2) -> pi^2`;
5. exact counterexample to the phase-zero conjecture at `s=10`;
6. finite comparison threshold improved from `O(s^(3/2))` repetitions to
   `O(s)`;
7. exact symbolic audit and an independent Lean formalization track for
   core algebraic inequalities.

The strongest desired addition before submission is the global sharp limit

` s^2(8-R_s) -> pi^2 `.

That result would turn the phase-slip phenomenon from a complication into a
central theorem: the maximizing phase is not exactly zero, but its drift is
small enough not to change the leading gap constant.

## Proposed theorem hierarchy

### Theorem A — all-even sub-eight family

State the primitive period-`4s` signing and prove `R_s<8` for every even
`s>=2` via chirality, the reduced threshold matrix and determinant positivity.

### Theorem B — quadratic-order gap

State

`1/(6s(s+2)) <= 8-R_s <= 4 sin^2(pi/(s+2))`.

The proof should emphasize the new ingredients:

- factorization of the threshold denominator into two Chebyshev channels;
- two-point mixture/covariance inequality;
- Pell-square derivative kernel;
- exact coefficient convolution retaining the cancellation lost in the
  earlier cubic estimate;
- inverse-trace lower bound for the least threshold eigenvalue.

### Theorem C — endpoint sharp constant

Prove

` s^2(8-rho(H_s(1))^2) -> pi^2 `.

Interpret the limiting equation as a soft-channel Dirichlet--Robin boundary
condition becoming asymptotically Neumann at the far endpoint.

### Proposition D — phase-zero failure

Give the exact `s=10` Sturm certificate:

- endpoint parameter `h=2`;
- interior parameter `h=19997/10000`;
- separator `y=317/40`;
- zero roots above the separator at the endpoint and one root above it at
  the interior phase.

This should be presented as an exact algebraic certificate, not numerical
sampling.

### Theorem E — global sharp limit (target)

Desired statement:

` s^2(8-R_s) -> pi^2 `.

Sufficient route:

- identify the two near-degenerate endpoint soft modes;
- derive a two-mode effective matrix for phase `phi=O(r^-2)`;
- prove the optimizer remains in that window;
- show the phase improvement is `o(r^-2)`.

A stronger second-order theorem may record the scaling of the phase slip and
the `r^-4` correction if it can be proved cleanly.

### Corollary F — finite signed-circulant comparison

For `N=4sL`, derive the explicit sufficient condition

`L > pi * sqrt(3 (s+2)(1+s^2)/(2s))`

for the antipodal family to beat both alternating holonomies.

## Section plan

1. **Introduction and positioning**
   - fixed-underlying-graph signing minimization;
   - signed circulants and the `C_n(1,2)` benchmark;
   - why the value `sqrt(8)` and the phase-slip phenomenon matter;
   - precise statement of what is and is not claimed about global optimal
     signings.
2. **Gauge, Bloch fibers and chiral reduction**
3. **Exact continuant determinant for even jumps**
4. **Positive generating functions and threshold positivity**
5. **Quadratic gap via the Pell derivative kernel**
6. **Endpoint `pi^2` asymptotics and the limiting Robin condition**
7. **Exact phase-slip counterexample**
8. **Small-phase effective theory and global sharp asymptotics**
9. **Finite-order consequences**
10. **Formal verification and reproducibility boundary**
11. **Literature comparison and open problems**

## Publication-strength boundary

The paper should not claim:

- a closed formula for the global minimum `m(N,s)` over all signings;
- that the period-`4s` family is globally optimal;
- that phase zero is the maximizing Bloch phase;
- novelty of general spectral-radius-two signed-graph theory;
- priority before the periodic/magnetic operator literature audit is
  completed.

A strong submission version should ideally contain Theorem E.  Without it,
the current package is still mathematically coherent but should be framed as
an explicit-family quantitative theory with an exact phase-slip phenomenon,
not as the final sharp classification.

## Formalization plan

The new Lean development remains separate from frozen `formal/TargetA`.
Suggested dependency order:

1. `CoreInequalities.lean` — algebraic factorization and two-point covariance;
2. `ChebyshevMixture.lean` — `B_i B_j <= 2 B_(i+j)` and mixture bound;
3. `PellKernel.lean` — Pell-square generating kernel and exponential bound;
4. `CoefficientConvolution.lean` — formal derivative coefficient estimate;
5. `TraceGap.lean` — abstract positive-definite inverse-trace bridge;
6. `QuadraticGapTheorem.lean` — assemble the analytic inequality once the
   matrix/determinant interfaces are formalized.

The exact Sturm `s=10` certificate can be formalized later either by a
verified polynomial certificate or by importing a generated exact witness;
it should not block the analytic Lean track.
