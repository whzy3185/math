# Leading physical-seam tunneling correction at the compressed antiperiodic well

Date: 2026-09-14

Status: **Proved**.

This theorem refines the hostile-audit correction of the `m>N` regime.  It determines the first term that depends on the odd multiplier and lives beyond every algebraic `1/m` order.

## 1. Setup

Write

\[
L=2(N+m),
\qquad
1+\varepsilon\le m/N\le C,
\]

with `N,m->infinity`. Let

\[
n=2q+1
\]

be the compatible odd multiplier.

Define the convenient physical antiperiodic endpoint gap

\[
e^-_{N,m}:=8-\rho(H_{N,m,q}(-1))^2.
\]

At `z=-1`,

\[
d=-2,
\qquad e=-2.
\]

Among all physical phases with the same compressed coordinate `d=-2`, the seam coordinate is maximal at

\[
z_0=e^{\pm i\pi/n},
\]

where

\[
e_*=2\cos\frac\pi n.
\tag{1.1}
\]

Put

\[
U_N:=U_{N-1}(3),
\qquad
\Lambda=3+2\sqrt2.
\]

Then `U_N=Theta(Lambda^N)`.

## Theorem A — leading seam correction to the gap

Uniformly for `m/N` in compact subsets of `(1,infinity)` and uniformly over odd `n`,

