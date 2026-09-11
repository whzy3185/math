# Strengthened rate-dichotomy theorem package

Date: 2026-09-11
Branch: `research/aml-production-consumption-stabilization`

## 1. Nonlinear mass-weighted coercivity

For `q >= 2`, `rho >= 0`, `int rho = m > 0`, `||rho||_2 <= K`, and finite weighted integral,

\[
\|f\|_2^2\le A\|\nabla f\|_2^2+B_q\left(\int_\Omega\rho|f|^q\right)^{2/q},
\]

with

\[
A=C_P^2\left(1+\frac{2|\Omega|K^2}{m^2}\right),\qquad
B_q=2|\Omega|m^{-2/q}.
\]

The proof uses Holder with respect to the measure `rho dx`, Cauchy-Schwarz, Poincare, and exact mean decomposition.

For rectangular boxes, the Poincare input is now Lean-derived. If the dimension is `N` and every side length is bounded by `C`, the formal tree proves

\[
\int_\Omega |f-\bar f|^2\le NC^2\sum_i\int_\Omega |\partial_i f|^2,
\]

hence an effective Poincare constant

\[
C_P=\sqrt N\,C.
\]

`FullBoxCoercivityBridge.lean` feeds this directly into the mass-weighted coercivity theorem, so no external box-level Poincare or variance-decomposition hypothesis is needed. `BoxPoincareCellInterfaceCore.lean` supplies the same geometry directly in the scalar form used by the cell-energy ODE assembly.

## 2. Abstract weighted-damping rate dichotomy

Let

\[
z_t=\Delta z+\rho(x,t)F(z),\qquad \partial_\nu z=0,
\]

with `z` in a compact interval `I`,

\[
\rho\ge0,\qquad \int_\Omega\rho=m>0,\qquad
\sup_{t\ge T}\|\rho(t)\|_2\le K,
\]

and explicitly

\[
F(z_*)=0,\qquad (s-z_*)F(s)\le-\beta|s-z_*|^q.
\]

For `q=2`, the signal decays exponentially. For `q>2`, with `R=max_I |s-z_*|`, define

\[
\Gamma_q=\max\{A+B_q\beta^{-2/q},1,|\Omega|R^2\},\qquad
c_q=\Gamma_q^{-q/2}.
\]

Then

\[
\|z(t)-z_*\|_2
\le
\Big(\|z(T)-z_*\|_2^{-(q-2)}+(q-2)c_q(t-T)\Big)^{-1/(q-2)}
\]

on the nonzero branch. If the energy reaches zero, it remains zero thereafter because the energy is nonincreasing.

The theorem uses no evolution equation for the weight `rho`.

## 3. Eventual finite Lp control implies full exponential stabilization

For

\[
u_t=\Delta(\varphi(v)u),\qquad v_t=\Delta v+uF(v),
\]

assume positive conserved mass, an invariant compact signal interval with `min phi > 0`, and for some finite

\[
p>\max\{n,2\},\qquad \sup_{t\ge T}\|u(t)\|_p\le U_p.
\]

If

\[
F(v_*)=0,\qquad (s-v_*)F(s)\le-\beta(s-v_*)^2,
\]

then

\[
\|u(t)-\bar u_0\|_\infty+\|v(t)-v_*\|_{W^{1,\infty}}
\le Ce^{-\lambda(t-T)},\qquad t\ge T+2.
\]

This strictly weakens the previous abstract hypothesis `sup ||u||_infty < infinity` to eventual finite `Lp` control.

## 4. Degenerate kinetics: algebraic full stabilization

Under the same eventual `Lp` condition, assume explicitly `F(v_*)=0` and

\[
(s-v_*)F(s)\le-\beta|s-v_*|^{2+\theta},\qquad \theta>0.
\]

Then

\[
\|v(t)-v_*\|_2=O((1+t-T)^{-1/\theta}).
\]

Moreover, for every

\[
0<\mu<\frac1\theta\min\left\{1,\frac{2(p-n)}{pn}\right\},
\]

\[
\|u(t)-\bar u_0\|_\infty+\|v(t)-v_*\|_{W^{1,\infty}}
=O((1+t-T)^{-\mu}).
\]

## 5. Sharpness

For

\[
F(s)=-\kappa(s-v_*)|s-v_*|^\theta,
\]

the signed homogeneous ODE profile satisfies

\[
|v(t)-v_*|=
\left(|w_0|^{-\theta}+\theta\kappa\bar u_0t\right)^{-1/\theta}.
\]

Lean verifies this exact absolute-value profile for arbitrary nonzero signed initial deviation. The PDE statement that spatially homogeneous data remain homogeneous still requires the corresponding PDE uniqueness/invariance infrastructure.

## 6. Concrete applications

- Qin-Zheng production-consumption bounded solutions: the published uniform `L-infinity` bound implies the strengthened eventual finite `Lp` hypothesis for every finite `p`, hence full exponential stabilization.
- Superlinear consumption `v_t = Delta v - u v^m`, `m>1`: on the nonnegative signal range use `F(s)=-s|s|^{m-1}`. Then `theta=m-1`, giving signal `L2` decay of order `t^{-1/(m-1)}` and the corresponding full uniform algebraic rate under eventual finite `Lp` control.

