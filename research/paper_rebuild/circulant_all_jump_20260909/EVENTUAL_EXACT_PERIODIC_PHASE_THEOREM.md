# Eventual exact Bloch-phase selection for the compressed two-defect family

Date: 2026-09-09

Status: **Proved**. This note strengthens the sharp asymptotic and first-correction theorems. It concerns only the explicit compressed periodic family.

The main point is qualitative as well as quantitative: for all sufficiently large even half-periods, the periodic Bloch phase `z=1` is not merely asymptotically optimal; it is the **exact unique global maximizing phase**, uniformly in the odd jump multiplier.

---

## 1. Statement

Let `L>=6` be even, `q>=0`, and let

\[
R_{L,q}=\max_{|z|=1}\rho(H_{L,q}(z))^2,
\qquad
g_{L,q}=8-R_{L,q}
\]

for the period-`2L` compressed two-defect family.

At `z=1`, write

\[
e_L^{\rm end}:=8-\rho(H_{L,q}(1))^2.
\]

This is independent of `q`.

### Theorem A — eventual exact periodic phase

There exists an even integer `L_0` such that for every even

\[
L\ge L_0
\]

and every `q>=0`,

\[
\boxed{R_{L,q}=\rho(H_{L,q}(1))^2.}
\tag{1.1}
\]

Moreover `z=1` is the unique maximizing Bloch phase on the unit circle. Equivalently,

\[
\boxed{g_{L,q}=e_L^{\rm end}}
\tag{1.2}
\]

for every `q` once `L>=L_0`.

The threshold `L_0` is not optimized here. Direct exact/numerical audits suggest that (1.1) already holds for every even `L>=6`, but only the eventual theorem is asserted in this note.

---

## 2. Local scaled variables

Put

\[
h=L^{-1}.
\]

For a Bloch phase `z=e^{it}`, define

\[
d=2\cos((2q+1)t),
\qquad
e=2\cos t,
\]

and the nonnegative phase-displacement variables

\[
D=L^2(2-d),
\qquad
E=2-e.
\tag{2.1}
\]

For a squared edge

\[
y=8-\gamma h^2,
\]

the exact characteristic formula from the compressed-family transfer theorem gives a scalar root equation

\[
\mathcal F(h,\gamma,D,E)=0.
\tag{2.2}
\]

Near

\[
(h,\gamma,D,E)
=(0,\Gamma_0,0,0),
\qquad
\Gamma_0=4a^2,
\qquad
a=\arccos(1/3),
\]

the apparent singularity caused by the growing Chebyshev degree is removable. Indeed, with

\[
\xi=\gamma-D
\]

and

\[
\theta(h,\xi)
=\arccos\left(1-\frac{\xi h^2}{2}\right),
\]

one has

\[
\frac{\theta(h,\xi)}h
=\sqrt\xi+O(h^2)
\]

real-analytically for `xi` near `Gamma_0>0`. Since

\[
m=\frac1{2h}-2,
\]

the normalized Chebyshev factors can be written as

\[
hU_m(\cos\theta)
=h\frac{\sin((m+1)\theta)}{\sin\theta},
\]

\[
hU_{m-1}(\cos\theta)
=h\frac{\sin(m\theta)}{\sin\theta}.
\]

The arguments

\[
(m+1)\theta
=\frac{\theta}{2h}-\theta,
\qquad
m\theta
=\frac{\theta}{2h}-2\theta
\]

therefore have real-analytic extensions at `h=0`. Hence the exact characteristic equation has a real-analytic extension in `(h,\gamma,D,E)` near the base point.

Its limiting value is

\[
\boxed{
\mathcal F(0,\gamma,D,E)
=32+E
-36\sin^2\left(\frac{\sqrt{\gamma-D}}2\right).
}
\tag{2.3}
\]

---

## 3. The local spectral branch

At the base point,

\[
\mathcal F(0,\Gamma_0,0,0)=0.
\]

Moreover

\[
\partial_\gamma\mathcal F(0,\Gamma_0,0,0)
=-\frac{2\sqrt2}{a}\ne0.
\tag{3.1}
\]

Therefore the real-analytic implicit-function theorem gives a neighborhood

\[
\mathcal U
\]

of `(h,D,E)=(0,0,0)` and a unique real-analytic function

\[
\boxed{\gamma=\Gamma(h,D,E)}
\tag{3.2}
\]

such that every root with `\gamma` near `Gamma_0` is given by (3.2).

Differentiate (2.3) at the base point. Since the limiting function depends on `\gamma-D`,

