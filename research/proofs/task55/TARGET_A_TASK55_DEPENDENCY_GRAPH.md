# Target A Task 55 Dependency Graph

## Scope And Evidence Convention

This file records logical dependencies, not merely thematic relationships.
An arrow `X -> Y` means that the accepted proof of `Y` uses `X`.  A dashed
statement of relevance is written separately and is not a proof edge.

The evidence labels used below have the following meanings.

| Label | Meaning |
|---|---|
| `PROVED` | A finite symbolic calculation or analytic deduction whose stated inputs are explicit.  If an input is computer-assisted, the conclusion remains conditional on that accepted input. |
| `COMPUTER_ASSISTED_PROVED` | A complete exact or outward-interval producer artifact is paired with an implementation-independent, fail-closed checker. |
| `EXACT_FINITE_READ_ONLY` | Exact arithmetic was reported for a finite computation, but a serialized producer artifact and independent reconstruction are absent.  It is evidence, not an integrated theorem. |
| `HIGH_PRECISION_DISCOVERY` | Arbitrary-precision numerical output used to locate structure.  It is not an exact or interval certificate. |
| `FALSIFIED_AS_STATED` | A stated claim has a proved counter-obstruction and must not be used as a dependency. |
| `OPEN` | A required implication or uniform theorem has not been proved. |

The strongest global finite-order conclusion in this graph is

```text
For even n>=8, the conjecture fails exactly at
n=32, n=40, and every even n>=48.
```

This classification is independent of the exact-`2r` asymptotic cluster
theorem.  Conversely, the exact-`2r` theorem supplies a sharper structural
description for separated G6 interfaces but does not improve the already
proved contiguous threshold `N_star=48`.

## Node Ledger

