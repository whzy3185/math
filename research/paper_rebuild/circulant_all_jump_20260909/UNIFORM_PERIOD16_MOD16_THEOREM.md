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

Because `s=16m+8`, the long jump changes a residue modulo sixteen by eight. In the sixteen-dimensional Bloch fiber, each antipodal pair receives two long-jump contributions carrying the phases `z^m` and `z^{-(m+1)}`.

Define

\[
d=z^n+z^{-n}=2\cos(nt),
\qquad
e=z+z^{-1}=2\cos t,
\]

and

\[
\boxed{
\begin{aligned}
F(x)={}&x^8-16x^7+72x^6+96x^5-1532x^4\\
&+2784x^3+5328x^2-21437x+17946.
\end{aligned}}
\tag{2.1}
\]

### Lemma B — exact generic threshold determinant

For every `m>=0` and every unit Bloch phase `z`, the characteristic polynomial of `H_s(z)` is even in `lambda`. If

\[
\det(\lambda I-H_s(z))=P_{m,z}(\lambda^2),
\]

then

\[
\boxed{P_{m,z}(8)=F(d)+d-e.}
\tag{2.2}
\]

#### Proof

Introduce an auxiliary variable

\[
r=z^m,
\qquad
w=r^2z=z^{2m+1}=z^n.
\]

Before imposing `r=z^m`, regard `r` and `z` as independent nonzero variables. For `0<=j<8`, the upper antipodal entry of the generic sixteen-dimensional fiber is

\[
 c_j=\tau_j^{\ddagger}r
     +\tau_{j+8}^{\ddagger}(rz)^{-1},
\]

and the reverse entry is

\[
 \bar c_j^{\rm alg}
 =\tau_j^{\ddagger}r^{-1}
  +\tau_{j+8}^{\ddagger}rz.
\]

Together with the nearest-neighbor sixteen-cycle and its seam entries `z^{-1},z`, these formulas specify the generic matrix algebraically.

At `lambda=2sqrt(2)`, direct elimination of this fixed `16 x 16` determinant gives

\[
\begin{aligned}
&\det(2\sqrt2 I-H(r,z))\\
={}&w^8+w^{-8}
-16(w^7+w^{-7})
+80(w^6+w^{-6})
-16(w^5+w^{-5})\\
&-1072(w^4+w^{-4})
+2928(w^3+w^{-3})
+336(w^2+w^{-2})\\
&-12684(w+w^{-1})+20920
-(z+z^{-1}).
\end{aligned}
\tag{2.3}
\]

This is a Laurent-polynomial identity in the independent variables `r,z`; in particular it is one calculation valid simultaneously for every `m`.

Now put

\[
x=w+w^{-1}.
\]

The recurrence

\[
S_0(x)=2,
\qquad S_1(x)=x,
\qquad S_{k+1}(x)=xS_k(x)-S_{k-1}(x)
\]

gives

\[
S_k(x)=w^k+w^{-k}.
\]

Substitution into (2.3) and elementary collection yield

\[
\det(2\sqrt2 I-H(r,z))
=F(x)+x-(z+z^{-1}).
\tag{2.4}
\]

Finally impose `r=z^m`, so `x=d`. This proves (2.2).

For completeness, applying the same generic determinant expansion before setting `lambda=2sqrt(2)` shows that only even powers of `lambda` occur. Equivalently, this evenness also follows from the signed-reflection chiral symmetry recorded in Section 6 below. Hence the notation `P_{m,z}(lambda^2)` is legitimate.

---

## 3. A Bernstein certificate for the threshold polynomial

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

the exact expansion is

\[
F(2-4u)-32
=\sum_{k=0}^8 b_kB_{k,8}(u),
\tag{3.2}
\]

with

\[
\begin{aligned}
(b_0,\ldots,b_8)=(&0,\frac{381}{2},\frac{7723}{7},\frac{58817}{14},
\frac{432814}{35},\\
&\frac{57457}{2},\frac{347521}{7},\frac{103659}{2},39156).
\end{aligned}
\tag{3.3}
\]

