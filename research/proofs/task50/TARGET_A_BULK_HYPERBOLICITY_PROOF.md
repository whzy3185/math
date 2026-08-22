# Target A Bulk Hyperbolicity Proof

## Theorem

On each of the rational intervals

\[
I_6=\left[\frac{1581}{200},\frac{3953}{500}\right],
\qquad
I_{10}=\left[\frac{7977}{1000},\frac{3989}{500}\right],
\]

the target period-eight monodromy has four distinct positive real
multipliers.  Two lie inside and two outside the unit circle, paired by
reciprocity.  More precisely, the two stable multipliers satisfy

\[
0<z_{6,f}<\frac18<z_{6,s}<\frac9{25}<1
\]

on `I6`, and

\[
0<z_{10,f}<\frac18<z_{10,s}<\frac4{15}<1
\]

on `I10`.  The unstable multipliers are their reciprocals.

## Proof

The palindromic reduction gives the two branches `w_-` and `w_+` in
`BULK_PALINDROMIC_REDUCTION.md`.  On both intervals,

\[
h(y)=2y^2-16y+13
\]

is increasing and `Delta(y)` is decreasing and positive.  Consequently a
lower bound for `w_-` is obtained from `h(left)-sqrt(Delta(left))`, while a
lower bound for `w_+` is obtained from
`h(left)+sqrt(Delta(right))`.

For `I6`, exact squaring gives

\[
\left(h(1581/200)-2(9/25+25/9)\right)^2
-\Delta(1581/200)
=\frac{40913042401}{32400000000}>0,
\]

and the unsquared left side is positive.  Hence

\[
w_-(y)>\frac9{25}+\frac{25}{9}.
\]

Similarly,

\[
\Delta(3953/500)-
\left(2(1/8+8)-h(1581/200)\right)^2
=\frac{1334775679}{400000000}>0,
\]

so `w_+(y)>1/8+8`.

For `I10`, the corresponding exact margins are

\[
\frac{4400583770569}{2250000000000}>0
\quad\hbox{and}\quad
\frac{1505980642159}{250000000000}>0.
\]

They imply

\[
w_-(y)>\frac4{15}+\frac{15}{4},
\qquad
w_+(y)>\frac18+8.
\]

For `0<q<1`, the inequality `w>q+q^{-1}` is equivalent to
`0<z_s(w)<q`.  In particular both `w` branches are greater than two.
Therefore each branch gives one positive stable and one positive unstable
root, and no multiplier lies on the unit circle.  The reciprocal form of the
quartic proves the stated pairing.

Finally,

\[
\sqrt5<\frac{1129}{500},qquad
10+2\frac{1129}{500}<\left(\frac{381}{100}\right)^2,
\]

so `eta<781/100<1581/200`; both intervals lie strictly above the bulk edge.

## Certificate

Every comparison above is performed over exact integers or rationals.  The
machine-readable margins and all monotonicity checks are in
`certificates/bulk_hyperbolicity_certificates.json`.

Status: `BULK_HYPERBOLICITY_PROVED`.
