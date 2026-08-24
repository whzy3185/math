# Candidate Attainment Lemma

Let $n\ge8$ be even and write the vertices of $C_n(1,2)$ as
$0,1,\ldots,n-1$. For $0\le i<n$, let $a_i$ be the sign on
$\{i,i+1\}$ and $b_i$ the sign on $\{i,i+2\}$, with indices reduced modulo
$n$. Define the signing $\sigma_n^-$ by

$$
a_i=\begin{cases}1,&0\le i\le n-2,\\-1,&i=n-1,\end{cases}
\qquad
b_i=\begin{cases}(-1)^i,&0\le i\le n-3,\\-1,&i=n-2,\\1,&i=n-1.
\end{cases}                                             \tag{1}
$$

Thus the step-one Hamilton-cycle holonomy is $-1$. The triangle based at
$i$ has flux

$$
\tau_i=a_i a_{i+1}b_i=(-1)^i,                            \tag{2}
$$

so (1) is the tree-gauge representative of the distinguished alternating
triangle-flux, negative-holonomy class.

Equivalently, its quadrilateral fluxes and holonomy satisfy $Q_i=-1$ and
$\alpha=-1$ for every $i$.

**Lemma (exact attainment).** For every even $n\ge8$, the signed adjacency
matrix $A_n^-=A_{\sigma_n^-}$ satisfies

$$
\rho(A_n^-)^2
=4\cos^2\frac{\pi}{n}+4\cos^2\frac{2\pi}{n}
=4+2\cos\frac{2\pi}{n}+2\cos\frac{4\pi}{n}
=\rho_-(n)^2.                                           \tag{3}
$$

In particular, if $m_n=\min_\sigma\rho(A_\sigma)$, then

$$
m_n\le\rho_-(n)                                         \tag{4}
$$

at every even order $n\ge8$.

## Proof

It is convenient to realise (1) as a periodic operator with a twisted
boundary condition. Let

$$
\mathcal U_n^-=
\{u:\mathbb Z\to\mathbb C:u_{j+n}=-u_j\}.
$$

On this $n$-dimensional space define

$$
(A_{\mathrm{tw}}u)_j
=u_{j-1}+u_{j+1}+(-1)^j(u_{j-2}+u_{j+2}).                \tag{5}
$$

Restricting (5) to $0\le j<n$ produces precisely the matrix in (1): an edge
that crosses the boundary once acquires the factor $-1$. For the step-one
edges this changes only $a_{n-1}$; for the step-two edges it changes
$b_{n-2}$ and $b_{n-1}$. Hence $A_{\mathrm{tw}}$ and $A_n^-$ are the same
unsquared adjacency operator under the natural identification
$\mathcal U_n^-\cong\mathbb C^n$.

The allowed Fourier parameters are

$$
\vartheta_k=\frac{(2k+1)\pi}{n},\qquad 0\le k<n,         \tag{6}
$$

because $e^{in\vartheta_k}=-1$. Multiplication by $(-1)^j$ sends the
Fourier mode $e^{ij\vartheta}$ to $e^{ij(\vartheta+\pi)}$. Consequently the
two-dimensional space

$$
E_\vartheta=
\operatorname{span}\{(e^{ij\vartheta})_j,
                      (e^{ij(\vartheta+\pi)})_j\}
$$

is invariant under $A_{\mathrm{tw}}$. In the displayed ordered basis, (5)
has the Hermitian matrix

$$
B(\vartheta)=
2\begin{pmatrix}
\cos\vartheta&\cos2\vartheta\\
\cos2\vartheta&-\cos\vartheta
\end{pmatrix}.                                         \tag{7}
$$

The spaces $E_{\vartheta_k}$ with $0\le k<n/2$ are mutually orthogonal and
their direct sum is $\mathcal U_n^-$. Moreover,

$$
B(\vartheta)^2
=4\bigl(\cos^2\vartheta+\cos^22\vartheta\bigr)I_2.      \tag{8}
$$

Thus the two eigenvalues of (7) are

$$
\pm2\sqrt{\cos^2\vartheta+\cos^22\vartheta}.            \tag{9}
$$

It remains only to locate the largest value among the discrete parameters.
Put $x=\cos2\vartheta$. Then

$$
\cos^2\vartheta+\cos^22\vartheta
=x^2+\frac{x}{2}+\frac12=:F(x).                         \tag{10}
$$

For the parameters (6), reduced modulo $\pi$, one has

$$
-1\le x\le x_n:=\cos\frac{2\pi}{n}.
$$

Since $F$ is convex, its maximum on $[-1,x_n]$ is attained at an endpoint.
Now $F(-1)=1$, whereas $n\ge8$ gives
$x_n\ge\cos(\pi/4)=1/\sqrt2$ and hence

$$
F(x_n)\ge F(1/\sqrt2)=1+\frac1{2\sqrt2}>1.              \tag{11}
$$

Therefore the discrete maximum is attained at
$\vartheta=\pi/n$ and $\vartheta=\pi-\pi/n$. Equations (8)-(10) yield

$$
\rho(A_n^-)^2
=4\left(\cos^2\frac{\pi}{n}+\cos^2\frac{2\pi}{n}\right).
$$

The double-angle identity gives the other two expressions in (3). This
proves (3). Since both spectral radii are nonnegative, equality of their
squares also gives $\rho(A_n^-)=\rho_-(n)$. Finally, (4) follows because
$\sigma_n^-$ is one of the signings over which $m_n$ is minimised. $\square$

## Role in the classification

Let

$$
\mathcal V=
\{8,10,12,14,16,18,20,22,24,26,28,30,34,36,38,42,44,46\}.
$$

The exact finite exhaustion proves $\rho(A_\sigma)\ge\rho_-(n)$ for every
signing whenever $n\in\mathcal V$, so $m_n\ge\rho_-(n)$. The present lemma
gives the reverse inequality using the explicit signing (1). Hence

$$
m_n=\rho_-(n)\qquad(n\in\mathcal V).                    \tag{12}
$$

At $n=32$, $n=40$, and every even $n\ge48$, the separate counterexample
certificates give a signing $\widehat\sigma_n$ with
$\rho(A_{\widehat\sigma_n})<\rho_-(n)$. Consequently
$m_n<\rho_-(n)$ there. The equality candidate (1) still exists at those
orders, but it is not a minimiser.

The proof of the attainment lemma is entirely analytic. It has no machine
dependency and does not rely on a producer or an independent checker. The
machine-assisted input to (12) is only the exhaustive lower bound on the
finite validity set.

For compatibility with ASCII evidence ledgers, the result is recorded as
`m_n<=rho_-(n)`. The spectral calculation above is a direct 2 x 2 Fourier
calculation, not a numerical eigensolve.
