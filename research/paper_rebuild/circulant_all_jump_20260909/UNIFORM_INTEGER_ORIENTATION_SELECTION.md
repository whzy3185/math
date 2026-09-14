# Uniform integer orientation selection in the macroscopic two-defect family

Date: 2026-09-14

Status: **Proved; corrected beyond-all-orders scale**.

Write

\[
L=2(N+m),\qquad N,m\to\infty,
\qquad 0<c_0\le m/N\le c_1<\infty,
\]

and let `n=2q+1` be the compatible odd multiplier.

## Theorem — integer orientation selection

For all sufficiently large comparable integer pairs:

\[
\boxed{m\le N}
\]

selects the periodic cusp branch globally, whereas

\[
\boxed{m>N}
\]

selects the compressed-antiperiodic well `d≈-2`.

Thus the algebraic orientation transition occurs exactly at

\[
\boxed{m=N.}
\]

### Periodic/balanced side

If `m<=N`,

\[
\Gamma_{N,m,q}\sim A(N)-C(N),
\]

where `A` is the universal endpoint Robin series and `C` is the periodic cusp-gain series.  At balance the cusp resolves the endpoint degeneracy.

### Compressed-antiperiodic side

If `m>N`, put

\[
U_N=U_{N-1}(3).
\]

The best exact compressed-antiperiodic roots are

\[
z_0=e^{\pm i\pi/n}.
\]

A maximizing phase can be written

\[
z_*=z_0e^{i\delta_*/n}
\]

with

\[
\boxed{
\delta_*
=-
\frac{\pi^2\sin(\pi/n)}
{64\sqrt2\,n\,U_Nm^3}
\left(1+O(m^{-1})\right)
+O(U_N^{-2}m^{-6}).
}
\]

Moreover

\[
\boxed{
 e^-_{N,m}-\Gamma_{N,m,q}
=
\frac{(2+2\cos(\pi/n))\pi^2}
{64\sqrt2\,U_Nm^3}
\left(1+O(m^{-1})\right)
+O(U_N^{-2}m^{-6}).
}
\]

Hence, to every algebraic order,

\[
\Gamma_{N,m,q}\sim A(m),
\]

and the first odd-multiplier dependence appears only at the hard-channel tunneling scale

\[
U_N^{-1}m^{-3}=\Theta((3+2\sqrt2)^{-N}m^{-3}).
\]

## Proof structure

The endpoint Robin function is strictly decreasing in the soft length:

\[
A'(\ell)=-\frac{\pi^2}{2\ell^3}+O(\ell^{-4}).
\]

Because `m-N` is integral, a one-site imbalance creates an `N^-3` endpoint advantage, while the periodic cusp is only `N^-4` and the physical-seam correction is exponentially smaller.  This selects the side.  Full-Bloch hard/soft localization excludes every other phase region.

The precise seam correction is proved in `ANTIPERIODIC_SEAM_TUNNELING_ASYMPTOTIC.md`.