# Feshbach-Schur Effective Hamiltonian

Let `P` project onto the normalized disjoint truncated G6 modes and set
`Q=I-P`. For `|lambda-c6|<=1/400`, the complement theorem gives

```text
||(QHQ-lambda)^(-1)|| <=400.
```

Define

```text
H_eff(lambda)=PHP-PHQ(QHQ-lambda)^(-1)QHP.
```

Block Gaussian elimination is by bounded invertible triangular factors.
Therefore `H-lambda` and `H_eff(lambda)-lambda P` have equal nullity and the
same local algebraic multiplicity. This is the exact, multiplicity-preserving
near-`c6` eigenvalue equivalence.

In the truncated-mode basis, exponential localization gives

```text
H_eff(lambda)=c6 I_r+T_1+R_2(lambda),
||T_1||=O_r((9/25)^L),
||R_2(lambda)||=O_r((9/25)^(2L)).
```

`T_1` contains direct overlaps along both ring arcs, with orientation and
holonomy retained. The second-order term is the complement Green-function
correction. No exact leading scalar coefficient or simplicity assertion is
made.

Status: `FESHBACH_EFFECTIVE_MATRIX_PROVED` / PROVED.
