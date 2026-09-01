# Residue-Two Block Schur Theorem

Let `n=8k+2`, `k>=6`, and use the standard one-G6, `alpha=+1` signing. Put

```text
M_k = 198 I - 25 A_(8k+2)^2.
```

Partition the vertices into a two-site block `V_0={0,1}` and `2k` four-site
blocks

```text
V_j={2+4(j-1),...,5+4(j-1)}, 1<=j<=2k.
```

Direct substitution of the one-G6 word gives a fixed diagonal block `D` and
alternating nearest-neighbour couplings `E_+`, `E_-`, all recorded in
`r2_block_riccati_template.json`. All other bulk blocks vanish. The only
non-nearest blocks are three fixed wrap-around couplings among
`V_0,V_1,V_(2k)`, also recorded there.

For a positive symmetric four-by-four block `X`, define

```text
F_+(X)=D-E_+^T X^(-1)E_+,
F_-(X)=D-E_-^T X^(-1)E_-,
Phi=F_- o F_+.
```

Each entry has the explicit rational form

```text
(det(X) D-E_±^T adj(X)E_±)_(ij)/det(X).
```

## Propagated dimension

The propagated state is a symmetric four-by-four matrix and hence has ten
coordinates. This is generically minimal for this Riccati formulation.
Indeed both `E_+` and `E_-` have determinant `25^4`, and

```text
D F_E(X)[H] = E^T X^(-1) H X^(-1) E.
```

For invertible `X`, this is an automorphism of the ten-dimensional vector
space of symmetric four-by-four matrices. Therefore no constant, zero, or
linear dependent coordinate can be removed from the general propagation
without first proving an additional invariant algebraic subvariety. The
previous observed low-rank numerical orbit is only a convergence feature of
one initial state, not a valid seven-dimensional state reduction.

## Exact reduction

Repeated block LDL congruence eliminates the interior four-site blocks. At
each step the next Schur pivot is exactly the appropriate `F_+` or `F_-`
iterate. Consequently `M_k` is positive definite if and only if every block
pivot in this alternating orbit is positive definite and the final fixed
boundary-core Schur complement is positive definite.

This is a purely algebraic all-`k` statement: it follows from the Schur
identity

```text
[X E; E^T Y] congruent diag(X, Y-E^T X^(-1)E)
```

applied inductively to the displayed block templates. No finite-order
spectral computation is part of this equivalence.

## Remaining analytic obligation

Construct a rational invariant domain for the alternating orbit of
`F_+`,`F_-`, prove each block stays positive, and prove the fixed
boundary-core Schur complement is positive on that domain. That would
establish `M_k>0` for every `k>=6` and remove the entire residue-two finite
LDL family.
