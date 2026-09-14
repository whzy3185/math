# Exact odd-total geometry orientation for `r=6,7,8`

Date: 2026-09-14

Status: **Proved with exact rational certificates**.

This note proves that the finite orientation switch has already occurred by `r=6`.

## 1. Setup

Fix

\[
N+m=2r+1,
\qquad r\in\{6,7,8\}.
\]

The two nearest-balanced orientations are

\[
A_r=(r+1,r)
\]

and

\[
B_r=(r,r+1).
\]

We prove that, uniformly in the odd multiplier,

\[
\boxed{
\Gamma_{r,r+1,q}
>
\Gamma_{N,m,q}
}
\tag{1.1}

for every other pair `N+m=2r+1`.

Use the rational separators

\[
\begin{array}{c|c|c}
r&g_r&y_r=8-g_r\\ \hline
6&2067/50000&397933/50000\\
7&3243/100000&796757/100000\\
8&2611/100000&797389/100000.
\end{array}
\tag{1.2}
\]

Every non-nearest geometry has

\[
M=\max\{N,m\}\ge r+2.
\]

Since

\[
D_M<\frac{10}{4M^2},
\]

one checks

\[
D_{r+2}<g_r
\]

in each row. Thus only `A_r` and `B_r` need direct comparison.

---

## 2. The compressed-antiperiodic orientation lies above the separator

For

\[
B_r=(r,r+1),
\]

use the all-energy single-square identity at `y=y_r` and relax the physical seam to its maximal value `e=2`.

Under

\[
d=4t-2,
\qquad0\le t\le1,
\]

the resulting polynomial has degree

\[
4r+2
\]

and its full Bernstein expansion has strictly positive exact rational coefficients.

The exact minimum coefficients are positive and have approximate sizes

\[
\begin{array}{c|c|c}
r&\deg&\min b_j\\ \hline
6&26&1.619\times10^3\\
7&30&2.716\times10^4\\
8&34&6.321\times10^5.
\end{array}
\tag{2.1}
\]

For example, at `r=6` the exact minimum is

\[
\frac{
241327995741594828928389647154230032062709781415480880095482307287282972962524219620878871989342147303840083187632846666498569
}{
1490116119384765625\,10^{104}
}>0.
\tag{2.2}
\]

Hence

\[
P_{r,r+1}(y_r;d,2)>0
\qquad(-2\le d\le2).
\tag{2.3}
\]

For every physical phase `e<=2`,

\[
P(y_r;d,e)>0.
\]

At the reference fiber `z=-1`, the squared characteristic polynomial factors into two monic degree `2r+1` factors. For each of the three rows, each factor and all derivatives through order `2r+1` are strictly positive at `y_r`. Therefore the reference fiber has no squared root at or above `y_r`, and inertia continuity gives

\[
\boxed{
R_{r,r+1,q}<y_r,
\qquad
\Gamma_{r,r+1,q}>g_r.
}
\tag{2.4}

uniformly in the odd multiplier.

---

## 3. A uniform physical phase witness against the opposite orientation

For

\[
A_r=(r+1,r),
\]

choose the following rational compressed coordinates:

\[
\begin{array}{c|c}
r&d_r\\ \hline
6&2-1/7200\\
7&2-1/11000\\
8&2-1/17250.
\end{array}
\tag{3.1}

Let

\[
d_r=2\cos\psi_r,
\qquad0<\psi_r<\pi/2.
\]

For an arbitrary odd multiplier

\[
n=2q+1,
\]

choose the physical phase

\[
z=e^{i\psi_r/n}.
\]

Then the compressed coordinate is exactly `d_r`, while

\[
e=z+z^{-1}=2\cos(\psi_r/n)
\ge2\cos\psi_r=d_r.
\tag{3.2}
\]

At the separator energy `y_r`, exact rational substitution into the all-energy characteristic identity gives

\[
\boxed{
P_{r+1,r}(y_r;d_r,e=d_r)<0
}
\tag{3.3}

for each `r=6,7,8`.

The exact negative values have large integer numerators; for orientation, their numerical sizes are approximately

\[
-6.334\times10^3,
\qquad
-1.756\times10^5,
\qquad
-3.706\times10^6.
\]

Because `P=\mathcal G-e` is decreasing in `e`, equation (3.2) implies for the actual physical phase

\[
P_{r+1,r,q,z}(y_r)
\le P_{r+1,r}(y_r;d_r,d_r)<0.
\tag{3.4}
\]

The exact phase diagram shows that `A_r` is sub-eight. Since its squared characteristic polynomial is monic and positive above its top root, (3.4) forces a squared eigenvalue in `(y_r,8)`. Thus

\[
\boxed{
\Gamma_{r+1,r,q}<g_r.
}
\tag{3.5}

This physical witness is uniform in the odd multiplier.

---

## Theorem — exact post-switch orientation for `r=6,7,8`

Combining (2.4), (3.5), and the distant-geometry Dirichlet bound gives

\[
\boxed{
(N,m)=(r,r+1)
}
\]

as the unique full-Bloch gap-maximizing geometry for

\[
r=6,7,8.
\]

Thus the periods

\[
p=52,60,68
\]

are already on the compressed-antiperiodic side of the orientation transition.

Together with `EXACT_ODD_TOTAL_ORIENTATION_R1_R5.md`, the finite data prove an exact switch between

\[
\boxed{r=5\quad\text{and}\quad r=6.}
\]

The remaining task for a complete all-period theorem is to make the eventual analytic orientation theorem effective from `r>=9` (or another explicit tail threshold).