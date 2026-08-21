# Target A Finite-Minimality Trust Map

Date: 2026-08-21

Status: **LARGE-ORDER RECORD-LEVEL ENUMERATION PASS; INDEPENDENT SPECTRAL DECISION PASS; COMPUTATIONAL CORE RE-REVIEW PASS**

## Coordinate and Decision Model

A switching class is first represented in Hamilton gauge by the triangle-flux
word `tau` and the step-one Hamilton holonomy `alpha`. Global edge-sign
negation identifies the two lifts of

```text
Q_i = tau_i tau_(i+1),   product_i Q_i = 1.
```

The finite spectral quotient is therefore `(Q,alpha)/D_n`: `Q` is an
even-parity binary word modulo the dihedral action and `alpha` is retained as
each of `-1,+1`. A `Q` orbit of size `s` represents `4s` switching classes:
two holonomies and two global-sign lifts.

Every nonoptimizer decision is an exact rational Rayleigh inequality against
a certified algebraic upper bound for the distinguished threshold. The unique
quotient optimizer is checked by exact characteristic-polynomial divisibility
and root isolation. Floating eigensolvers only propose integer vectors.

## Order-by-Order Map

| `n` | switching classes | canonical spectral states | primary enumeration | independent enumeration/check | record-level equality | aggregate checks | exact decision | residual trust boundary |
|---:|---:|---:|:---|:---|:---:|:---|:---|:---|
| 8 | 512 | 36 quotient states; raw run uses 512 classes | raw tree-gauge class scan | FKM and visited-orbit streams agree on all 18 `Q` records | PASS | Burnside shells; orbit sum | 510 rational Rayleigh certificates; two exact optimizer lifts | Historical raw proof objects are summarized, not archived one per class. |
| 10 | 2,048 | 88 quotient states; raw run uses 2,048 classes | raw tree-gauge class scan | FKM and visited-orbit streams agree on all 44 `Q` records | PASS | Burnside shells; orbit sum | 2,046 rational Rayleigh certificates; two exact optimizer lifts | Same historical-artifact boundary. |
| 12 | 8,192 | 244 quotient states; raw run uses 8,192 classes | raw tree-gauge class scan | FKM and visited-orbit streams agree on all 122 `Q` records | PASS | Burnside shells; orbit sum | 8,190 rational Rayleigh certificates; two exact optimizer lifts | Same historical-artifact boundary. |
| 14 | 32,768 | 724 quotient states; raw run uses 32,768 classes | raw tree-gauge class scan | FKM and visited-orbit streams agree on all 362 `Q` records | PASS | Burnside shells; orbit sum | 32,766 rational Rayleigh certificates; two exact optimizer lifts | Same historical-artifact boundary. |
| 16 | 131,072 | 2,324 quotient states; raw run uses 131,072 classes | raw tree-gauge class scan | FKM and visited-orbit streams agree on all 1,162 `Q` records | PASS | Burnside shells; orbit sum | 131,070 rational Rayleigh certificates; two exact optimizer lifts | Same historical-artifact boundary. |
| 18 | 524,288 | 7,828 quotient states; raw run uses 524,288 classes | raw tree-gauge class scan | FKM and visited-orbit streams agree on all 3,914 `Q` records | PASS | Burnside shells; orbit sum | 524,286 rational Rayleigh certificates; two exact optimizer lifts | Same historical-artifact boundary. |
| 20 | 2,097,152 | 27,296 | raw tree-gauge class scan | complete raw-versus-quotient comparison plus FKM/visited record equality | PASS | 2,097,152 represented classes; Burnside count | 2,097,150 rational Rayleigh certificates; two exact optimizer lifts | Independent quotient comparison shares the mathematical coordinate specification, necessarily. |
| 22 | 8,388,608 | 97,468 | visited full-code orbit generator | FKM record stream agrees on all 48,734 `Q` records; adversarial orbit/switching expansion | PASS | Burnside shells; orbit-size sum; both holonomies | 97,467 rational Rayleigh certificates; exact quotient optimizer | Stored result is aggregate; full exact decisions are deterministically regenerable. |
| 24 | 33,554,432 | 353,812 | FKM fixed-weight necklace generator | C full integer-space scan; earlier Python visited-set route retained as a third comparison | PASS: 176,906 `Q` records | defect and orbit histograms; 8,388,608 legal `Q`; both holonomies; checkpoint replay | Production: 353,811 exact Rayleigh exclusions and exact optimizer. Independent route: standalone matrix reconstruction and the same full exact decision count. | Per-state vectors are regenerated rather than archived; two separate decision runs bind ordered certificate digests. |
| 26 | 134,217,728 | 1,299,064 | FKM fixed-weight necklace generator | C full integer-space scan with direct dihedral orbit construction | PASS: 649,532 `Q` records | defect and orbit histograms; 33,554,432 legal `Q`; both holonomies; checkpoint replay | Production: 1,299,063 exact Rayleigh exclusions and exact optimizer. Independent route: standalone matrix reconstruction and the same full exact decision count. | Same regeneration boundary; neither enumeration nor spectral decisions rely only on aggregate agreement. |
| 28 | 536,870,912 | 4,810,472 | FKM fixed-weight necklace generator | C full integer-space scan with direct dihedral orbit construction | PASS: 2,405,236 `Q` records | defect and orbit histograms; 134,217,728 legal `Q`; both holonomies; checkpoint replay | Production: 4,810,471 exact Rayleigh exclusions and exact optimizer. Independent route: standalone matrix reconstruction and the same full exact decision count. | Same regeneration boundary; neither enumeration nor spectral decisions rely only on aggregate agreement. |
| 30 | 2,147,483,648 | 17,929,600 | FKM fixed-weight necklace generator | C full integer-space scan with direct dihedral orbit construction | PASS: 8,964,800 `Q` records | defect and orbit histograms; 536,870,912 legal `Q`; both holonomies; checkpoint replay | Production: 17,929,599 exact Rayleigh exclusions and exact optimizer. Independent route: standalone matrix reconstruction and the same full exact decision count. | Same regeneration boundary; neither enumeration nor spectral decisions rely only on aggregate agreement. |

