# Even defect gaps 6 through 14 are locally forbidden

Continue with the transition-mask notation for open width-five pentagon strips.  A transition mask is `31` exactly for a complement transition and is a **defect** otherwise.

## Theorem 1

Let `M` be an open width-five strip with

\[
\rho(M)^2<8.
\]

Suppose two specified defect transitions are separated by exactly `g` complement transitions, with

\[
\boxed{g\in\{6,8,10,12,14\}.}
\]

Then it is impossible for these two defects to have one further arbitrary transition on each side.  In transition notation, no sub-threshold strip contains

\[
\boxed{(*,d,31^g,e,*),\qquad d,e\ne31.}
\tag{1}
\]

### Proof

Normalize the first pentagon state to zero.  Transition masks are invariant under common row switching and global complementation; the residual symmetry is the dihedral group `D_5`, acting simultaneously on all masks.

For fixed `g`, the `31^2=961` labelled central choices

\[
(d,31^g,e),\qquad d,e\ne31,
\]

have exactly 121 dihedral orbits.  A branch is rejected only after an integer vector `w` certifies

\[
w^T(M^2-8I)w\ge0,
\qquad w\ne0.
\tag{2}
\]

Such a branch cannot occur in a strip of squared spectral radius below eight, and by interlacing none of its extensions can occur either.

For every `g` under consideration, exact pruning leaves 12 central survivors.  Add one completely arbitrary transition on the left and canonicalize again; then add one completely arbitrary transition on the right.  The exact counts are

\[
\begin{array}{c|c|c|c}
g&\text{central}&+\text{left}&+\text{right}\\ \hline
6&121\to12&336\to53&1624\to0,\\
8&121\to12&336\to40&1220\to0,\\
10&121\to12&336\to35&1060\to0,\\
12&121\to12&336\to19&572\to0,\\
14&121\to12&336\to14&412\to0.
\end{array}
\tag{3}
\]

The external transitions in (1) range independently over all 32 masks; in particular they are not assumed to be complement transitions.  Since the final survivor set is empty in every row, (1) is impossible. `square`

The verifier `verify_n5s_width5_even_gap_6_14.py` reproduces every orbit count and every exact integer branch rejection.  Floating eigenvectors are used only to propose integer witnesses; the decision to reject is always the exact inequality (2).

## Role in the cyclic problem

Together with the separate gap-2/gap-4 theorem, this controls every even gap up to fourteen once modest external context is available.  On the finite odd cycles of lengths 15 and 17 this leaves only the few cases in which a long even gap consumes almost the whole cycle; those cases must retain the helical seam and are treated by a separate complete cyclic certificate.