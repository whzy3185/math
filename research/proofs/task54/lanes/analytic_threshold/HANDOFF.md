# Lane Handoff

## Lane

name: B, analytic IMS optimization

role: producer plus independent read-only mathematical audit

entry base: `07a922ea9fc084f08dc48299dd4535c5a32bbf15`

local commit(s): pending integration commit

## Research Question

exact question: optimize the globally valid IMS cap and its all-even tail.

## Strongest Result

statement: the exact global error is `(240R-342)/(R(2R^2+1))`, and
`N_IMS=240`.

evidence: the exact IMS formula is PROVED; the integrated spectral cap is
COMPUTER_ASSISTED_PROVED because it inherits the certified G6 edge.

## Proof Boundary

proved: global `r=1,2,3` cap under `2(R+4)<D`, exact residue thresholds.

not proved: optimality among every possible localization partition.

## Dependencies

inherited: Task 53 IMS identity, patch classification, and G6 global edge.

new: exact tent sums and residue-specific geometry.

## Method

analytic: exact finite sums and rational endpoint inequalities.

exact computation: producer/checker endpoint reconstruction.

interval computation: none.

high-precision discovery: none used for acceptance.

## Constants

`C_IMS<=120`, `R=floor((D-9)/2)`, `N_IMS=240`.

## Certificates

producer: `target_a_task54_threshold.py`.

checker: `verify_target_a_task54_threshold.py`.

tamper tests: Task 54 focused suite.

## Tests

commands: `pytest -q research/scripts/test_target_a_task54.py`.

results: 45 passed after hostile-audit checker hardening.

## Falsification Findings

The first producer run failed closed because its residue-table loop started
from the residue value rather than a legal even order. The corrected loop was
independently checked.

## Risks / Blockers

The criterion is sufficient, not an optimal localization theorem.

## Suggested Verifier Attacks

Recheck cyclic wraparound, offset path counts, and residue-6 floor formulas.

## Integration Recommendation

ACCEPT.
