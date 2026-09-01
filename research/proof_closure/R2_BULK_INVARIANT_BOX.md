# Residue-Two Bulk Invariant Domain

Use the block maps `F_+`, `F_-` from `R2_BLOCK_SCHUR_THEOREM.md`. Define two
closed Loewner boxes

```text
B_i={X symmetric: L_i <= X <= U_i},  i=0,1,
```

where the explicit rational matrices `L_i,U_i` have denominator 500 and
Loewner radius `3/100`. They are stored directly in the exact verifier.

Exact rational LDL checks prove

```text
F_+(L0) >= L1,   F_+(U0) <= U1,
F_-(L1) >= L0,   F_-(U1) <= U0.
```

Since the Riccati maps are order preserving on positive definite matrices,
these four inequalities prove

```text
F_+(B0) subset B1,
F_-(B1) subset B0.
```

Starting at the exact first bulk block `D`, direct rational recurrence gives
membership in `B0` after four block pivots. Therefore all subsequent bulk
block Schur pivots are positive for every residue-two length.

This is an all-length analytic result with a fixed rational certificate. It
does not by itself prove positivity of the final cyclic boundary closure; that
is now the sole remaining residue-two finite-ring obligation.
