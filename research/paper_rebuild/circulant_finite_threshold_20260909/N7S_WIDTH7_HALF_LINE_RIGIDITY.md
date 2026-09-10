# Width-seven half-line rigidity at `sqrt(8)`

This note strengthens the first all-signing width-seven lemma for the horizontal resonance `N=7s`.  The key point is that a sufficiently long complement tail leaves only two defect types.

## Theorem 1 (fourteen-complement half-line rigidity)

Let `M` be an open width-seven heptagon strip with

\[
\rho(M)^2<8.
\]

Normalize the inter-column matchings to the identity and write the seven-bit transition masks as usual, with `127` denoting a complement transition.  Suppose the transition word has the form

\[
\boxed{127^3,d,127^{14}},\qquad d\ne127.
\tag{1}
\]

Then, up to the simultaneous dihedral action `D_7` on the seven row labels,

\[
\boxed{d\in\{47,63\}.}
\tag{2}
\]

The reversed statement holds as well.

### Exact proof

The 127 non-complement masks split into exactly 17 `D_7` orbits, represented by

\[
0,1,3,5,7,9,11,15,19,21,23,27,31,43,47,55,63.
\tag{3}
\]

For each representative other than `47,63`, an integer vector `w` satisfies

\[
w^T(M^2-8I)w\ge0,
\qquad w\ne0.
\tag{4}
\]

The exact excess/norm pairs returned by the reproducibility certificate are

\[
\begin{array}{c|c}
d&(w^T(M^2-8I)w,\ w^Tw)\\ \hline
0&(616,252)\\
1&(448,266)\\
3&(404,234)\\
5&(344,267)\\
7&(328,261)\\
9&(228,270)\\
11&(220,256)\\
15&(260,266)\\
19&(152,263)\\
21&(62,266)\\
23&(98,261)\\
27&(176,265)\\
31&(94,264)\\
43&(20,610)\\
55&(14,590).
\end{array}
\tag{5}
\]

Thus all 15 listed classes have squared spectral radius at least eight.  Only the two classes in (2) survive the exact pruning, proving the theorem. `square`

The verifier `verify_n7s_width7_half_line.py` reconstructs the 17 orbit representatives and evaluates every accepted rejection in exact integer arithmetic.  Floating eigenvectors are used only to propose integer directions.

---

## 2. Structural meaning of the two survivors

After three complement transitions, a defect `d` changes the interior heptagon state to

\[
127\oplus d.
\]

For the two surviving types this gives

\[
127\oplus47=80,
\qquad
127\oplus63=64.
\]

The signed cycle `C(80)` is balanced and has a `\{\pm1\}` eigenvector

\[
v_{47}=(-1,-1,-1,-1,-1,1,1)^T,
\qquad C(80)v_{47}=2v_{47},
\tag{6}
\]

whereas `C(64)` is unbalanced and has

\[
v_{63}=(1,-1,1,-1,1,-1,1)^T,
\qquad C(64)v_{63}=-2v_{63}.
\tag{7}
\]

Consequently both satisfy

\[
C^2v=4v.
\tag{8}
\]

Along a complement run the diagonal signed-cycle blocks alternate between `C` and `-C`.  For the matrix

\[
Q=M^2-8I,
\]
all nearest-column blocks cancel in the interior, while the same-parity recurrence is

\[
(Qw)_j=(C^2-6I)w_j+w_{j-2}+w_{j+2}.
\tag{9}
\]

On either critical vector (6) or (7), equation (9) reduces to

\[
\boxed{-2w_j+w_{j-2}+w_{j+2}=0.}
\tag{10}
\]

This is the same zero-energy second-order transfer relation that made the long-gap theorem possible on the width-five line.  Hence the two surviving defect classes are not arbitrary computational residues: they are exactly the balanced and unbalanced critical heptagon channels that can propagate through a long complement segment.