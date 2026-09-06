# A uniform all-signing obstruction on the resonance line `N=3s`

Date: 2026-09-06.

This note gives an infinite all-signing finite-order theorem, now with the
sharpened local margin `1/70`.

## 1. Main theorem

Let `s>=7` be odd and let `A_sigma` be the signed adjacency matrix of an
arbitrary edge signing of

\[
 C_{3s}(1,s).
\]

**Theorem 3S.** For every odd `s>=7` and every signing `sigma`,

\[
 \boxed{
 \rho(A_\sigma)^2\ge 8+\frac1{70}>8.}
 \tag{1}
\]

Consequently, if `m(N,s)` denotes the minimum signed spectral radius over all
edge signings of `C_N(1,s)`, then

\[
 \boxed{
 m(3s,s)^2\ge8+\frac1{70}
 \qquad(s\ge7\text{ odd}).}
 \tag{2}
\]

Thus the line `N=3s` is a genuine arithmetic obstruction family.  No edge
signing enters the sub-`sqrt(8)` regime.

The proof has one finite computer-assisted local lemma with exact integer
witnesses, plus a structural signed-triangle argument.  The short cases
`s=7,9` are independently covered by exact exhaustive certificates.

## 2. Hamilton gauge and width-three triangular strip

Switch along a Hamilton spanning path so that the step-one cycle has signs
`+1` except for its closing holonomy

\[
 \alpha\in\{+1,-1\}.
\]

Write vertices as

\[
 i=j+a s,
 \qquad
 0\le j<s,\quad a\in\{0,1,2\}.
\]

For fixed `j`, the three `s`-chords form a signed triangle.  Let its 3-by-3
signed adjacency matrix be `B_j`.  Each `B_j` has zero diagonal and all three
off-diagonal entries in `{+1,-1}`, hence exactly eight possible states.

Between ordinary neighboring columns the step-one edges give `I_3`.  The
closing matching from column `s-1` to column `0` is an orthogonal signed cyclic
permutation `S_alpha`.

For fixed `alpha`, the `3s` Hamilton-gauge chord signs are in bijection with
the arbitrary triangle-state word

\[
 (B_0,\ldots,B_{s-1}).
\]

Thus the width-three model represents every switching class.

## 3. Exact nine-column local rule

For an open chain of nine signed-triangle columns let

\[
 M(B_0,\ldots,B_8)
\]

be the block tridiagonal matrix with diagonal blocks `B_j` and identity
matchings between successive columns.

`verify_triangle_strip_local_rule.py` proves:

**Lemma 3S-L (nine-column rule).** For every eight-state word
`(B_0,...,B_8)`, either

\[
 \boxed{\|M\|^2\ge8+\frac1{70}}
 \tag{3}
\]

or the six middle transitions satisfy

\[
 \boxed{B_{j+1}=-B_j\qquad(j=1,2,\ldots,6).}
 \tag{4}
\]

### Exact certification boundary

The verifier recursively extends words.  Floating arithmetic only proposes
integer vectors.  A prefix is pruned only when exact integer arithmetic
verifies

\[
 70\,w^T(M^2-8I)w\ge w^Tw>0.
 \tag{5}
\]

The counts of unpruned prefixes at lengths `1,...,9` are

\[
 8,56,152,440,488,1016,656,1064,128.
 \tag{6}
\]

Every final survivor satisfies (4).  Hence every word violating (4) carries
an exact local Rayleigh certificate for (3).

The clean constant `1/70` is close to the true finite-state boundary.  A
numerical branch-and-bound search finds a violating 9-word with squared norm
approximately `8.014397`, so `1/69` is already too strong for this local
dichotomy.  This numerical observation is only a sharpness comment; the
`1/70` theorem is certified by (5).

## 4. Straightening a window across the helical seam

Take any nine consecutive cyclic columns of `C_(3s)(1,s)`.  For `s>=11`
these form a proper open principal subgraph.

