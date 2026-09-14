# Positive bases on the horizontal resonance `N=7s` through step 29

This note records six finite explicit signings on the third horizontal resonance. Together with the previously proved vertical theorems, they show that the odd positive region on `N=7s` extends continuously through step 29.

## Theorem 1

\[
\boxed{
 m(7s,s)<\sqrt8
 \quad\text{for every odd }s\in\{3,5,7,9,11,13,15,17,19,21,23,25,27,29\}.
}
\tag{1}
\]

The points through `s=17` were already supplied by the vertical fixed-step theorems. The six new points `s=19,21,23,25,27,29` are proved here by exact finite certificates.

---

## 1. Common Hamilton gauge

For each pair put `N=7s`. Use Hamilton gauge with

\[
h_i=+1\quad(0\le i<N-1),
\qquad
h_{N-1}=-1.
\]

Begin with the alternating chord word

\[
c_i=(-1)^i.
\]

For `s=19,21,23` use the following four chord reversals:

\[
\begin{array}{c|c}
(N,s)&\text{reversed chord indices}\\ \hline
(133,19)&110,111,116,117,\\
(147,21)&3,4,128,129,\\
(161,23)&43,44,116,117.
\end{array}
\tag{2}
\]

For every odd `s\in\{25,27,29\}` a uniform four-flip pattern works:

\[
\boxed{
2s-3,\quad 2s-2,\quad 3s+1,\quad 3s+2.
}
\tag{3}
\]

In fact the same pattern is numerically sub-threshold for every tested odd `s>=19`; only the exact bases stated here are promoted to theorem status.

Let `A` denote the resulting signed adjacency matrix and set

\[
K=8I-A^2.
\tag{4}
\]

For each of the six matrices, exact rational `LDL^T` decomposition has only positive diagonal pivots. Hence

\[
K\succ0,
\]

so every eigenvalue of `A^2` is strictly smaller than eight and therefore `rho(A)<sqrt(8)`.

The exact determinants are

\[
\begin{array}{c|r}
(N,s)&\det(8I-A^2)\\ \hline
(133,19)&6881113906591271314868115580534177008571456256473620931470387912,\\
(147,21)&2052458732243546448194681401672407273703693170869317348327038263943800,\\
(161,23)&24907296132626454444572251848041426045840481567809677574423420267114852501384,\\
(175,25)&1758165770944445569752092124506721227335573274962881828944710512735671046378917175416,\\
(189,27)&15677991793916311788147429358354018134700963356176700551533154605289188209355018145946009600,\\
(203,29)&139031874687624227325008974504113378822083728002061895279031442154489015618584145360970870352248832.
\end{array}
\tag{5}
\]

All determinants are positive; more importantly, the verifier checks every exact LDL pivot, not merely the determinant. This proves (1). `square`

The complete exact reconstruction is `verify_n7s_positive_bases_19_23.py`. No floating-point quantity is used for acceptance.

---

## 2. The emerging uniform four-flip pattern

For the uniform pattern (3), reordering `C_(7s)(1,s)` into its `s` chord-heptagon columns gives a particularly simple transition word away from the helical seam. The only non-complement transitions occur at

\[
0,\quad 2,\quad s-4,\quad s-2,
\]

with masks

\[
119,\quad119,\quad125,\quad125,
\]

respectively; every transition between the two end clusters is complement. Thus increasing `s` by two inserts exactly two complement columns in the long middle segment while leaving both finite boundary clusters unchanged.

This is the correct structure for the next analytic target: prove a two-column insertion/transfer theorem for the positive form `8I-A^2`. Such a theorem would promote the observed four-flip family from finitely many exact bases to all odd `s` and would complete the entire horizontal line `N=7s` on the positive side.

---

## Interpretation

The third horizontal resonance does **not** inherit the cutoff of the width-five line. In particular the first width-five negative point `s=15` has no analogue on `N=7s`: every odd step through 29 is strictly sub-threshold here.

Any genuine two-parameter phase boundary must therefore depend nontrivially on both the chord-cycle length and the step. The all-signing width-seven even-gap obstruction remains valuable for the negative side, but the present finite construction shows that its surviving defect clusters can support sub-threshold signings over a substantially larger range than on `N=5s`.