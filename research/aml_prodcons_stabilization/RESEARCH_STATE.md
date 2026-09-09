# RESEARCH_STATE — AML production–consumption stabilization

Date: 2026-09-09
Target journal: Applied Mathematics Letters
Branch: `research/aml-production-consumption-stabilization`

## Seed problem

Study the Neumann problem

\[
\begin{cases}
 u_t=\Delta(\varphi(v)u),\\
 v_t=\Delta v+u-\alpha uv,
\end{cases}
\qquad x\in\Omega,\ t>0,
\]

on a smooth bounded connected domain \(\Omega\subset\mathbb R^n\), with \(\alpha>0\), nonnegative initial data, and \(u_0\not\equiv0\).

Seed 0 is Qin–Zheng, *Applied Mathematics Letters* 180 (2026), 109995, which proves global classical boundedness under an explicit motility smallness condition for positive decreasing \(\varphi\).

## Target theorem (not yet promoted to Proved)

Conditional stabilization target:

> Assume \(\varphi\in C^2([0,\infty))\) and \(\varphi>0\). Let \((u,v)\) be a nonnegative global classical solution with
> \[
> \sup_{t>0}\|u(\cdot,t)\|_{L^\infty(\Omega)}<\infty.
> \]
> Then, with
> \[
> \bar u_0=|\Omega|^{-1}\int_\Omega u_0>0,
> \]
> there exist \(C,\lambda>0\) such that
> \[
> \|u(\cdot,t)-\bar u_0\|_{L^\infty}
> +\left\|v(\cdot,t)-\frac1\alpha\right\|_{W^{1,\infty}}
> \le Ce^{-\lambda t}
> \]
> for all sufficiently large \(t\).

The important strengthening axis is that the stabilization step appears not to require \(\varphi'<0\); positivity of \(\varphi\) on the bounded range of \(v\) is the structural condition.

## Current strongest proved core

Let
\[
w=v-\frac1\alpha,
\qquad m=\int_\Omega u_0>0,
\qquad U=\sup_{t>0}\|u(\cdot,t)\|_\infty<\infty.
\]

Mass conservation gives \(\int_\Omega u(\cdot,t)=m\). The maximum principle gives
\[
0\le v(x,t)\le M:=\max\{\|v_0\|_\infty,\alpha^{-1}\}.
\]
Moreover
\[
w_t=\Delta w-\alpha u w
\]
and therefore
\[
\frac12\frac d{dt}\|w\|_2^2+\|\nabla w\|_2^2+\alpha\int_\Omega u w^2=0.
\]

The previous proposed bottleneck “eventual uniform positivity of \(u\)” is unnecessary. An elementary coercivity lemma closes the \(w\)-energy directly:

If \(\rho\ge0\), \(\int_\Omega\rho=m>0\), and \(\|\rho\|_\infty\le U\), then for every \(f\in H^1(\Omega)\),
\[
\|f\|_2^2\le C_{\Omega,m,U}
\left(\|\nabla f\|_2^2+\int_\Omega\rho f^2\right).
\]

Indeed, writing \(f_\Omega=|\Omega|^{-1}\int_\Omega f\) and using Poincaré,
\[
m|f_\Omega|
\le \sqrt m\left(\int\rho f^2\right)^{1/2}
+\sqrt{Um}\,C_P\|\nabla f\|_2,
\]
which yields the claim after \(\|f\|_2^2\le2\|f-f_\Omega\|_2^2+2|\Omega||f_\Omega|^2\).

Applying this with \(\rho=u(t)\) gives a time-uniform \(c_0>0\) such that
\[
\|\nabla w\|_2^2+\alpha\int u w^2\ge c_0\|w\|_2^2,
\]
so
\[
\|v(\cdot,t)-\alpha^{-1}\|_2\le C e^{-c_0t}.
\]

## Next proof frontier

1. Close the standard Neumann-semigroup upgrade \(w:L^2\to W^{1,\infty}\) using interpolation to \(L^p\), \(p>n\), and Duhamel for \(w_t=\Delta w-\alpha uw\).
2. Use the resulting exponential decay of \(\nabla v\) in the energy estimate for \(q=u-\bar u_0\):
\[
\frac12\frac d{dt}\|q\|_2^2
=-\int\varphi(v)|\nabla u|^2
-\int u\varphi'(v)\nabla u\cdot\nabla v.
\]
Positivity of \(\varphi\) on \([0,M]\), boundedness of \(u\), and Young + Poincaré should give exponential \(L^2\)-decay of \(q\).
3. Close \(L^2\to L^\infty\) for \(q\) by a sourceable uniform parabolic smoothing/Hölder interpolation lemma.
4. Re-run exact-model novelty search before promoting the target theorem.

## Journal fit

The intended AML contribution is a short structural principle rather than a second boundedness proof:

**boundedness implies exponential stabilization** for the 2026 Qin–Zheng production–consumption model, with a stabilization argument that drops monotonicity of the motility function.

No claim of novelty/open status is certified yet.
