# Lean verification status — AML weighted-damping stabilization

Date: 2026-09-11  
Branch: `research/aml-production-consumption-stabilization`  
Verified formal-tree commit: `8af07749fe733276054660a732bceaed8a86da4c`  
Successful GitHub Actions run: `34586143612` (run 290)  
Toolchain: Lean `v4.33.1`, mathlib revision `0df444a360eaa60ab8c11dca51a86af692955474`  
Build command: `lake build` from `formal/`  
Result: **SUCCESS — `Build completed successfully (8800 jobs)`**.  
Proof-hygiene gate: **SUCCESS** — CI rejects `sorry`, `admit`, and explicit user `axiom` declarations before compilation.

The verification root `formal/AMLStabilization.lean` now imports **92 AMLStabilization modules**. The formal tree contains the arbitrary-real-order weighted-damping/rate machinery, exact eventual finite-`L^p` rate optimization, signed sharpness, dominated energy differentiation, rectangular-box divergence/Green/mass conservation, a fully derived finite-dimensional box Poincare theorem, box mass-weighted coercivity, a global box Neumann maximum principle, and now a **concrete rectangular-box cell-energy chain for signal-dependent motility `u_t = Delta(phi(v)u)` through final exponential/polynomial stabilization-rate assembly conditional only on explicitly named deep strong-signal/Choi interfaces**.

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

## 4. Time differentiation, box mass conservation, and Green identities are derived

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

`ProductRuleGreenCore.lean` and `CanonicalBoxGreenCore.lean` push the self-pairing Green identity down to local Frechet/product-rule data. `CrossBoxGreenCore.lean` proves the cross identity

```text
integral w * Delta h = - integral grad w . grad h
```

on boxes from local derivative data and zero normal derivative of `h`.

## 5. Signal-energy PDE interfaces are reduced on boxes

`SignalPDEPairingCore.lean` derives the integrated PDE pairing from the pointwise PDE and integrability rather than taking the pairing identity as an input.

`BoxSignalEnergyCore.lean` combines pointwise PDE data with the canonical box Green identity.

`TimeDependentBoxSignalEnergyCore.lean` additionally generates

```text
d/dt integral w^2 = 2 integral w w_t
```

internally from dominated differentiation. On boxes, the signal-energy chain therefore no longer requires opaque `hEnergyDerivative`, `hPDEPairing`, or global Green assumptions.

## 6. Rectangular-box Poincare is fully derived and wired into downstream estimates

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
- `FullBoxPoincareSqrtCore.lean`: square-root norm form;
- `BoxPoincareCellInterfaceCore.lean`: exact scalar form used by the cell-energy assembly.

For a nondegenerate rectangular box of dimension `N=n+1`, if every side length is at most `C`, Lean proves

```text
integral |f-fbar|^2 <= N * C^2 * sum_i integral |partial_i f|^2,
```

and hence the effective Poincare constant

```text
Cp = sqrt(N) * C.
```

`FullBoxCoercivityBridge.lean` feeds this directly into the mass-weighted coercivity theorem, while `BoxPoincareCellInterfaceCore.lean` feeds it directly into the cell-energy scalar interface. No external box-level variance decomposition or geometric Poincare hypothesis is needed in these endpoints.

## 7. Global Neumann maximum principle is derived on boxes

The compiled chain is:

- `InvariantRangeCore.lean`: dissipativity gives the inward reaction sign;
- `SpatialExtremumSecondDerivativeCore.lean`: interior extrema give Hessian/Laplacian trace signs;
- `MaximumPrincipleContactCore.lean`: combines Laplacian, reaction, and PDE signs;
- `FirstContactBarrierCore.lean`: epsilon-tilted time-contact contradiction;
- `GlobalBoxContactSelectionCore.lean`: compact space-time cylinder selection of a tilted global contact point;
- `BoxInteriorContactCore.lean` and `GlobalBoxInteriorMaximumPrincipleCore.lean`: interior-contact version;
- `NeumannEndpointSecondDerivativeCore.lean`: endpoint extremum plus zero derivative gives the required second-derivative sign;
- `BoxNeumannMaximumContactCore.lean`: face/edge/corner Laplacian sign under coordinate-face Neumann conditions;
- `GlobalBoxNeumannMaximumPrincipleCore.lean`: global upper/lower and two-sided invariant bounds.

