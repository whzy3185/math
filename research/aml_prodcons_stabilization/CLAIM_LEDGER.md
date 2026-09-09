# CLAIM_LEDGER — AML production–consumption stabilization

Evidence labels follow Math Research Full-Push v5.

| ID | Claim | Evidence | Notes |
|---|---|---|---|
| C1 | \(\int_\Omega u(t)=\int_\Omega u_0=:m>0\) for all \(t\) | Proved | Integrate \(u_t=\Delta(\varphi(v)u)\) and use Neumann boundary data. |
| C2 | \(0\le v(x,t)\le \max\{\|v_0\|_\infty,1/\alpha\}\) | Proved | Maximum principle applied to \(v_t=\Delta v+u(1-\alpha v)\), with \(u\ge0\). |
| C3 | Uniform weighted coercivity: if \(0\le\rho\le U\), \(\int\rho=m>0\), then \(\|f\|_2^2\le C(\|\nabla f\|_2^2+\int\rho f^2)\) | Proved | Elementary Poincaré + control of the spatial mean by the weighted term. |
| C4 | If \(\sup_t\|u(t)\|_\infty<\infty\), then \(\|v(t)-1/\alpha\|_2\le Ce^{-\lambda t}\) | Proved | Exact energy identity for \(w=v-1/\alpha\) + C3. |
| C5 | Under the same hypothesis, \(\|v(t)-1/\alpha\|_{W^{1,\infty}}\le Ce^{-\lambda t}\) | Observed | Complete Duhamel route identified; exact Neumann semigroup estimate/reference still to be pinned before promotion. |
| C6 | \(\|u(t)-\bar u_0\|_2\le Ce^{-\lambda t}\) | Observed | Follows from C5 via energy, positivity of \(\varphi\) on the bounded \(v\)-range, Young and Poincaré. |
| C7 | \(\|u(t)-\bar u_0\|_\infty\le Ce^{-\lambda t}\) | Observed | Needs a fully sourced uniform parabolic smoothing/Hölder interpolation step after C6. |
| C8 | Conditional stabilization needs no sign condition on \(\varphi'\) | Observed | Current proof uses bounded \(\varphi'\), not \(\varphi'<0\); requires closure of C5–C7. |
| C9 | Qin–Zheng 2026 bounded solution converges exponentially to \((\bar u_0,1/\alpha)\) | Observed | Intended corollary of C7/C8 plus their boundedness theorem. |
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
