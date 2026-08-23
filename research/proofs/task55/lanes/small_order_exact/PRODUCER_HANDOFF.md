# Task 55 Small-Order Exact Producer Handoff

## Scope

This lane classifies `n=34,36,38,42,44,46`. It does not modify or replace the
existing `orders_34_46` producer, checker, or documents. It supplies a separate
exact local-interlacing certificate for an independent checker.

## Run

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 \
VECLIB_MAXIMUM_THREADS=1 PYTHONPATH=research/scripts \
python3 research/scripts/target_a_task55_small_order_exact.py
```

Output:

`research/proofs/task55/certificates/small_order_exact_classification.json`

Latest completed producer run:

```text
elapsed_seconds: 153.7982560829987
output_bytes: 5388251
output_sha256: cb12d8502c6fcf31c5e8f1d23f3b9f1bb44b28b05a58f2e02067df08c04132b4
payload_core_sha256: 442823092667efc876214b035f8061b2e773da3a04023044ec732055985f4bd0
terminal_unresolved_total: 0
```

The JSON is intentionally compact. Window rows use the schema

```text
[window_code, numerator, denominator, integer_vector]
```

and are shared by all orders using the same support length.

## Acceptance boundary

Floating-point eigensolvers only propose integer vectors. The producer accepts
a local exclusion or terminal exclusion only after recomputing its quadratic
form with integers and comparing `Fraction(numerator,denominator)` strictly
against a rational upper endpoint proved symbolically above the exact
trigonometric threshold.

The all-negative `alpha=-1` terminal is checked by exact divisibility of its
`A^2` characteristic polynomial by the threshold minimal polynomial. This
proves that the threshold is an eigenvalue and is sufficient to exclude a
strict counterexample. No numerical nonexistence decision is used.

## Independent checker requirements

The checker must not import this producer. It should independently:

1. Reject duplicate JSON keys and noncanonical integer encodings.
2. Reconstruct all three local window tables and their row hashes.
3. Recompute every integer quadratic form from the Q-window.
4. Reprove each strict threshold enclosure from the trigonometric algebraic number.
5. Rebuild every per-order survivor partition from exact rational comparisons.
6. Rebuild the parity-lift overlap graph and all rooted closed words.
7. Independently canonicalize every rooted Q word under the dihedral action.
8. Reconstruct both alpha-sector full matrices and every terminal quotient.
9. Recheck the all-negative `alpha=-1` terminal by exact polynomial divisibility.
10. Require `terminal_unresolved=0` and exact agreement with every stored count and digest.

Required tamper cases include changed window code/vector/quotient, deleted or
duplicated rows, row reordering, altered threshold endpoint, survivor migration,
parity-bit changes, missing rooted words, noncanonical terminals, alpha swaps,
changed optimizer polynomial, forged count/hash, float-valued integers, and
oversized integers.

## Evidence status

Producer completion supports `EXACT_FINITE_PRODUCER`. Upgrade to
`COMPUTER_ASSISTED_PROVED` requires the independent checker and tamper suite.
