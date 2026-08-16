# Periodic Operator Equivalences and Zone Folding

Status: **TARGET_A_PERIODIC_OPERATOR_EQUIVALENCES_PROVED**

## Theorem

Let `tau` be a `p`-periodic Hamilton-gauge word and let

```text
(A_tau x)_i=x_{i-1}+x_{i+1}+tau_{i-2}x_{i-2}+tau_i x_{i+2}.
```

1. Translating `tau` by `r` is conjugation of `A_tau` by the lattice shift.
2. Reflecting the lattice sends `tau_i` to `tau_{-i-2}` and conjugates the
   corresponding operators. On flux words this is `Q_i -> Q_{-i-3}`.
3. Replacing `tau` by `-tau` gives
   `A_{-tau}=-D A_tau D`, where `(Dx)_i=(-1)^i x_i`; hence the squared
   infinite-volume spectrum is unchanged. For odd displayed cells this
   normalization changes the fiber parameter by `z -> -z`, as recorded in
   the general Bloch constructor.
4. If `tau` has primitive period `q` and is displayed in a repeated cell
   `p=mq`, then

```text
H_p(z)  is unitarily equivalent to
direct_sum_(w^m=z) H_q(w).
```

Consequently translation, reflection, global `tau` negation, and unit-cell
repetition preserve `R(Q)`. In particular the `p=16` target row is not a
second minimizer: it is the doubled-cell representation of the primitive
period-8 phase and has exactly the same `R(Q)=eta`.

## Proof

For translation, let `(T_r x)_i=x_{i-r}`. Direct substitution gives
`T_r A_tau T_r^{-1}=A_{tau'}` with `tau'_i=tau_{i-r}`. For reflection let
`(Jx)_i=x_{-i}`. Then `J A_tau J=A_{tau'}` with
`tau'_i=tau_{-i-2}`. Both are unitary conjugacies on `ell^2(Z)`.

For negation, the endpoints of a step-one edge have opposite `D` signs and
the endpoints of a step-two edge have equal `D` signs. Thus
`-D A_tau D` leaves step-one coefficients equal to one and negates exactly
the step-two coefficients.

For zone folding write an index in the repeated cell as `i=r+kq`, with
`0<=r<q` and `0<=k<m`. On the `w`-eigenspace of translation by `q`, put

```text
x_{r+kq}=w^k v_r.
```

The repeated boundary condition `x_{i+p}=z x_i` is equivalent to `w^m=z`.
Because every coefficient of `A_tau` is `q`-periodic, each of the four local
transitions factors out `w^k`, and the remaining action on `v` is exactly
`H_q(w)`. The `m` roots of `w^m=z` give mutually orthogonal eigenspaces of
the unitary internal cell shift and account for all `mq` dimensions. This
proves the direct sum and preserves multiplicity.

## Exact Audit

The independent checker works at the integer transition-kernel level and
does not import the low-period classifier. For every legal flux word with
`1<=p<=16` it reconstructs both lifts, checks the translation, reflection,
and negation intertwining identities, computes primitive `tau` period, and
checks every local transition in every nonprimitive displayed cell against
the zone-folded primitive action. This includes all repeated rows in the
2626-orbit table, not only the target row.

This theorem concerns infinite-volume periodic phases. It does not identify
finite holonomy sectors unless the discrete relation `z^L=alpha` is also
imposed.

`TARGET_A_PERIODIC_OPERATOR_EQUIVALENCES_PASS`
