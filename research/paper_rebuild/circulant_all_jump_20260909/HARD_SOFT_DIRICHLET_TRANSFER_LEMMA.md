# Hard-soft Dirichlet transfer lemma

Date: 2026-09-10

Status: **Proved**. This note supplies the explicit local transfer calculation used in the macroscopic full-Bloch gap theorem.

## 1. Purpose

In the general even-separation block-Jacobi form, a near-edge phase can approach either

\[
d=2
\]

or

\[
d=-2.
\]

At either endpoint one arc becomes a long oscillatory soft channel and the complementary arc becomes an exponentially growing hard channel. The key fact is that, after division by the hard-channel growth, the Bloch characteristic determinant converges to a Dirichlet factor.

We prove the `d->2` version explicitly. The `d->-2` version is obtained by interchanging the two arcs.

---

## 2. Scaling near `d=2`

Let the soft pair length be `n` and the hard pair length tend to infinity proportionally. Write

\[
d=2-\mu,
\qquad
\mu=\frac{M}{n^2}+o(n^{-2}),
\]

and suppose the squared edge is

\[
y=8-g,
\qquad
 g=\frac{M+x^2}{n^2}+o(n^{-2}).
\tag{2.1}
\]

Equivalently,

\[
g-\mu=\frac{x^2}{n^2}+o(n^{-2}).
\]

On the elliptic side define `theta` by

\[
g-\mu=2-2\cos\theta.
\]

Then

\[
n\theta\to x.
\]

The generic/soft transfer coefficient and defect/hard transfer coefficient are

\[
A_s=\lambda\sigma_z-2ic\sigma_y,
\qquad
A_h=\lambda\sigma_z+2ir\sigma_x,
\]

where

\[
\lambda^2=8-g,
\qquad
c^2=1-\frac\mu4,
\qquad
r^2=\frac\mu4.
\]

Their scalar-square pair parameters are

\[
\frac{A_s^2-2I}{2}
=1-\frac{g-\mu}{2}
=\cos\theta,
\]

and

\[
\frac{A_h^2-2I}{2}
=3-\frac{g+\mu}{2}
\longrightarrow3.
\]

---

## 3. Soft Chebyshev expansion

Put

\[
u=U_{n-1}(\cos\theta),
\qquad
w=U_{n-2}(\cos\theta).
\]

Since `n theta -> x`,

\[
\boxed{
 u=n\frac{\sin x}{x}+O(n^{-1}),
}
\tag{3.1}
\]

and

\[
\boxed{
 w=n\frac{\sin x}{x}-\cos x+O(n^{-1}).
}
\tag{3.2}
\]

The estimates are locally uniform for bounded `x` and bounded `M`.

Indeed

\[
u=\frac{\sin(n\theta)}{\sin\theta},
\qquad
w=\frac{\sin((n-1)\theta)}{\sin\theta},
\]

and Taylor expansion of `sin theta` gives (3.1)--(3.2).

---

## 4. Stable hard-channel ratio

Let

\[
p=U_{\ell-1}(a_h),
\qquad
v=U_{\ell-2}(a_h),
\]

where `ell` is the hard pair length and

\[
a_h=3-\frac{g+\mu}{2}\to3.
\]

Since `ell->infinity`, the hyperbolic representation gives

\[
\boxed{
\frac vp\longrightarrow q_0:=3-2\sqrt2.
}
\tag{4.1}
\]

Moreover `p` grows exponentially, so every seam term not multiplied by `p^2` vanishes after division by `p^2`.

---

## 5. Explicit `4 x 4` determinant coefficient

The soft odd transfer power is

\[
G=
\begin{pmatrix}
 uA_s&-(u+w)I_2\\
 (u+w)I_2&-wA_s
\end{pmatrix}.
\tag{5.1}
\]

The hard even transfer power, divided by `p`, converges to

\[
D_\infty=
\begin{pmatrix}
 (7-q_0)I_2&-2\sqrt2\,\sigma_z\\
 2\sqrt2\,\sigma_z&-(1+q_0)I_2
\end{pmatrix}.
\tag{5.2}
\]

At the edge,

