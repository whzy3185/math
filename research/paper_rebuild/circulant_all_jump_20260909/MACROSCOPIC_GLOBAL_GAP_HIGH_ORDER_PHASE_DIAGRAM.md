# High-order global gap phase diagram across the balanced transition

Date: 2026-09-14

Status: **Proved after hostile-audit correction**.

The displayed algebraic coefficients are unchanged. The correction is that the `m>N` optimizer is exponentially close to the compressed-antiperiodic well rather than generally exactly equal to physical `z=-1`.

## 1. Setup

Write

\[
L=2(N+m),\qquad N,m\to\infty,
\]

with the ratio bounded away from zero and infinity. Let

\[
\Gamma_{N,m,q}=8-\max_{|z|=1}\rho(H_{N,m,q}(z))^2.
\]

The leading theorem is symmetric:

\[
\max\{N,m\}^2\Gamma_{N,m,q}\to\frac{\pi^2}{4}.
\]

At higher order the two sides differ because only the periodic well has an algebraic cusp; the physical seam on the compressed-antiperiodic side produces only an exponentially small correction.

## Theorem A — periodic-dominant expansion

Assume

\[
\frac mN\to\gamma\in(0,1).
\]

Then uniformly over arbitrary odd multipliers,

\[
\boxed{
\begin{aligned}
\Gamma_{N,m,q}={}&\frac{\pi^2}{4N^2}
-\frac{\sqrt2\pi^2}{4N^3}\\
&+\frac{\pi^2(66-\pi^2)}{192N^4}\\
&+\frac{\sqrt2\pi^2(-52+3\pi^2)}{256N^5}\\
&+\frac{\pi^2(\pi^4-750\pi^2-960\sqrt2+7290)}{23040N^6}
+O(N^{-7}).
\end{aligned}}
\tag{1.1}
\]

The difference from the periodic endpoint first appears at order `N^-4`.

## Theorem B — compressed-antiperiodic-dominant expansion

Assume

\[
\frac mN\to\gamma\in(1,\infty).
\]

Then the global maximizing phase lies exponentially close to `d=-2`, and

\[
\boxed{
\begin{aligned}
\Gamma_{N,m,q}={}&\frac{\pi^2}{4m^2}
-\frac{\sqrt2\pi^2}{4m^3}\\
&+\frac{\pi^2(72-\pi^2)}{192m^4}\\
&+\frac{\sqrt2\pi^2(-64+3\pi^2)}{256m^5}\\
&+\frac{\pi^2(\pi^4-750\pi^2+7200)}{23040m^6}
+O(m^{-7})+O(\Lambda^{-2N}).
\end{aligned}}
\tag{1.2}
\]

There is no algebraic phase-slip subtraction on this side.

## Theorem C — balanced expansion

For

\[
N=m=r\to\infty,
\]

the endpoint gaps agree to every algebraic order, but the periodic cusp lowers the full global gap by an algebraic amount. Hence

\[
\boxed{
\begin{aligned}
\Gamma_r={}&\frac{\pi^2}{4r^2}
-\frac{\sqrt2\pi^2}{4r^3}\\
&+\frac{\pi^2(66-\pi^2)}{192r^4}\\
&+\frac{\sqrt2\pi^2(-52+3\pi^2)}{256r^5}\\
&+\frac{\pi^2(\pi^4-750\pi^2-960\sqrt2+7290)}{23040r^6}
+O(r^{-7}).
\end{aligned}}
\tag{1.3}
\]

---

## 2. Coefficient derivation

From `MACROSCOPIC_ENDPOINT_HIGH_ORDER_EXPANSION.md`, with soft length `ell`,

\[
\begin{aligned}
e_\ell={}&\frac{\pi^2}{4\ell^2}
-\frac{\sqrt2\pi^2}{4\ell^3}
+\frac{\pi^2(72-\pi^2)}{192\ell^4}\\
&+\frac{\sqrt2\pi^2(-64+3\pi^2)}{256\ell^5}\\
&+\frac{\pi^2(\pi^4-750\pi^2+7200)}{23040\ell^6}
+O(\ell^{-7}).
\end{aligned}
\tag{2.1}
\]

In the periodic well, `HIGH_ORDER_MACROSCOPIC_PHASE_SLIP.md` gives

\[
\begin{aligned}
e_\ell-\Gamma
={}&\frac{\pi^2}{32\ell^4}
-\frac{3\pi^2}{32\sqrt2\ell^5}\\
&+\frac{\pi^2(32\sqrt2-3)}{768\ell^6}
+O(\ell^{-7}).
\end{aligned}
\tag{2.2}
\]

Subtracting (2.2) from (2.1) gives (1.1) and (1.3).

On the `m>N` side, `ANTIPERIODIC_EXACT_LOCKING_AND_HIGH_ORDER_GAP.md` in its corrected form proves that the physical-seam correction is `O(Lambda^-2N)`, beyond every displayed algebraic order. Therefore the universal endpoint coefficients with `ell=m` give (1.2).

## 3. Structural consequence

The balanced transition is symmetric only in its endpoint Robin series. The full Bloch problem is orientation-sensitive because

- the periodic side has an algebraic avoided-crossing cusp;
- the compressed-antiperiodic side is analytic at algebraic scale and has only an exponentially small physical-seam displacement.

Thus the first algebraic orientation-sensitive coefficient occurs at order `ell^-4`, while the exact finite phase on the antiperiodic side carries an additional beyond-all-orders correction.