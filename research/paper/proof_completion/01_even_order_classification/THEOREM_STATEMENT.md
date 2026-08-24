# Complete Truth Classification at Even Order

## Setting

Let $X_n=C_n(1,2)$, where $n\ge 8$ is even.  For a signing
$\sigma:E(X_n)\to\{\pm1\}$, let $A_\sigma$ be its signed adjacency matrix and
put

$$
m_n=\min_\sigma\rho(A_\sigma),\qquad
\rho_-(n)^2=4+2\cos\frac{2\pi}{n}+2\cos\frac{4\pi}{n}.
$$

The strict inequality $m_n<\rho_-(n)$ says that the proposed lower bound fails
at order $n$.

## Main theorem

**Theorem (complete truth classification).**  For every even integer $n\ge8$,

$$
m_n<\rho_-(n)
\quad\Longleftrightarrow\quad
n=32,\quad n=40,\quad\text{or}\quad n\ge48.
$$

Equivalently, the proposed lower bound is valid exactly for

$$
\{8,10,12,14,16,18,20,22,24,26,28,30,34,36,38,42,44,46\}.
$$

This is a classification of the truth value of one inequality.  It does not
classify all minimising signings, determine $m_n$ at every failing order, or
assert that every signing at a failing order is a counterexample.

## Exhaustive partition

The admissible set is the disjoint union

$$
\begin{aligned}
\mathcal P_1&=\{n:8\le n\le30,\ n\text{ even}\},\\
\mathcal P_2&=\{32\},\\
\mathcal P_3&=\{34,36,38,42,44,46\},\\
\mathcal P_4&=\{40\},\\
\mathcal P_5&=\{n:48\le n<240,\ n\text{ even}\},\\
\mathcal P_6&=\{n:n\ge240,\ n\text{ even}\}.
\end{aligned}
$$

The inequality holds on $\mathcal P_1\cup\mathcal P_3$ and fails on the other
four pieces.  The fifth piece ends at 238; the odd order 239 is outside the
domain.

Evidence status: COMPUTER_ASSISTED_PROVED.  Every accepted matrix inequality
and algebraic endpoint comparison is exact.
