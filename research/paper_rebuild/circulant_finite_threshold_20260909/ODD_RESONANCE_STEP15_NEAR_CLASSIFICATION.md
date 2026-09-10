# Complete vertical `sqrt(8)` threshold for step fifteen

The positive constructions in this file, combined with the all-signing horizontal theorem `N5S_COMPLETE_THRESHOLD_CLASSIFICATION.md`, now give a complete threshold classification for the step-fifteen vertical family.

## Theorem 1

For every admissible integer `k>=3`,

\[
\boxed{
m(15k,15)<\sqrt8
\iff
k=4\text{ or }k\ge6.
}
\tag{1}
\]

The two non-sub-threshold chord-cycle lengths are `k=3` and `k=5`:

\[
\boxed{
m(45,15)^2\ge8+\frac{24}{1667}>8,
\qquad
m(75,15)\ge\sqrt8.
}
\tag{2}
\]

The first inequality is the horizontal `N=3s` obstruction.  The second is the all-signing width-five obstruction proved in `N5S_BASE_15_17_GLOBAL_OBSTRUCTION.md` and subsumed by the complete `N=5s` classification.

If `k` is even, then `N=15k` is even and the all-even-order finite construction gives `m(15k,15)<sqrt(8)`.  It remains only to record the independent finite constructions for odd `k>=7`.

---

## 1. Alternating seam signing for odd `k>=9`

Let `N=15k`, `k>=9` odd.  Use Hamilton seam `-1` and chord signs `c_i=(-1)^i`.  The two-seam-defect theorem gives, after multiplication-by-two reindexing,

\[
8I-A^2=L_\Sigma+E_-+E_+,
\tag{3}
\]

where

\[
E_-:\ \{0,N-8\}\text{ has coefficient }-2,
\]

and

\[
E_+:\ \{a,a+7\}\text{ has coefficient }+2,
\qquad a=\frac{N-15}{2}.
\tag{4}
\]

Take radius-five base-graph induced edge sets around the two pairs.  In the stable local pattern the negative absorber has 109 vertices and 188 base edges.  Exact rational `LDL^T` has only positive pivots and

\[
\det Q_-=3778167212446958262349168881634331311931392>0.
\tag{5}
\]

The positive absorber has 110 vertices and 192 base edges, every exact LDL pivot is positive, and

\[
\det Q_+=105402599868300324129777428804783514283081728>0.
\tag{6}
\]

For odd `k>=23` the two radius-five vertex sets are disjoint by the integer-offset bounds

\[
B_5(\{0,N-8\})\subset[-83,75]\pmod N,
\]

\[
B_5(\{a,a+7\})\subset a+[-75,82]\pmod N.
\]

Thus the full quadratic form is the sum of two positive-definite absorber forms and the remaining nonnegative signed-edge squares, proving

\[
8I-A^2\succ0
\qquad(k\ge23\text{ odd}).
\tag{7}
\]

The exact edge sets are already disjoint at `k=21`, so the same local matrices also handle `k=21`.

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
\tag{8}
\]

Together with the absorber argument, this proves the alternating construction for every odd `k>=9`.

---

## 3. The odd base `k=7`

For `N=105`, start from `c_i=(-1)^i` and reverse precisely the adjacent chord signs

\[
c_{86},\ c_{87}.
\tag{9}
\]

Keep the negative Hamilton seam.  Exact rational LDL of `8I-A^2` has 105 positive pivots and determinant

\[
1849301460651035605088456882195255546256126182948864>0.
\tag{10}
\]

Therefore

\[
m(105,15)<\sqrt8.
\tag{11}
\]

The positive constructions in Sections 1--3 cover every odd `k>=7`; even `k` are covered by the all-even theorem.  Together with the two all-signing negative points in (2), this proves Theorem 1. `square`

---

## Audit note

The earlier version of this file left `(75,15)` open because search failure was not a lower bound.  That status is obsolete.  The pair is now excluded over **all** signings by intrinsic width-five flux rules and an exact cyclic certificate, and the vertical step-fifteen theorem is complete.