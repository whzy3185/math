# Effective Coupling Formulas

Put the truncated modes in `Phi`, let `G=Phi^*Phi`, define the orthonormal
column map `U=Phi G^(-1/2)`, and write `E=(H-c6)Phi`. Use
`ell=floor((floor(D/4)-12)/8)`. The effective matrix is exactly

```text
H_eff(lambda)-c6 I
=G^(-1/2)Phi^*E G^(-1/2)
 -G^(-1/2)E^*Q(QHQ-lambda)^(-1)QE G^(-1/2).
```

The first term is the direct two-tail interaction. The second propagates the
two residual tails through the complementary Green function. The decay
theorem and `||(QHQ-lambda)^(-1)||<=400` imply, uniformly for fixed `r`,

```text
|<u_i,e_j>| = O((9/25)^ell),
|<e_i,Q(QHQ-lambda)^(-1)Qe_j>| = O((9/25)^(2ell)).
```

On a ring the direct term is the sum of the two arc contributions. Their
relative sign records holonomy and orientation; suppressing that sign would
not be invariant under the legal gauge choices.

Status: `EFFECTIVE_COUPLING_NORM_FORMULAS_PROVED` /
COMPUTER_ASSISTED_PROVED after inherited isolation; leading coefficients
remain OPEN/HIGH_PRECISION.
