# Two-integer localization of the fixed-period phase boundary

Date: 2026-09-10

Status: **Proved**. This sharpens the logarithmic bulk-width theorem from an `O(1)` statement to a two-adjacent-integer classification.

## Setup

Fix

\[
S=N+m\ge2,
\]

so the coefficient period is

\[
P=4S.
\]

Let

\[
N_*(S)=\min\{1\le N\le S-1:2(S-N)<T_N(3)\}
\]

be the smallest complementary bulk parameter for which the full Bloch spectrum is strictly sub-eight.

Put

\[
\Lambda:=3+2\sqrt2
\]

and

\[
A_S:=\log_{\Lambda}(4S),
\qquad
k_S:=\lfloor A_S\rfloor.
\]

## Theorem A — the cutoff lies on two adjacent integers

For every `S>=2`,

\[
\boxed{
N_*(S)\in\{k_S,k_S+1\}.
}
\tag{1.1}
\]

More precisely,

\[
\boxed{
N_*(S)=
\begin{cases}
k_S,&2(S-k_S)<T_{k_S}(3),\\
k_S+1,&2(S-k_S)>T_{k_S}(3).
\end{cases}}
\tag{1.2}
\]

There is no equality case because the left side is even and `T_{k_S}(3)` is odd.

### Proof: upper bound

Since

\[
k_S+1>A_S,
\]

we have

\[
\Lambda^{k_S+1}>4S.
\]

Using

\[
T_n(3)=\frac{\Lambda^n+\Lambda^{-n}}2,
\]

we obtain

\[
T_{k_S+1}(3)
>\frac{\Lambda^{k_S+1}}2
>2S
>2(S-k_S-1).
\]

Thus `N=k_S+1` is safe and

\[
N_*(S)\le k_S+1.
\tag{1.3}
\]

### Proof: lower bound

For `k_S=1`, the inequality `N_*(S)>=1=k_S` is automatic. Suppose `k_S>=2`.

Since

\[
\Lambda^{k_S}\le4S,
\]

we have

\[
T_{k_S-1}(3)
=\frac{\Lambda^{k_S-1}+\Lambda^{-(k_S-1)}}2
\le\frac{2S}{\Lambda}+\frac12.
\tag{1.4}
\]

On the other hand,

\[
2(S-k_S+1)
-\left(\frac{2S}{\Lambda}+\frac12\right)
=2S\left(1-\frac1\Lambda\right)-2k_S+\frac32.
\tag{1.5}
\]

Again using `4S>=Lambda^{k_S}`, the first term on the right is at least

\[
\frac{\Lambda^{k_S-1}(\Lambda-1)}2.
\]

For `k_S=2` this already exceeds `2k_S-3/2`; thereafter the exponential left side grows by the factor `Lambda>5`, whereas the required linear bound increases by only `2`. Hence (1.5) is strictly positive for every `k_S>=2`.

Therefore

\[
T_{k_S-1}(3)<2(S-k_S+1),
\]

so `N=k_S-1` is unsafe. By monotonicity of the exact criterion, every smaller `N` is also unsafe. Thus

\[
N_*(S)\ge k_S.
\tag{1.6}
\]

Combining (1.3) and (1.6) proves (1.1). Formula (1.2) follows by testing the only remaining candidate `N=k_S`.

---

## Corollary B — sub-two-unit accuracy for the maximum safe separation

The largest safe even defect separation is

\[
h_{\max}=2(S-N_*(S)).
\]

Since

\[
|N_*(S)-A_S|<1,
\]

we obtain the sharp finite estimate

\[
\boxed{
\left|
h_{\max}(P)
-\left(\frac P2-2\log_{\Lambda}P\right)
\right|<2,
\qquad P=4S.
}
\tag{2.1}
\]

Thus the logarithmic boundary location is accurate to less than one admissible separation step.

## Significance

The fixed-period phase boundary is not merely asymptotically logarithmic. Up to the unavoidable integer rounding, it is already determined by the elementary logarithm

\[
\log_{3+2\sqrt2}P.
\]

The exact Pell/Chebyshev test decides which of the two adjacent integers occurs.