# Referee Checklist

- [x] The G6 defect word, lift, operator, polynomial, and isolating interval
  are explicit.
- [x] The bulk hyperbolicity statement has stable and unstable dimensions
  two, not one.
- [x] Boundedness, self-adjointness, and finite range of `A_6` and `H_6` are
  proved directly from their matrix coefficients.
- [x] A two-tail Dirichlet decoupling differs from `H_6` by finite rank, and
  the finite middle block is explicitly removed from the essential spectrum.
- [x] Each periodic half-line essential spectrum is proved equal to its
  whole-line bulk spectrum in both directions: by cutoff Bloch Weyl sequences
  and by a full-line resolvent parametrix modulo finite rank.
- [x] Translation and diagonal switching identify both limit spectra with
  `sigma(H_ref)`, whose upper edge is `eta`.
- [x] Every spectral point above `eta` is shown to be discrete with finite
  multiplicity before the Evans matching argument is invoked.
- [x] The `H_6=A_6^2` eigenvector is decomposed into its `+sqrt(y)` and
  `-sqrt(y)` branches, and the `ell^2` condition is proved to force the
  stable/unstable tail planes and exponential decay.
- [x] The physical matching condition is stated coordinate free before any
  Grassmann chart.
- [x] Basis changes do not alter the zero set of the exterior determinant.
- [x] Forward and reflected orientations are related by unitary equivalence.
- [x] The local Evans root is unsquared, physical, unique, and simple.
- [x] The degree-ten polynomial identifies the physical root but is not used
  to declare every algebraic root physical.
- [x] The global chart cover includes the section degeneracy and the repeated
  multiplier energy.
- [x] Sturm counts make the candidate list complete.
- [x] Every candidate above `c6` is rejected by an unsquared determinant in
  two coordinate implementations.
- [x] The row-sum bound closes the interval above `16`.
- [x] The all-integer identities for `Q`, `tau`, and `K` prove the negative
  partner and rank two.
- [x] The proof does not call the squared level simple.
- [x] The isolating interval is named `J_6`; no occurrence incorrectly cites
  the reciprocal-quartic equation (1) as though it were that interval.

## Referee focus points

The logically delicate checks are the two inclusions in the half-line
essential-spectrum identity, the passage from a squared eigenvector to its
two unsquared branches, candidate completeness, chart coverage, and the
distinction between elimination candidates and physical unsquared zeros.
The first two are proved analytically in `ESSENTIAL_SPECTRUM_LEMMA.md`; the
certificate/checker list in `COMPUTER_ASSISTED_BOUNDARY.md` isolates the
finite exact checks used by the remaining points.
