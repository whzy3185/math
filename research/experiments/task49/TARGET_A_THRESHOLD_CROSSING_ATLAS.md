# Target A Threshold-Crossing Atlas

Let

\[
 T_n=\rho_-^2(n)=4\left(\cos^2\frac{\pi}{n}+\cos^2\frac{2\pi}{n}\right).
\]

The atlas compares `T_n` with the squared spectral radius of four prescribed
phase-slip families.  Numerical rows use dense symmetric eigensolves.  Every
row labeled `CERTIFIED_COUNTEREXAMPLE` also has an exact integer Rayleigh upper
certificate for the candidate matrix together with a rigorous elementary
lower bound for `T_n`.  Pre-crossing rows are deliberately reported only as
`NUMERICALLY_ABOVE_THRESHOLD` because no expensive exact lower comparison for
their spectral radius was attempted.

| Even class | Explicit family | Last numerical pre-crossing | First numerical crossing | First exact crossing |
|---|---|---:|---:|---:|
| 2 mod 8 | single gap-6, alpha=+1 | 42 | 50 | 50 |
| 6 mod 8 | single gap-10, alpha=+1 | 86 | 94 | 94 |
| 4 mod 16 | symmetric two gap-6, alpha=-1 | 36 | 52 | 52 |
| 12 mod 16 | one-cell-shifted two gap-6, alpha=-1 | 44 | 60 | 60 |

For the shifted family, the order-28 geometry is valid but remains above the
threshold numerically.  Order 44 is likewise above; order 60 is the first
certified crossing.  For gap-10, the previously delicate 86 versus 94
transition is resolved in the same way.

The asymptotic estimate substitutes the measured interface limit and Floquet
tail into `R_n=c+a mu^k` and compares it with `T_n`.  Its predicted transition
window contains the observed first crossing for every family.  This agreement
is explanatory evidence, while the exact first-crossing rows provide the
finite claims.

The phrase "first crossing" here always means first crossing of the named
explicit family.  It is not a minimality theorem within the residue class.

Raw data: `threshold_crossings/threshold_crossings.csv` and
`uniform_and_crossing_summary.json`.
