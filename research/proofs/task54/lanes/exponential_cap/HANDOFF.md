# Lane Handoff

## Lane

name: A, exponential global cap

role: spectral asymptotics and explicit-constant audit

entry base: `07a922ea9fc084f08dc48299dd4535c5a32bbf15`

local commit(s): pending integration commit

## Research Question

exact question: turn exact-`r` into a global exponential cap and extract
explicit constants if available.

## Strongest Result

historical statement: existential exponential global caps were claimed for
`r=1,2,3` with the correct period-eight-cell exponent.

historical Task 54 evidence: `OPEN_PENDING_2R_REPAIR`; the old proof used an
invalid one-mode-per-interface complement. Task 55 supersedes this status with
an independently checked exact-`2r` theorem and the explicit bound
`3505r(9/25)^ell`.

## Proof Boundary

withdrawn: cluster ownership of the spectral top and qualitative residue caps
as stated with only `r` squared modes.

not proved by this Task 54 lane: numerical `C_1,C_2,C_3` or `N_exp`.

proved subsequently in Task 55: `C_r=3505r` and the sufficient onset
`N_exp=3120`.

## Dependencies

inherited historical inputs: now-withdrawn exact-`r` and complement gap, plus
the surviving G6 cell decay.

new: canonical site-to-cell distance conversion.

## Method

analytic: min-max and cluster/complement separation.

exact computation: audit of stored constants.

interval computation: required for future tail normalization.

high-precision discovery: not used for acceptance.

## Constants

`q=9/25`, `ell=floor((floor(D/4)-12)/8)`, complement inverse 400.

## Certificates

producer: inherited exact-`r` package, now a retraction record.

checker: red-team distance-unit audit.

tamper tests: distance conversion and complement threshold tests.

## Tests

commands: Task 54 focused exact-`r` checker.

results: the old arithmetic was reproducible but the rank premise was false;
the theorem and numerical constants remain OPEN in Task 54.

## Falsification Findings

The original exponent used a site distance as though it were a full-cell
distance. It was corrected before accepting this lane.

## Risks / Blockers

Normalized G6 tail and Gram constants are absent.

## Suggested Verifier Attacks

Reconstruct the matched mode and test every site/cell/core-offset conversion.

## Integration Recommendation

WITHDRAW Task 54 qualitative theorem. Reassess only through a Task 55
codimension-`2r` certificate; retain explicit constants and `N_exp` as OPEN.
