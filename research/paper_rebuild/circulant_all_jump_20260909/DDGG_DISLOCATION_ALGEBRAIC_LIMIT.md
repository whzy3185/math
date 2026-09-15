# Exact algebraic edge of the `DDGG` dislocation limit

Date: 2026-09-15

Status: **Proved**.

This note explains the stable value near `7.700740906...` seen in the infinite family

\[
G(DDGG)^rG,
\qquad r\to\infty.
\]

The limit is an algebraic dislocation bound-state edge of the uniformly hyperbolic `DDGG` bulk.

---

## 1. General-energy one-dislocation matching equation

Let `y=lambda^2` be the squared spectral parameter and

\[
d=z+z^{-1}\in[-2,2].
\]

For the four-site `DDGG` bulk define

\[
\boxed{
\mathcal A(y,d)=y^2-8y+10-d^2.
}
\tag{1.1}
\]

Whenever `mathcal A>2`, put

\[
\rho(y,d)=
\frac{\mathcal A-\sqrt{\mathcal A^2-4}}2
\in(0,1).
\tag{1.2}
\]

Thus `rho` is the stable reciprocal eigenvalue of the bulk transfer.

For the finite word `G(DDGG)^rG`, write

\[
u_r=U_{r-1}(\mathcal A/2),
\qquad
v_r=U_{r-2}(\mathcal A/2).
\]

Exact reduction of the `4 x 4` transfer determinant gives

\[
\boxed{
P_r(y,d)
=\alpha(y,d)u_r^2
+\beta(y,d)u_rv_r
+\gamma(y,d),
}
\tag{1.3}
\]

where

\[
\boxed{
\begin{aligned}
\alpha(y,d)={}&d^6-2d^5y+8d^5-d^4y^2+8d^4y-6d^4\\
&+4d^3y^3-48d^3y^2+168d^3y-160d^3\\
&-d^2y^4+16d^2y^3-92d^2y^2+224d^2y-168d^2\\
&-2dy^5+40dy^4-296dy^3+992dy^2-1476dy+788d\\
&+y^6-24y^5+226y^4-1056y^3+2544y^2-2944y+1272,
\end{aligned}}
\tag{1.4}
\]

\[
\boxed{
\beta(y,d)
=-(y-d-4)
\Bigl(
 d^3-d^2y+4d^2-dy^2+8dy-12d\\
 +y^3-12y^2+40y-32
\Bigr),
}
\tag{1.5}
\]

and

\[
\boxed{
\gamma(y,d)
=d^2-2dy+7d+y^2-8y+14.
}
\tag{1.6}
\]

Equation (1.3) specializes at `y=31/4` to the matching formula in `INFINITE_DDGG_FAMILY_P8R4_THEOREM.md`.

---

## 2. Exponential bulk limit

For `mathcal A>2`,

\[
\frac{v_r}{u_r}
=\rho\,
\frac{1-\rho^{2r-2}}
{1-\rho^{2r}},
\tag{2.1}
\]

and

\[
u_r^{-2}=O(\rho^{2r}).
\tag{2.2}
\]

Hence, locally uniformly on every compact hyperbolic set,

\[
\boxed{
\frac{P_r(y,d)}{u_r^2}
=F_\infty(y,d)+O(\rho^{2r-1}),
}
\tag{2.3}
\]

where the limiting Evans function is

\[
\boxed{
F_\infty(y,d)
=\alpha(y,d)+\beta(y,d)\rho(y,d).
}
\tag{2.4}
\]

Thus the large-period dislocation dispersion is independent of the cell length.

---

## 3. Polynomial elimination of the stable bulk root

At a limiting dislocation eigenvalue,

\[
\alpha+\beta\rho=0.
\]

Together with

\[
\rho+\rho^{-1}=\mathcal A,
\]

this gives the exact algebraic curve

\[
\boxed{
E(y,d):=\alpha^2+\beta^2+\mathcal A\alpha\beta=0.
}
\tag{3.1}
\]

After expansion,

\[
\boxed{
\begin{aligned}
E(y,d)={}&d^8+4d^7-4d^6y^2+24d^6y-32d^6\\
&-4d^5y^2+48d^5y-88d^5\\
&+6d^4y^4-80d^4y^3+360d^4y^2-672d^4y+448d^4\\
&-4d^3y^4+32d^3y^3+16d^3y^2-448d^3y+608d^3\\
&-4d^2y^6+88d^2y^5-752d^2y^4+3168d^2y^3\\
&\qquad-6880d^2y^2+7168d^2y-2736d^2\\
&+4dy^6-80dy^5+584dy^4-1856dy^3+2240dy^2-1088d\\
&+y^8-32y^7+424y^6-3008y^5+12336y^4\\
&\qquad-29440y^3+39040y^2-25600y+6208.
\end{aligned}}
\tag{3.2}
\]

The equation `E=0` contains both stable and unstable reciprocal choices.  The physical branch is selected by

\[
\boxed{
0<-\alpha/\beta<1,
}
\tag{3.3}
\]

which forces `-alpha/beta=rho`.

---

## 4. Exact top stationary value

An interior extremum of a regular branch `E(y,d)=0` satisfies

