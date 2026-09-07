# Exact one-defect thresholds on the `L=7` and `L=9` resonance lines

Date: 2026-09-07.

This note extends `L5_ONE_DEFECT_THRESHOLD.md`.  It studies the canonical
near-alternating one-defect Hamilton family on

\[
 N=Ls,
\]

where `L` and `s` are odd.  The results below are complete for this explicit
family at `L=7` and `L=9`; they are not all-signing classifications of
`m(Ls,s)`.

Use

\[
 \tau_i=\varepsilon(-1)^i,
 \qquad \varepsilon\in\{+1,-1\},
\]

with Hamilton holonomy `alpha=+/-1`.  Since `N` is odd, the cyclic flux word
has one positive defect.  The anchor `epsilon=-1` is the unbalanced chord-cycle
sector and is the favorable short-order branch.

## Theorem 7S — exact one-defect threshold for `L=7`

For `epsilon=-1`, `alpha=+1`,

\[
 \boxed{\rho(A)^2<8
 \quad\text{for }s=3,5,7,9,11,13.}
 \tag{7.1}
\]

For every odd `s>=15` and every sector `(epsilon,alpha)`,

\[
 \boxed{
 \rho(A)^2\ge8+\frac1{142}>8.}
 \tag{7.2}
\]

Thus the canonical one-defect family changes side exactly between
`s=13=2L-1` and `s=15=2L+1`.

### Exact short positive certificates

For each short `s`, form `C=8I-A^2`.  Exact rational LDL decomposition gives
all-positive pivots.  The smallest pivot is

\[
\begin{array}{c|c}
 s & \min D_i \\ \hline
3&1007944/425541\\
5&2277788536/1454491811\\
7&5743822061896/5195865110761\\
9&14193384596521976/18465671512818127\\
11&30328484575097105032/64565507942151155669\\
13&620621017574070249992/3470219944037939379421.
\end{array}
\]

### Fixed 14-column obstruction

For odd `s>=15`, take the `14=2L` columns

\[
 s-7,\ldots,s-1,0,1,\ldots,6.
\]

They give a `98`-vertex principal matrix independent of `s` in each of the
four `(epsilon,alpha)` sectors.  A floating eigensolver is used only to
propose an integer vector; exact arithmetic then verifies in every sector

\[
 w^Tw=8,998,304,
 \qquad
 w^T(B^2-8I)w=63,800.
\]

Since

\[
 142\cdot63800=9,059,600>8,998,304,
\]

the exact Rayleigh excess is at least `1/142`, proving (7.2).

## Theorem 9S — exact one-defect threshold for `L=9`

For `epsilon=-1`, `alpha=+1`,

\[
 \boxed{\rho(A)^2<8
 \quad\text{for }s=3,5,7,9,11,13,15,17.}
 \tag{9.1}
\]

For every odd `s>=19` and every sector `(epsilon,alpha)`,

\[
 \boxed{
 \rho(A)^2\ge8+\frac1{652}>8.}
 \tag{9.2}
\]

Again the transition occurs precisely between `2L-1` and `2L+1`.

The exact LDL verifier checks positivity for all eight short cases.  The
smallest pivot remains positive at `s=17`; it is

\[
 \frac{661429367031989408053870728278961032}
 {4948147491252480043132928167652746337}.
\]

For the long side, the fixed `18=2L` seam columns give a `162`-vertex local
matrix.  In all four sectors a rounded witness is accepted only after exact
integer verification of

\[
 w^Tw=9,003,536,
 \qquad
 w^T(B^2-8I)w=13,818.
\]

Since

\[
 652\cdot13818=9,009,336>9,003,536,
\]

the exact local excess is at least `1/652`, proving (9.2).

## A stable `s=2L` transition pattern

Together with the earlier rigorous cases, the one-defect thresholds are now

\[
\begin{array}{c|c|c}
L & \rho^2<8\text{ proved through} & \rho^2>8\text{ proved from}\\ \hline
3 & s=5 & s=7\\
5 & s=9 & s=11\\
7 & s=13 & s=15\\
9 & s=17 & s=19.
\end{array}
\]

Thus in every proved odd chord-cycle length,

\[
 \boxed{
 s\le2L-1\Rightarrow\text{the favorable one-defect signing is sub-eight},
 }
\]

while

\[
 \boxed{
 s\ge2L+1\Rightarrow\text{every canonical one-defect sector is super-eight}.
 }
\]

This motivates the following explicit next conjecture.

**One-defect aspect-ratio conjecture.** For every odd `L>=3`, the favorable
canonical one-defect signing on `C_(Ls)(1,s)` is sub-`sqrt(8)` exactly for odd
`s<2L`, and every one-defect sector is super-`sqrt(8)` for odd `s>2L`.

The current proof is finite-in-`L`: the short side is exact LDL and the long
side is a fixed `2L`-column local Rayleigh certificate.  A general proof should
explain why the seam-localized mode crosses the threshold exactly at aspect
ratio `s/L=2`.

## Scope relative to global minimization

The theorem is about the canonical one-defect family only.  In particular,
for `L=5,7,9` it remains open whether a multi-defect signing can stay below
`sqrt(8)` after the one-defect threshold.  The `L=3` line is exceptional in
that an all-signing obstruction theorem is already proved.

The exact verifier is `verify_l7_l9_one_defect_thresholds.py`.
