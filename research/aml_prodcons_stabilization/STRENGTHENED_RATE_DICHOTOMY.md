# Strengthened rate-dichotomy theorem package

Date: 2026-09-10
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

spatially homogeneous data remain homogeneous and satisfy

\[
|v(t)-v_*|=
\left(|w_0|^{-\theta}+\theta\kappa\bar u_0t\right)^{-1/\theta}.
\]

Hence the signal exponent `1/theta` is optimal in general.

## 6. Concrete applications

- Qin-Zheng production-consumption bounded solutions: the published uniform `L-infinity` bound implies the strengthened eventual finite `Lp` hypothesis for every finite `p`, hence full exponential stabilization.
- Superlinear consumption `v_t = Delta v - u v^m`, `m>1`: on the nonnegative signal range use the `C1(R)` extension `F(s)=-s|s|^{m-1}`. Then `theta=m-1`, giving signal `L2` decay of order `t^{-1/(m-1)}` and the corresponding full uniform algebraic rate under eventual finite `Lp` control.

## 7. Prior-art status

Targeted searches on 2026-09-10 located nearby work on linear consumption, production-consumption stabilization with classical Keller-Segel flux, Qin-Zheng boundedness, and superlinear-consumption global solution theory. No theorem identical to the abstract fixed-mass time-dependent weighted-damping rate dichotomy, the eventual finite-`Lp` full stabilization theorem, or the algebraic-rate/sharpness package was located in this audit.

Evidence state: **Observed/promising novelty, not certified exhaustive novelty.**

## 8. Lean verification status

The current formal tree is verified at commit
`16fce36272273430fa31fe3fdb18f66b3e29941b`, GitHub Actions run
`34448754427` (run 150).  The proof-hygiene gate passed and the complete root
build finished with

```text
Build completed successfully (8752 jobs).
```

The root `formal/AMLStabilization.lean` imports **45 AMLStabilization modules**.
The current kernel-checked strengthening includes substantially more than the
older representative `q=4` branch:

- genuine arbitrary-real-`q` weighted Holder and nonlinear mass-weighted coercivity;
- arbitrary `q>2` Bihari integration, including the zero-energy branch;
- general quadratic/exponential and superquadratic/polynomial weighted-damping endpoints;
- a manuscript-facing `q=theta+2` degenerate endpoint with energy exponent `2/theta` and signal exponent `1/theta`;
- compact-positive-factor derivation of quantitative degenerate dissipativity for arbitrary real `theta>0`;
- finite-measure `L^p -> L^2`, Holder-product, and bounded-interpolation machinery;
- exact construction of an admissible spatial exponent for every `0 < mu < (1/theta) min{1,2(p-n)/(pn)}`;
- explicit mixed time exponent `Q=4p/(p-n)` satisfying `Q>2` and `n/p+2/Q<1`, including the one-dimensional cylinder-lift specialization;
- forced cell-energy exponential/polynomial decay, energy-to-norm conversion, and final full-rate assembly conditional on the named deep parabolic interfaces;
- direct superlinear-consumption specialization `F(s)=-s|s|^(m-1)` into the arbitrary-order signal theorem;
- signed sharpness with the exact absolute-value profile `|w(t)|=(|w0|^(-theta)+theta*k*t)^(-1/theta)`;
- scalar mass-conservation propagation and dominated differentiation of spatial integrals;
- **box-level Neumann geometry from mathlib's divergence theorem**: zero face flux gives zero total divergence, conservation laws give exact mass conservation, and zero normal derivative plus the local product rule gives Green's first identity.

This last item moves a genuine part of the PDE boundary below the abstract-interface level.  On rectangular boxes, the global flux and Green identities are now derived rather than assumed.

A literal first-principles Lean formalization of the manuscript theorem on an arbitrary smooth bounded Neumann domain is still not claimed.  The remaining deep infrastructure is concentrated in:

1. geometric Poincare theory in the manuscript's exact Sobolev setting;
2. extension of the now-verified box divergence/Green theory to arbitrary smooth Neumann domains and traces;
3. the invariant signal interval / maximum-principle argument;
4. Neumann heat-semigroup `L^p -> W^{1,infinity}` smoothing;
5. Choi's mixed-norm conormal/local boundedness theorem in the required arbitrary-domain setting;
6. the concrete function-space derivation of the cell-density PDE energy identity.

The correct formal claim is therefore stronger than before but still precise: the novel arbitrary-order weighted-damping/coercivity/rate machinery and the final stabilization-rate assembly are kernel-checked conditional on named deep analytic inputs; in addition, the conservative mass and Green identities are fully derived on rectangular boxes from mathlib's Bochner divergence theorem.  The arbitrary-smooth-domain geometric/parabolic infrastructure remains the genuine boundary.
