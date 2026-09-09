# Lean verification status — AML production-consumption stabilization

Date: 2026-09-09
Branch: `research/aml-production-consumption-stabilization`
Latest verified formal-tree commit: `29fae452f7de74d8876bcdd14fc4328435131c64`
Latest verification-gate commit: `a6e526bc09924be03f53a680b48399fc2a0b1509`
Latest successful GitHub Actions run: `34354367834`
Toolchain: Lean `v4.33.1`, mathlib `v4.33.1`
Build command: `lake build` from `formal/`
Result: **SUCCESS** (`Build completed successfully (8717 jobs)`).
Proof-hygiene gate: **SUCCESS** — CI rejects occurrences of `sorry`, `admit`, and explicit `axiom` declarations in the AML formal library before compilation.

All statements listed below compile without `sorry`, `admit`, placeholders, or explicit user axioms.

## 1. Algebraic / structural core

File: `formal/AMLStabilization/AlgebraicCore.lean`

1. `squareOfLinearBound`
2. `massWeightedCoercivityReduction`
3. `scaledDissipationCoercivity`
4. `productionConsumptionIdentityOfEquilibrium`
5. `productionConsumptionIdentity`
6. `pureConsumptionIdentity`
7. `endpointDissipativityDoesNotForceRoot`

These verify the algebraic coercivity closure, dissipation rescaling, the exact production-consumption cancellation, the pure-consumption specialization, and the P0 counterexample showing that one-sided dissipativity alone need not imply `F(v_*)=0` at an endpoint.

## 2. Differential energy decay / Gronwall core

File: `formal/AMLStabilization/EnergyDecay.lean`

8. `weightedEnergy_antitone`
9. `energy_le_exp_of_differential_inequality`
10. `energy_le_exp_from_zero`

These verify

`dE(t) + c E(t) <= 0  ==>  E(t) <= E(s) exp(-c(t-s))`.

## 3. PDE-style energy to scalar decay bridge

File: `formal/AMLStabilization/SignalEnergyBridge.lean`

11. `pdeEnergy_to_scalarDissipation`
12. `pdeEnergy_to_exponentialDecay`
13. `pdeEnergy_to_exponentialDecay_from_zero`

These verify the abstract implication

`coercivity + PDE-style energy inequality => scalar dissipation => exponential decay`.

## 4. Integral mass-weighted coercivity

File: `formal/AMLStabilization/IntegralCoercivity.lean`

14. `weightedDeviationIntegralIdentity`
15. `integralMassWeightedMeanEstimate`
16. `integralMassWeightedCoercivity`

The weighted-mean integral rearrangement and the subsequent coercivity algebra use actual Bochner integrals.

## 5. Holder / Cauchy-Schwarz closure

File: `formal/AMLStabilization/HolderCore.lean`

17. `integral_mul_cauchySchwarz`
18. `weightedFirstMoment_cauchySchwarz`
19. `weightedDeviation_cauchySchwarz`
20. `weightedDeviation_cauchySchwarz_of_bound`
21. `integralMassWeightedMeanEstimate_of_MemLp`

Mathlib's Holder theorem with exponents `(2,2)` is used to derive, rather than assume,

`|int f g| <= sqrt(int f^2) sqrt(int g^2)`,

including the two weighted estimates required in the paper.

## 6. Holder-to-coercivity bridge

File: `formal/AMLStabilization/HolderCoercivityBridge.lean`

22. `integralMassWeightedCoercivity_of_MemLp`

The former hand-supplied Cauchy-Schwarz inputs are fully discharged by `MemLp` hypotheses.

## 7. Mean decomposition and Poincare interface

File: `formal/AMLStabilization/PoincareMeanCore.lean`

23. `meanSquareDecomposition`
    - from actual integral identities `int 1 = V` and `int f = V*fbar`, proves exactly
      `int f^2 = int (f-fbar)^2 + V*fbar^2`.

24. `meanSquareBase_of_Poincare`
    - from the named geometric Poincare interface
      `sqrt(int (f-fbar)^2) <= Cp*grad`, proves the base square estimate used by coercivity.

25. `integralMassWeightedCoercivity_of_MemLp_and_Poincare`
    - combines the exact integral mean decomposition, Holder closure, and mass-weighted coercivity;
    - the only remaining domain-geometric input at this stage is the Poincare inequality itself.

## 8. Concrete signal-energy identity interface

File: `formal/AMLStabilization/SignalEnergyIdentityCore.lean`

26. `dissipativeReactionIntegral`
    - from `u>=0` and pointwise `w R <= -beta w^2`, proves
      `int u w R <= -beta int u w^2`.

27. `signalEnergyInequality_from_integralPDE`
    - takes the differentiated-energy identity, PDE testing identity, and Neumann Green identity as explicitly named analytic interfaces;
    - Lean verifies all subsequent integral reaction estimates and algebra and proves
      `dE + 2(gradSq + beta*int u w^2) <= 0`.

