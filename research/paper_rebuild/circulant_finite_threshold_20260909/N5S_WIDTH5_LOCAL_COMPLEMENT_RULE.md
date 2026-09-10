# An exact width-five local complement rule at the `sqrt(8)` threshold

This note begins the all-signing analysis of the next horizontal resonance `N=5s`.  It proves a local structural rule for the width-five strip obtained by reordering the chord pentagons.  The result is finite, exact, and independent of any chosen periodic signing.

## 1. Open width-five strips

For a state

\[
\eta=(\eta_0,\ldots,\eta_4)\in\{\pm1\}^5,
\]

let `C(eta)` be the signed adjacency matrix of the pentagon `C_5`, with edge signs `eta_r` on `r--(r+1)`.  For a word

\[
W=(\eta^{(0)},\ldots,\eta^{(L-1)})
\]

define the open strip matrix

\[
M(W)=
\begin{pmatrix}
C(\eta^{(0)})&I&&\\
I&C(\eta^{(1)})&I&\\
&\ddots&\ddots&\ddots\\
&&I&C(\eta^{(L-1)})
\end{pmatrix}.
\tag{1}
\]

This is exactly the induced signed adjacency matrix on `L` consecutive chord-pentagon columns of `C_(5s)(1,s)` after switching the step-one matching edges inside the interval to `+1`.

Call the transition between columns `j` and `j+1` a **complement transition** if

\[
\eta^{(j+1)}=-\eta^{(j)}.
\tag{2}
\]

Equivalently, all five elementary square fluxes between these two columns are negative.  Thus the notion is switching invariant once the inter-column matching is normalized, and its flux formulation is intrinsic.

## Theorem 1 (thirteen-column complement rule)

If a thirteen-column open strip satisfies

\[
\rho(M(W))^2<8,
\tag{3}
\]

then among its two central transitions at least one is a complement transition.  With columns numbered `0,...,12`,

\[
\boxed{
\eta^{(6)}=-\eta^{(5)}
\quad\text{or}\quad
\eta^{(7)}=-\eta^{(6)}.
}
\tag{4}
\]

In particular, two consecutive non-complement transitions cannot occur in the middle of a sub-`sqrt(8)` width-five strip once five columns of context are present on each side.

### Proof

The proof is an exhaustive finite lemma with exact branch rejection.  We give the symmetry reduction and the trust boundary explicitly.

Represent a pentagon state by a five-bit mask, with a bit recording a negative edge.  Three operations preserve the spectral radius of every open strip:

1. apply the same switching of the five row vertices in every column; on edge masks this is XOR by an even-parity five-bit mask;
2. apply the same dihedral automorphism of `C_5` in every column;
3. complement every pentagon state simultaneously.

For the third operation, if `D` is block diagonal with block `(-1)^j I_5` on column `j`, then

\[
M(-W)=-D M(W)D,
\]

so the spectral radius is unchanged.  The first two operations give `16*10=160` actions and global complementation doubles this to a group of 320 spectral-radius-preserving actions.  This group is transitive on the 32 one-column states.

At every prefix length we retain one lexicographically canonical representative of each orbit.  Completeness is recursive: if a length-`L` prefix is moved to its canonical representative by a group element `g`, applying the same `g` to any one-column extension sends the new last state to one of the same 32 allowed states.  Thus extending all canonical prefixes by all 32 states and canonicalizing again loses no orbit.

A prefix is rejected only after an integer vector `w` is found with

\[
w^T(M(W)^2-8I)w\ge0,
\qquad w\ne0.
\tag{5}
\]

Equation (5) proves exactly that `rho(M(W))^2>=8`; by interlacing, no extension of such a prefix can occur inside a strip satisfying (3).  A floating eigensolver is used only to propose directions from which integer vectors are rounded.  The inequality (5) itself is evaluated in exact integer arithmetic.  Failure to find a witness merely retains the branch, so floating error cannot create a false rejection.

The orbit-survivor counts through length eight are

\[
\boxed{1,7,33,130,548,1867,3870,10080.}
\tag{6}
\]

At length nine we only need words for which the two central transitions (between columns `3--4` and `4--5`) are both non-complement.  From all extensions of the 10,080 length-eight survivors, symmetry leaves exactly 7,392 such candidates.  Exact rejection (5) leaves only

\[
71
\tag{7}
\]

possible nine-column words.  In every one, both central transition masks have Hamming weight four.

Now extend these survivors while keeping the same central bad pair.  Appending one column gives 2,272 orbit candidates and 204 exact survivors; prepending one column gives 6,528 candidates and 135 survivors; appending once more gives 4,320 candidates and a single survivor; finally prepending one more column gives 32 candidates and

\[
\boxed{0}
\tag{8}
\]

survivors.  At this last stage the original central bad pair has shifted to transitions `5--6` and `6--7` in a thirteen-column word.  Hence no word satisfying (3) can have both of these transitions non-complement, proving (4). `square`

The complete enumeration and every exact integer branch certificate are reproduced by `verify_n5s_width5_local_complement.py`.

---

## 2. Consequence for a putative `N=5s` obstruction theorem

For a cyclic width-five representation of `C_(5s)(1,s)`, condition (4) says that wherever a thirteen-column interval avoids the helical seam, non-complement transitions must be isolated: every adjacent pair of transitions contains a complement transition.

This is the first all-signing local rigidity statement on the `N=5s` resonance.  It is not yet a global obstruction theorem.  An odd cyclic word can contain isolated non-complement defects, so an additional rule describing their type, separation, or seam compatibility is needed before one may conclude that `(75,15)` or `(85,17)` is above `sqrt(8)`.

Accordingly, no global `N=5s` threshold claim is made here.  The next target is to classify the isolated non-complement transitions surviving Theorem 1 and derive a second local rule strong enough to propagate around the odd cyclic seam.