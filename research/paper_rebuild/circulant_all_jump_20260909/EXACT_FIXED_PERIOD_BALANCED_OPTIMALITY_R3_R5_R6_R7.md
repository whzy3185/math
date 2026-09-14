# Exact balanced-separation optimality in the residual periods `r=3,5,6,7`

Date: 2026-09-14

Status: **Proved with exact rational Bernstein and derivative certificates**.

Together with the previously certified layers `r=2,4,8` and the analytic tail theorem for `r>=9`, this note closes all finite periods needed for the all-period balanced-geometry theorem.

## 1. Fixed-period setup

Fix

\[
N+m=2r,
\qquad
p=8r.
\]

The balanced geometry is

\[
N=m=r.
\]

For every unbalanced geometry,

\[
M:=\max\{N,m\}\ge r+1,
\]

and `UNIVERSAL_ENDPOINT_DIRICHLET_UPPER_BOUND.md` gives

\[
\Gamma_{N,m,q}<D_{r+1},
\qquad
D_j=2-2\cos\frac\pi{2j}.
\tag{1.1}
\]

We treat the four remaining values

\[
\boxed{r\in\{3,5,6,7\}}
\]

using the rational separators

\[
\begin{array}{c|c|c}
r&g_r&y_r=8-g_r\\ \hline
3&4/25&196/25\\
5&7/100&793/100\\
6&13/250&1987/250\\
7&1/25&199/25.
\end{array}
\tag{1.2}
\]

The elementary inequality

\[
D_j<\frac{\pi^2}{4j^2}<\frac{10}{4j^2}
\]

shows respectively

\[
D_4<\frac5{32}<\frac4{25},
\]

\[
D_6<\frac5{72}<\frac7{100},
\]

\[
D_7<\frac5{98}<\frac{13}{250},
\]

and

\[
D_8<\frac5{128}<\frac1{25}.
\tag{1.3}
\]

Hence every unbalanced competitor has gap strictly below the corresponding separator `g_r`.

It remains to prove

\[
\Gamma_{r,r,q}>g_r
\]

for each row.

---

## 2. Exact relaxed determinant certificates

For each `r`, use `ALL_ENERGY_SINGLE_SQUARE_IDENTITY.md` at the rational energy

\[
y=8-g_r.
\]

Set

\[
d=4t-2,
\qquad0\le t\le1.
\]

The relaxed balanced determinant

\[
P_{r,r}(8-g_r;4t-2,2)
\]

is a polynomial of degree `4r` in `t`.  Its Bernstein coefficients are exact rational numbers.

For all four values of `r`, **every Bernstein coefficient is strictly positive**.  The exact minimum coefficients are

\[
\begin{array}{c|c|c}
r&\deg&\min b_j\\ \hline
3&12&\displaystyle
\frac{7582743478769182416}{59604644775390625}\\[3mm]
5&20&\displaystyle
\frac{1325367230213242204023775402569185401608748001}
{10^{40}}\\[3mm]
6&24&\displaystyle
\frac{7309334570802773710548581925434793442618329381297257415546467361}
{3552713678800500929355621337890625\,10^{21}}\\[3mm]
7&28&\displaystyle
\frac{48464870332283091554725546075272754883417844701}
{1387778780781445675529539585113525390625}.
\end{array}
\tag{2.1}
\]

In particular the minima are approximately

\[
127.2,\quad1.325\times10^5,\quad2.057\times10^6,\quad3.492\times10^7,
\]

respectively.

Because Bernstein basis functions are nonnegative and sum to one,

\[
\boxed{
P_{r,r}(8-g_r;d,2)>0
\qquad(-2\le d\le2)
}
\tag{2.2}
\]

for each of the four residual periods.

For a physical Bloch phase `e=z+z^{-1}<=2`, the seam enters linearly, so

\[
P_{r,r,q,z}(8-g_r)
=P_{r,r}(8-g_r;d,2)+(2-e)>0.
\tag{2.3}
\]

---

## 3. Exact reference-fiber inertia

At `z=1`, the balanced squared characteristic polynomial factors into two monic degree-`2r` integer polynomials.

For each separator in (1.2), and for **each** of the two factors:

- the factor value at `y=8-g_r` is strictly positive;
- every derivative through order `2r` is strictly positive there.

The exact zeroth values of the two factors are:

\[
\begin{array}{c|c|c}
r&f_-(8-g_r)&f_+(8-g_r)\\ \hline
3&\displaystyle\frac{3151582196}{244140625}
&\displaystyle\frac{4128144696}{244140625}\\[3mm]
5&\displaystyle\frac{36236216095394246907249}{10^{20}}
&\displaystyle\frac{36636216095394246907249}{10^{20}}\\[3mm]
6&\displaystyle
\frac{85381742628891821475769205678481}{59604644775390625\,10^{12}}
&\displaystyle
\frac{85620161207993383975769205678481}{59604644775390625\,10^{12}}\\[3mm]
7&\displaystyle
\frac{220074127714545919036101}{37252902984619140625}
&\displaystyle
\frac{220223139326484395598601}{37252902984619140625}.
\end{array}
\tag{3.1}
\]

Since the top derivatives are positive constants, descending induction implies that both factors remain positive for every

\[
y\ge8-g_r.
\]

Thus the reference fiber has no squared eigenvalue at or above the separator energy.

Together with (2.3), inertia is constant around the Bloch circle, and hence

\[
\boxed{
R_{r,r,q}<8-g_r,
\qquad
\Gamma_{r,r,q}>g_r.
}
\tag{3.2}

---

## Theorem — exact residual-period optimizers

For every

\[
r\in\{3,5,6,7\}
\]

and every odd multiplier,

\[
\boxed{
\Gamma_{r,r,q}>\Gamma_{N,m,q}
\qquad
(N+m=2r,\ (N,m)\ne(r,r)).
}
\tag{4.1}
\]

Thus balanced separation is the unique full-gap optimizer in each of the primitive periods

\[
p=24,40,48,56.
\]

The accompanying verifier reconstructs every certificate from the exact all-energy single-square identity using rational arithmetic only.

## 5. Consequence

The finite balanced-optimality problem is now closed for every integer

\[
2\le r\le8:
\]

- `r=2`: `EXACT_MINIMAL_PERIOD_OPTIMALITY_K3.md`;
- `r=3,5,6,7`: this note;
- `r=4`: `EXACT_MINIMAL_PERIOD_OPTIMALITY_K4.md`;
- `r=8`: `EXACT_MINIMAL_PERIOD_OPTIMALITY_K5.md`.

Once the analytic tail is sharpened to `r>=9`, these certificates combine into an exact all-period theorem, not merely an all-`2`-adic-layer theorem.
