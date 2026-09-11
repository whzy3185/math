# Lean verification status — AML weighted-damping stabilization

Date: 2026-09-11  
Branch: `research/aml-production-consumption-stabilization`  
Verified formal-tree commit: `29edbb1d97ecc9b0409b8b13bbfc51c3b18eea84`  
Successful GitHub Actions run: `34564427878` (run 254)  
Toolchain: Lean `v4.33.1`, mathlib revision `0df444a360eaa60ab8c11dca51a86af692955474`  
Build command: `lake build` from `formal/`  
Result: **SUCCESS — `Build completed successfully (8786 jobs)`**.  
Proof-hygiene gate: **SUCCESS** — CI rejects `sorry`, `admit`, and explicit user `axiom` declarations before compilation.

The verification root `formal/AMLStabilization.lean` now imports **79 AMLStabilization modules**. The formal tree contains the arbitrary-real-order weighted-damping/rate machinery, exact eventual finite-`L^p` rate optimization, signed sharpness, dominated energy differentiation, box divergence/Green/mass conservation, a fully derived finite-dimensional box Poincare theorem, a direct box mass-weighted coercivity bridge, and now a **global Neumann maximum-principle/invariant-range theorem on rectangular boxes**, including face, edge, and corner contacts.

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

including `k = kappa * ubar`. The remaining PDE-level sharpness step is the uniqueness/invariance argument identifying spatially constant PDE data with that ODE solution.

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

## 6. Rectangular-box Poincare is fully derived

The compiled box Poincare chain contains:

- `BoxPoincareCore.lean`: one-dimensional `[0,h]` weak `L^2` Poincare from FTC;
- `IntervalPoincareShiftCore.lean`: arbitrary interval `[a,b]`;
- `IntervalPairPoincareCore.lean`: independent-double-copy interval estimate;
- `ProductVarianceCore.lean`: probability and finite-measure double-copy variance identities;
- `CoordinateTelescopingCore.lean` and `IntegratedCoordinateTelescopingCore.lean`: finite-coordinate hybrid Cauchy-Schwarz telescoping;
- `BoxProductMeasureCore.lean`, `PairedProductMeasureCore.lean`, `PairedSelectorMeasureCore.lean`, `RestHybridMeasureCore.lean`, and `PiCoordinateFubiniCore.lean`: product-measure/Fubini bookkeeping;
- `HybridFiberCore.lean` and `BoxHybridFiberPoincareCore.lean`: single-coordinate hybrid increment estimate;
- `BoxVolumeFactorCore.lean`: exact side-length/rest-volume factor identities;
- `FullBoxPoincareCore.lean`: final multi-dimensional theorem;
- `FullBoxPoincareSqrtCore.lean`: square-root norm form.

For a nondegenerate rectangular box of dimension `N=n+1`, if every side length is at most `C`, Lean proves

```text
integral |f-fbar|^2 <= N * C^2 * sum_i integral |partial_i f|^2,
```

and hence the effective Poincare constant

```text
Cp = sqrt(N) * C.
```

No external `hVarianceDecomp` or geometric `hPoincare` assumption occurs in this final box theorem.

## 7. Box Poincare is wired into mass-weighted coercivity

`FullBoxCoercivityBridge.lean` proves `integralMassWeightedCoercivity_on_rectangularBox`.

This theorem internally constructs the box volume, integral mean, Poincare estimate, exact mean-square decomposition, and coordinate-gradient energy, then feeds those results into the general mass-weighted coercivity theorem.

Therefore, **on rectangular boxes the mass-weighted coercivity layer no longer asks the caller for either a variance-decomposition hypothesis or a geometric Poincare hypothesis**. The remaining assumptions at that theorem are the genuinely weight-dependent `rho` data and the regularity/integrability needed to instantiate the box Poincare theorem.

## 8. Global Neumann maximum principle is now derived on boxes

The previous local contact machinery has now been completed into a global rectangular-box invariant-range theorem.

The compiled chain is:

- `InvariantRangeCore.lean`: dissipativity gives the correct inward reaction sign;
- `SpatialExtremumSecondDerivativeCore.lean`: ordinary interior extrema give the Hessian/Laplacian trace sign;
- `MaximumPrincipleContactCore.lean`: combines Laplacian, reaction, and PDE signs;
- `FirstContactBarrierCore.lean`: epsilon-tilted past-contact time derivative contradiction;
- `GlobalBoxContactSelectionCore.lean`: compact space-time cylinder selection of a tilted global contact point;
- `BoxInteriorContactCore.lean` and `GlobalBoxInteriorMaximumPrincipleCore.lean`: complete interior-contact version;
- `NeumannEndpointSecondDerivativeCore.lean`: one-dimensional endpoint maximum/minimum plus `f'=0` implies the correct second-derivative sign, proved via derivative-sign neighborhoods and the mean-value theorem;
- `BoxNeumannMaximumContactCore.lean`: applies those endpoint lemmas coordinatewise, so face/edge/corner extrema have the correct Laplacian trace sign under coordinate-face Neumann conditions;
- `GlobalBoxNeumannMaximumPrincipleCore.lean`: global upper/lower invariant bounds and the two-sided invariant interval on a nondegenerate rectangular box.

