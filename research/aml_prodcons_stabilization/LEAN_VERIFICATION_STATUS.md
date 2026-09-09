# Lean verification status — AML production-consumption stabilization

Date: 2026-09-09
Branch: `research/aml-production-consumption-stabilization`
Latest verified Lean tree commit: `8eba9ab96e0a9e42078f3e53fb035033c51151be`
Latest successful GitHub Actions run: `34347242173`
Toolchain: Lean `v4.33.1`, mathlib `v4.33.1`
Build command: `lake build` from `formal/`
Result: **SUCCESS** (`Build completed successfully (8710 jobs)`).

The later bridge-file change `c0cdd0a951a3770e4ab00db4cf450788f809ad0b` changes only documentation text, not theorem statements or proof terms. The exact compiled proof tree is recorded above.

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

8. `weightedEnergy_antitone`
   - assumes an everywhere differentiable scalar energy `E` with derivative `dE` and the pointwise inequality
     `dE(t) + c * E(t) <= 0`;
   - proves that `E(t) * exp(c*t)` is antitone.

9. `energy_le_exp_of_differential_inequality`
   - from the same differential inequality and `s <= t`, proves
     `E(t) <= E(s) * exp(-c * (t-s))`.

10. `energy_le_exp_from_zero`
    - gives
      `E(t) <= E(0) * exp(-c*t)` for `t >= 0`.

### 3. PDE-style energy to scalar decay bridge

File: `formal/AMLStabilization/SignalEnergyBridge.lean`

11. `pdeEnergy_to_scalarDissipation`
    - assumes pointwise nonnegativity of the gradient and weighted dissipations;
    - assumes the coercivity estimate
      `E <= C * (gradSq + weighted)` with `C > 0`;
    - assumes `0 <= delta <= 1` and `delta <= alpha`;
    - assumes the PDE-style energy inequality
      `dE + 2 * (gradSq + alpha * weighted) <= 0`;
    - proves the scalar differential inequality
      `dE + (2*delta/C) * E <= 0`.

12. `pdeEnergy_to_exponentialDecay`
    - combines theorem 11 with the verified Gronwall core;
    - proves the two-time estimate
      `E(t) <= E(s) * exp(-(2*delta/C)*(t-s))` for `s <= t`.

13. `pdeEnergy_to_exponentialDecay_from_zero`
    - proves the initial-time specialization
      `E(t) <= E(0) * exp(-(2*delta/C)*t)` for `t >= 0`.

Run `34347242173` explicitly logs:
- `Built AMLStabilization.EnergyDecay`;
- `Built AMLStabilization.AlgebraicCore`;
- `Built AMLStabilization.SignalEnergyBridge`;
- `Built AMLStabilization`;
- `Build completed successfully (8710 jobs)`.

Thus the following abstract chain is now genuinely compiled in Lean:

`coercivity + PDE-style energy inequality`
`=> scalar differential dissipation`
`=> exponential energy decay`.

For the signal equation in the paper, the intended substitution is
`E(t)=||v(t)-v_*||_2^2`,
`gradSq(t)=||grad(v(t)-v_*)||_2^2`,
and `weighted(t)=int u(t)(v(t)-v_*)^2`.

## What is NOT yet Lean-verified

The full PDE theorem is **not** currently Lean-verified. The remaining analytic layer includes:

- mass conservation obtained by integrating the Neumann PDE;
- maximum-principle invariant range for `v`;
- the integral/Poincare derivation of the mass-weighted coercivity hypothesis in the exact function-space setting;
- differentiation of the actual `L^2` norm-square energy along the classical PDE solution and identification of its derivative;
- derivation of the concrete PDE energy identity from integration by parts and the Neumann boundary condition;
- Neumann heat-semigroup `L^p -> W^{1,infinity}` smoothing;
- the cell-density `L^2` PDE energy inequality;
- Choi's boundary local `L^2 -> L^infinity` parabolic estimate and its application;
- assembly of these analytic nodes into the final uniform exponential stabilization theorem.

Therefore the correct provenance statement is now:

> **Lean-verified algebraic/coercive, scalar Gronwall, and PDE-style energy-to-decay bridge; the analytic PDE identities and regularity theory remain human-proved/sourced rather than Lean-verified.**

Do not describe the final PDE stabilization theorem itself as Lean-verified until those analytic dependencies are formalized and compiled.

## CI history

- Run `34342038855`: first algebraic-core build; failed only at an automatic factorization proof.
- Run `34342310962`: algebraic/structural core succeeded (`8708 jobs`).
- Runs `34343443424`, `34343769676`, `34344001280`: iterative API/alignment failures while introducing the calculus module; no mathematical counterexample or missing hypothesis was exposed.
- Run `34344308882`: EnergyDecay + AlgebraicCore + library root succeeded (`8709 jobs`).
- Run `34347158080`: succeeded but did not yet import the new bridge into the library root, so it was not used as bridge verification evidence.
- Run `34347242173` at commit `8eba9ab96e0a9e42078f3e53fb035033c51151be`: **SUCCESS**, explicitly compiling `SignalEnergyBridge` and the library root (`8710 jobs`).

## Next formalization frontier

Highest-value next targets are:

1. **Integral coercivity layer:** formalize the mass/mean estimate with mathlib integration and a Poincare hypothesis, reducing the gap between the PDE lemma and `massWeightedCoercivityReduction`.
2. **Concrete signal-energy identity interface:** formalize an abstract inner-product/integration-by-parts statement that produces the exact `henergy` input consumed by `SignalEnergyBridge.lean`.
3. Only after these are stable, attempt deeper parabolic PDE infrastructure such as maximum principles and semigroup smoothing.

This follows the repository rule that Lean is a second proof channel rather than decoration and that only compiled, statement-aligned results count as formal verification.
