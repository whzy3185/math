# Referee Checklist

- [x] The triangle-flux word, quadrilateral-flux word, Bloch convention, and
  ordered basis are fixed before any calculation.
- [x] The fiber is Hermitian on the unit circle.
- [x] The determinant is reduced to one polynomial `P(y,c)` with
  `y=x^2` and `c=z+z^(-1)`.
- [x] The root `eta` is derived exactly, not fitted numerically.
- [x] The positive expansion excludes every `y>eta` for every
  `c in [-2,2]`.
- [x] Equality forces `c=2`, and on the unit circle this forces `z=1`.
- [x] The strict inequality `eta<8` is established by rational bounds.
- [x] The finite Bloch grids `z^L=alpha` are distinguished from the full unit
  circle.
- [x] Gap `g=4` is identified with the reference bulk, not called an
  abnormal interface.
- [x] No machine-generated decimal is used in the proof.

## Referee recomputation

It is enough to check two identities: the determinant of the printed fiber
and expansion (3) in `FULL_PROOF.md`. The remaining argument is immediate
from Hermiticity and positivity.
