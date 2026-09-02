# A self-contained Fourier proof of the twisted benchmark

## Proposition

For even \(n\ge8\), the anti-periodic twisted signing of \(C_n(1,2)\) has

\[
\rho_-(n)^2
=4+2\cos\frac{2\pi}{n}+2\cos\frac{4\pi}{n}.
\tag{1}
\]

## Gauge form

Put \(\phi=\pi/n\), let \(R\) be the cyclic shift, and let
\(D=\operatorname{diag}((-1)^j)_{j=0}^{n-1}\).  In Hamilton gauge the
twisted class has \(\tau_j=(-1)^j\) and anti-periodic boundary
\(x_{j+n}=-x_j\).  Write

\[
x_j=e^{i\phi j}y_j,
\]

so that \(y_{j+n}=y_j\).  Substitution in

\[
(Ax)_j=x_{j-1}+x_{j+1}+\tau_{j-2}x_{j-2}+\tau_jx_{j+2}
\]

gives the Hermitian periodic-coordinate representative

\[
A_\phi=e^{i\phi}R+e^{-i\phi}R^*
+e^{2i\phi}DR^2+e^{-2i\phi}R^{-2}D.
\tag{2}
\]

The phase change is unitary, so (2) has the same spectrum as the real
twisted signed adjacency matrix.

## Fourier blocks

For \(f_k(j)=n^{-1/2}e^{2\pi ikj/n}\), put
\(\theta_k=2\pi k/n\).  Because \(Df_k=f_{k+n/2}\), the plane
\(\langle f_k,f_{k+n/2}\rangle\) is invariant.  On it, (2) is

\[
\begin{pmatrix}
2\cos(\theta_k+\phi)&2\cos(2\theta_k+2\phi)\\
2\cos(2\theta_k+2\phi)&-2\cos(\theta_k+\phi)
\end{pmatrix}.
\tag{3}
\]

Its eigenvalues are

\[
\pm2\sqrt{g(\theta_k+\phi)},\qquad
g(t)=\cos^2t+\cos^2(2t).
\tag{4}
\]

Thus the squared spectral radius is four times the maximum of \(g\) over
the shifted grid \(t=(2k+1)\pi/n\).

## Correct maximization on the shifted grid

By the symmetries \(g(-t)=g(t)=g(\pi-t)\), reduce every grid point to
\(t\in[\pi/n,\pi/2]\).  Set \(u=\cos^2t\).  Then

\[
g(t)=4u^2-3u+1.
\tag{5}
\]

If \(t\in[\pi/6,\pi/2]\), then \(0\le u\le3/4\), whence \(g(t)\le1\).
For \(0<t\le\pi/6\),

\[
g'(t)=-\sin(2t)\bigl(1+4\cos(2t)\bigr)<0.
\tag{6}
\]

Finally \(n\ge8\) gives \(\pi/n\le\pi/8<\pi/6\), and

\[
g(\pi/n)\ge g(\pi/8)=\frac{4+\sqrt2}{4}>1.
\]

Therefore the maximum on the shifted grid occurs at \(t=\pi/n\).  Expanding
\(4g(\pi/n)\) gives (1).

## Evidence boundary

This is an analytic Fourier calculation.  It replaces the inherited
benchmark formula in the article proof line.  The companion verifier checks
the displayed block and polynomial identities but is not used as a proof.
