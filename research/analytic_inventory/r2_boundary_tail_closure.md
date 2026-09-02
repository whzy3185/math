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

## Tail lemma target

The desired conclusion is that the exact response recurrence has a limit
\(S_\infty\), with

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

This proves the residue-two family for \(n\ge410\).  The exact finite-base
verifier covers the remaining orders \(50\le n<410\) with \(n\equiv2
\pmod8\).

## Reduction of (3)

The proof uses the recurrence, not numerical convergence.  Split the tail
into:

1. the bulk pivot error \(X_j-X_*\), controlled by the Riccati contraction;
2. the left and right response products \(R_j,W_j\), controlled by the
   dual \(Q\)-metric;
3. the quadratic increments in \(G,H,C\);
4. the fixed terminal correction \(W_{m-1}^{\rm total}=W_{m-1}+E_{m-1}\).

For the residue-two family, \(m=2k\) is even.  Starting with the fixed
initial matrices \(R_0,W_0,X_0\), define the open-chain sequences by the
displayed response recurrence.  They are independent of the eventual chain
length.  The terminal core of a chain of length \(m\) is obtained by stopping
these sequences at \(j=m-1\) and replacing the final propagated response by
\(W_{m-1}+E_{m-1}\).  Since \(m-1\) is always odd, the terminal coupling has
one fixed parity.  This is the required reindexing: no parity subsequence is
being silently mixed in the limit.

Consequently \(G,H,C\) are partial sums of the convergent Schur series

\[
RX^{-1}R^{\mathsf T},\qquad
W^{\mathsf T}X^{-1}W,\qquad
RX^{-1}W,
\]

plus the fixed-parity terminal correction.  This defines \(S_\infty\).

After the exact 24-step entrance, the dual response bounds and the local
two-cell contraction give, with \(q=2/3\),

\[
\|R_j\|_2,\ \|W_j\|_2
\le 3\cdot10^{-5}q^h
\tag{4}
\]

after \(h\) complete two-cell transfers.  The factor \(3\cdot10^{-5}\)
uses only \(Q\succeq9I/10\) and the exact entrance inequalities.  The
odd intermediate step is bounded by \(\|X^{-1}E\|_2\le12\), which is
already absorbed in the deliberately loose constants below.

The local Riccati contraction similarly gives

\[
\|X_j-X_*\|_2\le2\cdot10^{-10}(31/60)^h.
\tag{5}
\]

At \(m=102\), at least \(h=38\) complete transfers separate the entrance
from the terminal core.  Since

\[
(2/3)^{38}<(2/3)^{30}<50^{-3}=\frac1{125000},
\tag{6}
\]

the terminal propagated response has norm below
\(3\cdot10^{-5}/125000<3\cdot10^{-10}\).  Consequently the linear
terminal cross term is bounded by

\[
2\|E\|_F\|X^{-1}\|_2\|W\|_2
<24\cdot3\cdot10^{-10}<10^{-8}.
\]

The remaining missing step is a **term-by-term majorant lemma**: it must
bound the difference between the actual pivot inverses and their limiting
two-cycle, then insert those bounds into every increment of \(G,H,C\).
The informal phrase “a constant multiple” is not a proof of this lemma.
Once its explicit rational constants have been supplied, the geometric-series
calculation above will imply (3).  No floating difference between large
finite cores may be used to supply the missing lemma.

## Conditional residue-two theorem

If (3) is proved, then the exact finite boundary base for
\(50\le n<410\), together with (1), gives

\[
198I-25A_{8k+2}^2\succ0\qquad(k\ge6).
\]

The benchmark comparison then yields
\(\rho(A_{8k+2})^2<198/25<\rho_-(8k+2)^2\).  This conditional statement is
recorded to make the final dependency explicit; it is not yet promoted to a
theorem.

## Status

`ANALYTIC_TAIL_MAJORANT_OPEN`.  The proof has reduced the former unbounded
LDL family to one finite-dimensional majorant lemma.  It must not be promoted
into a manuscript theorem until that lemma is explicit and independently
audited.