| ID | Statement | Evidence | Exact scope / boundary |
|---|---|---|---|
| `G6-ROOT` | The positive unsquared G6 Evans root `+sqrt(c6)` is unique in its certified interval and simple. | `COMPUTER_ASSISTED_PROVED` | Task 50 single-interface certificate; this alone says nothing about the negative root. |
| `G6-K` | `Q_(6-i)=Q_i`, `tau_(7-i)=-tau_i`, and `(Ku)_i=(-1)^i u_(9-i)` give `K^2=-I`, `KA=-AK`, and `KH=HK`. | `PROVED` with exact finite controls | The `Q` identity is closed by the period-four tail representatives and core sites; the `tau` identity follows from the anchor and induction in both directions.  The finite windows are checks, not substitutes for the all-integer proof. |
| `G6-RANK2` | `rank P_(H6,{c6})=2`. | `COMPUTER_ASSISTED_PROVED` | Uses `G6-ROOT` and `G6-K`: the simple positive and negative `A` roots are distinct and square to the same `H=A^2` level. |
| `G6-EDGE` | `sup sigma(H6)=c6`. | `COMPUTER_ASSISTED_PROVED` | Uses the positive physical root, complete exact candidate exclusion above it, `||A6||<=4`, and `G6-K` for the negative-spectrum bridge. |
| `G6-GAP` | On the orthogonal complement of the full rank-two `c6` eigenspace, `H6<=c6-1/100`. | `COMPUTER_ASSISTED_PROVED` | Both G6 orientations; the projection removed here has rank two, not one. |
| `OLD-r` | Exactly `r` squared levels, a codimension-`r` complement, and a problem-specific `r x r` G6 Feshbach matrix. | `FALSIFIED_AS_STATED` | Contradicted already at one interface by `G6-RANK2`.  Task 54 cutoff arithmetic survives, but the old spectral conclusion does not. |
| `FLOQUET` | All eight period-eight cuts have two stable multipliers of modulus `<q=9/25`, with selected two-column basis condition number `<17`. | `COMPUTER_ASSISTED_PROVED` | Exact rational interval arithmetic reconstructed independently in the Task 55 exact-`2r` checker. |
| `2R-COUNT` | For `r in {1,2,3}` and minimum cyclic interface distance `D>=1040`, the fixed window `[c6-1/400,c6+1/400]` has Riesz rank exactly `2r`. | `COMPUTER_ASSISTED_PROVED` | Both orientations and both holonomies; multiplicity is counted.  Individual finite-ring levels need not be simple. |
| `2R-FESHBACH` | The cluster has a valid `2r x 2r` Gram-orthonormalized Feshbach reduction and every cluster level obeys `|lambda_j-c6|<3505 r(9/25)^ell`. | `COMPUTER_ASSISTED_PROVED` | `ell=floor((floor(D/4)-12)/8)`.  This is a norm bound, not an entrywise asymptotic expansion. |
| `N-EXP` | The exponential separated-interface construction covers every even `n>=3120`. | `COMPUTER_ASSISTED_PROVED` | `N_exp=3120` is sufficient, not minimal; it is weaker than `N_star=48`. |
| `N-STAR` | Explicit exact-LDL witnesses cover `48<=n<240`, and the global IMS argument covers every even `n>=240`; hence every even `n>=48` fails. | `COMPUTER_ASSISTED_PROVED` | Inherited Task 54 theorem.  It uses only the local cap `sup sigma(H6)=c6`, not the multiplicity at `c6`, so `G6-RANK2` does not invalidate it. |
| `LOW-32` | The conjecture holds for every even `8<=n<=30` and first fails at `n=32`. | `COMPUTER_ASSISTED_PROVED` | Inherited complete small-order classification and explicit exact `n=32` certificate. |
| `N40` | The displayed order-40 signing satisfies `rho(A)^2<15541/2000<63/8`. | `COMPUTER_ASSISTED_PROVED` | Exact rational LDL; the older bounded-search artifact remains the valid source of this positive certificate. |
| `SMALL-6` | No counterexample exists for `n=34,36,38,42,44,46`. | `COMPUTER_ASSISTED_PROVED` | Complete local-window partition, parity-lifted de Bruijn closure, both holonomies, and exact terminal checks; `terminal_unresolved=0`. |
| `ALL-EVEN` | Failure occurs exactly at `n=32`, `n=40`, and every even `n>=48`. | `COMPUTER_ASSISTED_PROVED` | Composite of `LOW-32`, `N40`, `SMALL-6`, and `N-STAR`; no asymptotic cluster theorem is needed. |
| `C6-ALG` | The degree-ten G6 Evans polynomial has exactly one root `c6` in the stored rational interval. | `COMPUTER_ASSISTED_PROVED` | Task 51 Sturm/physical-root certificate; supplies the strict rational upper endpoint used by finite Rayleigh witnesses. |
| `MG-18` | All 31,008 reflection-canonical primitive multi-gap cores with support sum in `{2,6,10,14,18}` have `sup sigma(A_g^2)>c6`. | `COMPUTER_ASSISTED_PROVED` | Complete only for the stated bounded class.  Exact acceptance evaluates the full outgoing `A_g v`, not a compressed square matrix. |
| `MG-33` | Every finite core containing consecutive gaps `(3,3)` has `sup sigma(A^2)>=419/53>c6`. | `PROVED` from the certified `c6` upper endpoint | Arbitrary total core length; 32 exact local dependency cases and both `tau` lifts.  It does not cover motif-free cores. |
| `B0-B2` | Every finite-core `B0 -> B2` interface has squared spectral top at least `c6`. | `OPEN` | `MG-18` and `MG-33` prove strict subclasses only.  No reference-cell deletion or terminating replacement theorem is available. |
| `SG-INV` | `e_6(lambda,P)=P^3 e_2(-lambda,P^-1)` in the reciprocal bulk quotient. | `COMPUTER_ASSISTED_PROVED` | Exact unsquared quotient identity.  `P -> P^-1` exchanges stable and unstable sheets. |
| `SG-REC` | Fixed-residue exterior-square observables satisfy the exact order-five recurrence determined by `(t-1)Q_4(t)`. | `COMPUTER_ASSISTED_PROVED` | The generic minimal polynomial has degree five.  At `c6`, the relevant modes form complex reciprocal pairs of equal modulus. |
| `SG-PHYS` | Every physical single-gap interface has spectral top at least `c6`. | `OPEN` | Neither `SG-INV` nor `SG-REC` selects the physical stable sheet or proves eventual sign/root ordering. |
| `REF-COST` | On the fixed 420-state/656-edge lifted grammar, calibrated `F4` and `F5` have no negative cycle and only the reference zero-cycle orbit. | `EXACT_FINITE_READ_ONLY` | No serialized edge table, potential, digest-bound producer, or independent checker; no spectral bridge. |
| `REF-RIGID` | Every nonreference closed walk in that fixed graph has positive calibrated cost. | `EXACT_FINITE_READ_ONLY` | Exact deduction from the reported cycle classification, but it inherits the read-only status and remains purely combinatorial. |
| `PER-24` | The unique primitive legal periodic phase below `c6` is the period-eight target for `p<=24`, modulo certified equivalences. | `COMPUTER_ASSISTED_PROVED` | Integrated Task 53 frontier only. |
| `PER-26` | At `p=25,26`, 58 and 95 post-filter survivors respectively all have exact Rayleigh witnesses above `c6`. | `EXACT_FINITE_READ_ONLY` | Reported complete counts are 337,594 and 649,532 canonical orbits, but no Task 55 serialized closure/checker exists.  The integrated frontier therefore remains `p<=24`. |
| `LIMINF-G6` | Any sequence retaining a rooted G6 interface with pure period-eight radius tending to infinity has `liminf rho(A_j)^2>=c6`. | `PROVED` from `G6-EDGE` | Restricted dilute-G6 theorem; no exact-`2r` count is used. |
| `LIMSUP` | For residues `2,4,6`, the explicit separated-G6 constructions give `limsup m_(8k+r)^2<=c6`. | `PROVED` | Uses legal residue constructions and global finite-range localization; exact-`2r` only sharpens their convergence rate. |
| `LIMINF-ALL` | For residues `2,4,6`, every minimizing sequence satisfies `liminf m_(8k+r)^2>=c6`. | `OPEN` | Tight non-G6 cores, dichotomy, normalized vanishing, and aperiodic limits remain uncontrolled. |
| `COMMON-LIMIT` | All three nonzero-residue limits exist and equal `c6`. | `OPEN` | Would follow immediately from `LIMSUP + LIMINF-ALL`; the missing dependency is `LIMINF-ALL`. |
| `INTERACT` | Universal leading interaction coefficients, physical finite-ring simplicity, pairwise leading structure, and a genuine three-body coefficient. | `OPEN` | The exact `2r` reduction controls norms only.  Representative 80/120/160-digit roots are `HIGH_PRECISION_DISCOVERY`, not coefficient or simplicity certificates. |

