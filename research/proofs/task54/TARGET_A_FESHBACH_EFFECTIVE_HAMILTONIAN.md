# Feshbach-Schur Effective Hamiltonian

> **Application superseded.** The abstract Gram-orthogonalized Feshbach
> identity below is correct, but the selected space has dimension `r` while
> the local G6 squared eigenspace has dimension two. The asserted complement
> inverse and `r x r` application are not proved. A corrected application
> must use `2r` columns.

For `r in {1,2,3}`, put the truncated modes in the column map `Phi`, let
`G=Phi^*Phi`, set `U=Phi G^(-1/2)`, and let `P=UU^*` project onto their span.
Set `Q=I-P`. For `|lambda-c6|<=1/400`, the complement theorem gives

```text
||(QHQ-lambda)^(-1)|| <=400.
```

Define

```text
H_eff(lambda)=U^*HU-U^*HQ(QHQ-lambda)^(-1)QHU.
```

Block Gaussian elimination by bounded invertible triangular factors shows
that `H-lambda` and `H_eff(lambda)-lambda I` have equal nullity and the same
local algebraic multiplicity.

Writing `E=(H-c6)Phi`, its exact orthonormal-coordinate form is

```text
H_eff(lambda)-c6 I
=G^(-1/2)Phi^*E G^(-1/2)
 -G^(-1/2)E^*Q(QHQ-lambda)^(-1)QE G^(-1/2).
```

Use `L_site=floor(D/4)-12` and
`ell=floor(L_site/8)`. The cutoffs start changing beyond site distance
`L_site+4`; since `9/25` is a period-eight-cell rate, range four and G6
localization give `||(H-c6)u_j||=O_r((9/25)^ell)`. Hence

```text
H_eff(lambda)=c6 I_r+T_1+R_2(lambda),
||T_1||=O_r((9/25)^ell),
||R_2(lambda)||=O_r((9/25)^(2ell)).
```

The big-O constants are not explicit. `T_1` retains both ring paths,
orientation, and holonomy. No universal leading scalar coefficient or
simplicity theorem is asserted.

The coordinate formulas are conditional on a valid complementary inverse.
Current problem-specific status: `OPEN_PENDING_2R_COMPLEMENT`; the abstract
Schur-complement identity remains proved.
