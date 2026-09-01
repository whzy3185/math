# Uniform Residue-Cap Program

## Three fixed-energy targets

For the structured one-, two-, and three-G6 finite-ring families, it is enough
to prove the fixed bounds

```text
T2 = 198/25,
T4 = 2679/338,
T6 = 5782/729.
```

Indeed these are exactly the rational benchmark lower bounds at the first
orders `50`, `52`, and `54`. The benchmark lower bound `8-200/n^2` is strictly
increasing, so a uniform estimate `rho(A_n)^2<T_r` closes the whole residue
class.

The exact checker reconstructs every structured matrix for `48<=n<240` and
proves

```text
T_r I-A_n^2 is positive definite
```

with the same `T_r` throughout each residue. All 72 matrices pass: 24 in each
nonzero residue. This is exact finite evidence for the uniform theorem, not
the desired all-length analytic proof.

## One-G6 symmetry reduction

For `n=8k+2`, the proved involution

```text
(K_n u)_i=(-1)^i u_(n-3-i)
```

satisfies `K_n^2=-I` and `K_n A_n=-A_n K_n`. Over `C`, split the space into
the `+i` and `-i` eigenspaces of `K_n`. If `j=n-3-i`, a normalized pair is

```text
u_i^+ = (e_i+i(-1)^i e_j)/sqrt(2),
u_i^- = (e_i-i(-1)^i e_j)/sqrt(2).
```

In these bases,

```text
A_n = [0 B_n^*; B_n 0],
A_n^2 = [B_n^*B_n 0; 0 B_nB_n^*].
```

The matrix `B_n` has size `n/2`, is complex symmetric, and has four nonzero
entries per generic row. Its interior coefficients have period four; all
nonreal coefficients are confined to a fixed boundary pattern. Thus the
residue-two theorem reduces to

```text
||B_n||^2 < 198/25  for every n=8k+2, n>=50.
```

This removes the multiplicity ambiguity and halves the transfer dimension.
The boundary magnetic flux prevents a complete real gauge, so a scalar
Perron/M-matrix argument is unavailable.

## Proposed analytic closure

At each fixed energy `T_r`, write `M_n=T_r I-A_n^2`. In an interior-first
ordering, `M_n` is a bandwidth-four matrix. Away from the finitely many
interfaces, exact Schur elimination is a period-eight matrix Riccati map.
The required proof has three components:

1. construct rational Loewner boxes around the attracting period-eight
   Riccati cycle;
2. verify that one bulk-cell map sends each box strictly into the next;
3. propagate the finite interface maps and prove the final boundary Schur
   complement positive for the minimum separations.

This would be an analytic proof with fixed rational matrix inequalities, not
an order-by-order enumeration. The current status is
`UNIFORM_CAP_EXACT_FINITE_VERIFIED_ANALYTIC_RICCATI_OPEN`.
