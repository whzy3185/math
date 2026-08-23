# Eventual Failure for Every Even Order

For the antibalanced comparison family,

```text
rho_-(n)^2=4cos^2(pi/n)+4cos^2(2pi/n).
```

Since `sin x<=x` and `pi^2<10`,

```text
rho_-(n)^2 >=8-20pi^2/n^2 >8-200/n^2.
```

For residues two, four, and six, the constructions in the residue theorem
have minimum separation at least `n/4`. For `n>=2500`, the chosen IMS radius
satisfies `R>=D/8>=n/32`, and hence

```text
m_n^2 <=c6+576/R^2
      <=c6_upper+589824/n^2.
```

For residue zero, the exact period-eight family is bounded by `eta<c6`, so
the same weaker displayed estimate also holds. Exact rational arithmetic at
`n=2500` verifies

```text
c6_upper+589824/2500^2 < 8-200/2500^2.
```

Both sides improve monotonically in the required direction as `n` grows.
Therefore, for every even `n>=2500`,

```text
m_n^2<rho_-(n)^2,
```

and hence `m_n<rho_-(n)`. The threshold is explicit and rigorous; no claim
of sharp onset is made.

Status: `EVENTUAL_ALL_EVEN_PROVED`, with `N=2500`.
