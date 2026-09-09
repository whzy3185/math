# Asymptotic spectral ordering by two-defect separation

Date: 2026-09-09

Status: **Proved**. This note belongs only to Paper I.

For fixed separation parameter `h>=1`, let

\[
\Gamma^{(h)}_{L,q}
=8-R^{(h)}_{L,q}
\]

be the global continuous squared Bloch gap of the period-`2L` two-defect phase whose positive local flux defects are separated by `2h` sites.

The global defect-separation theorem gives, uniformly in the odd multiplier,

\[
L^2\Gamma^{(h)}_{L,q}
\longrightarrow
\kappa_h,
\qquad
\kappa_h:=4\arccos^2\!\frac1{T_h(3)}.
\tag{1}
\]

The constants satisfy

\[
\kappa_1<\kappa_2<\kappa_3<\cdots<\pi^2.
\]

## Theorem A — eventual strict ordering

Fix two integers

\[
1\le h_1<h_2.
\]

Then there exists an even threshold `L_0(h_1,h_2)` such that for every even

\[
L\ge L_0(h_1,h_2)
\]

and every `q>=0`,

\[
\boxed{
\Gamma^{(h_2)}_{L,q}
>\Gamma^{(h_1)}_{L,q}.
}
\tag{2}
\]

Equivalently, the wider fixed defect separation has strictly smaller global squared Bloch edge:

\[
\boxed{
R^{(h_2)}_{L,q}
<R^{(h_1)}_{L,q}.
}
\tag{3}
\]

Thus defect separation is a genuine asymptotic variational parameter, not merely a source of different exact formulas.

### Proof

Put

\[
\Delta=\kappa_{h_2}-\kappa_{h_1}>0.
\]

The global sharp-gap convergence for each fixed separation is uniform in `q`. Hence there exists `L_0` such that, for all even `L>=L_0` and all `q`,

\[
\left|L^2\Gamma^{(h_i)}_{L,q}-\kappa_{h_i}\right|
<\frac\Delta3,
\qquad i=1,2.
\]

Therefore

\[
\begin{aligned}
L^2\left(
\Gamma^{(h_2)}_{L,q}-\Gamma^{(h_1)}_{L,q}
\right)
&>\kappa_{h_2}-\frac\Delta3
-\kappa_{h_1}-\frac\Delta3\\
&=\frac\Delta3>0.
\end{aligned}
\]

This proves (2)--(3).

## Corollary B — finite candidate classes

Fix

\[
1\le h_1<h_2<\cdots<h_m.
\]

Then, for all sufficiently large even `L`, uniformly in every odd multiplier,

\[
\boxed{
R^{(h_m)}_{L,q}
<\cdots<
R^{(h_2)}_{L,q}
<R^{(h_1)}_{L,q}.
}
\tag{4}
\]

Hence among any fixed finite list of even two-defect separations, the widest one is eventually the unique best phase in spectral-radius terms.

## Corollary C — approach to the Dirichlet constant

For every `epsilon>0`, there exists a fixed defect parameter `h_epsilon` such that

\[
\kappa_{h_\epsilon}>\pi^2-\epsilon.
\]

For that fixed geometry and all sufficiently large `L`, uniformly in `q`,

\[
\boxed{
L^2\Gamma^{(h_\epsilon)}_{L,q}
>\pi^2-2\epsilon.
}
\tag{5}
\]

Thus compressed two-defect phases can realize global quadratic gap constants arbitrarily close to the Dirichlet value `pi^2` while retaining the same period scale `2L`.

## Interpretation

The separation-two phase is distinguished by minimal geometric width and by the nontrivial Robin value `cos(alpha)=1/3`, but it is not asymptotically gap-optimal within the broader fixed-width two-defect family. Increasing the defect width strengthens the boundary condition continuously toward Dirichlet and strictly improves the global gap constant.