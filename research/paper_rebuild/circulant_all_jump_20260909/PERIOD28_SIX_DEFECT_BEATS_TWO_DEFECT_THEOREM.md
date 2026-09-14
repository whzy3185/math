# Period twenty-eight: a six-defect phase strictly beats the complete two-defect family

Date: 2026-09-14

Status: **Proved**.

This theorem shows that the multi-block transition continues: after four defects improve periods twenty and twenty-four, a six-defect phase gives a stronger improvement at period twenty-eight.

## 1. Setup

Take coefficient period

\[
p=28,
\qquad s=14.
\]

For a legal flux word `Q`, write

\[
R(Q)=\max_{|z|=1}\rho(H_Q(z))^2.
\]

Inside the complete even-separation reflection-chiral two-defect family, the fixed-period classification gives the unique optimizer

\[
(N,m)=(4,3),
\]

i.e. two positive flux defects at cyclic distance six. Denote its edge by `R_2def`.

## Theorem — explicit six-defect improvement

Let `Q^(6)` have positive flux sites

\[
\boxed{\{0,2,4,6,8,10\}}
\]

and all other sites negative. Then

\[
\boxed{
R(Q^{(6)})<\frac{31}{4}<R_{\rm 2def}.
}
\tag{1.1}
\]

Hence the period-twenty-eight periodic class contains an explicit six-defect phase that strictly beats every two-defect phase.

---

## 2. All-phase certificate for the six-defect phase

Set

\[
y_0=31/4.
\]

For the Hamilton-gauge lift with `tau_0=1`, sparse determinant elimination gives

\[
\det(y_0I-H_{Q^{(6)}}(z)^2)
=
\frac{F(z)^2}{2^{56}z^{28}},
\tag{2.1}
\]

where `F` is a palindromic degree-twenty-eight polynomial. With

\[
c=z+z^{-1},
\]

one has

\[
F(z)/z^{14}=f(c),
\]

where

\[
\boxed{
\begin{aligned}
f(c)={}&268435456c^{14}-2013265920c^{13}-9747562496c^{12}\\
&+97391738880c^{11}+107517837312c^{10}-1951912165376c^9\\
&+227788128256c^8+20743544242176c^7-14772973096960c^6\\
&-123275401693184c^5+130778048252160c^4\\
&+388405188537600c^3-500641039693904c^2\\
&-506842377670776c+735248754488513.
\end{aligned}}
\tag{2.2}
\]

The exact Sturm count gives

\[
\boxed{
\#\{c\in[-2,2]:f(c)=0\}=0.
}
\tag{2.3}
\]

Thus the test-energy determinant never vanishes on the Bloch circle.

At `z=1`, all twenty-eight leading principal minors of

\[
31I-4H_{Q^{(6)}}(1)^2
\]

are strictly positive. Sylvester's criterion therefore shows the reference fiber lies strictly below `31/4`. Since no test-energy crossing occurs on the connected unit circle, the inertia is constant and

\[
\boxed{R(Q^{(6)})<31/4.}
\tag{2.4}
\]

---

## 3. The complete two-defect family lies above the separator

The unique best two-defect geometry has defects at distance six. At its periodic fiber `z=1`, the fifteenth leading principal minor of

\[
31I-4H_{2\rm def}(1)^2
\]

is

\[
\boxed{-9783314151385<0.}
\tag{3.1}
\]

Hence the matrix is not positive definite and that single fiber already has a squared eigenvalue greater than `31/4`. Therefore

\[
R_{\rm 2def}>31/4.
\tag{3.2}
\]

Combining (2.4) and (3.2) proves (1.1).

---

## 4. Numerical orientation only

A corrected Hermitian Bloch optimization gives

\[
R(Q^{(6)})\approx7.70492555729137,
\]

where the maximizing phase lies slightly off `z=1`, while

\[
R_{\rm 2def}\approx7.89103763207757.
\]

These decimal values are not used in the proof.

## 5. Structural interpretation

The favorable defect count has now increased from four to six. The six positive fluxes form a contiguous even-site train

\[
0,2,4,6,8,10,
\]

which, after folding, corresponds to a further reorganization of the hard/soft block pattern. This strengthens the evidence that the correct large-period variational language is not `number of defects` alone but a multi-block scattering geometry with its own internal phase-slip mechanism.