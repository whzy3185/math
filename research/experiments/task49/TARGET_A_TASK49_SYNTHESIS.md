# Target A Task 49 Synthesis

## Decision Gates

| Gate | Result | Basis |
|---|---|---|
| P24 | `P24_READY_FOR_FORMAL_THEOREM` | independent 370,100-orbit destructive audit passes |
| Interface mechanism | `INTERFACE_MECHANISM_READY_FOR_PROOF` | localization, reciprocal Floquet data, invariance, and 160-digit splitting agree |
| Uniform bound | `UNIFORM_BOUND_TEMPLATE_FOUND` | stable single-tail and two-tail normalized envelopes |
| All-even target | `ALL_EVEN_PROOF_PROGRAM_READY` | every even residue has an explicit family and a coherent crossing atlas |

## Principal Findings

The p=17,...,24 frontier is now supported by a second implementation that
independently reconstructs canonical classes, flux lifts, moment exclusions,
both holonomies, primitive periods, and exact integer certificates.  Its
destructive accounting consumes all 370,100 legal dihedral orbits exactly
once and recovers 369,916 moment exclusions, 183 strict states, one equality,
and no lower or unresolved state.

The single-interface corrections admit stable empirical single-tail
normalizations.  The preferred two-interface families favor the expected
two-tail normalization.  The high-precision splitting computation now uses a
4x4 finite-ring Evans determinant, with FP64 matrices only for root location.
The ratio tends to the slow G6 bulk multiplier.  Positive real multipliers
explain the decay magnitude but leave finite holonomy and two-path geometry as
necessary ingredients in the mod16 branch preference.

The threshold atlas gives first exact crossings at 50, 94, 52, and 60 for the
G6, G10, symmetric two-G6, and shifted two-G6 families respectively.  These
are explicit-family onsets, not residue-class minimality claims.

The independent exact Hankel checker reproduces the 184-to-1 reduction through
depth five.  Insurance experiments support splitting total circumference
charge into separated +2 slips and support local four-step stability; the
high-period Hankel scan is explicitly only adversarial stress evidence.

## Remaining Mathematics

The main open step is a rigorous finite-defect theorem: certify the relevant
single-interface Evans zero and derive a uniform finite-ring estimate, then
extend the matching argument to two defects with both arc contributions and
twisted closure.  The empirical constants are inputs to that proof, not its
conclusion.

No generic expansion beyond order 2048 or period 40 is justified by the
present evidence.  The next task should be
`TARGET_A_TASK50_EXACT_INTERFACE_PROOF`.

## Final Status

`TARGET_A_TASK49_JCTB_PROOF_READY`
