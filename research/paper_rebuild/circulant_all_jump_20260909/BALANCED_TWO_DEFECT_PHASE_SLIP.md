# Second-order phase slip for the balanced two-defect geometry

Date: 2026-09-10

Status: **Proved**. This is the second-order refinement of the balanced macroscopic optimum.

## 1. Balanced geometry and compressed phase

Let

\[
N=m=r\to\infty,
\qquad
L=4r,
\qquad
h=2r.
\]

The primitive coefficient period is `2L=8r`. Let the jump be

\[
s=L(2q+1),
\qquad q\ge0,
\]

where the odd multiplier may vary.

Write

\[
z=e^{i\phi},
\qquad
\psi:=(2q+1)\phi.
\]

The compressed long-phase coordinate is

\[
d=2\cos\psi.
\]

Let

\[
\Gamma_r:=8-\max_{|z|=1}\rho(H_{r,r,q}(z))^2
\]

be the full Bloch gap. Let

\[
e_r^+:=8-\rho(H(1))^2,
\qquad
e_r^-:=8-\rho(H(-1))^2,
\]

and put

\[
e_r:=\min\{e_r^+,e_r^-\}.
\]

The endpoint Dirichlet laws give

\[
r^2e_r\to\frac{\pi^2}{4}.
\tag{1.1}
\]

The difference `|e_r^+-e_r^-|` is exponentially small: after the two equal arcs are interchanged, the only distinction between the two endpoint quantizations is tunneling through the opposite hyperbolic arc, whose stable transfer ratio is `Lambda^{-r}` with

\[
\Lambda=3+2\sqrt2.
\tag{1.2}
\]

Thus either endpoint may be used at every algebraic order below.

## Theorem A — balanced phase-slip law

Let `z_r` be a global maximizing Bloch phase. Choose the closer compressed endpoint `epsilon_r in {+1,-1}` and write the compressed phase displacement as

\[
\psi_r=\psi_{\rm end}+\delta_r,
\qquad
\psi_{\rm end}\in\{0,\pi\},
\]

with `delta_r` chosen in `[-pi,pi]`.

Then

\[
\boxed{
r^2|\delta_r|
\longrightarrow
\frac{\pi}{4\sqrt2}.
}
\tag{1.3}
\]

Moreover

\[
\boxed{
r^4(e_r-\Gamma_r)
\longrightarrow
\frac{\pi^2}{32}.
}
\tag{1.4}
\]

Hence

\[
\boxed{
\Gamma_r
=e_r-\frac{\pi^2}{32r^4}+o(r^{-4}).
}
\tag{1.5}
\]

The constants are independent of the odd multiplier.

---

## 2. Boundary-layer localization

The full-Bloch macroscopic theorem gives

\[
r^2\Gamma_r\to\frac{\pi^2}{4}
\]

and the two-well localization in its proof forces every global maximizer into a neighborhood of either `d=2` or `d=-2`.

By symmetry it is enough to analyze the `d=2` well. Put

\[
\mu:=2-d=2-2\cos\delta\ge0.
\]

Let `g` denote the local squared gap at the top branch. On the soft generic arc define `theta` by

\[
g-\mu=2-2\cos\theta
\]

and set

\[
x=r\theta.
\]

Let `x_r^0` be the endpoint soft coordinate, so

\[
e_r^+=2-2\cos(x_r^0/r),
\qquad
x_r^0\to\frac\pi2.
\tag{2.1}
\]

The exact block-transfer equation has one soft and one hard channel. The hard consecutive-transfer ratio tends to

\[
\Lambda^{-1}=3-2\sqrt2.
\]

Subtracting the endpoint equation from the phase-shifted equation and using the local inverse bound at the first soft root gives

\[
|x-x_r^0|
\le C\left(\sqrt\mu+|g-e_r^+|+\mu+\Lambda^{-r}\right).
\tag{2.2}
\]

The gap identity

\[
g-e_r^+
=\mu+
\left(2-2\cos\frac xr\right)
-
\left(2-2\cos\frac{x_r^0}{r}\right)
\tag{2.3}
\]

and the fact that a global phase can only improve the best endpoint imply

\[
\sqrt\mu=O(r^{-2}),
\qquad
|x-x_r^0|=O(r^{-2}),
\qquad
|g-e_r|=O(r^{-4}).
\tag{2.4}
\]

Since

\[
\mu=\delta^2+O(\delta^4),
\]

this proves the boundary-layer scale

\[
\boxed{|\delta|=O(r^{-2}).}
\tag{2.5}
\]

The same argument applies at the `d=-2` well after interchanging the two arcs.

---

## 3. The universal cusp coefficient

Take

\[
\delta=\frac\zeta{r^2},
\qquad \zeta=O(1).
\]

