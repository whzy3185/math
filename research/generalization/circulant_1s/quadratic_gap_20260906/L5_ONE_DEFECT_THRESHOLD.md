# Exact threshold for the canonical one-defect family on `C_(5s)(1,s)`

Date: 2026-09-07.

This note advances the finite resonance analysis from chord-cycle length
`L=3` to `L=5`.  It is a complete theorem for the canonical one-defect
near-alternating family.  It is **not** yet an all-signing classification of
`m(5s,s)`.

Throughout let `s>=3` be odd and `N=5s`.  In Hamilton gauge take

\[
 \tau_i=\varepsilon(-1)^i,
 \qquad \varepsilon\in\{+1,-1\},
\]

with Hamilton holonomy `alpha=+/-1`.  Since `N` is odd, the cyclic flux word
`Q_i=tau_i tau_(i+1)` has exactly one positive defect.  The two values of
`epsilon` are genuinely different on `N=5s`: they give opposite flux on each
odd chord 5-cycle.

## Theorem 5S-1 — one-defect phase transition

For the unbalanced-anchor sector `epsilon=-1`, `alpha=+1`,

\[
 \boxed{\rho(A)^2<8\qquad s\in\{3,5,7,9\}.}
 \tag{1}
\]

For every odd `s>=11`, every one-defect sector
`(epsilon,alpha) in {+/-1}^2` satisfies

\[
 \boxed{
 \rho(A)^2\ge 8+\frac1{34}>8.}
 \tag{2}
\]

Consequently the canonical one-defect repair works on

\[
 C_{15}(1,3),\ C_{25}(1,5),\ C_{35}(1,7),\ C_{45}(1,9),
\]

but fails uniformly from `C_55(1,11)` onward along the line `N=5s`.

This theorem is exact.  The short positive cases use rational LDL/Sylvester
certificates; the long negative side uses fixed integer Rayleigh witnesses on
a bounded seam window.

## 1. Width-five strip coordinates

Write

\[
 i=j+a s,
 \qquad 0\le j<s,\quad a\in\{0,1,2,3,4\}.
\]

For fixed `j`, the `s`-chords form a signed 5-cycle.  Since `s` is odd,

\[
 \tau_{j+a s}=\varepsilon(-1)^{j+a}.
 \tag{3}
\]

Hence ordinary neighboring column blocks alternate in sign.  The defect is
concentrated at the helical seam from column `s-1` to column `0`.

The anchor `epsilon=-1` flips all five signs of a chord 5-cycle and therefore
flips its switching-invariant cycle product.  This explains why the two
anchors are not spectrally equivalent on the odd chord cycles.

## 2. Exact positive certificates for `s=3,5,7,9`

Fix `epsilon=-1`, `alpha=+1` and form the exact integer matrix

\[
 C_s=8I-A_s^2.
\]

The verifier `verify_l5_one_defect_threshold.py` computes an exact rational
LDL decomposition without pivoting.  Every diagonal pivot is positive in the
four cases.  The smallest pivot is the final one and equals

\[
\begin{array}{c|c}
 s & \min D_i \\ \hline
 3 & 2872/1207\\
 5 & 5534344/3695961\\
 7 & 1076085176/1260574219\\
 9 & 6825469384/26186660017.
\end{array}
\tag{4}
\]

Thus `C_s` is positive definite by Sylvester's criterion, so every squared
eigenvalue of the displayed signing is strictly below `8`.  This proves (1).

The shrinking final pivot in (4) is consistent with the transition to the
localized seam state above `8` at larger `s`, but that interpretation is not
used in the proof.

## 3. A fixed ten-column seam window for every `s>=11`

Take the ten cyclic columns

\[
 s-5,s-4,s-3,s-2,s-1,0,1,2,3,4.
 \tag{5}
\]

For odd `s>=11` these are ten distinct columns.  Ordered column-by-column,
with five layer vertices in each column, they give a 50-vertex principal
submatrix `B_(epsilon,alpha)`.

**Lemma 5S-2.** For fixed `(epsilon,alpha)`, this 50-by-50 signed matrix is
independent of the odd integer `s>=11`.

Indeed, (3) makes all chord signs depend only on the parity of `j`, the layer
`a`, and `epsilon`; the parity pattern of (5) is fixed for odd `s`.  Ordinary
step-one matchings are identical, while the unique seam matching has the same
width-five helical permutation and holonomy `alpha` for every `s`.

Thus only four fixed local matrices need certification.

## 4. Exact integer margin `1/34`

For each of the four sectors, the verifier stores an integer vector `w` on
the 50 vertices.  Exact multiplication gives in every case

\[
 w^Tw=25532,
 \qquad
 w^T(B^2-8I)w=752.
 \tag{6}
\]

Since

\[
 34\cdot752=25568\ge25532,
\]

we have

\[
 \frac{w^TB^2w}{w^Tw}
 =8+\frac{752}{25532}
 \ge8+\frac1{34}.
 \tag{7}
\]

Extending `w` by zero to the full graph yields

\[
 \rho(A)^2\ge\|B\|^2\ge8+\frac1{34},
\]

proving (2).

The approximate local squared norm is about `8.02999`; this floating value is
only descriptive.  The theorem uses the exact integer inequality (6)--(7).

## 5. What this says about the `L=5` resonance

The `L=3` line has an all-signing obstruction from odd `s=7` onward.  The
`L=5` line behaves differently already at the canonical near-alternating
level:

- the unbalanced chord-cycle anchor remains sub-eight through `s=9`;
- the one-defect seam creates a bounded localized obstruction from `s=11`
  onward.

Therefore a future all-signing classification of `m(5s,s)` cannot be obtained
by simply copying the `L=3` threshold or by ignoring the odd-cycle flux
sector.

The present theorem leaves open whether multi-defect signings can repair the
`L=5` resonance for `s>=11`.

## 6. Next finite target

The natural next question is

\[
 m(5s,s)<\sqrt8\ ?
\]

for odd `s>=11`.  A six/seven-column switching-invariant finite-state search
shows that the low-norm `L=5` automaton has a large recurrent component, so
the `L=3` proof does not collapse to a single forced alternation rule at short
range.  The likely next tools are:

1. a longer-window exact automaton with a global invariant;
2. an analytic width-five transfer/Riccati inequality;
3. an explicit multi-defect counterexample, if the all-signing obstruction is
   false.

No conclusion about all signings is asserted here.
