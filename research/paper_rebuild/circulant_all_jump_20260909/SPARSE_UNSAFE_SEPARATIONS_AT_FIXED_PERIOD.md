# Asymptotically sparse unsafe defect separations at fixed period

Date: 2026-09-10

Status: **Proved**. This is a counting corollary of the exact phase diagram and the logarithmic bulk-width theorem.

## Setup

Fix a coefficient period

\[
P=4S,
\qquad S\ge2.
\]

The even two-defect separations are parametrized by

\[
m=1,2,\ldots,S-1,
\]

with

\[
N=S-m,
\qquad h=2m.
\]

Let `N_*(S)` be the smallest safe complementary bulk parameter:

\[
N_*(S)=\min\{1\le N\le S-1:2(S-N)<T_N(3)\}.
\]

## Theorem — only logarithmically many separations are unsafe

The number of even defect separations whose Bloch spectrum reaches or exceeds the squared threshold `8` is exactly

\[
\boxed{N_*(S)-1.}
\tag{1}
\]

Consequently, with

\[
\Lambda=3+2\sqrt2,
\]

\[
\boxed{
\#\{\text{unsafe even separations at period }P\}
=\log_{\Lambda}P+O(1).
}
\tag{2}
\]

Since the total number of admissible even separations is `S-1=P/4-1`, the unsafe proportion satisfies

\[
\boxed{
\frac{\#\{\text{unsafe separations}\}}
{\#\{\text{all even separations}\}}
=O\!\left(\frac{\log P}{P}\right)
\longrightarrow0.
}
\tag{3}
\]

Equivalently, asymptotically almost every even separation in this two-defect family is globally sub-eight.

## Proof

For fixed `S`, the exact phase diagram says that the separation corresponding to `N` is safe if and only if

\[
2(S-N)<T_N(3).
\]

The left side decreases strictly in `N`, while the right side increases strictly. Hence safety begins exactly at `N=N_*(S)` and persists for every larger `N`.

Therefore the unsafe values are

\[
N=1,2,\ldots,N_*(S)-1,
\]

which proves (1).

The logarithmic bulk-width theorem gives

\[
N_*(S)=\log_{\Lambda}(4S)+O(1).
\]

Since `P=4S`, this is exactly (2). Dividing by `S-1` yields (3).

## Interpretation

The threshold failure region is geometrically very thin in two different senses:

1. for fixed `(N,m)`, any dangerous Bloch phase is exponentially localized near the antiperiodic long-phase coordinate;
2. for fixed total cell size, only logarithmically many of the linearly many possible even defect separations are unsafe.

Thus the exact Chebyshev phase boundary describes a sparse boundary layer both in phase space and in defect-geometry space.