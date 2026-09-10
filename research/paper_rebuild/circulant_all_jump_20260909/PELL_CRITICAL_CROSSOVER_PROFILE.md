# Critical crossover profile at the Pell phase boundary

Date: 2026-09-10

Status: **Proved**. This refines the exact threshold classification by determining the spectral scale inside the antiperiodic fiber when the defect length is comparable to the Pell threshold.

## 1. Setup

Write

\[
L=2(N+m),\qquad h=2m,
\]

and put

\[
U_N:=U_{N-1}(3).
\]

At the antiperiodic phase `z=-1`, let

\[
\lambda^-_{N,m}:=\rho(H_{N,m,q}(-1))^2.
\]

This value is independent of the odd multiplier. Consider sequences

\[
N\to\infty,
\qquad
\frac{m}{U_N}\longrightarrow c\in(0,\infty).
\tag{1.1}
\]

The exact phase boundary satisfies

\[
2m<T_N(3)
\quad\Longleftrightarrow\quad
\lambda^-_{N,m}<8,
\]

and

\[
\frac{T_N(3)}{2U_N}\to\sqrt2.
\]

Thus the critical ratio in (1.1) is `c=sqrt(2)`.

---

## Theorem A — subcritical trigonometric profile

Assume

\[
0<c<\sqrt2.
\]

Let `x_c in (0,pi/2)` be the unique solution of

\[
\boxed{
x_c\cot x_c=\frac c{\sqrt2}.}
\tag{2.1}
\]

Then

\[
\boxed{
m^2\bigl(8-\lambda^-_{N,m}\bigr)
\longrightarrow x_c^2.}
\tag{2.2}
\]

For `c->0`, `x_c->pi/2`, recovering the ordinary antiperiodic Dirichlet constant `pi^2/4`.

## Theorem B — supercritical hyperbolic profile

Assume

\[
c>\sqrt2.
\]

Let `kappa_c>0` be the unique solution of

\[
\boxed{
\kappa_c\coth\kappa_c=\frac c{\sqrt2}.}
\tag{2.3}
\]

Then

\[
\boxed{
m^2\bigl(\lambda^-_{N,m}-8\bigr)
\longrightarrow\kappa_c^2.}
\tag{2.4}
\]

Thus the same critical scattering law analytically continues from `cot` to `coth` across the exact Pell transition.

---

## 2. Exact antiperiodic characteristic equation

Use the exact squared characteristic polynomial

\[
\begin{aligned}
P^-_{N,m}(y)={}&
 y(y-8)(y^2-8y+10)p^2u^2\\
&-y(y-8)(y-6)p^2uw\\
&+(y^2-12y+16)p^2\\
&-y(y-8)(y-2)pvu^2\\
&+2y(y-8)pvuw\\
&+y(y-4)u^2+4,
\end{aligned}
\tag{3.1}
\]

where

\[
a=\frac{y-2}{2},\qquad b=\frac{y-6}{2},
\]

\[
u=U_{N-1}(a),\quad w=U_{N-2}(a),
\]

\[
p=U_{m-1}(b),\quad v=U_{m-2}(b).
\]

The top antiperiodic squared eigenvalue is the root of (3.1) closest to `8` on the appropriate side.

---

## 3. Generic hard-channel normalization

On either side of the transition the spectral displacement from `8` is `O(m^-2)`. Since

\[
m\asymp U_N\asymp(3+2\sqrt2)^N,
\]

this displacement is exponentially small in `N`. Hence

\[
a=3+O(m^{-2}),
\]

and therefore

\[
\boxed{
\frac{u}{U_N}\to1,
\qquad
\frac wu\to\Lambda^{-1},
\qquad
\Lambda=3+2\sqrt2.
}
\tag{3.2}
\]

The perturbation of the hard Chebyshev factor caused by an `O(m^-2)` spectral shift is negligible because `Nm^-2->0`.

---

## 4. Subcritical limit

Suppose `c<sqrt(2)`. By the exact phase diagram, the antiperiodic top root lies below `8` for all sufficiently large `N`. Write

\[
y=8-g,
\qquad
g>0,
\]

and define

\[
g=2-2\cos\theta,
\qquad
x=m\theta.
\tag{4.1}
\]

The first-cell trial bound gives `x=O(1)`. Along a convergent subsequence let `x->x_*`.

Then

\[
p=\frac{\sin(m\theta)}{\sin\theta},
\qquad
v=\frac{\sin((m-1)\theta)}{\sin\theta},
\]

so, using `m/U_N->c`,

