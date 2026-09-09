# Lean verification status — AML production-consumption stabilization

Date: 2026-09-09
Branch: `research/aml-production-consumption-stabilization`
Latest verified Lean tree commit: `77df13f804b5334602984e249bc8f0a718d5e39d`
Latest successful GitHub Actions run: `34351354275`
Toolchain: Lean `v4.33.1`, mathlib `v4.33.1`
Build command: `lake build` from `formal/`
Result: **SUCCESS** (`Build completed successfully (8713 jobs)`).

All statements listed below compile without `sorry`, `admit`, placeholders, or extra axioms.

## 1. Algebraic / structural core

File: `formal/AMLStabilization/AlgebraicCore.lean`

1. `squareOfLinearBound`
   - squares a nonnegative linear mean bound and proves the quadratic estimate used later.

2. `massWeightedCoercivityReduction`
   - verifies the algebraic closure from a mean estimate plus Poincare/mean decomposition to the coercive bound.

3. `scaledDissipationCoercivity`
   - converts coercivity by `gradSq + weighted` into coercivity by the actual dissipation `gradSq + alpha * weighted` when `delta <= 1, alpha`.

4. `productionConsumptionIdentityOfEquilibrium`
   - verifies `(s-vstar)(1-alpha*s) = -alpha (s-vstar)^2` under `alpha*vstar=1`.

5. `productionConsumptionIdentity`
   - specializes to `vstar=1/alpha` for nonzero `alpha`.

6. `pureConsumptionIdentity`
   - verifies `s(-s)=-s^2`.

7. `endpointDissipativityDoesNotForceRoot`
   - verifies the P0 counterexample showing one-sided dissipativity alone need not force `F(v_*)=0` at an endpoint.

## 2. Differential energy decay / Gronwall core

File: `formal/AMLStabilization/EnergyDecay.lean`

8. `weightedEnergy_antitone`
   - from `dE(t)+c E(t)<=0`, proves `E(t) exp(c t)` is antitone.

9. `energy_le_exp_of_differential_inequality`
   - proves `E(t) <= E(s) exp(-c(t-s))` for `s<=t`.

10. `energy_le_exp_from_zero`
    - proves `E(t) <= E(0) exp(-ct)` for `t>=0`.

## 3. PDE-style energy to scalar decay bridge

File: `formal/AMLStabilization/SignalEnergyBridge.lean`

11. `pdeEnergy_to_scalarDissipation`
    - from nonnegative gradient/weighted dissipations, coercivity `E <= C(gradSq+weighted)`, and
      `dE + 2(gradSq+alpha*weighted) <= 0`, proves
      `dE + (2*delta/C) E <= 0` when `0<=delta<=1` and `delta<=alpha`.

12. `pdeEnergy_to_exponentialDecay`
    - combines theorem 11 with the verified Gronwall core.

13. `pdeEnergy_to_exponentialDecay_from_zero`
    - gives the initial-time exponential estimate.

## 4. Integral mass-weighted coercivity layer

File: `formal/AMLStabilization/IntegralCoercivity.lean`

14. `weightedDeviationIntegralIdentity`
    - using actual Bochner integrals and integrability hypotheses, verifies
      `int rho (f-fbar) = int rho f - fbar * int rho`.

15. `integralMassWeightedMeanEstimate`
    - assumes positive mass `int rho = m > 0`;
    - takes two Cauchy-Schwarz-type estimates and a Poincare estimate as inputs;
    - verifies the triangle estimate, mass substitution, Poincare substitution, and division by `m`.

16. `integralMassWeightedCoercivity`
    - combines theorem 15 with `massWeightedCoercivityReduction`;
    - verifies nonnegativity of `int f^2` and `int rho f^2` from pointwise squares and `rho>=0`;
    - proves the full integral coercivity inequality with explicit constants.

## 5. Holder / Cauchy-Schwarz closure

File: `formal/AMLStabilization/HolderCore.lean`

17. `integral_mul_cauchySchwarz`
    - derives the real-valued `L2` Cauchy-Schwarz inequality from mathlib's
      `integral_mul_le_Lp_mul_Lq_of_nonneg` with Holder exponents `(2,2)` and `MemLp` hypotheses;
    - proves
      `|int f*g| <= sqrt(int f^2) * sqrt(int g^2)`.

18. `weightedFirstMoment_cauchySchwarz`
    - applies theorem 17 to `sqrt(rho)` and `sqrt(rho)*f`;
    - under `rho>=0`, proves
      `|int rho*f| <= sqrt(int rho) * sqrt(int rho*f^2)`;
    - Lean verifies the square-root identities using `Real.sq_sqrt`.

