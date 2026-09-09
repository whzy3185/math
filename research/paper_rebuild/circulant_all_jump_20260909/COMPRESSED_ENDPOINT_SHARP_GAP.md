# Sharp endpoint gap for the compressed two-defect family

Date: 2026-09-09

Status: **Proved**. This note belongs only to Paper I. It concerns the periodic Bloch fiber `z=1` of the explicit compressed two-defect phase. It does **not** yet assert that `z=1` is the global maximizing Bloch phase for every parameter.

## 1. Setup

Let `L>=4` be even and let the period-`2L` two-defect word be

\[
Q_0=Q_2=1,\qquad Q_j=-1\quad(j\ne0,2),
\]

with Hamilton-gauge lift

\[
\tau_0=\tau_1=1,\qquad \tau_2=\tau_3=-1,\qquad
\tau_j=(-1)^j\quad(4\le j<2L).
\]

Let

\[
s=L(2q+1),\qquad q\ge0,
\]

and let `H_{L,q}(z)` denote the `2L x 2L` Bloch fiber of the corresponding signed step operator.

At `z=1`, the fiber is independent of `q`. Define its squared endpoint gap by

\[
e_L:=8-\rho(H_{L,q}(1))^2.
\]

Put

\[
r=L/2.
\]

The general compression theorem gives the exact factorization

\[
\det(\lambda I-H_{L,q}(1))
=p_r(y)\bigl(p_r(y)+4\bigr),\qquad y=\lambda^2,
\tag{1.1}
\]

where

\[
\begin{aligned}
p_r(y)={}&
U_{r-2}\!\left(\frac{y-6}{2}\right)(y^2-8y+6)\\
&-U_{r-3}\!\left(\frac{y-6}{2}\right)(y-2)-2,
\end{aligned}
\tag{1.2}
\]

with `U_{-1}=0`.

---

## 2. Exact Robin equation for the top squared eigenvalue

For a squared spectral value in `(6,8)`, write

\[
y=6+2\cos\theta
=8-(2-2\cos\theta),
\qquad 0<\theta<\pi/2.
\]

Then

\[
U_{r-2}(\cos\theta)=\frac{\sin((r-1)\theta)}{\sin\theta},
\qquad
U_{r-3}(\cos\theta)=\frac{\sin((r-2)\theta)}{\sin\theta}.
\]

Put

\[
x=r\theta.
\]

A direct trigonometric simplification of (1.2) gives the exact identity

\[
\boxed{
p_r(6+2\cos\theta)+2
=6\cos x+4\tan\frac{\theta}{2}\sin x.}
\tag{2.1}
\]

Indeed, after multiplying by `sin(theta)`, the left side reduces to

\[
4\sin x+5\sin(\theta-x)+\sin(\theta+x),
\]

which equals

\[
6\sin\theta\cos x+4(1-\cos\theta)\sin x.
\]

Dividing by `sin(theta)` proves (2.1).

The roots of the factor `p_r(y)` therefore satisfy

\[
\boxed{
3\cos x+2\tan\frac{x}{2r}\sin x=1.}
\tag{2.2}
\]

The roots of the companion factor `p_r(y)+4` satisfy the same left side with right side `-1`.

---

## 3. The top root is unique

Define

\[
\Phi_r(x)=6\cos x+4\tan\frac{x}{2r}\sin x,
\qquad 0\le x\le\frac\pi2.
\]

For `r>=2`, `Phi_r` is strictly decreasing on this interval. To see this,

\[
\Phi_r'(x)
=-6\sin x
+\frac2r\sec^2\frac{x}{2r}\sin x
+4\tan\frac{x}{2r}\cos x.
\]

By convexity of `tan` on `[0,pi/2)`,

\[
\tan\frac{x}{2r}\le\frac1{2r}\tan x,
\]

so

\[
4\tan\frac{x}{2r}\cos x\le\frac2r\sin x.
\]

Also

\[
\sec^2\frac{x}{2r}\le\sec^2\frac\pi8<\frac65.
\]

Hence

\[
\Phi_r'(x)
\le\sin x\left(-6+\frac{12}{5r}+\frac2r\right)<0
\]