## G6 And Exact-2r Proof Graph

```text
Task 50 simple positive G6 root [G6-ROOT]
        +
all-integer reflection/tau identity and K algebra [G6-K]
        v
rank P_(H6,{c6})=2 [G6-RANK2]
        +
complete physical candidate exclusion and ||A6||<=4
        v
sup sigma(H6)=c6 [G6-EDGE]
        +
single-interface physical isolation
        v
rank-two complement gap delta6=1/100 [G6-GAP]

[G6-RANK2] + [G6-EDGE] + [G6-GAP] + [FLOQUET]
        +
two-mode cutoff columns, exact Gram control,
range-four IMS error, and codimension-2r min-max
        v
exact 2r fixed-window count [2R-COUNT]
        +
Gram-coordinate Schur complement and resolvent bound 400
        v
2r Feshbach reduction and 3505 r q^ell bound [2R-FESHBACH]
        +
residue-specific distance formulas and exact trigonometric lower bounds
        v
continuous sufficient exponential onset N_exp=3120 [N-EXP]
```

The lower count in `2R-COUNT` comes from a `2r`-dimensional residual
subspace.  The upper count comes from a codimension-`2r` complement cap.  Both
halves are necessary; localized quasimodes alone give neither exact count nor
a Feshbach coordinate dimension.

The following is a forbidden path:

```text
one positive mode per interface
        -/-> codimension-r complement
        -/-> exact-r squared cluster
        -/-> r x r physical Feshbach matrix.
```

`G6-RANK2` proves that every arrow in this old chain fails at its first
spectral step.  The corrected `2r` chain above replaces it.

## Finite-Order Classification Graph

The inherited contiguous tail has two independent branches:

```text
Task 53 exact discrete IMS identity and local patch classification
        +
[G6-EDGE] and the period-eight bulk cap
        +
Task 54 exact tent translation sums and residue separation geometry
        v
global IMS cap for every even n>=240

deterministic structured signing for each even 48<=n<240
        +
exact positive-definiteness certificates for tI-A_n^2
        +
independent natural-order rational LDL reconstruction
        v
finite exact bridge for every even 48<=n<240

global IMS tail + finite exact bridge
        v
contiguous explicit-witness threshold N_star=48 [N-STAR].
```

Neither branch removes a one-dimensional approximation to the `c6`
eigenspace.  The first uses the local quadratic-form cap, and the second
checks finite matrices directly.  This is the precise reason the G6 rank
correction leaves `N-STAR` intact.

Combining that tail with the exact low orders gives:

