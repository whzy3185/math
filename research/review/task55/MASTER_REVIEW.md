# Target A Task 55 Hostile Independent Review

Date: 2026-08-24

Reviewed working checkpoint:

```text
branch  agent/target-a-discovery-snapshot
HEAD    bd1934da29a2eb56cf2045554c00c104d79a7959
state   uncommitted Task 53--55 research work in progress
```

## 1. Review standard and verdict

This review treats a stored status string as metadata, not evidence. A claim is
accepted only when its mathematical scope is explicit, its dependencies are
identified, and its accepting path is analytic, exact, interval-certified, or
independently reconstructed by a fail-closed checker. A bounded negative
search is never promoted to a theorem. High-precision agreement is never
promoted to exact evidence.

**Hostile verdict: PASS.** The central Task 55
repair is mathematically credible at its stated evidence tier. In particular,
the single-G6 squared level has rank two, the old exact-`r` chain is false, the
replacement exact-`2r` theorem for `r in {1,2,3}` and `D>=1040` passes an
implementation-independent reconstruction, and `N_exp=3120` is a proved
sufficient onset for that exponential construction. The exact small-order and
support-18 multi-gap certificates also pass independent reconstruction.

This verdict does **not** promote the computer-assisted inputs to pure analytic
theorems, does not prove any open interaction coefficient or simplicity claim,
and does not enlarge any read-only finite frontier.

## 2. Adverse findings

### Finding A: stale status prose after the exact-2r upgrade, resolved

Several documents still describe the corrected exact-`2r` theorem as pending
or open even though `certificates/exact_2r_cluster.json` records
`INDEPENDENT_CHECKER_PASS` and the checker passed in this review:

- `TARGET_A_G6_RANK_DOUBLING_CORRECTION.md` says the exact-`2r` theorem remains
  pending;
- `TARGET_A_COMMON_LIMINF_TASK55.md` calls the exact-`2r` certificate pending;
- `TARGET_A_COMMON_LIMIT_TASK55.md` discusses acceptance only hypothetically;
- `lanes/exact_2r/PRODUCER_HANDOFF.md` reports integration PASS near the top but
  still says final integration is blocked near the end;
- historical Task 54 exact-`r` documents correctly retract their own theorem
  but still call the later exact-`2r` replacement open.

These contradictions did not invalidate the certificate, but they made global
status extraction unsafe. Integration corrected the Task 55 files, marked the
Task 53 dimension as falsified, and added a Task 55 supersession notice to the
historical Task 54 status documents. The final active synthesis now cites the
Task 55 exact-`2r` theorem and certificate as authoritative.

### Finding B: exact-2r remains conditional on upstream computer-assisted inputs

The independent checker rebuilds the G6 symmetry, all 32 Floquet charts, the
exact rational constants, the dimension count, the Feshbach formulas, and the
residue endpoints. It binds three upstream artifacts by SHA-256. It does not
re-prove from first principles the Task 50 simple positive Evans root, the
Task 53 global edge classification, or the Task 54 complement isolation.

Accordingly, the exact-`2r` cluster, `3505r` estimate, and `N_exp=3120` have the
correct status `COMPUTER_ASSISTED_PROVED`, conditional on those bound certified
inputs. They must not be described as purely analytic or checker-independent
facts. The certificate's claim that two earlier mathematical audits passed is
also metadata unless the corresponding audit records are separately retained;
the present review does not count that string as additional evidence.

### Finding C: one administrative field was not fully fail-closed, resolved

The verifier originally accepted either `PENDING_INDEPENDENT_CHECKER_PASS` or
`INDEPENDENT_CHECKER_PASS` for the integration field. Integration tightened
the checker to require only the final value and added a tamper test that
rejects a regression to `PENDING`. The mathematics was unaffected, and the
administrative state is now fail-closed.

### Finding D: the global even-order classification is a composite theorem

The Task 55 small-order certificate proves nonexistence only for
`n=34,36,38,42,44,46`. The exact order-40 LDL certificate proves failure at
`n=40`. The statement

```text
failure exactly at n=32, n=40, and every even n>=48
```

