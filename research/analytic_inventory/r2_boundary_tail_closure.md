# Residue-two boundary-tail closure: exact remaining lemma

## Seed

The exact Fraction-LDL computation gives

\[
S_{410}-\frac9{20}I_8\succ0.
\tag{1}
\]

Here \(410=8\cdot51+2\), so the block chain has \(m=102\) four-site
blocks.  This seed is preferred to the earlier order-250 seed because it
lies much deeper in the proved local response regime.

## Inputs already available

After 24 open-chain eliminations, exact rational checks give

\[
RQR^{\mathsf T}\prec10^{-10}I_2,
\qquad W^{\mathsf T}QW\prec10^{-10}I_4.
\tag{2}
\]

The local dual transfer theorem gives a two-cell contraction by \(2/3\) in
the associated response norm.  The terminal core at the seed is separated
from the entrance by at least 38 complete two-cell transfers.

## Lemma required for closure

Prove directly from the exact recurrence that the cores have a limit
\(S_\infty\) and that

\[
\|S_m-S_\infty\|_2<\frac1{2000}
\qquad(m\ge102).
\tag{3}
\]

Then (1) and (3) imply

\[
S_m\succeq\left(\frac9{20}-\frac1{2000}\right)I_8\succ0
\qquad(m\ge102).
\]

This proves the residue-two family for \(n\ge410\).  A finite exact check
would then cover the remaining orders \(50\le n<410\) with \(n\equiv2
\pmod8\).

## How (3) must be proved

The proof must use the recurrence, not numerical convergence.  Split the
tail into:

1. the bulk pivot error \(X_j-X_*\), controlled by the Riccati contraction;
2. the left and right response products \(R_j,W_j\), controlled by the
   dual \(Q\)-metric;
3. the quadratic increments in \(G,H,C\);
4. the fixed terminal correction \(W_{m-1}^{\rm total}=W_{m-1}+E_{m-1}\).

All fixed matrices have rational entries and bounded dimension.  The final
estimate may be deliberately crude, but every norm conversion and geometric
series constant must be displayed.  A floating difference between large
finite cores is discovery evidence only and cannot establish (3).

## Status

`OPEN_ANALYTIC_LEMMA`.  This is now the sole residue-two obstruction; it is
not silently replaced by the former order-by-order LDL table.