```text
complete even orders 8,...,30 and exact n=32 failure [LOW-32]
        +
exact order-40 LDL counterexample [N40]
        +
exact nonexistence at 34,36,38,42,44,46 [SMALL-6]
        +
exact LDL bridge 48<=n<240 and IMS tail n>=240 [N-STAR]
        v
failure exactly at n=32, n=40, and every even n>=48 [ALL-EVEN]
```

The legacy orders-34--46 bounded searches are not negative-proof inputs.
They preserve discovery provenance and the valid `N40` certificate.  The six
nonexistence statements come only from `SMALL-6`, whose independent checker
reconstructs all local windows, overlap walks, canonical terminal classes,
and both holonomy sectors.

`N-EXP` is a separate corollary of the exact-`2r` chain.  It is not an input
to `ALL-EVEN`, since `N-STAR` already starts at 48 and is independently
proved.

## Interface Classification And Lower-Bound Graph

```text
Task 51 exact c6 polynomial and rational isolating interval [C6-ALG]
        +
complete recursive enumeration of the stated bounded primitive class
        +
exact full-image integer Rayleigh witnesses
        v
31,008 support-sum<=18 multi-gap cores lie strictly above c6 [MG-18]

[C6-ALG]
        +
three explicit local vectors, 32 dependency cases, opposite-lift conjugacy
        v
arbitrary-length cores containing (3,3) lie strictly above c6 [MG-33]

[MG-18] + [MG-33]
        -/-> universal finite-core B0->B2 theorem [B0-B2 OPEN].
```

The missing last arrow requires control of primitive support sums above 18
that avoid `(3,3)`.  Insertion or deletion of a period-eight reference cell
cannot supply that control: it multiplies matching data by a non-scalar bulk
monodromy and is not a spectral equivalence.

The single-gap algebra is a separate exact branch:

```text
exact transfer convention and reciprocal bulk quartic
        v
gap-2/gap-6 quotient involution [SG-INV]
        +
two exterior-square matrix classes and degree-five minimal polynomial
        v
order-five scalar recurrence [SG-REC]
        -/-> physical all-single-gap lower theorem [SG-PHYS OPEN].
```

The reciprocal involution sends the stable sheet to the unstable sheet, and
the recurrence has no one-mode Perron/sign mechanism at `c6`.  These are
specific mathematical obstructions, not merely missing computation time.

## Periodic, Reference-Cost, And Limit Graph

```text
integrated exact frontier through p<=24 [PER-24]

read-only exact p=25,26 enumeration [PER-26]
        -/-> extension of the integrated frontier to p<=26
        -/-> any aperiodic classification.

read-only calibrated finite graph cycle result [REF-COST]
        v
finite-grammar zero-cycle rigidity [REF-RIGID]
        -/-> local Rayleigh witness or operator lower bound
        -/-> vanishing control
        -/-> unrestricted liminf.
```

The accepted asymptotic implications are exactly:

```text
pointed compactness + finite-support form transfer + [G6-EDGE]
        v
restricted dilute-G6 lower bound [LIMINF-G6]

explicit legal residue constructions + global localization cap
        v
nonzero-residue upper bounds [LIMSUP]

[LIMSUP] + unrestricted lower bound [LIMINF-ALL OPEN]
        v
common nonzero-residue limit c6 [COMMON-LIMIT OPEN].
```

The four missing lower-bound branches must remain visible:

| Blocker | Needed dependency | Why current Task 55 evidence does not close it |
|---|---|---|
| Tight cluster | Universal finite-core `B0 -> B2` lower theorem | `MG-18` is support-bounded and `MG-33` is motif-restricted. |
| Dichotomy | Componentwise lower theorem plus controlled recombination | Components need not be G6 and no general interaction monotonicity is proved. |
| Normalized vanishing | Coercive spectral excursion lemma stable under long reference runs | `REF-COST` has no spectral bridge and cost can be diluted. |
| Aperiodic limit | A structural or operator lower theorem beyond finite periodic frontiers | `PER-24` is bounded and `PER-26` is read-only; neither controls aperiodic words. |

## Exact-2r Interaction Boundary

The accepted Feshbach output is

```text
H_eff(z)=c6 I_(2r)+T1+R2(z),
||T1||<=3504 r q^ell,
||R2(z)||<=400 r 3504^2 q^(2ell)<r q^ell.
```

It supports `2R-COUNT` and the common cluster radius, but no current node
proves an entrywise leading coefficient.  Consequently there is no valid
arrow from `2R-FESHBACH` alone to any of the following:

