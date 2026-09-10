# Universal optimal period-normalized gap constant in the macroscopic two-defect family

Date: 2026-09-10

Status: **Proved**. This is a normalized reformulation and optimization consequence of the full-Bloch macroscopic gap law.

## 1. Setup

Let

\[
L=2(N+m),\qquad h=2m,
\]

and let the primitive coefficient period be

\[
p=2L=4(N+m).
\]

Assume

\[
N,m\to\infty,
\qquad
\frac{m}{N+m}\to\alpha\in(0,1).
\]

Let

\[
\Gamma_{N,m,q}=8-\max_{|z|=1}\rho(H_{N,m,q}(z))^2
\]

for an arbitrary varying odd multiplier.

The full-Bloch macroscopic theorem gives

\[
L^2\Gamma_{N,m,q}
\to
\frac{\pi^2}{\max\{\alpha,1-\alpha\}^2}.
\]

Since `p=2L`, we obtain the exact normalized law

\[
\boxed{
p^2\Gamma_{N,m,q}
\longrightarrow
\frac{4\pi^2}{\max\{\alpha,1-\alpha\}^2}.
}
\tag{1.1}
\]

## Theorem A — universal period-normalized optimum

Among all macroscopic separation ratios,

\[
\boxed{
\limsup p^2\Gamma_{N,m,q}\le16\pi^2.
}
\tag{2.1}
\]

The constant `16 pi^2` is sharp, and equality in the limiting law occurs if and only if

\[
\boxed{
\alpha=\frac12.
}
\tag{2.2}
\]

For the exactly balanced family `N=m`,

\[
\boxed{
p^2\Gamma_{N,N,q}\to16\pi^2.}
\tag{2.3}
\]

### Proof

Equation (1.1) reduces the optimization to

\[
\max_{0<\alpha<1}
\frac{4\pi^2}{\max\{\alpha,1-\alpha\}^2}.
\]

The denominator is minimized uniquely at `alpha=1/2`, where it equals `1/4`. Hence the maximum is `16 pi^2`, proving (2.1)--(2.3).

---

## Corollary B — normalized rigidity

If a sequence of macroscopic two-defect phases satisfies

\[
p^2\Gamma_{N,m,q}\to16\pi^2,
\]

then necessarily

\[
\boxed{
\frac hL=\frac m{N+m}\to\frac12.
}
\tag{3.1}
\]

More quantitatively, if

\[
\left|\alpha-\frac12\right|\ge\epsilon>0,
\]

then

\[
\boxed{
\limsup p^2\Gamma_{N,m,q}
\le
\frac{16\pi^2}{(1+2\epsilon)^2}.
}
\tag{3.2}
\]

---

## Corollary C — optimized compatible-period hierarchy for a prescribed jump

Let

\[
s=2^k n,
\qquad k\ge2,
\qquad n\text{ odd}.
\]

For every odd divisor `d|n`, the compatible half-period

\[
L_d=2^k d
\]

has primitive period

\[
p_d=2^{k+1}d.
\]

Choose the balanced two-defect geometry inside that cell. Along any sequence for which `p_d->infinity`,

\[
\boxed{
p_d^2\Gamma_d\to16\pi^2,}
\tag{4.1}
\]

independently of the residual odd multiplier `n/d`.

Therefore, for two compatible balanced periods `p_1<p_2`,

\[
\frac{\Gamma(p_1)}{\Gamma(p_2)}
\sim
\left(\frac{p_2}{p_1}\right)^2.
\tag{4.2}
\]

Thus enlarging the compatible period does not improve the leading normalized efficiency: the same universal constant `16 pi^2` is retained, while the absolute spectral gap decays quadratically with the period.

In this sense the shortest compatible balanced phase is asymptotically Pareto-optimal: it simultaneously minimizes the period and maximizes the leading absolute gap among the balanced compatible hierarchy.

## 5. Significance

The arithmetic period-compression theorem and the geometric optimization theorem now meet in one sharp law:

\[
\boxed{
\text{best macroscopic two-defect efficiency}
=16\pi^2/p^2.
}
\]

The constant is universal; arithmetic chooses which periods are compatible, while balanced defect geometry saturates the optimal normalized coefficient.