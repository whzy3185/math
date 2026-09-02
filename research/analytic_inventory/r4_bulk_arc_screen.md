# Residue-four bulk-arc screen

## Exact template result

For the standard two-G6 residue-four construction at the cap
\(T_4=2679/338\), one four-site boundary block followed by eight-site cells
reveals exactly two bulk arc templates.  Exact Fraction block extraction at
orders \(76,92,108\) gives the same ordered pair of diagonal/coupling
templates in every case.

Thus a future R4 proof needs two fixed eight-by-eight Riccati maps, not a
growing collection of local matrix types.

## Numerical route screen only

Iterating the two extracted Riccati maps from their natural diagonal pivots
at orders 76, 92, and 108 produced positive attracting pivots, with observed
smallest eigenvalues about \(0.3003\) and \(0.3058\).  This is a feasibility
screen only.  It is not an exact positivity theorem and is not manuscript
evidence.

## Next proof task

For each of the two fixed arc maps, find rational invariant boxes and a local
Lyapunov metric.  Then derive the finite interface/boundary response system
joining the arcs.  Only after the joint terminal core has a rational positive
margin may the R4 cap theorem be claimed.

## Metric-complexity screen

The two arc linearizations have observed spectral radius about \(0.10114\),
but neither admits a useful Euclidean or diagonal-weight contraction.  The
screen found:

| Arc | Euclidean squared norm bound | diagonal-metric bound | dense Lyapunov squared bound |
|---|---:|---:|---:|
| I | \(23.79\) | \(8.32\) | \(0.9604\) |
| II | \(2.30\) | \(1.93\) | \(0.6993\) |

These are numerical route screens, not proof certificates.  Their practical
meaning is that a direct R4 continuation would require a dense
36-dimensional Lyapunov certificate, especially for arc I, unless a new
symmetry or low-rank coordinate reduction is found.

For an analytic-first article this fails the current simplicity threshold.
R4 remains a research direction, but is removed from the near-term mainline
until a structural reduction replaces the dense metric.
