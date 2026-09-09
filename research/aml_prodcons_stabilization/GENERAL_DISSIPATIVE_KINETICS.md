# GENERAL_DISSIPATIVE_KINETICS — strengthened theorem

Date: 2026-09-09

## General system

Consider
\[
\begin{cases}
 u_t=\Delta(\varphi(v)u),\\
 v_t=\Delta v+uF(v),
\end{cases}
\qquad x\in\Omega,\ t>0,
\]
with homogeneous Neumann boundary conditions on a smooth bounded connected domain \(\Omega\subset\mathbb R^n\).

Assume that a global nonnegative classical solution satisfies
\[
\int_\Omega u_0=m>0,
\qquad
\sup_{t>0}\|u(t)\|_\infty\le U<\infty,
\]
and that the signal range is contained in a compact interval \(I\subset\mathbb R\).

Let
\[
\varphi\in C^1(I),\qquad \min_I\varphi>0,
\]
and suppose that \(F\in C^1(I)\) possesses an equilibrium \(v_*\in I\) and a constant \(\beta>0\) such that
\[
F(v_*)=0
\tag{E}
\]
and
\[
(s-v_*)F(s)\le-\beta(s-v_*)^2
\qquad\text{for all }s\in I.
\tag{D}
\]
Condition (D) is a uniform one-sided dissipativity condition toward the equilibrium \(v_*\). The root condition (E) is stated explicitly because (D) alone does not force \(F(v_*)=0\) when \(v_*\) is an endpoint of \(I\).

## Theorem B — general boundedness-to-stabilization principle

Under the above assumptions, for every \(p\in[1,\infty)\) there exist \(C_p,\lambda_p>0\) such that
\[
\|u(t)-\bar u_0\|_{L^p(\Omega)}
+\|v(t)-v_*\|_{W^{1,\infty}(\Omega)}
\le C_p e^{-\lambda_p t},
\qquad t\ge1,
\]
where
\[
\bar u_0=\frac{m}{|\Omega|}.
\]
No monotonicity assumption on \(\varphi\) is required for this stabilization implication.

Moreover, the first signal-decay step needs only a uniform \(L^2\)-bound for \(u\): if
\[
\sup_{t>0}\|u(t)\|_2\le K<\infty,
\]
then
\[
\|v(t)-v_*\|_2\le Ce^{-\lambda t}.
\]

## Proof

### 1. Coercivity with only an \(L^2\)-bound on \(u\)

Mass conservation gives \(\int u(t)=m\). If \(\|u(t)\|_2\le K\), then for \(f\in H^1(\Omega)\),
\[
\begin{aligned}
m|f_\Omega|
&\le \left|\int uf\right|+\left|\int u(f_\Omega-f)\right|\\
&\le \sqrt m\left(\int uf^2\right)^{1/2}+K\|f-f_\Omega\|_2\\
&\le \sqrt m\left(\int uf^2\right)^{1/2}+KC_P\|\nabla f\|_2.
\end{aligned}
\]
Thus
\[
\|f\|_2^2\le C_{\Omega,m,K}\left(\|\nabla f\|_2^2+\int uf^2\right).
\tag{P}
\]
This is the only place where spatial concentration of \(u\) enters the signal-energy argument.

### 2. Signal \(L^2\)-decay from dissipativity

Set \(w=v-v_*\). Testing
\[
w_t=\Delta w+uF(v)
\]
by \(w\) and using (D),
\[
\frac12\frac d{dt}\|w\|_2^2+\|\nabla w\|_2^2
=\int uF(v)w
\le-\beta\int uw^2.
\]
By (P),
\[
\|\nabla w\|_2^2+\beta\int uw^2\ge c\|w\|_2^2,
\]
and hence
\[
\|w(t)\|_2\le Ce^{-\lambda_0t}.
\tag{S2}
\]

### 3. Signal \(W^{1,\infty}\)-decay under boundedness

Now assume \(u\) is uniformly bounded in \(L^\infty\). Since \(v\in I\), \(w\) is uniformly bounded. By interpolation, for every \(r\ge2\),
\[
\|w(t)\|_r\le C_r e^{-2\lambda_0t/r}.
\]
By (E) and \(F\in C^1(I)\),
\[
|F(v)|\le L_F|w|
\]
with \(L_F=\max_I|F'|\). Therefore
\[
\|uF(v)\|_r\le UL_F\|w\|_r\le C_re^{-\mu_rt}.
\]
Choose \(r>n\). Duhamel's formula on a fixed half-unit interval and the standard Neumann heat-semigroup estimate
\[
\|\nabla e^{\tau\Delta}f\|_\infty
\le C\left(1+\tau^{-\frac12-\frac n{2r}}\right)e^{-\lambda_1\tau}\|f\|_r
\]
yield
\[
\|\nabla w(t)\|_\infty\le Ce^{-\lambda_vt}.
\]
The spatial mean of \(w\) decays by (S2), so the \(W^{1,\infty}\)-Poincaré inequality yields
\[
\|w(t)\|_{W^{1,\infty}}\le Ce^{-\lambda_vt}.
\tag{Sinf}
\]

### 4. Cell-density \(L^2\)-decay

Let \(q=u-\bar u_0\), so \(\int q=0\). Set
\[
\varphi_*:=\min_I\varphi>0,
\qquad L_\varphi:=\max_I|\varphi'|.
\]
Then
\[
\frac12\frac d{dt}\|q\|_2^2
=-\int\varphi(v)|\nabla q|^2
-\int u\varphi'(v)\nabla q\cdot\nabla v.
\]
Young's inequality and (Sinf) imply
\[
\frac d{dt}\|q\|_2^2+c\|q\|_2^2\le Ce^{-2\lambda_vt},
\]
where Poincaré was used for \(q\). Hence
\[
\|q(t)\|_2\le Ce^{-\lambda_ut}.
\tag{U2}
\]

### 5. Every finite \(L^p\)

Since \(q\) is uniformly bounded in \(L^\infty\), interpolation between (U2) and \(L^\infty\) yields exponential decay in every finite \(L^p\), \(p\ge2\); bounded-domain Hölder gives the result for \(1\le p<2\).

This proves Theorem B.

## Two important special cases

### Production–consumption T-cell kinetics

\[
F(s)=1-\alpha s,
\qquad v_*=\frac1\alpha.
\]
Then
\[
F(v_*)=0,
\qquad
(s-v_*)F(s)=-\alpha(s-v_*)^2,
\]
so (E)–(D) hold with \(\beta=\alpha\). This recovers the exact Qin–Zheng 2026 model at the stabilization stage.

### Pure signal consumption

\[
F(s)=-s,
\qquad v_*=0,
\]
so
\[
F(v_*)=0,
\qquad
sF(s)=-s^2.
\]
This contains the direct signal-consumption model studied by Li–Zhao (ZAMP 2021) at the level of the stabilization mechanism.

## Why this strengthening matters for AML

The intended contribution is no longer merely an asymptotic add-on to one 2026 paper. The theorem isolates a general mechanism:

\[
\boxed{\text{mass + boundedness + dissipative signal kinetics}
\Longrightarrow \text{exponential stabilization}}
\]

for signal-dependent motility, independently of the sign of \(\varphi'\) in the stabilization implication.

The exact production–consumption model is then a timely application/corollary rather than the whole theorem.

## Novelty status

Observed/promising only. A fresh prior-art search is required specifically for abstract systems of the form
\[
u_t=\Delta(\varphi(v)u),\qquad v_t=\Delta v+uF(v)
\]
with boundedness-to-stabilization conclusions before this theorem can be described as new.
