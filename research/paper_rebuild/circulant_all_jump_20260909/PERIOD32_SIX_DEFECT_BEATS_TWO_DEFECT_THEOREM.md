# Period thirty-two: a six-defect phase strictly beats the complete two-defect family

Date: 2026-09-14

Status: **Proved**.

Together with the period-twenty-eight theorem, this result shows that six-defect improvements persist across two consecutive period layers.

## 1. Setup and theorem

Take

\[
p=32,
\qquad s=16.
\]

Inside the complete even-separation reflection-chiral two-defect family, the unique fixed-period optimizer is the balanced geometry

\[
(N,m)=(4,4),
\]

i.e. defect separation eight. Denote its edge by `R_2def`.

Let `Q^(6)` have positive flux sites

\[
\boxed{\{0,2,4,8,10,12\}}
\]

and all other fluxes negative. Then

\[
\boxed{
R(Q^{(6)})<\frac{31}{4}<R_{\rm 2def}.
}
\tag{1.1}
\]

Hence period thirty-two contains an explicit six-defect phase that strictly beats every two-defect phase.

---

## 2. Exact all-phase certificate

Set

\[
y_0=31/4.
\]

Sparse determinant elimination gives

\[
\det(y_0I-H_{Q^{(6)}}(z)^2)
=
\frac{F(z)^2}{2^{64}z^{32}},
\tag{2.1}
\]

where `F` is a palindromic degree-thirty-two polynomial. Writing

\[
c=z+z^{-1},
\]

one has

\[
F(z)/z^{16}=f(c),
\]

with

\[
\boxed{
\begin{aligned}
f(c)={}&4294967296c^{16}-345744867328c^{14}+11590439010304c^{12}\\
&+17179869184c^{11}-211636182843392c^{10}-604516646912c^9\\
&+2310709849751552c^8+8551414104064c^7\\
&-15499752407007232c^6-60462527938560c^5\\
&+62531457890491392c^4+211658118266880c^3\\
&-138961338006962304c^2-288838803767296c\\
&+130435427231218817.
\end{aligned}}
\tag{2.2}
\]

The exact Sturm root count gives

\[
\boxed{
\#\{c\in[-2,2]:f(c)=0\}=0.
}
\tag{2.3}
\]

At `z=-1`, all thirty-two leading principal minors of

\[
31I-4H_{Q^{(6)}}(-1)^2
\]

are strictly positive. Thus the reference fiber lies below `31/4`; because the test-energy determinant never vanishes on the unit circle, inertia is constant and

\[
\boxed{R(Q^{(6)})<31/4.}
\tag{2.4}
\]

---

## 3. Best two-defect phase lies above the separator

For the balanced period-thirty-two two-defect optimizer, at `z=-1` the seventeenth leading principal minor of

\[
31I-4H_{2\rm def}(-1)^2
\]

is

\[
\boxed{-12392271898986041<0.}
\tag{3.1}
\]

Hence that fiber already has squared spectral radius above `31/4`, and therefore

\[
R_{\rm 2def}>31/4.
\]

This proves (1.1).

---

## 4. Numerical orientation only

Corrected Hermitian optimization gives

\[
R(Q^{(6)})\approx7.70143408778191,
\]

whereas

\[
R_{\rm 2def}\approx7.89110134569558.
\]

The decimal values are not used in the proof.

## 5. Interpretation

The sequence of explicit multi-defect improvements is now:

- period 20: four defects;
- period 24: four defects;
- period 28: six defects;
- period 32: six defects.

The optimal block geometry changes with the period, but the improvement is robust. This strongly suggests an infinite multi-block hierarchy whose natural control parameter is the number and spacing of folded defect blocks rather than the original two-defect separation.