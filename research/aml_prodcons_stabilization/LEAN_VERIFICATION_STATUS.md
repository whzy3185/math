# Lean verification status — AML weighted-damping stabilization

Date: 2026-09-11  
Branch: `research/aml-production-consumption-stabilization`  
Verified formal-tree commit: `f7382928cdd5f525724cc18596dfde56b25c5ac3`  
Successful GitHub Actions run: `34559739511` (run 237)  
Toolchain: Lean `v4.33.1`, mathlib revision `0df444a360eaa60ab8c11dca51a86af692955474`  
Build command: `lake build` from `formal/`  
Result: **SUCCESS — `Build completed successfully (8780 jobs)`**.  
Proof-hygiene gate: **SUCCESS** — CI rejects `sorry`, `admit`, and explicit user `axiom` declarations before compilation.

The verification root `formal/AMLStabilization.lean` now imports **73 AMLStabilization modules**. The formal tree now contains the arbitrary-real-order weighted-damping/rate machinery, exact finite-`L^p` rate optimization, signed sharpness, dominated energy differentiation, box divergence/Green/mass conservation, local maximum-principle contact machinery, time-dependent box signal-energy identities, and a genuine multi-dimensional rectangular-box Poincare theorem wired directly into the mass-weighted coercivity chain.

## 1. Arbitrary-real-`q` weighted damping is kernel-checked

The following pieces are compiled for general real exponents rather than only a representative integer case:

- `WeightedHolderQ.lean`: weighted Holder with respect to a nonnegative finite-mass weight;
- `NonlinearCoercivityAlgebra.lean` and `NonlinearIntegralCoercivity.lean`: nonlinear mass-weighted coercivity for arbitrary real `q >= 2`;
- `GeneralSignalEnergyIdentityQ.lean`: arbitrary-order reaction dissipation and signal-energy inequality;
- `GeneralRateAssembly.lean`: fractional coercivity and `q/2`-power dissipation closure;
- `GeneralPolynomialEnergyDecay.lean`, `LocalPolynomialEnergyDecay.lean`, `ZeroEnergyBranch.lean`: arbitrary `q>2` Bihari decay including the zero-energy branch;
- `GeneralQuadraticWeightedDampingFinal.lean`: quadratic/exponential endpoint;
- `GeneralWeightedDampingFinal.lean` and `GeneralWeightedDampingNonnegativeFinal.lean`: superquadratic/polynomial endpoint.

Thus the theorem-level dichotomy

```text
q = 2  -> exponential signal decay,
q > 2  -> polynomial signal decay
```

is represented in Lean at arbitrary real damping order.

## 2. Degenerate kinetics and exact manuscript rate threshold

`DegenerateWeightedDampingFinal.lean` specializes to `q = theta + 2`, `theta > 0`, with energy exponent `2/theta` and signal `L^2` exponent `1/theta`.

`AttractorDissipativityCore.lean` proves quantitative dissipativity from

```text
F(s) = -h(s) (s-v_*) |s-v_*|^theta,
h(s) > 0
```

on a compact signal range, so the formal mechanism allows `F'(v_*)=0` and is not restricted to shifted affine consumption.

`LpRateOptimization.lean` kernel-checks the exact manuscript threshold: for every

```text
0 < mu < (1/theta) * min {1, 2(p-n)/(pn)},
```

an admissible exponent `r` is constructed with

```text
mu < 2(p-r)/(theta p r).
```

`MixedNormExponentCore.lean` provides the explicit finite time exponent

```text
Q = 4p/(p-n),
```

with `Q>2` and `n/p + 2/Q < 1`, including the one-dimensional cylinder-lift specialization.

## 3. Concrete superlinear consumption and sharpness

`SuperlinearConsumptionSignalFinal.lean` specializes the arbitrary-order theorem to

```text
F(s) = -s |s|^(m-1),
q = m+1,
```

so the signal exponent is `1/(m-1)`.

`SignedSharpnessCore.lean` kernel-checks, for nonzero signed initial deviation,

```text
|w(t)| = (|w0|^(-theta) + theta*k*t)^(-1/theta),
```

including `k = kappa * ubar`. This verifies the exact sharp ODE profile used in the manuscript. The remaining PDE-level sharpness step is the uniqueness/invariance argument identifying spatially constant PDE data with that ODE solution.