19. `weightedDeviation_cauchySchwarz`
    - from `MemLp rho 2` and `MemLp (f-fbar) 2`, proves
      `|int rho*(f-fbar)| <= sqrt(int rho^2) * sqrt(int (f-fbar)^2)`.

20. `weightedDeviation_cauchySchwarz_of_bound`
    - if additionally `sqrt(int rho^2) <= K`, proves the exact bound needed by the coercivity lemma.

21. `integralMassWeightedMeanEstimate_of_MemLp`
    - discharges both Cauchy-Schwarz inputs of theorem 15 internally from `MemLp` hypotheses;
    - only the Poincare estimate remains an external analytic inequality input.

## 6. Holder-to-coercivity bridge

File: `formal/AMLStabilization/HolderCoercivityBridge.lean`

22. `integralMassWeightedCoercivity_of_MemLp`
    - combines the Holder closure with `integralMassWeightedCoercivity`;
    - the two former hand-supplied Cauchy-Schwarz hypotheses are no longer assumptions;
    - under the `MemLp` assumptions, positive mass, `rho>=0`, an `L2` bound for `rho`, the Poincare input, and the base mean-decomposition estimate, Lean proves the full mass-weighted coercivity inequality.

Run `34351354275` at commit `77df13f804b5334602984e249bc8f0a718d5e39d` explicitly logs:
- `Built AMLStabilization.EnergyDecay`;
- `Built AMLStabilization.AlgebraicCore`;
- `Built AMLStabilization.SignalEnergyBridge`;
- `Built AMLStabilization.IntegralCoercivity`;
- `Built AMLStabilization.HolderCore`;
- `Built AMLStabilization.HolderCoercivityBridge`;
- `Built AMLStabilization`;
- `Build completed successfully (8713 jobs)`.

The currently compiled abstract signal-decay chain is therefore:

`MemLp / Holder`
`=> weighted Cauchy-Schwarz estimates`
`=> mass/integral identity`
`=> mass-weighted coercivity`
`=> PDE-style scalar dissipation bridge`
`=> Gronwall`
`=> exponential energy decay`.

## What is NOT yet Lean-verified

The full PDE theorem is **not** currently Lean-verified. The remaining analytic layer includes:

- mass conservation obtained directly by integrating the Neumann PDE in time;
- maximum-principle invariant range for `v`;
- the geometric Poincare inequality on the actual smooth bounded domain and its exact function-space setup;
- the base mean-decomposition estimate in the exact Sobolev/domain formulation;
- differentiation of the actual `L2` norm-square energy along the classical PDE solution;
- derivation of the concrete signal-energy identity from integration by parts and the Neumann boundary condition;
- Neumann heat-semigroup `L^p -> W^{1,infinity}` smoothing;
- the cell-density `L2` PDE energy inequality;
- Choi's boundary local `L2 -> Linfinity` parabolic estimate and its application;
- assembly of all analytic nodes into the final uniform exponential stabilization theorem.

The correct provenance statement is now:

> **Lean-verified Holder/Cauchy-Schwarz layer, integral/coercive core, scalar Gronwall core, and PDE-style energy-to-decay bridge; Poincare, PDE integration-by-parts, maximum principle, semigroup smoothing, and parabolic regularity remain human-proved or sourced rather than Lean-verified.**

Do not describe the final PDE stabilization theorem itself as Lean-verified until those analytic dependencies are formalized and compiled.

## CI history

- `34342038855`: first algebraic-core build; failed at an automatic factorization proof.
- `34342310962`: algebraic/structural core succeeded (`8708 jobs`).
- `34344308882`: EnergyDecay + AlgebraicCore + root succeeded (`8709 jobs`).
- `34347242173`: SignalEnergyBridge explicitly compiled and succeeded (`8710 jobs`).
- `34349011208`: IntegralCoercivity explicitly compiled and succeeded (`8711 jobs`).
- `34350299203`, `34350619099`: HolderCore iterations exposing only Lean representation/API issues (`MemLp` exponent representation and pointwise absolute-value representation), not mathematical failures.
- `34350978932`: HolderCore compiled successfully (`8712 jobs`).
- `34351354275`: **SUCCESS**, explicitly compiling HolderCore, HolderCoercivityBridge, and the full root (`8713 jobs`).

## Next formalization frontier

Highest-value next targets are:

1. **Domain Poincare layer:** replace the remaining abstract Poincare input by a theorem tied to the actual bounded-domain function-space setting.
2. **Concrete signal-energy identity:** formalize differentiation of the `L2` signal energy and the Neumann integration-by-parts step that produces the `henergy` hypothesis consumed by `SignalEnergyBridge.lean`.
3. **Mass conservation:** formalize the Neumann mass-conservation identity for the cell equation.

This follows the repository rule that Lean is a second proof channel rather than decoration and that only compiled, statement-aligned results count as formal verification.
