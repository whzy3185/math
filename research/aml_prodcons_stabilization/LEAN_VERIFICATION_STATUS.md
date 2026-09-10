# Lean verification status — AML mass-weighted stabilization rates

Date: 2026-09-10
Branch: `research/aml-production-consumption-stabilization`
Latest verified formal-tree commit: `499e78401b3667636242385f5aa0d51b836cd2a6`
Latest successful GitHub Actions run: `34428439465`
Toolchain: Lean `v4.33.1`, mathlib `v4.33.1`
Build command: `lake build` from `formal/`
Result: **SUCCESS** (`Build completed successfully (8719 jobs)`).
Proof-hygiene gate: **SUCCESS** — CI rejects `sorry`, `admit`, and explicit user `axiom` declarations before compilation.

The current library contains **50 compiled theorem nodes** across the original quadratic/exponential chain and the new polynomial-decay / `L^p` exponent modules.  All statements compile without `sorry`, `admit`, placeholders, or explicit user axioms.

## 1. Algebraic / structural core

File: `formal/AMLStabilization/AlgebraicCore.lean`

1. `squareOfLinearBound`
2. `massWeightedCoercivityReduction`
3. `scaledDissipationCoercivity`
4. `productionConsumptionIdentityOfEquilibrium`
5. `productionConsumptionIdentity`
6. `pureConsumptionIdentity`
7. `endpointDissipativityDoesNotForceRoot`

The last theorem formally records the endpoint counterexample showing why the equilibrium condition `F(v_*)=0` must be stated explicitly in the strengthened degenerate theorem.

## 2. Exponential scalar energy decay

File: `formal/AMLStabilization/EnergyDecay.lean`

8. `weightedEnergy_antitone`
9. `energy_le_exp_of_differential_inequality`
10. `energy_le_exp_from_zero`

These verify the scalar Gronwall implication `E' + cE <= 0 => exponential decay`.

## 3. PDE-style energy-to-decay bridge

File: `formal/AMLStabilization/SignalEnergyBridge.lean`

11. `pdeEnergy_to_scalarDissipation`
12. `pdeEnergy_to_exponentialDecay`
13. `pdeEnergy_to_exponentialDecay_from_zero`

## 4. Integral mass-weighted coercivity

File: `formal/AMLStabilization/IntegralCoercivity.lean`

14. `weightedDeviationIntegralIdentity`
15. `integralMassWeightedMeanEstimate`
16. `integralMassWeightedCoercivity`

## 5. Holder / Cauchy-Schwarz closure

File: `formal/AMLStabilization/HolderCore.lean`

17. `integral_mul_cauchySchwarz`
18. `weightedFirstMoment_cauchySchwarz`
19. `weightedDeviation_cauchySchwarz`
20. `weightedDeviation_cauchySchwarz_of_bound`
21. `integralMassWeightedMeanEstimate_of_MemLp`

## 6. Holder-to-coercivity bridge

File: `formal/AMLStabilization/HolderCoercivityBridge.lean`

22. `integralMassWeightedCoercivity_of_MemLp`

## 7. Mean decomposition / Poincare interface

File: `formal/AMLStabilization/PoincareMeanCore.lean`

23. `meanSquareDecomposition`
24. `meanSquareBase_of_Poincare`
25. `integralMassWeightedCoercivity_of_MemLp_and_Poincare`

The exact integral mean decomposition is internal.  The geometric Poincare theorem on the manuscript's arbitrary smooth bounded domain remains an explicitly named analytic interface.

## 8. Concrete signal-energy interface

File: `formal/AMLStabilization/SignalEnergyIdentityCore.lean`

26. `dissipativeReactionIntegral`
27. `signalEnergyInequality_from_integralPDE`
28. `productionConsumption_signalEnergyInequality`

## 9. Final quadratic signal-decay assembly

File: `formal/AMLStabilization/FinalSignalAssembly.lean`

29. `anisotropicCoercivity_to_exponentialDecay`
30. `anisotropicCoercivity_to_exponentialDecay_from_zero`
31. `massWeightedA`
32. `massWeightedB`
33. `massWeighted_coefficients_nonneg`
34. `massWeightedSignal_exponentialDecay`

## 10. End-to-end production-consumption signal theorem

File: `formal/AMLStabilization/ProductionConsumptionSignalFinal.lean`

35. `productionConsumptionSignal_exponentialDecay_from_interfaces`

This kernel-checks the quadratic production-consumption signal `L^2` decay chain from the named Poincare / PDE Green-energy interfaces through Holder, mass-weighted coercivity, reaction dissipation, coefficient tracking and Gronwall.

## 11. New polynomial-energy decay core

File: `formal/AMLStabilization/PolynomialEnergyDecay.lean`

