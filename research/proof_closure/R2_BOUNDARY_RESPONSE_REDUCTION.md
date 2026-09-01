# Residue-Two Boundary Response Reduction

Use the block partition of `R2_BLOCK_SCHUR_THEOREM.md`, with `V_0` of size
two and `V_1,...,V_m` of size four, where `m=2k`. Separate the fixed cyclic
wrap-around couplings from the open block chain.

After eliminating `V_1,...,V_(j-1)`, retain the following finite state:

```text
G_j : 2 x 2 left self-energy,
X_j : 4 x 4 current bulk pivot,
H_j : 4 x 4 right self-energy,
R_j : 2 x 4 left-to-current response,
W_j : 4 x 4 current-to-right response,
C_j : 2 x 4 direct left-to-right response.
```

All six matrices have dimensions independent of `k`. If `E_j` is the
alternating bulk coupling and `X_j` is positive, one block Schur elimination
gives the exact recurrences

```text
G_(j+1)=G_j-R_j X_j^(-1)R_j^T,
H_(j+1)=H_j-W_j^T X_j^(-1)W_j,
R_(j+1)=-R_j X_j^(-1)E_j,
W_(j+1)=-E_j^T X_j^(-1)W_j,
C_(j+1)=C_j-R_j X_j^(-1)W_j,
X_(j+1)=D-E_j^T X_j^(-1)E_j.
```

At the final block, replace `W_(m-1)` by the sum of its propagated response
and the fixed nearest-neighbour terminal coupling. The remaining six-by-six
Schur complement is

```text
[G  C; C^T H].
```

Therefore the residue-two theorem reduces to a fixed finite-dimensional
response recurrence. The bulk invariant boxes already prove `X_j>0` for all
large `j`; the remaining task is to bound `R_j,W_j` using the exact stable
multiplier estimate and prove the final six-by-six response matrix positive.

No finite order is used in this reduction. The formulas follow from repeated
application of the block Schur identity and the fixed bulk/boundary templates.
