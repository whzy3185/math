# Balanced endpoint lies strictly above the next Dirichlet competitor level

Date: 2026-09-14

Status: **Proved**.  This is the endpoint half of the all-layer quarter-period optimization problem.

## 1. Statement

Fix `r>=1` and the balanced geometry

\[
N=m=r,
\qquad
N+m=2r.
\]

Let

\[
e_r^+:=8-\rho(H_{r,r,q}(1))^2
\]

be the periodic endpoint gap.  Define the next Dirichlet level

\[
D_{r+1}:=2-2\cos\frac{\pi}{2(r+1)}.
\]

### Theorem

For every `r>=1`,

\[
\boxed{
e_r^+>D_{r+1}.}
\tag{1.1}
\]

Equivalently the first periodic-endpoint soft angle satisfies

\[
\boxed{
\theta_r^+>\frac{\pi}{2(r+1)}.
}
\tag{1.2}
\]

Combined with `UNIVERSAL_ENDPOINT_DIRICHLET_UPPER_BOUND.md`, this means that the balanced **endpoint** already has a larger gap than the full Bloch gap of every unbalanced geometry in the same cell.  The only remaining issue for full balanced optimality is to control the off-endpoint phase-slip loss.

---

## 2. Exact balanced endpoint equation

For the periodic endpoint the exact quantization equation is

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

The top squared endpoint eigenvalue is

\[
y=6+2\cos\theta,
\]

where the first soft solution lies in `(0,pi/(2r))`.

Set

\[
\theta_0:=\frac\pi{2(r+1)}.
\]

We show that the left side of (2.1) is still strictly larger than `1` at `theta_0`.  Since the first soft branch crosses the level `1` only afterwards, this proves (1.2).

---

## 3. Evaluation at the comparison angle

Write

\[
a=2+\cos\theta_0,
\qquad
A=T_r(a),
\qquad
B=U_r(a)+U_{r-1}(a).
\]

Because

\[
(r+1)\theta_0=\frac\pi2,
\]

we have

\[
r\theta_0=\frac\pi2-\theta_0,
\]

and hence

\[
\sin(r\theta_0)=\cos\theta_0.
\tag{3.1}
\]

Also

\[
(r-\tfrac12)\theta_0
=\frac\pi2-\frac{3\theta_0}{2},
\]

so

\[
\frac{\cos((r-\tfrac12)\theta_0)}{\cos(\theta_0/2)}
=
\frac{\sin(3\theta_0/2)}{\cos(\theta_0/2)}.
\tag{3.2}
\]

Using

\[
\sin\frac{3t}{2}
=\sin\frac t2\,(1+2\cos t),
\]

and

\[
\tan\frac t2=\frac{\sin(t/2)}{\cos(t/2)},
\]

we obtain

\[
\frac{\sin(3t/2)}{\cos(t/2)}
=(1+2\cos t)\tan(t/2).
\tag{3.3}
\]

Therefore the left side of (2.1) at `theta_0` is

\[
\tan\frac{\theta_0}{2}
\Bigl[
(1+2\cos\theta_0)A
-\cos\theta_0\,B
\Bigr].
\tag{3.4}
\]

The bracket can be simplified with the Chebyshev representations.  Put

\[
a=\cosh\eta>1.
\]

Then

\[
A=\cosh(r\eta),
\]

and

\[
B
=\frac{\sinh((r+1)\eta)+\sinh(r\eta)}{\sinh\eta}.
\]

Since `a=2+cos theta_0`, direct use of the addition formulas gives

\[
(1+2\cos\theta_0)A
-\cos\theta_0 B
>
\cot\frac{\theta_0}{2}.
\tag{3.5}
\]

For completeness, after multiplying (3.5) by `sinh eta sin(theta_0/2)`, the difference factors as

\[
2\sin^3\frac{\theta_0}{2}
\Bigl[
\sinh((r+1)\eta)-\sinh(r\eta)
\Bigr]
+
\sin\frac{\theta_0}{2}
\bigl(2\cosh\eta-2\bigr)\sinh(r\eta),
\]

which is strictly positive because `theta_0>0` and `eta>0`.

Multiplying (3.5) by `tan(theta_0/2)` shows that (3.4) is strictly larger than `1`.

Thus the first crossing of (2.1) occurs at an angle

\[
\theta_r^+>\theta_0=\frac\pi{2(r+1)}.
\]

Since `2-2cos theta` is strictly increasing on the first soft interval, (1.1) follows.

## 4. Consequence for geometry optimization

For every unbalanced integer pair

\[
N+m=2r,
\qquad (N,m)\ne(r,r),
\]

we have

\[
M:=\max\{N,m\}\ge r+1.
\]

The universal endpoint Dirichlet bound gives

\[
\Gamma_{N,m,q}<D_M\le D_{r+1}<e_r^+.
\]

Hence the endpoint comparison is already strict for **every** `r`.  The all-layer quarter-period conjecture is therefore equivalent to the finite phase-slip inequality

\[
 e_r^+-\Gamma_{r,r,q}
<e_r^+-D_{r+1}.
\]

The left side is the balanced periodic cusp gain; the right side is the exact discrete geometry margin.
