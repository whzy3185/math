# Lean verification status — AML weighted-damping stabilization

Date: 2026-09-10  
Branch: `research/aml-production-consumption-stabilization`  
Verified formal-tree commit: `b73db253fad60f65c31cff0f1f438096b10e6ec0`  
Successful GitHub Actions run: `34446453613` (run 147)  
Toolchain: Lean `v4.33.1`, mathlib revision `0df444a360eaa60ab8c11dca51a86af692955474`  
Build command: `lake build` from `formal/`  
Result: **SUCCESS — `Build completed successfully (8751 jobs)`**.  
Proof-hygiene gate: **SUCCESS** — CI rejects `sorry`, `admit`, and explicit user `axiom` declarations before compilation.

The verification root `formal/AMLStabilization.lean` now imports **44 AMLStabilization modules**.  Relative to the older strengthening note, the arbitrary-real-`q` weighted-damping chain is no longer merely represented by the `q=4` branch: the general coercivity, rate dichotomy, zero-energy branch, eventual finite-`L^p` exponent machinery, degenerate `theta` endpoint, superlinear-consumption specialization, exact rate optimization, signed sharpness formula, mass-conservation propagation, and dominated differentiation of the squared `L^2` energy are all present in the compiled tree.

## 1. Arbitrary-real-`q` weighted damping is kernel-checked

The following pieces are compiled for general real exponents rather than only a representative integer case:

- `WeightedHolderQ.lean`: weighted Holder with respect to a nonnegative finite-mass weight;
- `NonlinearCoercivityAlgebra.lean` and `NonlinearIntegralCoercivity.lean`: nonlinear mass-weighted coercivity for arbitrary real `q >= 2`;
- `GeneralSignalEnergyIdentityQ.lean`: arbitrary-order reaction dissipation and signal-energy inequality from named PDE/Green interfaces;
- `GeneralRateAssembly.lean`: fractional coercivity and `q/2`-power dissipation closure;
- `GeneralPolynomialEnergyDecay.lean`, `LocalPolynomialEnergyDecay.lean`, `ZeroEnergyBranch.lean`: arbitrary `q>2` Bihari decay including the natural nonnegative zero-energy branch;
- `GeneralQuadraticWeightedDampingFinal.lean`: quadratic/exponential endpoint;
- `GeneralWeightedDampingFinal.lean` and `GeneralWeightedDampingNonnegativeFinal.lean`: superquadratic/polynomial endpoint.

Thus the theorem-level dichotomy

```text
q = 2  -> exponential signal decay,
q > 2  -> polynomial signal decay
```

is represented in the Lean library at arbitrary real damping order, conditional only on the explicitly named geometric/PDE identities at the analytic boundary.

## 2. Degenerate kinetics now match the manuscript parameter `theta`

`DegenerateWeightedDampingFinal.lean` specializes the general theorem to

```text
q = theta + 2,   theta > 0,
```

and exposes the decay directly in manuscript variables.  The energy exponent is kernel-checked as `2/theta`, and the square-root signal `L^2` exponent as `1/theta`.

`AttractorDissipativityCore.lean` has also been strengthened.  If on a compact invariant signal set

```text
F(s) = -h(s) (s-v_*) |s-v_*|^theta,
h(s) > 0,
```

with continuous `h`, Lean obtains a quantitative `beta>0` and proves

```text
(s-v_*) F(s) <= -beta |s-v_*|^(theta+2).
```

This formalizes the structural mechanism that allows `F'(v_*)=0`; it is not restricted to shifted linear consumption.

## 3. Eventual finite-`L^p` exponent layer and the exact full-rate threshold

The compiled exponent layer now contains:

- `LpExponentCore.lean`: an admissible spatial exponent `r`, Holder partner `s`, the exact relation `1/r = 1/p + 1/s`, and positivity of the transfer rate;
- `LpFiniteMeasureCore.lean`: finite-measure `L^p -> L^2` transfer;
- `LpProductCore.lean`: actual `MemLp` product transfer for the Holder exponents;
- `BoundedInterpolationCore.lean`: bounded interpolation with exponential and polynomial rate propagation;
- `MixedNormExponentCore.lean`: an explicit finite time exponent

```text
Q = 4 p / (p-n)
```

satisfying `Q>2` and `n/p + 2/Q < 1` whenever `p>max{n,2}`.  The same module proves the one-dimensional cylinder-lift specialization: after lifting to effective dimension two, the hypothesis `p>2` is enough;
- `LpRateOptimization.lean`: for every

```text
0 < mu < (1/theta) * min {1, 2(p-n)/(pn)},
```

Lean constructs an admissible `r` for which

```text
mu < 2(p-r)/(theta p r).
```

This is the exact optimization step behind the polynomial full-stabilization threshold stated in the manuscript, rather than only positivity of one transfer exponent.

## 4. Cell-energy and full-rate assembly

The scalar/parabolic-rate bookkeeping remains compiled through:

- `CellEnergyCore.lean`, `ForcedEnergyDecay.lean`, `PolynomialForcedEnergyDecay.lean`, and `CellEnergyAssembly.lean`;
- `RateComparisonCore.lean` and `CellEnergyEnvelope.lean`;
- `RateRootCore.lean`;
- `FullStabilizationAssembly.lean`.

Consequently, once the named signal `W^{1,infinity}` smoothing estimate and Choi-type local boundedness estimate are supplied, Lean propagates the signal rate through coefficient forcing, cell `L^2` energy, square-root norm conversion, and the final cell `L^infinity` rate for both exponential and polynomial branches.

