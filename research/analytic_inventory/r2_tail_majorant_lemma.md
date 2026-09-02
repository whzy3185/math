# Residue-two tail majorant lemma (draft for line audit)

## Statement

Let \(S_m\) be the six-by-six cyclic core from the exact response recurrence
for the one-G6 residue-two signing.  For \(m=2k\) even and \(m\ge102\), the
intended bound is

\[
\|S_m-S_\infty\|_2<10^{-6}.
\tag{T}
\]

This document supplies explicit majorants for the four terms in the
recurrence.  It is a proof draft, not a promoted theorem, until a separate
line audit validates the coordinate/norm conversions.

## Exact entrance and local regime

After 24 single block eliminations, the pivot is exactly \(X_{12}\), because
the couplings alternate \(E_+,E_-\) and the two-step map is
\(\Phi=F_-\circ F_+\).  The exact verifier proves

\[
R_{24}QR_{24}^{\mathsf T}\prec10^{-10}I_2,
\qquad
W_{24}^{\mathsf T}QW_{24}\prec10^{-10}I_4,
\tag{E1}
\]

where \(Q\succeq9I/10\).  Hence

\[
\|R_{24}\|_2,\ \|W_{24}\|_2<\frac{1}{3}\,10^{-4}.
\tag{E2}

The local dual transfer bound is \(\|L(X)\|_Q<2/3\).  Thus after \(h\)
complete two-cell transfers,

\[
\|R_h\|_2,\ \|W_h\|_2<\frac13\,10^{-4}\left(\frac23\right)^h.
\tag{E3}

The odd intermediate map has norm at most \(12\), so the following single
block has the deliberately weaker but parity-free bound

\[
\|R\|_2,\ \|W\|_2<4\cdot10^{-4}\left(\frac23\right)^h.
\tag{E4}

All local pivot inverses satisfy \(\|X^{-1}\|_2\le3\).

## Schur-series tails

Write the three accumulated entries as

\[
\begin{aligned}
G_m&=G_0-\sum_{j<m}R_jX_j^{-1}R_j^{\mathsf T},\\
H_m&=H_0-\sum_{j<m}W_j^{\mathsf T}X_j^{-1}W_j
\quad\text{with the terminal correction below},\\
C_m&=C_0-\sum_{j<m}R_jX_j^{-1}W_j.
\end{aligned}
\tag{S}
\]

The terminal correction is

\[
(W_{m-1}+E_+)^{\mathsf T}X_{m-1}^{-1}(W_{m-1}+E_+),
\tag{B}
\]

because \(m-1\) is odd for every residue-two chain.

At \(m=102\), the terminal is at least 38 complete two-cell transfers past
the entrance.  Put \(q=2/3\).  From (E4), each quadratic Schur increment in
the remaining tail has norm at most

\[
3(4\cdot10^{-4})^2q^{2h}=\frac{48}{10^8}q^{2h}.
\]

Summing from \(h=38\),

\[
\sum_{h\ge38}\frac{48}{10^8}q^{2h}
\le\frac{48}{10^8}\frac{q^{76}}{1-q^2}
<10^{-18}.
\tag{Q}
\]

The terminal cross term in (B) has norm at most

\[
2\|E_+\|_F\|X^{-1}\|_2\|W_{m-1}\|_2
<24\cdot4\cdot10^{-4}q^{38}<10^{-9}.
\tag{C}
\]

## Pivot-limit term

The Riccati contraction gives

\[
\|X_j-X_*\|_2
\le 2\cdot10^{-10}\left(\frac{31}{60}\right)^h.
\]

Since \(\|X^{-1}-X_*^{-1}\|_2\le9\|X-X_*\|_2\), the fixed terminal
quadratic form in (B) changes by less than

\[
\|E_+\|_F^2\,9\cdot2\cdot10^{-10}
\left(\frac{31}{60}\right)^{38}<10^{-16}.
\tag{P}
\]

The same estimate dominates the pivot differences inside the already
quadratically decaying series.

Combining (Q), (C), and (P), and using the block norm bound
\(\|\left(\begin{smallmatrix}G&C\\C^T&H\end{smallmatrix}\right)\|_2
\le\|G\|_2+2\|C\|_2+\|H\|_2\), yields (T) with substantial slack.

## Audit boundary

The estimates deliberately exceed what is needed.  The only nontrivial
audit obligations are:

1. verify that the response entrance index and terminal index give the
   stated 38 complete transfers at \(m=102\);
2. verify the norm conversion from the dual \(Q\)-metric to (E3);
3. verify the stated single-step factor 12 for both alternating parities;
4. verify the fixed terminal coupling is always \(E_+\).

Until those four checks are independently replayed, (T) remains an analytic
draft rather than a manuscript theorem.