\[
\partial_D\mathcal F
=-\partial_\gamma\mathcal F
\]

there. Hence

\[
\boxed{
\partial_D\Gamma(0,0,0)=1.
}
\tag{3.3}
\]

Also

\[
\partial_E\mathcal F(0,\Gamma_0,0,0)=1,
\]

so

\[
\boxed{
\partial_E\Gamma(0,0,0)
=-\frac{1}{\partial_\gamma\mathcal F}
=\frac{a}{2\sqrt2}>0.
}
\tag{3.4}
\]

By continuity, after shrinking `\mathcal U` if necessary there are constants

\[
c_D>0,
\qquad c_E>0
\]

such that throughout `\mathcal U`,

\[
\boxed{
\partial_D\Gamma\ge c_D,
\qquad
\partial_E\Gamma\ge c_E.
}
\tag{3.5}
\]

Consequently, for `D,E>=0` with `(h,D,E) in\mathcal U`,

\[
\begin{aligned}
\Gamma(h,D,E)-\Gamma(h,0,0)
&=\int_0^1
\left[
D\,\partial_D\Gamma(h,tD,tE)
+E\,\partial_E\Gamma(h,tD,tE)
\right]dt\\
&\ge c_DD+c_EE.
\end{aligned}
\tag{3.6}
\]

In particular,

\[
\boxed{
\Gamma(h,D,E)>\Gamma(h,0,0)
\quad\text{whenever }D+E>0.
}
\tag{3.7}
\]

This is the local exact phase-selection inequality.

---

## 4. Global maximizers enter the local branch

The sharp global gap theorem proves uniformly in the odd multiplier that, for any global maximizing phase,

\[
\gamma_L:=L^2g_{L,q}\longrightarrow\Gamma_0,
\]

\[
D_L=L^2(2-d_L)\longrightarrow0,
\]

and

\[
E_L=2-e_L\longrightarrow0.
\tag{4.1}
\]

Because the convergence is uniform in `q`, there exists `L_0` such that for all even `L>=L_0`, every global maximizing root lies in the implicit-function neighborhood `\mathcal U`.

At the periodic phase `z=1`,

\[
D=E=0,
\]

and the endpoint theorem identifies its scaled gap with the same local branch:

\[
\gamma_L^{\rm end}
=L^2e_L^{\rm end}
=\Gamma(h,0,0).
\tag{4.2}
\]

For a global maximizing phase, (3.2) gives

\[
\gamma_L
=\Gamma(h,D_L,E_L).
\tag{4.3}
\]

But by definition of the global Bloch maximum,

\[
g_{L,q}\le e_L^{\rm end},
\]

so

\[
\gamma_L\le\Gamma(h,0,0).
\tag{4.4}
\]

On the other hand, (3.6) gives

\[
\gamma_L
\ge\Gamma(h,0,0)+c_DD_L+c_EE_L.
\tag{4.5}
\]

Combining (4.4) and (4.5) forces

\[
\boxed{D_L=E_L=0.}
\tag{4.6}
\]

Since `E_L=2-(z+z^{-1})` and `|z|=1`, `E_L=0` implies

\[
z=1.
\]

Thus the periodic Bloch phase is the unique global maximizer and

\[
g_{L,q}=e_L^{\rm end}.
\]

This proves Theorem A.

---

## 5. Consequences

### 5.1 Full asymptotic expansion is endpoint-controlled

For all sufficiently large even `L`, the global compressed gap is exactly the endpoint gap. Hence every coefficient of the asymptotic expansion can be obtained from the single scalar Robin equation

\[
3\cos(r\theta)
+2\tan(\theta/2)\sin(r\theta)=1,
\qquad r=L/2.
\]

In particular the already proved expansion

\[
g_{L,q}
=\frac{4a^2}{L^2}
+\frac{16a^2}{3L^3}
+o(L^{-3})
\]

can be continued to arbitrary algebraic order, with coefficients independent of `q`.

### 5.2 No compressed-family phase slip at large period

The older period-`4s` family has a genuine nonzero phase slip at a higher order. The compressed two-defect family behaves differently: once `L` is large enough, the periodic phase is selected **exactly**, not merely to leading order.

### 5.3 Remaining finite problem

The natural finite strengthening is now sharply isolated:

> Prove that the same exact phase selection holds for every even `L>=6`, eliminating the unspecified threshold `L_0`.

This is a finite/uniform inequality problem inside the explicit periodic family and does not concern minimization over all signings.
