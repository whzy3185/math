# PROOF_GRAPH — boundedness implies uniform exponential stabilization

## Main target T0

For
\[
u_t=\Delta(\varphi(v)u),\qquad v_t=\Delta v+uF(v),
\]
prove that every nonnegative global classical solution with positive cell mass and a uniform \(L^\infty\)-bound on \(u\) converges exponentially to \((\bar u_0,v_*)\) in
\[
L^\infty(\Omega)\times W^{1,\infty}(\Omega),
\]
provided \(\varphi>0\) on the signal range and the signal kinetics satisfy
\[
F(v_*)=0,
\qquad
(s-v_*)F(s)\le-\beta(s-v_*)^2.
\]
No sign assumption on \(\varphi'\) is imposed.

Status of T0: **Proved**.

## DAG

### P1 — mass and invariant signal range
Status: **Proved**

Mass is conserved. For the Qin–Zheng reaction \(F(v)=1-\alpha v\), the maximum principle yields
\[
0\le v\le \max\{\|v_0\|_\infty,1/\alpha\}.
\]
For the abstract theorem, a compact invariant signal interval is assumed.

### P2 — mass-weighted coercivity
Status: **Proved**

If \(\rho\ge0\), \(\int\rho=m>0\), and \(\|\rho\|_2\le K\), then
\[
\|f\|_2^2\le C_{\Omega,m,K}
\left(\|\nabla f\|_2^2+\int\rho f^2\right).
\]

### P3 — signal \(L^2\) dissipation
Status: **Proved**
Depends on: P1–P2 and dissipativity.

For \(w=v-v_*\),
\[
\frac12\frac d{dt}\|w\|_2^2+\|\nabla w\|_2^2
\le-\beta\int uw^2,
\]
so
\[
\|w(t)\|_2\le Ce^{-\lambda t}.
\]

### P4 — signal \(W^{1,\infty}\) decay
Status: **Proved**
Depends on: P3, boundedness of \(u\), \(F(v_*)=0\), Neumann heat-semigroup smoothing.

Interpolation gives exponentially decaying \(L^r\)-norms of \(w\). With \(r>n\), Duhamel and the standard gradient estimate imply
\[
\|v(t)-v_*\|_{W^{1,\infty}}\le Ce^{-\lambda_vt}.
\]

### P5 — cell-density \(L^2\) decay
Status: **Proved**
Depends on: P4.

For \(q=u-\bar u_0\),
\[
\frac12\frac d{dt}\|q\|_2^2
=-\int\varphi(v)|\nabla q|^2
-\int u\varphi'(v)\nabla q\cdot\nabla v.
\]
Positive \(\min\varphi\), bounded \(|\varphi'|\), P4, Young and Poincare yield
\[
\|q(t)\|_2\le Ce^{-\lambda_ut}.
\]

### P6 — cell-density \(L^\infty\) decay
Status: **Proved**
Depends on: P4–P5.

Rewrite
\[
q_t-\nabla\cdot(a\nabla q)=\nabla\cdot B,
\qquad
a=\varphi(v),
\qquad
B=u\varphi'(v)\nabla v,
\]
with conormal condition
\[
(a\nabla q+B)\cdot\nu=0.
\]
The coefficient \(a\) is uniformly elliptic and bounded. P4 gives
\[
\|B(t)\|_\infty\le Ce^{-\lambda_vt}.
\]
Apply Choi 2016, Theorem 1.1, locally up to the Neumann boundary on fixed backward cylinders:
\[
\|q\|_{L^\infty(Q_{r/2})}
\le C\|q\|_{L^2(Q_r)}
+C\|B\|_{L^{p_1,q_1}(Q_r)},
\]
where \(p_1>n\), \(q_1>2\), and \(n/p_1+2/q_1<1\). P5 and exponential decay of \(B\), followed by a finite covering of \(\Omega\), give
\[
\|u(t)-\bar u_0\|_\infty\le Ce^{-\lambda_\infty t}.
\]

Reference: J. Choi, *Bull. Korean Math. Soc.* 53 (2016), 1123–1148, Theorem 1.1, DOI 10.4134/BKMS.b150567.

### P7 — monotonicity removal
Status: **Proved**
Depends on: P2–P6.

No stabilization step uses the sign of \(\varphi'\). Only positivity of \(\varphi\) and boundedness of \(|\varphi'|\) on the signal range are used.

### P8 — Qin–Zheng 2026 corollary
Status: **Proved**
Depends on: T0 + their boundedness theorem.

For \(F(v)=1-\alpha v\), \(v_*=1/\alpha\) and
\[
(v-v_*)F(v)=-\alpha(v-v_*)^2.
\]
Thus every bounded solution supplied by their theorem satisfies
\[
\|u(t)-\bar u_0\|_\infty
+\|v(t)-1/\alpha\|_{W^{1,\infty}}
\le Ce^{-\lambda t}.
\]

## Superseded routes

1. **Eventual positivity/Harnack route** — unnecessary after P2.
2. **Uniform Hölder + interpolation route for \(u\)** — valid-looking but unnecessary after P6; Choi's inhomogeneous Neumann local boundedness estimate gives a shorter direct closure.

## Remaining frontier

The proof DAG is closed. Highest priority now moves from P3/P4 proof work to **P2 novelty comparison / manuscript-level adversarial audit**. The main mathematical strengthening still worth testing is whether the uniform boundedness hypothesis on \(u\) can be weakened while preserving the full \(L^\infty\) conclusion.
