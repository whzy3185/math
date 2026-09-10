# Variational optimality of balanced macroscopic defect geometry

Date: 2026-09-10

Status: **Proved**. This is a direct variational corollary of the exact macroscopic full-Bloch gap law.

Fix `0<epsilon<1/2`. For each large even half-period `L`, consider all admissible even defect separations `h` with

\[
\epsilon L\le h\le(1-\epsilon)L.
\]

For an arbitrary odd multiplier `2q+1`, let

\[
\Gamma_{L,h,q}=8-\max_{|z|=1}\rho(H_{L,h,q}(z))^2
\]

and define

\[
\Gamma_L^{\rm opt}(\epsilon,q)
=\max_{\substack{h\ {m even}\\
\epsilon L\le h\le(1-\epsilon)L}}
\Gamma_{L,h,q}.
\]

## Theorem A — optimal macroscopic gap

Uniformly for arbitrary variation of the odd multiplier,

\[
\boxed{
L^2\Gamma_L^{\rm opt}(\epsilon,q)\longrightarrow4\pi^2.
}
\]

## Theorem B — rigidity of near-optimal geometry

If `h_L` is any admissible sequence in the same macroscopic window and

\[
L^2\Gamma_{L,h_L,q_L}\longrightarrow4\pi^2,
\]

or more generally

\[
L^2\Gamma_{L,h_L,q_L}\ge4\pi^2-o(1),
\]

then necessarily

\[
\boxed{h_L/L\longrightarrow1/2.}
\]

## Proof

The macroscopic full-Bloch theorem gives, whenever `h_L/L -> alpha in [epsilon,1-epsilon]`,

\[
L^2\Gamma_{L,h_L,q_L}
\longrightarrow
C(\alpha):=\frac{\pi^2}{\max\{\alpha,1-\alpha\}^2}.
\]

The continuous function `C` has the unique maximum

\[
C(1/2)=4\pi^2.
\]

Choose admissible even `h_L` with `h_L/L -> 1/2`; this gives the lower bound for the optimized gap. For the upper bound, choose maximizing separations and use compactness of `[epsilon,1-epsilon]`; every convergent subsequence has limit `alpha` and hence limiting scaled gap at most `4pi^2`.

For near-optimal rigidity, every convergent subsequence of `h_L/L` must satisfy `C(alpha)=4pi^2`, hence `alpha=1/2`. Therefore the whole sequence converges to `1/2`.

## Quantitative stability

Because

\[
C(\alpha)=\frac{\pi^2}{(1/2+|\alpha-1/2|)^2},
\]

for each fixed `delta>0` there is a constant `c_delta>0` such that

\[
|\alpha-1/2|\ge\delta
\]

forces

\[
C(\alpha)\le4\pi^2-c_\delta.
\]

Thus balanced geometry is a rigid isolated variational optimum at the leading spectral scale.