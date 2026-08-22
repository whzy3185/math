# Target A Finite-Size Asymptotics

The structured rows near orders 128, 256, 512, and 1024 are consistent with a
correction governed by the slow G6 Floquet multiplier raised to the shortest
interface separation.  Residues four and six require a matrix-valued cluster,
not a scalar correction.

Several late two-/three-interface corrections fall below reliable FP64
resolution.  They are marked `BELOW_DOUBLE_RESOLUTION`; Task 51 neither extends
`n` nor fits constants from those rows.  A theorem would need high-precision
multi-interface Evans roots, an exact leading effective matrix, and a uniform
remainder.  The mod16 prefactor remains geometry-, orientation-, and
holonomy-dependent.

Status: limiting constants `STRONGLY_SUPPORTED`; leading coefficients and
finite-size expansion `OPEN`.