## Independence of the Large-Order Route

The new checker in `target_a_independent_orbit_scan.c` shares no code with the
FKM generator. It uses a different implementation language, scans integer
words instead of necklace leaves, constructs complete orbits instead of
filtering reflections, uses a visited bitmap instead of a recursion stack, and
does not decompose the traversal into defect shells.

The Python driver places every FKM record in a disk-mapped table indexed by
its claimed canonical word. The C scanner visits every integer in
`[0,2^n-1]`, independently identifies the least member and size of each legal
dihedral orbit, and destructively consumes the corresponding table entry. A
PASS requires all of the following:

1. every even-parity word is traversed;
2. every independently found canonical word occurs in the FKM set;
3. its independently computed orbit size equals the stored size;
4. every FKM record is consumed exactly once;
5. the defect and orbit-size histograms agree;
6. the orbit-size sum is exactly `2^(n-1)`;
7. adjoining both holonomies and both global-sign lifts gives `2^(n+1)`
   switching classes.

The comparison is ordering-independent and exact. SHA-256 stream digests are
retained for provenance only; they do not decide set equality.

## Independent Large-Order Spectral Decisions

The representative-set audit is followed by a second decision program,
`target_a_independent_spectral_audit.py`. Its input records are emitted by the
C full-space scanner, not by the production traversal. For every canonical
record it independently constructs the two Hamilton-gauge adjacency matrices.
It imports none of the production signing, matrix, threshold, or Rayleigh
certificate functions.

A floating eigensolver proposes an integer vector, but acceptance uses only the
exact rational quotient `||Av||^2/||v||^2` and a certified algebraic upper
endpoint for the distinguished threshold. The unique optimizer is checked by
exact characteristic-polynomial divisibility. The stored result contains the
state count, zero-uncertified check, source hashes, independent decision digest,
and detail-file hash for every order.

## Machine-Readable Evidence

The complete summaries are in
`research/reproducibility/target_a_large_order_completeness/`:

| `n` | legal `Q` words | canonical `Q` representatives | record equality | elapsed |
|---:|---:|---:|:---:|---:|
| 24 | 8,388,608 | 176,906 | PASS | 2.33 s |
| 26 | 33,554,432 | 649,532 | PASS | 7.51 s |
| 28 | 134,217,728 | 2,405,236 | PASS | 29.77 s |
| 30 | 536,870,912 | 8,964,800 | PASS | 126.40 s |

The timings are environmental observations, not mathematical evidence.

The authenticated computational-evidence manifest also binds its verifier,
the verifier regression test, and the manifest builder.  The top-level
minimality checker pins the resulting manifest digest before executing the
verifier, so the strengthened theorem gate fails if either evidence or
verification code is altered.

## Remaining Trust Boundary

The new routes close the previously disclosed representative-set risk at
`n=26,28,30`: compensating omissions and duplications can no longer hide
behind matching Burnside totals. They also separate the large-order spectral
decision from the production implementation by reconstructing and exactly
excluding every nonoptimizer a second time. They do not turn the compact
checkpoint files into an archive of every integer Rayleigh vector. Those
vectors are regenerated by both decision programs, while separate digests and
the production checkpoints bind their order and counts.

The two enumeration implementations necessarily share the proved
mathematical quotient specification `(Q,alpha)/D_n`. The orchestrating Python
program also prepares the temporary comparison table, although the C scanner
decides canonicality and orbit size independently. These residual interfaces
are disclosed; they are not numerical tolerances or missing orbit checks.
