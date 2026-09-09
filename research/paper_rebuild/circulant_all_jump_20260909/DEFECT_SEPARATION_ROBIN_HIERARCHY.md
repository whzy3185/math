# Defect-separation Robin hierarchy

Date: 2026-09-09

Status: **Proved** for the periodic Bloch phase `z=1`. This note belongs only to Paper I and concerns explicit periodic phases.

The purpose of this result is conceptual. The compressed two-defect theorem used two positive local flux defects at separation two. Allowing an arbitrary fixed even separation produces an infinite hierarchy of Robin constants. The previously proved constant

\[
4\arccos^2(1/3)
\]

is the first member, while the hierarchy converges monotonically to `pi^2`.

---

## 1. The separation-`2h` family

Fix an integer

\[
h\ge1.
\]

Let `L=2r` be even with

\[
r\ge h+2.
\]

On residues modulo `2L`, define the local flux word

\[
Q_0=Q_{2h}=1,
\qquad
Q_j=-1\quad(j\ne0,2h).
\tag{1.1}
\]

Choose the Hamilton-gauge lift with `tau_0=1`. Then the lift agrees with the alternating word except on the interval between the two defects:

\[
\tau_j=-(-1)^j\quad(1\le j\le2h),
\]

and

\[
\tau_j=(-1)^j
\quad(j=0\text{ or }2h+1\le j<2L).
\tag{1.2}
\]

The word satisfies the signed-reflection identity

\[
\boxed{
\tau_{2h+1-j}=-\tau_j
}
\tag{1.3}
\]

modulo `2L`. Hence for every jump `s=L(2q+1)` it has the same signed-reflection chiral symmetry as the separation-two family.

In this note we study the periodic Bloch phase `z=1`. At that phase the folded fiber is independent of the odd multiplier `2q+1`.

Let

\[
e_{L,h}:=8-\rho(H_{L,h}(1))^2.
\tag{1.4}
\]

---

## 2. Exact periodic-fiber factorization

Put

\[
y=\lambda^2,
\qquad
m=r-h-1,
\qquad
t=\frac{y-6}{2}.
\]

Define

\[
u=U_m(t),
\qquad
w=U_{m-1}(t),
\tag{2.1}
\]

with `U_{-1}=0`.

Introduce the two defect polynomials

\[
\boxed{
P_h(y)
=(y-6)U_h\!\left(\frac{y-2}{2}\right)
-6U_{h-1}\!\left(\frac{y-2}{2}\right),
}
\tag{2.2}
\]

and

\[
\boxed{
Q_h(y)
=2T_h\!\left(\frac{y-2}{2}\right).
}
\tag{2.3}
\]

### Proposition A — exact factorization

At the periodic Bloch phase,

\[
\boxed{
\det(\lambda I-H_{L,h}(1))
=p_{r,h}(y)\bigl(p_{r,h}(y)+4\bigr),
}
\tag{2.4}
\]

where

\[
\boxed{
p_{r,h}(y)=uP_h(y)-wQ_h(y)-2.}
\tag{2.5}
\]

#### Proof

After folding the period-`2L` cell into `L` two-component sites, the periodic phase has generic onsite block `2 sigma_x`, while the consecutive defect sites `1,...,2h` have zero onsite block. The transfer monodromy is therefore

\[
M=T(A_g)^{L-2h-1}T(A_d)^{2h}T(A_g),
\]

with

\[
A_g=\lambda\sigma_z-2i\sigma_y,
\qquad
A_d=\lambda\sigma_z.
\]

Since `L-2h-1=2m+1`, the generic power is

\[
T(A_g)^{2m+1}
=
\begin{pmatrix}
u A_g&-(u+w)I\\(u+w)I&-wA_g\end{pmatrix}.
\]

A direct multiplication of the fixed defect transfer `T(A_d)^{2h}` gives two scalar polynomial sequences. They satisfy

\[
P_h=(y-2)P_{h-1}-P_{h-2},
\]

\[
Q_h=(y-2)Q_{h-1}-Q_{h-2},
\]

with the initial data implied by (2.2)--(2.3); hence the closed Chebyshev forms there. Imposing the periodic closing involution and using

\[
u^2+w^2-(y-6)uw=1
\]

reduces the determinant exactly to (2.4)--(2.5).

For `h=1`,

\[
P_1(y)=y^2-8y+6,
\qquad
Q_1(y)=y-2,
\]

which recovers the factorization used in the compressed two-defect theorem.

---

## 3. No periodic-fiber root above eight

For `y>=8`, set

\[
x=\frac{y-2}{2}\ge3.
\]

The Chebyshev identity

\[
T_h(x)=U_h(x)-xU_{h-1}(x)
\]

gives

\[
\boxed{
P_h(y)-Q_h(y)
=(y-8)
\left[
U_h\!\left(\frac{y-2}{2}\right)
+U_{h-1}\!\left(\frac{y-2}{2}\right)
\right]
\ge0.
}
\tag{3.1}
\]

Also `u>= w>=0`. Therefore

\[
\begin{aligned}
p_{r,h}(y)+2
&=uP_h-wQ_h\\
&=(u-w)Q_h+u(P_h-Q_h)\\
&\ge Q_h(8).
\end{aligned}
\tag{3.2}
\]

