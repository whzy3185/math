# A general periodic defect obstruction

## Theorem

Let \(\tau\) have period \(p\), set

\[
Q_i=\tau_i\tau_{i+1},\qquad
d=\#\{i:Q_i=1\},
\]

and let \(a,b\) count positive \(Q\)-pairs at cyclic distances one and two.
Write

\[
R_p(\tau)=\sup_{|z|=1}\lambda_{\max}(H(z)^2)
\]

for its squared Bloch spectral edge.  For the phase-averaged even Floquet
moments
For the phase-averaged even Floquet moments

\[
M_k=\frac1{2\pi}\int_0^{2\pi}
\operatorname{tr}\bigl(H(e^{it})^{2k}\bigr)\,dt,
\]

one has

\[
M_1=4p,\qquad
M_2=20p+16d,\qquad
M_3=118p+168d+96a+48b.
\tag{1}
\]

If \(R_p(\tau)\le8\), then

\[
d\le\frac{3p}{4},\qquad
40d+96a+48b\le42p.
\tag{2}
\]

## Proof

The local square has the displacement coefficients

\[
\begin{array}{c|ccccccccc}
\text{displacement}&-4&-3&-2&-1&0&1&2&3&4\\ \hline
A_\tau^2&Q_{i-4}Q_{i-3}&\tau_{i-3}(1+Q_{i-3})&1&
\tau_{i-2}(1+Q_{i-2})&4&
\tau_{i-1}(1+Q_{i-1})&1&
\tau_i(1+Q_i)&Q_iQ_{i+1}.
\end{array}
\tag{3}
\]

It follows directly by multiplying the four allowed transitions.  The
diagonal of \(A_\tau^2\) is \(4\), proving the first formula.  Squaring the
row in (3) gives

\[
(A_\tau^4)_{ii}
=28+2(Q_{i-3}+Q_{i-2}+Q_{i-1}+Q_i).
\]

After summation, \(M_2=28p+8\sum_iQ_i=20p+16d\).

For \(M_3\), the exact rooted length-six closed-walk catalogue has 430
words.  Its complete nonzero monomial table is

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

The entries sum to \(430\).  Grouping this table by translate gives

\[
M_3=238p+156\sum_iQ_i+
24\sum_iQ_iQ_{i+1}+12\sum_iQ_iQ_{i+2}.
\tag{4}
\]

This is a finite integer expansion of (3), not a floating-point calculation.
With \(Q_i=2I_i-1\), the three sums in (4) become \(2d-p\),
\(4a-4d+p\), and \(4b-4d+p\), proving (1).

Finally, every Floquet squared eigenvalue \(y\) satisfies
\(0\le y\le8\) under the assumed edge bound.  Hence \(y^{k+1}\le8y^k\);
averaging yields \(M_{k+1}\le8M_k\).  The cases \(k=1,2\), together with
(1), are exactly the two inequalities in (2). \(\square\)

## Article role

This theorem is the general form of the local cancellation mechanism.  The
period-eight trichotomy is its first sharp application, not its hypothesis.
It should occupy a short final technical section after the infinite
counterexample theorem.
