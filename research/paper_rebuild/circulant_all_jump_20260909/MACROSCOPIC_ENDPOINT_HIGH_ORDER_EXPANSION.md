# High-order endpoint expansions in the macroscopic two-defect regime

Date: 2026-09-14

Status: **Proved**. This refines `MACROSCOPIC_ENDPOINT_CUBIC_CORRECTION.md` and applies simultaneously to the periodic and antiperiodic soft channels.

## 1. Setup

Write

\[
L=2(N+m),\qquad h=2m,
\]

and assume

\[
N,m\to\infty,
\qquad
0<c_0\le \frac mN\le c_1<\infty.
\tag{1.1}
\]

Let

\[
e^+_{N,m}:=8-\rho(H(1))^2,
\qquad
e^-_{N,m}:=8-\rho(H(-1))^2.
\]

At the periodic endpoint the soft length is `N`; at the antiperiodic endpoint the soft length is `m`.

Put

\[
\Lambda=3+2\sqrt2.
\]

Because the opposite arc is hyperbolic and has length comparable to the soft length, replacing its finite transfer ratio by the stable ratio produces an error `O(\Lambda^{-c\ell})`, where `\ell` denotes the soft length and `c>0` depends only on the compact ratio window in (1.1).

## Theorem A — universal soft-coordinate expansion

Let `\ell=N` at `z=1` and `\ell=m` at `z=-1`. Write the top endpoint root as

\[
8-e_\ell=6+2\cos\theta_\ell,
\qquad
x_\ell=\ell\theta_\ell.
\]

Then

\[
\boxed{
\begin{aligned}
x_\ell={}&\frac\pi2
-\frac{\pi}{2\sqrt2\,\ell}
+\frac{\pi}{4\ell^2}\\
&+\frac{\sqrt2\,\pi(\pi^2-96)}{768\ell^3}
+\frac{\pi(24-\pi^2)}{192\ell^4}
+O(\ell^{-5}).
\end{aligned}}
\tag{1.2}
\]

The expansion is the same at both endpoints.

## Theorem B — endpoint gap through sixth order

Uniformly under (1.1),

\[
\boxed{
\begin{aligned}
e_\ell={}&\frac{\pi^2}{4\ell^2}
-\frac{\sqrt2\,\pi^2}{4\ell^3}
+\frac{\pi^2(72-\pi^2)}{192\ell^4}\\
&+\frac{\sqrt2\,\pi^2(-64+3\pi^2)}{256\ell^5}\\
&+\frac{\pi^2(\pi^4-750\pi^2+7200)}{23040\ell^6}
+O(\ell^{-7}).
\end{aligned}}
\tag{1.3}
\]

Thus (1.3) with `\ell=N` gives `e^+_{N,m}` and with `\ell=m` gives `e^-_{N,m}`.

---

## 2. Stable-wall Robin equation

At the periodic endpoint the exact quantization equation is

\[
\frac{\cos((N-\tfrac12)\theta)}{\cos(\theta/2)}
-R_m(2+\cos\theta)\tan(\theta/2)\sin(N\theta)
=\frac1{T_m(2+\cos\theta)},
\tag{2.1}
\]

where

\[
R_m(a)=\frac{U_m(a)+U_{m-1}(a)}{T_m(a)}.
\]

Under (1.1), the right side is exponentially small and

\[
R_m(a)=R_\infty(a)+O(\Lambda^{-cm}),
\]

with

\[
\boxed{
R_\infty(a)=1+\sqrt{\frac{a+1}{a-1}}.
}
\tag{2.2}
\]

Using

\[
\frac{\cos((\ell-\tfrac12)\theta)}{\cos(\theta/2)}
=\cos x+\tan(\theta/2)\sin x,
\qquad x=\ell\theta,
\]

and `a=2+cos theta`, the algebraic-order endpoint equation becomes

\[
\boxed{
\cot x
=\sqrt{\frac{3+\cos\theta}{1+\cos\theta}}
\tan\frac\theta2,
\qquad \theta=\frac x\ell.
}
\tag{2.3}
\]

The antiperiodic soft channel gives the identical equation after exchanging the two arcs.

---

## 3. Solving the Robin equation

Seek

\[
x=\frac\pi2+
\frac{a_1}{\ell}+\frac{a_2}{\ell^2}
+\frac{a_3}{\ell^3}+\frac{a_4}{\ell^4}
+O(\ell^{-5}).
\tag{3.1}
\]

Taylor expansion of (2.3) gives successively

\[
a_1=-\frac{\pi}{2\sqrt2},
\qquad
a_2=\frac\pi4,
\tag{3.2}
\]

\[
a_3=\frac{\sqrt2\,\pi(\pi^2-96)}{768},
\qquad
 a_4=\frac{\pi(24-\pi^2)}{192}.
\tag{3.3}
\]

This proves (1.2).

---

## 4. Recovering the spectral gap

Since

\[
e_\ell=2-2\cos(x_\ell/\ell),
\]

use

\[
2-2\cos u
=u^2-\frac{u^4}{12}+\frac{u^6}{360}+O(u^8)
\]

and substitute (1.2). Collecting powers of `1/ell` yields exactly (1.3).

The exponentially small finite-hard-arc correction is smaller than every displayed algebraic order, uniformly under (1.1).

## 5. Consequence for the antiperiodic-dominant regime

If `m/N -> gamma>1`, the antiperiodic well is the unique leading macroscopic well. Combining (1.3) with the antiperiodic phase-slip theorem gives, already before the higher-order phase-slip refinement,

\[
\Gamma_{N,m,q}
=\frac{\pi^2}{4m^2}
-\frac{\pi^2}{2\sqrt2\,m^3}
+O(m^{-4}),
\]

uniformly over arbitrary odd multipliers. The next sections of the project refine the `m^-4,m^-5,m^-6` coefficients by incorporating the local phase-slip gain.