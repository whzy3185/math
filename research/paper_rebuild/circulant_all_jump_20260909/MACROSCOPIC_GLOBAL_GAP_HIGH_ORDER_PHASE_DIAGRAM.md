# High-order global gap phase diagram across the balanced transition

Date: 2026-09-14

Status: **Proved** by combining the endpoint and phase-slip refinements.

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

At higher order the two sides are not symmetric because only the periodic well has an algebraic cusp.

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

## Theorem B — antiperiodic-dominant expansion

Assume

\[
\frac mN\to\gamma\in(1,\infty).
\]

Then eventual exact antiperiodic locking gives

\[
\boxed{
\begin{aligned}
\Gamma_{N,m,q}={}&\frac{\pi^2}{4m^2}
-\frac{\sqrt2\pi^2}{4m^3}\\
&+\frac{\pi^2(72-\pi^2)}{192m^4}\\
&+\frac{\sqrt2\pi^2(-64+3\pi^2)}{256m^5}\\
&+\frac{\pi^2(\pi^4-750\pi^2+7200)}{23040m^6}
+O(m^{-7}).
\end{aligned}}
\tag{1.2}
\]

No phase-slip subtraction appears.

## Theorem C — balanced expansion

For

\[
N=m=r\to\infty,
\]

the periodic cusp beats the two endpoint values by an algebraic amount, while their mutual difference is only exponential. Hence

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

Thus the balanced geometry inherits the periodic-side algebraic expansion.

---

## 2. Proof by coefficient subtraction

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

Subtracting (2.2) from (2.1) gives the coefficients in (1.1) and (1.3).

In the antiperiodic-dominant regime, `ANTIPERIODIC_EXACT_LOCKING_AND_HIGH_ORDER_GAP.md` gives `Gamma=e^-` exactly for all sufficiently large parameters, so (1.2) is just (2.1) with `ell=m`.

## 3. Structural consequence

The balanced transition is symmetric only at the first three displayed scales:

\[
\ell^{-2},\qquad \ell^{-3},\qquad \text{and the endpoint part of }\ell^{-4}.
\]

The avoided-crossing cusp lowers the periodic-side global gap by

\[
\frac{\pi^2}{32\ell^4}+O(\ell^{-5}),
\]

whereas the antiperiodic side remains locked. Thus the first genuine orientation-sensitive coefficient occurs at fourth order.

This provides an algebraic signature of the spectral phase transition that is invisible in the leading Dirichlet theory.