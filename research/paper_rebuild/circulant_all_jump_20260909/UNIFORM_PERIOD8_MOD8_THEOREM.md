# A second uniform period-eight phase: jumps `s = 4 mod 8`

Date: 2026-09-09

Status: **Proved**. This note belongs only to Paper I. It concerns one explicit infinite periodic signing and makes no assertion about minimization over all finite signings.

The result is the second arithmetic short-period theorem. Together with the `s=2 mod 4` theorem, it shows that every even jump not divisible by eight already admits a fixed period-eight signing with a spectral gap bounded uniformly away from zero.

## 1. The fixed word and the statement

Fix

\[
\tau^\dagger=(-1,1,1,-1,-1,1,-1,1),
\]

extended with period eight. For an even jump `s`, define

\[
(A_sx)_j=x_{j-1}+x_{j+1}
+\tau^\dagger_{j-s}x_{j-s}+\tau^\dagger_jx_{j+s}.
\]

Let `H_s(z)` be the eight-dimensional Bloch fiber under

\[
x_{j+8}=zx_j,
\qquad |z|=1,
\]

and put

\[
R_s^\dagger=\max_{|z|=1}\rho(H_s(z))^2.
\]

### Theorem A

For every

\[
s=8m+4\qquad(m\ge0),
\]

one has

\[
\boxed{
R_s^\dagger
<4+\sqrt{10+2\sqrt5}
<8.}
\]

Consequently

\[
\boxed{
8-R_s^\dagger
>4-\sqrt{10+2\sqrt5}>0,}
\]

uniformly over the whole congruence class `s=4 mod 8`.

The strict inequality is important: unlike the `s=2 mod 4` family, whose edge equals the displayed constant, the present family stays below it for every fixed jump, although the bound need not be uniformly separated from it as `s` varies.

---

## 2. Explicit eight-dimensional fiber

Write

\[
n=2m+1=s/4,
\qquad z=e^{it}.
\]

Since

\[
s=8m+4,
\]

a jump by `s` changes the residue modulo eight by four. Define

\[
a_m=z^m+z^{-(m+1)},
\qquad
b_m=z^m-z^{-(m+1)}.
\]

In the residue order `0,1,\ldots,7`, the nearest-neighbor part is the usual eight-cycle Bloch matrix, with boundary entries `z^{-1}` and `z`. The long-jump terms couple antipodal residues. The four upper-triangular antipodal entries are

\[
H_{0,4}=-a_m,
\qquad
H_{1,5}=a_m,
\qquad
H_{2,6}=b_m,
\qquad
H_{3,7}=-b_m,
\]

with the reverse entries their complex conjugates. Thus

\[
H_s(z)=
\begin{pmatrix}
0&1&0&0&-a_m&0&0&z^{-1}\\
1&0&1&0&0&a_m&0&0\\
0&1&0&1&0&0&b_m&0\\
0&0&1&0&1&0&0&-b_m\\
-\bar a_m&0&0&1&0&1&0&0\\
0&\bar a_m&0&0&1&0&1&0\\
0&0&\bar b_m&0&0&1&0&1\\
z&0&0&-\bar b_m&0&0&1&0
\end{pmatrix}.
\tag{2.1}
\]

This matrix is Hermitian for `|z|=1`.

---

## 3. Exact characteristic polynomial

Put

\[
y=\lambda^2,
\]

and introduce the three real phase variables

\[
c=z^{2n}+z^{-2n}=2\cos(2nt),
\]

\[
d=z^n+z^{-n}=2\cos(nt),
\qquad
e=z+z^{-1}=2\cos t.
\]

### Lemma B

The characteristic polynomial of (2.1) is even in `lambda` and equals

\[
\det(\lambda I-H_s(z))=P_n(y,t),
\]

where

\[
\boxed{
\begin{aligned}
P_n(y,t)={}&y^4-16y^3+(80-2c)y^2\\
&+(-128+16c)y+c^2-16c+4d-e+54.
\end{aligned}}
\tag{3.1}
\]

Equivalently, after centering `y=X+4`,

\[
\boxed{
P_n(X+4,t)
=X^4-(16+2c)X^2+c^2+16c+4d-e+54.}
\tag{3.2}
\]

#### Proof

Expand the determinant of `lambda I-H_s(z)` using (2.1). Before imposing the relation `z^m` between the long-jump phase and the basic Bloch phase, write `r=z^m`. Clearing the harmless denominator `r^8z^4`, the determinant numerator is

