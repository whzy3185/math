# Task 55 Exact-2r Independent Verifier Handoff

## Scope

This lane owns only:

```text
research/scripts/verify_target_a_task55_exact_2r.py
research/scripts/test_target_a_task55_exact_2r.py
research/proofs/task55/lanes/exact_2r/VERIFIER_HANDOFF.md
```

No producer, certificate, theorem, manuscript, branch, worktree, commit, or
remote operation belongs to this verifier lane.

## Independence Boundary

The checker does not import the producer. It independently implements:

- `Q_i` for the G6 interface and `tau_(i+1)=Q_i tau_i`;
- the four-coordinate one-step transfer and ordered eight-step products;
- exact `Fraction` interval arithmetic with 120-digit outward square roots;
- first-three-row cofactor eigenvectors and nondegenerate two-coordinate
  charts;
- all 32 combinations of two lambda signs, two tail orientations, and eight
  bulk phases;
- symbolic monodromy determinants and characteristic polynomials;
- the exact anticommuting symmetry on three integer control windows;
- all tail, Gram, IMS, Feshbach, distance, and residue-endpoint inequalities.

The expensive reconstruction is memoized within one Python process. Tampered
certificates are still parsed and compared independently on every call.

## Certificate Contract

The expected artifact is:

```text
research/proofs/task55/certificates/exact_2r_cluster.json
```

Its required top-level blocks are:

```text
schema_version
status
evidence
mathematical_audit_status
integration_status
dependencies
rank_two_input
bulk_floquet
constants
gram
complement
counting
feshbach
exponential_tail
scope
checks
```

The checker compares every mathematical block with an independently rebuilt
value. Stored booleans cannot substitute for any reconstruction. The G6
global-edge dependency is bound by its current byte SHA-256 and is also
opened with duplicate-key rejection; its rank-two symmetry records are
recomputed from integer matrices.

The required `exponential_tail` block is exactly the return value of
`expected_exponential_tail()` in the checker. It binds `N_exp`, all three
nonzero-residue endpoints, the period-eight endpoint, and the last
distance-ineligible residue-six predecessor. Its compact field layout is:

```text
N_exp = 3120
distance_formulas = {2,4,6 formulas}
ell_formula = floor((floor(D/4)-12)/8)
residue_endpoints = independently rebuilt exact rational records
period_eight_endpoint = exact n=3120 margin record
predecessor_control = {n:3118,D:1038,ell:30}
```

No JSON floating-point value is accepted anywhere. Duplicate keys are
rejected before semantic verification. Legacy exact-`r`, rank-`r`, `r x r`,
`I_r`, and `H_eff-zP` contracts fail closed.

## Status Upgrade

The checker accepts the proof fields only as:

```text
status = EXACT_2R_R123_CLUSTER_AND_FESHBACH_PROVED
evidence = COMPUTER_ASSISTED_PROVED
mathematical_audit_status = TWO_INDEPENDENT_MATHEMATICAL_AUDITS_PASSED
```

During the checker run, `integration_status` may remain
`PENDING_INDEPENDENT_CHECKER_PASS`. After the checker and all 29 tests pass,
the producer-owned artifact and theorem may upgrade only these integration
records:

```text
integration_status = INDEPENDENT_CHECKER_PASS
checker_integration_note = independent exact-2r checker and 29 tamper tests PASS
checks.independent_checker_passed = true
```

The old `checks.checker_integration_still_pending` field must then be removed;
all mathematical fields and certificate digests remain unchanged except for
the required dependency-hash regeneration.

## Rebuilt Constants

The independent chain verifies:

```text
q = 9/25
K = 17
16 K^2/(1-q^2) = 10625/2 < 73^2
residual constant = (16+8) 73 = 1752
m = 2r, r in {1,2,3}
||G-I|| <= m 73^2 q^(2 ell)
D0 = 1040, ell0 = 31
IMS(D0) = 320/260^2 = 4/845
delta6-IMS > 1/200
window radius = 1/400
complement inverse bound = 400
||T1|| < 3504 r q^ell
||R2|| < r q^ell
|lambda_j-c6| < 3505 r q^ell
N_exp = 3120
```

The residue endpoints are `(2,1042)`, `(4,2084)`, and `(6,3126)`, all with
`D=1042` and `ell=31`. The checker also verifies the off-by-one controls
`ell(1039)=30`, `ell(1040)=31`, and the final ineligible residue-six order
`n=3118`, `D=1038`, `ell=30`.

## Tamper Coverage

Focused tests reject changes to:

- local or cluster dimensions;
- `K`, `q`, tail, residual, or Gram constants;
- IMS, complement window, and inverse constants;
- Feshbach dimension, coordinate equation, expansion, and both remainder
  bounds;
- `D0`, `ell0`, `N_exp`, residue labels, and residue endpoints;
- the G6 dependency hash or a monodromy hash;
- chart count, status-only checks, legacy exact-`r` fields, floats, and
  duplicate JSON keys.

## Execution

After the producer creates the certificate:

```bash
PYTHONPATH=research/scripts python3 research/scripts/verify_target_a_task55_exact_2r.py
PYTHONPATH=research/scripts python3 -m pytest -q research/scripts/test_target_a_task55_exact_2r.py
```

The success marker is:

```text
TARGET_A_TASK55_EXACT_2R_VERIFY_PASS
```

## Verification Result

On 2026-08-24 the independent checker was run against the producer-owned
certificate, including its completed top-level `exponential_tail` block. The
real certificate passed the full reconstruction, and all focused tamper tests
passed:

```text
TARGET_A_TASK55_EXACT_2R_VERIFY_PASS
29 passed in 41.52s
```

The independently rebuilt audit summary is:

```text
chart count = 32
maximum ceil(K^2 upper) = 93 < 17^2
chart record digest = 7322de4392ea740232c4290015e48f9f8b251b367c2b1c1bedfda3d7cecf37db
exact interval digest = f8a6e80916e82002f395f5c75598966acd3a6a1e8fcac6e39889fb1b3bbad58f
single-interface rank = 2
cluster dimensions = {1: 2, 2: 4, 3: 6}
symmetry-window digest = d368e9cb0605748e5dca5b8c155a0facd87f113885548576e79b23279d066020
G6 dependency SHA-256 = 299b5a17e8bbb13aaf183798883c52287c01bf3c5c8090aa80bf15ab005b621f
```

At verifier handoff time the producer artifact recorded
`PENDING_INDEPENDENT_CHECKER_PASS`. The integration-only upgrade has since
been applied: the certificate now records `INDEPENDENT_CHECKER_PASS`, and the
checker requires that final value.
