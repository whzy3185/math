# A uniform period-sixteen phase for jumps `s = 8 mod 16`

Date: 2026-09-09

Status: **Proved**. This note belongs only to Paper I. It concerns an explicit periodic signing and does not make any assertion about the minimum over all finite signings.

This is the third arithmetic short-period theorem. It covers the next `2`-adic layer after the two period-eight theorems.

## 1. The fixed period-sixteen word

Let the local flux word `Q` of length sixteen have

\[
Q_0=Q_2=1,
\qquad
Q_j=-1\quad(j\ne0,2).
\]

Choose the Hamilton-gauge lift with `tau_0=1`. Then

\[
\boxed{
\tau^{\ddagger}
=(1,1,-1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1).}
\tag{1.1}
\]

For a jump `s`, define the period-sixteen operator

\[
(A_sx)_j=x_{j-1}+x_{j+1}
+\tau^{\ddagger}_{j-s}x_{j-s}
+\tau^{\ddagger}_jx_{j+s}.
\]

Let `H_s(z)` be its sixteen-dimensional Bloch fiber under

\[
x_{j+16}=zx_j,
\qquad |z|=1,
\]

and define

\[
R_s^{[16]}=\max_{|z|=1}\rho(H_s(z))^2.
\]

### Theorem A

For every

\[
s=16m+8\qquad(m\ge0),
\]

one has

\[
\boxed{R_s^{[16]}<8.}
\]

In fact the gap is uniformly positive:

\[
\boxed{
8-R_s^{[16]}
\ge \frac{28}{8^7}.}
\tag{1.2}
\]

The constant in (1.2) is deliberately elementary rather than sharp. At the periodic phase `z=1`, the actual squared edge is approximately

\[
7.887839320581\ldots,
\]

but no numerical value is used in the proof.

---

## 2. Arithmetic phase reduction at the threshold

Write

\[
n=2m+1=s/8,
\qquad
z=e^{it}.
\]

Because `s=16m+8`, the long jump changes a residue modulo sixteen by eight. In the sixteen-dimensional Bloch fiber, each antipodal pair receives two long-jump contributions carrying the phases `z^m` and `z^{-(m+1)}`. A direct fixed-size determinant expansion has an especially simple form at the squared threshold `8`.

Define

\[
d= z^n+z^{-n}=2\cos(nt),
\qquad
e=z+z^{-1}=2\cos t,
\]

and the degree-eight polynomial

\[
\boxed{
\begin{aligned}
F(x)={}&x^8-16x^7+72x^6+96x^5-1532x^4\\
&+2784x^3+5328x^2-21437x+17946.
\end{aligned}}
\tag{2.1}
\]

### Lemma B — exact threshold determinant

For every `m>=0` and every unit Bloch phase `z`, the characteristic polynomial of `H_s(z)` is even in `lambda`. If

\[
\det(\lambda I-H_s(z))=P_{m,z}(\lambda^2),
\]

then

\[
\boxed{
P_{m,z}(8)=F(d)+d-e.}
\tag{2.2}
\]

#### Proof

The proof is a fixed `16 x 16` determinant identity. For `m=0`, collect reciprocal Laurent monomials in `z`. At `y=lambda^2=8` the result is exactly `F(z+z^{-1})`.

For general `m`, set

\[
w=z^n=z^{2m+1}.
\]

Expanding the same determinant before imposing the relation between the basic seam phase and the long-jump phase shows that every coefficient of a positive power of `lambda^2` is obtained from the `m=0` coefficient by the substitution `z -> w`. The constant coefficient has one additional seam correction,

\[
(w+w^{-1})-(z+z^{-1}).
\]

Therefore at `y=8`,

\[
P_{m,z}(8)=F(w+w^{-1})+(w+w^{-1})-(z+z^{-1}),
\]

which is (2.2). The same determinant expansion contains only even powers of `lambda`, proving the first assertion.

This identity is exact; it does not arise from sampling or asymptotic approximation.

---

## 3. A Bernstein certificate for the threshold polynomial

The key point is that `F` is uniformly large on the full phase interval.

### Lemma C

For every

\[
x\in[-2,2],
\]

one has

\[
\boxed{F(x)\ge32,}
\tag{3.1}
\]

with equality only at `x=2`.

#### Proof

Write

\[
x=2-4u,
\qquad 0\le u\le1.
\]

In the degree-eight Bernstein basis

\[
B_{k,8}(u)=\binom8k u^k(1-u)^{8-k},
\]

