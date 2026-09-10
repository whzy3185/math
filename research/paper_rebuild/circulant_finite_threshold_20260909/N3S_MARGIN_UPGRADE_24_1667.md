# Quantitative upgrade on the odd `N=3s` obstruction

This note strengthens the uniform excess in the finite-global triangle-resonance theorem without changing its local-to-global mechanism.

## Theorem 1

For every odd integer `s>=7`,

\[
\boxed{
 m(3s,s)^2\ge 8+\frac{24}{1667}.
}
\tag{1}
\]

Numerically,

\[
\frac{24}{1667}=0.0143971205758848\ldots,
\]

which is strictly larger than the previously certified excess `2/139`.

The proof has the same three ingredients as the earlier obstruction theorem: the exact base cases `s=7,9`, a nine-column finite local rule, and the analytic seam contradiction for all odd `s>=11`.  Only the quantitative local certificate is strengthened.

---

## 1. The `s=7` base is already stronger

The exhaustive Hamilton-gauge certificate for `C_21(1,7)` proves

\[
m(21,7)^2\ge 8+\frac{18}{131}.
\]

Since

\[
\frac{18}{131}>\frac{24}{1667},
\]

this base case automatically satisfies (1).  The exact enumeration covers `49,940` admissible `Q`-necklaces and `199,760` Hamilton-gauge representatives.

---

## 2. Strengthened nine-column local rule

Let `M` be the signed adjacency matrix of a nine-column open width-three triangle strip.  A column is one of the eight signed triangle states, and adjacent columns are joined by the identity matching.

The exact pruning test now accepts a Rayleigh witness `w in Z^27` only when

\[
1667\,w^T(M^2-8I)w\ge24\,w^Tw>0.
\tag{2}
\]

A floating eigensolver is used only to propose a direction; the pruning decision itself is the integer inequality (2).

The survivor counts by prefix length are exactly

\[
\boxed{
8,56,152,440,488,1016,656,1064,128.
}
\tag{3}
\]

Every one of the 128 length-nine survivors satisfies

\[
B_{j+1}=-B_j,
\qquad j=1,\ldots,6,
\tag{4}
\]

for its six middle transitions.  Thus every nine-column word either already has squared spectral radius at least `8+24/1667`, or obeys the same forced alternation rule as before.

The complete exact integer check is reproduced by `verify_n3s_margin_24_1667.py`.

---

## 3. The `s=9` cyclic base

For `C_27(1,9)`, Hamilton gauge and width-three reordering encode every signing by a nine-letter triangle-state word and a Hamilton holonomy `alpha=+-1`.

Using the strengthened pruning test (2), the first eight prefix counts remain

\[
8,56,152,440,488,1016,656,1064.
\]

The 1,064 surviving length-eight prefixes have eight final extensions in each of the two holonomy sectors, giving

\[
2\cdot1064\cdot8=17,024
\]

full cyclic candidates.  Every one has an exact integer witness satisfying (2).  Together with the exactly pruned prefixes this covers all

\[
2\cdot8^9=268,435,456
\]

Hamilton-gauge representatives.  Hence

\[
\boxed{m(27,9)^2\ge8+\frac{24}{1667}.}
\tag{5}
\]

---

## 4. Propagation to every odd `s>=11`

Assume that an odd `s>=11` admitted a signing with

\[
\rho(A)^2<8+\frac{24}{1667}.
\]

Every consecutive nine-column window would then avoid the first alternative of the strengthened local rule, so (4) would hold on every window.  Sliding the window forces global alternation of the signed triangle blocks.

The pre-existing analytic seam argument is independent of the numerical value of the positive excess: after one circuit around an odd number of columns, global alternation forces the seam relation

\[
S B_0 S^T=-B_0.
\]

Taking cubes and traces gives

\[
\operatorname{tr}(B_0^3)=-\operatorname{tr}(B_0^3),
\]

whereas a signed triangle has

\[
\operatorname{tr}(B_0^3)=\pm6.
\]

This contradiction proves (1) for all odd `s>=11`.  Together with Sections 1--3 it proves Theorem 1. `square`

---

## Audit note on the numerical boundary

The old historical script at margin `1/70` used a shorter integer-rounding scale list.  Merely replacing its denominator by a stronger rational is not a valid certificate.  The present verifier enlarges the finite list of integer rounding scales and still accepts branches only through exact cross-multiplication.

A numerical search places the local nine-column transition near excess `0.014397239...`; this number is **Observed**, not used as a theorem.  The stated rational `24/1667` lies below that numerical boundary and is the strongest clean margin retained in the manuscript at this stage.