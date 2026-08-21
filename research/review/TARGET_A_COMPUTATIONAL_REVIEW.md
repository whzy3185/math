# Target A Computational Review

Date: 2026-08-21

Role: independent referee for computer-assisted mathematics

Recommendation: **MAJOR REVISION**

Severity counts: **BLOCKER 0 / MAJOR 2 / MODERATE 3 / MINOR 1**

## Scope and Overall Assessment

I reviewed the new large-order enumeration route formed by
`target_a_independent_orbit_scan.c`, `target_a_record_set_audit.py`, its tests,
the machine-readable summaries in `target_a_large_order_completeness/`, and
`TARGET_A_FINITE_MINIMALITY_TRUST_MAP.md`. I also traced their interfaces to
`target_a_bracelets.py`, `target_a_minimality_search.py`, checkpoint replay,
the exact threshold/Rayleigh decision, and the top-level minimality verifier.

The new C full-space scan is a substantial and valid improvement over aggregate
Burnside checks. For the intended even orders it performs an exact,
ordering-independent consumption of every canonical `Q` record and checks the
corresponding dihedral orbit size. I found no concrete omission, duplication,
orbit-size error, arithmetic error, or holonomy-specific counterexample in the
reviewed runs. The archived `n=24,26,28,30` histograms are internally coherent,
and fresh referee runs at `n=24` and `n=26` reproduced the archived counts.

This does **not**, however, close the entire computational trust boundary for
the smallest-counterexample theorem. The new route independently checks the
enumerated `Q`-orbit set, but it does not independently reconstruct and verify
the exact spectral exclusion attached to each `(Q,alpha)` state. The existing
checkpoint replay authenticates opaque certificate digests rather than
recomputing the per-state certificates. That remaining correlated
implementation risk must be stated plainly.

## Findings

### MAJOR 1: Search/certificate separation remains incomplete

The C scanner consumes only `(canonical Q word, orbit size)` records
(`target_a_independent_orbit_scan.c`, lines 110--159). It never constructs a
signed adjacency matrix, visits either holonomy as a mathematical state, or
checks a Rayleigh inequality. The Python driver labels the resulting count as
`canonical_spectral_states = 2 * representatives` and declares holonomy
coverage (`target_a_record_set_audit.py`, lines 138--160), but those spectral
decisions remain entirely in `target_a_minimality_search.py`.

In the production search, the exact logic is sound in form: a floating
eigenvector only proposes an integer vector, `||Av||^2/||v||^2` is evaluated
with integer arithmetic, and comparison with a certified algebraic upper bound
is exact (`target_a_minimality_search.py`, lines 886--944). The problem is the
saved proof object. Each per-state record is fed into SHA-256 and then discarded
(lines 922--963); the integer vector is not retained for the overwhelmingly
dominant `RAYLEIGH_CERTIFIED` path. Checkpoint replay regenerates the input
cursor but merely hashes the already stored per-chunk certificate digests
(`target_a_checkpoint_replay.py`, lines 30--34 and 66--69). It cannot verify
that a stored numerator and denominator arose from the claimed state, because
those values are not present.

Consequently, the large-order conclusion still trusts the same implementation
for `Q -> tau -> signing`, matrix construction, numerical vector proposal, and
exact Rayleigh evaluation. The documented full regeneration is valuable, but
it reruns the same implementation and reproduces the same digest; it is not an
independent certificate verifier.

Required resolution: either archive compact per-state proof data sufficient
for a small independent verifier (at minimum state identifier plus an integer
Rayleigh vector, with deterministic chunking), or implement a genuinely
separate decision route that reconstructs every `(Q,alpha)` matrix and verifies
the exact exclusion through `n=30`. Until then, the representative-set risk is
closed but the per-state decision risk is not.

### MAJOR 2: The new evidence is not part of the trusted theorem gate

At review time all new scanner, driver, test, completeness, and trust-map files
were untracked by Git. More importantly, the top-level verifier does not load
or authenticate them. `verify_target_a_minimality_certificate.py` lists trusted
hashes for historical search results and checkpoint manifests (lines 21--36),
then audits those production summaries and replays their checkpoints (lines
154--197 and 225--253). A smallest-counterexample verification can therefore
pass if the new record-level audit is absent, stale, or replaced.

The existing submission manifest and English manuscript also retain the old
boundary: they state that recordwise generator equality stops at `n=24`, with
only aggregate checks at `n=26,28,30`
(`target_a_submission_artifact_manifest.json`, lines 144--147;
`sections/10_computational_verification.tex`, lines 121--129;
`appendices/12_appendix_orbit_completeness.tex`, lines 119--124). This conflicts
with the stronger claim in the new trust map.

Required resolution: commit the new evidence; add the driver, C source,
per-order results, summary, and trust map to the submission artifact manifest;
make the top-level minimality verifier require their hashes and PASS conditions;
and update the manuscript's disclosure in the same atomic revision. The new
audit should fail the publication gate when any required order or detail file
is missing or changed.

### MODERATE 1: Holonomy and the factor-four class multiplicity are asserted, not independently scanned

The C route scans only legal `Q` words. The fields `holonomy_coverage = [-1,1]`,
`canonical_spectral_states = 2 * representatives`, and
`sum_of_represented_switching_classes = 4 * represented_q_vectors` are assigned
by the orchestrating Python code (`target_a_record_set_audit.py`, lines
147--153). They do not arise from the independent scanner. Thus the new audit
does not independently test that both holonomies are emitted once, that the two
`tau` lifts are precisely global-sign partners for even `n`, or that the
dihedral action on `Q` preserves the intended spectral equivalence.

