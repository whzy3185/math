# Antiperiodic one-fiber detection principle

Date: 2026-09-10

Status: **Proved**. This is an immediate but conceptually important corollary of the exact general-separation phase diagram.

## Setup

For the even-separation two-defect family write

\[
L=2(N+m),\qquad h=2m,
\qquad N,m\ge1,
\]

and let

\[
s=L(2q+1),\qquad q\ge0.
\]

Let `H_{N,m,q}(z)` denote the Bloch fiber and

\[
R_{N,m,q}=\max_{|z|=1}\rho(H_{N,m,q}(z))^2.
\]

## Theorem — one fiber detects the entire threshold phase diagram

For every `N,m>=1` and every odd multiplier,

\[
\boxed{
R_{N,m,q}<8
\quad\Longleftrightarrow\quad
\rho(H_{N,m,q}(-1))^2<8.
}
\tag{1}
\]

Moreover,

\[
\boxed{
R_{N,m,q}<8
\quad\Longleftrightarrow\quad
2m<T_N(3).
}
\tag{2}
\]

Thus the full continuous Bloch-circle threshold question is decided by the single antiperiodic fiber.

### Proof

The exact general-separation theorem proves

\[
R_{N,m,q}<8
\iff2m<T_N(3).
\]

On the other hand, the exact antiperiodic determinant is

\[
P_{N,m,-1}(8)
=4\bigl(T_N(3)^2-4m^2\bigr).
\]

There is no equality case because `T_N(3)` is odd and `2m` is even. The endpoint fiber at `z=-1` is therefore strictly sub-eight exactly when `2m<T_N(3)`, and strictly super-eight exactly when `2m>T_N(3)`. Combining the two equivalences proves (1)--(2).

## Interpretation

This is stronger than saying that `z=-1` supplies a convenient obstruction. It says that for this entire two-parameter family there are no hidden interior-phase threshold failures:

> if the antiperiodic fiber is below `8`, every Bloch fiber is below `8`.

The proof of the full theorem is still genuinely global: it uses the compact threshold formula, exponential phase localization, and the finite arithmetic margin. The corollary summarizes that global work as a one-fiber diagnostic principle.