\[
\begin{aligned}
&r^8z^4\lambda^8-16r^8z^4\lambda^6\\
&\quad+\lambda^4\bigl(80r^8z^4-2r^{12}z^6-2r^4z^2\bigr)\\
&\quad+\lambda^2\bigl(-128r^8z^4+16r^{12}z^6+16r^4z^2\bigr)\\
&\quad+r^{16}z^8+r^{-0} -16r^{12}z^6-16r^4z^2
   +4r^{10}z^5+4r^6z^3-r^8z^5-r^8z^3+56r^8z^4,
\end{aligned}
\]

where the isolated `r^{-0}` notation means the constant `1` arising from the reciprocal extreme monomial. Dividing by `r^8z^4` and using

\[
r^4z^2=z^{4m+2}=z^{2n},
\qquad
r^2z=z^{2m+1}=z^n,
\]

turns the reciprocal monomial pairs into

\[
z^{\pm2n},\qquad z^{\pm n},\qquad z^{\pm1},\qquad z^{\pm4n}.
\]

Since

\[
z^{4n}+z^{-4n}=c^2-2,
\]

collecting coefficients gives exactly (3.1). Substitution `y=X+4` cancels the odd powers of `X` and yields (3.2).

The computation is a fixed `8 x 8` determinant identity; no limiting or numerical step is used.

---

## 4. Closed top branch

Regard (3.2) as a quadratic in

\[
W=X^2.
\]

Its two roots are

\[
\boxed{
W_\pm(t)=8+c\pm\sqrt{10-4d+e}.}
\tag{4.1}
\]

The largest squared eigenvalue is therefore

\[
\boxed{
Y_n(t)
=4+\sqrt{8+2\cos(2nt)
+\sqrt{10-8\cos(nt)+2\cos t}}.}
\tag{4.2}
\]

In particular

\[
R_s^\dagger=\max_{t\in\mathbb R}Y_n(t).
\]

---

## 5. Uniform strict bound

Set

\[
u=\cos(nt),
\qquad v=\cos t.
\]

Because

\[
2\cos(2nt)=4u^2-2,
\]

the inner quantity in (4.2) is

\[
W_+(t)=6+4u^2+\sqrt{10-8u+2v}.
\]

We prove

\[
W_+(t)<10+2\sqrt5.
\tag{5.1}
\]

The desired inequality is equivalent to

\[
\sqrt{10-8u+2v}
<4(1-u^2)+2\sqrt5.
\]

The right-hand side is positive. Squaring and subtracting the left-hand radicand gives

\[
\begin{aligned}
&\bigl(4(1-u^2)+2\sqrt5\bigr)^2
-(10-8u+2v)\\
&\qquad=
16(1-u^2)^2
+16\sqrt5(1-u^2)
+10+8u-2v.
\end{aligned}
\tag{5.2}
\]

Since `v<=1`, the last term obeys

\[
10+8u-2v\ge8(1+u)\ge0.
\]

Hence (5.2) is nonnegative. Equality in this lower bound would require simultaneously

\[
u=-1,\qquad v=1.
\]

But `v=1` means `t` is an integer multiple of `2pi`; because `n=2m+1` is odd, this forces `u=1`, not `-1`. Therefore (5.2) is in fact strictly positive for every `t`, proving (5.1).

Substitution into (4.2) gives

\[
Y_n(t)<4+\sqrt{10+2\sqrt5}
\]

for every phase. Compactness of the Bloch circle then gives the same strict inequality for its maximum. Since

\[
10+2\sqrt5<16,
\]

the right-hand side is below `8`. This proves Theorem A.

---

## 6. Arithmetic consequence

Combining this theorem with the independent `s=2 mod 4` period-eight theorem yields the following explicit periodic statement:

> Every even jump `s` with `8` not dividing `s` has a period-eight Hamilton-gauge signing whose continuous squared Bloch radius is strictly below `8` by at least
> \[
> 4-\sqrt{10+2\sqrt5}.
> \]

More precisely, the `s=2 mod 4` class attains the reference edge

\[
4+\sqrt{10+2\sqrt5},
\]

whereas the `s=4 mod 8` class lies strictly below it.

The only even jumps not covered by a fixed period-eight uniform-gap theorem are now those divisible by eight. This makes the `2`-adic valuation of the jump, rather than parity alone, the natural next structural parameter.
