# Exact quarter-period optimality in the `v_2(s)=6` minimal layer

Date: 2026-09-14

Status: **Proved** with exact rational Bernstein and endpoint derivative certificates.

## 1. Minimal cell

For

\[
2^6\Vert s,
\]

the minimal compatible half-period is `L=64`, the primitive coefficient period is

\[
p=128,
\]

and

\[
N+m=L/2=32.
\]

The quarter-period geometry is

\[
\boxed{N=m=16,
\qquad h=32=p/4.}
\]

Choose the rational separator

\[
\boxed{
g_0=\frac1{115},
\qquad y_0=8-\frac1{115}.}
\tag{1.1}
\]

Every unbalanced geometry has

\[
M=\max\{N,m\}\ge17.
\]

The universal endpoint bound gives

\[
\Gamma_{N,m,q}<D_{17}
=2-2\cos\frac\pi{34}.
\]

Since

\[
D_{17}<\frac{\pi^2}{1156}
<\frac{10}{1156}
=\frac5{578}
<\frac1{115},
\tag{1.2}
\]

all unbalanced competitors have gap smaller than `g_0`.

---

## 2. Exact balanced relaxed certificate

Apply the all-energy single-square identity with `N=m=16` and `y=y_0`.  After the affine change

\[
d=4t-2,
\qquad0\le t\le1,
\]

the relaxed determinant

\[
P_{16,16}(y_0;d,2)
\]

is a polynomial of degree `64` in `t`.

Its degree-64 Bernstein expansion has **65 strictly positive rational coefficients**.  The minimum is the `d=-2` endpoint coefficient; in decimal size it exceeds

\[
\boxed{4.5\times10^{20}}.
\tag{2.1}
\]

The positivity assertion is exact: every coefficient has positive integer numerator and positive integer denominator.  Therefore

\[
\boxed{
P_{16,16}(y_0;d,2)>0
\qquad(-2\le d\le2).
}
\tag{2.2}

For every physical Bloch phase `e=z+z^{-1}<=2`,

\[
P_{16,16,q,z}(y_0)
=P_{16,16}(y_0;d,2)+(2-e)>0.
\tag{2.3}

---

## 3. Reference-fiber inertia

At `z=1`, the balanced squared characteristic polynomial has degree `64` and factors exactly into two monic degree-32 integer polynomials.

At the rational test energy `y_0=8-1/115`, for **each** factor:

- the value itself is strictly positive;
- every derivative of orders `1,2,...,32` is strictly positive.

The order-32 derivative is a positive constant.  Descending induction therefore shows that both factors are positive on the whole interval

\[
[y_0,\infty).
\]

Thus the reference fiber has no squared eigenvalue at or above `y_0`.  Combining this with (2.3) and inertia continuity around the Bloch circle gives

\[
\boxed{
R_{16,16,q}<8-\frac1{115},
\qquad
\Gamma_{16,16,q}>\frac1{115}.
}
\tag{3.1}

---

## Theorem — exact `k=6` optimizer

Equations (1.2) and (3.1) yield, uniformly in every odd multiplier,

\[
\boxed{
\Gamma_{16,16,q}
>
\Gamma_{N,m,q}
\qquad
(N+m=32,\ (N,m)\ne(16,16)).
}
\]

Therefore for every jump

\[
s=64(2q+1),
\]

the unique gap-maximizing even-separation reflection-chiral two-defect geometry in the minimal primitive period `128` is the quarter-period geometry

\[
\boxed{h=32=p/4.}
\]

The certificate is a direct exact specialization of `ALL_ENERGY_SINGLE_SQUARE_IDENTITY.md`; no floating-point comparison is used as an acceptance criterion.
