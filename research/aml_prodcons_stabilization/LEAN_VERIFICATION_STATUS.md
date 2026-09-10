# Lean verification status — AML weighted-damping stabilization

Date: 2026-09-10  
Branch: `research/aml-production-consumption-stabilization`  
Verified formal-tree commit: `f39336bd3b36fa81102c398f2e087b2ca743e5f2`  
Successful GitHub Actions run: `34440860645` (run 119)  
Toolchain: Lean `v4.33.1`, mathlib revision `0df444a360eaa60ab8c11dca51a86af692955474`  
Build command: `lake build` from `formal/`  
Result: **SUCCESS — `Build completed successfully (8743 jobs)`**.  
Proof-hygiene gate: **SUCCESS** — CI rejects `sorry`, `admit`, and explicit user `axiom` declarations before compilation.

The verification root `formal/AMLStabilization.lean` imports **36 AMLStabilization modules**.  The strengthened algebraic, integral, weighted-damping, scalar-decay, finite-`L^p`, cell-energy propagation, sharpness, and final rate-assembly layers are kernel-checked.  The remaining gap to a literal arbitrary-smooth-domain PDE formalization is isolated to standard geometric/parabolic analytic infrastructure that mathlib does not presently provide in the required Neumann setting.

## 1. Original quadratic / production-consumption chain

The previously verified production-consumption chain remains intact:

- `AlgebraicCore`: linear/quadratic algebra, production-consumption identities, and the endpoint counterexample showing that dissipativity alone does not force `F(v_*)=0` at an endpoint;
- `EnergyDecay`: scalar Gronwall through monotonicity of `E(t) exp(ct)`;
- `SignalEnergyBridge`: PDE-style energy inequality to exponential decay;
- `IntegralCoercivity`, `HolderCore`, `HolderCoercivityBridge`, `PoincareMeanCore`: exact integral mean decomposition, genuine Bochner Cauchy-Schwarz/Holder steps, and the mass-weighted coercivity reduction;
- `SignalEnergyIdentityCore`: reaction dissipation and the production-consumption signal energy inequality from named PDE/Green identities;
- `FinalSignalAssembly`: coefficient normalization and exponential signal decay;
- `ProductionConsumptionSignalFinal`: end-to-end production-consumption signal `L^2` decay from the named geometric/PDE interfaces.

In particular, the production-consumption specialization with `R=-alpha*w` is still kernel-checked through the complete mass-weighted coercivity and Gronwall chain.

## 2. Genuine arbitrary-real-`q` weighted Holder

File: `formal/AMLStabilization/WeightedHolderQ.lean`

Lean now proves the real-exponent weighted Holder estimate itself, rather than accepting it as an interface.  For `q>1`, nonnegative `rho`, `∫rho=m`, and the required integrability,

```text
|∫ rho f| <= (∫ rho |f|^q)^(1/q) * m^(1-1/q).
```

The proof constructs the Holder conjugate `q/(q-1)`, proves the exact reciprocal identity, derives the relevant `MemLp` hypotheses, and invokes mathlib's Bochner-integral Holder inequality.

This removes the former verification gap for the arbitrary-real-`q` first-moment estimate.

## 3. Arbitrary-`q` nonlinear mass-weighted coercivity

Files:

- `NonlinearCoercivityAlgebra.lean`
- `NonlinearIntegralCoercivity.lean`

Lean verifies the exact nonlinear mass-weighted coercivity mechanism for arbitrary real `q >= 2`.  With the manuscript notation,

```text
A = Cp^2 * (1 + 2*V*K^2/m^2),
B_q = 2*V*m^(-2/q),
```

and the integral theorem proves

```text
∫ f^2 <= A * grad^2 + B_q * (∫ rho |f|^q)^(2/q).
```

The theorem is built from the genuine arbitrary-`q` Holder estimate, exact integral mean decomposition, the `L^2` weighted-deviation estimate, a named Poincare input, and kernel-checked coefficient algebra.

## 4. Arbitrary-order reaction dissipation and signal energy identity

File: `formal/AMLStabilization/GeneralSignalEnergyIdentityQ.lean`

For arbitrary real `q`, Lean proves that pointwise weighted damping

```text
w*R <= -beta*|w|^q
```

and `u >= 0` imply the weighted integral reaction estimate and, from the named differentiation/PDE-pairing/Neumann-Green identities,

```text
dE + 2*(gradSq + beta*∫u|w|^q) <= 0.
```

The cubic-degenerate `q=4` specialization is also kernel-checked.

