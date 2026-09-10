# Step fifteen at `sqrt(8)`: all chord-cycle lengths except one

The step-fifteen family is the first vertical family in which the current finite construction does not yet close every chord-cycle length.  Nevertheless the theorem below reduces the entire family to one finite-global base problem.

## Theorem 1

For the vertical family `C_(15k)(1,15)` one has

\[
\boxed{m(45,15)>\sqrt8,}
\tag{1}
\]

while

\[
\boxed{m(15k,15)<\sqrt8}
\tag{2}
\]

for

\[
\boxed{k=4\quad\text{or}\quad k\ge6.}
\tag{3}
\]

Thus the only unresolved admissible chord-cycle length in this vertical family is

\[
\boxed{k=5,\qquad (N,s)=(75,15).}
\tag{4}
\]

No claim is made here about (4).

### Proof of the negative point

Since `15` is odd and at least seven, the horizontal theorem on `N=3s` gives

\[
m(45,15)^2\ge8+\frac2{139}>8.
\]

### Even chord-cycle lengths

If `k` is even, then `N=15k` is even.  The all-even-order finite construction gives `m(15k,15)<sqrt(8)`.  This includes `k=4,6,8,...`.

It remains to prove (2) for odd `k>=7`.

---

## 1. Alternating seam signing for odd `k>=9`

Let `N=15k`, `k>=9` odd.  Use Hamilton seam `-1` and chord signs `c_i=(-1)^i`.  The two-seam-defect theorem gives, after multiplication-by-two reindexing,

\[
8I-A^2=L_\Sigma+E_-+E_+,
\tag{5}
\]

where the exceptional pairs are

\[
E_-:\ \{0,N-8\}\text{ with coefficient }-2,
\]

and

\[
E_+:\ \{a,a+7\}\text{ with coefficient }+2,
\qquad a=\frac{N-15}{2}.
\tag{6}
\]

Take radius-five base-graph induced edge sets around the two pairs.  In the stable local pattern the negative absorber has 109 vertices and 188 base edges.  Exact rational `LDL^T` has only positive pivots and

\[
\boxed{\det Q_-=3778167212446958262349168881634331311931392>0.}
\tag{7}
\]

The positive absorber has 110 vertices and 192 base edges, every exact LDL pivot is positive, and

\[
\boxed{\det Q_+=105402599868300324129777428804783514283081728>0.}
\tag{8}
\]

For odd `k>=23` the two radius-five vertex sets are disjoint by the elementary integer-offset bounds

\[
B_5(\{0,N-8\})\subset[-83,75]\pmod N,
\]

and

\[
B_5(\{a,a+7\})\subset a+[-75,82]\pmod N.
\]

Indeed `a=15(k-1)/2>=165` and `N-a=15(k+1)/2>=180`, which separates the two lifted intervals from both sides of the seam.  Hence the two local edge sets are disjoint, and the full quadratic form is the sum of two positive-definite local absorbers and the remaining nonnegative signed-edge squares.  Therefore

\[
8I-A^2\succ0
\qquad(k\ge23\text{ odd}).
\tag{9}
\]

The exact edge sets already become disjoint at `k=21`; the slightly later threshold in (9) is chosen only to keep the interval proof immediate.

---

## 2. Exact alternating bases `k=9,11,13,15,17,19`

For these six odd lengths the same alternating seam signing is certified directly.  Exact rational LDL has only positive pivots.  The determinants of `8I-A^2` are

\[
\begin{array}{c|c}
k&\det(8I-A^2)\\ \hline
9&29245809126400346085098954358334266552911234352814393414526937002488,\\
11&81345420562709807947141505074935918169325573548550037178098091486387968952830846792,\\
13&162521835310602873945303957432859962422579081241254071361556594492099339038312172488240807040047224,\\
15&293804017270487835611162286466320538777943101838852071037075676365802812233712833302287545180173427118677957140744,\\
17&510683970816354646530633036895217853290955435153117124541465070106856490524072524819498061323926375744552520079062894287446875000,\\
19&872488811110783040085698329295180035174154225756377199094999455714249783071274359877825226852699703364096334509183149674930571596815483736822600.
\end{array}
\tag{10}
\]

For `k=21`, the two radius-five absorber edge sets are already disjoint and the same local matrices (7)--(8) apply.  Thus (9) in fact extends to all odd `k>=21`.

Combining this with the six exact bases proves the alternating construction for every odd `k>=9`.

---

## 3. The odd base `k=7`

For `N=105`, the unmodified alternating chord word lies slightly above the threshold, so it is not used.  Start from `c_i=(-1)^i` and reverse precisely the adjacent chord signs

\[
c_{86},\ c_{87}.
\tag{11}
\]

Keep the negative Hamilton seam.  Exact rational LDL of the resulting matrix `8I-A^2` has 105 positive pivots and determinant

\[
\boxed{
1849301460651035605088456882195255546256126182948864>0.
}
\tag{12}
\]

Therefore

\[
m(105,15)<\sqrt8.
\tag{13}
\]

Sections 1--3, together with the even-order theorem, prove (2)--(3). `square`

---

## 4. Status of `(75,15)`

The pair `(75,15)` is deliberately left **Open**.  The basic alternating seam signing has squared radius approximately `8.0931`; the best small Hamming-neighbour modifications examined during this pass remain above eight.  These observations are search diagnostics only, not lower bounds and not theorem evidence.

Thus step fifteen presently marks the first point at which a genuinely new finite signing pattern or a global obstruction theorem is needed.