for `r>=2` and `x>0`.

Now

\[
\Phi_r(0)=6>2,
\]

whereas

\[
\Phi_r(\pi/2)=4\tan\frac\pi{4r}<2
\]

for every `r>=2`. Thus there is a unique

\[
x_r\in(0,\pi/2)
\]

with

\[
\Phi_r(x_r)=2.
\tag{3.1}
\]

Equivalently, `x_r` is the unique solution of (2.2).

The companion equation `Phi_r(x)=-2` cannot have a root before `x_r`, because `Phi_r>=2` on `[0,x_r]`. Therefore the largest squared eigenvalue of the endpoint fiber is the `p_r=0` root

\[
\boxed{
\rho(H_{L,q}(1))^2
=6+2\cos\frac{x_r}{r}.}
\tag{3.2}
\]

Consequently

\[
\boxed{
e_L=2-2\cos\frac{x_r}{r}.}
\tag{3.3}
\]

This is an exact one-dimensional characterization for every even `L>=4`.

---

## 4. Sharp leading constant

Let

\[
x_0:=\arccos\frac13.
\tag{4.1}
\]

Equation (2.2) can be written as

\[
3\cos x_r+2\tan\frac{x_r}{2r}\sin x_r=1.
\tag{4.2}
\]

Since the second term is positive,

\[
x_r>x_0.
\]

The sequence `x_r` stays in `(x_0,pi/2)`. Every convergent subsequence has a limit `x` satisfying, by (4.2),

\[
3\cos x=1.
\]

The only solution in `[x_0,pi/2]` is `x=x_0`. Hence

\[
\boxed{x_r\longrightarrow x_0=\arccos(1/3).}
\tag{4.3}
\]

Using (3.3) and `L=2r`,

\[
\begin{aligned}
L^2e_L
&=4r^2\left(2-2\cos\frac{x_r}{r}\right)\\
&\longrightarrow4x_0^2.
\end{aligned}
\]

Thus

\[
\boxed{
L^2e_L\longrightarrow
4\arccos(1/3)^2.}
\tag{4.4}
\]

Numerically,

\[
4\arccos(1/3)^2\approx6.06104434856.
\]

No numerical input is used in the proof.

---

## 5. Higher endpoint expansion

The exact equation (4.2) also gives a systematic expansion. Write

\[
h=r^{-1},
\qquad
x_r=x_0+a_1h+a_2h^2+a_3h^3+O(h^4).
\]

Expanding

\[
3\cos x_r+2\tan\frac{hx_r}{2}\sin x_r=1
\]

and using

\[
\cos x_0=\frac13,
\qquad
\sin x_0=\frac{2\sqrt2}{3},
\]

gives

\[
\boxed{
a_1=\frac{x_0}{3},}
\tag{5.1}
\]

\[
\boxed{
a_2=\frac{x_0(\sqrt2\,x_0+8)}{72},}
\tag{5.2}
\]

and

\[
\boxed{
a_3=
\frac{x_0(10x_0^2+9\sqrt2\,x_0+24)}{648}.}
\tag{5.3}
\]

In particular,

\[
\boxed{
\begin{aligned}
e_L={}&\frac{4x_0^2}{L^2}
+\frac{16x_0^2}{3L^3}\\
&+\frac{4x_0^2}{9L^4}
\bigl(-3x_0^2+\sqrt2\,x_0+12\bigr)
+O(L^{-5}).
\end{aligned}}
\tag{5.4}
\]

Thus the compressed two-defect family has a polynomial endpoint gap with an explicit Robin constant, vastly stronger than the elementary determinant lower bound `16/8^(L-1)`.

---

## 6. Scope and next target

Theorem (4.4) is an endpoint theorem. To turn it into a theorem for the full continuous Bloch edge

\[
R_{L,q}=\max_{|z|=1}\rho(H_{L,q}(z))^2,
\]

one still needs to prove either

\[
\rho(H_{L,q}(z))^2\le\rho(H_{L,q}(1))^2
\]

for all phases in the relevant range (numerically true for every tested `L>=6`), or at least prove that any phase improvement is `o(L^-2)` uniformly in the odd multiplier. This is now the main quantitative target.