## 4. Time differentiation, box mass conservation, and Green identity are derived

`EnergyDifferentiationCore.lean` uses mathlib's parametric-integral differentiation theorem to prove

```text
d/dt integral w(t,x)^2 dx = 2 integral w(t,x) w_t(t,x) dx
```

under local dominated-differentiation hypotheses.

`BoxNeumannFluxCore.lean` uses mathlib's Bochner divergence theorem on rectangular boxes to prove:

- zero face flux implies zero integral of the divergence;
- dominated differentiation of the spatial mass integral;
- `u_t = div J` plus zero face flux implies exact mass conservation;
- zero normal derivative plus the local product rule implies Green's first identity.

`ProductRuleGreenCore.lean` and `CanonicalBoxGreenCore.lean` push the Green identity down to local Frechet/product-rule data rather than assuming the global integration-by-parts formula.

## 5. Signal-energy PDE interfaces are reduced on boxes

`SignalPDEPairingCore.lean` derives the integrated PDE pairing from the pointwise PDE and integrability rather than taking the pairing identity as an input.

`BoxSignalEnergyCore.lean` combines pointwise PDE data with the canonical box Green identity.

`TimeDependentBoxSignalEnergyCore.lean` additionally generates

```text
d/dt integral w^2 = 2 integral w w_t
```

internally from dominated differentiation. On boxes, the signal-energy chain therefore no longer requires opaque `hEnergyDerivative`, `hPDEPairing`, or global Green assumptions.

## 6. Rectangular-box Poincare is now fully derived

The box Poincare chain is no longer an abstract tensorization interface. The compiled modules are:

- `BoxPoincareCore.lean`: one-dimensional `[0,h]` weak `L^2` Poincare from FTC;
- `IntervalPoincareShiftCore.lean`: arbitrary interval `[a,b]`;
- `IntervalPairPoincareCore.lean`: independent-double-copy interval estimate;
- `ProductVarianceCore.lean`: probability and finite-measure double-copy variance identities;
- `CoordinateTelescopingCore.lean` and `IntegratedCoordinateTelescopingCore.lean`: finite-coordinate hybrid Cauchy-Schwarz telescoping, pointwise and integrated;
- `BoxProductMeasureCore.lean`, `PairedProductMeasureCore.lean`, `PairedSelectorMeasureCore.lean`, `RestHybridMeasureCore.lean`, and `PiCoordinateFubiniCore.lean`: product-measure, paired-coordinate, selector, and Fubini bookkeeping;
- `HybridFiberCore.lean` and `BoxHybridFiberPoincareCore.lean`: identification and estimate of a single coordinate hybrid increment;
- `BoxVolumeFactorCore.lean`: exact side-length and rest-volume factor identities;
- `FullBoxPoincareCore.lean`: final multi-dimensional theorem.

For a nondegenerate rectangular box of dimension `N=n+1`, if every side length is at most `C`, Lean proves

```text
integral |f-fbar|^2 <= N * C^2 * sum_i integral |partial_i f|^2.
```

No external `hVarianceDecomp` or geometric `hPoincare` assumption occurs in this final box theorem.

`FullBoxPoincareSqrtCore.lean` exposes the square-root form with effective constant

```text
Cp = sqrt(N) * C.
```

## 7. Box Poincare is wired into mass-weighted coercivity

`FullBoxCoercivityBridge.lean` proves `integralMassWeightedCoercivity_on_rectangularBox`.

This theorem internally constructs:

- the rectangular-box volume;
- the integral mean;
- the Poincare estimate with `Cp = sqrt(N) * C`;
- the exact mean-square decomposition;
- the gradient energy as the sum of coordinate derivative energies.

It then feeds those results into `integralMassWeightedCoercivity_of_MemLp_and_Poincare`.

Therefore, **on rectangular boxes the mass-weighted coercivity layer no longer asks the caller for either a variance-decomposition hypothesis or a geometric Poincare hypothesis**. The remaining assumptions at that theorem are the genuinely weight-dependent `rho` mass/`L^2`/weighted-integrability data and the regularity/integrability needed to instantiate the box Poincare theorem.

## 8. Maximum-principle core has been pushed below the reaction-sign interface

The compiled tree contains:

