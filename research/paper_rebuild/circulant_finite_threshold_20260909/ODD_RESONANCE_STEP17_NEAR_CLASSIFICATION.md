# Step seventeen at `sqrt(8)`: all chord-cycle lengths except one

The step-seventeen family has the same current status as step fifteen: every admissible chord-cycle length is classified except `k=5`.

## Theorem 1

For `C_(17k)(1,17)`,

\[
\boxed{m(51,17)>\sqrt8,}
\]

while

\[
\boxed{m(17k,17)<\sqrt8}
\]

for

\[
\boxed{k=4\quad\text{or}\quad k\ge6.}
\]

Thus the only unresolved member of this vertical family is

\[
\boxed{(N,s)=(85,17),\qquad k=5.}
\]

No statement about this last pair is claimed.

### Negative and even cases

The point `k=3` lies on the horizontal odd resonance `N=3s`; hence

\[
m(51,17)^2\ge8+\frac2{139}>8.
\]

Every even `k` is sub-threshold by the all-even-order theorem.  It remains to prove the positive result for odd `k>=7`.

---

## 1. The alternating seam signing

For odd `k`, let `N=17k`, put all Hamilton path signs equal to `+1`, the Hamilton seam equal to `-1`, and set the step-seventeen chord signs to

\[
c_i=(-1)^i.
\]

The universal seam-defect identity gives, after multiplication-by-two reindexing,

\[
8I-A^2=L_\Sigma+E_-+E_+,
\]

with exceptional pairs

\[
E_-:\{0,N-9\}\text{ of coefficient }-2,
\]

and

\[
E_+:\{a,a+8\}\text{ of coefficient }+2,
\qquad a=\frac{N-17}{2}.
\]

For the stable radius-five neighborhoods, the negative local form has 116 vertices and 200 base edges, and exact rational LDL has only positive pivots with

\[
\det Q_-
=1298197880264878128887655318684082374017286144>0.
\]

The positive local form has 115 vertices and 196 base edges, with

\[
\det Q_+
=23317294279084925351390808058137339284684800>0.
\]

For every odd `k>=21` the two induced edge sets are disjoint.  Therefore the full quadratic form is the sum of the two positive-definite local forms and the remaining nonnegative signed-edge squares.  Connectivity then forces equality only at the zero vector, so

\[
8I-A^2\succ0
\qquad(k\ge21\text{ odd}).
\]

---

## 2. Exact alternating bases `k=9,11,13,15,17`

For these five odd values the same alternating signing is checked directly by exact rational `LDL^T`; every pivot is positive.  The determinants are

\[
\begin{array}{c|c}
k&\det(8I-A^2)\\ \hline
9&14515909660668351009683318712690479467173632461251542314345941502418804539392,\\
11&7492688793090569582564673800444737469151727278364707741193439534177466505946471336223647393400,\\
13&1790558664127079268604134543407240067983781936156338217991028943805500745920632781738041741663509291246243074952,\\
15&359500068543753471128877144761874214766696369741112968277913985433803897042182306477110866507366486440308567777925633255124585600,\\
17&67546510399825407661203323360067075501650647238200944763176564802007271032943793924756110194913954386721922113614655973379735941264038668273325832.
\end{array}
\]

Thus all five are strictly sub-threshold.

---

## 3. The overlapping base `k=19`

At `k=19`, the two radius-five neighborhoods still overlap, so they cannot simply be added as disjoint absorbers.  Instead take their union and include both exceptional terms.  The induced local form has 225 vertices and 398 allocated base edges.  Exact rational LDL has only positive pivots and determinant

\[
2240939829741199510432570344342121777520575243070525763176968864061624897220596058066905989120>0.
\]

The remaining base-edge squares are nonnegative, and equality again propagates to zero.  Therefore the alternating signing is strictly sub-threshold at `k=19`.

---

## 4. The base `k=7`

For `N=119`, the unmodified alternating chord word has squared radius slightly above eight and is not used.  Reverse precisely

\[
c_{98},\quad c_{99}.
\]

For this explicit signing, exact rational LDL of `8I-A^2` has 119 positive pivots and determinant

\[
\boxed{
2965591063002674643944833344304548941451919837762075140600>0.
}
\]

Hence `m(119,17)<sqrt(8)`.

Combining Sections 1--4 with the even-order theorem proves the stated positive range. `square`

---

## Status of `(85,17)`

The pair `(85,17)` is intentionally left **Open**.  Numerical exploration of the basic alternating seam signing and small Hamming modifications is not a lower-bound certificate and is not promoted above **Observed** status.
