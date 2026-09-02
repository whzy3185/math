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

## Scope

The inequalities are necessary only.  They do not prove that a word below
the two barriers has spectral edge at most eight, and they do not establish
global optimality of the period-eight word.  Their article role is structural:
they explain why high defect density and short defect clustering are forced
above the eight barrier.