Every Bernstein basis function is nonnegative on `[0,1]`, and every coefficient except `b_0` is strictly positive. Thus (3.1) follows. If `u>0`, at least one positive-coefficient term is nonzero, so equality is impossible. Hence equality occurs only at `u=0`, i.e. `x=2`.

---

## 4. Positivity at the squared edge `8`

Since `d,e in [-2,2]`, Lemma C and (2.2) give

\[
\boxed{P_{m,z}(8)\ge32-4=28>0.}
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

For `y>=8`, `p_a'''(y)>0`, `p_a''(8)=80>0`, and `p_a'(8)=40>0`. Hence `p_a` is strictly increasing on `[8,infinity)` and has no root there. Since `H_s(1)` is Hermitian, all squared eigenvalues are nonnegative, and (4.2) gives

\[
\rho(H_s(1))^2<8.
\]

The Hermitian fibers depend continuously on `z` along the connected unit circle. By (4.1), no eigenvalue of `8I-H_s(z)^2` can pass through zero. Therefore its inertia is constant, and positivity at `z=1` propagates to every Bloch phase:

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

Then

\[
P_{m,z}(8)=\prod_{j=1}^8(8-y_j(z))\ge28.
\]

Every factor is at most `8`. Hence, with

\[
\delta(z)=8-\max_jy_j(z),
\]

we have

\[
28\le \delta(z)8^7.
\]

Thus

\[
\delta(z)\ge\frac{28}{8^7}
\]

for every phase. Taking the worst Bloch phase proves (1.2).

---

## 6. Signed-reflection chiral symmetry

The two-defect lift (1.1) obeys the exact reversal identity

\[
\boxed{\tau^{\ddagger}_{3-j}=-\tau^{\ddagger}_j}
\tag{6.1}
\]

with indices taken modulo sixteen. More generally, the analogous two-defect word of any even period `2L>=8`, obtained from `Q_0=Q_2=1` and all other `Q_j=-1`, obeys the same identity.

If the jump is `s=L(2q+1)`, then `s=L mod 2L`. Reflection of the infinite lattice about the index `L+3` sends a chord beginning at `j` to the chord beginning at `3-j`. Multiplication by the alternating diagonal `D_j=(-1)^j` reverses the sign of every nearest-neighbor edge and leaves an even-length chord unchanged. Equation (6.1) therefore supplies the missing minus sign on the chord terms. Thus alternating sign times reflection is a chiral symmetry of the infinite periodic operator.

On a fixed complex Bloch fiber, reflection reverses the Bloch phase; composing with complex conjugation gives the corresponding antiunitary chiral symmetry on the same fiber. Hence the spectrum is symmetric under `lambda -> -lambda`, conceptually explaining the even characteristic polynomial used above.

This symmetry is not special to period sixteen. It is the structural reason the same two-defect construction remains a viable candidate for all higher `2`-adic layers.

---

## 7. Emerging `2`-adic hierarchy

The three proved short-period layers are now:

1. `v_2(s)=1`, equivalently `s=2 mod 4`: a fixed period-eight phase has the exact uniform edge
   \[
   4+\sqrt{10+2\sqrt5};
   \]
2. `v_2(s)=2`, equivalently `s=4 mod 8`: a second period-eight phase stays strictly below the same edge;
3. `v_2(s)=3`, equivalently `s=8 mod 16`: the period-sixteen word (1.1) has a uniform positive gap, with the explicit elementary lower bound (1.2).

Thus every even jump not divisible by sixteen is now covered by a periodic word of period at most sixteen with a spectral gap bounded away from zero on its entire `2`-adic congruence class.

The remaining structural problem for Paper I is to determine whether the hierarchy continues for arbitrary `v_2(s)`, and whether one can give a construction whose period depends only on the `2`-adic valuation rather than linearly on `s`.
