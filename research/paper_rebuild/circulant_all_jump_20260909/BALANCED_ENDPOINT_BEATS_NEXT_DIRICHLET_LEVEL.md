# Balanced endpoint lies above the next Dirichlet competitor level

Date: 2026-09-14

Status: **Proved after hostile audit**.

Correction record: the first version stated the endpoint comparison for `r>=1` and used an overstrong factorization. Direct evaluation shows that `r=1` is exceptional. The corrected theorem is for `r>=2`; this is exactly what is needed for the nontrivial minimal-period layers, while `r=1` has no competing separation at all.

## 1. Statement

Fix the balanced geometry

\[
N=m=r
\]

and let

\[
e_r^+:=8-\rho(H_{r,r,q}(1))^2
\]

be its periodic endpoint gap. Define

\[
D_{r+1}:=2-2\cos\frac{\pi}{2(r+1)}.
\]

### Theorem

For every

\[
\boxed{r\ge2,}
\]

one has

\[
\boxed{
e_r^+>D_{r+1}.}
\tag{1.1}
\]

Equivalently, if `theta_r^+` is the first periodic soft angle, then

\[
\boxed{
\theta_r^+>\frac{\pi}{2(r+1)}.
}
\tag{1.2}
\]

For `r=1` the reverse inequality holds, but the minimal cell has only the single separation `m=N=1`, so no optimization issue exists in that layer.

---

## 2. Exact endpoint equation

The periodic endpoint quantization is

\[
\begin{aligned}
&T_r(2+\cos\theta)
\frac{\cos((r-\tfrac12)\theta)}{\cos(\theta/2)}\\
&\quad-
\bigl[U_r(2+\cos\theta)+U_{r-1}(2+\cos\theta)\bigr]
\tan(\theta/2)\sin(r\theta)
=1.
\end{aligned}
\tag{2.1}
\]

At `theta=0` its left side is `T_r(3)>1`.

Put

\[
t:=\frac\pi{2(r+1)},
\qquad
c:=\cos t,
\qquad
a:=2+c.
\]

Since

\[
r t=\frac\pi2-t,
\]

we have

\[
\sin(rt)=c,
\]

and

\[
\frac{\cos((r-\tfrac12)t)}{\cos(t/2)}
=(1+2c)\tan(t/2).
\]

Thus the left side of (2.1) at `theta=t` is

\[
\tan\frac t2\,K_r,
\tag{2.2}
\]

where

\[
K_r
:=(1+2c)T_r(a)
-c\,[U_r(a)+U_{r-1}(a)].
\tag{2.3}
\]

It suffices to prove

\[
K_r>\cot(t/2).
\tag{2.4}
\]

---

## 3. Uniform lower bound on the bracket

Write

\[
a=\cosh\eta,
\qquad \eta>0.
\]

The exact ratio is

\[
\frac{U_r(a)+U_{r-1}(a)}{T_r(a)}
=1+\tanh(r\eta)\coth(\eta/2).
\tag{3.1}
\]

Because

\[
\coth(\eta/2)
=\sqrt{\frac{a+1}{a-1}}
=\sqrt{\frac{3+c}{1+c}},
\]

and for `r>=2`

\[
t\le\frac\pi6,
\qquad c\ge\frac{\sqrt3}{2}>rac35,
\]

we have

\[
\sqrt{\frac{3+c}{1+c}}<\frac32.
\tag{3.2}
\]

Using `tanh(r eta)<1`, equations (3.1)--(3.2) imply

\[
\frac{U_r+U_{r-1}}{T_r}<\frac52.
\]

Hence

\[
\begin{aligned}
K_r
&>T_r(a)\left(1+2c-\frac52c\right)\\
&=T_r(a)\left(1-\frac c2\right)\\
&\ge\frac12T_r(a).
\end{aligned}
\tag{3.3}
\]

---

## 4. Chebyshev growth beats the comparison angle

For `r>=2`, `T_r(x)` is convex on `[1,\infty)` and

\[
T_r(1)=1,
\qquad T_r'(1)=r^2.
\]

Therefore

\[
T_r(a)
\ge1+r^2(a-1).
\tag{4.1}
\]

Since `c>=sqrt(3)/2`,

\[
a-1=1+c
\ge1+\frac{\sqrt3}{2}.
\]

Combining with (3.3),

\[
K_r
>\frac12\left[1+r^2\left(1+\frac{\sqrt3}{2}\right)\right].
\tag{4.2}
\]

On the other hand, `tan x>x` for `x>0`, so

\[
\cot(t/2)
<\frac2t
=\frac{4(r+1)}\pi.
\tag{4.3}
\]

For `r=2`, the right side of (4.2) is

\[
\frac12(5+2\sqrt3)>\frac{12}{\pi},
\]

and the difference between the quadratic lower bound in (4.2) and the linear upper bound in (4.3) increases for every larger integer `r`. Therefore

\[
K_r>\cot(t/2)
\qquad(r\ge2).
\]

By (2.2), the left side of the exact endpoint equation is still larger than `1` at `theta=t`. The first soft crossing therefore occurs strictly after `t`, proving (1.2) and hence (1.1).

---

## 5. Geometry consequence

Fix total geometry

\[
N+m=2r.
\]

Every unbalanced pair has

\[
M:=\max\{N,m\}\ge r+1.
\]

By `UNIVERSAL_ENDPOINT_DIRICHLET_UPPER_BOUND.md`,

\[
\Gamma_{N,m,q}<D_M\le D_{r+1}.
\]

Thus for every `r>=2`,

\[
\boxed{
\Gamma_{N,m,q}<D_{r+1}<e_r^+
\qquad((N,m)\ne(r,r)).
}
\tag{5.1}
\]

The remaining all-layer balanced-optimality question is exactly whether the periodic phase-slip loss of the balanced full Bloch gap remains smaller than the endpoint margin

\[
e_r^+-D_{r+1}.
\]