Then

\[
r^2\sqrt\mu\to|\zeta|,
\qquad
r^4\mu\to\zeta^2.
\tag{3.1}
\]

The hard block has the same stable transfer root `Lambda` as in the original two-channel phase-slip calculation. After division by its dominant transfer factor, the square-root splitting term in the exact determinant is

\[
2\Lambda^{-1}\sqrt\mu+o(r^{-2}).
\tag{3.2}
\]

The normalized derivative of the soft Robin equation at the first Dirichlet root tends to

\[
-(1-\Lambda^{-2}).
\tag{3.3}
\]

Therefore the lower of the two locally split soft branches satisfies

\[
-(1-\Lambda^{-2})(x-x_r^0)
=2\Lambda^{-1}\sqrt\mu+o(r^{-2}).
\]

Using

\[
\frac{2\Lambda^{-1}}{1-\Lambda^{-2}}
=\frac1{2\sqrt2},
\]

we obtain

\[
\boxed{
r^2(x-x_r^0)
\longrightarrow
-\frac{|\zeta|}{2\sqrt2}.
}
\tag{3.4}
\]

The companion soft branch has the opposite sign and cannot produce the global improvement.

The basic seam coordinate is

\[
e=z+z^{-1}.
\]

If `n=2q+1`, then `phi=delta/n`, so

\[
2-e=O(\delta^2/n^2)=O(r^{-4}).
\]

In the transfer determinant this seam term is divided by the exponentially large hard-channel factor. Hence it is `o(r^{-4})` in the local root equation, uniformly in the odd multiplier. This is why the effective law depends only on the compressed phase `delta`.

---

## 4. Effective parabola

Let

\[
d_r(x)=2-2\cos(x/r).
\]

Equation (2.3) gives

\[
g-e_r^+=\mu+d_r(x)-d_r(x_r^0).
\]

Since

\[
x_r^0\to\frac\pi2
\]

and (3.4) holds,

\[
\begin{aligned}
r^4\bigl(d_r(x)-d_r(x_r^0)\bigr)
&\longrightarrow
2\left(\frac\pi2\right)
\left(-\frac{|\zeta|}{2\sqrt2}\right)\\
&=-\frac\pi{2\sqrt2}|\zeta|.
\end{aligned}
\]

Together with (3.1),

\[
\boxed{
r^4\bigl(g_r(\zeta/r^2)-e_r\bigr)
=\zeta^2-\frac\pi{2\sqrt2}|\zeta|+o(1),
}
\tag{4.1}
\]

locally uniformly for bounded `zeta`. This is the balanced effective phase-slip law.

The limiting function

\[
V(\zeta)=\zeta^2-\frac\pi{2\sqrt2}|\zeta|
\]

has exactly two minimizers

\[
\boxed{
\zeta=\pm\frac\pi{4\sqrt2}
}
\tag{4.2}
\]

and minimum

\[
\boxed{-\frac{\pi^2}{32}.}
\tag{4.3}
\]

---

## 5. Identification of the global optimizer

The localization (2.5) makes `r^2 delta_r` bounded after choosing the nearest endpoint. Take any convergent subsequence

\[
r^2\delta_r\to\zeta.
\]

Testing the explicit phase

\[
\delta=\frac{\pi}{4\sqrt2\,r^2}
\]

in the lower branch and using (4.1) gives

\[
\limsup r^4(\Gamma_r-e_r)
\le-\frac{\pi^2}{32}.
\]

At a true global maximizer, the companion branch is impossible because its effective correction is nonnegative. Hence the lower law (4.1) applies and yields

\[
\zeta^2-\frac\pi{2\sqrt2}|\zeta|
\le-\frac{\pi^2}{32}.
\]

But the left side has minimum exactly `-pi^2/32`, attained only at the two values in (4.2). Therefore every convergent subsequence satisfies

\[
|\zeta|=\frac\pi{4\sqrt2}.
\]

This proves (1.3), and substitution into (4.1) proves (1.4)--(1.5).

## 6. Interpretation

The balanced geometry equalizes the two macroscopic Dirichlet wells. At an endpoint the first soft pair is split only by exponentially small tunneling through the opposite hard arc. A compressed phase of size `r^-2` replaces that exponentially weak splitting by an algebraic `|delta|` cusp. The competition

\[
\text{quadratic phase cost }\delta^2
\quad\text{vs.}\quad
\text{linear cusp gain }|\delta|
\]

produces the universal effective parabola (4.1).

Thus balanced geometry has a two-level structure:

1. its leading period-normalized gap constant `16pi^2` is optimal;
2. the true global Bloch edge is shifted off the endpoints at the next algebraic scale, with universal constants `pi/(4sqrt2)` and `pi^2/32`.