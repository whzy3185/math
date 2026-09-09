# Sharp asymptotic constant for the compressed two-defect family

Date: 2026-09-09

Status: **Proved**. This note upgrades the quadratic estimate in `QUADRATIC_COMPRESSED_GAP_THEOREM.md` to the sharp leading constant for the global Bloch edge.

Let `L>=6` be even and let `q>=0`. For the period-`2L` two-defect phase of jump

\[
s=L(2q+1),
\]
write

\[
g_{L,q}:=8-\max_{|z|=1}\rho(H_{L,q}(z))^2.
\]

Set

\[
a:=\arccos\frac13.
\]

---

## Theorem A — sharp compressed gap

For every sequence of even integers `L -> infinity` and every sequence of integers `q=q(L)>=0`,

\[
\boxed{
L^2g_{L,q}\longrightarrow4a^2
=4\arccos^2\frac13.
}
\tag{A1}
\]

Equivalently, the convergence is uniform in the odd multiplier:

\[
\boxed{
\sup_{q\ge0}
\left|L^2g_{L,q}-4\arccos^2\frac13\right|
\longrightarrow0.
}
\tag{A2}
\]

Thus the compressed family has a second sharp spectral constant, distinct from the `pi^2` constant of the period-two/long-period asymptotic theory.

For `v_2(s)=k>=2`, taking `L=2^k` gives

\[
\boxed{
8-R_s^{\mathrm{comp}}
\sim
\frac{4\arccos^2(1/3)}{4^k},
}
\tag{A3}
\]

uniformly in the odd part of `s` as `k -> infinity`.

---

## 1. The periodic phase supplies the upper bound

At `z=1`, the fiber is independent of `q`. The previous quadratic-gap note proves that its top squared eigenvalue is

\[
6+2\cos\theta_L,
\]

where, writing `r=L/2`, the unique angle

\[
0<\theta_L<\frac{\pi}{2r}=\frac\pi L
\]

satisfies

\[
3\cos(r\theta_L)
+2\tan(\theta_L/2)\sin(r\theta_L)=1.
\tag{1.1}
\]

If

\[
a_L=r\theta_L,
\]

then

\[
a_L\to a=\arccos(1/3),
\]

and therefore the periodic-phase gap

\[
e_L:=8-\rho(H_{L,q}(1))^2
\]

obeys

\[
L^2e_L\to4a^2.
\tag{1.2}
\]

Since the global Bloch edge is at least its value at `z=1`,

\[
0<g_{L,q}\le e_L.
\tag{1.3}
\]

Consequently

\[
\limsup L^2g_{L,q}\le4a^2
\tag{1.4}
\]

uniformly in `q`. Also, from `theta_L<pi/L`,

\[
L^2g_{L,q}\le L^2e_L<\pi^2,
\tag{1.5}
\]

which gives the compactness needed below.

---

## 2. Maximizing phases and scaled variables

For each pair `(L,q)`, choose a Bloch phase `z_L` attaining the global edge and write

\[
y_L=8-g_{L,q}.
\]

Use the two phase variables from the transfer formula,

\[
d_L=\omega_L^2+\omega_L^{-2}
=2\cos((2q+1)t_L),
\]

\[
e_L^{\rm ph}=z_L+z_L^{-1}=2\cos t_L,
\]

where `z_L=e^{it_L}`.

Define the scaled quantities

\[
\gamma_L=L^2g_{L,q},
\qquad
D_L=L^2(2-d_L).
\tag{2.1}
\]

By (1.5),

\[
0<\gamma_L<\pi^2.
\tag{2.2}
\]

The characteristic equation is

\[
P(y_L,d_L,e_L^{\rm ph})=0,
\tag{2.3}
\]

with the exact formula

\[
P(y,d,e)=u^2\mathcal A(y,d)+uw\mathcal B(y,d)+\mathcal C(y,d,e)
\tag{2.4}
\]

from `QUADRATIC_COMPRESSED_GAP_THEOREM.md`, where

\[
u=U_m\!\left(\frac{y-d-4}{2}\right),
\qquad
w=U_{m-1}\!\left(\frac{y-d-4}{2}\right),
\qquad
m=\frac{L-4}{2}.
\]

---

## 3. Phase localization: `D_L` is bounded

### Lemma B

For any sequence of global maximizing phases,

\[
\boxed{D_L=O(1).}
\tag{3.1}
\]

#### Proof

Suppose instead that a subsequence has `D_L -> infinity`. Put

\[
\delta_L=2-d_L=D_L/L^2,
\qquad
g_L=\gamma_L/L^2.
\]

Because `gamma_L` is bounded, either `delta_L` has a positive limit along a further subsequence, or `delta_L ->0` but

\[
\delta_L/g_L\to\infty.
\]

In the first case, `y_L->8` and `d_L` stays a fixed distance below `2`. The Chebyshev argument

\[
\frac{y_L-d_L-4}{2}
\]

stays strictly above `1`. Hence `u_L->infinity` exponentially. At the threshold,

\[
A(d)>=0,\qquad B(d)<=0,
\]

and

\[
A(d)+B(d)>0\qquad(d<2).
\]

Since `0<=w_L/u_L<=1`, continuity gives

\[
\mathcal A(y_L,d_L)
+\frac{w_L}{u_L}\mathcal B(y_L,d_L)>c>0
\]

for all large `L`. Dividing (2.3) by `u_L^2` gives a contradiction because the scalar term is bounded.

