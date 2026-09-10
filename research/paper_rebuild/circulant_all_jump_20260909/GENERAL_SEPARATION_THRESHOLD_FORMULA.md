# Compact threshold formula for arbitrary even defect geometry

Date: 2026-09-10

Status: **Proved**. This note belongs only to Paper I.

This is the main algebraic reduction for the general even-separation family.

## 1. Parameters

Write

\[
L=2(N+m),
\qquad
h=2m,
\qquad
N,m\ge1.
\]

For a unit Bloch phase `z`, choose `eta^2=z` and put

\[
\omega=z^q\eta,
\qquad
\omega^2=z^{2q+1}.
\]

Define the two real phase variables

\[
\boxed{
d=\omega^2+\omega^{-2}\in[-2,2],
\qquad
e=z+z^{-1}\in[-2,2].}
\tag{1.1}
\]

At the squared spectral threshold `lambda^2=8`, put

\[
x=\frac{4-d}{2},
\qquad
y=\frac{4+d}{2}.
\tag{1.2}
\]

Thus `x,y in [1,3]` and `x+y=4`.

Set

\[
u=U_{N-1}(x),
\qquad
w=U_{N-2}(x),
\]

\[
p=U_{m-1}(y),
\qquad
q_0=U_{m-2}(y),
\tag{1.3}
\]

with `U_{-1}=0`, and define

\[
X=T_N(x)=xu-w,
\qquad
Y=T_m(y)=yp-q_0.
\tag{1.4}
\]

All six quantities `u,w,p,q_0,X,Y` are nonnegative on the phase interval.

## Theorem A — exact compact threshold determinant

For the arbitrary-even-separation two-defect fiber,

\[
\boxed{
P_{N,m,z}(8)=\mathcal F_{N,m}(d)-e,}
\tag{1.5}
\]

where

\[
\boxed{
\begin{aligned}
\mathcal F_{N,m}(d)-2
={}&\frac{(4-d^2)(20-d^2)}2\,p^2u^2\\
&+2(4-d^2)XYpu\\
&+(d^2+12d+4)p^2\\
&+(d^2-8d+12)u^2.
\end{aligned}}
\tag{1.6}
\]

No matrix dimension depending on `L` remains.

---

## 2. Proof from the block transfer matrix

Use the block-Jacobi reduction and the transfer notation

\[
T(A)=\begin{pmatrix}A&-I_2\\I_2&0\end{pmatrix}.
\]

At `lambda^2=8`, the generic and defect transfer coefficients satisfy

\[
A_g^2=(6-d)I_2,
\qquad
A_d^2=(6+d)I_2.
\]

The generic power of length `2N-1` is

\[
T(A_g)^{2N-1}
=
\begin{pmatrix}
u A_g&-(u+w)I_2\\
(u+w)I_2&-wA_g
\end{pmatrix}.
\tag{2.1}
\]

The defect power of length `2m` is

\[
T(A_d)^{2m}
=
\begin{pmatrix}
(U_m(y)+p)I_2&-pA_d\\
pA_d&-(p+q_0)I_2
\end{pmatrix}.
\tag{2.2}
\]

The monodromy is

\[
M=T(A_g)^{2N-1}T(A_d)^{2m}T(A_g),
\]

and the characteristic determinant is

\[
P_{N,m,z}(8)
=-\eta^{-2}\det(M-\eta J),
\qquad
J=\operatorname{diag}(\sigma_x,-\sigma_x).
\tag{2.3}
\]

Expanding this fixed `4 x 4` determinant and using the two Chebyshev identities

\[
u^2+w^2-2xuw=1,
\qquad
p^2+q_0^2-2ypq_0=1,
\tag{2.4}
\]

first collapses the boundary dependence to

\[
-(\eta^2+\eta^{-2})=-e.
\]

The remaining phase polynomial can initially be written as

\[
\begin{aligned}
\mathcal F-2={}&
p^2u^2(d^4-22d^2+72)
+p^2uw(d^3+4d^2-4d-16)\\
&+pq_0u^2(-d^3+4d^2+4d-16)
+pq_0uw(8-2d^2)\\
&+p^2(d^2+12d+4)
+u^2(d^2-8d+12).
\end{aligned}
\tag{2.5}
\]

Now substitute

\[
w=xu-X,
\qquad
q_0=yp-Y,
\]

with `x=(4-d)/2`, `y=(4+d)/2`. The mixed terms collapse and (2.5) becomes exactly (1.6).

This proves Theorem A.

---

## 3. Two endpoint specializations

At `d=2`, the first two terms and the `u^2` term vanish, giving

\[
\mathcal F_{N,m}(2)-2
=32\,U_{m-1}(3)^2
=4\bigl(T_m(3)^2-1\bigr)>0.
\tag{3.1}
\]

At `d=-2`,

\[
\mathcal F_{N,m}(-2)-2
=32\,U_{N-1}(3)^2-16m^2
=4\bigl(T_N(3)^2-4m^2-1\bigr).
\tag{3.2}
\]

For the physical antiperiodic phase `z=-1`, one has `e=-2`, so

\[
P_{N,m,-1}(8)
=\mathcal F(-2)+2
=4\bigl(T_N(3)^2-4m^2\bigr),
\]

recovering the exact antiperiodic obstruction theorem.

---

## 4. Universal localization of dangerous phases

The first two terms in (1.6) are nonnegative on `[-2,2]` because

\[
4-d^2\ge0,
\qquad
20-d^2>0,
\]

and all Chebyshev factors are nonnegative.

Also

\[
d^2-8d+12=(d-2)(d-6)\ge0
\qquad(-2\le d\le2).
\]

Thus the only coefficient in (1.6) that can be negative is

\[
d^2+12d+4.
\]

Its unique root in `[-2,2]` is

\[
\boxed{d_*=-6+4\sqrt2.}
\tag{4.1}
\]

Therefore, whenever

\[
\boxed{d\ge d_*=-6+4\sqrt2,}
\tag{4.2}
\]

we have

\[
\mathcal F_{N,m}(d)-2\ge0.
\]

Since `e<=2`, equation (1.5) gives

\[
\boxed{P_{N,m,z}(8)\ge0}
\]

throughout this whole phase region, with strict positivity except at impossible simultaneous degeneracies.

Hence any Bloch phase capable of producing a threshold crossing must satisfy

\[
\boxed{
d<-6+4\sqrt2\approx-0.34314575.}
\tag{4.3}
\]

Equivalently, the compressed long-jump phase must lie in a fixed neighborhood of the antiperiodic side of the phase circle.

## 5. Significance

The general separation problem has now been reduced to one explicit scalar inequality. The antiperiodic obstruction curve

\[
2m>T_N(3)
\]

captures one side of the phase diagram, while (4.3) shows that the entire converse problem is confined to a strict subinterval near `d=-2`.

The principal remaining theorem is to prove or disprove:

\[
2m<T_N(3)
\quad\Longrightarrow\quad
\mathcal F_{N,m}(d)>2
\text{ for every }d\in[-2,2].
\]

If true, this would give the exact global sub-eight classification for the complete even-separation two-defect family.