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
with homogeneous no-flux/Neumann boundary conditions on a smooth bounded connected domain \(\Omega\subset\mathbb R^n\).

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
Condition (D) is a uniform one-sided dissipativity condition toward \(v_*\). The root condition (E) is explicit because (D) alone does not force \(F(v_*)=0\) when \(v_*\) is an endpoint of \(I\).

## Theorem B — boundedness-to-uniform-stabilization principle

Under the above assumptions, there exist \(C,\lambda>0\) such that
\[
\boxed{
\|u(t)-\bar u_0\|_{L^\infty(\Omega)}
+\|v(t)-v_*\|_{W^{1,\infty}(\Omega)}
\le C e^{-\lambda t}
}
\qquad t\ge2,
\tag{T}
\]
where
\[
\bar u_0=\frac{m}{|\Omega|}.
\]
In particular, exponential convergence holds in every finite \(L^p\)-norm as well. No monotonicity assumption on \(\varphi\) is required for this stabilization implication.

Moreover, the first signal-decay step needs only a uniform \(L^2\)-bound for \(u\): if
\[
\sup_{t>0}\|u(t)\|_2\le K<\infty,
\]
then
\[
\|v(t)-v_*\|_2\le Ce^{-\lambda t}.
\]

## Proof

### 1. Mass-weighted coercivity

Mass conservation gives \(\int_\Omega u(t)=m\). If \(\|u(t)\|_2\le K\), then for \(f\in H^1(\Omega)\),
\[
\begin{aligned}
m|f_\Omega|
&\le \left|\int uf\right|+\left|\int u(f_\Omega-f)\right|\\
&\le \sqrt m\left(\int uf^2\right)^{1/2}+K\|f-f_\Omega\|_2\\
&\le \sqrt m\left(\int uf^2\right)^{1/2}+KC_P\|\nabla f\|_2.
\end{aligned}
\]
Hence
\[
\|f\|_2^2\le C_{\Omega,m,K}\left(\|\nabla f\|_2^2+\int uf^2\right).
\tag{P}
\]

### 2. Signal \(L^2\)-decay

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
and thus
\[
\|w(t)\|_2\le Ce^{-\lambda_0t}.
\tag{S2}
\]

### 3. Signal \(W^{1,\infty}\)-decay

Assume now the uniform \(L^\infty\)-bound on \(u\). Since \(v\in I\), \(w\) is uniformly bounded. Interpolation gives, for every \(r\ge2\),
\[
\|w(t)\|_r\le C_r e^{-2\lambda_0t/r}.
\]
By (E) and \(F\in C^1(I)\),
\[
|F(v)|\le L_F|w|,
\qquad L_F=\max_I|F'|,
\]
so \(\|uF(v)\|_r\le C_r e^{-\mu_rt}\). Choose \(r>n\). Duhamel on a fixed half-unit interval and the standard Neumann heat-semigroup gradient estimate
\[
\|\nabla e^{\tau\Delta}f\|_\infty
\le C\left(1+\tau^{-\frac12-\frac n{2r}}\right)e^{-\lambda_1\tau}\|f\|_r
\]
then yield
\[
\|\nabla w(t)\|_\infty\le Ce^{-\lambda_vt}.
\]
Together with the decay of the spatial mean from (S2),
\[
\|w(t)\|_{W^{1,\infty}}\le Ce^{-\lambda_vt}.
\tag{Sinf}
\]

### 4. Cell-density \(L^2\)-decay

Let \(q=u-\bar u_0\), so \(\int_\Omega q=0\), and set
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
Young, (Sinf), and Poincare imply
\[
\frac d{dt}\|q\|_2^2+c\|q\|_2^2\le Ce^{-2\lambda_vt},
\]
so
\[
\|q(t)\|_2\le Ce^{-\lambda_ut}.
\tag{U2}
\]

### 5. Uniform \(L^\infty\)-decay of the cell density

Rewrite the first equation as
\[
q_t-\nabla\cdot(a(x,t)\nabla q)=\nabla\cdot B(x,t),
\tag{Q}
\]
where
\[
a(x,t)=\varphi(v(x,t)),
\qquad
B(x,t)=u(x,t)\varphi'(v(x,t))\nabla v(x,t).
\]
The no-flux boundary condition is precisely
\[
(a\nabla q+B)\cdot\nu=0.
\]
Because the signal remains in \(I\),
\[
0<\varphi_*\le a(x,t)\le \varphi^*:=\max_I\varphi,
\]
so (Q) is uniformly parabolic with time-uniform ellipticity constants. By (Sinf),
\[
\|B(t)\|_\infty\le U L_\varphi\|\nabla v(t)\|_\infty
\le Ce^{-\lambda_vt}.
\tag{Binf}
\]

Apply the boundary local boundedness estimate of J. Choi, *Bull. Korean Math. Soc.* 53 (2016), Theorem 1.1, to (Q) on backward cylinders ending at time \(t\). Choose finite exponents \(p_1>n\), \(q_1>2\) with
\[
\frac n{p_1}+\frac2{q_1}<1.
\]
Since the lower-order coefficients vanish, the admissible radius in that theorem is uniform in time. For a fixed sufficiently small radius \(r_0>0\), the theorem gives, locally up to the Neumann boundary,
\[
\|q\|_{L^\infty(Q_{r_0/2})}
\le C\|q\|_{L^2(Q_{r_0})}
+C\|B\|_{L^{p_1,q_1}(Q_{r_0})},
\tag{LB}
\]
where powers of the fixed radius are absorbed into \(C\).

By (U2), for cylinders contained in \(\Omega\times(t-r_0^2,t)\),
\[
\|q\|_{L^2(Q_{r_0})}\le Ce^{-\lambda_u(t-r_0^2)},
\]
while (Binf) gives
\[
\|B\|_{L^{p_1,q_1}(Q_{r_0})}\le Ce^{-\lambda_v(t-r_0^2)}.
\]
A finite covering of the bounded domain by such spatial neighborhoods therefore yields
\[
\|q(t)\|_\infty\le Ce^{-\lambda_\infty t}
\qquad (t\ge2)
\tag{Uinf}
\]
for some \(\lambda_\infty>0\). Combining (Uinf) with (Sinf) proves (T).

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
so (E)–(D) hold with \(\beta=\alpha\). Hence every uniformly bounded classical solution of the exact Qin–Zheng 2026 model converges exponentially in
\[
L^\infty(\Omega)\times W^{1,\infty}(\Omega)
\]
to \((\bar u_0,1/\alpha)\).

### Pure signal consumption

\[
F(s)=-s,
\qquad v_*=0,
\]
so
\[
F(v_*)=0,
\qquad sF(s)=-s^2.
\]
This contains the direct signal-consumption law studied by Li–Zhao (ZAMP 2021) at the level of the stabilization mechanism.

## Citation used in the uniform upgrade

J. Choi, *Note on local estimates for weak solution of boundary value problem for second order parabolic equation*, Bull. Korean Math. Soc. 53 (2016), 1123–1148, Theorem 1.1, DOI 10.4134/BKMS.b150567.

## Novelty status

Mathematical status of Theorem B: **Proved**, subject to ordinary manuscript-level line checking and source verification.

Novelty status: **Observed/promising, not certified**. The deep audit has not located the same abstract theorem or an exact-model exponential-stabilization result, but pure-consumption and indirect-signal predecessors remain material prior art and must be compared explicitly before submission freeze.
