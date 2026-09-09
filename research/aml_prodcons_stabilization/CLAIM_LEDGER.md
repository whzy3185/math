# CLAIM_LEDGER — AML production–consumption stabilization

Evidence labels follow Math Research Full-Push v5.

| ID | Claim | Evidence | Notes |
|---|---|---|---|
| C1 | \(\int_\Omega u(t)=\int_\Omega u_0=:m>0\) for all \(t\) | Proved | Integrate \(u_t=\Delta(\varphi(v)u)\) and use Neumann boundary data. |
| C2 | For the Qin–Zheng kinetics, \(0\le v(x,t)\le \max\{\|v_0\|_\infty,1/\alpha\}\) | Proved | Maximum principle applied to \(v_t=\Delta v+u(1-\alpha v)\), with \(u\ge0\). |
| C3 | Uniform mass-weighted coercivity: if \(\rho\ge0\), \(\int\rho=m>0\), \(\|\rho\|_2\le K\), then \(\|f\|_2^2\le C(\|\nabla f\|_2^2+\int\rho f^2)\) | Proved | Elementary Poincaré + control of the spatial mean by the weighted term. Do not advertise the inequality itself as novel without separate evidence. |
| C4 | For \(F(v)=1-\alpha v\), a uniform \(L^2\)-bound on \(u\) implies \(\|v(t)-1/\alpha\|_2\le Ce^{-\lambda t}\) | Proved | Exact energy identity + C3. |
| C5 | If \(u\) is uniformly bounded, then \(\|v(t)-1/\alpha\|_{W^{1,\infty}}\le Ce^{-\lambda t}\) | Proved | Interpolation + Duhamel + standard Neumann heat-semigroup gradient estimate. |
| C6 | Under the same boundedness hypothesis, \(\|u(t)-\bar u_0\|_2\le Ce^{-\lambda t}\) | Proved | Energy estimate, positivity of \(\varphi\), C5, Young and Poincaré. |
| C7 | Under the same hypothesis, \(\|u(t)-\bar u_0\|_{L^p}\le C_pe^{-\lambda_p t}\) for all finite \(p\ge1\) | Proved | Uniform \(L^\infty\)-boundedness plus C6 and interpolation. |
| C8 | Finite-\(p\) conditional stabilization requires no sign condition on \(\varphi'\) | Proved | C3–C7 use only \(\min_I\varphi>0\) and bounded \(|\varphi'|\) on the signal range. |
| C9 | Qin–Zheng 2026 bounded solutions converge exponentially to \((\bar u_0,1/\alpha)\) in \(L^p\times W^{1,\infty}\) for every finite \(p\) | Proved | Their theorem supplies the bounded classical solution; C4–C8 supply stabilization. |
| C10 | General principle for \(u_t=\Delta(\varphi(v)u),\ v_t=\Delta v+uF(v)\) under \(F(v_*)=0\) and \((s-v_*)F(s)\le-\beta(s-v_*)^2\) | Proved | See `GENERAL_DISSIPATIVE_KINETICS.md`. Root condition is explicit after P0 audit. |
| C11 | No same-model published exponential-stabilization result for the exact Qin–Zheng 2026 system was located in the 2026-09-09 deep audit | Observed | Searches included exact equations/title, stabilization/large-time/global-dynamics variants, author follow-ups, and nearby 2025–2026 literature. This is not an open-status certificate. |
| C12 | The abstract dissipativity-to-stabilization theorem is new | Observed | No theorem with the same abstract hypothesis/conclusion was located, but pure-consumption and indirect-signal predecessors make novelty risk nontrivial. Do not certify novelty yet. |
| C13 | \(\|u(t)-\bar u_0\|_\infty\le Ce^{-\lambda t}\) | Observed | Likely follows from uniform parabolic Hölder regularity plus C6 and Hölder/L2 interpolation; not yet promoted until the regularity step is fully sourced/proved. |

## Explicit coercivity constant under \(0\le \rho\le U\)

Let \(C_P\) satisfy \(\|f-f_\Omega\|_2\le C_P\|\nabla f\|_2\). From
\[
m|f_\Omega|\le \sqrt m\left(\int\rho f^2\right)^{1/2}+\sqrt{Um}\,C_P\|\nabla f\|_2,
\]
one obtains
\[
\|f\|_2^2
\le
\left(2C_P^2+\frac{4|\Omega|UC_P^2}{m}\right)\|\nabla f\|_2^2
+\frac{4|\Omega|}{m}\int\rho f^2.
\]
Thus a valid time-uniform coercivity constant depends only on \(\Omega,m,U\).

## C5 closure

Set \(w=v-1/\alpha\). From C4 and the uniform \(L^\infty\)-bound for \(w\), for every \(p\ge2\),
\[
\|w(t)\|_p\le \|w(t)\|_\infty^{1-2/p}\|w(t)\|_2^{2/p}
\le C e^{-\mu_p t}.
\]
Fix \(p>n\). For \(t\ge1\), Duhamel on \([t-1/2,t]\) gives
\[
w(t)=e^{\frac12\Delta}w(t-1/2)-\alpha\int_{t-1/2}^t e^{(t-s)\Delta}(u(s)w(s))\,ds.
\]
The standard Neumann semigroup estimate
\[
\|\nabla e^{\tau\Delta}f\|_\infty
\le C\left(1+\tau^{-\frac12-\frac n{2p}}\right)e^{-\lambda_1\tau}\|f\|_p
\]
has an integrable singularity because \(p>n\). Hence \(\|\nabla w(t)\|_\infty\le Ce^{-\mu t}\). The spatial mean of \(w\) is bounded by \(|\Omega|^{-1/2}\|w\|_2\), and the \(W^{1,\infty}\)-Poincaré inequality then yields \(\|w\|_\infty\le Ce^{-\mu t}\).

## C6–C8 closure

Let \(q=u-\bar u_0\), so \(\int_\Omega q=0\). On the bounded signal range define
\[
\varphi_*:=\min\varphi>0,
\qquad L_\varphi:=\max|\varphi'|<\infty.
\]
Then
\[
\frac12\frac d{dt}\|q\|_2^2
=-\int\varphi(v)|\nabla q|^2
-\int u\varphi'(v)\nabla q\cdot\nabla v.
\]
Young and C5 give
\[
\frac d{dt}\|q\|_2^2+c\|q\|_2^2\le Ce^{-2\mu t},
\]
so C6 follows. Since \(q\) is uniformly bounded in \(L^\infty\), interpolation gives C7 for every finite \(p\). No sign of \(\varphi'\) enters this argument, proving C8.
