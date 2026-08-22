# Task 49 Uniform-Bound Reconnaissance

## Definitions

For the single-slip families, `bulk_cells` is the number of complete
period-eight cells between the defect core and the finite-ring closure in the
chosen gap encoding.  Thus the normalization uses that integer, rather than
the ambiguous surrogate `n/8`.  The constants `c6`, `c10`, `mu6`, and `mu10`
are the Task 48A high-precision infinite-interface values.

For two gap-6 slips, `L` and `M-L` are the two arc lengths measured in complete
period-eight bulk cells.  The preferred geometries in the two even residue
classes are evaluated for both finite-ring holonomies.

## Observations

| Family | Resolved rows | Below double resolution | observed sup Q | 1.1 safety candidate | 2x safety candidate |
|---|---:|---:|---:|---:|---:|
| G6 | 15 | 3 | 0.2550518878 | 0.2805570766 | 0.5101037757 |
| G10 | 14 | 3 | 0.1367718941 | 0.1504490835 | 0.2735437881 |

The resolved normalized errors remain bounded over onset, medium, and
approximately 128-, 256-, 512-, and 1024-site scales.  Rows whose direct FP64
correction is no longer resolved are retained and labeled
`BELOW_DOUBLE_RESOLUTION`; they are not treated as zero observations.

For the two-interface families, the two-tail normalization has coefficient of
variation `0.6653158639`, compared with `0.7402172143` for a one-tail
normalization.  Its observed normalized supremum is `0.04211546072` over 28
preferred-geometry rows.  The two-tail form also matches the finite-ring
mechanism: either defect can communicate through either bulk arc.

## Model Decision

The data support the following proof targets:

\[
 |R_n-c_e|\leq C_e|\mu_e|^{k},\qquad e\in\{6,10\},
\]

and

\[
 |R_{L,M}-c_6|\leq C\bigl(|\mu_6|^L+|\mu_6|^{M-L}\bigr).
\]

The conservative `2x` constants are recommended as starting values for a
computer-assisted interval proof.  They are empirical envelope candidates,
not theorem constants.

## Classification

- Single interface: `SIMPLE_SINGLE_TAIL_BOUND_SUPPORTED`
- Two interfaces: `TWO_TAIL_BOUND_SUPPORTED`
- Gate: `UNIFORM_BOUND_TEMPLATE_FOUND`

Raw data are in `uniform_bounds/`; the deterministic builder is
`research/scripts/target_a_task49_uniform_crossings.py`.

## Evidence Boundary

Bounded normalized errors select an analytic inequality template.  They do not
prove uniformity beyond the sampled orders.  A proof still needs a transfer
contraction or interval-Evans estimate with an explicit constant.
