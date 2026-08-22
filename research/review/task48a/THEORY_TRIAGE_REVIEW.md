# Reviewer Theory-Triage: Task 48A

## Verdict

- BLOCKER: 0
- MAJOR: 3
- MODERATE: 4
- MINOR: 2

The reconnaissance signals are internally coherent and sufficiently strong
to justify one focused proof attempt.  They do not justify changing the
formal theorem statements yet.

## Major findings

1. **The Evans equation is not exact yet.**  The one-step and cell transfer
   matrices have exact entries, but stable subspaces and the matching zero are
   evaluated numerically.  An exact resultant, algebraic stable-subspace
   construction, or rigorous interval argument is required before `c6` or
   `c10` can enter a theorem.

2. **Eventual all-even failure lacks uniform bounds.**  Finite data and
   localized limits do not control every member of each residue family.  The
   next proof must bound finite-ring self-interaction uniformly and compare it
   with an exact lower bound for the conjectured threshold.

3. **The p<=24 extension needs an independent implementation audit.**  Orbit
   accounting is complete and exact acceptance is independent of floating
   ranking, but the remaining 59 certificates reuse the established endpoint
   Rayleigh machinery.  A second checker should verify canonicalization,
   zone folding, both endpoint holonomies, and each certificate hash.

## Moderate findings

1. Very large two-interface separations become indistinguishable at double
   precision.  Parity and holonomy claims must be based on the resolved
   finite-size window or on high-precision transfer analysis, not late rows.

2. The degree-10 polynomial for `c6` passes numerical validation but remains
   a PSLQ candidate.  The rejected gap-10 relation demonstrates why the
   validation gate is necessary.

3. Localization fits must exclude the iterative noise floor.  The archived
   raw profiles permit rechecking the selected 2-to-12-cell window.

4. The Hankel witnesses are generated from floating generalized eigenvectors,
   although every accepted inequality is exact rational arithmetic.  A
   reviewer should independently recompute representative witnesses and the
   target PSD sanity check.

## Minor findings

1. The labels `bulk cell` and `displayed period` should be normalized before
   manuscript integration to avoid confusing Q period, tau period, and ring
   order.

2. The infinite interface has no finite-ring holonomy; reports correctly use
   holonomy only for finite rings, and the eventual proof should preserve this
   distinction.

## Active attempts to falsify the signals

- Changing the transfer boundary by one additional period-8 cell leaves the
  high-precision interface roots unchanged at the recorded precision floor.
- Power-law fits have materially worse BIC than one- and two-exponential fits.
- Left and right localization fits agree with the bulk slow multiplier within
  the reported window; fitting into the noise floor breaks the agreement and
  is therefore rejected.
- Both finite holonomies were scanned.  The late-size numerical ties are not
  interpreted as holonomy changes.
- The residue-12 sequence was exact-certified independently of the numerical
  threshold through rational upper bounds, sparse exact LDL positivity, and
  rational threshold lower bounds.
- The p<=24 partition consumes every orbit exactly once and retains primitive
  Q/tau periods and repeated-cell metadata.
- The moment support implication direction was tested on the exact target,
  which is not excluded.

No unresolved blocker prevents the next proof task.  All three major findings
must be closed before any corresponding formal theorem is upgraded.
