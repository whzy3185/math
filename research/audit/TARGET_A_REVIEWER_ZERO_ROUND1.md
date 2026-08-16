# Reviewer Zero Report - Round 1

Frozen-head target: `dfb9c9846fa95545fdb1a5153ceabe1767c9ee0a`

Gate recommendation: **BLOCK_PENDING_MAJOR_REVISIONS**

There are no CRITICAL findings. There are four MAJOR findings. The analytic period-8 core, the `n=32` exact witness, the finite/infinite Floquet distinction, the sharp `eta` argument, the period-8 trichotomy, the arbitrary-period moment direction, and the `p<=16` finite checks all survived this pass. The package is blocked by provenance and dependency/checker claims, not by a detected counterexample to those mathematical arguments.

## RZ-001 - MAJOR - The purported frozen paper package is not in the frozen tree

**Evidence:** `research/paper/target_a_claim_inventory.json:3-5`; `research/scripts/verify_target_a_paper_package.py:66-67`. At review time, `git status --short` reports the inventory, dependency graph, all paper-package Markdown files, and the paper-package verifier/tests as `??` untracked, while `HEAD` is the stated frozen head.

**Analysis:** The inventory declares itself complete and identifies a frozen head/tree, but those Git objects do not contain the package being reviewed. The verifier merely compares the two strings with hard-coded constants; it neither compares the live repository head/tree nor verifies that the package files are tracked by that tree. Consequently the frozen references cannot authenticate the current claim statements, graph, scope text, or package checker.

**Required action:** Put the complete reviewed package in an actual frozen commit/tree, or publish a content-addressed package manifest that includes every package file. Make the verifier compare the live `HEAD`/tree and verify tracked membership (or explicitly identify a separate package tree) instead of accepting hard-coded labels.

## RZ-002 - MAJOR - C24 omits the zone-folding theorem needed for repeated-cell equality

**Evidence:** `research/paper/target_a_claim_inventory.json:33`; `research/paper/target_a_theorem_dependency_graph.json:14`; `research/proofs/TARGET_A_PERIODIC_OPERATOR_EQUIVALENCES.md:21-32`; `research/proofs/TARGET_A_PERIODIC_OPERATOR_EQUIVALENCES.md:46-58`; `research/scripts/verify_target_a_low_period_spectral_frontier.py:258-270`.

**Analysis:** C24 depends only on orbit enumeration C22, but enumeration and primitive-period detection do not prove that a repeated `p=16` Bloch cell has the same infinite-volume spectrum as its primitive `p=8` cell. That implication is exactly the standalone zone-folding theorem. Its proof/checker exists in the filesystem, but the theorem is absent from the 25-claim inventory and dependency graph; the C24 checker only checks primitive words/repetition flags and assigns the Task 40A target certificate.

**Required action:** Add periodic conjugacy/zone folding as an inventoried claim and a dependency of C24 and C23, with its proof, certificate, checker, test, and hashes. Alternatively incorporate the full zone-folding proof and an explicit spectral direct-sum check into C24's listed artifacts.

## RZ-003 - MAJOR - The minimality checker authenticates digests and counts, not the per-state exact certificates

**Evidence:** `research/paper/TARGET_A_PROOF_CLASSIFICATION.md:23-25`; `research/scripts/target_a_minimality_search.py:919-927`; `research/scripts/target_a_minimality_search.py:963-963`; `research/scripts/target_a_minimality_search.py:824-839`; `research/scripts/target_a_checkpoint_replay.py:31-33`; `research/scripts/target_a_checkpoint_replay.py:66-79`; `research/scripts/verify_target_a_minimality_certificate.py:173-176`; `research/scripts/verify_target_a_minimality_certificate.py:241-253`.

**Analysis:** During a fresh search, each nonoptimizer is decided by an exact rational Rayleigh quotient, which is mathematically valid. However the checkpoint retains only aggregate counts and a hash of serialized decision records; ordinary successful records do not retain the integer vector, and replay hashes the already-stored certificate hashes without reconstructing the matrix or quotient. The total checker then trusts counts, zero fallbacks/counterexamples, and the replay. Thus the packaged JSON is an authenticated execution transcript, not an independently checkable chain of exact certificates. The separate full regeneration is valuable evidence, but it is not what the advertised minimality certificate checker performs.

**Required action:** Either persist enough per-state data for an independent checker to rebuild every Rayleigh inequality, or make full deterministic regeneration the required verifier and label checkpoint replay as provenance/completeness replay only. Revise the `2^31` trust explanation to say explicitly that 17,929,600 quotient states were regenerated and exactly screened after floating eigenvectors proposed integer vectors; do not describe digest-only checkpoints as independently verified exact certificate chains.

