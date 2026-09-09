# Compressed two-defect family: exact endpoint quantization and sharp large-period constant

Date: 2026-09-09

Status: **Proved**. This note belongs only to Paper I. It concerns the explicit compressed two-defect periodic phase and makes no statement about minimization over all finite signings.

This result supplements `GENERAL_TWO_DEFECT_COMPRESSION_THEOREM.md`. The general theorem proves a sub-eight Bloch edge for every even half-period `L>=4` and every odd jump multiplier. Here we identify the top squared eigenvalue at the periodic Bloch phase `z=1` exactly through a scalar Robin equation and obtain its sharp large-`L` asymptotics.

---

## 1. Setup

Let `L=2r>=6` be even and let

\[
s=L(2q+1),\qquad q\ge0,
\]

with the period-`2L` two-defect word from the general compression theorem. At the periodic Bloch phase `z=1`, the fiber is independent of `q`; denote it by

\[
H_L(1).
\]

Put

\[
e_L:=8-\rho(H_L(1))^2.
\]

The factorization already proved in the general theorem is

\[
\det(\lambda I-H_L(1))
=p_r(y)\bigl(p_r(y)+4\bigr),
\qquad y=\lambda^2,
\tag{1.1}
\]

where

\[
\begin{aligned}
p_r(y)={}&
U_{r-2}\!\left(\frac{y-6}{2}\right)(y^2-8y+6)\\
&-U_{r-3}\!\left(\frac{y-6}{2}\right)(y-2)-2.
\end{aligned}
\tag{1.2}
\]

The general theorem also shows that neither factor has a root in `[8,\infty)`.

---

## 2. Exact scalar quantization equation

Write

\[
y=6+2\cos\theta,
\qquad 0<\theta<\pi.
\tag{2.1}
\]

Then

\[
8-y=2-2\cos\theta.
\]

Using

\[
U_j(\cos\theta)=\frac{\sin((j+1)\theta)}{\sin\theta},
\]

and substituting `y=6+2\cos\theta` into (1.2), a direct simplification gives

\[
\frac12 p_r(y)\sin\theta
=(2+\cos\theta)\sin(r\theta)
-3\sin((r-1)\theta)-\sin\theta.
\tag{2.2}
\]

Set

\[
n=r-1=\frac L2-1,
\qquad x=n\theta.
\]

Expanding `\sin(r\theta)=\sin(x+\theta)` and using

\[
\frac{\cos\theta-1}{\sin\theta}
=-\tan\frac\theta2,
\]

shows that `p_r(y)=0` is equivalent to

\[
\boxed{
(2+\cos(x/n))\cos x
-(3+\cos(x/n))\tan\!\left(\frac{x}{2n}\right)\sin x
=1.
}
\tag{2.3}
\]

This is the exact Robin quantization law for the upper soft mode.

---

## 3. Unique top root

Define on `0<=x<=\pi/2`

\[
f_n(x)=
(2+\cos(x/n))\cos x
-(3+\cos(x/n))\tan\!\left(\frac{x}{2n}\right)\sin x-1.
\tag{3.1}
\]

We have

\[
f_n(0)=2>0,
\qquad
f_n(\pi/2)<0.
\]

Moreover `f_n` is strictly decreasing on `(0,\pi/2)`. Indeed,

\[
a_n(x):=2+\cos(x/n)
\]

is positive and nonincreasing, while `\cos x` is strictly decreasing. For the second coefficient, put

\[
t=\tan\frac{x}{2n}\ge0.
\]

Then

\[
(3+\cos(x/n))\tan\frac{x}{2n}
=\frac{2t(2+t^2)}{1+t^2},
\]

whose derivative with respect to `t` is

\[
\frac{2(t^4+t^2+2)}{(1+t^2)^2}>0.
\]

Since both this coefficient and `\sin x` increase, its negative contribution in (3.1) is strictly decreasing. Hence there is a unique

