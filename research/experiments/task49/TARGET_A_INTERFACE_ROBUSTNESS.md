# Target A Interface Robustness Archive

The Task 49 interface checks separate physical constants from representation
choices and finite-ring boundary data.

## Representation Checks

- Four period-eight cut shifts recover the same finite-ring level within
  `1e-9` for G6 and G10.
- Reversal of the ring/interface orientation recovers the same level.
- Dense and sparse finite-matrix routes agree on the selected finite states.
- The finite-ring 4x4 Evans roots agree with two representative 80-digit full
  matrix eigensolves to better than `3e-79`.
- The bulk Floquet multipliers occur in reciprocal pairs to high precision.

The two finite holonomies are retained as boundary conditions.  They are not
attributed to the infinite-interface constants.

## Localization Checks

Raw signed eigenvectors, site amplitudes, cell norms, slip locations, noise
floor estimates, and `A^2` residuals are archived for G6 at orders 258, 514,
and 1026 and for G10 at orders 254, 510, and 1022.  Left and right tails are
fitted separately on five fixed windows: 2--8, 2--10, 2--12, 3--10, and
3--12 cells.

All recorded fits have `R^2>0.98`.  The maximum fitted-multiplier distance from
the relevant slow bulk multiplier is `0.0308631`; the variation is largest in
the shortest/noisiest windows and does not change the decay classification.

## Decision and Boundary

- Representation invariance: pass
- Solver cross-check: pass
- Localization: `LOCALIZATION_ROBUST`
- Combined gate: `INTERFACE_MECHANISM_READY_FOR_PROOF`

The gate means that the numerical mechanism is stable enough to design a
proof.  It does not assert an exact interface theorem or exact Evans zero.