| Proposed conclusion | Missing dependency |
|---|---|
| Individual finite-ring cluster levels are simple | Certified root derivative or a leading static matrix with a gap larger than the remainder. |
| A universal orientation/holonomy sign law | Exact interval enclosure of the relevant normalized entries. |
| The three-interface leading matrix is pairwise additive | Consistent subtraction of one- and two-interface contributions with a smaller certified remainder. |
| A genuine three-body interaction is nonzero | A gauge-invariant three-body definition and a nonzero interval excluding all pairwise cycle-product effects. |

The representative high-precision Evans calculations may suggest these
lemmas, but they are not proof dependencies for any accepted theorem above.

## Bound Artifact Map

The following hashes were independently recomputed from the working-tree
artifacts while preparing this graph.

| Consumer | Bound input / certificate | SHA-256 | Role |
|---|---|---|---|
| `2R-COUNT`, `2R-FESHBACH` | `research/proofs/task50/certificates/g6_interface_certificate.json` | `134d5d29ab8aaae5141cc70493a6f0c1955afeda36bc15789076b0a9a8ae49ea` | simple positive G6 root |
| `2R-COUNT`, `2R-FESHBACH` | `research/proofs/task53/certificates/g6_global_edge.json` | `299b5a17e8bbb13aaf183798883c52287c01bf3c5c8090aa80bf15ab005b621f` | global edge and rank-two symmetry bridge |
| `2R-COUNT`, `2R-FESHBACH` | `research/proofs/task54/certificates/g6_spectral_isolation.json` | `2c4158bfc890979f2c3eb355db61c803d887d4a6fa8903cf4529756d02bbc29f` | rank-two complement isolation `1/100` |
| exact-`2r` chain | `research/proofs/task55/certificates/exact_2r_cluster.json` | `0cd6e2f107d3aaa28a19cf04ede9e69bdedb152e34a3a3165b89aa79d88a7356` | Floquet, Gram, count, Feshbach, and `N_exp` data |
| `SMALL-6` | `research/proofs/task55/certificates/small_order_exact_classification.json` | `cb12d8502c6fcf31c5e8f1d23f3b9f1bb44b28b05a58f2e02067df08c04132b4` | producer-stage complete finite certificate; final promotion comes from the separate checker |
| `MG-18`, `MG-33` | `research/proofs/task51/certificates/c6_exact_evans_elimination.json` | `3de93781004929852ebdbd31c7ecbfdf72d125e0eea2b1606b4e472237ecd225` | exact `c6` polynomial and isolating interval |
| `MG-18` | `research/proofs/task55/certificates/multigap_support18.jsonl` | `9c8ef135fc11ca7b8c1761c3d45fb89c65790d97c12f2081787814f046c038bf` | 31,008 canonical word/vector records |
| `SG-INV`, `SG-REC` | `research/proofs/task55/certificates/single_gap_structure.json` | `a09e055fd07460269ec11857add62c2566f589d40ed9fee0bf006be6f6e75a7f` | exact quotient and recurrence identities |

The small-order JSON deliberately retains the producer label
`EXACT_FINITE_PRODUCER; INDEPENDENT_CHECKER_REQUIRED_FOR_UPGRADE`.  This is
not the final theorem status: the separate checker reconstructs the complete
certificate and upgrades `SMALL-6` to `COMPUTER_ASSISTED_PROVED`.

## Verification Snapshot

The following implementation-independent checkers were run directly against
the artifacts represented in this graph and returned success:

```text
verify_target_a_task55_exact_2r.py          TARGET_A_TASK55_EXACT_2R_VERIFY_PASS
verify_target_a_task55_small_order_exact.py TARGET_A_TASK55_SMALL_ORDER_EXACT_VERIFY_PASS
verify_target_a_task55_multigap.py          TARGET_A_TASK55_MULTIGAP_VERIFY_PASS
verify_target_a_task55_multigap_alt.py      TARGET_A_TASK55_MULTIGAP_ALT_VERIFY_PASS
verify_target_a_task55_single_gap.py        TARGET_A_TASK55_SINGLE_GAP_VERIFY_PASS
```

These PASS results establish the certificate/checker edges shown above.  They
do not promote `EXACT_FINITE_READ_ONLY`, `HIGH_PRECISION_DISCOVERY`, or `OPEN`
nodes, and they do not repair any `FALSIFIED_AS_STATED` dependency.
