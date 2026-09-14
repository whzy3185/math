# High-order phase-slip expansion at the periodic soft well

Date: 2026-09-14

Status: **Proved after hostile audit**. This refines `BALANCED_TWO_DEFECT_PHASE_SLIP.md` and `MACROSCOPIC_PERIODIC_WELL_PHASE_SLIP.md`.

Important scope correction: the cusp law below is a property of the **periodic soft well** `d=2`. It does **not** hold at the antiperiodic well `d=-2`, which is analytic and is treated separately in `ANTIPERIODIC_EXACT_LOCKING_AND_HIGH_ORDER_GAP.md`.

## 1. Setup

Write

\[
L=2(N+m),\qquad N,m\to\infty,
\qquad 0<c_0\le m/N\le1.
\]

The strict inequality `m/N<1` gives the periodic-dominant regime; the endpoint `m=N` is the balanced regime.

Let

\[
e^+_{N,m}:=8-\rho(H(1))^2
\]

and let `delta` be the compressed displacement from the periodic endpoint. Put

\[
\Lambda=3+2\sqrt2.
\]

The opposite defect arc is hyperbolic and its finite-length error is exponentially small.

## Theorem A — refined periodic-well effective law

Write

\[
\delta=\frac\zeta{N^2},\qquad \zeta=O(1).
\]

For the improving top soft branch,

\[
\boxed{
N^4\bigl(g(\zeta/N^2)-e^+_{N,m}\bigr)
=Q_N\zeta^2-A_N|\zeta|+O(N^{-3})
}
\tag{1.1}
\]

locally uniformly for bounded `zeta`, where

\[
\boxed{
Q_N
=1-\frac1{\sqrt2 N}+\frac5{8N^2}+O(N^{-3}),
}
\tag{1.2}
\]

and

\[
\boxed{
A_N
=\frac\pi{2\sqrt2}-\frac\pi{2N}+\frac\pi{3N^2}+O(N^{-3}).
}
\tag{1.3}
\]

The coefficients are uniform for `m/N` in compact subsets of `(0,1]` and are independent of the odd multiplier.

## Theorem B — optimizing compressed phase

In the periodic-dominant regime, or locally at the periodic well in the balanced case,

\[
\boxed{
\begin{aligned}
N^2|\delta_N|
={}&\frac\pi{4\sqrt2}
-\frac\pi{8N}\\
&+\frac{\pi(32-27\sqrt2)}{192N^2}
+O(N^{-3}).
\end{aligned}}
\tag{1.4}
\]

Equivalently,

\[
\boxed{
|\delta_N|
=\frac\pi{4\sqrt2 N^2}
-\frac\pi{8N^3}
+\frac{\pi(32-27\sqrt2)}{192N^4}
+O(N^{-5}).
}
\tag{1.5}
\]

## Theorem C — periodic-well gain through order `N^-6`

\[
\boxed{
\begin{aligned}
e^+_{N,m}-\Gamma
={}&\frac{\pi^2}{32N^4}
-\frac{3\pi^2}{32\sqrt2 N^5}\\
&+\frac{\pi^2(32\sqrt2-3)}{768N^6}
+O(N^{-7}).
\end{aligned}}
\tag{1.6}
\]

For `m/N<1`, this is the global phase-slip gain. For `m=N=r`, it is the gain in either of the two algebraically identical balanced wells.

---

## 2. Endpoint coordinate

From `MACROSCOPIC_ENDPOINT_HIGH_ORDER_EXPANSION.md`,

\[
\boxed{
 x_N^0
=\frac\pi2
-\frac\pi{2\sqrt2 N}
+\frac\pi{4N^2}
+O(N^{-3}).
}
\tag{2.1}
\]

The finite hard-wall correction is exponentially small.

---

## 3. Refined local transfer expansion

Put

\[
\mu=2-2\cos\delta.
\]

At the boundary-layer scale,

\[
\mu=\frac{\zeta^2}{N^4}+O(N^{-8}).
\]

Expanding the exact `4 x 4` block-transfer determinant about the periodic endpoint, after dividing by the dominant hard transfer factor, gives

\[
N^2(x-x_N^0)
=-c_N|\zeta|+d_N\frac{\zeta^2}{N^2}+O(N^{-3}),
\tag{3.1}
\]

with

\[
\boxed{
\begin{aligned}
c_N={}&\frac1{2\sqrt2}-\frac1{4N}\\
&+\left(
\frac13-\frac{\sqrt2}{4}
+\frac{\sqrt2\pi^2}{96}
\right)\frac1{N^2}
+O(N^{-3}).
\end{aligned}}
\tag{3.2}
\]

The quadratic response in (3.1), together with the curvature of the soft dispersion, yields

\[
Q_N=1-\frac1{\sqrt2 N}+\frac5{8N^2}+O(N^{-3}).
\tag{3.3}
\]

The linear coefficient is

\[
2N\sin(x_N^0/N)c_N,
\]

and substitution of (2.1), (3.2) gives

\[
\boxed{
2N\sin(x_N^0/N)c_N
=\frac\pi{2\sqrt2}-\frac\pi{2N}+\frac\pi{3N^2}+O(N^{-3}).
}
\tag{3.4}
\]

Equations (3.3)--(3.4) prove the refined effective law.

---

## 4. Minimization

For `zeta>=0`, minimize

\[
V_N(\zeta)=Q_N\zeta^2-A_N\zeta.
\]

The minimizer is `A_N/(2Q_N)`, which expands to

\[
\frac\pi{4\sqrt2}
-\frac\pi{8N}
+\frac{\pi(32-27\sqrt2)}{192N^2}
+O(N^{-3}).
\]

The minimum is `-A_N^2/(4Q_N)`, giving

\[
\frac{A_N^2}{4Q_N}
=\frac{\pi^2}{32}
-\frac{3\pi^2}{32\sqrt2 N}
+\frac{\pi^2(32\sqrt2-3)}{768N^2}
+O(N^{-3}).
\]

This proves (1.4)--(1.6).

## 5. Balanced specialization

For `N=m=r`, the two endpoint gaps agree to every algebraic order and differ only by exponentially small tunneling. Hence the global balanced optimizer satisfies

\[
\boxed{
|\delta_r|
=\frac\pi{4\sqrt2 r^2}
-\frac\pi{8r^3}
+\frac{\pi(32-27\sqrt2)}{192r^4}
+O(r^{-5}),
}
\tag{5.1}
\]

and

\[
\boxed{
e_r-\Gamma_r
=\frac\pi^2}{32r^4}
-\frac{3\pi^2}{32\sqrt2 r^5}
+\frac{\pi^2(32\sqrt2-3)}{768r^6}
+O(r^{-7}).
}
\tag{5.2}
\]

These are the requested `r^-5/r^-6` balanced phase-slip coefficients.

## 6. Why the antiperiodic side is different

At `d=-2` the top soft root is nondegenerate in the physical Bloch phase. The local characteristic function is analytic and even in the displacement from `z=-1`; there is no `sqrt(mu)` splitting term and hence no `|delta|` cusp. Consequently the antiperiodic-dominant regime exhibits exact endpoint locking rather than phase slip.