Define

\[
\boxed{C_h:=T_h(3).}
\tag{3.3}
\]

Then

\[
P_h(8)=Q_h(8)=2C_h,
\]

so (3.2) implies

\[
p_{r,h}(y)\ge2C_h-2>0
\qquad(y\ge8).
\tag{3.4}
\]

The second factor in (2.4) is even larger. Thus the periodic fiber has no squared eigenvalue at or above eight.

---

## 4. Exact soft quantization equation

For a root below eight write

\[
y=6+2\cos\theta,
\qquad 0<\theta<\pi.
\tag{4.1}
\]

Then

\[
u=\frac{\sin((r-h)\theta)}{\sin\theta},
\qquad
w=\frac{\sin((r-h-1)\theta)}{\sin\theta}.
\]

Hence `p_{r,h}(y)=0` is exactly

\[
\boxed{
P_h(y)\sin((r-h)\theta)
-Q_h(y)\sin((r-h-1)\theta)
=2\sin\theta.
}
\tag{4.2}
\]

The equation `p_{r,h}(y)+4=0` has the same left side and right side `-2 sin theta`.

---

## 5. The Robin constant

Let

\[
\boxed{
\alpha_h:=\arccos\frac1{C_h}
=\arccos\frac1{T_h(3)}.
}
\tag{5.1}
\]

Because `C_h>1`,

\[
0<\alpha_h<\frac\pi2.
\]

Put

\[
\theta=\frac xr.
\]

Uniformly for `x` in compact subsets of `(0,pi)`,

\[
P_h(6+2\cos(x/r))=2C_h+O(r^{-2}),
\]

\[
Q_h(6+2\cos(x/r))=2C_h+O(r^{-2}).
\tag{5.2}
\]

Divide (4.2) by `2 sin(x/r)`. The difference quotient satisfies

\[
\frac{
\sin((r-h)x/r)-\sin((r-h-1)x/r)
}{\sin(x/r)}
\longrightarrow\cos x.
\tag{5.3}
\]

The contribution of `P_h-Q_h` vanishes in the limit because (3.1) is `O(r^-2)`. Therefore the scaled root equation converges locally uniformly to

\[
\boxed{C_h\cos x=1.}
\tag{5.4}
\]

The limiting equation has the unique root `x=alpha_h` in `(0,pi/2)`.
The derivative there is `-C_h sin(alpha_h) !=0`, so the implicit-function theorem (or uniform monotonicity in a fixed neighborhood) gives a unique root

\[
x_{r,h}\longrightarrow\alpha_h.
\tag{5.5}
\]

The root of the other factor converges instead to the solution of

\[
C_h\cos x=-1,
\]

namely `pi-alpha_h`, which is strictly farther from the edge `theta=0`. Thus the first root from (4.2) is the top squared eigenvalue for all sufficiently large `r`.

---

## 6. Sharp endpoint asymptotic

Since

\[
\theta_{r,h}=\frac{x_{r,h}}r,
\]

the periodic-fiber squared gap is

\[
e_{L,h}
=2-2\cos\theta_{r,h}.
\]

With `L=2r`, (5.5) yields

\[
\boxed{
L^2e_{L,h}
\longrightarrow
4\alpha_h^2
=4\arccos^2\!\frac1{T_h(3)}.
}
\tag{6.1}
\]

This is the defect-separation Robin hierarchy.

---

## 7. The constants form a strict bridge to `pi^2`

The values

\[
C_h=T_h(3)
\]

obey

\[
C_0=1,
\qquad
C_1=3,
\qquad
C_{h+1}=6C_h-C_{h-1}.
\tag{7.1}
\]

Thus

\[
C_1=3,
\quad
C_2=17,
\quad
C_3=99,
\quad
C_4=577,
\quad\ldots
\]

and `C_h` increases exponentially. Consequently

\[
\alpha_h=\arccos(1/C_h)
\]

increases strictly to `pi/2`, and therefore

\[
\boxed{
4\arccos^2\frac13
<4\arccos^2\frac1{17}
<4\arccos^2\frac1{99}
<\cdots<\pi^2.
}
\tag{7.2}
\]

In particular,

\[
\boxed{
4\arccos^2\frac1{T_h(3)}
\nearrow\pi^2.
}
\tag{7.3}
\]

The compressed constant `4 arccos^2(1/3)` is therefore not isolated. It is the first member of a canonical Robin family whose limiting value is exactly the `pi^2` constant appearing elsewhere in the periodic theory.

---

## 8. Scope and next target

Equation (6.1) is proved for the periodic Bloch phase `z=1` with fixed defect separation `2h` and `L->infinity`. It does **not yet** assert that `z=1` is globally maximizing for every fixed `h>1`.

Numerical experiments strongly indicate the stronger fixed-`h` statement

\[
L^2\bigl(8-R_{L,q}^{(h)}\bigr)
\longrightarrow
4\arccos^2\frac1{T_h(3)}
\]

uniformly in the odd multiplier, with eventual exact phase selection at `z=1`. That global extension is the next theorem to prove.