28. `productionConsumption_signalEnergyInequality`
    - specializes to `R=-alpha*w`, i.e. `w=v-1/alpha`, and proves the exact production-consumption energy inequality.

## 9. Final signal-decay assembly

File: `formal/AMLStabilization/FinalSignalAssembly.lean`

29. `anisotropicCoercivity_to_exponentialDecay`
30. `anisotropicCoercivity_to_exponentialDecay_from_zero`
31. `massWeightedA`
32. `massWeightedB`
33. `massWeighted_coefficients_nonneg`
34. `massWeightedSignal_exponentialDecay`

The two different coercivity coefficients are normalized automatically and Lean proves an explicit rate.  With

`A = 2 Cp^2 + 4 V (K Cp / m)^2`,
`B = 4 V (sqrt(m)/m)^2`,

one obtains

`E(t) <= E(s) * exp(-(2*delta/(1+A+B))*(t-s))`.

## 10. End-to-end production-consumption signal theorem

File: `formal/AMLStabilization/ProductionConsumptionSignalFinal.lean`

35. `productionConsumptionSignal_exponentialDecay_from_interfaces`

This is the final compiled entry point for the signal L2-decay mechanism.  For the time-dependent fields `u` and `w=v-1/alpha`, it internally assembles:

`MemLp / Holder`
`=> weighted Cauchy-Schwarz`
`=> exact integral mean decomposition`
`=> Poincare interface`
`=> mass-weighted coercivity`
`=> production-consumption reaction dissipation`
`=> signal energy inequality`
`=> coefficient normalization`
`=> Gronwall`
`=> explicit exponential L2 signal decay`.

For `alpha>0`, Lean chooses `delta = min 1 alpha` and verifies

`E(t) <= E(s) * exp(-(2*min(1,alpha)/(1+A+B))*(t-s))`.

## Final CI evidence

Run `34354367834` at verification-gate commit `a6e526bc09924be03f53a680b48399fc2a0b1509` records:

- `Reject placeholders and explicit axioms`: **SUCCESS**;
- `Built AMLStabilization.SignalEnergyIdentityCore`;
- `Built AMLStabilization.HolderCore`;
- `Built AMLStabilization.HolderCoercivityBridge`;
- `Built AMLStabilization.PoincareMeanCore`;
- `Built AMLStabilization.FinalSignalAssembly`;
- `Built AMLStabilization.ProductionConsumptionSignalFinal`;
- `Built AMLStabilization`;
- `Build completed successfully (8717 jobs)`.

## Verification boundary — what is not formalized in current mathlib

The **full uniform PDE stabilization theorem is not claimed to be fully Lean-verified**.  The final signal theorem above is Lean-verified *from explicitly named standard analytic interfaces*.  The following remain human-proved/sourced because the current mathlib library does not provide a ready general framework for the paper's arbitrary smooth bounded Neumann domain and parabolic regularity theory:

1. the geometric Poincare inequality on an arbitrary smooth bounded connected domain in exactly the manuscript's Sobolev setup;
2. derivation of the Neumann Green identity `int w Delta w = -int |grad w|^2` on that general domain;
3. differentiation under the spatial integral for the concrete classical PDE solution (mathlib has generic parametric-integral differentiation machinery, but it has not been specialized here to the full PDE solution object);
4. mass conservation derived directly from the cell PDE and Neumann boundary condition;
5. the maximum-principle invariant interval for `v`;
6. Neumann heat-semigroup `L^p -> W^{1,infinity}` smoothing;
7. the cell-density `L2` PDE energy estimate in the full spatial function-space representation;
8. Choi's boundary local `L2 -> Linfinity` parabolic estimate and its use in the final `u` upgrade;
9. assembly of those external analytic facts into the manuscript's final
   `Linfinity x W^{1,infinity}` stabilization theorem.

Mathlib searches performed on 2026-09-09 found no general smooth-bounded-domain Poincare theorem or general Neumann Green/parabolic-semigroup infrastructure matching these requirements.  Therefore replacing the interfaces above by fully internal proofs would require building substantial new PDE/domain infrastructure rather than merely completing missing tactics.

## Correct provenance statement

> **Final Lean verification (CAP4-style): the complete algebraic, Holder, integral, mass-weighted coercivity, reaction-dissipation, energy-to-Gronwall, coefficient-tracking, and end-to-end production-consumption signal L2-decay chain is kernel-checked under explicitly named geometric/PDE analytic interfaces.  CI rejects `sorry`, `admit`, and explicit user axioms.  The arbitrary-smooth-domain Poincare/Green and parabolic regularity infrastructure needed for the full `Linfinity x W^{1,infinity}` PDE theorem is not currently formalized and must not be described as Lean-verified.**

This is the strongest verification claim supported by the current compiled artifact and existing mathlib infrastructure.