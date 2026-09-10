# Logarithmic complementary-bulk width at fixed periodic cell size

Date: 2026-09-10

Status: **Proved**. This is a corollary of the exact general-separation phase diagram.

The exact criterion

\[
2m<T_N(3)
\]

has a striking geometric consequence when the total periodic cell is fixed and the defect separation is varied.

## 1. Fixed-cell parametrization

Write

\[
S=N+m,
\qquad N,m\ge1.
\]

Then

\[
L=2S,
\qquad h=2m,
\]

and the coefficient word has primitive ambient period

\[
P=2L=4S.
\]

For fixed `S`, increasing the defect separation `h` is equivalent to increasing `m=S-N`, hence decreasing the complementary alternating-bulk parameter `N`.

Define the smallest safe bulk parameter

\[
\boxed{
N_*(S):=
\min\{1\le N\le S-1:\ 2(S-N)<T_N(3)\}.
}
\tag{1.1}
\]

The exact phase-diagram theorem immediately gives:

### Theorem A — exact fixed-period cutoff

For a period `P=4S` two-defect word, the full Bloch spectrum is strictly sub-eight exactly when

\[
\boxed{N\ge N_*(S).}
\tag{1.2}
\]

Equivalently, the largest safe even defect separation is

\[
\boxed{
h_{\max}(P)=2\bigl(S-N_*(S)\bigr).}
\tag{1.3}
\]

The cutoff is unique because `2(S-N)` decreases strictly with `N`, while `T_N(3)` increases strictly.

---

## 2. Logarithmic asymptotic location of the cutoff

Put

\[
\Lambda:=3+2\sqrt2.
\]

The closed form

\[
T_N(3)=\frac{\Lambda^N+\Lambda^{-N}}2
\tag{2.1}
\]

shows that the transition occurs when

\[
\Lambda^N\asymp4S.
\]

More precisely,

\[
\boxed{
N_*(S)=\log_{\Lambda}(4S)+O(1)
\qquad(S\to\infty).
}
\tag{2.2}
\]

### Proof

Let

\[
A_S:=\log_{\Lambda}(4S).
\]

If

\[
N\ge\lceil A_S\rceil,
\]

then

\[
\Lambda^N\ge4S,
\]

and hence by (2.1)

\[
T_N(3)\ge\frac{\Lambda^N}{2}\ge2S>2(S-N).
\]

Therefore

\[
N_*(S)\le A_S+1.
\tag{2.3}
\]

Conversely, if

\[
N\le A_S-1,
\]

then

\[
\Lambda^N\le\frac{4S}{\Lambda}.
\]

Using `Lambda^{-N}<=1`,

\[
T_N(3)
\le\frac{2S}{\Lambda}+\frac12.
\tag{2.4}
\]

But `A_S=O(log S)`, so for all sufficiently large `S`,

\[
2(S-N)
\ge2S-2A_S
>\frac{2S}{\Lambda}+\frac12.
\]

Thus such an `N` is not safe. Consequently

\[
N_*(S)>A_S-1
\]

for all sufficiently large `S`. Together with (2.3) this proves (2.2).

---

## 3. Maximum safe defect separation

Since

\[
P=4S
\]

and

\[
h_{\max}=2(S-N_*),
\]

formula (2.2) gives

\[
\boxed{
 h_{\max}(P)
 =\frac P2
 -2\log_{\Lambda}P
 +O(1),
 \qquad
 \Lambda=3+2\sqrt2.
}
\tag{3.1}
\]

Equivalently, the complementary alternating arc needed to keep the whole Bloch spectrum below `8` has length only

\[
\boxed{
L-h_{\max}
=2\log_{\Lambda}P+O(1).
}
\tag{3.2}
\]

Thus an almost-half-period defect arc remains spectrally admissible provided one leaves a logarithmically growing alternating bulk buffer.

## 4. Interpretation

The general even-separation phase diagram has two very different geometric scales:

- the periodic cell size is linear in `S`;
- the minimum stabilizing alternating bulk width is only logarithmic in that size.

This is the finite-cell manifestation of the exponential Chebyshev threshold

\[
T_N(3)\asymp\frac12(3+2\sqrt2)^N.
\]

It provides a geometric interpretation of the exact phase boundary that is not visible from the original fixed-separation asymptotics.