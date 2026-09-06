# Manuscript architecture: sharp parity-resolved Bloch gaps in signed circulants

Date: 2026-09-06
Branch: `research/quadratic-gap-upgrade`

## Working title

**Sharp Quadratic Bloch Gaps and Phase Slip for Explicit Signings of `C_N(1,s)`**

Alternative:

**Parity, Phase Slip, and Sharp `pi^2` Gaps in Signed Circulants**

## Core contribution package

The manuscript is organized around the full jump parameter `s>=2`.  The
parity mechanisms differ, but the leading asymptotic is the same and the even
phase slip is now quantified one order further.

Current rigorous package:

1. explicit periodic sub-eight signings for every integer jump `s>=2`;
2. parity-free quadratic envelope
   `1/(6s(s+2)) <= 8-Rhat_s <= 4 sin^2(pi/(s+2))`;
3. sharp parity-free asymptotic `s^2(8-Rhat_s)->pi^2`;
4. odd `s`: exact Fourier dispersion, unique optimizer, Chebyshev critical
   equation, and sharp `pi^2` limit;
5. even `s`: primitive period-`4s` antipodal defect family and exact
   continuant determinant;
6. even quadratic inverse-trace lower bound;
7. exact `s=10` phase-zero counterexample;
8. global even phase localization and sharp `pi^2` limit;
9. **second-order even phase slip**
   `r^2 phi_r -> pi/(4sqrt2)` and
   `r^4(e_r-g_(2r))->pi^2/32`;
10. effective boundary-layer law
    `r^4(g_(2r)(z/r^2)-e_r) -> z^2-(pi/(2sqrt2))z`;
11. finite odd-jump coverage for every admissible even `N`;
12. even finite comparison threshold improved from `O(s^(3/2))` to `O(s)`;
13. exact odd-order obstruction to the naive one-defect repair;
14. symbolic/numerical verification scripts and a separate Lean track.

The leading and second-order explicit-family asymptotics are therefore closed.

## Proposed theorem hierarchy

### Theorem A — all-jump explicit sub-eight family

Define the parity-dependent construction:

- odd `s`: `tau_i=(-1)^i`, period two;
- even `s`: primitive period-`4s` antipodal word.

Prove `Rhat_s<8` for every `s>=2` and the common quadratic envelope.

### Theorem B — odd-jump exact model

For odd `s>=3`, derive the exact dispersion, prove uniqueness of the interior
optimizer, obtain

`s U_(s-1)(cos(2 theta_s))=1`,

localize it to `O(s^-3)` around `pi/(2s)`, and conclude

` s^2(8-M_s)->pi^2. `

### Theorem C — all-even antipodal construction

Prove `R_s<8` for every even `s>=2` using chirality, the reduced threshold
matrix, continuants, and determinant positivity.

### Theorem D — even quadratic-order gap

Prove

`1/(6s(s+2)) <= 8-R_s <= 4 sin^2(pi/(s+2))`.

Main ingredients: two-Chebyshev factorization, covariance/mixture inequality,
Pell-square derivative kernel, coefficient convolution, inverse trace.

### Theorem E — endpoint sharp constant

Prove

` s^2(8-rho(H_s(1))^2)->pi^2 `

through even jumps, with the limiting Robin equation.

### Proposition F — exact phase-zero failure

Give the exact `s=10` Sturm certificate.  This forces the global theory to
control a phase boundary layer rather than identify the endpoint as exact.

### Theorem G — even global sharp limit

Prove

` s^2(8-R_s)->pi^2  (s even). `

Use the explicit hyperbolic localization lemma, exclude the hyperbolic soft
limit, recover the oscillatory Robin root, and force the phase mass to be
lower order by endpoint comparison.

### Theorem H — second-order even phase slip

For `s=2r`, if `h_r=2 cos(phi_r)` is globally optimizing and `e_r` is the
phase-zero gap, prove

`r^2 phi_r -> pi/(4 sqrt(2))`

and

`r^4(e_r-g_(2r)) -> pi^2/32`.

The proof should be presented as a two-branch avoided crossing:

1. subtract the endpoint and global hard-divided root equations;
2. bootstrap global optimality to `mu=2-h=O(r^-4)`;
3. extract the phase square-root term `2 lambda^-1 sqrt(mu)`;
4. divide by the Robin slope `1-lambda^-2`;
5. obtain the exact displacement coefficient `1/(2sqrt2)`;
6. derive the effective parabola
   `z^2-(pi/(2sqrt2))z`;
7. minimize it to obtain both constants.

`SECOND_ORDER_LOCAL_IMPLICIT_LEMMA.md` should be cited for the quantitative
bootstrap rather than leaving the scale as a guessed ansatz.

### Corollary I — sharp all-jump limit

Combine odd and even subsequences:

` s^2(8-Rhat_s)->pi^2 `.

### Corollary J — finite signed-circulant consequences

Odd `s`: every admissible even `N` is covered by period two.

Even `s`: for `N=4sL`, use the antipodal word and the explicit linear-in-`s`
sufficient repetition threshold.

### Proposition K — odd-order one-defect obstruction

At `(N,s)=(21,7)`, exact integer Rayleigh certificates exclude the cyclic
one-defect near-alternating Ansatz in all four holonomy/anchor sectors.

## Section plan

1. Introduction and positioning
2. Gauge and universal squared-operator algebra
3. Odd jumps: exact Fourier model
4. Odd jumps: unique phase and sharp `pi^2` gap
5. Even jumps: antipodal chirality and reduced threshold matrix
6. Exact continuant determinant
7. Positive generating functions and threshold positivity
8. Even quadratic gap via the Pell derivative kernel
9. Endpoint `pi^2` asymptotics
10. Exact phase-slip counterexample
11. Global phase localization
12. Even global `pi^2` theorem
13. **Second-order avoided crossing and phase-slip asymptotics**
14. All-jump sharp corollary
15. Finite-order consequences and compatibility obstructions
16. Formal verification and reproducibility boundary
17. Literature comparison and open problems

## Publication-strength boundary

The paper should not claim:

- a closed formula for `m(N,s)` over all signings;
- global optimality of the parity-dependent family;
- phase-zero maximality for even jumps;
- coverage of every order `N`;
- higher-order phase-slip coefficients beyond those proved here;
- novelty or priority before the broader periodic/magnetic operator audit is
  completed.

## Formalization plan

The Lean development remains separate from frozen `formal/TargetA`.
Suggested dependency order:

1. `OddJumpCore.lean`;
2. `OddJumpTrig.lean`;
3. `OddJumpSharp.lean`;
4. `CoreInequalities.lean`;
5. `ChebyshevMixture.lean`;
6. `PellKernel.lean`;
7. `CoefficientConvolution.lean`;
8. `TraceGap.lean`;
9. `GlobalPhaseLocalization.lean`;
10. `EvenGlobalPi2.lean`;
11. `SecondOrderBootstrap.lean`;
12. `PhaseSlipConstants.lean`;
13. `AllSTheorem.lean`.

Exact Sturm and integer Rayleigh certificates can be formalized later as
finite algebraic witnesses and should not block the analytic Lean track.
