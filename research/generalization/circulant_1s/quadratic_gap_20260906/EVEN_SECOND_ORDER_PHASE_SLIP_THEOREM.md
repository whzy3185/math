# Even jumps: second-order phase-slip asymptotics

Date: 2026-09-06.

This note refines `EVEN_GLOBAL_PI2_THEOREM.md`.  The leading theorem proved
there is

\[
4r^2 g_{2r}\to\pi^2,
\]

where `g_(2r)` is the global Bloch gap of the period-`8r` antipodal family.
The exact `s=10` certificate in `PHASE_SLIP_COUNTEREXAMPLE.md` shows that the
maximizing phase is not always zero.  Here we identify the first nontrivial
phase boundary layer and the spectral gain it produces.

Throughout, write

\[
 e_r:=8-\rho(H_{2r}(1))^2
\]

for the phase-zero endpoint gap.  If `phi_r` is a global minimizing
square-root Bloch phase, choose it in `[0,pi]` and put

\[
 h_r=2\cos\phi_r,
 \qquad
 \mu_r=2-h_r=2-2\cos\phi_r.
\]

## Theorem S — second-order phase slip

As `r -> infinity`,

\[
 \boxed{r^2\phi_r\longrightarrow\frac\pi{4\sqrt2}.}
 \tag{S1}
\]

Moreover

\[
 \boxed{r^4(e_r-g_{2r})\longrightarrow\frac{\pi^2}{32}.}
 \tag{S2}
\]

Equivalently,

\[
 g_{2r}
 =e_r-\frac{\pi^2}{32r^4}+o(r^{-4}).
 \tag{S3}
\]

Thus the phase slip is genuine but affects only the second nontrivial scale;
it leaves the sharp leading constant `pi^2` unchanged.

A more informative local statement is the boundary-layer law below.

## Boundary-layer law

Set

\[
 a:=\frac\pi{2\sqrt2}.
\]

For a phase of the form

\[
 \phi=\frac z{r^2},\qquad z=O(1),
\]

the lower of the two soft branches adjacent to the endpoint satisfies

\[
 \boxed{
 r^4\bigl(g_{2r}(z/r^2)-e_r\bigr)
 =z^2-a z+o(1),}
 \tag{B1}
\]

locally uniformly for bounded nonnegative `z` on that branch.  The companion
soft branch has `z^2+a z+o(1)`.  The parabola in (B1) has the unique minimum

\[
 z_*=\frac a2=\frac\pi{4\sqrt2},
\]

with value

\[
 -\frac{a^2}{4}=-\frac{\pi^2}{32}.
\]

Equations (S1)--(S2) are therefore exactly the minimizer and minimum of the
boundary-layer effective law.

## 1. Exact soft/hard root equation

Use the notation of `EVEN_GLOBAL_PI2_THEOREM.md`.  At a squared edge
`y=8-g`, put

\[
 d_-=y-4-h,
 \qquad
 d_+=y-4+h,
\]

\[
 A_j=D_j(d_-),\qquad B_j=D_j(d_+),
\]

and

\[
 \beta=\frac{B_{r-1}}{B_r},\qquad
 \gamma=\frac{B_{r-2}}{B_r}.
\]

The exact determinant identity gives

\[
\begin{split}
 A_r-6\beta A_{r-1}+\gamma A_{r-2}
 ={}&\pm\frac2{B_r}
 \Bigl((4-\mu)A_{r-1}^2+
       \mu B_{r-1}^2\\
 &\qquad +(4\mu-\mu^2)A_{r-1}B_{r-1}
       +h^2/4\Bigr)^{1/2}.
\end{split}
\tag{1}
\]

The previous global theorem proves

\[
 g=O(r^{-2}),\qquad \mu=o(r^{-2})
\tag{2}
\]

for a globally minimizing phase.  Its localization lemma also gives a
uniformly nondegenerate hard channel.

## 2. Bootstrap from `o(r^-2)` to `O(r^-4)` phase mass

Let `theta_r` denote the oscillatory soft angle of the global edge,

\[
 g_{2r}-\mu_r=2-2\cos\theta_r,
\]

and let `theta_r^0` be the endpoint soft angle,

\[
 e_r=2-2\cos\theta_r^0.
\]

Put

\[
 x_r=r\theta_r,
 \qquad
 x_r^0=r\theta_r^0.
\]

The global and endpoint sharp theorems give

\[
 x_r,x_r^0\to\frac\pi2.
\tag{3}
\]

Multiply (1) by `sin(theta)/theta`.  In a fixed neighborhood of `pi/2`
in the `x=r theta` coordinate, the derivative of the normalized left side
tends to

\[
 -(1-\lambda^{-2}),
 \qquad
 \lambda=3+2\sqrt2,
\tag{4}
\]

and is therefore bounded away from zero.

The hard-channel ratios are smooth in `(g,mu)` near `(0,0)` and satisfy

\[
 \beta=\lambda^{-1}+O(r^{-2}),
 \qquad
 \gamma=\lambda^{-2}+O(r^{-2}).
\tag{5}
\]

Subtract the endpoint equation from the global equation.  The normalized
phase term on the right of (1) is `O(sqrt(mu_r))`; the change of the hard
ratios contributes `O(|g_(2r)-e_r|+mu_r)`.  Using (3)--(5) and the local
inverse bound from (4) gives

\[
 |x_r-x_r^0|
 \le C\bigl(\sqrt{\mu_r}+|g_{2r}-e_r|+\mu_r+e^{-cr}\bigr).
\tag{6}
\]

On the other hand, the elementary derivative bound for
`2-2 cos(x/r)` gives

\[
 |g_{2r}-e_r|
 \le \mu_r+\frac C{r^2}|x_r-x_r^0|.
\tag{7}
\]