\[
\frac p{U_N}
\longrightarrow
c\frac{\sin x_*}{x_*},
\qquad
\frac v{U_N}
\longrightarrow
c\frac{\sin x_*}{x_*}.
\tag{4.2}
\]

Also

\[
gm^2\to x_*^2.
\tag{4.3}
\]

Divide (3.1) by `U_N^2`. The coefficient limits at `y=8` are

\[
\frac{y(y-8)(y^2-8y+10)}g\to-80,
\]

\[
\frac{-y(y-8)(y-6)}g\to16,
\]

\[
\frac{-y(y-8)(y-2)}g\to48,
\]

\[
\frac{2y(y-8)}g\to-16,
\qquad
y(y-4)\to32.
\]

Because

\[
gp^2\to\sin^2x_*,
\qquad
gpv\to\sin^2x_*,
\]

while

\[
\frac{p^2}{U_N^2}	o
c^2\left(\frac{\sin x_*}{x_*}\right)^2,
\]

the limiting root equation is

\[
32\cos^2x_*
-16c^2\left(\frac{\sin x_*}{x_*}\right)^2=0.
\tag{4.4}
\]

The top root lies in the first oscillatory cell, so `0<=x_*<=pi/2`. Taking the positive square root in (4.4) gives

\[
\sqrt2\cos x_*
=c\frac{\sin x_*}{x_*},
\]

or

\[
x_*\cot x_*=\frac c{\sqrt2}.
\]

The function `x cot x` decreases strictly from `1` to `0` on `(0,pi/2)`, so for `0<c<sqrt(2)` there is a unique solution `x_c`. Every subsequence has the same limit, hence

\[
x\to x_c.
\]

Equation (4.3) proves (2.2).

---

## 5. Supercritical limit

Suppose `c>sqrt(2)`. The exact phase diagram gives a root above `8`. Write

\[
y=8+g,
\qquad g>0,
\]

and define

\[
g=2\cosh\theta-2,
\qquad
\kappa=m\theta.
\tag{5.1}
\]

Then

\[
p=\frac{\sinh(m\theta)}{\sinh\theta},
\qquad
v=\frac{\sinh((m-1)\theta)}{\sinh\theta}.
\]

Along a convergent subsequence `kappa->kappa_*`,

\[
\frac p{U_N}
\to c\frac{\sinh\kappa_*}{\kappa_*},
\qquad
\frac v{U_N}
\to c\frac{\sinh\kappa_*}{\kappa_*},
\]

and

\[
gm^2\to\kappa_*^2.
\]

Repeating the normalized calculation with hyperbolic functions gives

\[
32\cosh^2\kappa_*
-16c^2\left(\frac{\sinh\kappa_*}{\kappa_*}\right)^2=0.
\tag{5.2}
\]

Thus

\[
\sqrt2\cosh\kappa_*
=c\frac{\sinh\kappa_*}{\kappa_*},
\]

which is equivalent to

\[
\kappa_*\coth\kappa_*=rac c{\sqrt2}.
\]

The function `kappa coth kappa` increases strictly from `1` to infinity on `(0,infinity)`, so the solution is unique. Hence `kappa->kappa_c`, proving (2.4).

---

## 6. Near-critical expansion

The two profiles meet continuously at `c=sqrt(2)`. Write

\[
c=\sqrt2(1-\varepsilon),
\qquad\varepsilon\downarrow0.
\]

Since

\[
x\cot x=1-\frac{x^2}{3}+O(x^4),
\]

we obtain on the safe side

\[
\boxed{
x_c^2=3\varepsilon+O(\varepsilon^2).}
\tag{6.1}
\]

On the supercritical side, for

\[
c=\sqrt2(1+\varepsilon),
\]

use

\[
\kappa\coth\kappa
=1+\frac{\kappa^2}{3}+O(\kappa^4)
\]

to get

\[
\boxed{\kappa_c^2=3\varepsilon+O(\varepsilon^2).}
\tag{6.2}
\]

Thus the squared spectral displacement from `8` vanishes linearly in the relative distance from the Pell critical ratio, once measured in the natural `m^-2` scale.

## 7. Interpretation

The exact integer phase boundary is controlled by Pell arithmetic, but its local spectral shape is governed by a universal one-dimensional scattering law:

\[
\text{trigonometric Robin branch}
\longleftrightarrow
\text{critical point}
\longleftrightarrow
\text{hyperbolic bound-state branch}.
\]

The parameter `c=m/U_{N-1}(3)` is the natural renormalized defect length, and `c=sqrt(2)` is both the exact asymptotic Pell threshold and the bifurcation point of the limiting spectral equation.