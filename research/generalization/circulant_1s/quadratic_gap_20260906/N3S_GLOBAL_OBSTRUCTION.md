# A uniform all-signing obstruction on the resonance line `N=3s`

Date: 2026-09-06.

This note upgrades the finite-order analysis from isolated examples and
one-defect families to an infinite all-signing theorem.

## 1. Main theorem

Let `s>=7` be odd and let `A_sigma` be the signed adjacency matrix of an
arbitrary edge signing of

\[
 C_{3s}(1,s).
\]

**Theorem 3S.** For every odd `s>=7` and every signing `sigma`,

\[
 \boxed{
 \rho(A_\sigma)^2\ge 8+\frac1{1038}>8.}
 \tag{1}
\]

Consequently, if `m(N,s)` denotes the minimum signed spectral radius over all
edge signings of `C_N(1,s)`, then

\[
 \boxed{
 m(3s,s)^2\ge8+\frac1{1038}
 \qquad(s\ge7\text{ odd}).}
 \tag{2}
\]

Thus the line `N=3s` is a genuine arithmetic obstruction family.  This is not
merely a period-compatibility failure of the alternating construction: no
edge signing can enter the sub-`sqrt(8)` regime.

The proof has one finite computer-assisted lemma with exact integer witnesses,
plus a structural signed-triangle argument.  The two short base cases
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
off-diagonal entries in `{+1,-1}`.  Hence there are exactly eight possible
column states.

Between columns `j` and `j+1` for `0<=j<s-1`, the step-one edges give the
identity matching `I_3`.  The closing matching from column `s-1` to column
`0` is an orthogonal signed cyclic permutation `S_alpha`.

For fixed `alpha`, the map from the `3s` Hamilton-gauge chord signs to the
sequence

\[
 (B_0,\ldots,B_{s-1})
\]

is bijective: the three edge signs of each triangle are independent.  Thus
this width-three model represents every switching class.

## 3. Exact nine-column local rule

Consider an open chain of nine signed-triangle columns

\[
 M(B_0,\ldots,B_8)=
 \begin{pmatrix}
 B_0&I&&&&\\
 I&B_1&I&&&\\
 &I&B_2&\ddots&&\\
 &&\ddots&\ddots&I&\\
 &&&I&B_8
 \end{pmatrix}.
\]

`verify_triangle_strip_local_rule.py` proves the following finite statement.

**Lemma 3S-L (nine-column rule).** For every choice of the eight-state
triangle word `(B_0,...,B_8)`, either

\[
 \|M\|^2\ge8+\frac1{1038},
 \tag{3}
\]

or the six middle transitions satisfy

\[
 \boxed{
 B_{j+1}=-B_j\qquad(j=1,2,\ldots,6).}
 \tag{4}
\]

### Exact certification boundary

The verifier does not trust floating eigenvalues for a pruning decision.
Starting from the eight one-column states, it extends words recursively.
Whenever a prefix is pruned, a floating eigensolver merely proposes an
integer vector `w`; the script then checks exactly

\[
 w^T(M^2-8I)w>0
\]

and, cross-multiplied over the integers,

\[
 1038\,w^T(M^2-8I)w\ge w^Tw.
\tag{5}
\]

The numbers of unpruned prefixes at lengths `1,...,9` are

\[
 8,56,152,440,488,704,656,968,128.
\tag{6}
\]

Every one of the final 128 survivors satisfies (4).  Therefore any
nine-column word violating (4) was removed by an exact prefix witness and
obeys (3).  Floating arithmetic can only fail to propose a witness and leave
an extra survivor; it cannot make the exact inequality (5) pass falsely.

This is the only finite-state computer-assisted ingredient needed for all
odd `s>=11`.

## 4. Straightening a window across the helical seam

Take any nine consecutive cyclic columns of `C_(3s)(1,s)`.  When `s>=11`,
these nine columns form a proper open principal subgraph: at least two columns
remain outside the window.

If the window does not cross the Hamilton seam, its intercolumn matchings are
already `I_3`, so Lemma 3S-L applies directly.

If it crosses the seam, its unique exceptional matching is the orthogonal
signed permutation `S_alpha`.  Since the window is an open chain, conjugate
all columns after that matching by the same signed permutation
`S_alpha^T`.  This changes the seam matching to `I_3` and leaves every later
matching equal to `I_3`.  Conjugation by a signed permutation maps a signed
triangle to another signed triangle, so Lemma 3S-L again applies without
changing the operator norm.

