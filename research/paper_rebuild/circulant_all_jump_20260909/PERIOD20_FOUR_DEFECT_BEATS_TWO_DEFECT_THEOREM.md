# Period twenty: a four-defect phase strictly beats the complete two-defect family

Date: 2026-09-14

Status: **Proved**.

This theorem marks the first period at which the reflection-chiral two-defect ansatz is no longer globally variationally optimal inside the larger periodic flux class.

It does **not** rely on exhaustive full-class enumeration.

---

## 1. Setup

Take coefficient period

\[
p=20
\]

and jump

\[
s=10.
\]

Work in Hamilton gauge: nearest-neighbor coefficients are `+1`, and the jump-ten signs are a period-twenty word `tau`. Let

\[
Q_j=\tau_j\tau_{j+1}\in\{\pm1\}
\]

be the local flux word.

For a unit Bloch phase `z`, the `20 x 20` Hermitian fiber is denoted `H_Q(z)` and its continuous squared Bloch edge is

\[
R(Q)=\max_{|z|=1}\rho(H_Q(z))^2.
\]

The previously proved fixed-period geometry theorem identifies the unique optimizer inside the even-separation reflection-chiral two-defect family. Since

\[
20=8\cdot2+4,
\]

that two-defect optimizer is

\[
(N,m)=(3,2),
\]

equivalently two positive flux defects at cyclic distance

\[
h=2m=4.
\]

Call its edge `R_2def`.

---

# Theorem A — explicit four-defect improvement

Let `Q^(4)` be the period-twenty flux word with positive sites

\[
\boxed{\{0,2,4,6\}}
\]

and all other fluxes equal to `-1`.

Then

\[
\boxed{
R(Q^{(4)})<\frac{31}{4}<R_{\rm 2def}.
}
\tag{2.1}
\]

Consequently

\[
\boxed{
\min_{\text{all legal period-20 flux words}}R(Q)
<
\min_{\text{two-defect reflection-chiral words}}R(Q).
}
\tag{2.2}
\]

Thus the two-defect variational ansatz is genuinely non-optimal at period twenty.

The word `Q^(4)` has primitive period twenty: its four-point defect set is not preserved by any nonzero proper translation of `Z/20Z`.

---

## 2. Exact test energy for the four-defect phase

Set

\[
y_0=\frac{31}{4}.
\]

Choose the lift with `tau_0=1`. Direct sparse determinant elimination gives

\[
\boxed{
\det\!\left(y_0I-H_{Q^{(4)}}(z)^2\right)
=\frac{A(z)^2B(z)^2}{2^{40}z^{20}},
}
\tag{3.1}
\]

where

\[
A(z)=16z^4+16z^3-69z^2+16z+16,
\tag{3.2}
\]

and

\[
\begin{aligned}
B(z)={}&65536z^{16}-557056z^{15}+172032z^{14}+8787968z^{13}\\
&-14402560z^{12}-44016000z^{11}+100143200z^{10}\\
&+59814920z^9-222161773z^8+59814920z^7\\
&+100143200z^6-44016000z^5-14402560z^4\\
&+8787968z^3+172032z^2-557056z+65536.
\end{aligned}
\tag{3.3}
\]

Both factors are palindromic.

---

## 3. Reduction to the physical phase coordinate

Put

\[
c=z+z^{-1}\in[-2,2].
\]

Dividing `A(z)` by `z^2` gives

\[
\boxed{
A(z)/z^2=16c^2+16c-101=:a(c).
}
\tag{4.1}
\]

Its two roots are

\[
\frac{-2\pm\sqrt{105}}4,
\]

one larger than `2` and the other smaller than `-2`; hence

\[
a(c)\ne0\qquad(-2\le c\le2).
\tag{4.2}
\]

Similarly

\[
B(z)/z^8=b(c),
\]

where

\[
\boxed{
\begin{aligned}
b(c)={}&65536c^8-557056c^7-352256c^6+12687360c^5\\
&-14124032c^4-95754624c^3+158253152c^2\\
&+239702152c-451466285.
\end{aligned}}
\tag{4.3}
\]

The exact Sturm sequence of `b` has sign patterns

\[
(-,-,+,-,-,+,+,+,-)
\]

at `c=-2`, and

\[
(-,+,+,-,+,+,+,+,-)
\]

at `c=2`.

Each pattern has exactly four sign changes. Hence Sturm's theorem gives

\[
\boxed{
\#\{c\in[-2,2]:b(c)=0\}=0.
}
\tag{4.4}
\]

Therefore (3.1) never vanishes on the unit Bloch circle.

---

## 4. Reference-fiber inertia

At `z=1`, set

\[
M=31I-4H_{Q^{(4)}}(1)^2.
\]

The twenty leading principal minors are

\[
\begin{aligned}
&7,161,3335,21025,130935,2679201,54738183,340365601,\\
&2116008055,9367255345,12093554471,109667721521,\\
&911982564919,2759343640625,6676438036775,61389597667121,\\
&196731422410807,374413482954289,207593298017655,\\
&115099961256225.
\end{aligned}
\tag{5.1}
\]

All are positive. Sylvester's criterion therefore gives

\[
31I-4H_{Q^{(4)}}(1)^2>0.
\]

Equivalently,

\[
\rho(H_{Q^{(4)}}(1))^2<31/4.
\]

Because the determinant at the test energy never vanishes on the connected Bloch circle, the inertia of

\[
y_0I-H_{Q^{(4)}}(z)^2
\]

is constant in `z`. Hence it is positive definite for every unit phase and

\[
\boxed{R(Q^{(4)})<31/4.}
\tag{5.2}
\]

---

## 5. The best two-defect phase lies above the same separator

By `ALL_PERIODS_DIVISIBLE_BY_FOUR_OPTIMAL_GEOMETRY.md`, the unique best two-defect geometry at period twenty is `(N,m)=(3,2)`, i.e. defect separation four.

At its periodic fiber `z=1`, form

\[
M_{2}=31I-4H_{2\rm def}(1)^2.
\]

Its thirteenth leading principal minor is exactly

\[
\boxed{
\det M_2[1\!:\!13,1\!:\!13]
=-154959222793<0.
}
\tag{6.1}
\]

Therefore `M_2` is not positive definite, and the fiber already has a squared eigenvalue strictly larger than `31/4`:

\[
R_{\rm 2def}>31/4.
\tag{6.2}
\]

Combining (5.2) and (6.2) proves Theorem A.

---

## 6. Numerical orientation only (not used in the proof)

A corrected Hermitian Bloch computation gives

\[
R(Q^{(4)})\approx7.72503939417635,
\]

while the best two-defect edge is

\[
R_{\rm 2def}\approx7.83584080853474.
\]

These decimal values are only orientation; the strict theorem is the rational separation (2.1).

---

## 7. Consequences

This result changes the paper-level variational picture.

The sequence of full-period classes now behaves as follows:

- period `8`: two-defect optimizer is globally optimal, analytically proved;
- period `12`: two-defect optimizer is globally optimal, exact finite verified;
- period `16`: two-defect optimizer is globally optimal, exact finite verified, although other sub-eight multi-defect phases already exist;
- period `20`: a four-defect phase strictly beats **every** two-defect phase.

Hence the natural next problem is no longer to prove universal two-defect rigidity. It is to understand the **defect-number transition** and determine the optimal periodic flux geometry as the period grows.