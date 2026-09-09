# Lean verification status — AML production-consumption stabilization

Date: 2026-09-09
Branch: `research/aml-production-consumption-stabilization`
Lean commit verified: `7cb4d1aaebcc26286e2ae65c853ffd811614b2bd`
GitHub Actions run: `34342310962`
Toolchain: Lean `v4.33.1`, mathlib `v4.33.1`
Build command: `lake build` from `formal/`
Result: **SUCCESS** (`Build completed successfully (8708 jobs)`).

## What is Lean-verified

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

## What is NOT yet Lean-verified

The full PDE theorem is **not** currently Lean-verified. In particular, the following remain outside the formal build:

- mass conservation obtained by integrating the Neumann PDE;
- maximum-principle invariant range for `v`;
- Sobolev/Poincare inequality on a smooth bounded domain in the exact function-space setup;
- differentiation of the `L^2` energy along the classical solution;
- Neumann heat-semigroup `L^p -> W^{1,infinity}` smoothing;
- the cell-density `L^2` energy inequality;
- Choi's boundary local `L^2 -> L^infinity` parabolic estimate and its application;
- assembly of all analytic nodes into the final uniform exponential stabilization theorem.

Therefore the correct provenance statement is:

> **Lean-verified algebraic/structural core; full PDE theorem proved in the manuscript argument but not formally verified in Lean.**

Do not describe the final PDE theorem itself as Lean-verified until the analytic dependencies are formalized and compiled.

## CI history

Run 1 (`34342038855`) failed only at the automatic proof of the production-consumption factorization. The mathematical identity was correct; `nlinarith` did not discover the factorization automatically.

The proof was changed to explicitly rewrite `1` as `alpha * vstar` using the equilibrium relation and then close by `ring`.

Run 2 (`34342310962`) succeeded completely.

## Next formalization frontier

Highest-value next target:

1. formalize an abstract energy-decay lemma (coercive dissipation + differential inequality -> exponential decay), then
2. formalize the finite-dimensional/smooth-function version of the mass/mean estimate more directly with mathlib integration, before attempting full parabolic PDE infrastructure.

This follows the repository rule that Lean is a second proof channel rather than decoration and that only compiled, statement-aligned results count as formal verification.
