# Exact quarter-period optimality in the `v_2(s)=4` minimal layer

Date: 2026-09-14

Status: **Proved** with exact rational Bernstein and derivative certificates.

## 1. Minimal cell

Let

\[
2^4\Vert s.
\]

The minimal compatible half-period is `L=16`, so the primitive coefficient period is

\[
p=32.
\]

Write

\[
N+m=L/2=8.
\]

The quarter-period geometry is

\[
\boxed{N=m=4,\qquad h=8=p/4.}
\]

We prove that it uniquely maximizes the full Bloch gap among all even-separation two-defect geometries in this minimal cell, uniformly in the odd multiplier.

---

## 2. A rational separator

Choose

\[
\boxed{g_0=\frac1{10},\qquad y_0=8-g_0=\frac{79}{10}.}
\tag{2.1}
\]

Every unbalanced geometry has

\[
M:=\max\{N,m\}\ge5.
\]

By `UNIVERSAL_ENDPOINT_DIRICHLET_UPPER_BOUND.md`,

\[
\Gamma_{N,m,q}<D_M\le D_5,
\qquad
D_5=2-2\cos\frac\pi{10}.
\]

Using `cos x>1-x^2/2` and `pi^2<10`,

\[
D_5<\frac{\pi^2}{100}<\frac1{10}.
\tag{2.2}
\]

Thus every unbalanced competitor has gap strictly smaller than `1/10`. It remains to prove that the balanced full gap is strictly larger than `1/10`.

---

## 3. Relaxed balanced determinant at `y_0`

Use the all-energy single-square formula with `N=m=4`.  After substituting `y=79/10` and relaxing the seam to its hardest value `e=2`, one obtains a degree-16 polynomial

\[
P_{4,4}(y_0;d,2),
\qquad -2\le d\le2.
\]

Set

\[
d=4t-2,
\qquad0\le t\le1.
\]

In the degree-16 Bernstein basis, every coefficient is an exact positive rational number.  The first three and last three are

\[
\begin{aligned}
&\frac{69362734112006121761}{10^{16}},\\
&\frac{3004870560441296074561}{10^{16}},\\
&\frac{217408224415329014132963}{3\cdot10^{16}},
\end{aligned}
\]

and

\[
\begin{aligned}
&\frac{215817613076489014132963}{3\cdot10^{16}},\\
&\frac{2633706767781296074561}{10^{16}},\\
&\frac{70859931072006121761}{10^{16}}.
\end{aligned}
\]

The remaining eleven coefficients are also strictly positive; the exact minimum is the first coefficient and satisfies

\[
\boxed{
\min b_j
=\frac{69362734112006121761}{10^{16}}>6900.
}
\tag{3.1}
\]

Therefore

\[
\boxed{
P_{4,4}(y_0;d,2)>0
\qquad(-2\le d\le2).
}
\tag{3.2}

For a physical Bloch phase `e=z+z^{-1}<=2`, the all-energy formula is linear in the seam coordinate, hence

\[
P_{4,4,q,z}(y_0)
=P_{4,4}(y_0;d,2)+(2-e)>0.
\tag{3.3}
\]

Thus no Bloch eigenvalue can cross the test energy `y_0` as the phase varies.

---

## 4. Reference-fiber inertia

At `z=1`, the balanced characteristic polynomial in the squared variable factors exactly as

\[
P_{4,4,1}(y)=f_{1152}(y)f_{1156}(y),
\tag{4.1}
\]

where

\[
\boxed{
\begin{aligned}
f_a(y)={}&y^8-32y^7+420y^6-2912y^5+11428y^4\\
&-25152y^3+28544y^2-13312y+a
\end{aligned}}
\tag{4.2}
\]

with `a=1152,1156`.

At `y_0=79/10`, exact arithmetic gives

\[
f_{1152}(y_0)>82,
\qquad
f_{1156}(y_0)>86.
\tag{4.3}
\]

Moreover for each factor, every derivative from the first through the eighth is strictly positive at `y_0`; explicitly the common first seven derivative values begin

\[
8313.479\ldots,
43311.166\ldots,
125182.268\ldots,
\]

and all are rational numbers with positive numerator, while the eighth derivative is the positive constant `40320`.

This gives an exact inductive positivity certificate on `[y_0,\infty)`: the eighth derivative is positive; hence the seventh derivative is increasing and positive from `y_0` onward; descending inductively, every derivative and finally each `f_a` remains positive for all `y>=y_0`.

Therefore the reference fiber has no squared eigenvalue at or above `y_0`.

Together with (3.3) and inertia continuity around the Bloch circle,

\[
\boxed{
R_{4,4,q}<\frac{79}{10}.
}
\tag{4.4}

Hence

\[
\boxed{
\Gamma_{4,4,q}>\frac1{10}.
}
\tag{4.5}

---

## Theorem — exact `k=4` optimizer

Equations (2.2) and (4.5) give, for every odd multiplier,

\[
\boxed{
\Gamma_{4,4,q}
>
\Gamma_{N,m,q}
\qquad
(N+m=8,\ (N,m)\ne(4,4)).
}
\tag{5.1}

Thus for every jump

\[
s=16(2q+1),
\]

the unique gap-maximizing even-separation reflection-chiral two-defect geometry in the minimal primitive period `32` is the quarter-period separation

\[
\boxed{h=8=p/4.}
\]

No floating-point acceptance test is used in the proof; decimal displays in Section 4 are shorthand for positive exact rational evaluations.
