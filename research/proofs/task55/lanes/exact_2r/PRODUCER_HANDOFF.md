# Exact-2r Producer Handoff

Proof status: `EXACT_2R_R123_CLUSTER_AND_FESHBACH_PROVED`.

Evidence: `COMPUTER_ASSISTED_PROVED`.

Mathematical audits: `TWO_INDEPENDENT_MATHEMATICAL_AUDITS_PASSED`
(`PASS`, then `PASS_WITH_SHARPENING`).

Integration: `INDEPENDENT_CHECKER_PASS`. The bulk monodromy convention
mismatch was repaired by comparing the original matrices; the independent
checker and all 29 fail-closed tests pass.

## Producer

Run from the repository root:

```bash
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=research/scripts python3 \
  research/scripts/target_a_task55_exact_2r.py
```

The producer writes only:

```text
research/proofs/task55/certificates/exact_2r_cluster.json
```

It does not write a checker, tests, either formal manuscript, or Git state.

## Stored proof chain

The certificate contains:

- strict contracts and SHA-256 bindings for the positive G6 Evans root,
  global G6 edge, and `delta6=1/100` isolation artifacts;
- a rebuilt `K^2=-I`, `KA=-AK`, `KH=HK` rank-two certificate;
- all eight period-eight monodromy cuts, in both tail directions;
- the common reciprocal Floquet characteristic and exact multiplier bound
  `|mu|<9/25`;
- exact Cauchy--Binet conditioning checks below 17 for every phase;
- the tail calculation `10625/2<73^2`;
- `D0=1040`, `S0=260`, `L_site=248`, and `ell0=31`;
- the exact IMS value `4/845` and complement surplus `9/33800`;
- same-interface and different-interface Gram bounds for all `2r` columns;
- codimension-`2r` min--max and exact fixed-window rank `2r`;
- the correct Gram-orthogonalized `2r` Feshbach identity;
- the explicit bound `|lambda_j-c6|<3505r(9/25)^ell`.

Every acceptance condition is exact rational, integer, symbolic, or strict
interval arithmetic. Decimal condition-number values are diagnostics only.
The producer raises before writing if a dependency contract, phase count,
cofactor pivot, Gram determinant, multiplier bound, constant identity, or
final inequality fails.

## Evidence boundary

Computer-assisted inputs:

```text
simple positive unsquared G6 root
single-G6 global edge and delta6 isolation
exact-rational Floquet multiplier/eigenbasis enclosures
```

Analytic deductions:

```text
K-generated negative mode
rank-two local squared eigenspace
two-mode Gram invertibility
codimension-2r IMS complement
exact 2r fixed-window count
2r Feshbach expansion and 3505r bound
```

The scope is exactly `r=1,2,3` G6 interfaces with period-eight bulk elsewhere
and minimum cyclic site separation `D>=1040`. Rings containing additional
non-G6 defects are outside scope. The `n=100/102` controls are deliberately
absent from the theorem dependencies.

## Independent checker requirements

The checker must not import this producer. It should independently:

1. parse JSON with duplicate-key rejection and enforce the exact schema;
2. rebuild `Q`, `tau`, `A`, and `K`, including reflected orientation;
3. reconstruct all eight symbolic monodromies with an independent product
   implementation;
4. reconstruct stable and unstable Floquet columns and verify every exact
   Cauchy--Binet condition inequality;
5. recompute tail, Gram, IMS, min--max, and Feshbach constants using
   `Fraction` or another exact rational type;
6. reject changed dependency hashes, missing or reordered phases, invalid
   pivots, altered `r` records, weakened strict inequalities, extra JSON keys,
   and any attempt to use `n=100/102` as a large-distance proof input.

This producer lane did not supply the checker or tests. They were subsequently
implemented independently; the certificate now records
`INDEPENDENT_CHECKER_PASS`, and all 29 fail-closed tests pass. Final
integration is no longer blocked.
