# Infinite `DDGG` multi-defect family for every period `8r+4`

Date: 2026-09-15

Status: **Proved**.

This theorem upgrades the separate period-20, 28, and 36 certificates to an infinite analytic family.  It is the first theorem in this project showing that the two-defect variational ansatz fails at infinitely many periods.

---

## 1. Statement

Let

\[
p=8r+4,\qquad s=p/2=4r+2,
\qquad r\ge2.
\]

Define the legal period-`p` flux word `Q^(r)` by

\[
\boxed{
Q_j^{(r)}=+1
\iff
j\in\{0,2,4,\ldots,4r-2\},
}
\tag{1.1}
\]

and put `Q_j=-1` at every other site.  Thus `Q^(r)` has exactly `2r` positive flux defects.

Let

\[
R_r:=\max_{|z|=1}\rho(H_{Q^{(r)}}(z))^2.
\]

### Theorem A — uniform separator

For every integer `r>=2`,

\[
\boxed{R_r<\frac{31}{4}.}
\tag{1.2}
\]

### Theorem B — strict improvement over the complete two-defect family

Let `R_{2\rm def}^{(p)}` be the minimum continuous squared Bloch edge over the complete even-separation reflection-chiral two-defect family of the same period `p`.  Then for every `r>=2`,

\[
\boxed{
R_r<\frac{31}{4}<R_{2\rm def}^{(8r+4)}.
}
\tag{1.3}
\]

Consequently the two-defect ansatz is variationally non-optimal for **every** period

\[
\boxed{p\equiv4\pmod8,\qquad p\ge20.}
\tag{1.4}
\]

The word `Q^(r)` has primitive period exactly `p`.

---

## 2. Folded `DDGG` word

Choose the Hamilton-gauge lift `tau_0=1`, `tau_{j+1}=Q_j tau_j`.  Since the jump is exactly half the coefficient period, fold residues `j` and `j+p/2`.

After the standard local Pauli gauge, a folded site is of type

\[
G:\quad V_g=2\cos\beta\,\sigma_x
\]

or

\[
D:\quad V_d=2\sin\beta\,\sigma_y,
\]

where `z=e^{2i beta}`.  A direct reconstruction from (1.1) gives the folded onsite word

\[
\boxed{
G(DDGG)^rG.
}
\tag{2.1}
\]

Thus every increase `r -> r+1` inserts one copy of the same four-site bulk motif `DDGG`.

The cyclic gap sequence of the positive flux sites consists of `2r-1` gaps equal to `2` and one gap equal to `4r+6`.  The unique large gap must be fixed by every translation symmetry of the defect set, hence only the zero translation preserves the word.  Therefore the primitive period is `8r+4`.

---

## 3. Bulk transfer reduction

At the squared test energy

\[
y_0=\frac{31}{4},
\]

let

\[
d=z+z^{-1}\in[-2,2].
\]

Write `T_g,T_d` for the one-site `4 x 4` transfers of the folded `G,D` sites and put

\[
B=T_g^2T_d^2.
\]

(The alternative order `T_d^2T_g^2` is conjugate and has the same minimal polynomial.)

By `DDGG_BULK_UNIFORM_HYPERBOLICITY.md`,

\[
\boxed{
B^2-\mathcal A(d)B+I_4=0,
\qquad
\mathcal A(d)=\frac{129}{16}-d^2.
}
\tag{3.1}
\]

Since `|d|<=2`,

\[
\mathcal A(d)\ge\frac{65}{16}>2.
\]

For

\[
\xi(d)=\frac{\mathcal A(d)}2,
\qquad
u=U_{r-1}(\xi),
\qquad
v=U_{r-2}(\xi),
\]

we therefore have

\[
B^r=uB-vI_4.
\tag{3.2}
\]

The folded word (2.1) has monodromy `T_g B^r T_g` up to the harmless cyclic convention in the transfer ordering.  Substitution of (3.2) into the exact Bloch closing determinant, followed by the Chebyshev identity

\[
u^2+v^2-\mathcal Auv=1,
\tag{3.3}
\]

gives the following exact scalar formula.

---

## 4. Exact matching polynomial at `31/4`

Define

\[
\boxed{
\begin{aligned}
\alpha(d)
={}&\frac1{4096}\bigl(
4096d^6-30720d^5-16640d^4+495360d^3\\
&\hspace{17mm}-481296d^2-1919096d+2782657
\bigr),\\[1mm]
\beta(d)
={}&\frac{(4d-15)(64d^3-240d^2-644d+1455)}{256},\\[1mm]
\gamma(d)
={}&\frac{16d^2-136d+193}{16}.
\end{aligned}}
\tag{4.1}
\]

