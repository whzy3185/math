# Manuscript architecture: sharp parity-resolved Bloch gaps in signed circulants

Date: 2026-09-06
Branch: `research/quadratic-gap-upgrade`

## Working title

**Sharp Quadratic Bloch Gaps for Explicit Signings of `C_N(1,s)` for All Jumps**

Alternative:

**Parity, Phase Slip, and Sharp `pi^2` Gaps in Signed Circulants**

## Core contribution package

The paper should be organized around the full jump parameter `s>=2`.
The parity mechanisms are different, but the leading asymptotic is now the
same and fully proved for the explicit family.

Current rigorous package:

1. an explicit periodic sub-eight signing for every integer jump `s>=2`;
2. parity-free quadratic envelope
   `1/(6s(s+2)) <= 8-Rhat_s <= 4 sin^2(pi/(s+2))`;
3. sharp parity-free asymptotic
   `s^2(8-Rhat_s) -> pi^2`;
4. odd `s`: exact Fourier dispersion, unique interior optimizer, Chebyshev
   critical equation, `O(s^-3)` phase localization;
5. even `s`: primitive period-`4s` antipodal defect family and exact
   continuant determinant;
6. even `s`: quadratic inverse-trace lower bound;
7. even `s`: exact `s=10` phase-zero counterexample;
8. even `s`: global phase localization and sharp `pi^2` limit despite the
   phase slip;
9. finite odd-jump coverage for every admissible even order `N`;
10. even finite comparison threshold improved from `O(s^(3/2))`
    repetitions to `O(s)`;
11. exact odd-order obstruction to the naive one-defect repair;
12. symbolic verification scripts and a separate Lean formalization track.

The leading asymptotic problem is therefore closed.  The strongest optional
addition before submission is now **second-order phase-slip asymptotics**, not
the leading constant.

## Proposed theorem hierarchy

### Theorem A — all-jump explicit sub-eight family

Define the parity-dependent construction:

- odd `s`: `tau_i=(-1)^i`, period two;
- even `s`: primitive period-`4s` antipodal word.

Prove `Rhat_s<8` for every integer `s>=2` and

`1/(6s(s+2)) <= 8-Rhat_s <= 4 sin^2(pi/(s+2))`.

### Theorem B — odd-jump exact model

For odd `s>=3`, prove

`M_s=max_theta [4+2 cos(2theta)-2 cos(2s theta)] < 8`

and

`8-M_s=4 min_theta [sin^2 theta+cos^2(s theta)]`.

Show the unique minimizer `theta_s` satisfies

`s U_(s-1)(cos(2 theta_s))=1`

and

`0 < pi/(2s)-theta_s <= pi^2/(4s^3)`.

Conclude

` s^2(8-M_s) -> pi^2. `

### Theorem C — all-even antipodal construction

Prove `R_s<8` for every even `s>=2` using chirality, reduced threshold
matrix, continuants and determinant positivity.

### Theorem D — even quadratic-order gap

Prove

`1/(6s(s+2)) <= 8-R_s <= 4 sin^2(pi/(s+2))`.

Main ingredients:

- two-Chebyshev factorization;
- two-point mixture/covariance inequality;
- Pell-square derivative kernel;
- coefficient convolution retaining the cancellation lost in the old cubic
  estimate;
- inverse-trace bridge.

### Theorem E — endpoint sharp constant

Prove

` s^2(8-rho(H_s(1))^2) -> pi^2 `

through even jumps, with the limiting soft-channel Robin equation.

### Proposition F — exact phase-zero failure

Give the `s=10` Sturm certificate with

- `h=2`;
- `h=19997/10000`;
- separator `y=317/40`.

This establishes a genuine phase slip, so the global sharp theorem cannot be
reduced to the endpoint theorem by a false phase-location claim.

### Theorem G — even global sharp limit

Prove

` s^2(8-R_s) -> pi^2  (s even). `

The proof architecture is:

1. choose a global root and write `mu=2-h`;
2. derive the exact hard-divided root equation;
3. prove `mu=O(r^-2)` using the explicit hyperbolic localization lemma;
4. rule out the hyperbolic soft scaling because the normalized limit would
   require `cosh x=0`;