A window not crossing the Hamilton seam already has identity intercolumn
matchings.  If a window crosses the seam, conjugate all columns after the
unique exceptional matching by the same signed permutation `S_alpha^T`.
This straightens the seam matching to `I_3`; signed-permutation conjugation
maps a signed triangle to another signed triangle and preserves norm.

Therefore every nine-column cyclic window obeys the same dichotomy (3)--(4).

## 5. Absence of a local witness forces global alternation

Assume for contradiction

\[
 \rho(A_\sigma)^2<8+\frac1{70}.
 \tag{7}
\]

Then no nine-column principal window can satisfy (3).  Applying (4) in
sliding windows forces every ordinary transition to alternate:

\[
 \boxed{B_{j+1}=-B_j\qquad(0\le j<s-1).}
 \tag{8}
\]

Since `s` is odd,

\[
 B_{s-1}=B_0.
 \tag{9}
\]

Apply the local rule to a window in which the helical seam is a middle
transition.  After straightening that matching, (4) gives

\[
 S_\alpha B_0S_\alpha^T=-B_{s-1}=-B_0
 \tag{10}
\]

(up to transposing `S_alpha`).

## 6. Signed-triangle trace obstruction

If a signed triangle `B` has edge signs `u,v,w`, then

\[
 \operatorname{tr}(B^3)=6uvw\in\{+6,-6\}.
 \tag{11}
\]

Orthogonal similarity preserves this trace, whereas

\[
 \operatorname{tr}((-B)^3)=-\operatorname{tr}(B^3).
\]

Thus no signed triangle is orthogonally similar to its negative.  Equation
(10) is impossible.  This proves (1) for every odd `s>=11`.

Equivalently, the two signed-triangle spectra are

\[
 \{2,-1,-1\},\qquad\{-2,1,1\},
\]

and negation exchanges rather than preserves them.

## 7. Short odd base cases

### `s=7`, `N=21`

`C21_S7_GLOBAL_OBSTRUCTION.md` exhausts all switching classes and proves the
stronger bound

\[
 \rho(A)^2\ge8+\frac{18}{131}.
\]

Since `18/131>1/70`, Theorem 3S holds here.

### `s=9`, `N=27`

`verify_c27_s9_all_signings.py` gives a prefix-pruned exact exhaustive
certificate.  Hamilton gauge has

\[
 2\cdot8^9=268,435,456
\]

triangle-state/holonomy representatives.  Quantitative prefix pruning at
margin `1/70` leaves `1064` length-eight prefixes.  Their eight extensions in
both holonomy sectors require only

\[
 2\cdot1064\cdot8=17,024
\]

final cyclic exact checks.  All pruning and final certificates verify

\[
 70\,w^T(A^2-8I)w\ge w^Tw>0.
\]

Thus (1) holds for `s=9` as well.

Combining Sections 5--7 proves Theorem 3S for every odd `s>=7`.

## 8. Consequences

The project now has two complementary phenomena.

### Continuous/jump-parameter side

Every integer jump `s>=2` has an explicit periodic Bloch family below
`sqrt(8)` with

\[
 s^2(8-\widehat R_s)\to\pi^2.
\]

### Finite arithmetic side

On the infinite resonance line

\[
 N=3s,\qquad s\ge7\text{ odd},
\]

**every** finite signing remains a fixed positive distance above `sqrt(8)`:

\[
 \rho(A)^2\ge8+\frac1{70}.
\]

Thus finite-order passage is not merely sampling the periodic Bloch edge.  The
short odd chord cycles create a robust arithmetic/topological obstruction.

## 9. Next directions

1. Determine the exact values or large-`s` asymptotics of `m(3s,s)`.
2. Classify other short odd chord-cycle lengths
   `L=N/gcd(N,s)` by width-`L` strip methods.
3. Seek a hand matrix inequality replacing the exact nine-column state
   certificate.
4. Formalize the signed-triangle trace argument and finite-state certificate
   interface in Lean.
5. Compare the finite strip mechanism with magnetic/flux-phase operator
   literature before making priority claims.

Unlike the explicit Bloch-family theorems, Theorem 3S is an all-signing
partial classification result for the finite minimization problem.
