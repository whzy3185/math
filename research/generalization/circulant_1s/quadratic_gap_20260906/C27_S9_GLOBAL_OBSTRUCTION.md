# Exact all-signing obstruction for `C_27(1,9)`

Date: 2026-09-06.

This is the short base case needed by `N3S_GLOBAL_OBSTRUCTION.md` before the
sliding nine-column argument becomes available.

## Theorem 27

For every edge signing `sigma` of `C_27(1,9)`,

\[
 \boxed{
 \rho(A_\sigma)^2\ge8+\frac1{70}.}
\]

The proof is a finite exact computer-assisted certificate with prefix pruning.

## Hamilton-gauge population

After switching along the step-one Hamilton cycle, retain its holonomy

\[
 \alpha\in\{+1,-1\}.
\]

Since `27=3*9`, reorder vertices into nine columns of three vertices.  The
nine chord triangles are arbitrary signed triangles, so each column has 8
states.  For fixed `alpha`, the 27 chord signs are in bijection with the
`8^9` triangle-state words.

Thus the full Hamilton-gauge population is

\[
 2\cdot8^9=268,435,456.
\]

## Exact prefix pruning

For an open prefix matrix `M`, define

\[
 K=M^2-8I.
\]

A candidate prefix is eliminated only when an integer vector `w` verifies

\[
 \boxed{70\,w^TKw\ge w^Tw>0.}
\tag{1}
\]

This implies `||M||^2>=8+1/70`; since `M` is a principal compression of every
extension, no extension of that prefix can beat the target.

A floating eigensolver is used only to propose a direction to round.  The
pruning decision is equation (1), evaluated over integers.

At margin `1/70`, the unpruned prefix counts at lengths `1,...,8` are

\[
 8,56,152,440,488,1016,656,1064.
\]

Hence only `1064` length-eight prefixes require extension.

## Final cyclic checks

Each surviving length-eight prefix has eight ninth states and two holonomy
sectors.  Therefore only

\[
 2\cdot1064\cdot8=17,024
\]

full cyclic matrices reach the final stage.

For every one, the verifier again finds an integer vector satisfying

\[
 70\,w^T(A^2-8I)w\ge w^Tw>0.
\]

This proves the theorem for every representative not already eliminated by a
prefix witness, and prefix compression proves it for all the eliminated
families.

The complete population `2*8^9` is therefore covered.

## Reproducibility

The executable certificate is

`verify_c27_s9_all_signings.py`.

Its correctness boundary is one-sided and exact:

- floating error may fail to propose a useful witness and make the script
  stop at an assertion;
- floating error cannot make the integer inequality (1) true when it is
  false.

Thus a successful run is an exact certificate for the stated finite
population.

## Relation to the infinite theorem

For `s>=11` odd, the same `1/70` margin comes from the nine-column local rule
plus the signed-triangle seam contradiction.  The pair `(27,9)` is too short
for a proper nine-column sliding window, so this pruned exhaustive theorem is
used as a separate base case.  The other short base case `(21,7)` has the
stronger bound `8+18/131`.
