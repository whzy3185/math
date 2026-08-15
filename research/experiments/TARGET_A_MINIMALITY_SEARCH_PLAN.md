# Target A Minimality Search Plan

Date: 2026-08-15

Status: **DESIGN ONLY**.  No spectral search at `n=24,26,28,30` has been
started by this task.

## Goal and stopping condition

Search every switching class of `C_n(1,2)` for exactly

`n in {24,26,28,30}`

through a proved quotient representation.  If all four searches complete
with exact exclusions and no counterexample, then the already verified
`n=32` witness establishes computational minimality over even `n>=8`.

Random sampling is not part of this plan.  Floating eigenvalues may propose
certificates and order near-minimizers, but may not decide the final result.

## Why `(Q,alpha)` covers the spectral search space

There are `2^(n+1)` switching classes because `C_n(1,2)` is connected and
has cycle rank `2n-n+1=n+1`.  The `n` triangle fluxes `tau_i` together with
the step-1 Hamilton-cycle holonomy `alpha` are coordinates on this cycle
space.

Put `Q_i=tau_i*tau_(i+1)`.  Necessarily `product_i Q_i=1`, so Q has an even
number of `+1` entries and there are `2^(n-1)` possible Q-vectors.  Given Q,
there are exactly two triangle-flux lifts, distinguished by `tau_0`.  Global
edge negation exchanges those lifts: it flips every odd-cycle flux `tau_i`,
leaves `alpha` unchanged because `n` is even, sends `A` to `-A`, and hence
preserves spectral radius.  Thus the pre-dihedral spectral state space has

`2^(n-1) * 2 = 2^n`

states `(Q,alpha)`.

Rotations and reflections of the vertex cycle are graph automorphisms.  They
act dihedrally on Q, preserve `alpha`, and conjugate signed adjacency matrices
up to switching.  One binary-bracelet representative of every even-parity Q
orbit, paired with each `alpha=±1`, therefore covers every spectral radius.

## Exact quotient counts

Let `g=gcd(n,k)` for rotation by `k`, and let `ell=n/g` be its cycle length.
The number of even-weight binary strings fixed by that rotation is

```text
F(n,k) = 2^g       if ell is even,
         2^(g-1)   if ell is odd.
```

For even `n`, each of the `n` reflections fixes exactly `2^(n/2)`
even-weight strings.  Burnside's lemma therefore gives the number of
even-weight Q-bracelets

```text
B_even(n) = (sum_(k=0)^(n-1) F(n,k) + n*2^(n/2)) / (2n).
```

The final quotient-state count is `2*B_even(n)` because `alpha` is retained.

| n | raw switching classes `2^(n+1)` | spectral states `2^n` | Q-bracelets | quotient states with alpha |
|---:|---:|---:|---:|---:|
| 24 | 33,554,432 | 16,777,216 | 176,906 | 353,812 |
| 26 | 134,217,728 | 67,108,864 | 649,532 | 1,299,064 |
| 28 | 536,870,912 | 268,435,456 | 2,405,236 | 4,810,472 |
| 30 | 2,147,483,648 | 1,073,741,824 | 8,964,800 | 17,929,600 |

These counts must be asserted by the generator before any matrix is built.

## Defect-shell counts

The following are Q-bracelet counts before multiplying by the two alpha
values.  They are independent Burnside targets for shell checkpoints.

```text
n=24: d=0:1, 2:12, 4:256, 6:2920, 8:15581, 10:41272,
      12:56822, 14:41272, 16:15581, 18:2920, 20:256, 22:12, 24:1

n=26: d=0:1, 2:13, 4:328, 6:4576, 8:30415, 10:102817,
      12:186616, 14:186616, 16:102817, 18:30415, 20:4576,
      22:328, 24:13, 26:1

n=28: d=0:1, 2:14, 4:413, 6:6916, 8:56021, 10:235378,
      12:544802, 14:718146, 16:544802, 18:235378, 20:56021,
      22:6916, 24:413, 26:14, 28:1

n=30: d=0:1, 2:15, 4:511, 6:10133, 8:98254, 10:502303,
      12:1444147, 14:2427036, 16:2427036, 18:1444147,
      20:502303, 22:98254, 24:10133, 26:511, 28:15, 30:1
```

For weight `d`, these numbers can also be independently recomputed by
fixed-weight Burnside counts.  A rotation contributes
`binomial(g,d/ell)` when `ell` divides `d`.  The two reflection types are
counted separately by their fixed points and transpositions.

## Generator design

The existing ascending scanner marks a `bytearray(2^n)`.  It is suitable for
the completed `n=20,22` audits and is tolerable at `n=24,26`, but would use
256 MiB at `n=28` and 1 GiB at `n=30` before matrix work.  It must not be the
production `n=28,30` generator.

The production generator will:

1. generate binary necklaces in deterministic lexicographic order with a
   constant-memory Fredricksen-Kessler-Maiorana style recursion;
2. retain only even weight;
3. apply one reflection test to retain the bracelet representative;
4. emit shells in increasing `d`, then canonical Q-code, then `alpha=-1,+1`;
5. assert total and per-shell Burnside counts;
6. never materialize the full Q-vector space or a `2^n` visited array.

