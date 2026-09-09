# Complete minimizer rigidity at the `sqrt(6)` boundary

The parameter classification

\[
m(N,s)^2=6
\iff
(N,s)\in\{(12,4),(16,3),(16,5),(20,8)\}
\]

is complete in `SIX_BOUNDARY_TRIANGLE_3T.md`.  This note strengthens that theorem by classifying the number of **labelled switching classes** attaining the boundary value.

## Theorem 1

Among Hamilton-gauge labelled switching classes, the complete equality counts are

\[
\boxed{
\begin{array}{c|c}
(N,s)&\#\{\text{labelled minimizing switching classes}\}\\ \hline
(12,4)&2,\\
(16,3)&32,\\
(16,5)&32,\\
(20,8)&2.
\end{array}}
\tag{1}
\]

Moreover:

1. the two `(12,4)` classes both have Hamilton holonomy `-1` and characteristic polynomial
   \[
   (x^2-6)^2(x^4-6x^2+6)^2;
   \tag{2}
   \]
2. the 32 `(16,3)` classes split evenly between Hamilton holonomy `-1` and `+1`; every one has
   \[
   \chi_A(x)=x^2(x-2)(x+2)(x^2-6)^4(x^2-2)^2,
   \tag{3}
   \]
   and every defect `B=A^2-4I` has exactly two off-diagonal entries of absolute value `2` above the diagonal;
3. multiplication by `5` on `Z_16` transports the 32 `(16,3)` classes bijectively to the 32 `(16,5)` classes;
4. the two `(20,8)` classes have Hamilton holonomy `-1`, opposite chord words, and characteristic polynomial
   \[
   (x^2-6)^2
   (x^8-14x^6+66x^4-114x^2+41)^2.
   \tag{4}
   \]

Thus the repeated-root equality mechanism at order 16 is genuinely much less rigid than the duplicate-free equality mechanism at orders 12 and 20.

---

## 1. Exact finite certification for `(12,4)`

Hamilton-path switching gives exactly

\[
2^{N+1}=2^{13}=8192
\]

labelled switching classes, parametrized by Hamilton holonomy `alpha=+-1` and twelve chord signs.

For every representative form

\[
K=6I-A^2.
\]

The script `verify_six_boundary_minimizer_rigidity.py` rejects a class only after producing an integer vector `z` satisfying the exact inequality

\[
z^T Kz<0.
\tag{5}
\]

A floating eigensolver is used only to propose `z`; it is never used for branch acceptance.  Exactly two classes are not rejected.  For both survivors exact symbolic factorization gives

\[
\chi_K(x)=x^4(x^2-6x+6)^4,
\tag{6}
\]

whose roots are all nonnegative, so `K` is positive semidefinite.  Both survivors have `alpha=-1`, opposite chord words, and the exact `A` polynomial (2).  Hence they are precisely the two minimizers.

---

## 2. Exact finite certification for `(16,3)`

Hamilton gauge now contains

\[
2^{17}=131072
\]

labelled switching classes.  The same exact integer-witness rejection rule (5) leaves exactly 32 survivors.

Their Hamilton holonomies split as

\[
16\text{ with }\alpha=-1,
\qquad
16\text{ with }\alpha=+1.
\tag{7}
\]

For every survivor exact symbolic algebra gives the same two factorizations

\[
\chi_A(x)
=x^2(x-2)(x+2)(x^2-6)^4(x^2-2)^2,
\tag{8}
\]

and

\[
\chi_K(x)
=x^8(x-6)^2(x-4)^4(x-2)^2.
\tag{9}
\]

Equation (9) certifies `K>=0` exactly.  In addition, direct integer inspection of

\[
B=A^2-4I
\]

shows that every survivor has exactly two unordered vertex pairs with

\[
|B_{ij}|=2.
\tag{10}
\]

Thus every order-16 minimizer lies genuinely on the repeated-root side of the root-quotient lemma.  The earlier explicit example was not exceptional inside the minimizing set; it represents a 32-class boundary stratum.

---

## 3. Transport to `(16,5)`

Multiplication by `5` is a unit of `Z_16` and sends

\[
\{\pm1,\pm3\}
\longmapsto
\{\pm5,\pm15\}
=
\{\pm1,\pm5\}.
\]

Therefore

\[
C_{16}(1,3)\cong C_{16}(1,5).
\]

Graph isomorphism preserves switching classes, spectra, and minimization.  Hence the 32 classes in Section 2 transport bijectively to exactly 32 minimizing labelled switching classes for `(16,5)`.

---

## 4. Analytic rigidity for `(20,8)`

Here the reduced parity component is `C_10(1,2)`.  The complete `t=2` component theorem proves that an index-at-most-two component has a **unique** labelled switching class, with negative consecutive triangle flux and step-one holonomy

\[
\alpha=-1.
\tag{11}
\]

For an original equality signing, the mixed channels are off the parity support and there are no twins.  They therefore vanish.  In Hamilton gauge let `h_i` be the step-one signs and `c_i` the step-eight chord signs.  The vanishing mixed channel gives

\[
c_{i+1}=-h_i h_{i+8}c_i.
\tag{12}
\]

The component holonomy forces the original Hamilton holonomy to be `-1`; after Hamilton-path switching,

\[
h_0=\cdots=h_{18}=1,
\qquad h_{19}=-1.
\tag{13}
\]

Equation (12) determines the entire chord word from the single choice `c_0=+-1`.  Its cyclic consistency is automatic because

\[
\prod_{i=0}^{19}(-h_i h_{i+8})
=(-1)^{20}\left(\prod_i h_i\right)^2=1.
\tag{14}
\]

Thus there are **at most two** equality classes.  Both choices occur: they are opposite chord words, have the same defect after mixed cancellation, and exact characteristic-polynomial expansion gives (4).  Hence there are exactly two.

---

## 5. Structural conclusion

The complete six-boundary theorem is therefore rigid in two different senses.

- At `(12,4)` and `(20,8)`, equality is duplicate-free and the lift equations leave only one binary chord phase, producing two labelled classes.
- At `(16,3)` and `(16,5)`, the exceptional `K_{4,4}` parity quotient admits repeated roots; the equality set expands to 32 labelled classes while retaining a single exact spectrum.

This distinction should be stated together with the parameter classification in the final manuscript: the four equality pairs are spectrally identical only at the threshold value `m^2=6`, but their minimizing switching geometry is not uniform.
