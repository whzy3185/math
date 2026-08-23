# Lane Handoff

## Lane

name: C, finite structured counterexample tail

role: exact finite spectral certification

entry base: `07a922ea9fc084f08dc48299dd4535c5a32bbf15`

local commit(s): pending integration commit

## Research Question

exact question: bridge the finite orders below the analytic tail with full
spectral-radius certificates.

## Strongest Result

statement: all 96 even orders `48<=n<240` have certified structured
counterexamples; combined `N_star=48`.

evidence: COMPUTER_ASSISTED_PROVED.

## Proof Boundary

proved: full spectral top below the conjectured threshold at every stored
order.

not proved: globally minimal eventual onset or optimality of the witnesses.

## Dependencies

inherited: signing reconstruction and exact sparse LDL utilities.

new: compressed 96-row certificate and natural-order independent checker.

## Method

analytic: `rho_-^2(n)>8-200/n^2`.

exact computation: positive definiteness of `qI-pA^2`.

interval computation: none.

high-precision discovery: used only before rational certification.

## Constants

`N_finite=48`, finite bridge endpoint `238`.

## Certificates

producer: `target_a_task54_threshold.py`.

checker: `verify_target_a_task54_threshold.py` with a different ordering.

tamper tests: remove order, mutate word, alter upper bound, corrupt endpoint.

## Tests

commands: `pytest -q research/scripts/test_target_a_task54.py`.

results: 45 passed after hostile-audit checker hardening.

## Falsification Findings

No missing order in the structured tail. This is not a global signing census.

## Risks / Blockers

Certificate regeneration takes about 20 seconds per complete pass.

## Suggested Verifier Attacks

Check integer width, holonomy reconstruction, full-spectrum inequality
direction, and ordered-record completeness.

## Integration Recommendation

ACCEPT.
