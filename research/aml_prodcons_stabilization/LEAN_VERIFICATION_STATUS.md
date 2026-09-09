# Lean verification status — AML production-consumption stabilization

Date: 2026-09-09
Branch: `research/aml-production-consumption-stabilization`
Latest verified Lean tree commit: `cee4e97b99d32506b45d0d4e1b59021fa886a300`
Latest successful GitHub Actions run: `34349011208`
Toolchain: Lean `v4.33.1`, mathlib `v4.33.1`
Build command: `lake build` from `formal/`
Result: **SUCCESS** (`Build completed successfully (8711 jobs)`).

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
    - This removes the previously informal integral-rearrangement step from the coercivity proof.

15. `integralMassWeightedMeanEstimate`
    - assumes positive mass `int rho = m > 0`;
    - takes the two Cauchy-Schwarz-type integral estimates and the Poincare estimate as explicit analytic inputs;
    - verifies the triangle estimate, use of the conserved mass, Poincare substitution, and division by `m`;
    - proves
      `|fbar| <= (sqrt(m)/m)*sqrt(int rho f^2) + (K*Cp/m)*grad`.

16. `integralMassWeightedCoercivity`
    - combines theorem 15 with `massWeightedCoercivityReduction`;
    - verifies nonnegativity of `int f^2` and `int rho f^2` from pointwise squares and `rho>=0`;
    - proves a full integral coercivity inequality with explicit constants.

Run `34349011208` at commit `cee4e97b99d32506b45d0d4e1b59021fa886a300` explicitly logs:
- `Built AMLStabilization.EnergyDecay`;
- `Built AMLStabilization.AlgebraicCore`;
- `Built AMLStabilization.SignalEnergyBridge`;
- `Built AMLStabilization.IntegralCoercivity`;
- `Built AMLStabilization`;
- `Build completed successfully (8711 jobs)`.

The currently compiled abstract signal-decay chain is therefore:

`mass/integral identity + CS/Poincare analytic inputs`
`=> mass-weighted coercivity`
`=> PDE-style scalar dissipation bridge`
`=> exponential energy decay`.

## What is NOT yet Lean-verified

The full PDE theorem is **not** currently Lean-verified. The remaining analytic layer includes:

- mass conservation obtained directly by integrating the Neumann PDE in time;
- maximum-principle invariant range for `v`;
- derivation of the two Cauchy-Schwarz-type integral inputs in `IntegralCoercivity.lean` from `MemLp`/Holder hypotheses;
- the geometric Poincare inequality on the actual smooth bounded domain and its exact function-space setup;
- differentiation of the actual `L^2` norm-square energy along the classical PDE solution;
- derivation of the concrete signal-energy identity from integration by parts and the Neumann boundary condition;
- Neumann heat-semigroup `L^p -> W^{1,infinity}` smoothing;
- the cell-density `L^2` PDE energy inequality;
- Choi's boundary local `L^2 -> L^infinity` parabolic estimate and its application;
- assembly of all analytic nodes into the final uniform exponential stabilization theorem.

The correct provenance statement is now:

> **Lean-verified integral/coercive core, scalar Gronwall core, and PDE-style energy-to-decay bridge; the remaining Holder/Poincare/PDE integration-by-parts and parabolic regularity layers are human-proved or sourced rather than Lean-verified.**

Do not describe the final PDE stabilization theorem itself as Lean-verified until those analytic dependencies are formalized and compiled.

## CI history

- `34342038855`: first algebraic-core build; failed at an automatic factorization proof.
- `34342310962`: algebraic/structural core succeeded (`8708 jobs`).
- `34344308882`: EnergyDecay + AlgebraicCore + root succeeded (`8709 jobs`).
- `34347242173`: SignalEnergyBridge explicitly compiled and succeeded (`8710 jobs`).
- `34348683733`: first IntegralCoercivity attempt; only failure was a redundant tactic after `field_simp` had already closed the goal.
- `34349011208`: **SUCCESS**, explicitly compiling IntegralCoercivity and the full library root (`8711 jobs`).

## Next formalization frontier

Highest-value next targets are:

1. **Holder/Cauchy-Schwarz closure:** derive the two integral bounds currently passed to `integralMassWeightedMeanEstimate` directly from mathlib `MemLp`/Holder machinery.
2. **Concrete signal-energy identity interface:** formalize an inner-product/integration-by-parts layer that produces the exact `henergy` input consumed by `SignalEnergyBridge.lean`.
3. **Domain Poincare layer:** connect the abstract Poincare input to the actual smooth bounded domain setting.

This follows the repository rule that Lean is a second proof channel rather than decoration and that only compiled, statement-aligned results count as formal verification.