## 5. Arbitrary-`q>2` Bihari decay, including the zero-energy branch

Files:

- `GeneralPolynomialEnergyDecay.lean`
- `ZeroEnergyBranch.lean`
- `LocalPolynomialEnergyDecay.lean`

Lean verifies the exact Bihari calculation for every real `q>2`:

```text
E' + 2*c*E^(q/2) <= 0
```

implies

```text
E(t) <=
  (E(s)^(-(q-2)/2) + (q-2)*c*(t-s))^(-2/(q-2)).
```

The final nonnegative version does **not** require a global strict-positivity hypothesis on the energy.  If the nonnegative energy hits zero on `[s,t]`, Lean proves that it remains zero by antitonicity; otherwise the local positive-energy Bihari theorem applies.  This closes the technical `E=0` branch inside the kernel.

The older `PolynomialEnergyDecay.lean` `q=4` / inverse-linear branch remains as an independently verified representative specialization.

## 6. Fractional dissipation closure and the general rate dichotomy

File: `formal/AMLStabilization/GeneralRateAssembly.lean`

Lean verifies the nonlinear closure from

```text
E <= A*Y + B*Z^(2/q),
E <= M,
D = Y + beta*Z
```

to a fractional coercivity estimate

```text
E <= Gamma * D^(2/q)
```

with an explicit `rateGamma`, and then derives the scalar `q/2`-power differential inequality needed by Bihari.

This is the kernel-checked algebra behind the quadratic/exponential versus superquadratic/polynomial rate dichotomy.

## 7. End-to-end general weighted-damping signal endpoints

Files:

- `GeneralQuadraticWeightedDampingFinal.lean`
- `GeneralWeightedDampingFinal.lean`
- `GeneralWeightedDampingNonnegativeFinal.lean`

Lean now contains both sides of the abstract signal-rate theorem:

- **quadratic damping (`q=2`)**: general exponential signal `L^2` decay;
- **superquadratic damping (`q>2`)**: general algebraic signal `L^2` decay;
- the preferred superquadratic endpoint only assumes the natural nonnegativity `E>=0`, not `E>0` for all times.

These theorems internally assemble the genuine arbitrary-`q` Holder estimate, nonlinear mass-weighted coercivity, reaction dissipation, fractional closure, and Gronwall/Bihari step.  Poincare and the concrete PDE differentiation/Green identities remain explicitly named analytic inputs.

## 8. Eventual finite-`L^p` weakening

Files:

- `LpExponentCore.lean`
- `LpFiniteMeasureCore.lean`
- `LpProductCore.lean`
- `BoundedInterpolationCore.lean`

Lean verifies:

- the manuscript's explicit exponent selection for `p > max{n,2}`;
- finite-measure `L^p -> L^2` membership and seminorm transfer;
- the Holder product exponent relation and actual `MemLp` product transfer;
- bounded `L^2`-to-higher-moment interpolation, including exponential and polynomial rate propagation.

Thus the non-PDE exponent bookkeeping behind the eventual finite-`L^p` hypothesis is no longer only paper-level.

## 9. Cell-energy propagation

Files:

- `CellEnergyCore.lean`
- `ForcedEnergyDecay.lean`
- `PolynomialForcedEnergyDecay.lean`
- `CellEnergyAssembly.lean`
- `RateComparisonCore.lean`
- `CellEnergyEnvelope.lean`

Lean verifies the scalar closure of the cell-density `L^2` energy stage.  From a Poincare-controlled cell energy and a coefficient forcing `H`, it derives a linearly damped forced energy inequality.  It then proves:

- explicit exponential-forcing bounds;
- explicit polynomial-forcing bounds;
- correct time-centered forcing `exp(-lambda*(t-T))` bookkeeping;
- absorption of the faster exponential transient into a single slower exponential or polynomial envelope.

The resulting energy-scale envelopes have the form

```text
Q(t) <= C * exp(-2*lambda*(t-T))
```

or

```text
Q(t) <= C * (1+t-T)^(-2*b).
```

This removes the former verification gap in the scalar cell-energy rate propagation.  What remains external is the PDE derivation of the concrete cell-energy inequality itself.

## 10. Energy-to-norm and Choi-interface rate closure

File: `formal/AMLStabilization/RateRootCore.lean`

Lean verifies:

- square-root conversion from an energy rate with exponent `2*lambda` / `2*b` to the corresponding norm rate `lambda` / `b`;
- scalar closure of a Choi-type parabolic upgrade interface

```text
U_infty <= C1*sqrt(Q) + C2*H
```

