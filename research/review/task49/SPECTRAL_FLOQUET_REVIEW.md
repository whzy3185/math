# Task 49 Independent Spectral/Floquet Review

## Findings

### MAJOR 1: the exact interface theorem is not yet closed

The Evans roots, stable two-planes, and two-defect splitting are numerical,
although now computed in the correct four-dimensional transfer model and
validated at increasing precision.  A JCTB theorem still requires exact or
interval isolation of the stable subspaces, a simple zero, and a uniform
finite-ring remainder.  This is a proof blocker for the future theorem, not a
defect in Task 49's mechanism-validation claim.

### MODERATE 1: positive Floquet phase does not explain mod16 selection

The slow multiplier controls the magnitude of the splitting but has argument
zero.  Any manuscript explanation must retain the two propagation arcs and
the finite holonomy.  It must not present `L`-parity of `mu6^L` as the cause.

### MODERATE 2: empirical envelope constants are not certified constants

The normalized errors are stable and select sensible one-tail and two-tail
forms.  The proposed `1.1x` and `2x` constants remain experimental until a
transfer contraction or interval-Evans estimate proves them uniformly.

### MINOR 1: fit-window variation should remain visible

All localization fits have `R^2>0.98`, but the largest distance from the slow
multiplier is about `0.0309`.  A future figure should show several windows or
an uncertainty band rather than one regression line.

## Positive Checks

The finite/infinite distinction is explicit.  Holonomy is confined to the
finite twisted closure.  The two-interface calculation uses FP64 only for
initial root locations, then 80/120/160-digit 4x4 Evans solving.  Two full
arbitrary-precision finite matrices agree to about 79 digits.  Four matching
margins and the equivalent left-match construction recover the same Evans
zeros, and the reciprocal Floquet structure is numerically clean.

## Verdict

- BLOCKER: 0
- MAJOR: 1
- MODERATE: 2
- MINOR: 1

`INTERFACE_MECHANISM_READY_FOR_PROOF` is justified.  `EXACT_INTERFACE_THEOREM`
would not be justified.
