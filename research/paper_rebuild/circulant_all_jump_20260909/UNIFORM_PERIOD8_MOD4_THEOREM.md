# A uniform period-eight phase for every jump `s = 2 mod 4`

Date: 2026-09-09

Status: **Proved**. This note belongs only to Paper I. It is a theorem about one explicit periodic signing and does not make any statement about the minimum over all finite signings.

The result materially strengthens the previous all-even construction on the arithmetic subfamily `s=2 mod 4`: the period can be kept equal to eight and the spectral gap can be kept uniformly positive, independently of `s`.

## 1. The fixed period-eight word

Fix the period-eight Hamilton-gauge word

\[
\tau_*=(1,1,-1,1,-1,-1,1,-1),
\]

so that

\[
\tau_{i+4}=-\tau_i.
\]

For an even jump `s`, consider the infinite periodic signed step operator

\[
(A_sx)_i=x_{i-1}+x_{i+1}
+\tau_{i-s}x_{i-s}+\tau_i x_{i+s}.
\]

Let `H_s(z)` be its eight-dimensional Bloch fiber under

\[
x_{i+8}=zx_i,
\qquad |z|=1.
\]

Define

\[
R_s^{[8]}:=\max_{|z|=1}\rho(H_s(z))^2.
\]

## Theorem A — uniform `s=2 mod 4` spectral edge

For every

\[
s=4q+2\qquad(q\ge0),
\]

the fixed word `tau_*` has

\[
\boxed{
R_s^{[8]}
=4+\sqrt{10+2\sqrt5}
<8.}
\]

The maximum is attained at the periodic Bloch phase `z=1`.

Equivalently, the squared spectral gap is the same positive constant for the entire congruence class:

\[
\boxed{
8-R_s^{[8]}
=4-\sqrt{10+2\sqrt5}>0.}
\]

Thus, for jumps `s=2 mod 4`, the earlier period-`4s` construction and its `Theta(s^-2)` gap are not the strongest explicit periodic result: a fixed period-eight phase already gives a uniform gap.

---

## 2. Chiral reduction for arbitrary `s=4q+2`

Write

\[
n=2q+1=s/2,
\qquad
\epsilon=(-1)^q.
\]

Choose `w` on the unit circle with

\[
w^2=z.
\]

Because `tau_(i+4)=-tau_i` and `s` is even, the usual half-cell chiral involution applies. On one chiral eigenspace we may use the coordinates `0,1,2,3`, with

\[
x_{i+4}=w(-1)^i x_i.
\]

A direct squaring of the range-`(1,s)` operator gives the following `4 x 4` squared block:

\[
S_q(w)=
\begin{pmatrix}
(4-h)I_2&U_q(w)\\
U_q(w)^*&(4+h)I_2
\end{pmatrix},
\]

where

\[
h=\epsilon\bigl(w^n+w^{-n}\bigr)
\]

and

\[
U_q(w)=
\begin{pmatrix}
1+w^{-1}&2\epsilon w^q\\
2w^q&1-w^{-1}
\end{pmatrix}.
\]

For `q=0`, this is exactly the period-eight squared block of the original jump-two calculation. The point is that the same scalar-block structure survives for every odd `n=s/2`.

The identity can be checked directly from the two-step channels. The displacement `2s=8q+4` reduces to the half-cell scalar `w^(2q+1)=w^n`; the mixed channels reduce to the two entries of magnitude two shown above. No finite-ring extremal statement is involved.

---

## 3. Exact dispersion reduction

For `|w|=1`,

\[
\operatorname{tr}(U_qU_q^*)=12.
\]

Also

\[
\det U_q
=1-w^{-2}-4\epsilon w^{2q}.
\]

Write

\[
w=e^{i\phi},
\qquad
a=\sin\phi,
\qquad
u=\sin(n\phi).
\]

Since multiplication by `w` does not change modulus,

\[
D:=|\det U_q|^2
=|w-w^{-1}-4\epsilon w^n|^2
=16+4a^2-16\epsilon a u.
\]

Because the diagonal `2 x 2` blocks of `S_q` are scalar,

\[
\det(yI-S_q)
=Q^2-12Q+D,
\]

where

\[
Q=(y-4)^2-h^2.
\]

The two eigenvalues of `U_qU_q^*` are nonnegative and have sum `12`, so `D<=36`. Hence the top squared branch is

\[
\boxed{
Y_q(\phi)
=4+\sqrt{h^2+6+\sqrt{36-D}}.}
\]

Using

\[
h^2=4\cos^2(n\phi)=4(1-u^2)
\]

and

\[
36-D=20-4a^2+16\epsilon a u,
\]

we now obtain a uniform bound independent of `q`.

---

## 4. The key inequality

We claim

\[
\sqrt{20-4a^2+16\epsilon a u}
\le4u^2+2\sqrt5.
\]

The right-hand side is positive, so it is enough to square. The difference between the square of the right-hand side and the expression under the radical is

\[
\begin{aligned}
&(4u^2+2\sqrt5)^2
-(20-4a^2+16\epsilon a u)\\
&\qquad=
4\Bigl[
(a-2\epsilon u)^2
+4u^4
+4(\sqrt5-1)u^2
\Bigr]
\ge0.
\end{aligned}
\]

Therefore

\[
\begin{aligned}
h^2+6+\sqrt{36-D}
&\le4(1-u^2)+6+4u^2+2\sqrt5\\
&=10+2\sqrt5.
\end{aligned}
\]

Consequently

\[
Y_q(\phi)
\le4+\sqrt{10+2\sqrt5}.
\]

At `phi=0` we have `a=u=0`, `h^2=4`, `D=16`, and equality holds. Since `z=w^2=1`, this proves both the exact edge and its attaining phase.

Finally,

\[
10+2\sqrt5<16
\]

because `sqrt(5)<3`, so the edge is strictly below `8`.

This proves Theorem A.

---

## 5. Consequences for the paper architecture

The periodic theory now has a genuine arithmetic hierarchy rather than a mere odd/even split:

- odd `s`: period two is already optimal inside the period-two sector, with gap `g_s ~ pi^2/s^2`;
- `s = 2 mod 4`: one fixed period-eight phase gives the uniform edge
  \[
  4+\sqrt{10+2\sqrt5};
  \]
- `s = 0 mod 4`: the previously proved period-`4s` antipodal family still gives a strict sub-eight phase, but shorter/uniform phases remain an open strengthening target.

In particular, the old statement that the explicit all-even antipodal family has a sharp `pi^2/s^2` gap remains correct for that family, but it should no longer be presented as the strongest available construction on the entire even subsequence.

## 6. Next research target

Computational exploration suggests that jumps `s=4 mod 8` also admit period-eight sub-eight phases, but with a different word. This is not asserted here. The natural next question is whether the above theorem begins a `2`-adic hierarchy of bounded or compressed periods for successive valuation classes `v_2(s)=1,2,3,...`.
