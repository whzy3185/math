# Target A Floquet Phase and the mod16 Signal

## Full Multipliers

At the Task 48A interface levels, the period-eight bulk monodromy has two
stable and two unstable multipliers.  All four are positive real in both
cases, and the stable/unstable pairs are reciprocal to the recorded
high-precision tolerance.

| Interface | Stable multipliers (magnitudes) | Unstable multipliers |
|---|---|---|
| G6 | 0.122279..., 0.350506116132922... | 2.853017..., 8.178016... |
| G10 | 0.119209..., 0.258502064633171... | 3.868..., 8.388... |

The exact values and arguments are recorded in
`interface_mechanism/floquet_multipliers_full.json`.

## Two-Interface Splitting

The finite-ring eigenvalue condition is evaluated through the four-dimensional
twisted Evans determinant

\[
 E_{n,\alpha}(\lambda)=\det(M_n(\lambda)-\alpha I_4).
\]

FP64 finite matrices locate the two interface levels.  Their roots are then
refined independently at 80, 120, and 160 decimal digits.  Across `L=1,...,12`
and both holonomies, the median successive splitting ratio over the resolved
tail is `0.3507688884`, compared with
`mu6=0.3505061161`.  Two representative full arbitrary-precision finite-matrix
eigensolves agree with the Evans roots to better than `3e-79`.  The maximum
FP64-to-160-digit squared-level difference is `1.58e-14`.

This computation follows the dimension-reduced route.  Full arbitrary-
precision matrix diagonalization is not the primary algorithm and is retained
only for the two representative checks.

## Phase and Holonomy

Because the relevant slow multiplier is positive, `mu6^L` has no alternating
sign.  Floquet phase alone therefore cannot produce the observed switch
between symmetric `4 mod 16` and one-cell-shifted `12 mod 16` geometries.
Finite-ring holonomy and the geometry of the two matching paths remain
essential.  The infinite single-interface constant itself has no finite-ring
holonomy.

## Decision

`PARTIAL_PHASE_EXPLANATION`

The magnitude explains the exponential scale and the splitting ratio.  It
does not by itself explain branch selection modulo 16.  An exact two-defect
matching expansion must retain both arc amplitudes and the twisted closure.
