# Exact antiperiodic threshold obstruction curve

Date: 2026-09-10

Status: **Proved**. This note belongs only to Paper I.

This result gives the first exact two-parameter obstruction for the general even-separation family. It also corrects the preliminary numerical guess that a fixed number of alternating bulk pairs might always suffice.

## 1. Parameters

Let

\[
L=2(N+m),
\qquad
h=2m,
\]

with integers

\[
N\ge1,\qquad m\ge1.
\]

Thus

\[
N=\frac{L-h}{2}
\]

is the number of alternating bulk pairs and `m=h/2` is the half-length of the defect arc.

Use the even-separation two-defect phase and any jump

\[
s=L(2q+1).
\]

Let

\[
\det(\lambda I-H_{L,q,h}(z))
=P_{N,m,z}(\lambda^2).
\]

By reflection chirality, `P` is a monic real polynomial in the squared variable on every unit Bloch fiber.

## Theorem A — exact determinant at the antiperiodic phase

At

\[
z=-1,
\]

the squared-edge determinant is

\[
\boxed{
P_{N,m,-1}(8)
=4\left(T_N(3)^2-4m^2\right).
}
\tag{1.1}
\]

Consequently, if

\[
\boxed{2m>T_N(3),}
\tag{1.2}
\]

then

\[
\boxed{
\rho(H_{L,q,h}(-1))^2>8,
}
\tag{1.3}
\]

and the periodic phase is not globally sub-eight.

Because `T_N(3)` is odd for every integer `N>=1`, equality `2m=T_N(3)` never occurs. Thus the antiperiodic threshold has no integer equality case.

---

## 2. Threshold transfer matrices

Use the general block-Jacobi reduction. At `z=-1`, choose `eta=i`. Since the odd multiplier is odd,

\[
\omega^2=z^{2q+1}=-1.
\]

We may choose the gauge with

\[
\cos\beta=0,
\qquad
\sin\beta=1.
\]

At `lambda^2=8`, the two transfer coefficients are therefore

\[
A_g=\sqrt8\,\sigma_z,
\qquad
A_d=\sqrt8\,\sigma_z+2i\sigma_x,
\]

and satisfy

\[
A_g^2=8I_2,
\qquad
A_d^2=4I_2.
\tag{2.1}
\]

Let

\[
T(A)=
\begin{pmatrix}A&-I_2\\I_2&0\end{pmatrix}.
\]

The monodromy is

\[
M=T(A_g)^{2N-1}T(A_d)^{2m}T(A_g).
\tag{2.2}
\]

The boundary involution is

\[
J=\operatorname{diag}(\sigma_x,-\sigma_x),
\]

and, because `eta=i`, the Bloch determinant is

\[
P_{N,m,-1}(8)=\det(M-iJ).
\tag{2.3}
\]

---

## 3. Closed transfer powers

For `A_g^2=8I`, the relevant scalar Chebyshev argument is `3`. Put

\[
a_N:=U_{N-1}(3),
\qquad
b_N:=U_{N-2}(3),
\]

with `U_{-1}=0`. The matrix-continuant identity gives

\[
T(A_g)^{2N-1}
=
\begin{pmatrix}
a_NA_g&-(a_N+b_N)I_2\\
(a_N+b_N)I_2&-b_NA_g
\end{pmatrix}.
\tag{3.1}
\]

For `A_d^2=4I`, the scalar Chebyshev argument is `1`, so `U_j(1)=j+1`. Hence

\[
\boxed{
T(A_d)^{2m}
=
\begin{pmatrix}
(2m+1)I_2&-mA_d\\
mA_d&-(2m-1)I_2
\end{pmatrix}.}
\tag{3.2}
\]

Substitute (3.1)--(3.2) into (2.2)--(2.3). This is now a fixed `4 x 4` determinant. Using only the Pauli identities

\[
\sigma_i^2=I,
\qquad
\sigma_i\sigma_j=-\sigma_j\sigma_i\quad(i\ne j),
\]

the determinant reduces to

\[
P_{N,m,-1}(8)
=4\left[(3a_N-b_N)^2-4m^2\right].
\tag{3.3}
\]

Finally the standard identity

\[
T_N(x)=xU_{N-1}(x)-U_{N-2}(x)
\]

gives

\[
3a_N-b_N=T_N(3).
\]

This proves (1.1).

---

## 4. From determinant sign to a super-eight root

By chirality,

\[
P_{N,m,-1}(y)=\prod_{j=1}^{L}(y-y_j),
\]

where the `y_j` are the nonnegative squared eigenvalues of the Hermitian fiber.

The polynomial is monic, so

\[
P_{N,m,-1}(y)\to+\infty
\qquad(y\to+\infty).
\]

If `2m>T_N(3)`, equation (1.1) gives

\[
P_{N,m,-1}(8)<0.
\]

By continuity there is a real root

\[
y_*>8.
\]

Therefore

\[
\rho(H_{L,q,h}(-1))^2\ge y_*>8,
\]

which proves (1.3).

---

## 5. Exact first obstruction thresholds

The numbers `T_N(3)` begin

\[
3,17,99,577,3363,\ldots
\]

and satisfy

\[
T_{N+1}(3)=6T_N(3)-T_{N-1}(3).
\]

Hence the first integer obstruction occurs at

\[
m_{\rm crit}(N)=\frac{T_N(3)+1}{2}.
\]

The first cases are

\[
\begin{array}{c|c|c}
N&T_N(3)&m\text{ forcing }R>8\\ \hline
1&3&m\ge2\\
2&17&m\ge9\\
3&99&m\ge50\\
4&577&m\ge289\\
5&3363&m\ge1682.
\end{array}
\]

Thus the safe-looking region for fixed `N` can be very large, but it is never infinite: every fixed number of alternating bulk pairs eventually loses the global sub-eight property as the defect arc grows.

---

## 6. Exponential geometry of the obstruction curve

Let

\[
\Lambda=3+2\sqrt2.
\]

Since

\[
T_N(3)=\frac{\Lambda^N+\Lambda^{-N}}2,
\]

the antiperiodic obstruction condition is asymptotically

\[
\boxed{
m>\frac14\Lambda^N.}
\tag{6.1}
\]

Equivalently, to accommodate a defect half-length `m` without triggering this explicit obstruction, the complementary bulk length must satisfy at least

\[
N\gtrsim\frac{\log(4m)}{\log(3+2\sqrt2)}.
\]

This logarithmic/exponential tradeoff is a new geometric scale in the periodic-phase problem.

## 7. Consequences and corrected research target

The former tentative conjecture

> `N>=3` might imply global sub-eight

is false: for example `N=3` already fails once `m>=50`.

The evidence now points to a much sharper candidate phase diagram:

\[
\boxed{
2m<T_N(3)
}
\]

may be the exact condition for the entire Bloch circle to remain below `8` in the arbitrary-even-separation family.

Only the necessity direction is proved in this note. The converse remains open and is now the principal strengthening target.