\[
\boxed{
 e^-_{N,m}-\Gamma_{N,m,q}
=
\frac{(2+e_*)\pi^2}
{64\sqrt2\,U_N\,m^3}
\left(1+O(m^{-1})\right)
+O(U_N^{-2}m^{-6}).
}
\tag{1.2}

Equivalently,

\[
\boxed{
 e^-_{N,m}-\Gamma_{N,m,q}
=
\frac{4\cos^2(\pi/(2n))\,\pi^2}
{64\sqrt2\,U_N\,m^3}
\left(1+O(m^{-1})\right)
+O(U_N^{-2}m^{-6}).
}
\tag{1.3}

For `n=1`, the leading coefficient vanishes because `e_*=-2`; this is the genuine physical `z=-1` symmetry case.

Thus the first odd-multiplier dependence is exponentially small in the hard length `N`, with scale

\[
\boxed{U_N^{-1}m^{-3}=Theta(\Lambda^{-N}m^{-3}).}
\tag{1.4}

---

## Theorem B — exponentially small phase displacement

Choose the root

\[
z_0=e^{i\pi/n}
\]

and write a nearby physical phase as

\[
z=z_0e^{i\delta/n}.
\]

Let `delta_*` denote the compressed displacement of the maximizing phase. Then

\[
\boxed{
\delta_*
=-
\frac{\pi^2\sin(\pi/n)}
{64\sqrt2\,n\,U_N\,m^3}
\left(1+O(m^{-1})\right)
+O(U_N^{-2}m^{-6}).
}
\tag{1.5}

The conjugate maximizing phase has the opposite displacement.

In particular,

\[
\boxed{
|\delta_*|=O(U_N^{-1}m^{-3}).
}
\tag{1.6}

This is the correct finite seam-locking scale.

---

## 2. Exact characteristic equation at `d=-2`

At

\[
d=-2,
\]

write a near-edge squared root as

\[
y=6+2\cos\theta.
\]

Then the defect arc is oscillatory and the generic arc is hyperbolic. Put

\[
c=\cos\theta,
\]

\[
p=U_{m-1}(c)
=\frac{\sin(m\theta)}{\sin\theta},
\]

\[
u=U_{N-1}(2+c),
\qquad
X=T_N(2+c),
\]

and

\[
Z
=X\cos(m\theta)
+(c-1)(c+3)u\,p.
\tag{2.1}
\]

The all-energy single-square identity reduces exactly to

\[
\boxed{
P(y;-2,e)
=4\bigl(Z^2-1-4p^2\bigr)+(2-e).
}
\tag{2.2}

At `z=-1`, `e=-2`, so the top root is characterized by

\[
\boxed{Z=2p.}
\tag{2.3}

At another exact compressed-antiperiodic phase with seam coordinate `e`, equation (2.2) becomes

\[
\boxed{
Z^2=4p^2+\frac{2+e}{4}.
}
\tag{2.4}

Thus the physical seam changes the right side only by an `O(1)` quantity, while both the root derivative and the hard transfer grow exponentially.

---

## 3. Derivative of the soft root

Write

\[
R_N(\theta)=\frac{T_N(2+\cos\theta)}{U_{N-1}(2+\cos\theta)}.
\]

Equation (2.3) is equivalent to

\[
H(\theta)=0,
\]

where

\[
H(\theta)
=R_N(\theta)\cos(m\theta)
+\left((c-1)(c+3)-\frac2u\right)
\frac{\sin(m\theta)}{\sin\theta}.
\tag{3.1}
\]

The antiperiodic Dirichlet law gives

\[
m\theta\to\frac\pi2,
\qquad
\theta\sim\frac\pi{2m}.
\tag{3.2}
\]

The hard ratio satisfies

\[
R_N(\theta)=2\sqrt2+O(m^{-2})+O(\Lambda^{-2N}),
\]

and

\[
u=U_N\left(1+O(m^{-1})\right).
\tag{3.3}
\]

Differentiating (3.1), the dominant contribution is the derivative of the soft cosine:

\[
\boxed{
H'(\theta)
=-2\sqrt2\,m
\left(1+O(m^{-1})\right).
}
\tag{3.4}

Since

\[
\frac{dy}{d\theta}=-2\sin\theta,
\]

and

\[
Z-2p=uH,
\]

we obtain at the endpoint root

\[
\begin{aligned}
\frac d{dy}(Z^2-4p^2)
&=4p\frac d{dy}(Z-2p)\\
&=4pu\frac{H'(\theta)}{-2\sin\theta}\\
&=
\boxed{
\frac{16\sqrt2}{\pi^2}
U_Nm^3
\left(1+O(m^{-1})\right).
}
\tag{3.5}
\end{aligned}

Here we used

\[
p\sim\frac{2m}{\pi},
\qquad
\sin\theta\sim\frac\pi{2m}.
\]

---

## 4. Root response to the seam coordinate

Let

\[
F(y):=Z(y)^2-4p(y)^2.
\]

At the `z=-1` root,

\[
F(y_-)=0.
\]

For another exact `d=-2` root with seam `e`, (2.4) gives

\[
F(y_e)=\frac{2+e}{4}.
\]

By the implicit expansion and (3.5),

\[
\begin{aligned}
y_e-y_-
&=
\frac{2+e}{4F'(y_-)}
\left(1+O(m^{-1})\right)\\
&=
\boxed{
\frac{(2+e)\pi^2}
{64\sqrt2\,U_Nm^3}
\left(1+O(m^{-1})\right).
}
\tag{4.1}
\end{aligned}

Since the spectral gap is `8-y`, larger `e` decreases the gap. Taking `e=e_*` proves the leading term in (1.2).

---

## 5. Displacement away from exact `d=-2`

Parameterize around the best exact compressed-antiperiodic root:

\[
z=e^{i(\pi+\delta)/n}.
\]

Then

\[
d=-2+\delta^2+O(\delta^4)
\tag{5.1}
\]

and

\[
e=e_*
-\frac{2}{n}\sin\frac\pi n\,\delta
+O(\delta^2/n^2).
\tag{5.2}
\]

Changing `d+2` produces the direct soft mass cost

\[
\delta^2(1+O(m^{-1})),
\]

whereas by (4.1) the seam contribution to the gap is

\[
-
\frac{\pi^2}{64\sqrt2\,U_Nm^3}
(e-e_*)
\left(1+O(m^{-1})\right).
\]

Therefore the local gap has the form

\[
\begin{aligned}
g(\delta)-g(0)
={}&\delta^2
+
\frac{\pi^2\sin(\pi/n)}
{32\sqrt2\,n\,U_Nm^3}\delta\\
&+O(m^{-1}\delta^2)
+O(U_N^{-1}m^{-3}\delta^2)
+O(\delta^4).
\end{aligned}
\tag{5.3}

Minimizing this quadratic perturbation gives exactly (1.5). Its additional gain is `O(U_N^-2 m^-6)`, proving the final remainder in (1.2).

---

## 6. Significance

The `m>N` side contains two different beyond-all-orders effects:

1. **finite seam selection at exact `d=-2`:** size
   \[
   U_N^{-1}m^{-3};
   \]
2. **displacement away from `d=-2`:** size
   \[
   U_N^{-1}m^{-3}
   \]
   in phase and only
   \[
   U_N^{-2}m^{-6}
   \]
   in the gap.

Both are exponentially smaller than every algebraic Robin coefficient, which is why the entire `1/m` phase diagram is independent of the odd multiplier.