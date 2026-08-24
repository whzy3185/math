# Exact `2r` Cluster for Separated G6 Interfaces

## Hypotheses

Let `H=A^2` be a legal finite-ring squared signed adjacency obtained from the
period-eight reference phase by inserting exactly `r in {1,2,3}` elementary
G6 interfaces. Both interface orientations and both Hamilton holonomies are
allowed. Let `D` be the minimum cyclic site distance between consecutive
interfaces; for `r=1`, it is the length of the bulk return arc. Assume

```text
D>=1040.
```

Set

```text
S=floor(D/4),
L_site=S-12,
ell=floor(L_site/8),
q_F=9/25.                                             (1)
```

## Exact-count theorem

The fixed near-edge window contains exactly `2r` squared eigenvalues counted
with algebraic multiplicity:

```text
rank 1_[c6-1/400,c6+1/400](H)=2r.                    (2)
```

If these eigenvalues are listed with multiplicity as
`lambda_1,...,lambda_(2r)`, then

```text
|lambda_j-c6|<3505 r q_F^ell,
1<=j<=2r.                                             (3)
```

No assertion of individual simplicity is made.

## Feshbach theorem

There is a canonical `2r`-dimensional quasimode space with an orthonormal
coordinate map `U:C^(2r)->C^n`. Let `P=UU^*` and `Q_perp=I-P`. For
`|z-c6|<=1/400`, with the inverse taken on `ran Q_perp`, define

```text
H_eff(z)=U^*HU-U^*H Q_perp
         (Q_perp H Q_perp-z)^(-1) Q_perp H U.         (4)
```

Then the finite-ring eigenvalue equation in the window is

```text
det(H_eff(z)-z I_(2r))=0.                             (5)
```

Moreover

```text
H_eff(z)=c6 I_(2r)+T_1+R_2(z),
||T_1||<=3504 r q_F^ell,
||R_2(z)||<r q_F^ell.                                (6)
```

## Historical correction

Each infinite G6 interface contributes two squared modes, not one. Therefore
the accepted cluster dimension, complement codimension, and Feshbach
dimension are all `2r`. The older exact-`r`, codimension-`r`, and unrestricted
`r x r` formulations are false as stated and are not hypotheses or
consequences of this theorem.