\[
E=0,
\qquad
\partial_dE=0.
\]

The exact resultant factors as

\[
\begin{aligned}
\operatorname{Res}_d(E,E_d)
={}&2^{40}(y-5)^2(y-2)^2\\
&\times
\bigl(y^6-21y^5+173y^4-715y^3+1550y^2-1628y+608\bigr)^2\\
&\times\boxed{P_{18}(y)},
\end{aligned}
\tag{4.1}
\]

where

\[
\boxed{
\begin{aligned}
P_{18}(y)={}&4096y^{18}-253952y^{17}+7202816y^{16}-123850752y^{15}\\
&+1442367744y^{14}-12039139456y^{13}+74327494784y^{12}\\
&-345302878816y^{11}+1216045619104y^{10}-3244450364032y^9\\
&+6503830300217y^8-9629549440496y^7+10232289676866y^6\\
&-7451061319416y^5+3448205009681y^4-892757273520y^3\\
&+108340611788y^2-10175921504y+1098075296.
\end{aligned}}
\tag{4.2}
\]

Exact Sturm counts give

\[
\#\{y\in(77/10,31/4):P_{18}(y)=0\}=1,
\tag{4.3}
\]

whereas the displayed sextic in (4.1) has no root in that interval.

Let this unique root be

\[
\boxed{R_\infty.}
\]

It is isolated by

\[
\boxed{
7.7007<R_\infty<7.7008,
}
\tag{4.4}
\]

and numerically

\[
R_\infty
=7.700740906353718237408340378670746\ldots.
\tag{4.5}
\]

The corresponding common solution of `E=E_d=0` on the physical stable branch has

\[
\boxed{
1.992<d_\infty<1.993,
}
\tag{4.6}
\]

and more precisely

\[
d_\infty
=1.99290373256884878015491534997\ldots.
\]

Exact interval evaluation gives `0<-alpha/beta<1` in a rational isolating box around this pair, so it is the stable rather than the reciprocal unstable solution.

---

## 5. Why this stationary point is the global top of the physical dislocation branch

Consider the compact top window

\[
\mathcal K=[77/10,31/4]\times[-2,2].
\]

First, the separator proof in `INFINITE_DDGG_FAMILY_P8R4_THEOREM.md` passes to the limit and gives

\[
F_\infty(31/4,d)>0
\qquad(-2\le d\le2).
\tag{5.1}
\]

Second, at the phase boundaries the elimination polynomial factors as

\[
E(y,-2)
=(y-2)^2(y^2-8y+4)
(y^4-20y^3+120y^2-208y+16),
\tag{5.2}
\]

and

\[
E(y,2)
=(y^4-16y^3+80y^2-128y+32)^2.
\tag{5.3}
\]

Exact Sturm counts show that neither boundary polynomial has a root for

\[
77/10\le y\le31/4.
\tag{5.4}
\]

Therefore any physical zero of `F_infty` in `mathcal K` whose `y`-coordinate is maximal is an interior stationary point.  By the resultant factorization (4.1)--(4.3), the only possible stationary `y` in this top window is `R_infty`.  The stable solution in the isolating box proves that this value is attained.  Hence

\[
\boxed{
\max\{y:(y,d)\in\mathcal K,\ F_\infty(y,d)=0\}
=R_\infty.
}
\tag{5.5}
\]

---

## 6. Convergence of the finite-cell edges

The hyperbolicity margin is uniform on a neighborhood of the compact physical top branch.  Equation (2.3) therefore holds with all first derivatives.  The root at `(R_infty,d_infty)` is nondegenerate, so the implicit-function theorem produces a nearby finite-`r` branch and gives the lower bound

\[
\liminf_{r\to\infty}R_r\ge R_\infty.
\]

Conversely, `INFINITE_DDGG_FAMILY_P8R4_THEOREM.md` gives `R_r<31/4`.  Any maximizing sequence with limit at least `77/10` has a convergent subsequence `(y_r,d_r)->(y_*,d_*)` in `mathcal K`; after division by `u_r^2`, (2.3) forces

\[
F_\infty(y_*,d_*)=0.
\]

By (5.5), `y_*<=R_infty`.  If a subsequence stays below `77/10`, the same upper bound is automatic.  Thus

\[
\boxed{
R_r\longrightarrow R_\infty.
}
\tag{6.1}
\]

In fact the Chebyshev ratio formula (2.1) and nondegeneracy give exponential convergence:

\[
\boxed{
R_r-R_\infty=O(\rho_*^{\,2r}),
}
\tag{6.2}
\]

for some absolute `0<rho_*<1` determined by the uniform bulk hyperbolicity near the maximizing branch.

Likewise every maximizing compressed phase satisfies

\[
d_r\to d_\infty.
\]

---

## 7. Interpretation

The stable number `7.700740906...` appearing from periods `20` onward is not a finite-period accident.  It is the exact top bound state of a single `GGGG` dislocation in an infinite uniformly hyperbolic `DDGG` bulk.

The polynomial `P_18` is therefore a new spectral constant of the periodic-flux problem.  The defect staircase should be viewed as finite-ring realizations of this bulk-dislocation spectral geometry, rather than as unrelated collections of positive flux sites.
