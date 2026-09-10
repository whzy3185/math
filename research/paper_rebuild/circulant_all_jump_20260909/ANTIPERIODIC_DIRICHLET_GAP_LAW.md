# Sharp antiperiodic Dirichlet gap law

Date: 2026-09-10

Status: **Proved**. This complements the periodic-endpoint Robin/Dirichlet theory for general even defect separation.

## 1. Setup

Write

\[
L=2(N+m),\qquad h=2m,
\qquad N,m\ge1.
\]

For any odd multiplier `2q+1`, consider the even-separation two-defect Bloch fiber. At the antiperiodic phase

\[
z=-1,
\]

we have

\[
d=z^{2q+1}+z^{-(2q+1)}=-2.
\]

The spectrum of this fiber is independent of the sign choice induced by `q`, so write simply

\[
e^-_{N,m}:=8-\rho(H_{N,m,q}(-1))^2.
\]

We shall work in the macroscopic regime

\[
N\to\infty,
\qquad m\to\infty,
\qquad\frac mN\to\gamma\in(0,\infty).
\tag{1.1}
\]

The exact phase diagram implies that the antiperiodic fiber is sub-eight for all sufficiently large pairs in (1.1), because `T_N(3)` grows exponentially while `m=O(N)`.

## Theorem A — antiperiodic Dirichlet law

Under (1.1),

\[
\boxed{
 m^2 e^-_{N,m}
 \longrightarrow\frac{\pi^2}{4}.
}
\tag{1.2}
\]

Equivalently, the soft defect arc has the universal first Dirichlet quantization constant `pi/2`.

---

## 2. Exact antiperiodic characteristic equation

Let

\[
y=\lambda^2,
\]

and define

\[
a=\frac{y-2}{2},
\qquad
b=\frac{y-6}{2},
\]

\[
u=U_{N-1}(a),
\qquad
w=U_{N-2}(a),
\]

\[
p=U_{m-1}(b),
\qquad
v=U_{m-2}(b).
\]

A direct reduction of the `4 x 4` transfer determinant at `z=-1` gives

\[
\boxed{
\begin{aligned}
P^-_{N,m}(y)={}&
 y(y-8)(y^2-8y+10)p^2u^2\\
&-y(y-8)(y-6)p^2uw\\
&+(y^2-12y+16)p^2\\
&-y(y-8)(y-2)pvu^2\\
&+2y(y-8)pvuw\\
&+y(y-4)u^2+4.
\end{aligned}}
\tag{2.1}
\]

This is the monic characteristic polynomial of the antiperiodic fiber in the squared spectral variable.

At `y=8`, formula (2.1) reduces to

\[
32U_{N-1}(3)^2-16m^2+4
=4\bigl(T_N(3)^2-4m^2\bigr),
\]

recovering the exact threshold formula.

### Derivation of (2.1)

At `z=-1`, choose `eta=i`. In the block-Jacobi normal form,

\[
A_g=\lambda\sigma_z,
\qquad
A_d=\lambda\sigma_z+2i\sigma_x
\]

(up to a harmless unitary change when the sign of `sin beta` is reversed). Their scalar-square identities are

\[
A_g^2=yI,
\qquad
A_d^2=(y-4)I.
\]

The generic and defect transfer powers are therefore reduced by the two Chebyshev pairs `(u,w)` and `(p,v)`. Substitution into

\[
\det(\lambda I-H)
=-\eta^{-2}\det(M-\eta J)
\]

with `eta=i`, followed by the two identities

\[
u^2+w^2-(y-2)uw=1,
\]

\[
p^2+v^2-(y-6)pv=1,
\]

gives (2.1). No growing determinant remains.

---

## 3. A trial-state upper bound on the gap

At `z=-1`, the defect arc consists of `2m` consecutive sites with constant block onsite potential `2 sigma_y` up to unitary sign, and nearest-neighbor block `sigma_z`.

Consider the open defect arc with Dirichlet boundary conditions. Its sine mode

\[
f_j=\sin\frac{\pi j}{2m+1},
\qquad1\le j\le2m,
\]

reduces the block operator to

\[
2\cos\frac\pi{2m+1}\,\sigma_z+2\sigma_y.
\]

The squared eigenvalue of this `2 x 2` matrix is

\[
8-4\sin^2\frac\pi{2m+1}.
\]

Extend the corresponding vector by zero outside the defect arc. The two boundary leakage terms only increase `||Hv||^2`, so the Rayleigh quotient of `H^2` gives