into a final exponential or polynomial `L^infinity` rate.

The Choi regularity theorem itself is not re-proved in Lean; once supplied as the explicitly named analytic interface, all subsequent rate bookkeeping is kernel-checked.

## 11. Full stabilization rate assembly from the deep analytic interfaces

File: `formal/AMLStabilization/FullStabilizationAssembly.lean`

The two final assembly theorems are kernel-checked:

- `fullExponentialStabilization_from_analytic_interfaces`;
- `fullPolynomialStabilization_from_analytic_interfaces`.

They take as explicit deep analytic inputs:

1. a signal `W^{1,infinity}` decay estimate, representing the Neumann heat-semigroup smoothing stage;
2. a Choi-type local `L^2 -> L^infinity` estimate for the cell equation.

Lean then automatically propagates

```text
signal W^{1,infinity} rate
  -> coefficient forcing rate H
  -> cell L^2 energy rate
  -> cell L^2 norm rate
  -> cell L^infinity rate,
```

for both the exponential and polynomial branches.

Therefore the **full rate assembly conditional on explicitly named standard parabolic analytic inputs is Lean-verified**.

## 12. Sharpness and superlinear-consumption application algebra

Files:

- `SharpnessCore.lean`
- `SuperlinearConsumptionCore.lean`

Lean verifies the spatially homogeneous sharpness ODE profile, including its derivative identity, and the superlinear consumption law

```text
F(s) = -s*|s|^(m-1)
```

with the exact dissipativity identity

```text
s*F(s) = -|s|^(m+1)
```

for `m>1`.

Thus the scalar algebra behind the polynomial-rate sharpness/application examples is kernel-checked.

## Final CI evidence

GitHub Actions run `34440860645` (run 119), at formal-tree commit
`f39336bd3b36fa81102c398f2e087b2ca743e5f2`, records:

- `Reject placeholders and explicit axioms`: **SUCCESS**;
- `Built AMLStabilization.LocalPolynomialEnergyDecay`;
- `Built AMLStabilization.GeneralWeightedDampingNonnegativeFinal`;
- `Built AMLStabilization.CellEnergyAssembly`;
- `Built AMLStabilization.CellEnergyEnvelope`;
- `Built AMLStabilization.FullStabilizationAssembly`;
- `Built AMLStabilization`;
- **`Build completed successfully (8743 jobs)`**.

All 36 modules imported by the verification root compile under the pinned Lean/mathlib toolchain.

## What is still not a literal full PDE formalization

The phrase “fully Lean-verified PDE theorem on an arbitrary smooth bounded domain” would still be too strong.  The following deep analytic/geometric ingredients are not currently formalized in this library and were not found as ready-made mathlib theorems in the exact required Neumann-domain setup:

1. the geometric Poincare inequality on an arbitrary smooth bounded connected domain in the manuscript's exact Sobolev setup;
2. the Neumann Green identity `∫ w Δw = -∫|∇w|^2` on that domain;
3. differentiation under the integral sign specialized to the concrete classical PDE solution;
4. cell mass conservation derived directly from the PDE/Neumann boundary condition;
5. the invariant signal range / maximum-principle argument for the concrete system;
6. the Neumann heat-semigroup `L^p -> W^{1,infinity}` smoothing theory needed for the signal upgrade;
7. Choi's conormal local parabolic boundedness theorem and its arbitrary-smooth-domain implementation;
8. the concrete function-space derivation of the cell-density PDE energy identity.

These are **explicit analytic interfaces**, not hidden axioms: the CI gate rejects user `axiom` declarations, and every theorem downstream of those named hypotheses is kernel-checked.

## Correct provenance statement

> **Strengthened Lean verification (final rate-assembly level):** the complete novel algebraic/integral machinery for arbitrary real weighted-damping order, including genuine weighted Holder, nonlinear mass-weighted coercivity, quadratic/exponential and superquadratic/polynomial signal endpoints, the nonnegative zero-energy branch, eventual finite-`L^p` exponent/product/interpolation machinery, sharpness/application algebra, forced cell-energy decay, single-rate cell envelopes, energy-to-norm conversion, and the final exponential/polynomial full-stabilization rate assembly conditional on explicitly named Neumann-semigroup/Choi/geometric PDE interfaces, is kernel-checked in Lean 4/mathlib. CI rejects `sorry`, `admit`, and explicit user axioms. The arbitrary-smooth-domain Neumann PDE analytic infrastructure itself is not presently formalized and must not be described as Lean-verified.