Then the exact characteristic value is

\[
\boxed{
\det(\sqrt{y_0}I-H_{Q^{(r)}}(z))
=\alpha(d)u^2+\beta(d)uv+\gamma(d).
}
\tag{4.2}
\]

The normalization in (4.2) agrees with all previous finite certificates.  For example at `r=2`,

\[
\alpha u^2+\beta uv+\gamma
=2^{-20}a_{20}(d)b_{20}(d),
\]

where

\[
a_{20}(d)=16d^2+16d-101
\]

and `b_20` is exactly the degree-eight Sturm polynomial from `PERIOD20_FOUR_DEFECT_BEATS_TWO_DEFECT_THEOREM.md`.  At `r=3` it is exactly `2^-28` times the period-28 Sturm polynomial recorded in `PERIOD28_SIX_DEFECT_BEATS_TWO_DEFECT_THEOREM.md`.

---

## 5. Uniform positivity on the Bloch circle

Because `mathcal A>2`,

\[
0<t_r:=\frac vu<1,
\qquad
u\ge\mathcal A,
\tag{5.1}
\]

for every `r>=2`.  Moreover the recurrence

\[
t_{r+1}=\frac1{\mathcal A-t_r},
\qquad t_2=\frac1{\mathcal A},
\]

implies

\[
\boxed{t_r\ge\frac1{\mathcal A}.}
\tag{5.2}
\]

Divide (4.2) by `u^2`:

\[
F_r(d)=\alpha(d)+\beta(d)t_r+\frac{\gamma(d)}{u^2}.
\tag{5.3}
\]

We prove `F_r(d)>0` on three fixed rational intervals.

### Region I: `-2 <= d <= 9/5`

On this interval

\[
\alpha>0,
\qquad
\alpha+\beta>0,
\qquad
\gamma>0.
\tag{5.4}
\]

These are elementary fixed-polynomial inequalities.  An exact Bernstein certificate on `[-2,9/5]` gives, after clearing the displayed denominators, minimum Bernstein coefficients respectively

\[
\frac{655990561}{15625},
\qquad
\frac{867666961}{15625},
\qquad
\frac1{25},
\]

all positive.

Since `0<t_r<1`,

\[
\alpha+\beta t_r\ge\min\{\alpha,\alpha+\beta\}>0,
\]

and (5.3) is positive.

### Region II: `9/5 <= d <= 19/10`

Here

\[
\beta>0,
\qquad
\alpha>0,
\qquad
\alpha+\gamma>0.
\tag{5.5}
\]

Again all three assertions have exact positive Bernstein coefficients on the stated rational interval.  If `gamma>=0`, then `F_r>alpha>0`.  If `gamma<0`, then `u>=1` gives

\[
\frac\gamma{u^2}\ge\gamma,
\]

so

\[
F_r\ge\alpha+\gamma>0.
\]

### Region III: `19/10 <= d <= 2`

On this interval

\[
\beta>0,
\qquad
\gamma<0.
\]

Using (5.1)--(5.2),

\[
F_r(d)
\ge
\alpha+\frac\beta{\mathcal A}
+\frac\gamma{\mathcal A^2}.
\tag{5.6}
\]

The right side factors exactly as

\[
\boxed{
\frac{a_{20}(d)b_{20}(d)}
{4096(16d^2-129)^2}.
}
\tag{5.7}
\]

The quadratic `a_20` is strictly negative on `[-2,2]`: its two roots are

\[
\frac{-2\pm\sqrt{105}}4,
\]

which lie outside that interval.  The exact Sturm calculation already recorded for period twenty proves that `b_20` has no root on `[-2,2]`, and `b_20(0)<0`.  Hence `b_20<0` throughout `[-2,2]`.  Therefore (5.7) is strictly positive.

Combining the three regions proves

