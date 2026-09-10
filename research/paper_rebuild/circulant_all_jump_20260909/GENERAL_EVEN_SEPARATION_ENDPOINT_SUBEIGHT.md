# Every even-separation endpoint fiber is strictly sub-eight

Date: 2026-09-10

Status: **Proved**. This note belongs only to Paper I.

## Theorem

Let `L>h>=2` be even and let the period be `2L`. Put `h=2m` and use the two-defect flux word

\[
Q_0=Q_h=1,\qquad Q_j=-1\quad(j\ne0,h).
\]

For any odd multiplier `2q+1`, set

\[
s=L(2q+1).
\]

Then the periodic Bloch endpoint is strictly below the squared edge `8`:

\[
\boxed{
\rho(H_{L,q,h}(1))^2<8.
}
\tag{1}
\]

This holds for every admissible finite pair `(L,h)`, with no large-period assumption.

## Proof

At `z=1`, the folded fiber decomposes into scalar channels `J_+` and `J_-`, with

\[
J_-=-D_LJ_+D_L.
\]

Hence they have opposite spectra and it is enough to exclude an eigenvalue of `J_+` with squared value `y>=8`.

Let

\[
N=\frac{L-h}{2}\ge1,
\qquad m=\frac h2\ge1.
\]

With scalar transfer matrices

\[
T_v(\lambda)=
\begin{pmatrix}\lambda-v&-1\\1&0\end{pmatrix},
\]

define

\[
B=T_2T_{-2},\qquad D=T_0^2.
\]

The endpoint monodromy has trace

\[
\operatorname{tr}(B^ND^m).
\]

A periodic scalar eigenvalue requires

\[
\operatorname{tr}(B^ND^m)=2.
\tag{2}
\]

Write `y=lambda^2` and

\[
x=\frac{y-6}{2},\qquad a=\frac{y-2}{2}.
\]

For `y>=8`, one has `x>=1` and `a>=3`. By Cayley--Hamilton,

\[
B^N=U_{N-1}(x)B-U_{N-2}(x)I.
\]

Also

\[
A_m(y):=\operatorname{tr}D^m=2T_m(a)
\]

and the exact identity

\[
\operatorname{tr}(BD^m)-A_m(y)
=(y-8)\bigl(U_m(a)+U_{m-1}(a)\bigr)
\]

gives

\[
\begin{aligned}
\operatorname{tr}(B^ND^m)
={}&A_m(y)\bigl(U_{N-1}(x)-U_{N-2}(x)\bigr)\\
&+(y-8)\bigl(U_m(a)+U_{m-1}(a)\bigr)U_{N-1}(x).
\end{aligned}
\tag{3}
\]

For `x>=1`,

\[
U_{N-1}(x)\ge U_{N-2}(x)\ge0
\]

and in fact

\[
U_{N-1}(x)-U_{N-2}(x)\ge1.
\]

For `a>=3`, all the remaining Chebyshev quantities in (3) are nonnegative and

\[
A_m(y)=2T_m(a)\ge2T_m(3)\ge6.
\]

Therefore

\[
\boxed{
\operatorname{tr}(B^ND^m)\ge6>2
\qquad(y\ge8).
}
\tag{4}
\]

This contradicts the periodic eigenvalue condition (2). Hence `J_+` has no eigenvalue with squared value at least `8`. Since `J_-` has the opposite spectrum, neither does the full endpoint fiber.

Thus

\[
\rho(H_{L,q,h}(1))^2<8,
\]

proving (1).

## Consequence

The endpoint sub-eight property is therefore universal across the entire even-separation reflection-chiral family. What can fail for some geometries is not the endpoint inequality but global Bloch dominance: away from `z=1`, some large-separation families can cross above `8`. This cleanly separates the endpoint problem from the full Bloch optimization problem.