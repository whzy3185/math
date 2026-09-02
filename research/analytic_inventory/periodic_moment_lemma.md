# Periodic moment barrier: analytic lemma target

## Purpose

The period-eight construction should not appear as an unexplained lucky
pattern.  This note isolates the low-moment mechanism that rules out many
periodic competitors before any Floquet determinant is considered.

## Setup

For a periodic triangle-flux word \(\tau\), set

\[
Q_i=\tau_i\tau_{i+1},\qquad
d=\#\{i:Q_i=1\},
\]

and let \(a\) and \(b\) count pairs of positive \(Q\)-sites at cyclic
distance one and two, respectively.  For a period \(p\) Bloch operator
\(H(z)\), define the phase-averaged even moments

\[
M_k=\operatorname{CT}_z\operatorname{tr}(H(z)^{2k}).
\]

## Candidate lemma

For every legal period word,

\[
M_1=4p,
\qquad M_2=20p+16d,
\qquad M_3=118p+168d+96a+48b.
\]

If every squared Bloch eigenvalue is at most \(8\), then

\[
d\le \frac{3p}{4},
\qquad
40d+96a+48b\le42p.
\]

Indeed, under the spectral bound, \(y^{k+1}\le8y^k\) for every squared
eigenvalue \(y\in[0,8]\), hence \(M_{k+1}\le8M_k\).  Substitution gives
the two displayed necessary inequalities.

## Hand-proof route

The required local identity is

\[
\begin{array}{c|ccccccccc}
\text{displacement}&-4&-3&-2&-1&0&1&2&3&4\\ \hline
A_\tau^2&Q_{i-4}Q_{i-3}&\tau_{i-3}(1+Q_{i-3})&1&
\tau_{i-2}(1+Q_{i-2})&4&
\tau_{i-1}(1+Q_{i-1})&1&
\tau_i(1+Q_i)&Q_iQ_{i+1}
\end{array}
\]

It follows by multiplying the four allowed one-step transitions.  The
second and third moment formulas should then be derived by taking the
diagonal of \(A^4\) and \(A^6\), grouping translates, and replacing
\(Q_i\) by \(2I_i-1\).  This is the preferred manuscript proof.  A
computer enumeration of closed walks may cross-check the coefficients but
does not replace this calculation.

### Direct fourth-moment calculation

The \(A^4\) identity is already completely local.  Since

\[
(A^4)_{ii}=\sum_j(A^2_{ij})^2,
\]

the two displacement-four and two displacement-two terms contribute
\(2+2\), the diagonal term contributes \(16\), and the four odd-distance
terms contribute

\[
2(1+Q_{i-3})+2(1+Q_i)
+2(1+Q_{i-2})+2(1+Q_{i-1}).
\]

Thus

\[
(A^4)_{ii}=28+2(Q_{i-3}+Q_{i-2}+Q_{i-1}+Q_i).
\]

Summing over a period gives

\[
M_2=28p+8\sum_iQ_i=20p+16d.
\]

This part requires no walk enumeration or symbolic computation.

### Complete sixth-moment catalogue

For \(M_3\), enumerate the 430 rooted step words of length six in
\(\{-2,-1,1,2\}\) with total displacement zero.  A \(\pm2\) step toggles the
triangle variable at its departing (for \(+2\)) or arriving (for \(-2\))
site.  Pairing the remaining triangle variables in increasing order replaces
them by the intervening \(Q\)-intervals.  The resulting rooted catalogue is
the following complete 20-row table; an empty support means the monomial
\(1\).

\[
\begin{array}{c|rrrrrrrrr}
\text{support}&\varnothing&-5&-4&-3&-2&-1&0&1&2\\ \hline
\text{coefficient}&238&2&4&34&38&38&34&4&2
\end{array}
\]

\[
\begin{array}{c|rrrrrrrrrrr}
\text{support}&-5,-3&-4,-3&-4,-2&-3,-2&-3,-1&
-2,-1&-2,0&-1,0&-1,1&0,1&0,2\\ \hline
\text{coefficient}&2&4&2&4&2&8&2&4&2&4&2
\end{array}
\]

The entries sum to \(430\).  On summing over every root, all singleton
translates have total coefficient \(156\), adjacent pairs total \(24\), and
distance-two pairs total \(12\).  Thus

\[
M_3=238p+156\sum_iQ_i+
24\sum_iQ_iQ_{i+1}+12\sum_iQ_iQ_{i+2}.
\tag{2}
\]

Writing \(Q_i=2I_i-1\) gives

\[
\sum_iQ_i=2d-p,\quad
\sum_iQ_iQ_{i+1}=4a-4d+p,\quad
\sum_iQ_iQ_{i+2}=4b-4d+p.
\]

Substitution into (2) yields

\[
M_3=118p+168d+96a+48b.
\]

This is a finite combinatorial table, not a floating-point or spectral
calculation.  In a manuscript it may sit in a compact appendix; the
fourth-moment derivation and the subsequent barrier argument remain in the
main text.

## Scope

The inequalities are necessary only.  They do not prove that a word below
the two barriers has spectral edge at most eight, and they do not establish
global optimality of the period-eight word.  Their article role is structural:
they explain why high defect density and short defect clustering are forced
above the eight barrier.
