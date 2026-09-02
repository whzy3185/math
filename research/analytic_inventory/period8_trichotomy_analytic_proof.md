# Period-eight sub-eight trichotomy

## Theorem

Let \(Q\) be a legal eight-periodic quadrilateral-flux word and let
\(R(Q)\) be the supremum of the squared spectral radius over its Bloch
fibers.  Put

\[
\eta=4+\sqrt{10+2\sqrt5}.
\]

Then exactly one of the following holds:

\[
\begin{array}{c|c}
Q\text{-type}&R(Q)\\ \hline
Q=(-)^8&8\\
\{i:Q_i=+1\}=\{j,j+4\}&\eta<8\\
\text{all other legal }Q&>8.
\end{array}
\]

Thus the antipodal two-defect phase is the unique sub-eight period-eight
phase, up to cyclic translation, reflection, and the two lifts.

## Proof

Legality is \(\prod_iQ_i=1\), so the defect number
\(d=\#\{i:Q_i=1\}\) is even.  Hence \(d\in\{0,2,4,6,8\}\).

### Zero defects

If \(d=0\), then \(\tau_i=(-1)^i\) after choosing a lift.  With
\(C=S+S^{-1}\), \(E=S^2+S^{-2}\), and
\(D=\operatorname{diag}((-1)^i)\), one has

\[
A=C+DE,\qquad CD=-DC,\qquad ED=DE.
\]

Therefore

\[
A^2=4I+S^2+S^{-2}+S^4+S^{-4}.
\]

Its unit-circle symbol is
\(4+2\cos(2\theta)+2\cos(4\theta)\le8\), with equality at
\(\theta=0\).  Thus \(R(Q)=8\).

### Four or more defects

Let \(a\) and \(b\) count positive-flux pairs at cyclic distances one and
two.  Directly from the local row of \(A^2\),

\[
M_1=32,\qquad M_2=160+16d,
\qquad M_3=944+168d+96a+48b.
\]

If \(R(Q)\le8\), phase averaging of squared Bloch eigenvalues gives
\(M_{k+1}\le8M_k\).  Hence

\[
F_2:=M_3-8M_2=-336+40d+96a+48b\le0.
\tag{1}
\]

For \(d=4\), the four cyclic positive gaps sum to eight.  If there are at
least two unit gaps, then \(2a\ge4\).  If there are no unit gaps, all gaps
are two, so \(b=4\).  If there is one unit gap, the remaining gaps are
\(2,2,3\), so \(2a+b=4\).  In all cases \(2a+b\ge4\), and

\[
F_2=-176+48(2a+b)>0.
\]

For \(d=6\), the two negative sites destroy at most four cyclic adjacent
positive-positive pairs, so \(a\ge4\), whence \(F_2>0\).  For \(d=8\),
\(M_2-8M_1=32>0\).  Thus every legal phase with \(d\ge4\) has \(R(Q)>8\).

### Two defects

Up to dihedral symmetry, place the two positive entries at \(0\) and
\(s\), with \(s\in\{1,2,3,4\}\).  For each \(s<4\), the table gives a
single Bloch fiber and an integer vector \(v\) satisfying
\(v^{\mathsf T}H(z)^2v/\|v\|^2>8\):

\[
\begin{array}{c|c|c|c}
s&z&v&\text{Rayleigh quotient}\\ \hline
1&1&(-1,-1,-1,-1,-1,-1,-1,-1)&72/8\\
2&-1&(-1,-1,-1,0,-1,-1,-1,1)&60/7\\
3&1&(-1,-1,-1,0,-1,-1,-1,-1)&60/7
\end{array}
\]

Each quotient follows by multiplying the explicit eight-by-eight Bloch
matrix arising from the local signing rule.  Thus \(R(Q)>8\) for
\(s=1,2,3\).

For \(s=4\), the flux is the period-eight target phase
\((+---)^2\).  The chiral Floquet calculation in
`period8_complete_analytic_proof.md` gives \(R(Q)=\eta<8\).

The cases exhaust all legal eight-periodic phases, proving the theorem.
