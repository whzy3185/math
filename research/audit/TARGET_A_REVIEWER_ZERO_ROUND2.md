# Reviewer Zero Round 2 Report

## Review Identity

- Repository: `/Users/muelsyse/Documents/Codex/2026-08-15/cha-k/work/math`
- Branch: `agent/target-a-discovery-snapshot`
- HEAD reviewed: `b9e00bd34222d40e9ac954d3d5c4817644650be0`
- HEAD tree: `3873fb1c948a85443a2b55a642dbf1dba9359bdb`
- Reviewed UTC: `2026-08-16T09:08:30Z`
- Mode: read-only review of an isolated archive of committed HEAD, with the three blinded artifacts excluded before extraction

## Verdict

**PASS WITH MODERATE REPAIRS.** I found no critical or major mathematical correctness blocker. The theorem scopes are substantially disciplined, the period-8 analytic chain is coherent, the exact finite witness and finite exclusions reproduced successfully, and the operator/zone-folding boundary is correctly stated. The package is ready to begin manuscript drafting. It is not yet submission-grade as a reproducibility bundle: the environment is not locked, two independent-checker boundaries are weaker than their surrounding prose suggests, one human proof omits a required branch premise, and the canonical snapshot identifiers do not name the reviewed HEAD.

## Gate

- CRITICAL: **0**
- MAJOR: **0**
- MODERATE: **5**
- MINOR: **1**
- Gate pass: **true** (CRITICAL=0 and MAJOR=0)

## Findings

### RZ2-001

- Severity: **MODERATE**
- Category: Reproducibility
- Title: No committed environment lock or portable bootstrap
- Affected claims/files: Executable evidence for C3-C6, C10, C14, C17-C25; `research/experiments/TARGET_A_REPRODUCTION.md`; `research/paper/TARGET_A_FINITE_COMPUTATION_TRUST_MODEL.md`; `research/reproducibility/target_a_full_slow_reproduction_summary.json`
- Evidence: The historical reproduction records versions but obtains NumPy from a machine-specific absolute `PYTHONPATH` (`research/experiments/TARGET_A_REPRODUCTION.md:8-10,82-109`). The trust model itself says a submission supplement should include a machine-readable environment lock and command manifest (`research/paper/TARGET_A_FINITE_COMPUTATION_TRUST_MODEL.md:52-59`). The summary records versions and shell templates but is not an installable lock (`research/reproducibility/target_a_full_slow_reproduction_summary.json:22-30`). In a clean committed-tree copy, the documented project interpreter initially failed test collection because `numpy` was absent; installing the recorded `numpy==2.3.5` into the temporary review directory made the suite pass.
- Consequence: A referee cannot execute the advertised default suite from a fresh checkout without reconstructing an undocumented host-specific dependency path. This is a concrete reproducibility gap, although not evidence against the theorem results.
- Required action: Commit a portable, machine-readable lock/bootstrap (including Python, NumPy, SymPy, and pytest), replace absolute-path commands with repository-relative commands, and demonstrate the default and slow lanes in a clean environment created only from that lock.
- Disposition: **OPEN**

### RZ2-002

- Severity: **MODERATE**
- Category: Proof correctness
- Title: Human radical comparison omits the `r>4` branch premise
- Affected claims/files: C23, C25; `research/proofs/TARGET_A_LOW_PERIOD_SPECTRAL_FRONTIER.md`; `research/scripts/verify_target_a_low_period_spectral_frontier.py`
- Evidence: The proof defines `u=((r-4)^2-10)/2` and states that `u>0` and `u^2>5` imply `r>eta` (`research/proofs/TARGET_A_LOW_PERIOD_SPECTRAL_FRONTIER.md:179-197`). That implication is false without selecting the positive branch `r>4`; small nonnegative `r` can satisfy the two displayed conditions. The checker correctly guards the comparison with `value <= 4: return False` (`research/scripts/verify_target_a_low_period_spectral_frontier.py:171-177`).
- Consequence: The machine certificates are not invalidated, but the standalone human proof contains a genuine logical omission that could be copied into the manuscript.
- Required action: Add the exact premise/proof `r>4` before squaring, include it in the displayed certificate conditions, and add a negative regression showing that the low branch is rejected.
- Disposition: **OPEN**

### RZ2-003

