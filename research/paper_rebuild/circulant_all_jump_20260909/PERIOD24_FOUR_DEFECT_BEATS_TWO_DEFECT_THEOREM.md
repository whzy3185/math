# Period twenty-four: a four-defect phase strictly beats the complete two-defect family

Date: 2026-09-14

Status: **Proved**.

This is the second analytic multi-defect improvement after period twenty. It shows that the defect-block-splitting mechanism persists beyond its first occurrence.

---

## 1. Setup

Take coefficient period

\[
p=24
\]

and jump

\[
s=12.
\]

For a legal period-twenty-four flux word `Q`, let

\[
R(Q)=\max_{|z|=1}\rho(H_Q(z))^2
\]

be its continuous squared Bloch edge.

Inside the complete even-separation reflection-chiral two-defect family, `ALL_PERIODS_DIVISIBLE_BY_FOUR_OPTIMAL_GEOMETRY.md` gives the unique optimizer

\[
(N,m)=(3,3),
\]

i.e. two positive flux defects at cyclic distance

\[
h=2m=6.
\]

Denote its edge by `R_2def`.

---

# Theorem A — explicit four-defect improvement

Let `Q^(4)` have positive flux sites

\[
\boxed{\{0,2,4,8\}}
\]

and all remaining fluxes equal to `-1`.

Then

\[
\boxed{
R(Q^{(4)})<\frac{31}{4}<R_{\rm 2def}.
}
\tag{2.1}
\]

Consequently the period-twenty-four full periodic class contains an explicit four-defect phase that strictly beats **every** reflection-chiral two-defect phase.

---

## 2. Exact all-phase certificate for the four-defect phase

Set

\[
y_0=\frac{31}{4}.
\]

Choose the Hamilton-gauge lift with `tau_0=1`. Direct sparse determinant elimination gives

\[
\boxed{
\det\!\left(y_0I-H_{Q^{(4)}}(z)^2\right)
=\frac{F(z)^2}{2^{48}z^{24}},
}
\tag{3.1}
\]

where the palindromic degree-twenty-four polynomial is

\[
\begin{aligned}
F(z)={}&16777216z^{24}-878706688z^{22}+17109549056z^{20}\\
&+67108864z^{19}-156687220736z^{18}-742391808z^{17}\\
&+737862848256z^{16}+2210136064z^{15}-1842013676640z^{14}\\
&-835960832z^{13}+2496883070657z^{12}-835960832z^{11}\\
&-1842013676640z^{10}+2210136064z^9+737862848256z^8\\
&-742391808z^7-156687220736z^6+67108864z^5\\
&+17109549056z^4-878706688z^2+16777216.
\end{aligned}
\tag{3.2}
\]

Put

\[
c=z+z^{-1}\in[-2,2].
\]

Since `F` is palindromic,

\[
F(z)/z^{12}=f(c),
\]

where

\[
\boxed{
\begin{aligned}
f(c)={}&16777216c^{12}-1080033280c^{10}+26802585600c^8\\
&+67108864c^7-326197395456c^6-1212153856c^5\\
&+2065874095872c^4+6861619200c^3\\
&-6499974488160c^2-11648090112c+8006020627841.
\end{aligned}}
\tag{3.3}
\]

The exact Sturm root count gives

\[
\boxed{
\#\{c\in[-2,2]:f(c)=0\}=0.
}
\tag{3.4}
\]

Hence the test-energy determinant (3.1) never vanishes on the unit Bloch circle.

---

## 3. Reference-fiber inertia

At `z=-1`, put

\[
M=31I-4H_{Q^{(4)}}(-1)^2.
\]

Its twenty-four leading principal minors are

\[
\begin{aligned}
&23,161,1015,21025,430215,2679201,16659447,73814449,\\
&326765671,6335627825,122820541175,2723519179041,\\
&32168084189383,101088070749985,299988606672055,\\
&3025923939380769,15100189544063687,42379473892826401,\\
&160719273138794615,208450211517906225,241299126551232295,\\
&719562889489112369,4253691563943840135,39745799911808686081.
\end{aligned}
\tag{4.1}
\]

All are positive. Therefore Sylvester's criterion gives

\[
31I-4H_{Q^{(4)}}(-1)^2>0,
\]

or equivalently

\[
\rho(H_{Q^{(4)}}(-1))^2<31/4.
\]

Since the determinant at the test energy never vanishes around the connected unit Bloch circle, inertia is constant. Thus

\[
\boxed{R(Q^{(4)})<31/4.}
\tag{4.2}
\]

---

## 4. The complete two-defect family lies above the separator

The unique period-twenty-four optimizer inside the even-separation two-defect family is the balanced geometry with positive flux sites at distance six.

At its `z=-1` fiber form

\[
M_2=31I-4H_{2\rm def}(-1)^2.
\]

The eighteenth leading principal minor is

\[
\boxed{
\det M_2[1\!:\!18,1\!:\!18]
=-67886552575679<0.
}
\tag{5.1}
\]

Thus `M_2` is not positive definite and

\[
R_{\rm 2def}>31/4.
\tag{5.2}
\]

Combining (4.2) and (5.2) proves Theorem A.

---

## 5. Numerical orientation only

A corrected Hermitian Bloch optimization gives

\[
R(Q^{(4)})\approx7.71462528378528,
\]

while the best two-defect phase has

\[
R_{\rm 2def}\approx7.83384008996410.
\]

These decimals are not used in the proof.

---

## 6. Structural interpretation

Period twenty already showed that one long two-defect scattering block can be improved by splitting it into multiple shorter defect blocks. Period twenty-four confirms that the effect is not a one-period accident.

The new four-defect pattern is not the same word as the period-twenty winner: the favorable placement changes with the ambient period. The natural next task is therefore to formulate the optimization in terms of **multi-block scattering geometry** rather than raw defect count.