Thus, for the box problem `z_t = Delta z + rho F(z)` with nonnegative `rho`, dissipative `F`, and coordinate-face Neumann conditions, the box-level invariant-range/maximum-principle hypothesis is no longer external.

## 8. The concrete rectangular-box cell-energy PDE chain is now derived

This was previously a genuine unresolved interface. It is now kernel-checked on rectangular boxes.

The compiled chain contains:

- `CrossBoxGreenCore.lean`: cross integration by parts;
- `FiniteGradientCauchyCore.lean`: finite-dimensional pointwise and integrated gradient Cauchy-Schwarz;
- `BoxCellEnergyPDECore.lean`: from `u_t = Delta(cu)` and `c >= a0 > 0`, derives the exact tested energy identity and the raw inequality

```text
Q' + 2 a0 g^2 <= 2 H g;
```

- `TimeDependentBoxCellEnergyCore.lean`: generates `Q' = 2 integral (u-ubar) u_t` internally by dominated differentiation;
- `MotilityChainRuleCore.lean`: for `c = phi(v)`, derives `grad c = phi'(v) grad v`, coordinate formulas, continuity, and Neumann-face inheritance;
- `MotilityForcingCore.lean`: derives the generic `L^2` forcing bound and drift `MemLp` from a pointwise multiplier bound;
- `BoxMotilityForcingCore.lean`: on boxes, generates the drift measurability and obtains

```text
||u phi'(v) grad v||_2 <= U L_phi ||grad v||_2;
```

- `BoxMotilityCellEnergyCore.lean`: specializes the cell PDE energy estimate to `c = phi(v)`, internally producing coefficient-gradient continuity, Neumann inheritance, diffusion/drift integrability, and drift `MemLp`;
- `TimeDependentBoxMotilityCellEnergyCore.lean`: combines that specialization with dominated time differentiation.

Therefore the rectangular-box cell-energy PDE identity is **no longer an external analytic hypothesis**.

## 9. Cell decay and full rate assembly are now connected to the concrete box PDE package

The downstream scalar/rate assembly is no longer separated from the box PDE formalization by opaque cell-energy assumptions.

- `BoxMotilityCellScalarInterfaceCore.lean` defines the concrete quantities

```text
Q(t)  = integral_box (u(t)-ubar)^2,
g(t)  = (integral_box |grad u(t)|^2)^(1/2),
H(t)  = U L_phi (integral_box |grad v(t)|^2)^(1/2),
Cp    = sqrt(N) C,
```

and constructs at each time the derivative, nonnegativity, Poincare, and raw energy fields needed by the ODE layer.

- `CellEnergyInterfaceAssemblyCore.lean` drives the exponential and polynomial cell-energy decay theorems directly from that packaged pointwise interface instead of six independent assumptions.

- `BoxMotilityCellDecayCore.lean` derives the forcing rate from a signal-gradient `L^2` rate and proves the corresponding exponential/polynomial cell-energy decay with the explicit `U L_phi` factor.

- `BoxMotilityFullStabilizationCore.lean` connects the concrete box `Q,dQ,g,H` package to `FullStabilizationAssembly.lean`. Consequently, for the rectangular-box motility problem, the final exponential/polynomial stabilization-rate assembly no longer asks for abstract `hQderiv`, `hPoincare`, or `henergy` assumptions.

The only intentionally retained high-level analytic interfaces at this final box endpoint are:

1. a strong signal rate (the manuscript's Neumann semigroup/mixed-norm smoothing side);
2. comparison of the signal `L^2` gradient with that strong signal norm;
3. the Choi-type local/parabolic upgrade from cell `L^2`/forcing control to cell `L^infinity`.

These are the genuinely deep parabolic inputs rather than hidden cell-energy algebra.

## 10. Final CI evidence

GitHub Actions run `34586143612` (run 290), at formal-tree commit
`8af07749fe733276054660a732bceaed8a86da4c`, records:

- checkout of exactly that commit;
- `Reject placeholders and explicit axioms`: **SUCCESS**;
- successful compilation of `BoxMotilityForcingCore`;
- successful compilation of `BoxMotilityCellEnergyCore`;
- successful compilation of `TimeDependentBoxMotilityCellEnergyCore`;
- successful compilation of `BoxPoincareCellInterfaceCore`;
- successful compilation of `BoxMotilityCellScalarInterfaceCore`;
- successful compilation of `CellEnergyInterfaceAssemblyCore`;
- successful compilation of `BoxMotilityCellDecayCore`;
- successful compilation of `BoxMotilityFullStabilizationCore` at `[8798/8800]`;
- successful compilation of the root `AMLStabilization` target at `[8799/8800]`;
- **`Build completed successfully (8800 jobs)`**.

The root imports **92 AMLStabilization modules**, all compiled under the pinned Lean/mathlib toolchain.

## 11. What still prevents a literal arbitrary-smooth-domain PDE formalization

It would still be inaccurate to say that the entire manuscript theorem on an arbitrary smooth bounded Neumann domain is formalized from first principles. The remaining infrastructure is now concentrated in:

1. extension of the verified rectangular-box Poincare/divergence/Green/Neumann-maximum-principle/cell-energy geometry to arbitrary smooth bounded connected Neumann domains and traces;
2. Neumann heat-semigroup `L^p -> W^{1,infinity}` smoothing in the manuscript's required domain/function-space setting;
3. Choi's mixed-norm conormal/local boundedness theorem in the required setting;
4. the strong-signal-norm-to-`L^2`-gradient comparison in the exact manuscript function-space formulation (the final box theorem currently keeps this as an explicit analytic interface);
5. PDE uniqueness/invariance for the spatially homogeneous sharpness reduction.

The rectangular-box geometric Poincare input, global invariant-range/maximum-principle input, concrete motility cell-energy identity, forcing bound, and cell-energy-to-final-rate assembly are **no longer part of the unresolved list**.

## 12. Correct provenance statement

> **Strengthened Lean verification (current formal-tree level):** the arbitrary-real-order weighted-damping machinery — weighted Holder, nonlinear mass-weighted coercivity, quadratic/exponential versus superquadratic/polynomial signal endpoints, zero-energy branch, degenerate `theta` specialization, exact eventual finite-`L^p` exponent and rate-threshold arithmetic, mixed-norm time-exponent selection including the one-dimensional lift, superlinear-consumption specialization, signed sharpness, dominated time differentiation, forced cell-energy decay, energy-to-norm conversion, and final exponential/polynomial rate bookkeeping — is kernel-checked in Lean 4/mathlib. On rectangular boxes, the conservative zero-flux identity, exact mass conservation, Green and cross-Green identities, a genuine finite-dimensional `L^2` Poincare inequality and its `Cp = sqrt(N) C` forms, the resulting mass-weighted coercivity bridge, the global Neumann invariant-range theorem including boundary/edge/corner contacts, and the concrete signal-dependent-motility cell-energy chain `u_t = Delta(phi(v)u)` through exponential/polynomial cell decay and final stabilization assembly are all derived rather than assumed. The final box stabilization theorem remains conditional only on explicitly named deep strong-signal smoothing/comparison and Choi-type parabolic-upgrade inputs. CI rejects `sorry`, `admit`, and explicit user axioms. The remaining gap is the arbitrary-smooth-domain geometric/parabolic infrastructure, Neumann semigroup smoothing, Choi local boundedness, the exact strong-norm comparison layer, and PDE uniqueness for the sharpness reduction.
