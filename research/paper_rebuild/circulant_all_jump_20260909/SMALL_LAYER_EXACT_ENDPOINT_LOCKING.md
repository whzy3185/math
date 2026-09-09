# Exact endpoint locking for the four small compressed layers

Date: 2026-09-09

Status: **Proved** with exact rational Bernstein certificates. This note belongs only to Paper I.

The multiplier-uniform endpoint theorem proves exact phase locking for all sufficiently large `L`. The present result closes the four smallest nontrivial half-periods after the exceptional layer `L=4`.

## Theorem A

For

\[
\boxed{L\in\{6,8,10,12\}}
\]

and every integer `q>=0`, the period-`2L` separation-two compressed phase with jump

\[
s=L(2q+1)
\]

has unique global maximizing Bloch phase

\[
\boxed{z=1.}
\]

Equivalently,

\[
\boxed{
R_{L,q}=\rho(H_{L,q}(1))^2
}
\tag{1}
\]

for all four layers and every odd multiplier.

---

## 1. Endpoint polynomials

Write

\[
L=2r,
\qquad r\in\{3,4,5,6\}.
\]

The endpoint top squared eigenvalue `y_r` is the unique upper root of

\[
p_r(y)=0,
\]

where

\[
p_r(y)
=U_{r-2}\!\left(\frac{y-6}{2}\right)(y^2-8y+6)
-U_{r-3}\!\left(\frac{y-6}{2}\right)(y-2)-2.
\tag{2}
\]

For the four values of `r`, these are

\[
\begin{aligned}
p_3(y)&=y^3-14y^2+53y-36,\\
p_4(y)&=y^4-20y^3+136y^2-344y+196,\\
p_5(y)&=y^5-26y^4+255y^3-1146y^2+2209y-1156,\\
p_6(y)&=y^6-32y^5+410y^4-2656y^3+8949y^2-14064y+6724.
\end{aligned}
\tag{3}
\]

The endpoint monotonicity theorem gives uniqueness of the relevant top root. Exact sign evaluations isolate it in the following rational intervals, each of width `10^-6`:

\[
\begin{array}{c|c|c}
r&L&\text{isolating interval for }y_r\\ \hline
3&6&[1557743/200000,\ 1947179/250000]\\
4&8&[7887839/10^6,\ 49299/6250]\\
5&10&[3965319/500000,\ 7930639/10^6]\\
6&12&[3976457/500000,\ 1590583/200000].
\end{array}
\tag{4}
\]

In each row, exact integer/rational arithmetic gives

\[
p_r(a_r)<0<p_r(b_r),
\]

so `y_r in (a_r,b_r)`.

---

## 2. Relaxed phase comparison

Write the exact characteristic equation as

\[
P(y;d,e)=G_r(y,d)-e.
\]

Put

\[
d=2-\mu,
\qquad 0\le\mu\le4.
\]

For every `y`, define

\[
D_r(y,\mu)
:=G_r(y,2-\mu)-G_r(y,2).
\]

Since `D_r(y,0)=0` identically, it factors as

\[
\boxed{
D_r(y,\mu)=\mu Q_r(y,\mu)
}
\tag{5}
\]

with an explicit polynomial `Q_r` having rational coefficients.

At the endpoint root,

\[
G_r(y_r,2)=2,
\]

so

\[
G_r(y_r,2-\mu)-2
=\mu Q_r(y_r,\mu).
\tag{6}
\]

Thus the problem is reduced to proving

\[
Q_r(y_r,\mu)>0
\qquad(0\le\mu\le4).
\tag{7}
\]

---

## 3. Exact bivariate Bernstein certificate

For each `r`, map the rectangle

\[
[y,\mu]\in[a_r,b_r]\times[0,4]
\]

affinely to `[0,1]^2`, and write `Q_r` in the tensor-product Bernstein basis.

All Bernstein coefficients are exact rational numbers. The exact verifier

`verify_small_layer_endpoint_locking.py`

reconstructs them from the defining Chebyshev formula without floating-point acceptance tests.

The minimum Bernstein coefficient in each layer satisfies the simple certified lower bound

\[
\begin{array}{c|c|c}
r&L&\min\text{ Bernstein coefficient}\\ \hline
3&6&>46\\
4&8&>98\\
5&10&>168\\
6&12&>257.
\end{array}
\tag{8}
\]

Since every Bernstein basis function is nonnegative and the basis functions sum to one on the unit square, (8) gives

\[
\boxed{
Q_r(y,\mu)>0
}
\tag{9}
\]

throughout the whole rational rectangle. In particular it holds at the exact algebraic endpoint root `y=y_r`.

Therefore, for every `mu>0`,

\[
\boxed{
G_r(y_r,2-\mu)>2.
}
\tag{10}
\]

---

## 4. Return to physical Bloch phases

For a physical phase,

\[
e=z+z^{-1}\le2.
\]

If `d<2`, equation (10) gives

\[
P(y_r;d,e)
=G_r(y_r,d)-e
>2-e
\ge0.
\tag{11}
\]

If `d=2` but `z\ne1`, then

\[
P(y_r;2,e)=2-e>0.
\tag{12}
\]

Thus the endpoint energy `y_r` is a Bloch root only at `z=1`.

The endpoint top root is simple. Near `z=1`, continuity keeps the second squared root below `y_r`, and (11)--(12) force the top root below `y_r`. On the punctured Bloch circle, the number of roots in `(y_r,8)` cannot change because a crossing of `y_r` is excluded by (11)--(12), while a crossing of `8` is excluded by the general compression theorem. Since the punctured circle is connected, there are no roots above `y_r` at any nontrivial phase.

Hence `z=1` uniquely maximizes the squared Bloch edge, proving Theorem A.

---

## 5. Consequence for the finite-threshold conjecture

The only exceptional compressed layer now known is

\[
L=4,
\]

where genuine non-endpoint maximizers occur.

The exact theorem now covers

\[
L=6,8,10,12
\]

and the multiplier-uniform eventual theorem covers every sufficiently large `L`.

Therefore any remaining obstruction to the sharp statement

\[
L\ge6\Longrightarrow z=1\text{ uniquely maximizes}
\]

is confined to a finite intermediate set of even half-periods. The next task is to make the large-`L` threshold effective and close that finite gap.