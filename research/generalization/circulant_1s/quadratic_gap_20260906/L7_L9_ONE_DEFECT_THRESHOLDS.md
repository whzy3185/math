# Exact one-defect thresholds on the `L=7` and `L=9` resonance lines

Date: 2026-09-07.

> **Correction / supersession (2026-09-07).** The `s=2L` extrapolation that
> originally appeared at the end of this note is **false in general**.
> `L13_ONE_DEFECT_THRESHOLD_AND_STAIRCASE.md` gives an exact counterexample:
> at `L=13,s=27=2L+1` the favorable one-defect signing is still strictly
> sub-`sqrt(8)`, and its first certified failure is `s=29=2L+3`.
> The `L=7` and `L=9` theorems below remain valid exactly as stated.

This note extends `L5_ONE_DEFECT_THRESHOLD.md`.  It studies the canonical
near-alternating one-defect Hamilton family on `N=Ls`, with odd `L,s`.
It is a theorem about this explicit family, not an all-signing classification
of `m(Ls,s)`.

Use

\[
 \tau_i=\varepsilon(-1)^i,
 \qquad \varepsilon\in\{+1,-1\},
\]

with Hamilton holonomy `alpha=+/-1`.  The anchor `epsilon=-1` is the favorable
unbalanced chord-cycle sector at short orders.

## Theorem 7S

For `epsilon=-1`, `alpha=+1`,

\[
 \boxed{\rho(A)^2<8
 \quad\text{for }s=3,5,7,9,11,13.}
\]

For every odd `s>=15` and every one-defect sector,

\[
 \boxed{\rho(A)^2\ge8+\frac1{142}>8.}
\]

The short side is certified by exact rational LDL decomposition of
`8I-A^2`.  The minimum pivots are

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

For the long side, the fixed `14=2L` seam columns give a `98`-vertex local
matrix independent of odd `s>=15`.  In each sector an exact integer witness
satisfies

\[
 w^Tw=8,998,304,
 \qquad
 w^T(B^2-8I)w=63,800,
\]

and `142*63800 > 8,998,304`.

## Theorem 9S

For `epsilon=-1`, `alpha=+1`,

\[
 \boxed{\rho(A)^2<8
 \quad\text{for }s=3,5,7,9,11,13,15,17.}
\]

For every odd `s>=19` and every one-defect sector,

\[
 \boxed{\rho(A)^2\ge8+\frac1{652}>8.}
\]

The exact LDL verifier certifies all eight short cases.  At `s=17` the
smallest pivot is

\[
 \frac{661429367031989408053870728278961032}
 {4948147491252480043132928167652746337}>0.
\]

For the long side, the fixed `18=2L` seam columns give a `162`-vertex local
matrix.  Exact integer witnesses satisfy

\[
 w^Tw=9,003,536,
 \qquad
 w^T(B^2-8I)w=13,818,
\]

and `652*13818 > 9,003,536`.

## What remains true about the small-`L` pattern

For the four rigorously treated values `L=3,5,7,9`, the favorable canonical
one-defect family happens to be sub-eight through `s=2L-1` and super-eight
from `s=2L+1` onward.  This is a valid finite list of theorems.

It must **not** be promoted to a theorem or conjecture for every odd `L`.
The exact `L=13` counterexample shows that the critical integer begins to
move to the right.  The corrected general problem is to determine the
critical staircase and its large-`L` limiting ratio using the endpoint
reduction in `ONE_DEFECT_ENDPOINT_REDUCTION.md`.

## Scope relative to global minimization

For `L=5,7,9`, it remains open whether multi-defect signings can stay below
`sqrt(8)` after the canonical one-defect threshold.  Only the `L=3` line is
currently classified over all signings.

The exact verifier for this note is
`verify_l7_l9_one_defect_thresholds.py`.
