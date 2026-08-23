# Task 55 Small-Order Exact Verifier Handoff

## Scope

This lane independently verifies the exact finite classification at

```text
n = 34, 36, 38, 42, 44, 46.
```

It writes only:

```text
research/scripts/verify_target_a_task55_small_order_exact.py
research/scripts/test_target_a_task55_small_order_exact.py
research/proofs/task55/lanes/small_order_exact/VERIFIER_HANDOFF.md
```

The verifier does not import the producer and does not use floating point on
an accepting path.

## Independent Reconstruction

For each order, the checker independently constructs

```text
theta_n = 4 + 2 cos(2 pi/n) + 2 cos(4 pi/n).
```

It computes the exact minimal polynomial and isolates its rightmost real root.
This is the required root: every conjugate has the form

```text
2 + 2c + 4c^2,  c = cos(2 pi k/n),
```

and the `k=+/-1` value is the unique largest conjugate for these orders.  The
stored tighter interval is then proved to lie inside the independently
isolated interval and to contain exactly one polynomial root.

For every binary Q window, the checker builds the open-line rectangular
operator `C_Q` directly from

```text
(Av)_i = v_(i-1) + v_(i+1) + tau_(i-2) v_(i-2) + tau_i v_(i+2),
Q_i = tau_i tau_(i+1),
```

and forms `M_Q=C_Q^T C_Q`.  Fraction-free Sylvester tests at independent
rational lower and upper endpoints classify every window:

```text
lower*I-M_Q positive definite  => ALLOWED,
upper*I-M_Q not positive definite => EXCLUDED.
```

The interval between the two tests contains no unresolved window.

The allowed windows are used as de Bruijn edges.  The checker independently
enumerates length-n rooted closed walks, applies even Q parity, takes binary
dihedral canonical representatives, and checks both `alpha=-1,+1` terminal
sectors.  Nonoptimizer terminals are closed by exact integer Rayleigh
quotients above a rigorously checked threshold upper endpoint.  The
`Q=0, alpha=-1` optimizer is checked by exact `charpoly(A^2)` factorization and
rightmost-root isolation; its threshold factor and largest-root multiplicity
are both four.

## Independent Counts

| n | support | allowed windows | automaton states | rooted even | rooted odd | canonical Q | terminals |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 34 | 12 | 124 | 92 | 1 | 0 | 1 | 2 |
| 36 | 13 | 128 | 92 | 1 | 4 | 1 | 2 |
| 38 | 14 | 184 | 132 | 77 | 38 | 3 | 6 |
| 42 | 14 | 232 | 166 | 337 | 392 | 7 | 14 |
| 44 | 14 | 240 | 171 | 353 | 620 | 10 | 20 |
| 46 | 14 | 240 | 171 | 599 | 690 | 10 | 20 |

The independent local reconstruction has zero unresolved windows.  The
expected terminal total is 84 and the required final unresolved total is
zero.

## Fail-Closed Boundary

The checker rejects duplicate JSON keys, BOM/CRLF, JSON floating numbers,
nonintegral integer fields, noncanonical or oversized vectors, and all count
or digest mismatches.  Tamper tests cover missing, duplicate, and out-of-order
window rows, survivor windows, closed walks, and terminals, together with
changes to Q, alpha, vectors, thresholds, polynomial data, hashes, and
`terminal_unresolved`.

## Final Verification

The producer atomically wrote

```text
research/proofs/task55/certificates/small_order_exact_classification.json
sha256 cb12d8502c6fcf31c5e8f1d23f3b9f1bb44b28b05a58f2e02067df08c04132b4
```

The certificate binds producer SHA-256

```text
6dad3e00b821ead460efefdeb1153a5bdf92243beefedd63f451f6de26dd745e
```

and the independent checker verified that binding before reading any stored
mathematical conclusion.

```text
PYTHONPATH=research/scripts .venv/bin/python \
  research/scripts/verify_target_a_task55_small_order_exact.py

TARGET_A_TASK55_SMALL_ORDER_EXACT_VERIFY_PASS
n=34 allowed=124 rooted_even=1 classes=1 terminals=2
n=36 allowed=128 rooted_even=1 classes=1 terminals=2
n=38 allowed=184 rooted_even=77 classes=3 terminals=6
n=42 allowed=232 rooted_even=337 classes=7 terminals=14
n=44 allowed=240 rooted_even=353 classes=10 terminals=20
n=46 allowed=240 rooted_even=599 classes=10 terminals=20
```

```text
PYTHONPATH=research/scripts .venv/bin/python -m pytest -q \
  research/scripts/test_target_a_task55_small_order_exact.py

23 passed in 38.58s
```

Final verifier status:

```text
TASK55_SMALL_ORDER_EXACT_CLASSIFICATION_PROVED
terminal_unresolved = 0
```

Therefore no counterexample exists at any of
`n=34,36,38,42,44,46`.  This statement is an exact finite classification,
not a bounded-search observation.
