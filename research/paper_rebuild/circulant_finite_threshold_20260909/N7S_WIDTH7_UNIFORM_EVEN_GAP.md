# Uniform exclusion of every positive even defect gap on the width-seven line

This note upgrades `N7S_WIDTH7_EVEN_GAP_2_20_RULE.md` from a finite list to a uniform theorem.  The proof combines the two critical half-line defect classes from `N7S_WIDTH7_HALF_LINE_RIGIDITY.md` with a fixed reduced quadratic form that is unchanged when two complement columns are inserted into the middle of a long gap.

## Theorem 1

Let `M` be an open width-seven heptagon strip with

\[
\rho(M)^2<8.
\]

Suppose two defect transitions `d,e` are separated by a positive even number `g` of complement transitions and there are three complement transitions on both exterior sides.  Then no such strip exists.  Equivalently, for every even integer `g>=2`,

\[
\boxed{
127^3,d,127^g,e,127^3
}
\tag{1}
\]

has squared spectral radius at least eight for all `d,e!=127`.

### Short gaps

The cases

\[
g=2,4,6,8,10,12,14,16,18,20
\]

are exactly the finite theorem `N7S_WIDTH7_EVEN_GAP_2_20_RULE.md`.

It remains to treat even `g>=22`.

---

## 1. Critical defect reduction at both ends

Assume a word (1) with even `g>=22` were sub-threshold.  Its left end contains the proper subword

\[
127^3,d,127^{14},
\]

so the fourteen-complement half-line theorem forces, up to `D_7`,

\[
d\in\{47,63\}.
\tag{2}
\]

Applying the reversed half-line theorem at the other end gives the same conclusion for `e`.

Fix `d`.  The stabilizer of either critical mask in `D_7` has order two.  The relative positions of the right critical defect reduce to the following 16 types:

\[
\begin{array}{c|l}
d& e\\ \hline
47&47,61,87,117,63,95,119,123,\\
63&47,87,94,107,63,95,111,119.
\end{array}
\tag{3}
\]

Thus only sixteen finite boundary interactions remain.

---

## 2. Critical vectors and the fixed reduced form

Immediately after the left defect, the heptagon state is

\[
127\oplus47=80
\quad\text{or}\quad
127\oplus63=64.
\]

Put

\[
v_{47}=(-1,-1,-1,-1,-1,1,1)^T,
\qquad C(80)v_{47}=2v_{47},
\tag{4}
\]

and

\[
v_{63}=(1,-1,1,-1,1,-1,1)^T,
\qquad C(64)v_{63}=-2v_{63}.
\tag{5}
\]

In either case

\[
C^2v_d=4v_d.
\tag{6}
\]

Let

\[
Q_g=M_g^2-8I
\]

for the word (1).  Retain all seven coordinates on the first six and last six columns.  On every middle column restrict the vector to a scalar multiple of `v_d`, using one scalar `a` on one column parity and one scalar `b` on the other.  This defines an integral linear map

\[
P_g:\mathbb R^{86}\longrightarrow\mathbb R^{7(g+9)}.
\]

Set

\[
R_g=P_g^TQ_gP_g.
\tag{7}
\]

### Lemma 2.1 (two-column insertion invariance)

For every critical relative type in (3) and every even `g>=6`,

\[
\boxed{R_{g+2}=R_g.}
\tag{8}
\]

### Proof

Inside the complement run, adjacent signed-cycle blocks are negatives of one another.  Hence the nearest-column blocks of `Q_g` vanish.  The distance-two blocks are identities, while on the critical vector (6) the diagonal block acts as

\[
(C^2-6I)v_d=-2v_d.
\]

Consequently the middle restricted scalar recurrence is

\[
-2z_j+z_{j-2}+z_{j+2}.
\tag{9}
\]

The restricted vector is constant on each column parity, so (9) vanishes identically.  Inserting one column of each parity in the interior therefore adds zero quadratic energy and does not change either boundary coupling.  This proves (8). `square`

Thus all even long gaps have exactly the same 86-dimensional reduced quadratic form.

---

## 3. Exact finite witnesses for the sixteen types

It is enough to test `g=6`.  Exact integer Rayleigh witnesses for the matrices `R_6` fall into three classes:

\[
\begin{array}{c|c|c}
\text{critical types}&z^TR_6z&z^Tz\\ \hline
47\to47&10&2332,\\
47\leftrightarrow63&3&1041,\\
63\to63&24&1034.
\end{array}
\tag{10}
\]

Here each row covers all four relative orientations of the corresponding pair of critical orbits in (3).  In particular every one of the sixteen matrices has a vector with strictly positive `R_6`-quadratic form.

By (8), the same coordinate vector gives the same positive numerator for every even `g>=6`.  Therefore every critical word (1) has

\[
\rho(M_g)^2>8.
\]

This contradicts the assumed sub-threshold word for every even `g>=22`.  Combining with the finite theorem through `g=20` proves Theorem 1. `square`

The finite orbit reduction, the equality `R_6=R_8`, and every exact integer witness in (10) are reproduced by `verify_n7s_width7_uniform_even_gap.py`.

---

## Consequence

The width-seven negative-side problem now has the same parity backbone as the completed width-five theorem: in any sufficiently embedded sub-threshold cyclic strip, a positive even complement gap between consecutive defects is impossible.  The remaining obstruction problem is therefore concentrated in adjacent defects, odd gaps, and the finitely many clusters that touch the helical seam.