5. in the oscillatory regime recover the endpoint Robin limit `cos x=0`;
6. obtain `r theta->pi/2`;
7. compare with the endpoint upper bound to force `r^2 mu->0`;
8. conclude `4r^2 g_(2r)->pi^2`.

The companion `GLOBAL_PI2_LOCALIZATION_LEMMA.md` supplies the delicate step
with explicit constants: `|R_r|<=2 sqrt(11)` and the factorization

`(p-lambda q)(p-lambda^(-1)q)/p`.

### Corollary H — sharp all-jump limit

Combine Theorems B and G:

` s^2(8-Rhat_s) -> pi^2 `

through all integer jumps.

This should be the final headline asymptotic theorem in the introduction.

### Corollary I — finite signed-circulant consequences

Odd `s`:

- every admissible even `N` is covered by the period-two word;
- both holonomy sectors have `rho^2<8`.

Even `s`:

- for `N=4sL`, the antipodal word gives `rho^2<8`;
- sufficient comparison threshold
  `L > pi * sqrt(3 (s+2)(1+s^2)/(2s))`.

### Proposition J — odd-order one-defect obstruction

At `(N,s)=(21,7)`, exact integer Rayleigh certificates show that all four
holonomy/anchor representatives of the cyclic one-`Q`-defect near-alternating
Ansatz satisfy `rho^2>8`.

This prevents the finite-order section from suggesting an invalid trivial
repair for odd `N`.

## Optional second-order theorem target

Numerics strongly suggest that for even `s=2r`, if
`h_r=2 cos(phi_r)` is globally optimizing and `e_r` is the endpoint gap,

`r^2 phi_r -> pi/(4 sqrt(2))`

and

`r^4(e_r-g_(2r)) -> pi^2/32`.

Equivalently, the conjectural effective law is

`g_(2r)(phi)=e_r+phi^2-(pi/(2sqrt2)) |phi|/r^2+o(r^-4)`.

This would be a valuable refinement, but the manuscript no longer depends on
it for a sharp leading theorem.

## Section plan

1. **Introduction and positioning**
2. **Gauge and universal squared-operator algebra**
3. **Odd jumps: exact Fourier model**
4. **Odd jumps: unique phase and sharp `pi^2` gap**
5. **Even jumps: antipodal chirality and reduced threshold matrix**
6. **Exact continuant determinant**
7. **Positive generating functions and threshold positivity**
8. **Even quadratic gap via the Pell derivative kernel**
9. **Endpoint `pi^2` asymptotics**
10. **Exact phase-slip counterexample**
11. **Global phase localization**
12. **Even global `pi^2` theorem**
13. **All-jump sharp corollary**
14. **Finite-order consequences and compatibility obstructions**
15. **Second-order phase-slip numerics/conjecture**
16. **Formal verification and reproducibility boundary**
17. **Literature comparison and open problems**

## Publication-strength boundary

The paper should not claim:

- a closed formula for `m(N,s)` over all signings;
- global optimality of the parity-dependent family;
- phase-zero maximality for even jumps;
- coverage of every order `N`;
- the second-order phase-slip constants as theorems;
- novelty or priority before the broader periodic/magnetic operator audit is
  completed.

The sharp all-`s` explicit-family theorem is already a complete central
result; second-order phase slip is an enhancement rather than a prerequisite.

## Formalization plan

The Lean development remains separate from frozen `formal/TargetA`.
Suggested dependency order:

1. `OddJumpCore.lean` — weighted-distance/Cauchy algebra;
2. `OddJumpTrig.lean` — trigonometric variational identity and monotonicity;
3. `OddJumpSharp.lean` — unique phase and sharp odd limit;
4. `CoreInequalities.lean` — even factorization and covariance;
5. `ChebyshevMixture.lean`;
6. `PellKernel.lean`;
7. `CoefficientConvolution.lean`;
8. `TraceGap.lean`;
9. `GlobalPhaseLocalization.lean` — hyperbolic coefficient factorization and
   endpoint localization;
10. `EvenGlobalPi2.lean` — limiting Robin argument;
11. `AllSTheorem.lean` — parity-free sharp assembly.

The exact Sturm and integer Rayleigh certificates can be formalized later as
finite algebraic witnesses and should not block the analytic Lean track.
