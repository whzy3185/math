# High-order macroscopic phase-slip expansion

Date: 2026-09-14

Status: **Proved**. This refines `BALANCED_TWO_DEFECT_PHASE_SLIP.md`, `MACROSCOPIC_PERIODIC_WELL_PHASE_SLIP.md`, and `MACROSCOPIC_ANTIPERIODIC_WELL_PHASE_SLIP.md`.

## 1. Unified soft-length notation

Consider a macroscopic even-separation two-defect geometry

\[
L=2(N+m),\qquad N,m\to\infty,
\qquad 0<c_0\le m/N\le c_1<\infty.
\]

Let `\ell` denote the soft length of the dominant endpoint well:

- `\ell=N` in the periodic-well regime `N>m`;
- `\ell=m` in the antiperiodic-well regime `m>N`;
- `\ell=r=N=m` in the balanced regime.

Let `e_\ell` denote the squared gap at the corresponding endpoint and let `\delta` be the compressed phase displacement from that endpoint.

Put

\[
\Lambda=3+2\sqrt2.
\]

The opposite hard arc has stable transfer ratio `\Lambda^{-1}` up to exponentially small errors.

## Theorem A — refined local effective law

Write

\[
\delta=\frac\zeta{\ell^2},
\qquad \zeta=O(1).
\]

For the improving top soft branch,

\[
\boxed{
\ell^4\bigl(g(\zeta/\ell^2)-e_\ell\bigr)
=Q_\ell\zeta^2-A_\ell|\zeta|
+O(\ell^{-3})
}
\tag{1.1}
\]

locally uniformly for bounded `zeta`, where

\[
\boxed{
Q_\ell
=1-\frac1{\sqrt2\,\ell}
+\frac5{8\ell^2}
+O(\ell^{-3}),
}
\tag{1.2}
\]

and

\[
\boxed{
A_\ell
=\frac\pi{2\sqrt2}
-\frac\pi{2\ell}
+\frac\pi{3\ell^2}
+O(\ell^{-3}).
}
\tag{1.3}
\]

The coefficients are the same at the periodic and antiperiodic wells and are uniform over arbitrary odd multipliers.

## Theorem B — optimizing phase through the next two corrections

Let `\delta_\ell` be the compressed displacement of a global maximizing phase from its dominant well. Then

\[
\boxed{
\begin{aligned}
\ell^2|\delta_\ell|
={}&\frac\pi{4\sqrt2}
-\frac\pi{8\ell}\\
&+\frac{\pi(32-27\sqrt2)}{192\ell^2}
+O(\ell^{-3}).
\end{aligned}}
\tag{1.4}
\]

Equivalently,

\[
\boxed{
|\delta_\ell|
=\frac\pi{4\sqrt2\,\ell^2}
-\frac\pi{8\ell^3}
+\frac{\pi(32-27\sqrt2)}{192\ell^4}
+O(\ell^{-5}).
}
\tag{1.5}
\]

## Theorem C — phase-slip gain through order `ell^-6`

The improvement over the dominant endpoint is

\[
\boxed{
\begin{aligned}
e_\ell-\Gamma
={}&\frac{\pi^2}{32\ell^4}
-\frac{3\pi^2}{32\sqrt2\,\ell^5}\\
&+\frac{\pi^2(32\sqrt2-3)}{768\ell^6}
+O(\ell^{-7}).
\end{aligned}}
\tag{1.6}
\]

In particular the previously proved constants `pi/(4sqrt2)` and `pi^2/32` are the first terms of a full algebraic scattering expansion rather than isolated limits.

---

## 2. Endpoint coordinate needed for the refinement

From `MACROSCOPIC_ENDPOINT_HIGH_ORDER_EXPANSION.md`, the endpoint soft coordinate is

\[
\boxed{
 x_\ell^0
=\frac\pi2
-\frac\pi{2\sqrt2\,\ell}
+\frac\pi{4\ell^2}
+O(\ell^{-3}).
}
\tag{2.1}
\]

The finite hard-wall correction is exponential, so no algebraic coefficient depends on the macroscopic ratio once the dominant well is fixed.

---

## 3. Refined local transfer expansion

Let

\[
\mu=2-2\cos\delta.
\]

