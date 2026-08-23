# Geometric Resolvent Cross-Check

On `|z-c6|=1/300`, use the local single-interface reduced Green function and
the translated bulk Green functions from the Task 54 decay theorem. A
two-overlap partition gives the standard geometric-resolvent parametrix

```text
R_app(z)=sum_j chi_j R_j(z) chi_j.
```

The error consists only of finite-range commutators and exponentially small
interface tails. Its norm tends to zero as transition width and interface
separation tend to infinity. Hence `I+K_L(z)` is invertible uniformly on the
contour for sufficiently large separation.

This supplies an independent resolvent existence check. Rank is taken from
the complement-gap/min-max proof, not inferred from the nonprojective raw
parametrix. This avoids the invalid shortcut of assigning a rank directly to
`sum chi_j P_j chi_j`.

Status: `GEOMETRIC_RESOLVENT_CROSSCHECK_PROVED`; primary rank proof is the
complement-gap theorem.
