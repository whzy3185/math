# Exact p<=24 Frontier Relative to c6

## Theorem

Up to dihedral equivalence, tau negation, primitive normalization, and zone
folding, the period-eight target is the only primitive periodic phase of
period at most 24 with `R(Q)<c6`. Every primitive non-target phase in this
range satisfies `R(Q)>c6`.

## Certificate mechanism

The inherited complete frontiers divide every orbit into an exact moment
exclusion, a target repetition, or a stored exact endpoint Rayleigh
certificate. Task 53 audited the old Rayleigh thresholds against the rational
upper endpoint for `c6`. Sixteen phase keys required new or stronger data:
the twelve primitive numerical sub-eight non-targets and four additional
low-period keys whose old witness crossed `eta` but not `c6`.

For each key the producer chooses `z` from `{1,-1,i,-i}`, rounds one discovery
eigenvector to a Gaussian integer vector, and stores

```text
||H_Q(z)v||^2/||v||^2 > c6_upper.
```

Acceptance uses only exact Gaussian integer arithmetic. The independent
checker rebuilds every Bloch matrix and quotient.

Status: `P24_C6_FRONTIER_PROVED` / COMPUTER_ASSISTED_PROVED.