also depends on inherited complete results for `8<=n<=32` and on the separate
finite-plus-IMS theorem for every even `n>=48`. It is valid as a composite
project theorem if those inherited dependencies remain accepted; it is not a
self-contained consequence of the small-order JSON alone. This review reran
the Task 55 small-order and order-40 checkers, but did not rerun the full
pre-Task-55 classification or the complete `N_star=48` regression.

## 3. Evidence ledger

### A. Theorem-valid analytic deductions

The following deductions are valid at the mathematical level stated in their
documents, with any certified inputs kept explicit:

1. The symmetry
   `K^2=-I`, `KA=-AK`, `KH=HK` maps a simple positive G6 root to a simple
   negative root and gives `rank P_(H6,{c6})=2`.
2. The Gram-orthonormalized Schur complement is genuinely `2r` dimensional and
   uses `det(H_eff(z)-z I_(2r))=0`; the old coordinate expression with `-zP`
   was dimensionally invalid.
3. The static Hermitian simplicity criteria and the exact Feshbach derivative
   criterion are correct abstract statements. They do not establish physical
   finite-ring simplicity.
4. The restricted dilute-G6 liminf and the explicit-family common limsup upper
   bounds survive the rank correction.
5. The `(3,3)` local motif lemma has a complete finite dependency closure and
   yields the uniform exact bound `419/53>c6` for arbitrary finite core length.

### B. Computer-assisted proved

The following are accepted as `COMPUTER_ASSISTED_PROVED`, not as read-only
experiments:

- single-G6 rank two and the negative-spectrum bridge;
- for `r=1,2,3`, `D>=1040`, exactly `2r` squared levels in
  `[c6-1/400,c6+1/400]`;
- the bound
  `|lambda_j-c6|<3505r(9/25)^ell` and the corrected `2r` Feshbach reduction;
- the sufficient continuous exponential onset `N_exp=3120`;
- no counterexample at `n=34,36,38,42,44,46`;
- the exact order-40 counterexample;
- all 31,008 canonical primitive multi-gap cores with support sum in
  `{2,6,10,14,18}` have an exact integer Rayleigh witness above `c6`;
- the gap-2/gap-6 quotient involution and order-five recurrence, within their
  explicitly nonphysical algebraic scope.

The stronger full even-order classification is accepted only as the composite
theorem described in Finding D.

### C. Exact finite read-only

The following calculations use exact arithmetic but lack a bound producer and
independent proof artifact. They are research evidence, not repository
theorems:

- the reference-relative `F4/F5` graph calculation on 105 states/164 edges
  and its 420-state/656-edge phase lift;
- the associated no-negative-cycle and reference-only-zero-orbit excursion
  statements;
- the period-25 and period-26 frontier counts and exact witnesses for their
  153 survivors.

These items remain `EXACT_FINITE_READ_ONLY`. In particular, the integrated
periodic frontier remains `p<=24`, not `p<=26`.

### D. Falsified, withdrawn, or rejected

The following claims must not re-enter any theorem statement or dependency
graph:

- exactly `r` squared G6 levels for `r` separated interfaces;
- a codimension-`r` complement and problem-specific `r x r` Feshbach model;
- the mixed-space equation `H_eff-zP`;
- the raw uncalibrated `c6`-weighted moment/coboundary strict-sign claim;
- insertion or deletion of a period-eight reference cell as a spectral
  equivalence.

The earlier `(3,3)` wording that assigned numerator exactly `874` to every
`a=1` case was also false. The corrected statement records possible
numerators `{874,902}` and the valid uniform lower bound `N>=874`; the final
`419/53` theorem is unaffected.

### E. Open

No Task 55 artifact proves any of the following:

- the universal finite-core `B0 -> B2` lower theorem;
- motif-free primitive multi-gap cores beyond support sum 18;
- the physical all-single-gap hierarchy;
- unrestricted common-residue liminf or the three common nonzero-residue
  limits;
- finite-ring simplicity of the individual `2r` cluster levels;
- a universal leading interaction coefficient, pairwise-additive three-site
  model, or genuine three-body interaction;
- a spectral bridge from reference-relative graph cost to operator norm;
- an integrated periodic frontier beyond period 24 or control of aperiodic
  limits.

