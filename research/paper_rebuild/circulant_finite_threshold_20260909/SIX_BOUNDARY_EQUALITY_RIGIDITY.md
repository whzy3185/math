# Rigidity at the four `sqrt(6)` equality pairs

The parameter classification

\[
m(N,s)^2=6
\iff
(N,s)\in\{(12,4),(16,3),(16,5),(20,8)\}
\]

is proved in `SIX_BOUNDARY_TRIANGLE_3T.md`.  This note classifies the labelled switching classes attaining the minimum at all four pairs.

## Theorem 1 (complete labelled equality rigidity)

The numbers of labelled minimizing switching classes are

\[
\boxed{
\begin{array}{c|cccc}
(N,s)&(12,4)&(16,3)&(16,5)&(20,8)\\ \hline
\#\text{ minimizers}&2&32&32&2.
\end{array}}
\tag{1}
\]

For `(12,4)` and `(20,8)` the classification is analytic.  For `(16,3)` a complete exact finite certificate over the `2^17` Hamilton-gauge switching classes is used; `(16,5)` follows by the multiplier `5` isomorphism.

---

# 1. The analytic pairs `(12,4)` and `(20,8)`

Let `(N,s)` be either `(12,4)` or `(20,8)`, and suppose

\[
\rho(A)^2\le6.
\]

Put `B=A^2-4I`.  The parity graph has two nonempty connected components, one on each parity class.  The two mixed two-walk displacements `s-1,s+1` are odd, hence join the two parity classes and lie outside `supp(B mod 2)`.

If such an off-support entry had absolute value `2`, the `K=6I-A^2` root lemma would force its endpoints to be twins in the parity graph.  Vertices in distinct parity components cannot be twins because their nonempty neighbourhoods lie in disjoint components.  Hence both mixed channels vanish identically.

Write `h_i` for the step-one signs and `c_i` for the step-`s` signs.  One mixed equation is

\[
h_i c_{i+1}+c_i h_{i+s}=0,
\]

so

\[
c_{i+1}=-h_i h_{i+s}c_i.
\tag{2}
\]

Switch a Hamilton path.  Then all step-one signs are `+1` except the seam, whose sign is the Hamilton holonomy

\[
\alpha\in\{\pm1\}.
\]

For each fixed `alpha`, recurrence (2) determines the entire chord word from its first sign

\[
\varepsilon=c_0\in\{\pm1\}.
\]

Thus at most four labelled switching classes can occur.  The four candidates can be diagonalized exactly.

## `(12,4)`

For `alpha=-1`, both values of `epsilon` have

\[
\chi_A(x)
=(x^2-6)^2(x^4-6x^2+6)^2,
\tag{3}
\]

so `rho(A)^2=6`.

For `alpha=+1`, both values have

\[
\chi_A(x)
=(x-2)^3(x+2)^3(x^2-8)(x^2-2)^2,
\tag{4}
\]

so `rho(A)^2=8`.

Therefore `(12,4)` has exactly two labelled minimizing switching classes.

## `(20,8)`

For `alpha=-1`, both values of `epsilon` have

\[
\chi_A(x)
=(x^2-6)^2
(x^8-14x^6+66x^4-114x^2+41)^2,
\tag{5}
\]

and the finite anti-periodic calculation already proves `rho(A)^2=6`.

For `alpha=+1`,

\[
\chi_A(x)
=(x-2)(x+2)(x^2-8)(x^2-3)^4
(x^4-8x^2+11)^2,
\tag{6}
\]

so `rho(A)^2=8`.

Therefore `(20,8)` also has exactly two labelled minimizing switching classes.

This proves the first and fourth entries of (1) without enumeration.

---

# 2. The exceptional repeated-root pair `(16,3)`

At `(16,3)` the parity component is

\[
C_8(1,3)=K_{4,4},
\]

which has the exceptional order-four translation stabilizer.  Repeated/antipodal roots genuinely occur, so the preceding mixed-channel recurrence does not classify all equality signings.

We therefore use the complete Hamilton-path gauge.  Every labelled switching class has a unique representative determined by

\[
\alpha\in\{\pm1\}
\]

and sixteen chord signs.  Hence there are exactly

\[
2^{17}=131072
\]

classes to audit.

For each class form the integer symmetric matrix

\[
K=6I-A^2.
\]

The condition `rho(A)^2<=6` is exactly `K>=0`.

The script `verify_n16_equality_classes.py` audits all `131072` classes with the following exact trust boundary:

1. a floating eigensolver may propose a negative direction;
2. a class is rejected **only** after an integer vector `v` has been produced and the exact integer inequality
   \[
   v^T K v<0
   \]
   has been checked;
3. every non-rejected class is checked by exact symbolic characteristic polynomial.

Thus floating arithmetic can only make the script fail to find a certificate; it cannot cause a false rejection or false acceptance.

The exhaustive result is:

\[
131040\text{ classes have an exact negative integer witness},
\]

and exactly

\[
\boxed{32}
\]

classes remain.  All 32 have the same exact characteristic polynomial

\[
\boxed{
\chi_A(x)=x^2(x-2)(x+2)(x^2-6)^4(x^2-2)^2.
}
\tag{7}
\]

Hence all 32 have squared spectral radius exactly six.  They split evenly by Hamilton holonomy:

\[
16\text{ with }\alpha=-1,
\qquad
16\text{ with }\alpha=+1.
\tag{8}
\]

This is a complete finite certificate, not a numerical observation.

---

# 3. The pair `(16,5)`

Multiplication by `5` on `Z_16` is a vertex permutation and sends

\[
\{\pm1,\pm3\}
\longmapsto
\{\pm5,\pm15\}
=
\{\pm5,\pm1\}.
\]

Thus

\[
C_{16}(1,3)\cong C_{16}(1,5).
\]

The permutation transports signings bijectively, commutes with switching up to relabelling, and preserves adjacency spectra.  Therefore it induces a bijection between labelled switching classes attaining the minimum on the two graphs.

Consequently `(16,5)` also has exactly 32 labelled minimizing switching classes, completing (1). `square`

---

## Corollary 1.1

The complete six-threshold theorem can be stated with equality rigidity:

\[
\boxed{
\begin{array}{c|c}
(N,s)&\#\text{ labelled switching classes with }\rho^2=6\\ \hline
(12,4)&2\\
(16,3)&32\\
(16,5)&32\\
(20,8)&2.
\end{array}}
\]

No other admissible parameter pair has a signing with squared spectral radius exactly six.