## RZ-004 - MAJOR - The dependency graph conflates logical premises, alternative proofs, and circular verification cross-checks

**Evidence:** `research/paper/target_a_claim_inventory.json:17`; `research/paper/target_a_claim_inventory.json:32`; `research/paper/target_a_theorem_dependency_graph.json:9-11`; `research/proofs/TARGET_A_LOW_PERIOD_SPECTRAL_FRONTIER.md:162-230`; `research/scripts/verify_target_a_period8_structural_mechanism.py:19-25`; `research/scripts/verify_target_a_period8_structural_mechanism.py:419-430`.

**Analysis:** C8 is declared dependent on C10, while C10's listed checker hard-pins and reads the C8/C9 classification artifact as a required input. That is an executable evidence cycle even though the JSON claim graph is syntactically acyclic. Separately, C23 is declared dependent on C25 and the deletion test says removing C25 leaves five competitors uncertified, but C23's own frontier proof already supplies exact certificates for all 2624 competitors; C25 is a later compression/alternative route. These are not faithful logical deletion semantics.

**Required action:** Maintain separate graphs for mathematical implication, primary-proof dependencies, and optional independent cross-checks. Remove C25 as a logical premise of C23 unless Theorem F is explicitly redefined as the compressed proof, and make the C10 checker able to verify the structural proof without requiring the classification result it is meant to cross-check.

## RZ-005 - MODERATE - C11's short-cell collision scope is not exercised by its listed checker

**Evidence:** `research/paper/target_a_claim_inventory.json:20`; `research/proofs/TARGET_A_GENERAL_PERIOD_MOMENT_OBSTRUCTIONS.md:93-97`; `research/scripts/target_a_general_period_moments.py:94-115`; `research/scripts/verify_target_a_period8_structural_mechanism.py:26-26`; `research/scripts/verify_target_a_period8_structural_mechanism.py:109-139`.

**Analysis:** C11 says quotient fibers retain multiplicities under short-cell residue collisions, and the general proof says its row check includes those collisions. The cited row implementation compares coefficients keyed by absolute displacements `-4,...,+4`, so it never merges residues modulo `p`; C11's listed independent checker fixes `N=8`. The later Laurent moment checks do support C17-C19 for small `p`, but they do not directly verify the quotient-level `A^2` collision statement attached to C11.

**Required action:** Add a direct quotient/Laurent `A^2` identity check for `p=1,2,3,4` that sums all coincident residue entries with their cell powers, and point C11 to it. Otherwise narrow C11's scope to the infinite-lattice displacement identity and leave collision coverage to C17-C19.

## RZ-006 - MINOR - The reproducibility statement falsely says checkpoint chunks are uncommitted

**Evidence:** `research/paper/TARGET_A_REPRODUCIBILITY_STATEMENT.md:37-40`; `research/reproducibility/target_a_full_slow_reproduction_summary.json:200-203`. At review time `git ls-files` reports 29, 77, 251, and 909 tracked files under the `n24`, `n26`, `n28`, and `n30` checkpoint directories respectively.

**Analysis:** Both documents state that large chunk files are not committed, but the reviewed repository tracks the complete production checkpoint directories. This does not harm the theorem, but it makes the repository/supplement trust boundary factually wrong.

**Required action:** Update the statements to distinguish committed production checkpoints from uncommitted external fresh-regeneration outputs and full runtime logs.

## RZ-007 - MINOR - A proved Target A period-10 theorem is outside the "complete" claim inventory without an exclusion record

**Evidence:** `research/paper/target_a_claim_inventory.json:3-9`; `research/paper/target_a_claim_inventory.json:35-36`; `research/proofs/TARGET_A_PERIOD10_FAMILY.md:5-21`.

**Analysis:** The inventory declares itself complete and lists only scope exclusions about global optima, while a tracked `TARGET_A_` proof states a second infinite counterexample family for multiples of 10. Its evidence is explicitly still subject to independent human audit, so omission may be intentional, but the package gives no status explaining whether this theorem is rejected, deferred, or supplement-only.

**Required action:** Add an explicit excluded/deferred-claims section identifying the period-10 family and its unmet audit gate, or complete its independent audit and inventory it with an appropriate manuscript role.

## Verification Performed

Read-only executions passed for the paper-package verifier, periodic-operator equivalences, exact `n=32` certificate, period-8 infinite family, sharp constant, pattern classification, structural mechanism, general-period moments, low-period spectral frontier, and low-period structural frontier. The full `n=24,26,28,30` regeneration was not rerun during this prompt; the review inspected its saved summary, search implementation, checkpoints, replay, and total checker.
