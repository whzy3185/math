# Computer-Assisted Boundary

## Certified inputs

The proof imports three computer-assisted one-interface/Floquet facts:

1. the positive unsquared G6 root is simple and the squared `c6` eigenspace
   has rank two;
2. the complement of that full eigenspace lies below `c6-1/100`;
3. for all 32 combinations of Bloch phase, sign, and tail direction, the
   stable contraction is below `q_F=9/25` and the selected Floquet basis has
   condition number below `17`.

The finite exact object is

```text
research/proofs/task55/certificates/exact_2r_cluster.json.
```

## Analytic part after the inputs

The cutoff construction, tail summation, Gram estimate, lower count, IMS
identity, min-max upper count, Schur complement, and constants

```text
73, 1752, 3504, 3505, 1040, 1/400, 1/200, 400
```

are exact deductions printed in `FULL_PROOF.md`. No matrix eigensolve or
floating-point level count is used for a finite ring.

## Independent checker

The checker

```text
research/scripts/verify_target_a_task55_exact_2r.py
```

does not import the producer. It rebuilds the transfer matrices, outward
rational intervals, cofactor charts, symmetry controls, tail constants, Gram
bounds, IMS arithmetic, counting inequalities, Feshbach bounds, and scope
records. The focused suite

```text
research/scripts/test_target_a_task55_exact_2r.py
```

contains 29 passing tamper tests. The accepted integration status is
`INDEPENDENT_CHECKER_PASS`; legacy exact-`r`, `I_r`, `r x r`, and
`H_eff-zP` fields fail closed.

## Why the verification implies exact counting

The finite verification supplies uniform constants, not sampled eigenvalue
counts. Those constants feed two analytic dimension arguments: the residual
estimate forces at least `2r` window states, and the codimension-`2r`
quadratic-form cap permits at most `2r`. Equality of the two bounds proves the
exact count for every legal ring in the stated scope.

## Boundary and nonclaims

- Scope is exactly `r in {1,2,3}` and `D>=1040`.
- Eigenvalues are counted with multiplicity.
- Individual simplicity, nonzero leading interactions, and a universal
  interaction sign remain open.
- Full arbitrary-precision finite-matrix eigensolves are not proof inputs.