- Severity: **MODERATE**
- Category: Classification independence
- Title: Low-period checker counts rows but does not bind them to the full canonical orbit set
- Affected claims/files: C22, C23, C25; `research/scripts/verify_target_a_low_period_spectral_frontier.py`; `research/proofs/target_a_low_period_spectral_frontier.json`
- Evidence: The checker independently recomputes only per-period orbit counts (`research/scripts/verify_target_a_low_period_spectral_frontier.py:238-240`), requires 2,626 unique `orbit_id` values (`:244-246`), and checks that each supplied row is individually canonical (`:250-262`). It never asserts uniqueness of `(p, canonical_q_signs)` or equality between the supplied row set and an independently enumerated canonical set. By contrast, the period-8 checker explicitly zips the stored table against independently generated representatives (`research/scripts/verify_target_a_period8_pattern_classification.py:248-281`). A separate Reviewer Zero enumeration confirmed that the committed 2,626-row table actually has no missing, extra, or duplicate canonical representatives.
- Consequence: The committed classification is complete in fact, but the advertised independent checker could accept an omitted orbit replaced by a duplicated canonical word under a fresh unique ID, provided the duplicate carries a valid certificate. This weakens tamper detection and the evidentiary independence of C22-C25.
- Required action: Independently enumerate the canonical `(p,Q)` set for every `1<=p<=16`, compare it exactly with the stored set, bind `orbit_id` deterministically to that ordering, and add omission/duplicate tamper-negative tests.
- Disposition: **OPEN**

### RZ2-004

- Severity: **MODERATE**
- Category: Finite-computation trust boundary
- Title: The canonical minimality checker does not replay per-state mathematics for `n<=22`
- Affected claims/files: C3 and Theorem A; `research/scripts/verify_target_a_minimality_certificate.py`; `research/paper/TARGET_A_FINITE_COMPUTATION_TRUST_MODEL.md`; `research/paper/TARGET_A_REPRODUCIBILITY_STATEMENT.md`
- Evidence: For `n<=20`, the checker validates aggregate status, counts, and optimizer records from pinned JSON (`research/scripts/verify_target_a_minimality_certificate.py:98-118`); for `n=22` it similarly validates aggregate shell/certificate counts and one optimizer row (`:121-150`). It does not reconstruct the historical per-state Rayleigh vectors. The package correctly discloses that checkpoint replay is integrity-only (`research/paper/TARGET_A_FINITE_COMPUTATION_TRUST_MODEL.md:20-31`) and that fresh frozen-worktree regeneration covers only `n=24,26,28,30` (`:33-42`; `research/paper/TARGET_A_REPRODUCIBILITY_STATEMENT.md:5-20`). Reviewer Zero reran exact `n=8,10,...,22` computations from reviewed HEAD; all passed with zero fallbacks and zero counterexamples.
- Consequence: No mismatch was found, but the committed one-command certificate verification for C3 is partly an attestation/hash check, not a mathematical replay over the whole range. The theorem therefore retains execution-trust exposure for the historical smaller-order logs.
- Required action: Retain the explicit computer-assisted label. For submission, add a clean-HEAD full-range regeneration manifest for `n=8,...,30` or archive independently replayable per-state certificates for `n<=22`; do not describe the current minimality checker alone as a complete mathematical replay.
- Disposition: **ACCEPTED_RISK**

### RZ2-005

- Severity: **MINOR**
- Category: Provenance
- Title: Canonical package snapshots do not identify the reviewed HEAD
- Affected claims/files: All C1-C25 provenance; `research/paper/target_a_claim_inventory.json`; `research/reproducibility/target_a_full_slow_reproduction_summary.json`; `research/scripts/verify_target_a_paper_package.py`
- Evidence: The claim inventory names frozen HEAD `dfb9c984...` and tree `7a15c449...` (`research/paper/target_a_claim_inventory.json:4-5`), while the slow reproduction names baseline commit `c5cadf3e...` and tree `dc08b21b...` (`research/reproducibility/target_a_full_slow_reproduction_summary.json:6-11`). The package verifier hard-codes the former identifiers (`research/scripts/verify_target_a_paper_package.py:62-67`). Neither canonical record names reviewed HEAD `b9e00bd34222d40e9ac954d3d5c4817644650be0` / tree `3873fb1c...`.
- Consequence: Artifact hashes currently pass, so this is not a mathematical defect, but a reader cannot determine from the canonical package metadata whether the final reviewed commit is itself the frozen theorem snapshot or merely contains an older frozen subset.
- Required action: Issue a final package manifest naming the submission/drafting HEAD and tree, or add an explicit immutable mapping proving that the reviewed HEAD changes no claim-bearing artifact relative to the frozen theorem snapshot.
- Disposition: **OPEN**

### RZ2-006