The human cycle-space argument in the manuscript and the earlier raw/quotient
cross-checks materially mitigate this risk. The production stream also loops
over both `alpha` values (`target_a_minimality_search.py`, lines 265--269), and
checkpoint input replay verifies its state count. Nevertheless, the trust map
should distinguish "proved and exercised by the production route" from
"independently checked by the new C route." A small independent expansion test
should be linked explicitly as evidence for this interface.

### MODERATE 2: The independence metadata is too categorical

The two implementations use different languages, traversal orders, and data
structures, which is a real independence gain. They nevertheless share the
same binary representation, parity convention, and rotation/reflection
formulas. Compare the C orbit construction at lines 22--37 and 122--132 with
`target_a_bracelets.py`, lines 15--28 and 78--88. A common mistake in the
specified dihedral action or the `Q` encoding could therefore survive exact
record equality. Moreover, `canonicality_failures == 0` is partly an internal
consistency check: in an ascending full-space scan, the first unvisited member
is minimal under whatever orbit relation that same scanner constructed.

The trust map acknowledges the shared mathematical quotient specification and
Python orchestration (lines 93--97), but `summary.json` states simply that
`canonicalization_shared` is false. Replace this with a more precise statement:
no canonicalization *code or traversal* is shared, while the group action and
state semantics are shared. This is a correlated implementation risk, not a
demonstrated failure.

### MODERATE 3: Recorded-run provenance is incomplete

`summary.json` records the C source hash and compiler, but it does not bind the
hashes of `target_a_record_set_audit.py` or `target_a_bracelets.py`, the Git
commit/tree, the exact command, or the hashes of the four detail JSON files.
`test_target_a_record_set_audit.py` checks that the current C source matches the
recorded hash and then trusts the PASS booleans in the detail files (lines
23--40). This is enough for regression convenience, not for an archival proof
manifest.

Required resolution: include all executable-source hashes, commit/tree,
environment, command, and per-detail file hashes in one authenticated manifest;
have the test recompute cross-file totals and verify every referenced hash.
Timing metadata may remain informational.

### MINOR 1: The public input domain accepts odd orders with the wrong parity convention

The C program and Python driver accept every `1 <= n <= 30`
(`target_a_independent_orbit_scan.c`, lines 64--71;
`target_a_record_set_audit.py`, lines 100--103), but both enumerate even Hamming
weight. With bit `1` meaning `Q_i=+1`, `product_i Q_i=1` requires Hamming weight
congruent to `n` modulo two. The current convention is therefore correct only
for even `n`. A fresh `n=9` run incorrectly returned PASS over the complementary
parity class. This does not affect `n=24,26,28,30`, but the interface should
reject odd `n` or implement the general parity rule and add an odd-order test.

## Positive Technical Checks

- The disk table uses one byte per word with zero as an absence sentinel; all
  valid orbit sizes are in `1..2n <= 60`, so the representation is lossless for
  the supported production orders.
- The C scan visits all `2^n` words, filters the legal even-parity half, directly
  constructs rotations and reflected rotations, marks every orbit member, and
  checks independently computed orbit sizes before destructive consumption.
- Driver-level checks detect missing records, duplicate primary outputs,
  noncanonical extras through count mismatch, orbit-size mismatches, parity
  errors, histogram disagreement, and an incorrect represented-space sum.
- The rational Rayleigh path is exact after vector proposal. With scale `10^9`
  and graph degree four, the `int64` matrix-vector product cannot overflow at
  `n <= 30`; squaring is performed after conversion to Python integers.
- The threshold interval is obtained from a minimal polynomial and exact sign
  tests. No reviewed theorem decision depends on a floating tolerance.
- The archived defect and orbit histograms for all four orders independently
  satisfy representative totals, weighted orbit sums `2^(n-1)`, shell-complement
  symmetry, and the factor-four total `2^(n+1)`.

## Referee Executions

All executions used repository inputs read-only and temporary output directories.

| Check | Result |
|---|---|
| Targeted test suite for record audit, minimality search, checkpoint replay, and minimality verifier | `20 passed, 3 subtests passed` |
| Fresh record-set audit, `n=24` | PASS; 176,906 `Q` representatives; 353,812 spectral-state count |
| Fresh record-set audit, `n=26` | PASS; 649,532 `Q` representatives; 1,299,064 spectral-state count |
| Fresh checkpoint replay, `n=24,26` | PASS; all 12 checks per order |
| Fresh full minimality search, `n=8` | PASS; 36 quotient states, 35 exact Rayleigh exclusions, zero fallbacks |
| C strict-warning compile | PASS; no diagnostics |
| C AddressSanitizer/UndefinedBehaviorSanitizer run, `n=12` | PASS; no sanitizer diagnostics |
| Archived `n=24,26,28,30` histogram recomputation | PASS for all totals and multiplicities |
| Deliberate odd-domain probe, `n=9` | Returned PASS, confirming MINOR 1 |

I did not rerun the full `n=28` or `n=30` record scan, and I did not rerun the
17,929,600-state `n=30` spectral search. The repository records a prior full
same-code regeneration with matching ordered certificate digests; I treat that
as strong reproducibility evidence but not as independent per-state
certification.

## Final Computational Verdict

There is no BLOCKER and no observed evidence that the finite-minimality theorem
is false. The new record-set route credibly closes the former risk that matching
aggregate counts could hide compensating omissions and duplicates at
`n=26,28,30`. It should be retained.

The computational package is not yet ready to advertise a fully independent
verification of the smallest-counterexample theorem. Before publication, the
authors should (1) integrate the new record evidence into the authenticated
top-level gate and manuscript, and (2) separate the large search from a small
independent verifier for the per-state exact exclusions, or explicitly retain
that decision layer as a disclosed correlated implementation trust boundary.