\[
\rho(H(-1))^2
\ge8-4\sin^2\frac\pi{2m+1}.
\]

Therefore

\[
\boxed{
0<e^-_{N,m}
\le4\sin^2\frac\pi{2m+1}
=O(m^{-2}).
}
\tag{3.1}
\]

---

## 4. Soft angle and hard-channel asymptotics

Write

\[
g=e^-_{N,m}
\]

and define the soft angle `theta` by

\[
g=2-2\cos\theta,
\qquad0<\theta<\pi.
\tag{4.1}
\]

Then the top squared root is

\[
y=8-g=6+2\cos\theta,
\]

so

\[
b=\cos\theta
\]

and

\[
p=\frac{\sin(m\theta)}{\sin\theta},
\qquad
v=\frac{\sin((m-1)\theta)}{\sin\theta}.
\tag{4.2}
\]

The trial bound (3.1) implies

\[
\frac\theta2\le\frac\pi{2m+1},
\]

and hence

\[
0<m\theta<\pi.
\tag{4.3}
\]

For the generic channel,

\[
a=3-\frac g2\longrightarrow3.
\]

Write `a=cosh eta`. Since `N->infinity`,

\[
u=\frac{\sinh(N\eta)}{\sinh\eta}\longrightarrow\infty
\]

exponentially, and

\[
\boxed{
\frac wu\longrightarrow
\Lambda^{-1},
\qquad
\Lambda=3+2\sqrt2.
}
\tag{4.4}
\]

Because `m=O(N)`, the soft quantities `p,v` grow at most polynomially, so

\[
\frac{p^2}{u^2}\to0,
\qquad
\frac1{u^2}\to0.
\tag{4.5}
\]

---

## 5. Limiting quantization equation

Set

\[
x_{N,m}:=m\theta.
\]

By (4.3), every sequence has a subsequence on which

\[
x_{N,m}\to x\in[0,\pi].
\]

At the top root,

\[
P^-_{N,m}(8-g)=0.
\]

Divide (2.1) by `u^2`. As `g->0`, the coefficient limits are

\[
\frac{y(y-8)(y^2-8y+10)}g\to-80,
\]

\[
\frac{-y(y-8)(y-6)}g\to16,
\]

\[
\frac{-y(y-8)(y-2)}g\to48,
\]

\[
\frac{2y(y-8)}g\to-16,
\qquad
y(y-4)\to32.
\tag{5.1}
\]

Moreover, from (4.1)--(4.2),

\[
\begin{aligned}
gp^2
&=\sec^2(\theta/2)\sin^2(m\theta)
\longrightarrow\sin^2x,\\
gpv
&=\sec^2(\theta/2)
\sin(m\theta)\sin((m-1)\theta)
\longrightarrow\sin^2x.
\end{aligned}
\tag{5.2}
\]

Using (4.4)--(4.5), the normalized root equation therefore tends to

\[
\begin{aligned}
0={}&(-80+16\Lambda^{-1})\sin^2x\\
&+(48-16\Lambda^{-1})\sin^2x+32\\
={}&32\cos^2x.
\end{aligned}
\]

Thus

\[
\cos x=0.
\]

Since `x in [0,pi]`, necessarily

\[
\boxed{x=\frac\pi2.}
\tag{5.3}
\]

Every convergent subsequence has the same limit, so

\[
\boxed{m\theta\to\frac\pi2.}
\tag{5.4}
\]

---

## 6. Recovering the gap

Finally,

\[
\begin{aligned}
m^2e^-_{N,m}
&=4m^2\sin^2(\theta/2)\\
&=(m\theta)^2
\left(\frac{\sin(\theta/2)}{\theta/2}\right)^2
\longrightarrow\frac{\pi^2}{4}.
\end{aligned}
\]

This proves Theorem A.

## 7. Geometric corollary

If

\[
\frac hL=\frac m{N+m}\longrightarrow\alpha\in(0,1),
\]

then `m/N -> alpha/(1-alpha)` and

\[
\boxed{
L^2e^-_{N,m}
\longrightarrow\frac{\pi^2}{\alpha^2}.
}
\tag{7.1}
\]

Together with the previously proved periodic-endpoint law

\[
L^2e^+_{N,m}
\longrightarrow\frac{\pi^2}{(1-\alpha)^2},
\]

this exhibits the two complementary Dirichlet scales attached to the two macroscopic arcs.