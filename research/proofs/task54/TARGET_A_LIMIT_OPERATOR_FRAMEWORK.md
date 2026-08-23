# Pointed Limit-Operator Framework

Let `A_j` be legal signed adjacency operators on `C_(n_j)(1,2)`, with
`n_j` tending to infinity, and put `H_j=A_j^2`. After choosing roots,
orientations, and local tree gauges, the lifted coefficients lie in the
finite alphabet `{+1,-1}`.

## Pointed compactness

A diagonal subsequence has a bi-infinite coefficient word `tau_infinity`
that agrees with the lifted finite words on every fixed window for all
sufficiently large `j`. It defines a bounded self-adjoint operator
`A_infinity` on `ell^2(Z)` and the range-four nonnegative operator
`H_infinity=A_infinity^2`.

For every finitely supported vector `v`, its canonical embedding `J_j v`
around the selected root satisfies

```text
<J_j v,H_j J_j v>=<v,H_infinity v>
```

eventually. Since finitely supported vectors are dense,

```text
||H_infinity|| <=liminf_j ||H_j||
                =liminf_j rho(A_j)^2.
```

This is the required direction: a high-energy pointed limit forces a lower
bound on the finite-ring spectral tops. Pointed convergence does not provide
the reverse limsup inequality.

## Conditional liminf criterion

If every putative contradiction sequence in a fixed nonzero even residue
admits roots and a pointed limit with spectral top at least `c6`, then its
finite spectral tops have liminf at least `c6`. In particular this applies
when the sequence contains G6 neighborhoods whose radii tend to infinity,
using the finitely supported truncated G6 state.

It does not yet apply to arbitrary legal signings.

Status: PROVED for pointed compactness and the spectral-transfer inequality;
the unrestricted common liminf remains OPEN.
