# CLAIM_LEDGER — AML production–consumption stabilization

Evidence labels follow Math Research Full-Push v5.

| ID | Claim | Evidence | Notes |
|---|---|---|---|
| C1 | \(\int_\Omega u(t)=\int_\Omega u_0=:m>0\) for all \(t\) | Proved | Integrate \(u_t=\Delta(\varphi(v)u)\) and use Neumann boundary data. |
| C2 | \(0\le v(x,t)\le \max\{\|v_0\|_\infty,1/\alpha\}\) | Proved | Maximum principle applied to \(v_t=\Delta v+u(1-\alpha v)\), with \(u\ge0\). |
| C3 | Uniform weighted coercivity: if \(0\le\rho\le U\), \(\int\rho=m>0\), then \(\|f\|_2^2\le C(\|\nabla f\|_2^2+\int\rho f^2)\) | Proved | Elementary Poincaré + control of the spatial mean by the weighted term. |
| C4 | If \(\sup_t\|u(t)\|_\infty<\infty\), then \(\|v(t)-1/\alpha\|_2\le Ce^{-\lambda t}\) | Proved | Exact energy identity for \(w=v-1/\alpha\) + C3. |
| C5 | Under the same hypothesis, \(\|v(t)-1/\alpha\|_{W^{1,\infty}}\le Ce^{-\lambda t}\) | Proved | Interpolate C4 to \(L^p\), choose \(p>n\), then use Duhamel and the standard Neumann heat-semigroup gradient estimate. |
| C6 | \(\|u(t)-\bar u_0\|_2\le Ce^{-\lambda t}\) | Proved | Energy estimate for \(q=u-\bar u_0\), positivity of \(\varphi\) on the bounded \(v\)-range, C5, Young and Poincaré. |
| C7 | \(\|u(t)-\bar u_0\|_\infty\le Ce^{-\lambda t}\) | Observed | Needs a fully pinned uniform parabolic smoothing/Hölder interpolation step after C6. |
| C8 | Conditional stabilization needs no sign condition on \(\varphi'\) | Observed | C1–C6 use bounded \(\varphi'\), not \(\varphi'<0\); full promotion waits for C7. |
| C9 | Qin–Zheng 2026 bounded solution converges exponentially to \((\bar u_0,1/\alpha)\) in at least \(L^2\times W^{1,\infty}\) | Proved | Combine their boundedness theorem with C4–C6. The stronger \(L^\infty\) convergence rate for \(u\) remains tied to C7. |
| C10 | The conditional stabilization theorem is new for the exact production–consumption signal-dependent-motility model | Observed | Search dated 2026-09-09 is promising but not sufficient for novelty certification. |

## Explicit coercivity constant

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

A convenient published source for the semigroup estimate is Lemma 1.1(ii) in the Springer chapter *Chemotaxis–Fluid System* (2022), which cites Winkler (2010), Lemma 1.3, and Cao (2015), Lemma 2.1.

## C6 closure

Let \(q=u-\bar u_0\), so \(\int_\Omega q=0\). Since \(v\in[0,M]\), define
\[
\varphi_*:=\min_{[0,M]}\varphi>0,
\qquad L_\varphi:=\max_{[0,M]}|\varphi'|<\infty.
\]
Then
\[
\frac12\frac d{dt}\|q\|_2^2
=-\int\varphi(v)|\nabla q|^2
-\int u\varphi'(v)\nabla q\cdot\nabla v
\]
and Young's inequality gives
\[
\frac12\frac d{dt}\|q\|_2^2
\le -\frac{\varphi_*}{2}\|\nabla q\|_2^2
+\frac{U^2L_\varphi^2}{2\varphi_*}\|\nabla v\|_2^2.
\]
Using C5 and Poincaré,
\[
\frac d{dt}\|q\|_2^2+c\|q\|_2^2\le Ce^{-2\mu t},
\]
which yields exponential \(L^2\)-decay by Gronwall/ODE comparison.
