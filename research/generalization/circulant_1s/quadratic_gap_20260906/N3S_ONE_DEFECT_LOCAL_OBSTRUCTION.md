# A uniform local obstruction for the one-defect family on `C_(3s)(1,s)`

Date: 2026-09-06.

This note turns the strongest seam-safe resonance seen in
`ODD_ORDER_RESONANCE_MAP.md` into an analytic finite-family theorem.  It is a
theorem about the **one-defect near-alternating Hamilton word**, not about all
signings.  The exceptional pair `(21,7)` has the stronger all-signing theorem
in `C21_S7_GLOBAL_OBSTRUCTION.md`.

## 1. Statement

Let `s>=7` be odd and `N=3s`.  In Hamilton gauge choose

\[
 \tau_i=\varepsilon(-1)^i,
 \qquad \varepsilon\in\{+1,-1\},
\]

and let the Hamilton holonomy be

\[
 \alpha\in\{+1,-1\}.
\]

Because `N` is odd, the cyclic flux word `Q_i=tau_i tau_(i+1)` has one
positive defect at the closing seam; this is the canonical one-defect repair
of the infinite period-two odd-jump signing.

Let `A_(s,epsilon,alpha)` be the corresponding seam-safe signed adjacency
matrix of `C_(3s)(1,s)`.

**Theorem 3S-1.** For every odd `s>=7` and every `epsilon,alpha`,

\[
 \boxed{
 \rho(A_{s,\varepsilon,\alpha})^2
 \ge \frac{193}{24}
 =8+\frac1{24}>8.}
 \tag{1}
\]

Thus the one-defect family fails uniformly throughout the resonance line
`N=3s`.

The proof is local: a fixed 18-vertex principal submatrix already has operator
norm squared at least `193/24`.

## 2. Width-three coordinates

Write every vertex uniquely as

\[
 i=j+a s,
 \qquad
 0\le j<s,\quad a\in\{0,1,2\}.
\]

For fixed `j`, the three vertices

\[
 j,\quad j+s,\quad j+2s
\]

form a triangle under the `s`-chords because `3s=N`.  Hence `C_(3s)(1,s)` is
naturally a cyclic strip of width three:

- each column `j` carries a signed triangle;
- step-one edges couple neighboring columns;
- the transition from column `s-1` to column `0` is helical in the `a`
  coordinate and carries the Hamilton holonomy on the final wrap.

For the one-defect word,

\[
 \tau_{j+a s}
 =\varepsilon(-1)^{j+a}
\tag{2}
\]

because `s` is odd.  Thus the signed triangle pattern depends only on the
parity of `j`, not on the magnitude of `s`.

## 3. A fixed six-column window

Take the six cyclic columns

\[
 s-3,\ s-2,\ s-1,\ 0,\ 1,\ 2.
\tag{3}
\]

Since `s>=7`, these are six distinct columns and no unwanted short-column
collision occurs.  Order their 18 vertices column-by-column, with the three
`a=0,1,2` vertices inside each column.

Let `B_(epsilon,alpha)` be the principal 18-by-18 signed adjacency matrix on
this vertex set.

The key observation is:

**Lemma 3S-2 (local stability).** For fixed `epsilon,alpha`, the matrix
`B_(epsilon,alpha)` is literally independent of the odd integer `s>=7`.

### Proof

Only two kinds of graph edges can remain inside the six-column set.

1. **Chord edges.** They stay inside one column.  By (2), their signs depend
   only on `epsilon`, `alpha`, the layer `a`, and the parity of the column.
   The parity pattern of (3) is

   \[
   \text{even},\text{odd},\text{even},
   \text{even},\text{odd},\text{even}
   \]

   for every odd `s`.

2. **Step-one edges.** Away from the cyclic cut they give the same identity
   matching between adjacent columns.  The edge from column `s-1` to column
   `0` gives the same helical matching for every `s`; the single total
   Hamilton wrap is weighted by the fixed sector `alpha`.

No other edge type exists in `C_N(1,s)`.  Since the six columns are distinct
for `s>=7`, this determines the induced matrix and proves the claim.

The companion verifier checks the literal matrix equality for several larger
odd `s` as an indexing regression, but the lemma itself is the structural
argument above.

## 4. Four exact integer witnesses

For the four sectors `(epsilon,alpha)`, use the following integer vectors in
the 18-vertex order of Section 3:

| `(epsilon,alpha)` | witness `w` |
|---|---|
| `(+1,+1)` | `(-1,1,1, 1,0,-1, -3,1,3, -3,3,1, 1,-1,0, -1,1,1)` |
| `(+1,-1)` | `(-1,-1,1, -1,0,1, -3,-1,3, -3,-3,1, -1,-1,0, -1,-1,1)` |
| `(-1,+1)` | `(1,-1,-1, 1,0,-1, 3,-1,-3, -3,3,1, -1,1,0, -1,1,1)` |
| `(-1,-1)` | `(1,1,-1, -1,0,1, 3,1,-3, -3,-3,1, 1,1,0, -1,-1,1)` |

A direct integer multiplication gives in every sector

\[
 w^Tw=48
\tag{4}
\]

and

\[
 w^T(B^2-8I)w=2.
\tag{5}
\]

Therefore

\[
 \frac{w^TB^2w}{w^Tw}
 =8+\frac2{48}
 =\frac{193}{24}.
\tag{6}
\]

Since `B` is real symmetric,

\[
 \|B\|^2\ge\frac{193}{24}.
\]

The four calculations (4)--(5) are exactly reproduced by
`verify_n3s_one_defect_local_obstruction.py`; no floating arithmetic is used
for the certificate.

## 5. Passage from the local block to the full graph

A principal compression cannot increase the operator norm:

\[
 \|B\|\le\|A\|.
\]

Equivalently, extend the local witness `w` by zero to all `3s` vertices.  If
`P` denotes the projection to the 18-vertex window, then `B=PAP`, and

\[
 \|Aw\|^2
 \ge \|PAw\|^2
 =\|Bw\|^2.
\]

Hence

\[
 \rho(A)^2=\|A\|^2
 \ge\|B\|^2
 \ge\frac{193}{24},
\]

which proves Theorem 3S-1.

## 6. Meaning of the obstruction

This theorem identifies a concrete mechanism behind the `N=3s` resonance:
the closing defect is already visible in a bounded-width neighborhood of the
helical seam.  Increasing `s` does not dilute that local configuration, so
the one-defect family remains a fixed distance above the `sqrt(8)` threshold.

This differs sharply from the continuous odd-jump period-two model, where the
Bloch gap is asymptotically `pi^2/s^2` below `8`.  The finite odd ring cannot
simply inherit that word with one parity defect when the chord cycles are
triangles.

## 7. Scope and next step

Theorem 3S-1 does **not** prove that every signing of `C_(3s)(1,s)` has
spectral radius above `sqrt(8)`.  At `s=7` the stronger all-signing result is
known by exhaustive exact certification.  For `s=9,11,...`, a multi-defect
word might in principle remove the local seam configuration.

The next structural target is therefore one of the following:

1. prove an all-signing `N=3s` obstruction by showing that every signed
   width-three triangular strip contains one of finitely many bad local
   patterns;
2. find a counterexample multi-defect signing below `sqrt(8)` for some
   `s>=9`;
3. formulate the problem as a finite-state transfer/forbidden-pattern
   classification on signed triangle columns.

The local theorem makes option 3 especially natural: the global finite-order
problem has been reduced from arbitrary edge signs to the interaction of a
small set of column states and helical transition states.
