# Lean verification status — AML production-consumption stabilization

Date: 2026-09-09
Branch: `research/aml-production-consumption-stabilization`
Latest verified Lean commit: `51215689ace63e5478c5bf67c60a012836b85407`
Latest successful GitHub Actions run: `34344308882`
Toolchain: Lean `v4.33.1`, mathlib `v4.33.1`
Build command: `lake build` from `formal/`
Result: **SUCCESS** (`Build completed successfully (8709 jobs)`).

## What is Lean-verified

### 1. Algebraic / structural core

File: `formal/AMLStabilization/AlgebraicCore.lean`

The following statements compile without `sorry`, `admit`, placeholders, or extra axioms:

1. `squareOfLinearBound`
   - verifies the quadratic estimate obtained by squaring a nonnegative linear mean bound and applying `(x+y)^2 <= 2x^2+2y^2`.

2. `massWeightedCoercivityReduction`
   - verifies the algebraic closure of the paper's mass-weighted coercivity lemma:
     from a mean estimate and Poincare/mean decomposition, derives the explicit coercive bound used in the signal energy argument.
   - This is a reduction theorem: the measure-theoretic Poincare inequality and the derivation of the mean estimate from integrals are still human/sourced analytic inputs.

3. `scaledDissipationCoercivity`
   - verifies the algebraic step converting the unweighted coercivity bound into control by the actual dissipation `gradSq + alpha * weighted` whenever `delta <= 1` and `delta <= alpha`.

4. `productionConsumptionIdentityOfEquilibrium`
   - verifies exactly that if `alpha * vstar = 1`, then
     `(s-vstar)(1-alpha*s) = -alpha (s-vstar)^2`.

5. `productionConsumptionIdentity`
   - verifies the paper specialization `vstar = 1/alpha` for nonzero `alpha`.

6. `pureConsumptionIdentity`
   - verifies the pure-consumption special case `s(-s) = -s^2`.

7. `endpointDissipativityDoesNotForceRoot`
   - formally verifies the P0 audit counterexample: on `[0,1]`, `F=-1` satisfies the one-sided quadratic dissipativity inequality at endpoint `0` but `F(0) != 0`.
   - This justifies keeping `F(v_*)=0` as a separate explicit hypothesis in the general theorem.

### 2. Differential energy decay / Gronwall core

File: `formal/AMLStabilization/EnergyDecay.lean`

The following additional statements are now Lean-verified:

8. `weightedEnergy_antitone`
   - assumes an everywhere differentiable scalar energy `E` with derivative `dE` and the pointwise inequality
     `dE(t) + c * E(t) <= 0`;
   - proves that `E(t) * exp(c*t)` is antitone.
   - This formally verifies the integrating-factor calculus step used in the PDE argument.

9. `energy_le_exp_of_differential_inequality`
   - from the same differential inequality and `s <= t`, proves the exact two-time estimate
     `E(t) <= E(s) * exp(-c * (t-s))`.

10. `energy_le_exp_from_zero`
    - specializes the preceding theorem to `s=0`, yielding
      `E(t) <= E(0) * exp(-c*t)` for `t >= 0`.

These theorems formalize the abstract implication

`dE/dt + c E <= 0  ==>  exponential decay of E`.

They can be reused for both the signal energy and the cell-density energy once the corresponding PDE energy identities/inequalities are supplied as analytic inputs.

## What is NOT yet Lean-verified

The full PDE theorem is **not** currently Lean-verified. In particular, the following remain outside the formal build:

- mass conservation obtained by integrating the Neumann PDE;
- maximum-principle invariant range for `v`;
- Sobolev/Poincare inequality on a smooth bounded domain in the exact function-space setup;
- differentiation of the `L^2` energy along the classical PDE solution and identification of its derivative;
- conversion of the PDE signal-energy identity plus mass-weighted coercivity into the scalar hypothesis required by `EnergyDecay.lean`;
- Neumann heat-semigroup `L^p -> W^{1,infinity}` smoothing;
- the cell-density `L^2` PDE energy inequality;
- Choi's boundary local `L^2 -> L^infinity` parabolic estimate and its application;
- assembly of all analytic nodes into the final uniform exponential stabilization theorem.

Therefore the correct provenance statement is now:

> **Lean-verified algebraic/structural and scalar energy-decay core; full PDE stabilization theorem proved by the analytic manuscript argument but not formally verified in Lean.**

Do not describe the final PDE theorem itself as Lean-verified until the analytic dependencies are formalized and compiled.

## CI history

- Run `34342038855`: first algebraic-core build; failed only at an automatic factorization proof.
- Run `34342310962`: algebraic/structural core succeeded completely (`8708 jobs`).
- Runs `34343443424`, `34343769676`, `34344001280`: iterative API/alignment failures while introducing the calculus module; these exposed no mathematical counterexample or missing hypothesis.
- Run `34344308882` at commit `51215689ace63e5478c5bf67c60a012836b85407`: **SUCCESS**, including `AMLStabilization.EnergyDecay`, `AMLStabilization.AlgebraicCore`, and the library root (`8709 jobs`).

## Next formalization frontier

Highest-value next targets are:

1. **PDE-to-scalar bridge:** formalize a theorem whose inputs are the signal energy identity and the mass-weighted coercivity bound and whose output is the scalar differential inequality needed by `energy_le_exp_of_differential_inequality`.
2. **Integral coercivity layer:** formalize the mass/mean estimate itself with mathlib integration and Poincare assumptions, reducing the gap between the paper lemma and `massWeightedCoercivityReduction`.
3. Only after these are stable, attempt deeper parabolic PDE infrastructure.

This follows the repository rule that Lean is a second proof channel rather than decoration and that only compiled, statement-aligned results count as formal verification.