- Severity: **MODERATE**
- Category: Enumeration trust boundary
- Title: Production generator independence above `n=24` is aggregate rather than recordwise
- Affected claims/files: C3 at `n=26,28,30`; `research/audit/DIRECT_BRACELET_GENERATOR_AUDIT.md`; `research/scripts/target_a_direct_generator_audit.py`; `research/paper/TARGET_A_FINITE_COMPUTATION_TRUST_MODEL.md`
- Evidence: Full ordered record equality against the visited-set reference is established only through `n=22` (`research/audit/DIRECT_BRACELET_GENERATOR_AUDIT.md:27-46`), and the package says the dual-generator recordwise comparison extends through `n=24` (`research/paper/TARGET_A_FINITE_COMPUTATION_TRUST_MODEL.md:44-50`). For `n=26,28,30`, the slow Burnside audit checks shell totals, total counts, represented-size sums, ordering, and parity (`research/scripts/target_a_direct_generator_audit.py:155-164`), but not independent per-record canonicality or orbit size. Reviewer Zero reran all three slow audits successfully.
- Consequence: The same FKM implementation is well tested and no discrepancy was observed, but a production-only representative/orbit-size defect that preserves all aggregates is outside the independent audit at the largest orders. This is residual implementation trust in the exhaustive portion of C3.
- Required action: Either provide a proof-oriented validation of the FKM/reflection/orbit-size implementation for arbitrary `n`, or add a feasible independent recordwise/checksummed validation strategy for `n=26,28,30` (for example, partitioned independent canonicality/orbit checks with a separately implemented generator).
- Disposition: **ACCEPTED_RISK**

## High-Risk Repair Checklist

- [x] Claim scope is explicitly limited: no all-period optimum, no all-signings optimum, and no assertion that every even `n>=32` fails.
- [x] The `n=32` witness has exact positive-definiteness, exact threshold comparison, and an independent second-gauge reconstruction.
- [x] Finite and infinite Floquet spectra are separated, with both finite holonomies covered by `z^L=alpha`.
- [x] The period-8 determinant, uniform positivity, sharp constant, and unique edge `z=1` have independent exact routes.
- [x] The moment barrier is used only in the valid direction `F_k>0 => R(Q)>8`; negative excesses are not promoted to upper bounds.
- [x] Short-cell collision multiplicities are represented by Laurent entries and cyclic statistics; direct tests include `p=1,2,3,4` behavior.
- [x] Period-8 classification covers all 128 legal flux words and separates exact spectral signatures from numerical coincidences.
- [x] Translation, reflection, global negation (including odd-cell `z -> -z`), and repeated-cell zone folding are proved; the `p=16` target is correctly identified as a doubled period-8 cell.
- [~] The 2,626-row low-period table is complete in the committed artifact, but its independent checker needs exact stored-set binding (RZ2-003).
- [~] Finite minimality regeneration and generator audits are strong but not uniform in trust level across all orders (RZ2-004, RZ2-006).
- [~] Reproduction versions are recorded, but a portable environment lock and final-HEAD provenance manifest are still missing (RZ2-001, RZ2-005).

## Commands and Checks Run

- Verified `git rev-parse --verify HEAD` and `git symbolic-ref --short HEAD` against the requested commit and branch.
- Built an isolated committed-tree archive with all three blinded paths excluded before extraction.
- Full default suite: `python -m pytest -q research/scripts` -> **241 passed, 3 skipped, 17 subtests passed** in 138.73 s.
- Explicit slow generator suite for `n=26,28,30` -> **3 passed** in 151.82 s.
- Exact raw regeneration `n=8,10,...,18` -> all PASS; 698,868 non-optimizers Rayleigh-certified, zero fallbacks, zero counterexamples.
- Exact raw regeneration `n=20` -> 2,097,152 classes; 2,097,150 Rayleigh-certified; zero fallbacks/counterexamples.
- Exact quotient regeneration `n=22` -> 48,734 Q-orbits, 97,468 spectral states, 8,388,608 represented switching classes; zero fallbacks/counterexamples.
- `verify_target_a_paper_package.py` -> `TARGET_A_PAPER_PACKAGE_LINT_PASS` and all component PASS statuses.
- `verify_target_a_minimality_certificate.py` -> `TARGET_A_MINIMALITY_CERTIFICATE_PASS`.
- `verify_target_a_period8_infinite_family.py` -> PASS.
- `verify_target_a_period8_sharp_constant.py` -> PASS.
- `verify_target_a_periodic_operator_equivalences.py` -> PASS.
- `verify_target_a_low_period_spectral_frontier.py` -> PASS.
- Independent Reviewer Zero canonical-set enumeration for all `1<=p<=16` -> 2,626 rows, no missing, extra, or duplicate representatives.

## Final Readiness Judgment

The mathematical package clears the requested gate and is suitable as the source for manuscript drafting. Drafting should preserve the present scope boundaries and proof-type labels. Before external submission or a reproducibility claim stronger than “regeneration-based computer-assisted proof,” resolve RZ2-001 through RZ2-003 and RZ2-005, and either strengthen or explicitly retain the accepted risks RZ2-004 and RZ2-006.
