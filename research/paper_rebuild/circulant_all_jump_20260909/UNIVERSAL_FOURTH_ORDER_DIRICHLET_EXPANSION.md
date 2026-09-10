# Universal fourth-order Dirichlet expansion at both endpoint fibers

Date: 2026-09-10

Status: **Proved**. This refines `UNIVERSAL_DIRICHLET_BOUNDARY_SHIFT.md` by one further order.

## 1. Statement

Assume

\[
N,m\to\infty,
\qquad
m/N\to\gamma\in(0,\infty).
\]

Let `n` denote the soft pair length:

- `n=N` at the periodic endpoint `z=1`;
- `n=m` at the antiperiodic endpoint `z=-1`.

Let

\[
e_n=8-\rho(H(z_\pm))^2
\]

for the corresponding endpoint fiber.

### Theorem A — common fourth-order expansion

At either endpoint,

\[
\boxed{
 e_n
 =\frac{\pi^2}{4n^2}
 -\frac{\pi^2}{2\sqrt2\,n^3}
 +\left(\frac{3\pi^2}{8}-\frac{\pi^4}{192}\right)\frac1{n^4}
 +o(n^{-4}).
}
\tag{1.1}
\]

Equivalently, if the soft angle is written

\[
e_n=2-2\cos\theta_n,
\qquad
x_n=n\theta_n,
\]

then

\[
\boxed{
 x_n
 =\frac\pi2
 -\frac{\pi}{2\sqrt2\,n}
 +\frac{\pi}{4n^2}
 +O(n^{-3}).
}
\tag{1.2}
\]

The equality of the coefficients on the two endpoint sides is nontrivial: the antiperiodic calculation requires the second-order variation of the stable hard-channel ratio.

---

## 2. Periodic endpoint

After dividing the exact endpoint quantization equation by the exponentially large hard-block factor, one has

\[
\cos x-K(\theta)\tan(\theta/2)\sin x
=o(n^{-K_0})
\tag{2.1}
\]

for every fixed `K_0`, where

\[
x=n\theta
\]

and

\[
K(\theta)
=\frac{a+1}{\sqrt{a^2-1}},
\qquad
 a=2+\cos\theta.
\]

Since

\[
K(0)=\sqrt2,
\]

and `K` is even,

\[
K(\theta)=\sqrt2+O(\theta^2).
\]

Thus (2.1) is

\[
\cot x
=\frac{\theta}{\sqrt2}+O(\theta^3).
\tag{2.2}
\]

Put

\[
\varepsilon=\frac\pi2-x.
\]

Since `cot x=tan epsilon`, equation (2.2) gives

\[
\boxed{
\varepsilon
=\frac\theta{\sqrt2}+O(\theta^3).
}
\tag{2.3}
\]

But

\[
\theta=\frac{x}{n}
=\frac{\pi/2-\varepsilon}{n}.
\]

Substituting (2.3) once and iterating,

\[
\varepsilon
=\frac{\pi}{2\sqrt2\,n}
-\frac{\pi}{4n^2}
+O(n^{-3}).
\]

Hence (1.2) follows at `z=1`.

---

## 3. Antiperiodic endpoint and the stable-ratio cancellation

At `z=-1`, let

\[
y=6+2\cos\theta.
\]

The generic/hard pair parameter is

\[
a_h=\frac{y-2}{2}=2+\cos\theta.
\]

Its stable Chebyshev ratio is not exactly the endpoint constant `3-2sqrt(2)` but

\[
q(\theta)
=a_h-\sqrt{a_h^2-1}.
\tag{3.1}
\]

The exact antiperiodic characteristic formula, divided by the exponentially growing hard-channel square and with the hard ratio replaced by (3.1) up to exponentially small error, becomes a scalar expression

\[
\mathcal D(\theta,x)=0,
\qquad x=m\theta.
\]

Expanding this exact expression at `theta=0`, while keeping `x` independent, gives

\[
\begin{aligned}
\mathcal D(\theta,x)
={}&32\cos^2x
-16\sqrt2\,\theta\sin(2x)\\
&+\theta^2\bigl(28\sin^2x-12\bigr)
+O(\theta^3)
\end{aligned}
\tag{3.2}
\]

only if the stable ratio is frozen at zeroth order. The second-order expansion of `q(theta)` contributes exactly the missing correction. After the stable-ratio variation is included, put

\[
x=\frac\pi2-\varepsilon.
\]

The determinant expansion through total degree four in `(theta,epsilon)` takes the form

\[
\boxed{
\mathcal D
=32\left(\varepsilon-\frac\theta{\sqrt2}\right)^2
+O\bigl((|\varepsilon|+|\theta|)^4\bigr),
}
\tag{3.3}
\]

with no independent cubic or quadratic displacement term.

More explicitly, writing

\[
\varepsilon=a\theta+b\theta^2+O(\theta^3),
\]

the coefficient of `theta^2` in the exact normalized determinant is

\[
16(2a^2-2\sqrt2a+1),
\]

forcing

\[
a=1/\sqrt2.
\]

The coefficient of `theta^3` then vanishes identically. At order `theta^4`, after the `theta^2` correction in (3.1) is retained, the only dependence on `b` is

\[
32b^2.
\]

Therefore

\[
\boxed{b=0,}
\]

and hence

\[
\varepsilon
=\frac\theta{\sqrt2}+O(\theta^3).
\tag{3.4}
\]

The rest of the calculation is identical to the periodic side: substituting

\[
\theta=(\pi/2-\varepsilon)/m
\]

into (3.4) yields

\[
x_m
=\frac\pi2
-\frac{\pi}{2\sqrt2\,m}
+\frac{\pi}{4m^2}
+O(m^{-3}).
\]

Thus (1.2) holds at the antiperiodic endpoint as well.

---

## 4. Gap expansion

From (1.2), write

\[
\theta_n
=\frac\pi{2n}
-\frac\pi{2\sqrt2\,n^2}
+\frac\pi{4n^3}
+O(n^{-4}).
\]

Then

\[
2-2\cos\theta_n
=\theta_n^2-\frac{\theta_n^4}{12}+O(\theta_n^6).
\]

The square contributes

\[
\theta_n^2
=\frac{\pi^2}{4n^2}
-\frac{\pi^2}{2\sqrt2\,n^3}
+\frac{3\pi^2}{8n^4}
+O(n^{-5}),
\]

while

\[
\frac{\theta_n^4}{12}
=\frac{\pi^4}{192n^4}+O(n^{-5}).
\]

Subtracting proves (1.1).

## 5. Interpretation

To fourth order, the two macroscopic endpoint fibers are governed by the same effective soft length

\[
n+\frac1{\sqrt2}.
\]

The distinction between the periodic and antiperiodic geometries is therefore beyond this algebraic order; in balanced configurations their finite splitting is controlled by exponentially small tunneling through the complementary hard arc.