\[
\boxed{
\det(\sqrt{31/4}I-H_{Q^{(r)}}(z))>0
\quad\text{for every }|z|=1,\ r\ge2.
}
\tag{5.8}

Thus no Bloch fiber has a squared eigenvalue equal to `31/4`.

---

## 6. Uniform reference-fiber inertia

It remains to determine on which side of the separator the spectrum lies.  Use the reference fiber `z=1` and keep the squared energy `y` variable.

Put

\[
\mathcal A_y=y^2-8y+6,
\qquad
u_y=U_{r-1}(\mathcal A_y/2),
\qquad
v_y=U_{r-2}(\mathcal A_y/2).
\]

The same transfer reduction gives

\[
\boxed{
P_r(y)
=A_6(y)u_y^2+B_4(y)u_yv_y+C_2(y),
}
\tag{6.1}
\]

where

\[
\boxed{
\begin{aligned}
A_6(y)
={}&(y^3-14y^2+52y-28)(y^3-14y^2+54y-40),\\
B_4(y)
={}&-(y-8)(y-6)(y^2-6y+4),\\
C_2(y)
={}&(y-8)(y-4).
\end{aligned}}
\tag{6.2}
\]

For `y>=31/4`, `mathcal A_y>2`.

### `31/4 <= y <= 8`

Here `B_4>=0` and `C_2<=0`.  As above,

\[
\frac{v_y}{u_y}\ge\frac1{\mathcal A_y},
\qquad
u_y\ge\mathcal A_y.
\]

Therefore

\[
\frac{P_r(y)}{u_y^2}
\ge
A_6+\frac{B_4}{\mathcal A_y}
+\frac{C_2}{\mathcal A_y^2}.
\tag{6.3}
\]

The numerator of the right side is

\[
\begin{aligned}
&(y^5-22y^4+171y^3-542y^2+589y-200)\\
&\qquad\times
(y^5-22y^4+171y^3-542y^2+589y-196).
\end{aligned}
\tag{6.4}
\]

After the shift

\[
y=31/4+s,
\qquad s\ge0,
\]

the product (6.4) expands as

\[
\begin{aligned}
&s^{10}+\frac{67}{2}s^9+\frac{7357}{16}s^8+\frac{26585}{8}s^7
+\frac{1734921}{128}s^6\\
&\quad+\frac{8002617}{256}s^5+\frac{80430169}{2048}s^4
+\frac{50614265}{2048}s^3\\
&\quad+\frac{447501933}{65536}s^2
+\frac{74127107}{131072}s
+\frac{10728465}{1048576},
\end{aligned}
\tag{6.5}
\]

whose coefficients are all strictly positive.  Hence `P_r(y)>0`.

### `y >= 8`

Now `B_4<=0` and `C_2>=0`.  Since `v_y/u_y<1`,

\[
\frac{P_r(y)}{u_y^2}
>A_6+B_4.
\]

Writing `y=8+s`,

\[
\boxed{
A_6+B_4
=s^6+20s^5+141s^4+420s^3+520s^2+208s+32>0.
}
\tag{6.6}
\]

Thus

\[
P_r(y)>0
\qquad(y\ge31/4).
\tag{6.7}
\]

The chiral fiber polynomial `det(lambda I-H(1))` is a polynomial in `y=lambda^2`, and its roots are exactly the squared fiber eigenvalues.  Equation (6.7) therefore shows that the reference fiber has no squared eigenvalue at or above `31/4`.

Together with the no-crossing statement (5.8) and connectedness of the Bloch circle, this proves Theorem A.

---

## 7. Comparison with every two-defect phase

For `r=2`, the period-twenty theorem already gives the exact certificate

\[
R_{2\rm def}^{(20)}>31/4.
\]

For `r>=3`, the exact fixed-period two-defect classification shows that its optimal geometry has longer soft length

\[
M=r+1.
\]

The universal endpoint Dirichlet upper bound on the two-defect gap gives

\[
8-R_{2\rm def}^{(8r+4)}
< D_{r+1}
:=2-2\cos\frac{\pi}{2(r+1)}.
\]

Since `r+1>=4`,

\[
D_{r+1}\le D_4
=2-2\cos\frac\pi8
<\frac14.
\]

Hence

\[
R_{2\rm def}^{(8r+4)}>31/4
\qquad(r\ge3).
\]

This proves Theorem B for every `r>=2`.

---

## 8. Consequences

The previously separate exact constructions at periods `20,28,36` are the first three members of one analytic family:

\[
\boxed{
G(DDGG)^rG,
\qquad r=2,3,4,\ldots.
}
\]

Their defect counts are

\[
2r=2\left\lfloor\frac{p-4}{8}\right\rfloor.
\]

Thus one half of the observed staircase is now an infinite theorem, not a finite pattern.

The remaining complementary staircase `p=8r` requires the analogous matching analysis for the `DDDD/GGGG` dislocation in the same uniformly hyperbolic `DDGG` bulk.