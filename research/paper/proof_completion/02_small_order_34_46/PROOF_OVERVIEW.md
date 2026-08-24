# Proof Overview

## Normal form

Switch along a spanning path so that all nearest-neighbour signs are positive
except possibly the cyclic seam.  Its sign is
$\alpha\in\{\pm1\}$.  If $\tau_i$ denotes the triangle flux, define

$$
Q_i=\tau_i\tau_{i+1}.
$$

Cyclicity gives $\prod_iQ_i=1$.  Conversely, a cyclic $Q$-word with product
one, a holonomy $\alpha$, and one choice of $\tau_0$ reconstruct a signing.
The two choices of $\tau_0$ are isospectral at even order, so fixing
$\tau_0=1$ loses no spectral-radius case.

## Local exclusion

On $L$ consecutive vertices, the action of $A$ is a rectangular integer
matrix $C_W$ determined by a $Q$-window $W$ of length $L+1$.  Its Gram matrix
is

$$
M_W=C_W^{\mathsf T}C_W=PA^2P.
$$

If an integral vector $v$ satisfies

$$
\frac{v^{\mathsf T}M_Wv}{v^{\mathsf T}v}>b_n>\theta_n,
$$

then every cyclic signing containing $W$ has
$\rho(A)^2>\theta_n$.  This lemma is independent of enumeration.

## Global closure

The surviving windows are edges of an order-$L$ de Bruijn graph.  A state
stores $L$ consecutive $Q$-bits; an edge appends one bit and moves to the
suffix state.  A parity coordinate records the sum of appended bits modulo
two.  Because $n$ is even, parity zero is equivalent to $\prod_iQ_i=1$.

Length-$n$ closed walks in the parity lift are therefore exactly the globally
legal cyclic $Q$-words whose local windows all survive.  Rotation and
reflection remove duplicate words, while the two holonomies remain separate.

## Exact outcome

| $n$ | support | allowed/all windows | states | rooted even words | canonical $Q$ | terminals |
|---:|---:|---:|---:|---:|---:|---:|
| 34 | 12 | 124 / 8,192 | 92 | 1 | 1 | 2 |
| 36 | 13 | 128 / 16,384 | 92 | 1 | 1 | 2 |
| 38 | 14 | 184 / 32,768 | 132 | 77 | 3 | 6 |
| 42 | 14 | 232 / 32,768 | 166 | 337 | 7 | 14 |
| 44 | 14 | 240 / 32,768 | 171 | 353 | 10 | 20 |
| 46 | 14 | 240 / 32,768 | 171 | 599 | 10 | 20 |

At each order, the all-negative $Q$-word with $\alpha=-1$ is closed by exact
characteristic-polynomial divisibility and largest-root isolation.  Every
other terminal has an exact integer Rayleigh quotient above $b_n$.  Thus all
64 terminals are resolved.

## Order 40

Order 40 is separate.  Its explicit signing satisfies

$$
15541I_{40}-2000A_{40}^2\succ0.
$$

Forty exact rational LDL pivots prove positivity.  The sandwich

$$
\frac{15541}{2000}<\frac{63}{8}
=8-\frac{200}{40^2}<\theta_{40}
$$

then gives a counterexample with no floating endpoint.
