# Exact `L=13` one-defect threshold and correction to the `s=2L` pattern

Date: 2026-09-07.

This note corrects the finite-`L` pattern suggested by the exact
`L=3,5,7,9` calculations.  The canonical one-defect transition is **not**
uniformly located at `s=2L`.

Let `L=13`, let `s>=3` be odd, and put `N=13s`.  In Hamilton gauge use

\[
 \tau_i=\varepsilon(-1)^i,
 \qquad \varepsilon\in\{\pm1\},
\]

with Hamilton holonomy `alpha=+/-1`.

## Theorem 13S — exact one-defect threshold

For the favorable unbalanced chord-cycle sector

\[
 \varepsilon=-1,\qquad \alpha=+1,
\]

one has

\[
 \boxed{\rho(A)^2<8
 \quad\text{for every odd }3\le s\le27.}
 \tag{1}
\]

For every odd `s>=29` and every one-defect sector
`(epsilon,alpha) in {+/-1}^2`,

\[
 \boxed{
 \rho(A)^2\ge8+\frac1{940}>8.}
 \tag{2}
\]

Thus the canonical favorable one-defect family changes side between

\[
 s=27=2L+1
 \quad\text{and}\quad
 s=29=2L+3.
\tag{3}
\]

In particular, the earlier extrapolation

\[
 s>2L\Longrightarrow\rho(A)^2>8
\]

from `L=3,5,7,9` is false.

## 1. Exact positive side via the endpoint reduction

For `s=2r+1>=5`, use the exact `4L`-dimensional Schur complement

\[
 \mathcal S_{13,r}^{-1,+1}
\]

from `ONE_DEFECT_ENDPOINT_REDUCTION.md`.  Since all eliminated interior
blocks are positive definite,

\[
 8I-A^2>0
 \iff
 \mathcal S_{13,r}^{-1,+1}>0.
\]

The verifier `verify_l13_one_defect_threshold.py` performs an exact rational
LDL decomposition of this `52 x 52` matrix for every odd

\[
 s=5,7,\ldots,27.
\]

Every pivot is positive.  At the last positive case `s=27`, the smallest
pivot is the final pivot and equals

\[
\frac{
34711137558517051035049506742633767044754656503383368699339387762158670526312117126114217676759647131272965735829546682764
}{
2482320805271566909283500776197027191081146597946554058884007825707214591259782947192296754738102759532913467542825416748387
}>0.
\tag{4}
\]

The short case `s=3` is checked directly by exact LDL on the full
`39 x 39` threshold matrix.  This proves (1).

For scale intuition only,

\[
 \rho(A)^2\approx7.9998962586
\]

at `(L,s)=(13,27)`.  The theorem does not rely on this floating number.

## 2. A fixed 28-column seam obstruction from `s=29`

For odd `s>=29`, take the cyclic columns

\[
 s-14,s-13,\ldots,s-1,
 0,1,\ldots,13.
\tag{5}
\]

They are `28=2L+2` distinct columns and contain `364` vertices.  For each
fixed `(epsilon,alpha)`, the induced signed adjacency matrix is literally
independent of the odd integer `s>=29`: the parity pattern of the columns,
the chord signs, and the unique helical seam matching are unchanged.

Let `B_(epsilon,alpha)` be this fixed local adjacency.  A floating eigensolver
is used only to propose an integer vector `w`; exact integer multiplication
then verifies, in all four sectors,

\[
 w^Tw=65756,
 \qquad
 w^T(B^2-8I)w=70.
\tag{6}
\]

Since

\[
 940\cdot70=65800\ge65756,
\]

we obtain the exact local Rayleigh inequality

\[
 \frac{w^TB^2w}{w^Tw}
 \ge8+\frac1{940}.
\tag{7}
\]

Extending `w` by zero to the full graph proves (2).

The actual local excess is larger than `1/940`; the clean rational constant
is chosen only to make the certificate concise.

## 3. Exact endpoint sign flip at `s=27/29`

The endpoint reduction also gives a compact exact certificate of the
transition.  For `epsilon=-1, alpha=+1`:

- at `s=27`, all 52 rational LDL pivots are positive;
- at `s=29`, exactly one endpoint LDL pivot is negative.

By Schur-complement inertia equivalence, the full threshold matrix therefore
has zero negative eigenvalues at `s=27` and one negative eigenvalue at
`s=29`.

This is an exact sign change, not a numerical near-zero ambiguity.

## 4. Corrected resonance picture

The proven one-defect thresholds now begin

\[
\begin{array}{c|c|c}
L & \text{last proved favorable }s & \text{first uniform failure }s\\ \hline
3&5&7\\
5&9&11\\
7&13&15\\
9&17&19\\
13&27&29.
\end{array}
\tag{8}
\]

The first four rows accidentally fit the simple law `s=2L`.  The fifth row
does not.

Using the exact endpoint reduction, numerical scans for larger odd `L` show a
staircase in the critical integer `s`.  Interpolating the smallest endpoint
eigenvalue between adjacent integer `r=(s-1)/2` values suggests a limiting
critical ratio near

\[
 \frac{s_c(L)}L\approx2.0974.
\tag{9}
\]

Equation (9) is **numerical/observed only**.  It is not used in any theorem.
The analytic problem is now to derive the limiting scattering/Robin equation
of the `4L` endpoint matrix as `L,r->infinity` with `r/L` fixed.

## 5. Supersession

The `One-defect aspect-ratio conjecture` recorded at the end of
`L7_L9_ONE_DEFECT_THRESHOLDS.md` is superseded and disproved by Theorem 13S.
The exact `L=3,5,7,9` theorems in that note remain valid.

The new working conjecture is only the weaker statement that a limiting
critical ratio exists for the favorable one-defect family.  Its value and
characterizing equation remain open.
