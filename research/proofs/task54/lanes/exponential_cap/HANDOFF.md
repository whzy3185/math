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

statement: existential exponential global caps hold for `r=1,2,3` with the
correct period-eight-cell exponent.

evidence: COMPUTER_ASSISTED_PROVED overall; the implication from the certified
isolation/complement inputs is analytic.

## Proof Boundary

proved: cluster ownership of the spectral top and qualitative residue caps.

not proved: numerical `C_1,C_2,C_3` or `N_exp`.

## Dependencies

inherited: corrected exact-`r`, complement gap, G6 cell decay.

new: canonical site-to-cell distance conversion.

## Method

analytic: min-max and cluster/complement separation.

exact computation: audit of stored constants.

interval computation: required for future tail normalization.

high-precision discovery: not used for acceptance.

## Constants

`q=9/25`, `ell=floor((floor(D/4)-12)/8)`, complement inverse 400.

## Certificates

producer: inherited exact-`r` package.

checker: red-team distance-unit audit.

tamper tests: distance conversion and complement threshold tests.

## Tests

commands: Task 54 focused exact-`r` checker.

results: arithmetic checker and corrected theorem red-team pass; numerical
constants remain OPEN.

## Falsification Findings

The original exponent used a site distance as though it were a full-cell
distance. It was corrected before accepting this lane.

## Risks / Blockers

Normalized G6 tail and Gram constants are absent.

## Suggested Verifier Attacks

Reconstruct the matched mode and test every site/cell/core-offset conversion.

## Integration Recommendation

ACCEPT qualitative theorem; retain explicit constants and `N_exp` as OPEN.