Now suppose `delta_L->0` while `D_L->infinity`. Then

\[
\delta_L-g_L>0
\]

for all large `L`, and

\[
L\sqrt{\delta_L-g_L}\to\infty.
\]

Thus the Chebyshev argument is hyperbolic and again `u_L->infinity`; moreover

\[
u_L^2\delta_L\to\infty.
\tag{3.2}
\]

Expanding the two transfer coefficients at `(y,d)=(8,2)` gives

\[
\mathcal A(y_L,d_L)+\mathcal B(y_L,d_L)
=36(\delta_L-g_L)+o(\delta_L)>0.
\tag{3.3}
\]

In this regime `\mathcal B(y_L,d_L)<0`, so `w_L/u_L<=1` implies

\[
\mathcal A(y_L,d_L)
+\frac{w_L}{u_L}\mathcal B(y_L,d_L)
\ge
\mathcal A(y_L,d_L)+\mathcal B(y_L,d_L).
\]

By (3.2)--(3.3), the first two terms in (2.4) tend to `+infinity`, while `\mathcal C` remains bounded, again contradicting (2.3). This proves (3.1).

---

## 4. The continuum Chebyshev limit

By Lemma B and (2.2), after passing to a subsequence we may assume

\[
\gamma_L\to\gamma,
\qquad
D_L\to D,
\qquad
 e_L^{\rm ph}\to e_*\in[-2,2].
\tag{4.1}
\]

Set

\[
\xi=\gamma-D.
\tag{4.2}
\]

Then

\[
\frac{y_L-d_L-4}{2}
=1-\frac{\xi+o(1)}{2L^2}.
\tag{4.3}
\]

The standard Chebyshev scaling limit gives

\[
\frac{u_L}{L},\frac{w_L}{L}
\longrightarrow\Phi(\xi),
\tag{4.4}
\]

where

\[
\Phi(\xi)=
\begin{cases}
\displaystyle\frac{\sin(\sqrt\xi/2)}{\sqrt\xi},&\xi>0,\\[1.2ex]
\displaystyle\frac12,&\xi=0,\\[1.2ex]
\displaystyle\frac{\sinh(\sqrt{-\xi}/2)}{\sqrt{-\xi}},&\xi<0.
\end{cases}
\tag{4.5}
\]

Indeed, for `xi>0` write the argument as `cos(theta_L)` with `L theta_L->sqrt(xi)` and use

\[
U_m(\cos\theta)=\frac{\sin((m+1)\theta)}{\sin\theta};
\]

the hyperbolic case is identical with `cosh/sinh`.

The coefficient functions in (2.4) have the first-order expansions

\[
L^2\mathcal A(y_L,d_L)
\longrightarrow-84\gamma+60D,
\tag{4.6}
\]

\[
L^2\mathcal B(y_L,d_L)
\longrightarrow48\gamma-24D,
\tag{4.7}
\]

while

\[
\mathcal C(y_L,d_L,e_L^{\rm ph})
\longrightarrow34-e_*.
\tag{4.8}
\]

Substitution into the exact root equation (2.3) yields

\[
0=34-e_*-36\xi\Phi(\xi)^2.
\tag{4.9}
\]

---

## 5. The limiting variational inequality

If `xi<0`, then

\[
\xi\Phi(\xi)^2
=-\sinh^2(\sqrt{-\xi}/2),
\]

so the right side of (4.9) is strictly positive. Hence

\[
\xi\ge0.
\]

For `xi>=0`, (4.9) becomes

\[
\boxed{
36\sin^2\left(\frac{\sqrt\xi}{2}\right)
=34-e_*.
}
\tag{5.1}
\]

Because `e_*<=2`,

\[
\sin^2\left(\frac{\sqrt\xi}{2}\right)
\ge\frac89.
\tag{5.2}
\]

On the other hand, (1.5) and `D>=0` give

\[
0\le\xi\le\gamma\le\pi^2,
\]

so

\[
0\le\frac{\sqrt\xi}{2}\le\frac\pi2.
\]

The sine is increasing on this interval. Since

\[
\sin a=\frac{2\sqrt2}{3},
\qquad a=\arccos(1/3),
\]

(5.2) forces

\[
\frac{\sqrt\xi}{2}\ge a,
\]

and therefore

\[
\boxed{\xi\ge4a^2.}
\tag{5.3}
\]

Finally

\[
\gamma=D+\xi\ge4a^2.
\tag{5.4}
\]

Thus every subsequential limit of `L^2g_{L,q}` is at least `4a^2`. Together with the periodic-phase upper bound (1.4),

\[
\boxed{L^2g_{L,q}\to4a^2.}
\]

Because the argument allowed an arbitrary sequence `q=q(L)`, the convergence is uniform in `q`. This proves Theorem A.

---

## 6. Interpretation

The sharp constant arises from a genuine scaled variational law. In the window

\[
y=8-\gamma/L^2,
\qquad
d=2-D/L^2,
\]

the transfer determinant converges to

\[
34-e-36\sin^2\left(\frac{\sqrt{\gamma-D}}2\right).
\]

The phase displacement contributes the nonnegative cost `D`, while `e<=2` can only increase the required gap. The unique leading optimum is therefore

\[
D=0,
\qquad e=2,
\qquad
\gamma=4\arccos^2(1/3).
\]

So the periodic Bloch phase is asymptotically optimal even though an exact finite-`L` global-phase theorem is not required for the sharp limit.