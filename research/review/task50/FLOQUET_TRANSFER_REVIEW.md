# Task 50 Floquet/Transfer Review

## Findings

### BLOCKER 1: no invariant cone for the finite-closure recurrence

The exterior-power reduction gives an exact order-nine recurrence in the
number of bulk cells.  After `y=8+u`, its coefficients have strict alternating
signs.  The first nine closure polynomials have a common strict sign, but the
naive coefficient cone is not invariant under this recurrence.  An invariant
cone, block-Riccati inequality, or equivalent resolvent estimate is required
before extrapolating to every cell count.

### MINOR 1: cut conventions must accompany every transfer product

The exact files do this correctly.  The paper should preserve the order
`T_{stop-1}...T_start`, distinguish the G6 cuts `[-8,14]` from the G10 cuts
`[-8,18]`, and define cell distance `k` by the gap word rather than `n/8`.

## Accepted Components

Direct multiplication reproduces the reciprocal quartic.  The substitution
`w=z+z^{-1}` and discriminant are exact.  The rational inequalities prove all
four relevant multipliers positive real, with reciprocal pairing and explicit
stable bounds.  Both finite holonomies appear in the twisted closure.

## Verdict

- BLOCKER: 1
- MAJOR: 0
- MODERATE: 0
- MINOR: 1
