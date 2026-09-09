# CLAIM_LEDGER — AML production–consumption stabilization

Evidence labels follow Math Research Full-Push v5.

| ID | Claim | Evidence | Notes |
|---|---|---|---|
| C1 | \(\int_\Omega u(t)=\int_\Omega u_0=:m>0\) for all \(t\) | Proved | Integrate the first equation and use no-flux boundary data. |
| C2 | For the Qin–Zheng kinetics, \(0\le v(x,t)\le \max\{\|v_0\|_\infty,1/\alpha\}\) | Proved | Maximum principle. |
| C3 | Uniform mass-weighted coercivity: if \(\rho\ge0\), \(\int\rho=m>0\), \(\|\rho\|_2\le K\), then \(\|f\|_2^2\le C(\|\nabla f\|_2^2+\int\rho f^2)\) | Proved | Elementary Poincare + control of the spatial mean. |
| C4 | Uniform \(L^2\)-boundedness of \(u\) plus dissipative signal kinetics imply \(\|v(t)-v_*\|_2\le Ce^{-\lambda t}\) | Proved | Energy + C3. |
| C5 | Uniform boundedness of \(u\) implies \(\|v(t)-v_*\|_{W^{1,\infty}}\le Ce^{-\lambda t}\) | Proved | Interpolation + Duhamel + Neumann heat-semigroup gradient estimate. |
| C6 | Uniform boundedness implies \(\|u(t)-\bar u_0\|_2\le Ce^{-\lambda t}\) | Proved | Energy estimate, positivity of \(\varphi\), C5, Young and Poincare. |
| C7 | Uniform boundedness implies \(\|u(t)-\bar u_0\|_\infty\le Ce^{-\lambda t}\) | Proved | Rewrite as a uniformly parabolic divergence-form equation with exponentially decaying flux forcing and apply Choi 2016, Thm. 1.1, on backward Neumann cylinders. |
| C8 | Therefore \(\|u(t)-\bar u_0\|_\infty+\|v(t)-v_*\|_{W^{1,\infty}}\le Ce^{-\lambda t}\) | Proved | C5 + C7. |
| C9 | Conditional uniform stabilization requires no sign condition on \(\varphi'\) | Proved | Only \(\min_I\varphi>0\) and bounded \(|\varphi'|\) on the signal range enter C3–C8. |
| C10 | Qin–Zheng 2026 bounded solutions converge exponentially to \((\bar u_0,1/\alpha)\) in \(L^\infty\times W^{1,\infty}\) | Proved | Their theorem supplies boundedness; the present principle supplies stabilization. |
| C11 | General principle for \(u_t=\Delta(\varphi(v)u),\ v_t=\Delta v+uF(v)\) under \(F(v_*)=0\) and \((s-v_*)F(s)\le-\beta(s-v_*)^2\) | Proved | See `GENERAL_DISSIPATIVE_KINETICS.md`. |
| C12 | No same-model published exponential-stabilization result for the exact Qin–Zheng 2026 system was located in the 2026-09-09 deep audit | Observed | Not an open-status certificate. |
| C13 | The abstract dissipativity-to-uniform-stabilization theorem is new | Observed | No exact collision located; pure-consumption and indirect-signal predecessors remain material novelty risks. |

## Uniform-upgrade proof record

Set \(q=u-\bar u_0\). Then
\[
q_t-\nabla\cdot(a\nabla q)=\nabla\cdot B,
\qquad
a=\varphi(v),
\qquad
B=u\varphi'(v)\nabla v,
\]
with
\[
(a\nabla q+B)\cdot\nu=0.
\]
On the compact signal range,
\[
0<a_*\le a\le a^*<\infty.
\]
By C5,
\[
\|B(t)\|_\infty\le Ce^{-\lambda_v t}.
\]
By C6,
\[
\|q(t)\|_2\le Ce^{-\lambda_u t}.
\]

Use J. Choi, *Bull. Korean Math. Soc.* 53 (2016), Theorem 1.1, for the Neumann problem
\[
Pq=\operatorname{div}B,
\qquad
(a\nabla q+B)\cdot\nu=0.
\]
Choose finite \(p_1>n\), \(q_1>2\) with \(n/p_1+2/q_1<1\). On each fixed backward cylinder of radius \(r_0\), Choi's estimate gives
\[
\|q\|_{L^\infty(Q_{r_0/2})}
\le C\|q\|_{L^2(Q_{r_0})}
+C\|B\|_{L^{p_1,q_1}(Q_{r_0})}.
\]
Both right-hand terms decay exponentially in the terminal time. A finite covering of the bounded smooth domain yields
\[
\|q(t)\|_\infty\le Ce^{-\lambda_\infty t}.
\]

Reference: J. Choi, *Note on local estimates for weak solution of boundary value problem for second order parabolic equation*, Bull. Korean Math. Soc. 53 (2016), 1123–1148, DOI 10.4134/BKMS.b150567.

## Evidence warning

The uniform theorem is now mathematically **Proved** in the campaign sense, but novelty remains **Observed** until the final prior-art audit. Do not use “first”, “new”, “open”, or “sharp” without explicit literature evidence.