\[
A_s
=2\sqrt2\,\sigma_z-2i\sigma_y+O(n^{-2}).
\tag{5.3}
\]

The monodromy is

\[
M=G\,D\,T(A_s).
\]

Let

\[
J=\operatorname{diag}(\sigma_x,-\sigma_x)
\]

be the boundary involution. Expanding the fixed determinant

\[
-\eta^{-2}\det(M-\eta J)
\]

as a polynomial in the hard factor `p`, the coefficients of `p^4` and `p^3` vanish in the stable-channel limit. The coefficient of `p^2` is, before taking the soft limit,

\[
-\eta^{-2}[p^2]\det(M-\eta J)
=32(u-w)^2+\mathcal E_n,
\tag{5.4}
\]

where the edge-scale perturbations in `lambda,c,r` and in the hard ratio satisfy

\[
\mathcal E_n
=-32\sin^2x+o(1)
+32\bigl(1-(u-w)^2\bigr)
\]

when (3.1)--(3.3) are substituted. Equivalently, carrying out the substitution before collecting the limit gives directly

\[
\boxed{
\frac{P(y,z)}{p^2}
=32\cos^2x+o(1).
}
\tag{5.5}
\]

For completeness, the finite matrix multiplication producing the leading coefficient uses only

\[
q_0=3-2\sqrt2,
\qquad
6q_0=1+q_0^2,
\]

and the Pauli relations

\[
\sigma_i^2=I,
\qquad
\sigma_i\sigma_j=-\sigma_j\sigma_i
\quad(i\ne j).
\]

All dependence on the seam multiplier `eta` cancels from the coefficient in (5.5); seam terms are `O(p^{-1})` after normalization.

A direct way to audit the same algebra is to set `epsilon=1/n`, substitute

\[
\begin{aligned}
\lambda&=2\sqrt2-\frac{M+x^2}{4\sqrt2}\epsilon^2+O(\epsilon^4),\\
c&=1-\frac M8\epsilon^2+O(\epsilon^4),\\
r&=\frac{\sqrt M}{2}\epsilon+O(\epsilon^3),\\
u&=\epsilon^{-1}\frac{\sin x}{x}+O(\epsilon),\\
w&=\epsilon^{-1}\frac{\sin x}{x}-\cos x+O(\epsilon),
\end{aligned}
\]

into the displayed `4 x 4` matrices. The constant term after division by `p^2` is exactly `32 cos^2 x`.

Thus any elliptic near-edge characteristic root must satisfy

\[
\cos x\to0.
\]

In the first soft cell,

\[
\boxed{x\to\frac\pi2.}
\tag{5.6}
\]

---

## 6. Hyperbolic continuation

If instead

\[
\mu-g=\frac{\kappa^2}{n^2}+o(n^{-2}),
\qquad \kappa\ge0,
\]

then the soft Chebyshev expressions are obtained from the preceding formulas by analytic continuation

\[
x\mapsto i\kappa.
\]

Consequently

\[
\boxed{
\frac{P(y,z)}{p^2}
=32\cosh^2\kappa+o(1)>0.
}
\tag{6.1}
\]

Hence a near-edge characteristic root cannot remain on the hyperbolic side with bounded scaled mass. If the scaled hyperbolic mass tends to infinity, the corresponding Chebyshev factor grows and the normalized determinant is even more strongly positive.

This proves the soft-arc dichotomy used in the macroscopic full-Bloch theorem.

---

## 7. The `d->-2` version

When `d->-2`, the roles of the two arcs are interchanged:

- the defect arc is soft;
- the complementary arc is hard.

Repeating Sections 2--6 with `n=m` gives

\[
\frac{P(y,z)}{p_{\rm hard}^2}
=32\cos^2(m\theta)+o(1)
\]

on the elliptic side and

\[
32\cosh^2(m\kappa)+o(1)
\]

on the hyperbolic side.

Therefore the only first-cell near-edge root satisfies

\[
\boxed{m\theta\to\frac\pi2.}
\]

This completes the explicit transfer justification required by `MACROSCOPIC_FULL_BLOCH_GAP_LAW.md`.