# RESEARCH_STATE — AML mass-weighted stabilization project

Date: 2026-09-11
Target journal: Applied Mathematics Letters
Branch: `research/aml-production-consumption-stabilization`

## Seed

Qin–Zheng, *Applied Mathematics Letters* 180 (2026), 109995, studies
\[
\begin{cases}
 u_t=\Delta(\varphi(v)u),\\
 v_t=\Delta v+u-\alpha uv,
\end{cases}
\]
with `partial_nu u = partial_nu v = 0` on a smooth bounded domain in `R^n`, `n >= 1`, and proves global classical boundedness under an explicit motility condition for positive decreasing \(\varphi\).

## Current strongest theorem

Consider
\[
 u_t=\Delta(\varphi(v)u),
 \qquad
 v_t=\Delta v+uF(v)
\]
on a smooth bounded connected domain \(\Omega\subset\mathbb R^n\), \(n\ge1\), with homogeneous Neumann boundary conditions. Assume:

- \(m=\int_\Omega u_0>0\);
- the signal remains in a compact interval \(I\);
- \(\varphi\in C^1(I)\) and \(\min_I\varphi>0\);
- for some finite \(p>\max\{n,2\}\), \(T\ge0\),
  \[
  \sup_{t\ge T}\|u(t)\|_p<\infty;
  \]
- \(F\in C^1(I)\), \(F(v_*)=0\) for some \(v_*\in I\).

The proof splits by damping order.

### Quadratic branch

If
\[
(s-v_*)F(s)\le-\beta|s-v_*|^2,
\]
then
\[
\boxed{
\|u(t)-\bar u_0\|_{L^\infty}
+\|v(t)-v_*\|_{W^{1,\infty}}
\le Ce^{-\lambda(t-T)}
}
\qquad (t\ge T+2).
\]

### Degenerate branch

If for some \(\theta>0\),
\[
(s-v_*)F(s)\le-\beta|s-v_*|^{2+\theta},
\]
then
\[
\|v(t)-v_*\|_2=O((1+t-T)^{-1/\theta}),
\]
and for every
\[
0<\mu<\frac1\theta
\min\left\{1,\frac{2(p-n)}{pn}\right\},
\]
\[
\boxed{
\|u(t)-\bar u_0\|_{L^\infty}
+\|v(t)-v_*\|_{W^{1,\infty}}
=O((1+t-T)^{-\mu}).
}
\]

Evidence status: **proof chain line-checked in the manuscript**. Novelty status remains **Observed**, not certified.

## Structural core

### 1. Nonlinear mass-weighted coercivity

For every \(q\ge2\), \(\rho\ge0\), \(\int\rho=m>0\), \(\|\rho\|_2\le K\),
\[
\|f\|_2^2
\le A\|\nabla f\|_2^2
+B_q\left(\int_\Omega\rho|f|^q\right)^{2/q},
\]
with
\[
A=C_P^2\left(1+\frac{2|\Omega|K^2}{m^2}\right),
\qquad
B_q=2|\Omega|m^{-2/q}.
\]

### 2. Weighted-damping rate dichotomy

For
\[
z_t=\Delta z+\rho(x,t)F(z)
\]
with fixed positive mass and only a uniform \(L^2\) bound on \(\rho\), the coercivity estimate closes the signal energy without using any evolution law for \(\rho\). Quadratic damping gives exponential decay; order \(q>2\) gives \(t^{-1/(q-2)}\).

### 3. Finite-`L^p` transfer to strong norms

An eventual finite \(L^p\) bound with \(p>\max\{n,2\}\) is enough to control the reaction source in some \(L^r\), \(r>n\). Unit-interval Neumann semigroup smoothing gives the strong signal rate. A cell energy estimate gives \(L^2\) decay of \(u-\bar u_0\).

### 4. Direct `L^infinity` cell upgrade

Write
\[
q_t-\nabla\cdot(a\nabla q)=\nabla\cdot B,
\qquad
a=\varphi(v),
\qquad
B=u\varphi'(v)\nabla v,
\]
with the exact conormal boundary condition
\[
(a\nabla q+B)\cdot\nu=0.
\]
For \(n\ge2\), Choi 2016, Theorem 1.1, gives the required fixed-radius local boundedness estimate because all lower-order coefficients vanish and \(B\in L_t^{Q_*}L_x^p\) with
\[
Q_*=\frac{4p}{p-n},
\qquad
\frac np+\frac2{Q_*}<1.
\]

Choi states the Neumann theorem for spatial dimension \(d\ge2\). The manuscript closes \(n=1\) separately: on an interval, the mixed-norm embedding used in Choi's De Giorgi iteration follows from the one-dimensional Gagliardo--Nirenberg inequality whenever
\[
\frac1P+\frac2Q=\frac12.
\]
The lower measure bound is automatic, and the remaining lower-order-free iteration is unchanged. Thus the full theorem retains \(n\ge1\).

## Applications

### Qin–Zheng production--consumption

For
\[
F(s)=1-\alpha s,
\qquad v_*=1/\alpha,
\]
\[
(s-v_*)F(s)=-\alpha(s-v_*)^2.
\]
The maximum principle gives the invariant signal interval
\[
0\le v(x,t)\le\max\left\{\|v_0\|_\infty,\frac1\alpha\right\},
\]
and Qin--Zheng's uniform boundedness theorem supplies the finite-`L^p` hypothesis for every finite \(p\). Hence their bounded solutions stabilize exponentially for every \(n\ge1\). The stabilization implication itself does **not** use \(\varphi'<0\).

### Superlinear consumption

For \(F(s)=-s^m\), \(m>1\), the degenerate branch has \(\theta=m-1\), giving the exact signal exponent \(1/(m-1)\) and the corresponding full-rate threshold.

### Sharpness

For
\[
F(s)=-\kappa(s-v_*)|s-v_*|^\theta,
\]
spatially homogeneous data satisfy
\[
|v(t)-v_*|
=\left(|w_0|^{-\theta}+\theta\kappa\bar u_0 t\right)^{-1/\theta}.
\]
This certifies sharpness of the signal exponent \(1/\theta\), not of the full strong-norm threshold.

## Novelty posture

Material predecessors remain essential:

- Li–Zhao 2021: direct pure-consumption signal-dependent motility with exponential large-time behavior;
- Tao–Winkler 2025: simultaneous production--consumption with classical chemotactic sensitivity;
- Qin–Zheng 2026: exact production--consumption signal-dependent-motility system with global boundedness.

Safe contribution architecture:

1. nonlinear mass-weighted coercivity as the mechanism;
2. abstract quadratic/superquadratic rate dichotomy;
3. eventual finite-`L^p` rather than uniform-`L^infinity` input for full stabilization;
4. explicit algebraic strong-norm threshold;
5. Qin–Zheng exponential corollary and superlinear-consumption algebraic corollary;
6. homogeneous sharpness for the signal exponent.

## Current priority

The manuscript proof chain is closed for `n >= 1` after the 2026-09-11 hardening pass. Next priorities are:

1. fresh theorem-to-theorem novelty/referee audit;
2. LaTeX compile and AML page-count compression;
3. bibliography/source audit, especially the original Neumann semigroup source;
4. author/funding/submission metadata.