This is a **kernel-checked full rate assembly conditional on the deep analytic interfaces**.  It is not a claim that those arbitrary-domain parabolic regularity theorems themselves have been formalized.

## 5. Concrete superlinear-consumption application

`SuperlinearConsumptionCore.lean` proves for real `ell>1`

```text
F(s) = -s |s|^(ell-1),
s F(s) = -|s|^(ell+1).
```

`SuperlinearConsumptionSignalFinal.lean` now feeds this identity directly into the arbitrary-`q` weighted-damping theorem with `q=ell+1`.  Thus the superlinear-consumption application is no longer represented only by an isolated reaction identity: its polynomial signal-rate specialization is a compiled endpoint theorem under the same named geometric/PDE interfaces as the abstract result.

For the manuscript model `v_t = Delta v - u v^m`, one sets `ell=m`, so `q-2=m-1` and the signal norm exponent is `1/(m-1)`.

## 6. Sharpness has been upgraded to arbitrary sign

`SharpnessCore.lean` retains the positive homogeneous profile and its exact ODE derivative identity.

`SignedSharpnessCore.lean` adds the signed profile for every nonzero initial deviation `w0`, proves recovery of the initial value, and kernel-checks the exact absolute-value formula

```text
|w(t)| = (|w0|^(-theta) + theta*k*t)^(-1/theta),
```

including the manuscript substitution `k = kappa * ubar`.

Therefore the sharp signal order `t^(-1/theta)` is represented in Lean with the same absolute-value formula stated in the paper, not only on the `w0>0` branch.

## 7. Two former calculus interfaces have been reduced

`MassConservationCore.lean` proves that a differentiable scalar mass functional with zero derivative is constant, and propagates an initial positive integral mass to a fixed positive mass at all times.  The remaining PDE-specific task is to derive the zero derivative from the divergence-form equation and the Neumann boundary condition.

`EnergyDifferentiationCore.lean` uses mathlib's dominated parametric-integral differentiation theorem to prove

```text
d/dt integral w(t,x)^2 dx = 2 integral w(t,x) w_t(t,x) dx
```

under standard local measurability, integrability, domination, and pointwise time-differentiability hypotheses.  Thus differentiation under the integral is no longer an opaque algebraic interface; what remains is verifying these hypotheses from the concrete classical PDE solution.

## 8. Final CI evidence

GitHub Actions run `34446453613` (run 147), at formal-tree commit
`b73db253fad60f65c31cff0f1f438096b10e6ec0`, records:

- checkout of exactly that commit;
- `Reject placeholders and explicit axioms`: **SUCCESS**;
- successful compilation of `EnergyDifferentiationCore`;
- successful compilation of `MassConservationCore`;
- successful compilation of `MixedNormExponentCore`;
- successful compilation of `LpRateOptimization`;
- successful compilation of `AttractorDissipativityCore`;
- successful compilation of `SignedSharpnessCore`;
- successful compilation of `SuperlinearConsumptionSignalFinal`;
- successful compilation of `DegenerateWeightedDampingFinal`;
- successful compilation of the root `AMLStabilization` target;
- **`Build completed successfully (8751 jobs)`**.

The root imports **44 modules**, all compiled under the pinned Lean/mathlib toolchain.

## 9. What still prevents a literal arbitrary-smooth-domain PDE formalization

It would still be inaccurate to write that the entire chemotaxis PDE theorem on an arbitrary smooth bounded domain has been formalized from first principles.  The genuinely remaining analytic infrastructure is concentrated in the following areas:

1. geometric Poincare theory in the manuscript's exact Sobolev setting on an arbitrary smooth bounded connected domain;
2. Neumann Green/integration-by-parts identities on that domain, including the PDE-specific flux identity needed to derive zero mass derivative;
3. the invariant signal interval / maximum-principle argument for the concrete system;
4. Neumann heat-semigroup `L^p -> W^{1,infinity}` smoothing on the required domains;
5. Choi's mixed-norm conormal/local boundedness estimate in the required arbitrary-domain implementation;
6. the concrete function-space derivation of the cell-density PDE energy identity.

The calculus part of differentiating the squared `L^2` energy and the scalar propagation part of mass conservation are now Lean-proved; only their PDE-specific analytic hypotheses remain to be connected.

A targeted mathlib audit in this formalization pass found no ready-made theorems matching the required arbitrary-smooth-domain analytic Poincare inequality, Neumann heat-semigroup smoothing, parabolic maximum principle, or Choi conormal estimate.  Mathlib does provide a parametric-integral differentiation theorem, which is now used in `EnergyDifferentiationCore`; its divergence-theorem infrastructure located in the audit is not the arbitrary smooth Neumann-domain package required here.

## 10. Correct provenance statement

> **Strengthened Lean verification (current formal-tree level):** the novel arbitrary-real-order weighted-damping machinery — genuine weighted Holder, nonlinear mass-weighted coercivity, quadratic/exponential versus superquadratic/polynomial signal endpoints, the nonnegative zero-energy branch, degenerate `theta` specialization, exact eventual finite-`L^p` exponent and rate-threshold arithmetic, mixed-norm time-exponent selection including the one-dimensional lift, superlinear-consumption signal specialization, signed sharpness formula, scalar mass-conservation propagation, dominated differentiation of the squared `L^2` energy, forced cell-energy decay, energy-to-norm conversion, and final exponential/polynomial rate assembly conditional on explicitly named Neumann-semigroup/Choi/geometric PDE inputs — is kernel-checked in Lean 4/mathlib.  CI rejects `sorry`, `admit`, and explicit user axioms.  The remaining arbitrary-smooth-domain Neumann PDE geometry and regularity infrastructure is not claimed to be Lean-verified.
