# Response to Reviewer One

We thank Reviewer One for a careful and constructive report. The reviewed V1
is preserved byte-for-byte. All revisions below appear in V2 and its separate
section sources.

## R1-001 - accessible computer-assisted proof artifact

Resolved. Sections 9.5 and C.1 now cite the public immutable artifact snapshot
at commit `c81be34a3b12a7ac47adbb4499c475df7bf4fc04`. The new machine-readable
submission manifest binds Theorems A and F to SHA-256 hashes of the checker
source, pinned environment, production checkpoint data, complete 2,626-row
low-period table, and regeneration records. Its checker reads the files from
the pinned Git object. The text now states exactly which data are committed
and which per-state decisions require deterministic full regeneration.

## R1-002 - order-32 certificate not displayed

Resolved by removing the undisplayed elimination from the logical proof.
Proposition 3.1 now invokes the explicit fiber matrix, determinant polynomial,
positive-coefficient expansion, and finite Floquet decomposition displayed in
Sections 4.1-4.3. The LDL/Bareiss computation remains only an independent
cross-check in Appendix B.4.

## R1-003 - lift and basis for residual vectors

Resolved. Sections 2.3 and B.2 define the canonical lift
`tau_0=+1`, `tau_(i+1)=Q_i tau_i`, the ordered fiber basis
`(v_0,...,v_(p-1))`, and the unitary transport to the other lift.

## R1-004 - closed-walk derivation

Resolved. Section 7.2 now gives an exact integer dynamic-programming recurrence
for every closed-walk moment. Appendix B.3 displays the full moment and excess
table for all four two-defect separations, including the first positive values
`F_4=5504`, `F_6=64336`, and `F_9=2872096`. The text explicitly classifies the
word collection as finite computer-assisted symbolic algebra and names its
checker.

## R1-005 - citations and novelty boundary

Resolved. The introduction and Section 2.6 cite [5] at the inherited family,
threshold formula, and Conjecture 3, cite the companion context [4], and state
which ingredients are inherited and which theorems are new.

## R1-006 - order-eight quadrilaterals

Resolved. Section 2.2 now calls `Q` the distinguished local quadrilateral flux
word, records the two additional step-two quadrilaterals at order eight, and
explains why the complete `(tau,alpha)` cycle coordinates still cover every
finite signing.

## R1-007 - primitive-period domain

Resolved. Theorem F and Section 8 now define the domain as infinite operators
whose Hamilton-gauge triangle word has least positive period at most 16,
identify the objective as squared infinite-volume radius, exclude finite
holonomy sectors, and explain repeated-cell accounting via zone folding.

## Requested gate

The revised manuscript is to be re-reviewed against the same criteria. The
Markdown readiness gate may pass only if the independent second round reports
zero CRITICAL and zero MAJOR findings.

## Round 2 follow-up

The fresh second review reported `CRITICAL=0`, `MAJOR=0`, `MODERATE=2`, and
`MINOR=3`, so the requested readiness gate passed. We nevertheless resolved
all five nonblocking findings before freezing the paper draft: Section 9.1 now
classifies the moment coefficient collection consistently; Appendix C gives
end-to-end regeneration commands, expected chain hashes, and measured resource
requirements; Section 5.2 proves irreducibility of (5.7); Section 2.3 formally
defines `H_Q(z)`; and “global negation” is now called global edge-sign
negation.