36. `reciprocalEnergyShift_monotone`
37. `reciprocalEnergy_lower_of_quadratic_dissipation`
38. `energy_le_inverse_linear_of_quadratic_dissipation`
39. `quarticCoercivity_to_quadraticDissipation`
40. `quarticDamping_to_inverseLinearEnergyDecay`
41. `cubicDegenerateIdentity`

This is the representative **`q=4` / `theta=2` algebraic branch** of the strengthened manuscript.  In particular Lean verifies

`E' + c E^2 <= 0  =>  E(t) <= E(s)/(1+c E(s)(t-s))`,

and also verifies the quartic coercivity-to-quadratic-dissipation reduction and the exact cubic-degenerate reaction identity

`(s-v_*)*(-kappa*(s-v_*)^3) = -kappa*(s-v_*)^4`.

Run `34427848707` first established this module together with the previous library (`8718 jobs`).

## 12. New `L^p` exponent arithmetic core

File: `formal/AMLStabilization/LpExponentCore.lean`

42. `two_mul_p_div_p_add_two_lt_p`
43. `lpLowerThreshold_lt_p`
44. `lpChoice_between`
45. `lpChoice_gt_n_and_lt_p`
46. `two_mul_p_div_p_add_two_lt_lpChoice`
47. `holderPartner_identity`
48. `two_lt_holderPartner_of_threshold`
49. `lpChoice_exponent_package`
50. `transferRate_pos`

The module defines

`holderPartner p r = p*r/(p-r)`,

`lpLowerThreshold n p = max n (2p/(p+2))`,

and the midpoint choice `lpChoice`.  From `p > max n 2`, Lean verifies a concrete `r` satisfying

`n < r < p`,

`2 < s := holderPartner p r`,

and the exact Holder relation

`1/r = 1/p + 1/s`.

It also verifies positivity of the transfer exponent

`2(p-r)/(theta*p*r)`

under the natural sign assumptions.  These are the exponent constraints used in the strengthened eventual-finite-`L^p` PDE theorem.

## Final CI evidence

Run `34428439465` at commit `499e78401b3667636242385f5aa0d51b836cd2a6` records:

- `Reject placeholders and explicit axioms`: **SUCCESS**;
- `Built AMLStabilization.LpExponentCore`;
- `Built AMLStabilization.PolynomialEnergyDecay`;
- all previously verified AMLStabilization modules built successfully;
- `Built AMLStabilization`;
- `Build completed successfully (8719 jobs)`.

The immediately preceding failed exponent run `34428180153` is preserved as evidence: it exposed only a missing abstract positivity derivation for the chosen `r`; the proof was corrected by deriving `r>0` from `r>2p/(p+2)>0`.  No mathematical theorem was weakened.

## Strengthened paper theorem status

### Paper-level proved

The strengthened manuscript proves, at the human/PDE level:

1. nonlinear mass-weighted coercivity for arbitrary real `q >= 2`;
2. an abstract fixed-mass weighted-damping **exponential/algebraic rate dichotomy**;
3. full exponential stabilization from an eventual finite `L^p` bound with `p > max{n,2}`;
4. algebraic full stabilization for degenerate kinetics of order `2+theta`;
5. sharpness of the signal exponent `1/theta` by spatially homogeneous solutions;
6. applications to Qin--Zheng production-consumption and superlinear signal consumption.

### Lean-verified strengthening

Lean now independently verifies:

- the previous complete quadratic mass-weighted / exponential signal-decay core;
- the representative `q=4` algebraic scalar-energy branch;
- the exact cubic-degenerate reaction identity;
- the exponent-selection arithmetic needed by the eventual finite-`L^p` upgrade.

### Not yet Lean-verified

The following strengthened components remain paper-level rather than kernel-checked:

- the arbitrary-real-`q` weighted Holder inequality and nonlinear mass-weighted coercivity with the exact manuscript constants `A,B_q`;
- arbitrary-real-`q>2` Bihari integration (only the representative `q=4` branch is formalized);
- interpolation and Neumann heat-semigroup estimates for the concrete PDE;
- the cell-density PDE `L^2` energy identity in a full spatial function-space representation;
- Choi's conormal local boundedness theorem/application;
- the one-dimensional lifting argument as a concrete PDE object;
- the full `L^infinity x W^{1,infinity}` exponential/algebraic stabilization theorem.

The same underlying mathlib infrastructure limitations remain: general smooth-domain Poincare/Green identities and the needed parabolic regularity theory are not available as ready theorem interfaces.

## Correct provenance statement

> **Strengthened Lean verification:** the quadratic mass-weighted signal-decay chain, a representative quartic-damping/inverse-linear algebraic-decay core, the cubic-degenerate identity, and the eventual-`L^p` exponent-selection arithmetic are kernel-checked in Lean 4/mathlib.  CI rejects `sorry`, `admit`, and explicit user axioms.  The arbitrary-`q` nonlinear Holder/coercivity layer and the full smooth-domain parabolic PDE regularity assembly remain human-proved or sourced and must not be described as fully Lean-verified.
