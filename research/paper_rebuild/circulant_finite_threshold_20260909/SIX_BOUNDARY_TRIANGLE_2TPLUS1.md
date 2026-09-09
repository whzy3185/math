# Complete analysis of the triangle locus `q=2t+1`

This note closes the second triangle locus from
`SIX_BOUNDARY_ARITHMETIC_LOCALIZATION.md`.

As before,

\[
q=\frac N{\gcd(N,2)},
\qquad
 t=\min\{s,q-s\}.
\]

## Theorem 1

Assume the generic parity reduction and

\[
q=2t+1.
\tag{1}
\]

Then no new equality at six occurs.  More precisely,

\[
\boxed{m(N,s)^2\le6}
\]

on this locus if and only if

\[
\boxed{
(N,s)\in\{(5,2),(10,3),(14,3),(14,4)\}.
}
\tag{2}
\]

All four values are **strictly** below six:

\[
m(5,2)^2=m(10,3)^2=5,
\]

and

\[
m(14,3)^2=m(14,4)^2=4+\beta<6,
\]

where `beta` is the largest root of `x^3-7x+7`.

Consequently

\[
\boxed{
q=2t+1\quad\Longrightarrow\quad m(N,s)^2\ne6.
}
\tag{3}

### Proof

The reduced parity graph is

\[
C_q(1,t).
\]

Multiplication by `2` on `Z_q` sends

\[
\{\pm1,\pm t\}
\longmapsto
\{\pm2,\pm(2t)\}
=
\{\pm2,\pm1\},
\]

because `2t=-1 mod q`.  Hence

\[
\boxed{C_q(1,t)\cong C_q(1,2).}
\tag{4}
\]

The component theorem in `SIX_BOUNDARY_TRIANGLE_T2.md` now applies.  For `q>=7`, a signing of this reduced graph can have largest eigenvalue at most `2` only for

\[
q\in\{7,8,9,10,12\}.
\]

But (1) makes `q` odd.  Including the separately treated `q=5` complete graph, the only possible reduced orders are therefore

\[
\boxed{q=5,7,9.}
\tag{5}

We inspect these three orders.

---

## 1. Odd original order

If `N` is odd, then `N=q` and `s=t`, so the original graph itself satisfies

\[
C_q(1,t)\cong C_q(1,2).
\]

The complete `t=2` analysis gives

\[
m(q,2)>\sqrt6
\qquad(q=7,9),
\]

while `(q,t)=(5,2)` has `m^2=5`.  Thus the odd-order part contributes only `(5,2)` to (2).

---

## 2. Even original order

Now `N=2q`.  Since `q=2t+1`, the two original steps representing the same reduced value `t` are

\[
s=t\qquad\text{or}\qquad s=t+1.
\tag{6}

### `q=5`

These are `(10,2)` and `(10,3)`.  The exact low-end classification gives

\[
m(10,3)^2=5,
\qquad
m(10,2)^2>6.
\]

### `q=7`

These are `(14,3)` and `(14,4)`.  The exact order-14 theorem gives

\[
m(14,3)^2=m(14,4)^2=4+\beta<6.
\]

### `q=9`

The only remaining candidates are

\[
(18,4),\qquad(18,5).
\tag{7}

We show that neither admits a signing with squared radius at most six.

Suppose otherwise.  The parity graph consists of two copies of

\[
C_9(1,4)\cong C_9(1,2).
\]

This graph has no twins.  Hence the root-quotient lemma rules out defect entries of absolute value `2`, and the two parity components are honest signed adjacency matrices with largest eigenvalue at most `2`.

By the `q=9` row of the component theorem, there is exactly one possible switching class.  In the `C_9(1,2)` realization its step-one Hamilton holonomy is `-1`.  Under the multiplier isomorphism (4), step one corresponds to step four in `C_9(1,4)`.  Therefore every admissible defect component must satisfy

\[
\boxed{\text{step-4 cycle holonomy}=-1.}
\tag{8}

We derive the opposite sign from liftability.

Let `h_i` be the original step-one signs, `c_i` the step-`s` signs, and

\[
\alpha=\prod_{i=0}^{17}h_i.
\]

Both mixed displacements are outside the parity support for the pairs (7).  Hence

\[
c_{i+1}=-h_i h_{i+s}c_i.
\tag{9}

Also, every triangle of the admissible defect component is negative.  The product of its nine triangle fluxes equals the product of its step-one defect edges, because every step-four edge occurs twice.  Thus

\[
-1=\prod_{j=0}^8(h_{2j}h_{2j+1})=\alpha.
\tag{10}

So `alpha=-1`.

#### The pair `(18,4)`

The step-four defect edges arise from two original step-four chord edges.  Their cycle holonomy on the even parity component is

\[
\prod_{j=0}^{8} c_{2j}c_{2j+4}=+1,
\tag{11}
\]

because multiplication by `+4` permutes the even indices, making the product a square.  This contradicts (8).

#### The pair `(18,5)`

Here the reduced step-four edges come from the original pure-chord two-walks of displacement `10`, i.e. reduced step `-4`.  Their cycle holonomy is

\[
\prod_{i=0}^{17}c_i.
\tag{12}
\]

Switch the Hamilton path so that all `h_i=+1` except the seam `h_17=alpha`.  Iterating (9) around the eighteen vertices gives exactly

\[
\prod_{i=0}^{17}c_i=-\alpha.
\tag{13}
\]

(Equivalently, in the product formula for the recurrence there is one seam-shifted factor with odd multiplicity.)  By (10), the right-hand side of (13) is `+1`, again contradicting (8).

Thus both pairs in (7) satisfy `m^2>6`.  Combining the three reduced orders proves (2)--(3). `square`

---

## Consequence for the global equality problem

The four-locus theorem originally left

\[
t=2,
\qquad q=2t+1,
\qquad q=2t+2,
\qquad q=3t.
\]

The first three loci are now completely closed.  Therefore every still-unclassified equality pair satisfies the single resonance

\[
\boxed{q=3t.}
\tag{14}

This is the only remaining arithmetic mechanism for `m(N,s)^2=6`.