High-precision transfer/Evans splitting data may guide these questions but
remain discovery evidence until enclosed by exact or interval certificates.

## 4. Explicit audits requested

### Rank-two G6

**PASS at `COMPUTER_ASSISTED_PROVED`.** The checker reconstructs the infinite
coefficient identities over a full period/core reduction and verifies finite
integer control windows of dimensions 58, 90, and 138. Together with the
bound simple positive Evans root, anticommutation gives the negative root and
two-dimensional squared eigenspace. This directly falsifies exact-`r`.

### Exact-2r

**PASS at `COMPUTER_ASSISTED_PROVED`.** The verifier is separate from the
producer and rebuilds transfer products, reciprocal Floquet structure, phase
charts, condition bounds, Gram estimates, IMS loss, min-max count, and the
Schur-complement constants. The theorem is restricted to `r in {1,2,3}`,
period-eight bulk outside the interfaces, both orientations and holonomies,
and minimum cyclic interface separation `D>=1040`. It makes no level
simplicity or coefficient nonvanishing claim.

### N_exp=3120

**PASS as a sufficient, nonminimal threshold.** The exact checker reconstructs
the first eligible nonzero-residue endpoints `1042`, `2084`, and `3126`, all
with effective distance `1042` and `ell=31`, as well as the residue-zero
period-eight comparison at `n=3120`. Monotonicity within each residue class
then covers every even `n>=3120`. This does not improve or replace the stronger
independent project threshold `N_star=48`.

### Small-order classification

**PASS at `COMPUTER_ASSISTED_PROVED`.** The checker does not import the
producer and uses no floating point on an accepting path. It independently
reconstructs exact threshold polynomials, all local window decisions, the
de Bruijn closure, parity, dihedral classes, both holonomy sectors, and every
terminal witness. The six orders have zero unresolved terminals. The separate
order-40 checker also passes its exact rational LDL reconstruction.

### Multi-gap support through 18

**PASS at `COMPUTER_ASSISTED_PROVED`, with a strict bounded scope.** Two
independently organized checkers reproduce the counts
`1,16,186,2275,28530`, all 31,008 exact full-image Rayleigh inequalities, the
JSONL digest, the unique weakest word `(3,3)`, and the corrected 32-case local
lemma. No conclusion is available for arbitrary support merely from this
finite certificate.

### Frozen manuscripts

**PASS.** At the reviewed HEAD the Git tree hashes are:

```text
English  59e3a8f73a152ef06f994e979b7219a3365efeae
Chinese  57ae03fb5b90866f84d0d72b414008678e8f5004
```

Both manuscript directories have no tracked diff and no untracked files.
Task 55 results remain outside the frozen formal manuscripts.

## 5. Verification actually run

The following commands were run with the bundled Python runtime during this
review:

```text
verify_target_a_task55_exact_2r.py                 PASS
verify_target_a_task55_small_order_exact.py        PASS
verify_target_a_task55_multigap.py                 PASS
verify_target_a_task55_multigap_alt.py             PASS
verify_target_a_task55_orders_34_46.py             PASS
verify_target_a_task55_single_gap.py               PASS
```

Focused fail-closed tests were initially run in three invocations:

```text
exact-2r + rank correction + small order + multigap   92 passed
orders 34--46 legacy/order-40 lane                    18 passed
single-gap quotient/recurrence lane                   19 passed
total focused pytest cases                           129 passed
```

After Findings A and C were resolved, integration reran the tightened
exact-`2r` suite (`30 passed`) and then ran the complete feasible research
regression:

```text
pytest -q research/scripts
684 passed, 3 skipped, 20 subtests passed
```

The skipped cases are retained repository skips, not newly suppressed Task 55
failures. `git diff --check` also passed after integration.

## 6. Publication disposition

Task 55 is fit to serve as a research checkpoint. Publication text may rely
on rank two, exact
`2r`, the explicit exponential constants, `N_exp=3120`, the exact small-order
closure, and the bounded multi-gap theorem only with their computer-assisted
dependencies and precise scopes disclosed. The open and read-only items above
must remain outside theorem statements.
