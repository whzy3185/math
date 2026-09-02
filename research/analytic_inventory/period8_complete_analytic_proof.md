# A complete analytic proof of the period-eight counterexample family

## Theorem

For every integer \(L\ge4\), put \(n=8L\).  There is a signing of
\(C_n(1,2)\) such that

\[
\rho(A)^2<\frac{1561}{200}<\rho_-(n)^2.
\]

Hence the twisted signing is not spectrally optimal for every multiple of
eight at least \(32\).

## Proof

Use Hamilton gauge and the period-eight triangle-flux word

\[
(\tau_0,\ldots,\tau_7)=(1,1,-1,1,-1,-1,1,-1).
\]

Thus, on the infinite periodic lift,

\[
(Ax)_i=x_{i-1}+x_{i+1}+\tau_{i-2}x_{i-2}+\tau_i x_{i+2}.
\tag{1}
\]

For either finite holonomy \(\alpha\in\{\pm1\}\), impose
\(x_{i+n}=\alpha x_i\).  The block Fourier ansatz
\(x_{8m+r}=z^m v_r\) has \(z^L=\alpha\), hence \(|z|=1\), and converts
(1) into the Hermitian matrix

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
\tag{2}
\]

Choose \(\xi\) with \(\xi^2=z\), let \(T_4(z)\) translate a cell by four
sites, and put \(D=\operatorname{diag}((-1)^r)_{r=0}^7\).  A direct
inspection of (2) gives

\[
J_z=\xi^{-1}DT_4(z),\qquad J_z^2=I,\qquad J_zH(z)=-H(z)J_z.
\tag{3}
\]

In the \(\pm1\)-eigenspace decomposition of \(J_z\),

\[
H(z)=\begin{pmatrix}0&B\\C&0\end{pmatrix}.
\]

Writing \(s=\xi+\xi^{-1}\), the product \(BC\) has diagonal blocks
\((4-s)I_2\), \((4+s)I_2\), and off-diagonal blocks

\[
Q=\begin{pmatrix}1+\xi^{-1}&2\\2&1-\xi^{-1}\end{pmatrix},
\qquad
R=\begin{pmatrix}1+\xi&2\\2&1-\xi\end{pmatrix}.
\]

The block determinant identity gives

\[
\det(yI_4-BC)=
\det\!\left(((y-4)^2-s^2)I_2-RQ\right).
\]

Expanding the displayed two-by-two determinant gives

\[
\det(yI_4-BC)=P(y,c),\qquad c=\xi^2+\xi^{-2},
\tag{4}
\]

where

\[
P(y,c)=y^4-16y^3+(80-2c)y^2+(-128+16c)y+c^2-13c+38.
\]

Equation (3) shows that the spectrum of \(H(z)\) is symmetric about zero,
and (4) therefore gives the characteristic equation for its squared
eigenvalues.  Since \(|z|=1\), we have \(c\in[-2,2]\).

Set \(B_0=1561/200\).  For \(y\ge B_0\),

\[
\partial_cP(y,c)=2c-2y^2+16y-13<0
\qquad(-2\le c\le2),
\]

because \(y^2-8y+13/2\) is increasing for \(y>4\) and takes the value
\(199121/40000>2\) at \(B_0\).  Hence
\(P(y,c)\ge P(y,2)\).  With \(u=y-B_0\ge0\),

\[
\begin{aligned}
P(B_0+u,2)={}&u^4+\frac{761}{50}u^3
+\frac{1337363}{20000}u^2\\
&+\frac{136311081}{2000000}u
+\frac{84332641}{1600000000}>0.
\end{aligned}
\]

Thus no squared eigenvalue of any allowed Floquet block is at least \(B_0\),
so

\[
\rho(A)^2<B_0.
\tag{5}
\]

Finally,

\[
\rho_-(n)^2=4+2\cos\frac{2\pi}{n}+2\cos\frac{4\pi}{n}
\]

is increasing for \(n\ge8\).  At \(n=32\), apply

\[
\cos t>1-\frac{t^2}{2}+\frac{t^4}{24}-\frac{t^6}{720}
\qquad(0<t<1)
\]

to \(t=\pi/16\) and \(t=\pi/8\), using \(9<\pi^2<10\) in the
favourable directions.  This gives

\[
\rho_-(32)^2>
\frac{1178731111}{150994944}>
\frac{1561}{200}=B_0.
\tag{6}
\]

Monotonicity extends (6) to every \(n=8L\ge32\).  Combining (5) and (6)
proves the theorem. \(\square\)

## Boundary of this theorem

The theorem proves one infinite counterexample family.  It does not classify
all signings at these orders, determine \(m_n\), or settle any nonzero
residue class modulo eight.