Since the global phase can only improve the endpoint, `g_(2r)<=e_r`.
Combining (6)--(7), absorbing the `r^-2 |g-e|` term, and writing
`u_r=sqrt(mu_r)` gives

\[
 u_r^2\le \frac C{r^2}u_r+\frac C{r^4}.
\]

Hence

\[
 \boxed{\sqrt{\mu_r}=O(r^{-2}),
 \qquad \mu_r=O(r^{-4}).}
\tag{8}
\]

This is the missing boundary-layer localization.  Since
`mu_r=2-2 cos(phi_r)=phi_r^2+O(phi_r^4)`, it is equivalent to

\[
 \phi_r=O(r^{-2}).
\tag{9}
\]

Equation (6) then also improves to

\[
 |x_r-x_r^0|=O(r^{-2}),
 \qquad |g_{2r}-e_r|=O(r^{-4}).
\tag{10}
\]

## 3. The cusp coefficient

Now suppose along a subsequence

\[
 r^2\phi_r\to z\ge0.
\tag{11}
\]

Then

\[
 r^2\sqrt{\mu_r}\to z,
 \qquad
 r^4\mu_r\to z^2.
\tag{12}
\]

Because of (10), the hard-channel ratios at the global root differ from
their endpoint values by only `O(r^-4)`.  In (1), all terms containing
`A_(r-1)/B_r` are exponentially small.  Therefore the normalized square-root
term has the sharp expansion

\[
 \frac2{B_r}\sqrt{\cdots}
 =2\lambda^{-1}\sqrt\mu+o(r^{-2}).
\tag{13}
\]

Subtract the endpoint root equation and linearize in the `x` coordinate.
For the lower soft branch this yields

\[
 -(1-\lambda^{-2})(x_r-x_r^0)
 =2\lambda^{-1}\sqrt{\mu_r}+o(r^{-2}).
\tag{14}
\]

The exact algebraic simplification

\[
 \frac{2\lambda^{-1}}{1-\lambda^{-2}}
 =\frac1{2\sqrt2}
\tag{15}
\]

therefore gives

\[
 \boxed{
 r^2(x_r-x_r^0)
 \longrightarrow-\frac{z}{2\sqrt2}.}
\tag{16}
\]

For the companion branch the sign is reversed.  This is the origin of the
absolute-value cusp in the phase variable.

## 4. Effective parabola

Write

\[
 d_r(x)=2-2\cos(x/r).
\]

Then

\[
 g_{2r}-e_r
 =\mu_r+d_r(x_r)-d_r(x_r^0).
\tag{17}
\]

Since `x_r,x_r^0->pi/2`, Taylor's theorem and (16) give

\[
\begin{split}
 r^4\bigl(d_r(x_r)-d_r(x_r^0)\bigr)
 &\longrightarrow
 2\left(\frac\pi2\right)
 \left(-\frac z{2\sqrt2}\right)\\
 &=-\frac\pi{2\sqrt2}z.
\end{split}
\tag{18}
\]

Combining (12), (17) and (18) proves the lower-branch law

\[
 r^4(g_{2r}-e_r)
 \longrightarrow
 z^2-\frac\pi{2\sqrt2}z.
\tag{19}
\]

The same calculation with the other sign in (14) gives the companion
parabola with a plus sign.

## 5. Identifying the global minimizer

The localization (9) makes the sequence `r^2 phi_r` bounded.  Take any
convergent subsequence with limit `z`.

For a fixed test value

\[
 z_0=\frac\pi{4\sqrt2},
\]

the local implicit equation corresponding to the lower sign has, for all
large `r`, a root at phase `phi=z_0/r^2` in the first soft pair.  Applying
(19) to this test root gives

\[
 \limsup r^4(g_{2r}-e_r)
 \le -\frac{\pi^2}{32}.
\tag{20}
\]

At the actual global root, the upper soft branch is impossible in (20),
since its scaled correction is nonnegative.  Hence (19) applies with the
minus sign and gives along the subsequence

\[
 z^2-\frac\pi{2\sqrt2}z
 \le -\frac{\pi^2}{32}.
\tag{21}
\]

But the left side is the quadratic

\[
 \left(z-\frac\pi{4\sqrt2}\right)^2
 -\frac{\pi^2}{32},
\]

whose minimum is exactly `-pi^2/32`.  Thus equality must hold in (21), and
necessarily

\[
 z=\frac\pi{4\sqrt2}.
\]

Every convergent subsequence has the same limit, proving (S1).  Substitution
into (19) proves (S2)--(S3).

## 6. Spectral interpretation

At phase zero, the two first soft eigenvalues are split only by an
exponentially small hard-channel tunneling term.  Turning on a phase
`phi=Theta(r^-2)` replaces that exponentially tiny splitting by the algebraic
term

\[
 2\lambda^{-1}|\phi|.
\]

After division by the Robin slope `1-lambda^-2`, this shifts the soft
quantization coordinate by

\[
 -\frac{|\phi|}{2\sqrt2}.
\]

The diagonal phase cost is `mu~phi^2`.  The competition between this
quadratic cost and the linear cusp is exactly the effective parabola (B1).
The optimizer is therefore an avoided-crossing/degenerate-perturbation
phenomenon, not an ordinary analytic perturbation of a simple endpoint
eigenvalue.

## 7. Proof-audit boundary

The argument uses only exact identities already established in the preceding
notes plus a local implicit-function estimate around the first soft Robin
root.  A submission version should state that local estimate as a separate
lemma with explicit constants and should include a first-soft-pair isolation
lemma.  These are quantitative packaging steps; they do not change the
asymptotic mechanism or constants above.

The theorem concerns the explicit even-jump antipodal family.  It does not
assert global optimality over all signings of `C_N(1,s)`.