## 7. Prior-art status

Targeted searches located nearby work on linear consumption, production-consumption stabilization with classical Keller-Segel flux, Qin-Zheng boundedness, and superlinear-consumption global solution theory. No theorem identical to the abstract fixed-mass time-dependent weighted-damping rate dichotomy, the eventual finite-`Lp` full stabilization theorem, or the algebraic-rate/sharpness package was located in this audit.

Evidence state: **Observed/promising novelty, not certified exhaustive novelty.**

## 8. Lean verification status

The current formal tree is verified at commit
`8af07749fe733276054660a732bceaed8a86da4c`, GitHub Actions run
`34586143612` (run 290). The proof-hygiene gate passed and the complete root build finished with

```text
Build completed successfully (8800 jobs).
```

The root `formal/AMLStabilization.lean` imports **92 AMLStabilization modules**.

The current kernel-checked strengthening includes:

- arbitrary-real-`q` weighted Holder and nonlinear mass-weighted coercivity;
- arbitrary `q>2` Bihari integration including the zero-energy branch;
- general quadratic/exponential and superquadratic/polynomial weighted-damping endpoints;
- the `q=theta+2` degenerate endpoint with energy exponent `2/theta` and signal exponent `1/theta`;
- compact-positive-factor derivation of degenerate dissipativity for arbitrary real `theta>0`;
- exact eventual finite-`Lp` rate optimization and mixed time exponent `Q=4p/(p-n)`;
- direct superlinear-consumption signal specialization and signed sharpness;
- dominated differentiation of spatial energies;
- rectangular-box divergence theorem applications giving zero-flux mass conservation, Green's first identity, and cross Green identities;
- pointwise-PDE-to-integrated-pairing and time-dependent box signal-energy endpoints;
- a genuine multi-dimensional rectangular-box Poincare theorem derived from one-dimensional FTC, independent-copy variance, finite-coordinate telescoping, and product-measure Fubini;
- its square-root and cell-energy forms with `Cp = sqrt(N) C`;
- a direct rectangular-box mass-weighted coercivity bridge with no external geometric Poincare or variance-decomposition hypothesis;
- a global rectangular-box Neumann maximum principle/invariant-range theorem, including contacts on faces, edges, and corners;
- **the concrete rectangular-box motility cell-energy identity for `u_t = Delta(phi(v)u)`**, including dominated time differentiation, cross integration by parts, `grad(phi(v)) = phi'(v) grad v`, Neumann inheritance, integrated finite-gradient Cauchy-Schwarz, drift `MemLp`, and the forcing estimate

```text
||u phi'(v) grad v||_2 <= U L_phi ||grad v||_2;
```

- `BoxMotilityCellScalarInterfaceCore.lean`, which packages the concrete box quantities `Q,dQ,g,H,Cp` and automatically supplies the derivative, nonnegativity, Poincare, and raw energy fields expected by the ODE layer;
- `CellEnergyInterfaceAssemblyCore.lean` and `BoxMotilityCellDecayCore.lean`, which drive exponential/polynomial cell decay directly from the pointwise PDE package and the signal-gradient rate;
- `BoxMotilityFullStabilizationCore.lean`, which connects those concrete box objects to the final rate assembly.

Consequently, at the **rectangular-box** level, the final exponential/polynomial stabilization-rate assembly no longer asks for abstract cell-energy hypotheses such as `hQderiv`, `hPoincare`, or `henergy`. The intentionally retained deep analytic interfaces are now concentrated in:

1. the strong signal rate produced by the Neumann semigroup/mixed-norm regularity argument;
2. the comparison from that strong signal norm to the box signal `L^2` gradient used in the cell forcing;
3. the Choi-type local/parabolic upgrade from cell `L^2` energy and forcing to cell `L^infinity`.

A literal first-principles Lean formalization of the manuscript theorem on an arbitrary smooth bounded Neumann domain is still not claimed. The remaining deep infrastructure is concentrated in:

1. extending the verified box Poincare/divergence/Green/Neumann-maximum-principle/cell-energy machinery to arbitrary smooth Neumann domains and traces;
2. Neumann heat-semigroup `L^p -> W^{1,infinity}` smoothing;
3. Choi's mixed-norm conormal/local boundedness theorem;
4. the exact strong-norm-to-`L^2`-gradient comparison in the manuscript's function-space formulation;
5. PDE uniqueness/invariance for the full spatially homogeneous sharpness reduction.

The correct formal claim is therefore substantially stronger than the old run-254 state: the novel arbitrary-order weighted-damping/coercivity/rate machinery is kernel-checked, and on rectangular boxes the conservative mass/Green identities, geometric Poincare inequality, mass-weighted coercivity, global Neumann invariant range, concrete signal-dependent-motility cell-energy PDE identity, forcing estimate, cell decay, and final stabilization-rate assembly are all formally connected. The arbitrary-smooth-domain geometry and the genuinely deep strong-signal/Choi parabolic estimates remain the boundary.
