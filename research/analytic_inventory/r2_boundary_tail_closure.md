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

## Tail lemma

The exact response recurrence has a limit \(S_\infty\), and

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

## Proof of (3)

The proof uses the recurrence, not numerical convergence.  Split the tail
into:

1. the bulk pivot error \(X_j-X_*\), controlled by the Riccati contraction;
2. the left and right response products \(R_j,W_j\), controlled by the
   dual \(Q\)-metric;
3. the quadratic increments in \(G,H,C\);
4. the fixed terminal correction \(W_{m-1}^{\rm total}=W_{m-1}+E_{m-1}\).

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

The quadratic Schur increments in \(G,H,C\) are bounded by a constant
multiple of \((3\cdot10^{-5})^2q^{2h}\).  Even using the crude factor
\(3\cdot12^2\) for the inverse and odd-step transfer, their geometric tail
is below \(10^{-10}\).  Finally, because \(31/60<2/3\), (5) gives a
terminal pivot error below \(2\cdot10^{-10}/125000\); after multiplication
by the fixed boundary matrices and inverse bounds this is below \(10^{-9}\).
Thus

\[
\|S_m-S_\infty\|_2<\frac1{10000}<\frac1{2000}
\qquad(m\ge102),
\]

which establishes (3).  All constants above are rational upper bounds; no
floating difference between large finite cores is used.

## Residue-two theorem

For every \(n=8k+2\ge50\), the standard one-G6 signing satisfies

\[
198I-25A_n^2\succ0.
\]

For \(50\le n<410\), this follows from the exact six-by-six boundary base
and the analytic bulk-pivot theorem.  For \(n\ge410\), it follows from
(1)--(3).  Hence

\[
\rho(A_n)^2<\frac{198}{25}<\rho_-(n)^2.
\]

The final strict benchmark comparison holds at \(n=50\) by
\(\cos t>1-t^2/2\) and \(\pi^2<10\), and remains true because
\(\rho_-(n)^2\) increases with even \(n\).

## Status

`ANALYTIC_TAIL_DRAFT_PENDING_LINE_AUDIT`.  The proof has replaced the
former unbounded LDL family by a local contraction, a response recurrence,
an exact finite boundary base, and a geometric tail.  It must receive a
separate line audit before being promoted into a manuscript theorem.