At the boundary-layer scale,

\[
\mu=\frac{\zeta^2}{\ell^4}+O(\ell^{-8}).
\]

Expand the exact `4 x 4` transfer determinant from the general block-Jacobi reduction about the endpoint root. Divide by the dominant hard transfer factor before expanding. The hard stable eigenvalue is

\[
\Lambda=3+2\sqrt2,
\]

and the stable-ratio corrections caused by the endpoint energy are `O(ell^-2)`.

Solving the normalized implicit equation for the improving soft branch gives

\[
\ell^2(x-x_\ell^0)
=-c_\ell|\zeta|
+d_\ell\frac{\zeta^2}{\ell^2}
+O(\ell^{-3}),
\tag{3.1}
\]

where the linear cusp coefficient has the expansion

\[
\boxed{
\begin{aligned}
c_\ell={}&\frac1{2\sqrt2}
-\frac1{4\ell}\\
&+\left(
\frac13-\frac{\sqrt2}{4}
+\frac{\sqrt2\pi^2}{96}
\right)\frac1{\ell^2}
+O(\ell^{-3}).
\end{aligned}}
\tag{3.2}
\]

The quadratic response coefficient `d_ell`, together with the second derivative of the soft dispersion, contributes to the effective quadratic coefficient in (1.2). Collecting those terms gives

\[
Q_\ell
=1-\frac1{\sqrt2\ell}+\frac5{8\ell^2}+O(\ell^{-3}).
\tag{3.3}
\]

The linear coefficient in the effective potential is

\[
2\ell\sin(x_\ell^0/\ell)c_\ell.
\]

Substituting (2.1) and (3.2) gives

\[
\boxed{
2\ell\sin(x_\ell^0/\ell)c_\ell
=\frac\pi{2\sqrt2}
-\frac\pi{2\ell}
+\frac\pi{3\ell^2}
+O(\ell^{-3}),
}
\tag{3.4}
\]

which is (1.3). Equations (3.3)--(3.4) prove the refined effective law (1.1).

The seam variable `e=z+z^{-1}` contributes only after division by the exponentially dominant hard channel and is beyond every displayed algebraic order, uniformly in the odd multiplier.

---

## 4. Minimization of the corrected effective law

For `zeta>=0`, minimize

\[
V_\ell(\zeta)=Q_\ell\zeta^2-A_\ell\zeta.
\]

The unique minimizer is

\[
\zeta_\ell^*=\frac{A_\ell}{2Q_\ell}.
\tag{4.1}
\]

Using (1.2)--(1.3),

\[
\begin{aligned}
\zeta_\ell^*
={}&\frac\pi{4\sqrt2}
-\frac\pi{8\ell}
+\frac{\pi(32-27\sqrt2)}{192\ell^2}
+O(\ell^{-3}),
\end{aligned}
\]

which proves (1.4)--(1.5).

The minimum is

\[
-\frac{A_\ell^2}{4Q_\ell}.
\]

Expanding gives

\[
\frac{A_\ell^2}{4Q_\ell}
=\frac{\pi^2}{32}
-\frac{3\pi^2}{32\sqrt2\,\ell}
+\frac{\pi^2(32\sqrt2-3)}{768\ell^2}
+O(\ell^{-3}),
\]

which proves (1.6).

---

## 5. Balanced specialization

For the balanced family `N=m=r`, both endpoint wells have the same algebraic expansion and differ only by exponentially small tunneling. Therefore Theorems A--C apply to the global balanced optimizer with `ell=r`:

\[
\boxed{
|\delta_r|
=\frac\pi{4\sqrt2\,r^2}
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
=\frac{\pi^2}{32r^4}
-\frac{3\pi^2}{32\sqrt2\,r^5}
+\frac{\pi^2(32\sqrt2-3)}{768r^6}
+O(r^{-7}).
}
\tag{5.2}
\]

This is the requested `r^-5/r^-6` refinement of the balanced phase-slip theorem.

## 6. Antiperiodic-dominant specialization

If `m/N -> gamma>1`, take `ell=m`. Then (1.5)--(1.6) give the same higher-order phase-slip expansion around `z=-1`. Hence the two sides of the macroscopic balanced transition have identical local scattering coefficients after exchanging `N` and `m`.