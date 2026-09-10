# Complete vertical `sqrt(8)` threshold for step seventeen

The positive constructions in this file, together with the complete all-signing horizontal theorem `N5S_COMPLETE_THRESHOLD_CLASSIFICATION.md`, now close the step-seventeen vertical family.

## Theorem 1

For every admissible integer `k>=3`,

\[
\boxed{
m(17k,17)<\sqrt8
\iff
k=4\text{ or }k\ge6.
}
\tag{1}
\]

The two non-sub-threshold chord-cycle lengths are

\[
\boxed{
m(51,17)^2\ge8+\frac{24}{1667}>8,
\qquad
m(85,17)\ge\sqrt8.
}
\tag{2}
\]

The first is the horizontal `N=3s` obstruction; the second is the all-signing width-five obstruction.  Every even `k` is sub-threshold by the all-even-order theorem.  It remains to record the independent constructions for odd `k>=7`.

---

## 1. Alternating seam signing for large odd `k`

For odd `k`, put `N=17k`, take all Hamilton path signs `+1`, Hamilton seam `-1`, and chord signs

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

For every odd `k>=21` the two induced edge sets are disjoint.  Therefore the full quadratic form is the sum of the two positive-definite local forms and the remaining nonnegative signed-edge squares, giving

\[
8I-A^2\succ0
\qquad(k\ge21\text{ odd}).
\tag{3}
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
\tag{4}
\]

---

## 3. The overlapping base `k=19`

At `k=19`, use the union of the two overlapping radius-five absorber neighborhoods and include both exceptional terms.  The induced 225-vertex local form has exact positive rational LDL pivots and determinant

\[
2240939829741199510432570344342121777520575243070525763176968864061624897220596058066905989120>0.
\tag{5}
\]

Hence the alternating signing is sub-threshold at `k=19`.

---

## 4. The base `k=7`

For `N=119`, reverse precisely

\[
c_{98},\quad c_{99}
\]

from the alternating chord word while retaining the negative Hamilton seam.  Exact rational LDL of `8I-A^2` has 119 positive pivots and determinant

\[
2965591063002674643944833344304548941451919837762075140600>0.
\tag{6}
\]

Thus `m(119,17)<sqrt(8)`.

Sections 1--4 cover every odd `k>=7`; the even cases follow from the even-order theorem.  Together with the two all-signing negative points in (2), Theorem 1 follows. `square`

---

## Audit note

The former version of this file left `(85,17)` open because failure to find a signing was correctly not treated as a lower bound.  That status has now been superseded by the all-signing width-five proof, so the step-seventeen threshold theorem is complete.