Before use at a new `n`, the direct bracelet stream must match the old
visited-orbit generator at every even `n<=22` and match Burnside totals at
`n=24,26,28,30` without performing spectral work.

## Spectral and exact-decision pipeline

For each representative:

1. reconstruct `tau` with `tau_0=+1` and construct the tree-gauge signing;
2. build the integer signed adjacency matrix once;
3. run one dense symmetric eigendecomposition to obtain both the numeric
   radius and an extremal eigenvector;
4. integerize that eigenvector and compute the exact rational Rayleigh
   quotient `||Av||^2/||v||^2`;
5. compare it with a certified rational upper endpoint for `rho_-(n)^2`;
6. if the quotient is at least that endpoint, record an exact exclusion;
7. otherwise invoke the independent exact Sylvester verifier and save its
   full result;
8. stop immediately and freeze a candidate if an exact counterexample is
   found.

The optimizer state `d=0, alpha=-1` is checked by the exact minimal-polynomial
divisibility/root-isolation route.  Floating comparison never decides PASS.

For the reported second minimum, retain a numeric top queue during the scan,
then exactly compare the small final candidate set by characteristic
polynomials and root isolation.  At `n=30`, preserve the top 100
non-optimizer states with Q, tau, alpha, orbit size, rational certificate,
and numeric gap.

## Checkpoint and resume format

Checkpoints are immutable chunks within one defect shell.  A manifest stores:

```text
schema_version
git_commit
n
defect_count
expected_q_orbits
expected_spectral_states
chunk_index
first_canonical_q
last_canonical_q
completed_states
rayleigh_certified
exact_fallbacks
counterexamples
top_state_summary
ordered_input_sha256
ordered_certificate_sha256
previous_chain_sha256
chain_sha256
```

The chain digest is computed from the previous chain digest, the current
ordered-input digest, and the current ordered-certificate digest.  Files are
written to a temporary path and atomically renamed.  Resume verifies:

1. schema and git commit;
2. expected Burnside shell count;
3. chunk file SHA-256;
4. hash-chain continuity;
5. regeneration of the first and last canonical representatives;
6. monotonic cursor order.

The final manifest is valid only when completed states equal exactly twice
the expected Q-bracelet count in every shell.  A final log records the digest
of the complete ordered checkpoint manifest.

## Storage estimates

The search streams representatives; a full queue is optional.  The bitset
column shows the size of one completion bit per quotient state.  Compact
columns show hypothetical 16-byte and 32-byte records and are upper planning
bounds, not required checkpoint sizes.

| n | completion bitset | 16-byte/state | 32-byte/state | planned persistent checkpoint budget |
|---:|---:|---:|---:|---:|
| 24 | 43.2 KiB | 5.4 MiB | 10.8 MiB | < 10 MiB |
| 26 | 158.6 KiB | 19.8 MiB | 39.6 MiB | < 25 MiB |
| 28 | 587.2 KiB | 73.4 MiB | 146.8 MiB | < 75 MiB |
| 30 | 2.14 MiB | 273.6 MiB | 547.2 MiB | < 250 MiB, including top-100 data |

The certificate hash chain avoids storing millions of large rational vectors
while keeping the complete deterministic computation reproducible.  Any
exact fallback is stored in full.

## Complexity and runtime budget

If `S_n=2*B_even(n)`, direct bracelet generation costs `O(S_n*n)` bit work.
Each state uses one `O(n^3)` dense eigendecomposition to propose a certificate
and `O(n^2)` exact integer work to verify the Rayleigh quotient.  The dominant
planned cost is therefore `O(S_n*n^3)`, plus rare exact fallbacks.

Observed `n=20,22` throughput is roughly 20,000 spectral states/second on the
frozen machine, but larger matrices, direct-generation overhead, checkpoint
hashing, and top-state bookkeeping require conservative budgets:

| n | quotient states | conservative wall-clock budget |
|---:|---:|---:|
| 24 | 353,812 | 1-3 minutes |
| 26 | 1,299,064 | 3-10 minutes |
| 28 | 4,810,472 | 15-45 minutes |
| 30 | 17,929,600 | 1-3 hours |

These are planning estimates, not completion claims.  Actual elapsed time,
CPU information, peak RSS, certificate counts, and checkpoint hashes must be
recorded in each result.

## Required result fields

Every final `target_a_search_nN.json` must include:

- expected and completed Q-orbits and spectral states;
- represented raw switching classes;
- completion fraction, exactly `1` before PASS;
- optimizer representative and represented optimizer-class count;
- global minimum and exact equality evidence;
- second minimum, gap, and near-minimizer data;
- rational Rayleigh certificate count and aggregate digest;
- exact fallback count and full fallback records;
- counterexample records;
- per-shell and final checkpoint hashes;
- elapsed time, environment, git commit, and command;
- status using `VERIFIED_NO_COUNTEREXAMPLE` only at 100% completion.

## Authorization gate

Task 33 (`n=24`) may start only after
`research/audit/QUOTIENT_COMPLETENESS_AUDIT.md` records `PASS`.  This plan
does not authorize Task 33 by itself.
