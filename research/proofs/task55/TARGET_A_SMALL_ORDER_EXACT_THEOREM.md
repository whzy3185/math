# Target A Small-Order Exact Classification

## Theorem

For each

\[
n\in\{34,36,38,42,44,46\},
\]

every signing satisfies

\[
\rho(A)^2\ge
4\left(\cos^2\frac{\pi}{n}+\cos^2\frac{2\pi}{n}\right).
\]

Consequently none of these six orders is a counterexample. Combined with the
inherited complete classification through order 32, the exact counterexample
at order 40, and the certified tail for every even order at least 48, the
classification for even `n>=8` is:

\[
\boxed{\text{failure exactly at }n=32,\ n=40,\text{ and every even }n\ge48.}
\]

The independent checker has reconstructed the complete certificate without
importing the producer and without floating point on any accepting path.  Its
final output is

```text
TARGET_A_TASK55_SMALL_ORDER_EXACT_VERIFY_PASS
terminal_unresolved = 0
```

and the 23-case fail-closed tamper suite passes.  The theorem therefore has
final evidence status `COMPUTER_ASSISTED_PROVED`.  The generated JSON retains
its producer-stage `EXACT_FINITE_PRODUCER` label intentionally; the separate
checker and verifier handoff are the second artifact that upgrades the
mathematical conclusion.

## Local interlacing lemma

Fix `L` consecutive vertices and a Q-window of length `L+1`. After a local tree
gauge, let `C_Q` map a vector supported on those `L` vertices to its image under
the signed adjacency operator. The range-two property gives an output support
of length `L+4`, and

\[
M_Q=C_Q^T C_Q=P A^2P.
\]

Thus every cyclic signing containing the window satisfies

\[
\lambda_{\max}(A^2)\ge\lambda_{\max}(M_Q)
\ge \frac{v^TM_Qv}{v^Tv}
\]

for every integer vector `v`. The two local tau lifts differ by an exact signed
conjugacy, so one lift per Q-window suffices. The ring holonomy `alpha` does not
enter this local certificate.

For each order the producer proves an exact strict enclosure

\[
L_n<\rho_-(n)^2<U_n
\]

and deletes a window only when its stored integer vector satisfies

\[
v^TM_Qv>U_n v^Tv.
\]

No floating-point comparison is accepted as a certificate.

## Finite closure

The surviving windows form a de Bruijn overlap graph. The producer enumerates
all length-`n` closed walks in its parity lift, retains exactly the even-parity
Q words, and then quotients them by rotations and reflections. The exact counts
are:

| n | support L | surviving/all windows | graph states | rooted legal words | canonical Q terminals | `(Q,alpha)` terminals |
|---:|---:|---:|---:|---:|---:|---:|
| 34 | 12 | 124 / 8,192 | 92 | 1 | 1 | 2 |
| 36 | 13 | 128 / 16,384 | 92 | 1 | 1 | 2 |
| 38 | 14 | 184 / 32,768 | 132 | 77 | 3 | 6 |
| 42 | 14 | 232 / 32,768 | 166 | 337 | 7 | 14 |
| 44 | 14 | 240 / 32,768 | 171 | 353 | 10 | 20 |
| 46 | 14 | 240 / 32,768 | 171 | 599 | 10 | 20 |

Every terminal is checked in both holonomy sectors. For the all-negative Q word
with `alpha=-1`, exact characteristic-polynomial divisibility proves that the
conjectured threshold itself is an eigenvalue; this already excludes a strict
counterexample. Every other terminal has a stored full-ring integer Rayleigh
quotient strictly above `U_n`. Hence `terminal_unresolved=0` at all six orders.

## Certificate boundary

The compact certificate stores all 57,344 local windows across supports 12,
13, and 14. Each row contains the window code, integer numerator, integer
denominator, and integer vector. Per-order records bind the exact threshold
interval, complete survivor partition, rooted closed walks, canonical terminal
Q codes, both alpha sectors, all terminal witnesses, and SHA-256 digests.

The producer is
`research/scripts/target_a_task55_small_order_exact.py`; the generated artifact
is `research/proofs/task55/certificates/small_order_exact_classification.json`.
Its SHA-256 digest is
`cb12d8502c6fcf31c5e8f1d23f3b9f1bb44b28b05a58f2e02067df08c04132b4`.
The implementation-independent verifier is
`research/scripts/verify_target_a_task55_small_order_exact.py`, and its
fail-closed suite is
`research/scripts/test_target_a_task55_small_order_exact.py`.  Full verifier
details and exact reconstructed counts are recorded in
`research/proofs/task55/lanes/small_order_exact/VERIFIER_HANDOFF.md`.  Neither
formal manuscript is modified by this result.