Thus every nine-column cyclic window has the same dichotomy: either it already
carries the local margin (3), or its six middle transitions alternate after
the obvious seam straightening.

## 5. If no local witness exists, all bulk triangle states alternate

Assume, toward a contradiction, that

\[
 \rho(A_\sigma)^2<8+\frac1{1038}.
 \tag{7}
\]

Then no nine-column principal window can satisfy (3), since compression
cannot increase operator norm.  Hence every such window obeys the alternating
rule (4).

Choose windows so that each ordinary transition `j -> j+1`,
`0<=j<s-1`, appears as one of the six middle transitions.  If a chosen window
crosses the seam elsewhere, both columns of the ordinary transition receive
the same signed-permutation conjugation, so the relation transforms back
unchanged.  Therefore

\[
 \boxed{B_{j+1}=-B_j\qquad(0\le j<s-1).}
 \tag{8}
\]

Since `s` is odd, `s-1` is even, and (8) gives

\[
 B_{s-1}=B_0.
 \tag{9}
\]

Now choose a nine-column window in which the helical seam itself is one of the
middle transitions.  Straightening its matching as in Section 4 and applying
(4) gives

\[
 S_\alpha B_0S_\alpha^T=-B_{s-1}=-B_0
 \tag{10}
\]

(up to replacing `S_alpha` by its transpose, which is immaterial below).

## 6. A signed triangle cannot be orthogonally similar to its negative

For a signed triangle `B`, let its three edge signs be `u,v,w`.  A direct
three-step closed-walk count gives

\[
 \operatorname{tr}(B^3)=6uvw\in\{+6,-6\}.
 \tag{11}
\]

Orthogonal similarity preserves `tr(B^3)`, while

\[
 \operatorname{tr}((-B)^3)=-\operatorname{tr}(B^3).
\]

Therefore no signed triangle is orthogonally similar to its negative.
Equation (10) is impossible.

This contradiction proves (1) for every odd `s>=11`.

Equivalently, one may use the two possible triangle spectra

\[
 \{2,-1,-1\},\qquad\{-2,1,1\},
\]

which are exchanged rather than preserved by `B -> -B`.

## 7. The two short odd cases

The nine-column sliding argument requires a proper nine-column window, so the
short resonance cases are certified separately.

### `s=7`, `N=21`

`C21_S7_GLOBAL_OBSTRUCTION.md` exhausts all switching classes (after rotation
reduction) and proves the stronger bound

\[
 \rho(A)^2\ge8+\frac{18}{131}.
\]

### `s=9`, `N=27`

`verify_c27_s9_all_signings.py` gives a pruned exact exhaustive certificate.
After Hamilton gauge there are

\[
 2\cdot8^9=268,435,456
\]

triangle-state/holonomy representatives.  Exact open-prefix witnesses reduce
the only unresolved length-eight prefixes to 968; their eight final
extensions are checked in both holonomy sectors, so only

\[
 2\cdot968\cdot8=15,488
\]

full cyclic matrices require final certification.  Every pruning and final
certificate obeys the uniform exact margin `1/1038`.

Thus (1) also holds for `s=7,9`, completing the proof for every odd `s>=7`.

## 8. Consequences

The project now has two qualitatively different sharp statements.

### Continuous/jump-parameter side

For every integer jump `s>=2`, the parity-dependent explicit periodic family
has Bloch edge below `sqrt(8)` and

\[
 s^2(8-\widehat R_s)\to\pi^2.
\]

### Finite arithmetic side

For the infinite resonance line

\[
 N=3s,\qquad s\ge7\text{ odd},
\]

**every** finite signing remains uniformly above `sqrt(8)` by (1).

Hence passage from the periodic Bloch problem to a finite circulant is not a
mere sampling issue.  The arithmetic topology of the chord cycles can create
a robust spectral obstruction that no signing removes.

## 9. Next research directions

1. Determine the exact values `m(3s,s)` or their large-`s` asymptotics.
2. Classify other short odd chord-cycle lengths
   `L=N/gcd(N,s)` using the same finite-state strip method.
3. Identify whether `L=5,7,...` have all-signing obstruction subfamilies or
   only defeat low-defect constructions.
4. Replace the exact 9-column finite-state lemma by a hand proof, if a compact
   matrix inequality can be found.
5. Formalize the eight-state local lemma and the signed-triangle trace
   obstruction in Lean.

Theorem 3S is a theorem about all signings; unlike the preceding explicit
Bloch-family results, it is a genuine partial classification result for the
finite minimization problem.
