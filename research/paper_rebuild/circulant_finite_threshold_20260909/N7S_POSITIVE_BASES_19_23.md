# New positive bases on the horizontal resonance `N=7s`

This note records three finite explicit signings on the third horizontal resonance.  Together with the previously proved vertical theorems, they show that the odd positive region on `N=7s` extends at least through step 23.

## Theorem 1

\[
\boxed{
 m(133,19)<\sqrt8,
 \qquad
 m(147,21)<\sqrt8,
 \qquad
 m(161,23)<\sqrt8.
}
\tag{1}
\]

Consequently

\[
\boxed{
 m(7s,s)<\sqrt8
 \quad\text{for every odd }s\in\{3,5,7,9,11,13,15,17,19,21,23\}.
}
\tag{2}
\]

The points through `s=17` were already supplied by the vertical fixed-step theorems.  The three new points are proved below by exact finite certificates.

---

## 1. Common Hamilton gauge

For each of the three pairs put `N=7s`.  Use Hamilton gauge with

\[
h_i=+1\quad(0\le i<N-1),
\qquad
h_{N-1}=-1.
\]

Begin with the alternating chord word

\[
c_i=(-1)^i.
\]

Then reverse the following four chord signs:

\[
\begin{array}{c|c}
(N,s)&\text{reversed chord indices}\\ \hline
(133,19)&110,111,116,117,\\
(147,21)&3,4,128,129,\\
(161,23)&43,44,116,117.
\end{array}
\tag{3}
\]

Let `A` denote the resulting integer signed adjacency matrix and set

\[
K=8I-A^2.
\tag{4}
\]

For each of the three matrices, exact rational `LDL^T` decomposition has only positive diagonal pivots.  Hence

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
(161,23)&24907296132626454444572251848041426045840481567809677574423420267114852501384.
\end{array}
\tag{5}
\]

All are positive; more importantly, the verifier checks every exact LDL pivot, not merely the determinant.  Thus (1) follows. `square`

The complete exact reconstruction is `verify_n7s_positive_bases_19_23.py`.  No floating-point quantity is used for acceptance.

---

## Interpretation

The third horizontal resonance does **not** inherit the cutoff of the width-five line.  In particular the first width-five negative point `s=15` has no analogue on `N=7s`: the points `s=15,17,19,21,23` are all strictly sub-threshold here.

This materially constrains any proposed two-parameter phase boundary.  The width-seven all-signing even-gap obstruction developed in the companion notes must therefore be combined with a different defect-cluster mechanism before a horizontal negative theorem can begin; the cutoff, if finite, lies beyond 23.