- `InvariantRangeCore.lean`: reaction-sign preservation algebra;
- `SpatialExtremumSecondDerivativeCore.lean`: spatial extremum gives the expected Hessian/Laplacian sign;
- `MaximumPrincipleContactCore.lean`: combines contact sign, Laplacian sign, and PDE data;
- `FirstContactBarrierCore.lean`: epsilon-tilted first-contact time barrier.

Thus the local contradiction mechanism behind the parabolic maximum principle is kernel-checked. What is not yet claimed is the complete global-in-time first-contact selection theorem for a continuous PDE solution on an arbitrary smooth Neumann domain.

## 9. Full rate assembly remains kernel-checked

The cell/rate tree remains compiled through:

- `CellEnergyCore.lean`, `ForcedEnergyDecay.lean`, `PolynomialForcedEnergyDecay.lean`, `CellEnergyAssembly.lean`;
- `RateComparisonCore.lean`, `CellEnergyEnvelope.lean`, `RateRootCore.lean`;
- `FullStabilizationAssembly.lean`.

Consequently, once the named signal `W^{1,infinity}` smoothing estimate and Choi-type local boundedness estimate are supplied, Lean propagates the signal rate through coefficient forcing, cell `L^2` energy, square-root conversion, and final cell `L^infinity` rate for both exponential and polynomial branches.

## 10. Final CI evidence

GitHub Actions run `34559739511` (run 237), at formal-tree commit
`f7382928cdd5f525724cc18596dfde56b25c5ac3`, records:

- checkout of exactly that commit;
- `Reject placeholders and explicit axioms`: **SUCCESS**;
- successful compilation of `BoxVolumeFactorCore`, `BoxHybridFiberPoincareCore`, `FullBoxPoincareCore`, `FullBoxPoincareSqrtCore`, and `FullBoxCoercivityBridge`;
- successful compilation of the root `AMLStabilization` target;
- **`Build completed successfully (8780 jobs)`**.

The root imports **73 AMLStabilization modules**, all compiled under the pinned Lean/mathlib toolchain.

## 11. What still prevents a literal arbitrary-smooth-domain PDE formalization

It would still be inaccurate to say that the entire manuscript theorem on an arbitrary smooth bounded Neumann domain is formalized from first principles. The remaining genuinely deep infrastructure is now concentrated in:

1. extension of the now-verified rectangular-box Poincare/divergence/Green/trace machinery to arbitrary smooth bounded connected Neumann domains;
2. a global parabolic maximum-principle/invariant-range theorem for the concrete system, beyond the already verified local extremum/contact/barrier core;
3. Neumann heat-semigroup `L^p -> W^{1,infinity}` smoothing on the required arbitrary domains;
4. Choi's mixed-norm conormal/local boundedness theorem in the required arbitrary-domain setting;
5. the concrete function-space derivation of the cell-density PDE energy identity;
6. PDE uniqueness/invariance for the spatially homogeneous sharpness reduction.

The rectangular-box geometric Poincare input is **no longer part of this unresolved list**: it is now derived and connected to coercivity in Lean.

## 12. Correct provenance statement

> **Strengthened Lean verification (current formal-tree level):** the arbitrary-real-order weighted-damping machinery — weighted Holder, nonlinear mass-weighted coercivity, quadratic/exponential versus superquadratic/polynomial signal endpoints, zero-energy branch, degenerate `theta` specialization, exact eventual finite-`L^p` exponent and rate-threshold arithmetic, mixed-norm time-exponent selection including the one-dimensional lift, superlinear-consumption specialization, signed sharpness, dominated time differentiation, forced cell-energy decay, energy-to-norm conversion, and final exponential/polynomial rate assembly conditional on explicitly named deep parabolic inputs — is kernel-checked in Lean 4/mathlib. On rectangular boxes, the conservative zero-flux identity, exact mass conservation, Green's first identity, a genuine finite-dimensional `L^2` Poincare inequality, its `Cp = sqrt(N) C` square-root form, and the resulting mass-weighted coercivity bridge are all derived rather than assumed. CI rejects `sorry`, `admit`, and explicit user axioms. The remaining gap is the arbitrary-smooth-domain geometric/parabolic extension together with the global maximum principle, Neumann semigroup, Choi, cell-energy, and PDE-uniqueness infrastructure.
