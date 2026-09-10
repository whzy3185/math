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

The strengthened Lean tree is verified at commit `499e78401b3667636242385f5aa0d51b836cd2a6`, GitHub Actions run `34428439465`, with the proof-hygiene gate passing and `Build completed successfully (8719 jobs)`.

Two new modules are compiled:

- `PolynomialEnergyDecay.lean`: representative `q=4` / `theta=2` algebraic branch, including reciprocal-energy monotonicity, explicit inverse-linear energy decay, quartic coercivity-to-dissipation, and the cubic-degenerate identity.
- `LpExponentCore.lean`: concrete `r` and Holder-partner `s` selection from `p>max{n,2}`, exact identity `1/r=1/p+1/s`, `s>2`, and positivity of the transfer-rate exponent.

The arbitrary-real-`q` Holder/coercivity theorem and the full parabolic `Lp` PDE regularity assembly remain paper-level proofs. The full strengthened `L-infinity x W^{1,infinity}` theorem is therefore **not** claimed to be fully Lean-verified.