\[
\boxed{x_n\in(0,\pi/2)}
\tag{3.2}
\]

satisfying (2.3).

Let

\[
\theta_n=\frac{x_n}{n},
\qquad
y_n=6+2\cos\theta_n.
\]

For `0<\theta<\theta_n`, equation (2.2) and the strict monotonicity above give `p_r(y)>0`. Therefore `p_r(y)+4>0` as well. Thus no root of either factor in (1.1) lies in `(y_n,8]`, whereas `p_r(y_n)=0`. Consequently

\[
\boxed{ho(H_L(1))^2=y_n,}
\tag{3.3}
\]

and hence

\[
\boxed{
e_L=2-2\cos\theta_n.}
\tag{3.4}
\]

So (2.3) is not merely an auxiliary root equation: it determines the exact top squared eigenvalue at `z=1`.

---

## 4. Limiting Robin constant

Let

\[
\alpha:=\arccos\frac13\in(0,\pi/2).
\tag{4.1}
\]

As `n\to\infty`, the functions `f_n` converge uniformly on `[0,\pi/2]` to

\[
f_\infty(x)=3\cos x-1.
\]

The latter has the unique zero `x=\alpha`. Since every `f_n` is strictly decreasing and has a unique zero, it follows that

\[
\boxed{x_n\longrightarrow\alpha.}
\tag{4.2}
\]

A first-order expansion is also explicit. Uniformly for `x` in compact subsets of `(0,\pi/2)`,

\[
f_n(x)
=3\cos x-1-rac{2x}{n}\sin x+O(n^{-2}).
\tag{4.3}
\]

Writing

\[
x_n=\alpha+\frac a n+O(n^{-2})
\]

and inserting this in (4.3), the coefficient of `n^{-1}` is

\[
-(3a+2\alpha)\sin\alpha.
\]

Therefore

\[
\boxed{
x_n
=\alpha-\frac{2\alpha}{3n}+O(n^{-2}).}
\tag{4.4}
\]

---

## 5. Sharp endpoint gap asymptotic

Since

\[
n=\frac L2-1,
\]

(4.4) gives

\[
\theta_n
=\frac{2\alpha}{L}
+\frac{4\alpha}{3L^2}
+O(L^{-3}).
\tag{5.1}
\]

Using

\[
2-2\cos\theta=\theta^2+O(\theta^4),
\]

we obtain

\[
\boxed{
e_L
=\frac{4\alpha^2}{L^2}
+\frac{16\alpha^2}{3L^3}
+O(L^{-4}),
\qquad
\alpha=\arccos\frac13.
}
\tag{5.2}
\]

In particular,

\[
\boxed{
L^2e_L
\longrightarrow
4\arccos^2\frac13
=6.0610443485\ldots .
}
\tag{5.3}
\]

Equivalently,

\[
L^2e_L
=4\alpha^2+rac{16\alpha^2}{3L}+O(L^{-2}).
\tag{5.4}
\]

The constant is different from the `\pi^2` constant in the older period-`4s` family. The compressed two-defect family therefore has a genuinely different soft-boundary quantization mechanism.

---

## 6. Consequence and remaining global-phase problem

Let

\[
g_{L,q}:=8-R_{L,q}
\]

be the full continuous Bloch gap of the compressed family. Since `z=1` is one admissible Bloch phase,

\[
0<g_{L,q}\le e_L.
\]

Hence

\[
\boxed{
\limsup_{L\to\infty}L^2g_{L,q}
\le4\arccos^2\frac13
}
\]

for any sequence of odd multipliers `2q+1` for which the compressed family is defined.

Exact numerical exploration strongly indicates that for every even `L>=6` and every `q>=0`, the global Bloch edge is actually attained at `z=1`, in which case `g_{L,q}=e_L` and (5.2)--(5.3) would become the sharp global compressed-family asymptotic. This equality is **not** asserted here; proving the global phase localization is the next analytic target.
