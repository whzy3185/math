# Even jumps: next correction beyond the second-order phase-slip law

Date: 2026-09-06.

This note refines `EVEN_SECOND_ORDER_PHASE_SLIP_THEOREM.md` by retaining the
first finite-`r` correction in the Robin geometry.  It gives the next term in
the optimizing phase and in the spectral gain over phase zero.

Throughout `s=2r`.  Let `phi_r` be a globally optimizing square-root Bloch
phase, let

\[
 e_r=8-\rho(H_{2r}(1))^2,
 \qquad
 g_{2r}=8-R_{2r},
\]

and choose `phi_r>=0`.

## Theorem T — first correction to the boundary-layer minimizer

As `r -> infinity`,

\[
 \boxed{
 \phi_r
 =\frac\pi{4\sqrt2\,r^2}
 -\frac{3\pi}{16r^3}
 +o(r^{-3}).}
 \tag{T1}
\]

Equivalently,

\[
 \boxed{
 r\left(r^2\phi_r-\frac\pi{4\sqrt2}\right)
 \longrightarrow-\frac{3\pi}{16}.}
 \tag{T2}
\]

The corresponding phase-slip gain satisfies

\[
 \boxed{
 e_r-g_{2r}
 =\frac{\pi^2}{32r^4}
 -\frac{3\pi^2}{32\sqrt2\,r^5}
 +o(r^{-5}).}
 \tag{T3}
\]

Equivalently,

\[
 \boxed{
 r\left(r^4(e_r-g_{2r})-\frac{\pi^2}{32}\right)
 \longrightarrow-\frac{3\pi^2}{32\sqrt2}.}
 \tag{T4}
\]

## 1. Endpoint soft-root correction

Put

\[
 q=\lambda^{-1}=3-2\sqrt2.
\]

At phase zero, after replacing the hard ratios by `q,q^2`, whose error is
`O(r^-2)`, the first soft Robin equation is

\[
 \cos\left(x+\frac{x}{2r}\right)
 =q^2\cos\left(x-\frac{x}{2r}\right),
\tag{1}
\]

where `x=r theta`.  Rewriting (1) gives

\[
 \cot x
 =\frac{1+q^2}{1-q^2}
   \tan\frac{x}{2r}+O(r^{-2}).
\tag{2}
\]

The exact algebraic identity

\[
 \frac{1+q^2}{1-q^2}=\frac{3\sqrt2}{4}
\tag{3}
\]

and `x->pi/2` therefore imply

\[
 \boxed{
 x_r^0
 =\frac\pi2-rac{3\sqrt2\,\pi}{16r}
 +O(r^{-2}).}
\tag{4}
\]

The `O(r^-2)` hard-ratio correction cannot affect the displayed `1/r`
coefficient.

## 2. Finite-`r` cusp slope

For the endpoint-subtracted lower soft branch, let `c_r` be the coefficient
relating the Robin coordinate displacement to `sqrt(mu)`:

\[
 x-x_r^0=-c_r\sqrt\mu+o(\sqrt\mu).
\tag{5}
\]

Using the finite-`r` derivative of (1),

\[
\begin{split}
 D_r={}&
 \left(1+\frac1{2r}\right)
 \sin\left(x_r^0+\frac{x_r^0}{2r}\right)\\
 &-q^2\left(1-\frac1{2r}\right)
 \sin\left(x_r^0-\frac{x_r^0}{2r}\right),
\end{split}
\tag{6}
\]

while the phase square-root term contributes

\[
 2q\sqrt\mu\cos\frac{x_r^0}{2r}.
\]

Hence

\[
 c_r=
 \frac{2q\cos(x_r^0/(2r))}{D_r}+O(r^{-2}).
\tag{7}
\]

Substituting (4) and expanding (6) gives

\[
 \boxed{
 c_r=\frac1{2\sqrt2}-\frac{3}{16r}+O(r^{-2}).}
\tag{8}
\]

The leading coefficient is the one already used in the second-order theorem.

## 3. Refined effective linear coefficient

Take a boundary-layer phase

\[
 \phi=\frac z{r^2},
 \qquad z=O(1).
\]

Then

\[
 \mu=2-2\cos\phi=\frac{z^2}{r^4}+O(r^{-8}).
\]

The soft-gap change is controlled by

\[
 2r\sin\left(\frac{x_r^0}{r}\right)c_r.
\]

Define

\[
 a_r:=2r\sin\left(\frac{x_r^0}{r}\right)c_r.
\tag{9}
\]

Because

\[
 r\sin(x_r^0/r)=x_r^0+O(r^{-2}),
\]

(4) and (8) give

\[
\begin{split}
 a_r
 &=\frac\pi{2\sqrt2}
 +\frac1r\left[
 2\left(-\frac{3\sqrt2\pi}{16}\right)
   \frac1{2\sqrt2}
 +\pi\left(-\frac3{16}\right)
 \right]
 +O(r^{-2})\\
 &=\boxed{
 \frac\pi{2\sqrt2}-\frac{3\pi}{8r}+O(r^{-2}).}
\end{split}
\tag{10}
\]

Thus the refined boundary-layer law is

\[
 \boxed{
 r^4\bigl(g_{2r}(z/r^2)-e_r\bigr)
 =z^2-a_rz+o(r^{-1})}
\tag{11}
\]

uniformly for `z` in fixed compact intervals on the lower first-soft branch.
The companion branch has `+a_r z`.

## 4. Minimization

The lower effective quadratic has unique minimizer

\[
 z_r^*=\frac{a_r}{2}
 =\frac\pi{4\sqrt2}-\frac{3\pi}{16r}+o(r^{-1}).
\tag{12}
\]

The global phase localization from
`SECOND_ORDER_LOCAL_IMPLICIT_LEMMA.md` keeps the true optimizer in this
boundary layer, while global optimality selects the lower branch.  Therefore

\[
 r^2\phi_r=z_r^*+o(r^{-1}),
\]

which proves (T1)--(T2).

The minimum effective value is

\[
 -\frac{a_r^2}{4}.
\]

Using (10),

\[
 \frac{a_r^2}{4}
 =\frac{\pi^2}{32}
 -\frac{3\pi^2}{32\sqrt2\,r}
 +o(r^{-1}),
\tag{13}
\]

which gives (T3)--(T4).

## 5. Numerical audit

The gain correction is especially stable numerically.  For example, the
quantity

\[
 r\left(r^4(e_r-g_{2r})-\frac{\pi^2}{32}\right)
\]

approaches

\[
 -\frac{3\pi^2}{32\sqrt2}\approx-0.6543.
\]

The direct phase optimizer is less well conditioned in double precision
because `phi_r=Theta(r^-2)` and the spectral improvement is only
`Theta(r^-4)`.  A local quadratic fit in the scaled variable `z=r^2 phi`
converges consistently to the expansion (12).

The script `verify_second_order_phase_slip.py` can be extended to report
these corrected targets; it is an audit only and is not used in the proof.

## 6. Scope

This is a higher-order refinement for the explicit even antipodal family.
It does not address global optimality over all signings.  Terms beyond those
shown here require the `O(r^-2)` expansion of the hard-channel ratios and the
next endpoint Robin correction; those are natural but algebraically longer
next targets.
