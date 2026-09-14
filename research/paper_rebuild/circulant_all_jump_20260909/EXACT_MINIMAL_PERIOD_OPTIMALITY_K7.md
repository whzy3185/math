# Exact quarter-period optimality in the `v_2(s)=7` minimal layer

Date: 2026-09-14

Status: **Proved** with exact rational Bernstein and endpoint derivative certificates.

## 1. Minimal cell

For

\[
2^7\Vert s,
\]

the minimal compatible half-period is `L=128`, the primitive coefficient period is

\[
p=256,
\]

and

\[
N+m=L/2=64.
\]

The quarter-period geometry is

\[
\boxed{N=m=32,
\qquad h=64=p/4.}
\]

Choose the rational separator

\[
\boxed{
g_0=\frac{23}{10000},
\qquad y_0=8-\frac{23}{10000}.}
\tag{1.1}
\]

Every unbalanced geometry has

\[
M=\max\{N,m\}\ge33.
\]

By the universal endpoint Dirichlet bound,

\[
\Gamma_{N,m,q}<D_{33}
=2-2\cos\frac\pi{66}.
\]

Using `cos x>1-x^2/2` and `pi^2<10`,

\[
D_{33}<\frac{10}{4\cdot33^2}
=\frac{10}{4356}
<\frac{23}{10000}.
\tag{1.2}
\]

Thus all unbalanced competitors have gap smaller than `g_0`.

---

## 2. Balanced relaxed certificate

Apply `ALL_ENERGY_SINGLE_SQUARE_IDENTITY.md` with `N=m=32` and `y=y_0`.  Under

\[
d=4t-2,
\qquad0\le t\le1,
\]

the relaxed determinant

\[
P_{32,32}(y_0;d,2)
\]

is a degree-128 polynomial in `t`.

Its degree-128 Bernstein expansion has **129 strictly positive exact rational coefficients**.  The minimum is again the first coefficient, corresponding to the antiperiodic long-phase endpoint `d=-2`, and satisfies numerically in size

\[
\boxed{
\min b_j>4.1\times10^{43}.
}
\tag{2.1}
\]

The sign statement is exact: every coefficient has positive integer numerator and positive integer denominator. Therefore

\[
P_{32,32}(y_0;d,2)>0
\qquad(-2\le d\le2).
\tag{2.2}
\]

For a physical Bloch phase `e<=2`,

\[
P_{32,32,q,z}(y_0)
=P_{32,32}(y_0;d,2)+(2-e)>0.
\tag{2.3}

---

## 3. Reference-fiber inertia

At `z=1`, the balanced squared characteristic polynomial has degree `128` and factors exactly into two monic degree-64 integer polynomials.

At the rational test energy `y_0=8-23/10000`, each factor and **all of its derivatives from order 1 through order 64** are strictly positive in exact rational arithmetic. Since the top derivative is a positive constant, descending induction proves that both factors remain positive for every

\[
y\ge y_0.
\]

Thus the reference fiber has no squared eigenvalue at or above `y_0`.  Equation (2.3) prevents any Bloch crossing of `y_0`, so inertia is constant around the circle and

\[
\boxed{
R_{32,32,q}<8-\frac{23}{10000},
\qquad
\Gamma_{32,32,q}>\frac{23}{10000}.
}
\tag{3.1}

---

## Theorem — exact `k=7` optimizer

Combining (1.2) and (3.1), for every odd multiplier,

\[
\boxed{
\Gamma_{32,32,q}
>
\Gamma_{N,m,q}
\qquad
(N+m=64,\ (N,m)\ne(32,32)).
}
\]

Therefore for every jump

\[
s=128(2q+1),
\]

the unique gap-maximizing even-separation reflection-chiral two-defect geometry in the minimal primitive period `256` is

\[
\boxed{h=64=p/4.}
\]

## 5. Structural pattern exposed by the exact layers

The exact layers `k=4,5,6,7` share two striking features:

1. at a separator strictly between the universal competitor bound `D_{r+1}` and the balanced gap, **every Bernstein coefficient of the relaxed balanced determinant is positive**;
2. the smallest Bernstein coefficient occurs at `d=-2`.

This strongly suggests a direct all-`r` Bernstein/total-positivity proof of the quarter-period theorem, rather than layer-by-layer certification.  Establishing that recurrence is the next target.
