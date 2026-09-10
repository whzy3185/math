# Universal cubic correction for the macroscopic endpoint gaps

Date: 2026-09-10

Status: **Proved**. This refines the periodic and antiperiodic Dirichlet laws by one order.

## 1. Setup

Write

\[
L=2(N+m),\qquad h=2m,
\]

and assume a macroscopic regime

\[
N,m\to\infty,
\qquad
0<c_0\le\frac mN\le c_1<\infty.
\tag{1.1}
\]

Let

\[
e^+_{N,m}:=8-\rho(H(1))^2,
\qquad
e^-_{N,m}:=8-\rho(H(-1))^2.
\]

## Theorem A — periodic endpoint cubic correction

Uniformly under (1.1),

\[
\boxed{
e^+_{N,m}
=
\frac{\pi^2}{4N^2}
-
\frac{\pi^2}{2\sqrt2\,N^3}
+o(N^{-3}).
}
\tag{1.2}
\]

## Theorem B — antiperiodic endpoint cubic correction

Uniformly under (1.1),

\[
\boxed{
e^-_{N,m}
=
\frac{\pi^2}{4m^2}
-
\frac{\pi^2}{2\sqrt2\,m^3}
+o(m^{-3}).
}
\tag{1.3}
\]

The same universal coefficient appears at both endpoints.

---

## 2. Periodic quantization to first correction

Use the exact periodic endpoint equation with `h=2m`:

\[
\frac{\cos((N-\tfrac12)\theta)}{\cos(\theta/2)}
-
R_m(2+\cos\theta)
\tan(\theta/2)\sin(N\theta)
=
\frac1{T_m(2+\cos\theta)},
\tag{2.1}
\]

where

\[
R_m(a)=\frac{U_m(a)+U_{m-1}(a)}{T_m(a)}.
\]

Under (1.1), the endpoint theorem gives `theta=O(N^-1)`. Hence

\[
a=2+\cos\theta=3+O(N^{-2}).
\]

Since `m` is comparable to `N`, the right side of (2.1) is exponentially small. Moreover the hyperbolic formula gives

\[
R_m(a)=R_\infty(3)+O(N^{-2})+O(\Lambda^{-2m}),
\tag{2.2}
\]

with

\[
\Lambda=3+2\sqrt2
\]

and

\[
R_\infty(3)
=\frac{\Lambda+1}{2\sqrt2}
=1+\sqrt2.
\tag{2.3}
\]

Put

\[
x=N\theta.
\]

Expand (2.1) uniformly for `x` in a fixed neighborhood of `pi/2`:

\[
\cos x
+
\frac{x}{2N}\bigl(1-R_\infty(3)\bigr)\sin x
+O(N^{-2})=0.
\tag{2.4}
\]

Write

\[
x=\frac\pi2+\frac aN+O(N^{-2}).
\]

Since

\[
\cos x=-\frac aN+O(N^{-2}),
\qquad
\sin x=1+O(N^{-2}),
\]

substitution into (2.4) gives

\[
-a+\frac\pi4(1-R_\infty(3))=0.
\]

Using (2.3),

\[
\boxed{
a=-\frac\pi{2\sqrt2}.}
\tag{2.5}
\]

Therefore

\[
\boxed{
N\theta
=\frac\pi2-rac\pi{2\sqrt2\,N}+O(N^{-2}).
}
\tag{2.6}
\]

Since

\[
e^+_{N,m}=2-2\cos\theta
=\theta^2+O(\theta^4),
\]

and `theta=x/N`, equations (2.5)--(2.6) give

\[
\begin{aligned}
e^+_{N,m}
&=
\frac1{N^2}
\left(
\frac{\pi^2}{4}
+\frac{\pi a}{N}
+O(N^{-2})
\right)\\
&=
\frac{\pi^2}{4N^2}
-
\frac{\pi^2}{2\sqrt2\,N^3}
+O(N^{-4}),
\end{aligned}
\]

uniformly under (1.1). This proves (1.2), in fact with an `O(N^-4)` remainder when the ratio stays in a fixed compact subset of `(0,infinity)`.

---

## 3. Antiperiodic correction by the dual soft channel

At `z=-1`, the defect arc is the soft channel of length `m` and the complementary generic arc is the hard channel of length `N`. The exact antiperiodic transfer equation is obtained from the same `4 x 4` monodromy after interchanging the two scalar-square channel parameters.

Under (1.1), the generic hard channel has the same stable transfer ratio

\[
\Lambda^{-1}=3-2\sqrt2.
\]

Writing the antiperiodic soft angle as `vartheta` and

\[
y=m\vartheta,
\]

the same first-order normalized equation is

\[
\cos y
+
\frac{y}{2m}(1-R_\infty(3))\sin y
+O(m^{-2})=0.
\]

Therefore

\[
\boxed{
m\vartheta
=\frac\pi2-rac\pi{2\sqrt2\,m}+O(m^{-2}),}
\tag{3.1}
\]

and hence

\[
e^-_{N,m}
=2-2\cos\vartheta
=
\frac{\pi^2}{4m^2}
-
\frac{\pi^2}{2\sqrt2\,m^3}
+O(m^{-4}).
\]

This proves (1.3).

---

## 4. Interpretation

The leading Dirichlet constant `pi^2/4` is universal because the opposite arc becomes an asymptotically impenetrable wall. The first correction remembers that the wall is not exactly Dirichlet: its stable hyperbolic transfer ratio is

\[
3-2\sqrt2.
\]

The resulting Robin shift is

\[
-\frac\pi{2\sqrt2}
\]

in the scaled soft coordinate, and this produces the identical cubic coefficient at the two Bloch endpoints.

This common cubic correction is the key finite-size input for proving eventual exact balanced-geometry optimality at a fixed period.