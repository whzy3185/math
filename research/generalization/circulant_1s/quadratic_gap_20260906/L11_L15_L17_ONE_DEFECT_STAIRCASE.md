# Exact one-defect staircase at `L=11,15,17,19`

Date: 2026-09-07.

This note extends the exact canonical one-defect resonance theory beyond
`L=3,5,7,9,13`.  It uses the exact `4L` endpoint reduction from
`ONE_DEFECT_ENDPOINT_REDUCTION.md` on the positive side and fixed seam
windows on the negative tail.

Throughout

\[
 N=Ls,\qquad L,s\text{ odd},
\]

and in Hamilton gauge

\[
 \tau_i=\varepsilon(-1)^i,
 \qquad (\varepsilon,\alpha)\in\{\pm1\}^2.
\]

The favorable sector is `epsilon=-1, alpha=+1`.

## Theorem 11S

For `L=11`, the favorable sector satisfies

\[
 \boxed{\rho(A)^2<8\qquad 3\le s\le21,\ s\text{ odd}.}
\]

At `s=23`, the exact `44 x 44` endpoint matrix has one negative LDL pivot in
**each** of the four one-defect sectors.  Hence every one-defect sector has
`rho(A)^2>8` at `s=23`.

For every odd `s>=25`, the 24-column seam window consisting of 12 columns on
each side of the helical seam is independent of `s`.  In every sector an
integer witness satisfies

\[
 w^T(B^2-8I)w=12334,
 \qquad
 w^Tw=2361940.
\]

Since

\[
 192\cdot12334\ge2361940,
\]

we obtain the uniform tail bound

\[
 \boxed{\rho(A)^2\ge8+\frac1{192}\qquad(s\ge25\text{ odd}).}
\]

Thus the canonical one-defect transition for `L=11` occurs between `s=21`
and `s=23`.

## Theorem 15S

For `L=15`, the favorable sector satisfies

\[
 \boxed{\rho(A)^2<8\qquad 3\le s\le31,\ s\text{ odd}.}
\]

For every odd `s>=33`, take the fixed 32-column seam window with `16` columns
on each side.  In all four one-defect sectors an exact integer witness gives

\[
 w^T(B^2-8I)w=1510,
 \qquad
 w^Tw=1048602.
\]

Since

\[
 695\cdot1510\ge1048602,
\]

\[
 \boxed{\rho(A)^2\ge8+\frac1{695}\qquad(s\ge33\text{ odd}).}
\]

Hence the transition lies exactly between `s=31` and `s=33`.

## Theorem 17S

For `L=17`, the favorable sector satisfies

\[
 \boxed{\rho(A)^2<8\qquad 3\le s\le35,\ s\text{ odd}.}
\]

At `s=37`, all four endpoint matrices have exactly one negative LDL pivot.
Moreover the fixed 36-column seam window (18 columns on each side) gives in
every sector

\[
 w^T(B^2-8I)w=766,
 \qquad
 w^Tw=1047612.
\]

As

\[
 1368\cdot766\ge1047612,
\]

we have the uniform tail estimate

\[
 \boxed{\rho(A)^2\ge8+\frac1{1368}\qquad(s\ge37\text{ odd}).}
\]

Thus the transition lies exactly between `s=35` and `s=37`.

## Theorem 19S

For `L=19`, the favorable sector satisfies

\[
 \boxed{\rho(A)^2<8\qquad 3\le s\le39,\ s\text{ odd}.}
\]

At `s=41`, all four endpoint matrices have exactly one negative LDL pivot.
The fixed 40-column seam window (20 columns on each side) is independent of
odd `s>=41` and yields in every sector

\[
 w^T(B^2-8I)w=2034,
 \qquad
 w^Tw=4193544.
\]

Since

\[
 2062\cdot2034\ge4193544,
\]

\[
 \boxed{\rho(A)^2\ge8+\frac1{2062}\qquad(s\ge41\text{ odd}).}
\]

Hence the transition lies exactly between `s=39` and `s=41`.

## Exact certification

The companion verifier

`verify_l11_l15_l17_one_defect_staircase.py`

performs:

1. exact rational LDL on the full short `s=3` matrices;
2. exact rational LDL on the `4L` endpoint Schur matrices for every favorable
   odd `s` up to the stated last positive value;
3. exact inertia checks at the first negative endpoint where used;
4. exact integer quadratic-form checks for all fixed seam witnesses.

Floating eigensolvers are used only to *propose* the integer seam vectors.
The theorem checks are integer/rational.

## Corrected staircase

Combining this note with the previously proved rows gives

\[
\begin{array}{c|c|c}
L & \text{last favorable odd }s & \text{first all-sector failure }s\\ \hline
3&5&7\\
5&9&11\\
7&13&15\\
9&17&19\\
11&21&23\\
13&27&29\\
15&31&33\\
17&35&37\\
19&39&41.
\end{array}
\]

The jump at `L=13` disproves the old exact law `s_c=2L`; the later rows show
that the correction is a genuine staircase rather than a single exceptional
case.

These are theorems only for the canonical one-defect family.  For `L>=5`,
all-signing repair beyond the one-defect threshold remains open.