Thus, for the box problem `z_t = Delta z + rho F(z)` with nonnegative `rho`, dissipative `F`, and coordinate-face Neumann conditions, the formal tree now proves preservation of the signal interval from initial data. **The box-level invariant-range/maximum-principle hypothesis is no longer external.**

## 9. Full rate assembly remains kernel-checked

The cell/rate tree remains compiled through:

- `CellEnergyCore.lean`, `ForcedEnergyDecay.lean`, `PolynomialForcedEnergyDecay.lean`, `CellEnergyAssembly.lean`;
- `RateComparisonCore.lean`, `CellEnergyEnvelope.lean`, `RateRootCore.lean`;
- `FullStabilizationAssembly.lean`.

Consequently, once the named signal `W^{1,infinity}` smoothing estimate and Choi-type local boundedness estimate are supplied, Lean propagates the signal rate through coefficient forcing, cell `L^2` energy, square-root conversion, and final cell `L^infinity` rate for both exponential and polynomial branches.

## 10. Final CI evidence

GitHub Actions run `34564427878` (run 254), at formal-tree commit
`29edbb1d97ecc9b0409b8b13bbfc51c3b18eea84`, records:

- checkout of exactly that commit;
- `Reject placeholders and explicit axioms`: **SUCCESS**;
- successful compilation of `NeumannEndpointSecondDerivativeCore`;
- successful compilation of `BoxNeumannMaximumContactCore`;
- successful compilation of `GlobalBoxContactSelectionCore`;
- successful compilation of `GlobalBoxInteriorMaximumPrincipleCore`;
- successful compilation of `GlobalBoxNeumannMaximumPrincipleCore`;
- successful compilation of the root `AMLStabilization` target;
- **`Build completed successfully (8786 jobs)`**.

The root imports **79 AMLStabilization modules**, all compiled under the pinned Lean/mathlib toolchain.

## 11. What still prevents a literal arbitrary-smooth-domain PDE formalization

It would still be inaccurate to say that the entire manuscript theorem on an arbitrary smooth bounded Neumann domain is formalized from first principles. The genuinely remaining infrastructure is now concentrated in:

1. extension of the now-verified rectangular-box Poincare/divergence/Green/Neumann-maximum-principle machinery to arbitrary smooth bounded connected Neumann domains and traces;
2. Neumann heat-semigroup `L^p -> W^{1,infinity}` smoothing on the required arbitrary domains;
3. Choi's mixed-norm conormal/local boundedness theorem in the required arbitrary-domain setting;
4. the concrete function-space derivation of the cell-density PDE energy identity;
5. PDE uniqueness/invariance for the spatially homogeneous sharpness reduction.

The rectangular-box geometric Poincare input and the rectangular-box global invariant-range/maximum-principle input are **no longer part of the unresolved list**.

## 12. Correct provenance statement

> **Strengthened Lean verification (current formal-tree level):** the arbitrary-real-order weighted-damping machinery — weighted Holder, nonlinear mass-weighted coercivity, quadratic/exponential versus superquadratic/polynomial signal endpoints, zero-energy branch, degenerate `theta` specialization, exact eventual finite-`L^p` exponent and rate-threshold arithmetic, mixed-norm time-exponent selection including the one-dimensional lift, superlinear-consumption specialization, signed sharpness, dominated time differentiation, forced cell-energy decay, energy-to-norm conversion, and final exponential/polynomial rate assembly conditional on explicitly named deep parabolic inputs — is kernel-checked in Lean 4/mathlib. On rectangular boxes, the conservative zero-flux identity, exact mass conservation, Green's first identity, a genuine finite-dimensional `L^2` Poincare inequality, its `Cp = sqrt(N) C` norm form, the resulting mass-weighted coercivity bridge, and the global Neumann invariant-range/maximum-principle theorem including boundary, edge, and corner contacts are all derived rather than assumed. CI rejects `sorry`, `admit`, and explicit user axioms. The remaining gap is the arbitrary-smooth-domain extension together with Neumann semigroup smoothing, Choi local boundedness, the concrete cell-energy PDE identity, and PDE uniqueness for the sharpness reduction.
