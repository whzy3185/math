# Fixed-r Method Selection

Scores use 1 (poor) through 5 (strong).

| Method | Counting | Localization | Error | Holonomy | r=3 | Exact | Interval | Clarity | Risk |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Piecewise Evans / dichotomy | 3 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 2 |
| Feshbach-Schur / Grushin | 3 | 5 | 4 | 4 | 5 | 3 | 4 | 5 | 3 |
| Matrix Weyl / DtN | 4 | 4 | 5 | 4 | 5 | 4 | 5 | 4 | 3 |
| Boundary triple | 4 | 4 | 5 | 4 | 5 | 4 | 4 | 3 | 3 |
| Matrix Pruefer / Maslov | 5 | 3 | 3 | 4 | 4 | 2 | 4 | 3 | 4 |
| Grassmannian / Pluecker | 3 | 5 | 5 | 4 | 5 | 5 | 5 | 3 | 3 |
| Jost / scattering | 3 | 5 | 5 | 5 | 5 | 3 | 4 | 5 | 3 |

Primary method: piecewise Evans/exponential dichotomy, expressed on
`Gr(2,4)` through exterior-square coordinates. This is one method rather
than two competing formalisms: the Grassmannian representation removes
basis singularities from the Evans propagation.

Secondary checker: finite-ring transfer Evans determinant, seeded only by
ordinary finite-matrix eigenvalues. It supports validated root counting and
retains holonomy exactly. A Pruefer/Maslov implementation was not selected
because no existing exact kernel supports it and the current blocker is
global counting, not local mode existence.

Jost/scattering and Weyl/DtN remain equivalent future presentations. The
Jost language is particularly clear for interaction coefficients, while
DtN is attractive for a future global cap. Neither was promoted to a second
primary implementation in this task.

Status: `PRIMARY_PIECEWISE_EVANS_SECONDARY_FINITE_RING_EVANS_SELECTED`.
