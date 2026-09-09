# Scaling obstruction for almost-antipodal defect width

Date: 2026-09-09

Status: **Proved**. This note belongs only to Paper I.

The fixed-separation Robin hierarchy shows that, for every fixed defect separation `2h`, widening `h` improves the large-period quadratic gap constant and the constants approach `pi^2`. The present theorem shows that this conclusion cannot be extrapolated to defect widths growing arbitrarily with the half-period.

In the almost-antipodal regime the same two-defect family actually crosses **above** the squared edge `8`.

## 1. Setup

Let

\[
L=2r,
\qquad r\ge3,
\]

and choose the two positive local flux defects at positions

\[
0
\quad\text{and}\quad
2h=L-2,
\qquad h=r-1.
\]

Thus the defect separation is as large as possible while the two-point local-flux pattern still has primitive period `2L`.

Take any jump

\[
s=L(2q+1),
\qquad q\ge0.
\]

At the antiperiodic Bloch phase

\[
z=-1,
\]

the compressed long-jump phase satisfies

\[
z^{2q+1}=-1,
\]

so the relevant fiber is independent of the odd multiplier up to a harmless unitary sign change.

## Theorem A — exact edge crossing

For every `r>=3`, the antiperiodic fiber has a squared eigenvalue strictly larger than `8`. In particular,

\[
\boxed{
R^{(r-1)}_{2r,q}>8
}
\tag{1.1}
\]

for every `q>=0`.

Thus the almost-antipodal two-defect geometry is **not** a sub-eight phase.

### Proof

At `z=-1`, choose the square root `eta=i`. After the standard half-period folding and Pauli gauge, there are exactly two generic sites and `L-2=2r-2` consecutive defect sites.

Write

\[
y=\lambda^2,
\qquad
N=r-1,
\qquad
t=\frac{y-6}{2},
\]

and put

\[
u=U_N(t),
\qquad
v=U_{N-1}(t).
\]

A direct `4 x 4` transfer reduction gives the exact squared characteristic determinant

\[
\boxed{
D_N(y)
=uv\,(y^3-10y^2+16y)
+v^2(-y^2+4y+16)
+(y-2)^2.
}
\tag{1.2}
\]

The derivation uses the even-power continuant formula for the defect transfer and the Chebyshev identity

\[
u^2+v^2-(y-6)uv=1.
\]

At the threshold `y=8`,

\[
y^3-10y^2+16y=0,
\]

\[
-y^2+4y+16=-16,
\]

and because `t=1`,

\[
v=U_{N-1}(1)=N=r-1.
\]

Hence

\[
\boxed{
D_N(8)
=36-16(r-1)^2<0
\qquad(r\ge3).
}
\tag{1.3}
\]

The squared characteristic polynomial is monic, so

\[
D_N(y)\to+\infty
\qquad(y\to+\infty).
\]

Since the fiber is Hermitian, all squared spectral roots are real and nonnegative. By continuity, (1.3) forces at least one squared eigenvalue in `(8,infinity)`. This proves Theorem A.

---

## 2. The limiting bound-state energy

The crossing does not vanish as the period grows. In fact it converges to an explicit algebraic value.

### Theorem B

Let `y_r>8` be the largest squared eigenvalue of the `z=-1` fiber. Then

\[
\boxed{
y_r\longrightarrow y_*
:=\frac{38+10\sqrt{13}}9
=8.228390306071\ldots.}
\tag{2.1}
\]

Consequently

\[
\boxed{
\liminf_{r\to\infty}
\bigl(R^{(r-1)}_{2r,q}-8\bigr)
\ge
\frac{10\sqrt{13}-34}{9}>0.
}
\tag{2.2}
\]

The limit is independent of the odd multiplier.

### Proof

For fixed `y>8`, set

\[
a(y)
:=t-\sqrt{t^2-1},
\qquad t=\frac{y-6}{2}.
\]

Then

\[
0<a(y)<1,
\qquad
\frac{v}{u}\longrightarrow a(y)
\]

uniformly on compact subsets of `(8,infinity)`, while `uv->infinity`.

Divide (1.2) by `uv`. The last term vanishes and the normalized determinant converges to

\[
f(y)
:=y^3-10y^2+16y
+a(y)(-y^2+4y+16).
\tag{2.3}
\]

The hyperbolic parameter satisfies

\[
a^2-(y-6)a+1=0,
\]

so

\[
y=6+a+a^{-1}.
\]

Substituting this into (2.3) gives the exact factorization

\[
\boxed{
f(y(a))
=\frac{(a^2-4a-1)(9a^2-4a-1)}{a^3}.}
\tag{2.4}
\]

On the physical interval `0<a<1`, the first factor has no zero. The second has the unique positive root

\[
\boxed{
a_*=rac{2+\sqrt{13}}9.}
\tag{2.5}
\]

Since `a(y)` decreases strictly from `1` to `0` as `y` increases from `8` to infinity, the corresponding unique physical zero is

\[
\begin{aligned}
y_*
&=6+a_*+a_*^{-1}\\
&=\boxed{\frac{38+10\sqrt{13}}9}.
\end{aligned}
\]

The zero is simple. Uniform convergence of the normalized determinants on compact neighborhoods of `y_*` gives a squared eigenvalue `y_r->y_*`.

The remaining roots above the bulk edge are excluded from having a larger limit by the uniqueness of the physical zero of (2.3); roots escaping to infinity are impossible because the operator norms are uniformly bounded by `4`. Hence the top squared eigenvalue converges to `y_*`.

---

## 3. Interpretation

The geometry of the two-defect family has two distinct regimes.

### Fixed width

For fixed `h` and `L->infinity`,

\[
L^2(8-R^{(h)}_{L,q})
\longrightarrow
4\arccos^2\!\frac1{T_h(3)}
>0,
\]

and the constant increases to `pi^2` as `h->infinity` **after** the fixed-width large-`L` limit.

### Width proportional to the cell

The choice

\[
h=r-1\asymp L
\]

produces a finite-rank bound state above the threshold instead:

\[
R>8.
\]

Therefore the two limits do not commute:

\[
\boxed{
\lim_{h\to\infty}\lim_{L\to\infty}
L^2(8-R^{(h)}_{L,q})=\pi^2
}
\]

is compatible with the failure of sub-eight spectral control when `h/L` stays macroscopic.

This obstruction is essential when formulating any defect-width optimization theorem. The correct next problem is to determine the growth window `h=h(L)` for which the compressed phase remains below `8` and to locate the transition from the Robin regime to the above-edge bound-state regime.