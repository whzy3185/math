# Embedded even-gap exclusion in width-five strips

This note strengthens the all-signing local analysis of the horizontal resonance `N=5s`.  As in `N5S_WIDTH5_LOCAL_COMPLEMENT_RULE.md`, an open width-five strip is encoded by signed pentagon states

\[
\eta_0,\eta_1,\ldots,
\in\{\pm1\}^5,
\]

with identity matchings between adjacent columns.  Write the transition mask

\[
\delta_j=\eta_j\oplus\eta_{j+1}\in\{0,\ldots,31\}.
\]

The transition is **complement** precisely when `delta_j=31`; otherwise it is a **defect**.

## Theorem 1 (embedded gap-2/gap-4 exclusion)

Let `M` be the signed adjacency matrix of an open width-five strip satisfying

\[
\rho(M)^2<8.
\]

Suppose two specified defect transitions are separated by exactly `g` complement transitions, where

\[
g\in\{2,4\}.
\]

Then these two defects cannot have two further arbitrary transitions available on one side and one further arbitrary transition on the other side.  Equivalently, no transition word of either form

\[
(*,*,d,31^g,e,*)
\qquad\text{or its reversal}
\]

with `d,e!=31` occurs in a sub-`sqrt(8)` open strip.

Thus, in any sufficiently embedded seam-free portion of a cyclic `N=5s` strip, two consecutive non-complement defects can never be separated by exactly two or four complement transitions.

### Proof

The proof is a finite exact certificate.  We describe the quotient and every survivor count.

First normalize the initial pentagon state to the all-positive state.  Common row switching together with global complementation is transitive on the 32 pentagon states.  These operations cancel from every transition mask, so after this normalization the residual symmetry on a transition word is only the dihedral group `D_5`, of order ten, acting simultaneously on all five-bit masks.

Fix `g=2` or `4`.  Before adding external context, the central words are

\[
(d,31^g,e),\qquad d,e\in\{0,\ldots,30\}.
\]

The `31^2` labelled choices reduce to exactly 121 dihedral orbits.  A candidate word is discarded only after an integer vector `w` is found for which

\[
w^T(M^2-8I)w\ge0,
\qquad w\ne0.
\tag{1}
\]

Equation (1) is an exact certificate that the corresponding open strip has squared spectral radius at least eight.  By principal-submatrix interlacing, every extension of a discarded word is also impossible inside a sub-threshold strip.

The exact survivor chains are:

\[
\begin{array}{c|c|c|c|c}
g&\text{central}&+\text{left}&+\text{right}&+\text{left}\\ \hline
2&121\to12&336\to61&1880\to8&256\to0,\\
4&121\to12&336\to57&1752\to1&32\to0.
\end{array}
\tag{2}
\]

At each extension stage all 32 possible transition masks are allowed; no hypothesis is imposed on the added context.  Dihedral canonicalization is performed after every extension, and rejection is only through the exact integer inequality (1).  The final zero survivor count proves that no word `(*,*,d,31^g,e,*)` with `g=2` or `4` can have squared spectral radius below eight.  Reversing the strip gives the stated symmetric version. `square`

The complete reproducible certificate is `verify_n5s_width5_even_gap_24.py`.  A floating eigensolver in that script is used only to propose integer directions; every branch rejection is accepted only after (1) is evaluated in exact integer arithmetic.  Therefore numerical error can retain an unnecessary branch but cannot create a false rejection.

## Consequence for the `N=5s` program

Together with the thirteen-column complement rule, this excludes the first two even spacings in the finite defect-spacing system.  The remaining step toward a global odd-`s` obstruction is to control even complement gaps at least six (where the spectral excess approaches the threshold and a transfer/response argument is preferable to a fixed local window) and then impose the cyclic parity condition.