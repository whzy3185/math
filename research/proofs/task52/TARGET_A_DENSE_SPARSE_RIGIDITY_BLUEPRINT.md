# Dense-Sparse Rigidity Blueprint at c6

## Exact weighted moments

For `k=1,...,5` define

```text
F_k^(c6)=M_(k+1)-c6 M_k.
```

If `R^2<=c6`, the spectral measure identity gives
`F_k^(c6)<=0`. Substituting the exact closed-walk expansions gives local
translation-invariant forms over `Q(c6)`. Their union supports contain
`2,4,10,27,76` motif classes for `k=1,...,5`. Every coefficient is stored
as `a+b*c6`; no floating coefficient enters the artifact. A bounded search
of small rational combinations found no low-dimensional positivity
decomposition, so generation stops at M6.

## Exact finite low-energy grammar

For support lengths 6 through 10, every `tau` window was tested against the
deterministic integer Rayleigh-vector family. A window is excluded only when
its exact rational quotient exceeds the rational upper endpoint for `c6`.
At support length 10, 3768 of 4096 `tau` windows are excluded and 164
distinct length-11 `Q` windows survive. Their overlap automaton has 105 nodes
and 164 edges. It admits 48 primitive cycles through period 16, including
the period-eight bulk cycle.

Thus the current grammar is exact finite evidence but weak: it does not force
a bulk-plus-slip language and does not supply a positive-density defect
penalty.

## Truncated-interface lower bound

Suppose a legal finite configuration contains an `L`-cell neighborhood that
is exactly gauge-equivalent to the G6 interface. Let `psi` be the normalized
exact G6 eigenstate of `A^2` and let `chi_L psi` be its truncation inside that
neighborhood. Finite propagation range and the Task 50 decay estimate imply

```text
||(A^2-c6)chi_L psi|| <= C (9/25)^L,
||chi_L psi|| >= 1-C (9/25)^L.
```

The Rayleigh quotient, or equivalently the distance from `c6` to the finite
spectrum, therefore gives

```text
rho(A)^2 >= c6-C' (9/25)^L.
```

The constants are absolute after fixing the local gauge. This theorem is a
lower bound whenever an actual G6 neighborhood is present; it does not prove
that every sparse near-minimizer contains such a neighborhood.

## Future dichotomy

The desired proof architecture is:

```text
positive bad-gap density
    -> moment/motif lower bound above c6,
sparse bad-gap density
    -> pointed local limits and finite interface clusters
    -> fixed-defect lower bounds,
```

followed by concentration compactness. Task 52 proves the weighted forms,
the finite grammar, and the truncated G6 lemma. The dense-defect bound,
sparse local-limit classification, and global liminf remain OPEN.

Artifacts:

- `../../experiments/task52/c6_weighted_moments.json`;
- `../../experiments/task52/c6_low_energy_grammar.json`.

Status: `C6_RIGIDITY_FRAMEWORK_PARTIAL_TRUNCATED_G6_LOWER_BOUND_PROVED`.
