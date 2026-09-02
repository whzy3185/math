# Period-eight sub-eight trichotomy

## Theorem

For a legal eight-periodic quadrilateral-flux word \(Q\), let \(R(Q)\) be
the supremum of the squared spectral radius over its Bloch fibers and put
\(\eta=4+\sqrt{10+2\sqrt5}\).  Then

\[
R(Q)=\begin{cases}
8,&Q=(-)^8,\\
\eta<8,&\{i:Q_i=+1\}=\{j,j+4\}\text{ for some }j,\\
>8,&\text{otherwise}.
\end{cases}
\]

Thus the antipodal two-defect phase is the unique sub-eight period-eight
phase, up to cyclic translation, reflection, and the two lifts.

## Proof

Legality gives \(\prod_iQ_i=1\), so the defect number
\(d=\#\{i:Q_i=+1\}\) belongs to \(\{0,2,4,6,8\}\).

If \(d=0\), choose the lift \(\tau_i=(-1)^i\).  With
\(C=S+S^{-1}\), \(E=S^2+S^{-2}\), and
\(D=\operatorname{diag}((-1)^i)\), one has

\[
A=C+DE,\qquad CD=-DC,\qquad ED=DE,
\]

and hence

\[
A^2=4I+S^2+S^{-2}+S^4+S^{-4}.
\]

Its unit-circle symbol is
\(4+2\cos(2\theta)+2\cos(4\theta)\le8\), with equality at
\(\theta=0\).  Thus \(R(Q)=8\).

For all phases, let \(a\) and \(b\) count positive-flux pairs at cyclic
distances one and two.  The local closed-walk calculation gives

\[
M_1=32,\qquad M_2=160+16d,
\qquad M_3=944+168d+96a+48b.
\]

If \(R(Q)\le8\), phase averaging gives \(M_{k+1}\le8M_k\), so

\[
F_2:=M_3-8M_2=-336+40d+96a+48b\le0.
\tag{1}
\]

For \(d=4\), the four cyclic positive gaps sum to eight.  Their elementary
gap cases imply \(2a+b\ge4\); therefore
\(F_2=-176+48(2a+b)>0\).  For \(d=6\), the two negative sites destroy at
most four adjacent positive-positive edges, so \(a\ge4\) and \(F_2>0\).
For \(d=8\), \(M_2-8M_1=32>0\).  Hence all phases with \(d\ge4\) have
\(R(Q)>8\).

For \(d=2\), place the two positive entries at \(0\) and
\(s\in\{1,2,3,4\}\), up to dihedral symmetry.  The finite exact
closed-walk recurrence in `period8_two_defect_closed_walk_lemma.md` gives

\[
\begin{array}{c|c|c}
s&\text{first positive excess}&\text{value}\\ \hline
1&F_4=M_5-8M_4&5504\\
2&F_6=M_7-8M_6&64336\\
3&F_9=M_{10}-8M_9&2872096.
\end{array}
\]

Thus \(R(Q)>8\) for \(s=1,2,3\).  The values are exact integer
closed-walk counts, not numerical spectral estimates.  For \(s=4\), the
target Floquet proof in `period8_complete_analytic_proof.md` gives
\(R(Q)=\eta<8\).  The cases exhaust all legal phases.

## Evidence boundary

The zero-defect and high-defect parts are hand derivations.  The three
non-antipodal two-defect cases use a small exact closed-walk recurrence and
table; it should remain visible as a finite algebraic sublemma in any
manuscript or supplementary proof note.
