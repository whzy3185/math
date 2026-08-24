# Target A Manuscript Import Safety Manifest

Status: `CANONICAL_CURRENT`.

This manifest is the mandatory source-selection contract for manuscript
reconstruction. It changes no mathematical theorem. Its purpose is to prevent
historical wording, especially the withdrawn one-mode-per-interface model,
from being copied into a current proof.

## Precedence Rule

Classification is by normalized repository-relative path. An exact-file rule
overrides a directory rule. Among directory rules, the longest matching path
wins. An unlisted path outside the canonical root is not approved for direct
theorem import and must be treated as `IMPORT_WITH_CAUTION` until reviewed.

The four allowed category labels are:

```text
CANONICAL_IMPORT
IMPORT_WITH_CAUTION
DO_NOT_IMPORT_CURRENT_CLAIMS
HISTORICAL_ONLY
```

`DO_NOT_IMPORT_CURRENT_CLAIMS` bars theorem statements, formulas, and proof
prose from current use. A file in that category may still be cited as
historical provenance. `HISTORICAL_ONLY` permits only an explicitly labeled
historical or retraction citation; no claim in such a file is a current
dependency merely because later work corrected a related result.

## Directory Defaults

| Path | Category | Import rule |
|---|---|---|
| `research/paper/proof_completion/` | `CANONICAL_IMPORT` | Canonical-current default. Exact-path and subdirectory rules below take precedence. |
| `research/paper/proof_completion/11_stale_claim_audit/` | `IMPORT_WITH_CAUTION` | Editorial audit and rejection language only; do not import as theorem prose. |
| `research/paper/proof_completion/12_referee_review/` | `IMPORT_WITH_CAUTION` | Review findings and presentation constraints only; do not replace proofs with review verdicts. |
| `research/paper/manuscript_tex_pub/` | `HISTORICAL_ONLY` | Frozen pre-reframe manuscript; it is not a source of updated Task 57 claims. |
| `research/paper/manuscript_tex_pub_zh/` | `HISTORICAL_ONLY` | Frozen pre-reframe translation; it is not a source of updated Task 57 claims. |
| `research/proofs/task52/` | `IMPORT_WITH_CAUTION` | Research-stage source; use only after matching every imported claim to the canonical package. |
| `research/proofs/task53/` | `IMPORT_WITH_CAUTION` | Research-stage source containing both surviving results and superseded formulations. |
| `research/proofs/task54/` | `IMPORT_WITH_CAUTION` | Mixed research stage: some non-rank results survive, while exact-path overrides below quarantine the superseded exact-`r` corpus. |
| `research/proofs/task55/` | `IMPORT_WITH_CAUTION` | Corrected certificates and theorem sources; canonical wording in this package remains controlling. |
| `research/proofs/task56/` | `IMPORT_WITH_CAUTION` | Later research source; import only a claim already registered canonically. |

## Current-Claim Blacklist

The following exact paths are `DO_NOT_IMPORT_CURRENT_CLAIMS`:

| Exact path | Hazard |
|---|---|
| `research/proofs/task52/TARGET_A_MULTI_SLIP_INTERACTION_ASYMPTOTICS.md` | Contains the obsolete heuristic `H_eff=c6 I_r+...`; the accepted local space has dimension `2r`. |
| `research/proofs/task54/TARGET_A_COMMON_RESIDUE_LIMIT_SCOPE.md` | Uses the phrase "exact-r theory" for a theory that was later falsified and replaced by the separated exact-`2r` theorem. |

Neither file may supply a current theorem, formula, lemma statement, proof
step, or dimension count. If its surrounding topic is discussed, rewrite from
the canonical proof package and cite the historical path only as provenance.

## Superseded Exact-r Corpus

The following exact paths are `HISTORICAL_ONLY`:

```text
research/proofs/task53/TARGET_A_FESHBACH_EFFECTIVE_MATRIX.md
research/proofs/task53/TARGET_A_TASK53_REVIEWS.md
research/proofs/task54/TARGET_A_COMPLEMENT_GAP_THEOREM.md
research/proofs/task54/TARGET_A_EFFECTIVE_COUPLING_FORMULAS.md
research/proofs/task54/TARGET_A_EXACT_R_PHASE_SLIP_EXCITATION_THEOREM.md
research/proofs/task54/TARGET_A_EXACT_R_RIESZ_THEOREM.md
research/proofs/task54/TARGET_A_EXPONENTIAL_EVENTUAL_THRESHOLD.md
research/proofs/task54/TARGET_A_EXPONENTIAL_FIXED_R_GLOBAL_CAP.md
research/proofs/task54/TARGET_A_EXPONENTIAL_RESIDUE_BOUNDS.md
research/proofs/task54/TARGET_A_FESHBACH_EFFECTIVE_HAMILTONIAN.md
research/proofs/task54/TARGET_A_GEOMETRIC_RESOLVENT_GLUE.md
research/proofs/task54/TARGET_A_TASK54_CONTINUATION_BASELINE.md
research/proofs/task54/TARGET_A_TASK54_CONTINUATION_DEPENDENCY_GRAPH.md
research/proofs/task54/TARGET_A_TASK54_CONTINUATION_MASTER_LEDGER.md
research/proofs/task54/TARGET_A_TASK54_CONTINUATION_SYNTHESIS.md
research/proofs/task54/lanes/exponential_cap/HANDOFF.md
```

The retraction certificate and its producer/checker are also
`HISTORICAL_ONLY` as mathematical sources:

```text
research/proofs/task54/certificates/exact_r_complement_gap.json
research/scripts/target_a_task54_exact_r.py
research/scripts/verify_target_a_task54_exact_r.py
```

They may be retained and executed to verify that the old claim is retracted;
they do not verify a positive exact-`r` theorem.

## Canonical Rank Contract

Current manuscript prose must preserve all four statements:

```text
dim ker(H_6-c6)=2;
r separated G6 interfaces give exactly 2r near-c6 squared levels;
the complementary space has codimension 2r;
the problem-specific Feshbach operator is 2r x 2r.
```

An occurrence of rank one, exact-`r`, codimension-`r`, `I_r`, or an `r x r`
problem-specific G6 model is admissible only inside an explicit rejection,
historical description, or fail-closed tamper test. It must never be promoted
to an active theorem.

## Classification Logic Contract

Use

```text
theta_n:=rho_-(n)^2,
failure at n iff m_n<rho_-(n) iff m_n^2<theta_n.
```

For the equality formulation `m_n=rho_-(n)`, a valid-order proof has two
independent logical inputs: the lower-bound/exhaustion direction and explicit
candidate attainment. Importing only the first does not establish equality.

## Producer And Verification Boundary

This manifest and the stale-word scan are producer-side editorial controls.
Their existence is not independent mathematical verification. A manuscript
import review must separately check every selected theorem dependency and
confirm that no exact-path override was bypassed.

## Manual Import Checklist

- [ ] The hierarchy contains exactly seven main theorem families, 1.1--1.7.
- [ ] `m_n` is compared with `rho_-(n)` and `m_n^2` with `theta_n`.
- [ ] Equality wording cites candidate attainment as well as exhaustion.
- [ ] No blacklisted exact path supplies a current claim or formula.
- [ ] Every historical exact-`r` citation is explicitly labeled retracted.
- [ ] Rank two, exact `2r`, codimension `2r`, and `2r x 2r` remain paired.
- [ ] Producer output is not described as independent verification.
- [ ] Both frozen manuscript trees remain unchanged during this repair.
