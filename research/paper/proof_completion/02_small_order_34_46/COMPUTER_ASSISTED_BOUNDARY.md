# Computer-Assisted Boundary

## Finite proposition verified

For every $n\in\{34,36,38,42,44,46\}$, the checker verifies:

1. the exact minimal polynomial and strict rational interval select
   $\theta_n$ as the rightmost real conjugate;
2. every binary window of length $L_n+1$ is reconstructed and classified;
3. the stored survivor list equals the independently reconstructed list and
   no window is unresolved;
4. the overlap graph gives exactly the stored rooted walks, dihedral classes,
   and both-holonomy terminal list;
5. every terminal has an exact threshold equality or an exact integral
   Rayleigh quotient above the threshold upper endpoint;
6. all counts, orderings, digests, and unresolved totals match.

The lemmas in FULL_PROOF.md prove that this finite proposition implies the
universal no-counterexample statement.

## Local finite object

The reusable support-12, support-13, and support-14 tables contain

$$
2^{13}+2^{14}+2^{15}=57,344
$$

rows.  Each row stores a window code, the integer numerator
$v^{\mathsf T}M_Wv$, the positive denominator $v^{\mathsf T}v$, and a
primitive integer vector.

The producer may use a floating eigensolver to propose $v$.  Acceptance uses
only the reconstructed integer matrix and exact fraction comparison.  The
checker does not import the producer and uses no floating number on an
accepting path.

## Global finite object

| $n$ | allowed windows | states | rooted even | rooted odd | canonical $Q$ | terminals | unresolved |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 34 | 124 | 92 | 1 | 0 | 1 | 2 | 0 |
| 36 | 128 | 92 | 1 | 4 | 1 | 2 | 0 |
| 38 | 184 | 132 | 77 | 38 | 3 | 6 | 0 |
| 42 | 232 | 166 | 337 | 392 | 7 | 14 | 0 |
| 44 | 240 | 171 | 353 | 620 | 10 | 20 | 0 |
| 46 | 240 | 171 | 599 | 690 | 10 | 20 | 0 |

The terminal total is 64.  The number 84 is a stale documentation error, not
an alternate accepted count.

## Human completeness boundary

The following implications are proved in the text rather than delegated to a
program:

- every signing yields legal $(Q,\alpha)$ data;
- the two $\tau$-lifts are isospectral;
- a forbidden local window forces the spectral lower bound;
- overlap closure plus parity closure is equivalent to a legal cyclic word;
- dihedral canonicalisation preserves spectral radius;
- checking both holonomies exhausts the remaining sectors;
- resolving every terminal with no unresolved record proves the universal
  statement.

The machine verifies the finite premises.

## Order-40 boundary

The checker reconstructs the signing from (18), forms

$$
15541I_{40}-2000A_{40}^2,
$$

and recomputes forty positive exact rational LDL pivots.  It binds the matrix,
pivot stream, and preserved sources by SHA-256.  The spectral consequence and
$63/8<\theta_{40}$ are human deductions given in the proof.

## Fail-closed behavior

The small-order checker rejects duplicate JSON keys, BOM or CRLF, JSON
floating numbers, nonintegral fields, noncanonical or oversized vectors,
missing or reordered windows, survivor changes, walk changes, terminal
changes, threshold or polynomial changes, digest changes, and any nonzero
unresolved count.  The focused suite contains 23 tamper tests.

## Reproduction

    PYTHONPATH=research/scripts python3 research/scripts/verify_target_a_task55_small_order_exact.py
    PYTHONPATH=research/scripts python3 -m pytest -q research/scripts/test_target_a_task55_small_order_exact.py
    PYTHONPATH=research/scripts python3 research/scripts/verify_target_a_task55_orders_34_46.py
    PYTHONPATH=research/scripts python3 -m pytest -q research/scripts/test_target_a_task55_orders_34_46.py

Expected markers are TARGET_A_TASK55_SMALL_ORDER_EXACT_VERIFY_PASS and
TARGET_A_TASK55_ORDERS_34_46_VERIFY_PASS.
