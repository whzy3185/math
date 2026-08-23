# Task 55 Lane A handoff: orders 34--46

## Final status

```text
TASK55_ORDERS_34_46_PARTIAL_N40_ONLY
```

- \(n=40\): `COMPUTER_ASSISTED_PROVED`, explicit exact rational LDL
  counterexample certificate.
- \(n=34,36,38,42,44,46\): `OPEN_BOUNDED_SEARCH_ONLY`.
- all even \(n\ge32\) fail: `NOT_PROVED`.

The bounded searches at the six open orders are evidence records only.  They
must not be cited as nonexistence proofs.

## Artifacts

- `research/proofs/task55/TARGET_A_ORDERS_34_46_CERTIFICATES.json`
- `research/proofs/task55/TARGET_A_ORDERS_34_46_DISCOVERY.md`
- `research/proofs/task55/TARGET_A_ORDERS_34_46_EXACT_CLASSIFICATION.md`
- `research/scripts/target_a_task55_orders_34_46.py`
- `research/scripts/verify_target_a_task55_orders_34_46.py`
- `research/scripts/test_target_a_task55_orders_34_46.py`

## Verification

Run with the bundled Python runtime from the repository root:

```bash
PY=/Users/muelsyse/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3
$PY research/scripts/verify_target_a_task55_orders_34_46.py
$PY -m pytest -q research/scripts/test_target_a_task55_orders_34_46.py
```

The tamper suite covers the top-level and order-level statuses; missing,
duplicate, and reordered rows; promotion of an open row; the order-40 word,
lift, rational bound, pivot hash, matrix hash, and both legacy hashes; bounded
search overstatement; an all-even-\(n\ge32\) overclaim; and duplicate JSON
keys.
