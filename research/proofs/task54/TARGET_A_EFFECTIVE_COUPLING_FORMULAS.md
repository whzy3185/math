# Effective Coupling Formulas

For normalized truncated modes `u_i`, write `e_i=(H-c6)u_i`. The effective
entries are exactly

```text
(H_eff(lambda)-c6 P)_ij
= <u_i,e_j>
  - <e_i,Q(QHQ-lambda)^(-1)Qe_j>.
```

The first term is the direct two-tail interaction. The second propagates the
two residual tails through the complementary Green function. The decay
theorem and `||(QHQ-lambda)^(-1)||<=400` imply, uniformly for fixed `r`,

```text
|<u_i,e_j>| = O((9/25)^distance(i,j)),
|<e_i,Q(QHQ-lambda)^(-1)Qe_j>| = O((9/25)^(2L)).
```

On a ring the direct term is the sum of the two arc contributions. Their
relative sign records holonomy and orientation; suppressing that sign would
not be invariant under the legal gauge choices.

Status: `EFFECTIVE_COUPLING_NORM_FORMULAS_PROVED`; leading coefficients remain
OPEN/HIGH_PRECISION.