the polynomial `F(2-4u)-32` has the exact expansion

\[
F(2-4u)-32
=\sum_{k=0}^8 b_k B_{k,8}(u),
\tag{3.2}
\]

where

\[
\begin{aligned}
(b_0,\ldots,b_8)=(&0,\frac{381}{2},\frac{7723}{7},\frac{58817}{14},
\frac{432814}{35},\\
&\frac{57457}{2},\frac{347521}{7},\frac{103659}{2},39156).
\end{aligned}
\tag{3.3}
\]

Every Bernstein basis function is nonnegative on `[0,1]`, and every coefficient except `b_0` is strictly positive. Thus (3.1) follows. If `u>0`, at least one positive-coefficient Bernstein term is nonzero, so equality is impossible. Hence equality occurs only at `u=0`, i.e. `x=2`.

---

## 4. Positivity at the squared edge `8`

Since `d,e in [-2,2]`, Lemma C and (2.2) give

\[
\boxed{
P_{m,z}(8)
\ge32-4=28>0.}
\tag{4.1}
\]

Thus no squared Bloch eigenvalue can cross the value `8` as the phase varies.

It remains to fix the inertia in one fiber. At `z=1`, the matrix is independent of `m`. Its characteristic polynomial factors exactly as

\[
\begin{aligned}
\det(\lambda I-H_s(1))={}&
\bigl(y^4-20y^3+136y^2-344y+196\bigr)\\
&\times
\bigl(y^4-20y^3+136y^2-344y+200\bigr),
\qquad y=\lambda^2.
\end{aligned}
\tag{4.2}
\]

For

\[
p_a(y)=y^4-20y^3+136y^2-344y+a,
\qquad a\in\{196,200\},
\]

we have

\[
p_{196}(8)=4,
\qquad p_{200}(8)=8.
\]

Moreover

\[
p_a'(y)=4y^3-60y^2+272y-344,
\]

\[
p_a''(y)=12y^2-120y+272,
\qquad
p_a'''(y)=24y-120.
\]

For `y>=8`, `p_a'''(y)>0`, `p_a''(8)=80>0`, and `p_a'(8)=40>0`. Hence `p_a` is strictly increasing on `[8,infinity)` and has no root there. Because `H_s(1)` is Hermitian, all its squared eigenvalues are real and nonnegative, so (4.2) implies

\[
\rho(H_s(1))^2<8.
\]

The Hermitian fibers depend continuously on `z` along the connected unit circle. By (4.1), no eigenvalue of `8I-H_s(z)^2` can pass through zero. Therefore the inertia of `8I-H_s(z)^2` is constant, and positivity at `z=1` propagates to every Bloch phase:

\[
8I-H_s(z)^2>0.
\]

This proves the strict part of Theorem A.

---

## 5. Uniform quantitative gap

Because the characteristic polynomial is even, write its eight nonnegative squared roots as

\[
y_1(z),\ldots,y_8(z).
\]

The preceding section shows `0<=y_j(z)<8`. Equation (2.2) gives

\[
P_{m,z}(8)=\prod_{j=1}^8(8-y_j(z))\ge28.
\]

Each factor is at most `8`, so if

\[
\delta(z)=8-\max_j y_j(z),
\]

then

\[
28\le \delta(z)8^7.
\]

Hence

\[
\delta(z)\ge\frac{28}{8^7}
\]

for every phase. Taking the worst Bloch phase proves (1.2).

---

## 6. Emerging `2`-adic hierarchy

The three proved short-period layers are now:

1. `v_2(s)=1`, equivalently `s=2 mod 4`: a fixed period-eight phase has the exact uniform edge
   \[
   4+\sqrt{10+2\sqrt5};
   \]
2. `v_2(s)=2`, equivalently `s=4 mod 8`: a second period-eight phase stays strictly below the same edge;
3. `v_2(s)=3`, equivalently `s=8 mod 16`: the period-sixteen word (1.1) has a uniform positive gap, with the explicit elementary lower bound (1.2).

Thus every even jump not divisible by sixteen is now covered by a periodic word of period at most sixteen with a spectral gap bounded away from zero on its entire `2`-adic congruence class.

The remaining structural problem for Paper I is no longer merely to improve the old period-`4s` estimate. It is to determine whether this hierarchy continues for arbitrary `v_2(s)`, and whether one can give a uniform construction whose period depends only on the `2`-adic valuation rather than linearly on `s`.
