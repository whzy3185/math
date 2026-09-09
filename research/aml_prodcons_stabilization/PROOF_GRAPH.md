# PROOF_GRAPH — boundedness implies exponential stabilization

## Main target T0

For the production–consumption system
\[
u_t=\Delta(\varphi(v)u),\qquad v_t=\Delta v+u-\alpha uv,
\]
prove that any nonnegative global classical solution with \(u_0\not\equiv0\) and \(\sup_t\|u(t)\|_\infty<\infty\) converges exponentially to
\[
\left(\bar u_0,\frac1\alpha\right),
\qquad \bar u_0=|\Omega|^{-1}\int_\Omega u_0,
\]
under \(\varphi>0\) and sufficient smoothness, without assuming \(\varphi'<0\).

## DAG

### P1 — mass and invariant range
Status: **Proved**

- \(m:=\int u(t)=\int u_0>0\).
- \(0\le v\le M:=\max\{\|v_0\|_\infty,1/\alpha\}\).
- Hence \(\varphi_*:=\min_{[0,M]}\varphi>0\), while \(\max_{[0,M]}|\varphi'|<\infty\).

### P2 — weighted coercivity
Status: **Proved**
Depends on: P1 and \(U:=\sup_t\|u(t)\|_\infty<\infty\).

For all \(f\in H^1(\Omega)\),
\[
\|f\|_2^2\le C_{\Omega,m,U}\left(\|\nabla f\|_2^2+\int u(t)f^2\right)
\]
uniformly in \(t\).

This replaces the earlier, more expensive route via eventual pointwise positivity of \(u\).

### P3 — exact signal dissipation
Status: **Proved**
Depends on: P1.

For \(w=v-1/\alpha\),
\[
w_t=\Delta w-\alpha u w
\]
and
\[
\frac12\frac d{dt}\|w\|_2^2+\|\nabla w\|_2^2+\alpha\int u w^2=0.
\]

### P4 — exponential \(L^2\) signal decay
Status: **Proved**
Depends on: P2, P3.

With \(\delta=\min\{1,\alpha\}\),
\[
\|\nabla w\|_2^2+\alpha\int u w^2
\ge \delta C_{\Omega,m,U}^{-1}\|w\|_2^2.
\]
Hence \(\|w(t)\|_2\le Ce^{-\lambda_v t}\).

### P5 — exponential \(W^{1,\infty}\) signal decay
Status: **Observed; proof route complete modulo source pinning**
Depends on: P4, boundedness of \(u,w\), standard Neumann heat-semigroup smoothing.

Choose \(p>n\). Since \(w\) is uniformly bounded and decays in \(L^2\), interpolation gives
\[
\|w(t)\|_p\le C e^{-\mu t}.
\]
For \(t\ge1\), Duhamel on \([t-1/2,t]\) gives
\[
w(t)=e^{\frac12\Delta}w(t-1/2)
-\alpha\int_{t-1/2}^t e^{(t-s)\Delta}(u(s)w(s))\,ds.
\]
Use
\[
\|\nabla e^{\tau\Delta}f\|_\infty
\le C\bigl(1+\tau^{-\frac12-\frac n{2p}}\bigr)\|f\|_p,
\]
whose singularity is integrable because \(p>n\). Together with \(\|uw\|_p\le U\|w\|_p\), this yields
\[
\|w(t)\|_{W^{1,\infty}}\le Ce^{-\mu t}.
\]

### P6 — exponential \(L^2\) cell-density decay
Status: **Observed**
Depends on: P1, P5.

Let \(q=u-\bar u_0\), so \(\int q=0\). Then
\[
\frac12\frac d{dt}\|q\|_2^2
=-\int\varphi(v)|\nabla u|^2
-\int u\varphi'(v)\nabla u\cdot\nabla v.
\]
Using \(\varphi(v)\ge\varphi_*>0\), bounded \(u\), bounded \(\varphi'\), and Young,
\[
\frac d{dt}\|q\|_2^2
\le -\varphi_*\|\nabla u\|_2^2+C\|\nabla v\|_2^2.
\]
Poincaré and P5 imply
\[
\frac d{dt}\|q\|_2^2+c\|q\|_2^2\le Ce^{-2\mu t},
\]
hence exponential \(L^2\)-decay.

### P7 — exponential \(L^\infty\) cell-density decay
Status: **Observed; current highest proof dependency**
Depends on: P6 and a uniform-in-time parabolic Hölder/smoothing estimate for bounded solutions of the uniformly parabolic first equation.

Preferred short route for AML:
- bounded \(u\) + bounded \(\nabla v\) imply uniform parabolic Hölder regularity \(\sup_{t\ge1}\|u(t)\|_{C^\theta}<\infty\) for some \(\theta\in(0,1)\);
- interpolate \(C^\theta\) with exponentially decaying \(L^2\):
\[
\|q(t)\|_\infty
\le C\|q(t)\|_{C^\theta}^{\frac n{n+2\theta}}
\|q(t)\|_2^{\frac{2\theta}{n+2\theta}},
\]
which preserves exponential decay with a smaller rate.

Need: pin an exact theorem/reference or provide a compact self-contained smoothing lemma.

### P8 — monotonicity removal
Status: **Observed**
Depends on: P5–P7.

No step after boundedness uses the sign of \(\varphi'\). The argument only uses positivity of \(\varphi\) on the bounded signal range and boundedness of \(\varphi'\). Thus the conditional stabilization principle should extend to positive non-monotone motilities.

### P9 — Qin–Zheng corollary
Status: **Observed**
Depends on: T0 plus their 2026 boundedness theorem.

Their assumptions imply the boundedness hypothesis of T0, yielding exponential stabilization as a new large-time conclusion for their exact model.

## Failed / superseded route

**Eventual positivity route:** prove \(\inf_x u(x,t)\ge c>0\) via Harnack and then damp \(w\) pointwise.

Status: superseded, not needed. The weighted coercivity P2 is elementary, dimension-free, and avoids an additional regularity/Harnack dependency.
