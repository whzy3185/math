# Period-eight counterexample family: analytic derivation draft

## Status

This is a hand-checkable derivation target extracted from the local period-8
operator.  The operator, its determinant identity, and the inequalities below
have been recomputed symbolically in the local environment.  Before use in a
manuscript, the determinant reduction must receive a line-by-line human
check; no JSON audit is cited as proof here.

## Proposition (draft)

For every multiple \(n=8L\geq32\), there is a signing of \(C_n(1,2)\)
with

\[
 \rho(A)^2<\frac{1561}{200}<\rho_-(n)^2.
\]

Consequently the twisted signing is not spectrally optimal at every such
order.

## Periodic operator

Use Hamilton gauge and the period-eight triangle-flux word

\[
 (\tau_0,\ldots,\tau_7)=(1,1,-1,1,-1,-1,1,-1).
\]

Away from the cyclic seam the signed operator is

\[
 (Ax)_i=x_{i-1}+x_{i+1}+\tau_{i-2}x_{i-2}+\tau_i x_{i+2}.
\]

For the cell ansatz \(x_{8m+r}=z^m v_r\), the Floquet block is

\[
H(z)=
\begin{pmatrix}
0&1&1&0&0&0&z^{-1}&z^{-1}\\
1&0&1&1&0&0&0&-z^{-1}\\
1&1&0&1&-1&0&0&0\\
0&1&1&0&1&1&0&0\\
0&0&-1&1&0&1&-1&0\\
0&0&0&1&1&0&1&-1\\
z&0&0&0&-1&1&0&1\\
z&-z&0&0&0&-1&1&0
\end{pmatrix}.
\]

For \(|z|=1\), this matrix is Hermitian.  Direct determinant expansion,
followed by division by \(z^2\), gives

\[
 \det(xI-H(z))=P(x^2,z+z^{-1}),
\]
where

\[
P(y,c)=y^4-16y^3+(80-2c)y^2+(-128+16c)y+c^2-13c+38.
\]

The remaining presentation task is to record a short row-elimination proof
of this displayed determinant, rather than delegating the equality to a CAS.

## Uniform spectral bound

Put \(B=1561/200\).  For \(u\geq0\), direct expansion gives

\[
\begin{aligned}
P(B+u,2)={}&u^4+\frac{761}{50}u^3
+\frac{1337363}{20000}u^2\\
&+\frac{136311081}{2000000}u
+\frac{84332641}{1600000000}>0.
\end{aligned}
\]

Moreover

\[
 \partial_cP(y,c)=2c-2y^2+16y-13
 =2\left(c-y^2+8y-\frac{13}{2}\right).
\]

For \(y\geq B\) and \(c\leq2\), this derivative is negative, since

\[
 B^2-8B+\frac{13}{2}=\frac{199121}{40000}>2
\]

and the left-hand quadratic is increasing for \(y>4\).  Hence

\[
 P(y,c)\geq P(y,2)>0\qquad(y\geq B,\; -2\leq c\leq2).
\]

Thus every squared Floquet eigenvalue is strictly smaller than \(B\).

## Passage to finite rings

For \(n=8L\), the two cyclic holonomies correspond to the finite Bloch
sets \(z^L=\alpha\), where \(\alpha\in\{\pm1\}\).  Every such \(z\)
has \(|z|=1\), so the preceding uniform bound yields

\[
 \rho(A_{8L,\alpha})^2<B.
\]

Finally,

\[
 \rho_-(n)^2=4+2\cos\frac{2\pi}{n}+2\cos\frac{4\pi}{n}
\]

is increasing for \(n\geq8\).  The Taylor lower bound at \(n=32\), using
\(9<\pi^2<10\), gives

\[
 \rho_-(32)^2>
 \frac{1178731111}{150994944}>
 \frac{1561}{200}=B.
\]

Therefore \(B<\rho_-(n)^2\) for every \(n=8L\geq32\), which proves the
draft proposition.

## Why this matters

This result is a candidate main-text theorem for Route B.  It gives an
infinite, explicit, analytic counterexample family without using the 96-row
LDL bridge, finite-state equality machinery, or the G6 physical-branch
atlas.  It does not determine the complete truth pattern or the minimum
spectral radius at any failing order.
