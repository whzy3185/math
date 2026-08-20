# Appendix B. Exact Classification and Residual Certificates

## B.1 Period-eight orbit table

Use `0` for negative flux and `1` for positive flux. The 128 legal period-eight
words form 18 dihedral orbits. The structural proof in Section 6 gives the
following exact classification.

| canonical `Q` | `d` | orbit size | primitive `tau` period | exact conclusion |
|---|---:|---:|---:|---|
| `00000000` | 0 | 1 | 2 | `R=8` |
| `00000011` | 2 | 8 | 8 | `R>8` |
| `00000101` | 2 | 8 | 8 | `R>8` |
| `00001001` | 2 | 8 | 8 | `R>8` |
| `00001111` | 4 | 8 | 8 | `R>8` |
| `00010001` | 2 | 4 | 8 | `R=eta` |
| `00010111` | 4 | 16 | 8 | `R>8` |
| `00011011` | 4 | 8 | 8 | `R>8` |
| `00100111` | 4 | 8 | 8 | `R>8` |
| `00101011` | 4 | 16 | 8 | `R>8` |
| `00101101` | 4 | 8 | 8 | `R>8` |
| `00110011` | 4 | 4 | 4 | `R>8` |
| `00111111` | 6 | 8 | 8 | `R>8` |
| `01010101` | 4 | 2 | 4 | `R>8` |
| `01011111` | 6 | 8 | 8 | `R>8` |
| `01101111` | 6 | 8 | 8 | `R>8` |
| `01110111` | 6 | 4 | 8 | `R>8` |
| `11111111` | 8 | 1 | 1 | `R>8` |

The orbit sizes sum to 128. The unique sub-eight orbit is `00010001`, and the
unique equality orbit at eight is `00000000`.

## B.2 Five low-period residual certificates

For each row below, `H=H_Q(z)` and the listed integer vector is denoted by
`v`. Direct matrix multiplication gives the stated rational quotient
`r=||Hv||^2/||v||^2`.

| `p`, `Q` | `z` | vector `v` | `r` |
|---|---:|---|---:|
| 10, `0000010001` | -1 | `(3,2,-3,3,0,5,-5,5,-5,2)` | `1066/135` |
| 12, `000000010001` | 1 | `(-5,-5,-5,-1,-4,-2,-3,0,-2,-2,0,-4)` | `1022/129` |
| 14, `00000000010001` | 1 | `(-1,2,0,2,-1,3,-2,3,-1,4,-4,4,-3,0)` | `119/15` |
| 14, `00010010001001` | 1 | `(-4,-5,-4,0,-2,0,1,0,-2,0,-4,-5,-4,-6)` | `1270/159` |
| 16, `0000000000010001` | 1 | `(-5,-5,-5,-1,-4,-2,-4,-1,-3,-1,-2,0,-2,-2,0,-4)` | `1204/151` |

All five quotients exceed four. For the transformation

```text
u=((r-4)^2-10)/2,
```

the exact comparison data are:

| `r` | `u` | `u^2-5` |
|---:|---:|---:|
| `1066/135` | `47213/18225` | `568314244/332150625` |
| `1022/129` | `44813/16641` | `623590564/276922881` |
| `119/15` | `1231/450` | `502861/202500` |
| `1270/159` | `74573/25281` | `2365487524/639128961` |
| `1204/151` | `65995/22801` | `1755912020/519885601` |

Every entry in the last two columns is positive. Because `r>4`, the branch
argument (8.6) proves `r>eta`, and Rayleigh's principle proves `R(Q)>eta`.
These five computations are the only individual endpoint certificates needed
by the compressed proof of Theorem F.

## B.3 The order-32 positive-definiteness certificate

For the witness (3.1), form `M=1561I-200A_32^2`. The exact certificate consists
of the 32 positive pivots of rational `LDL^T` elimination. Fraction-free
Bareiss elimination independently produces the leading principal minors, and
the cumulative products of the `LDL^T` pivots agree with those minors. This
double route verifies both arithmetic consistency and the hypothesis of
Sylvester's criterion. The conclusion is the strict inequality
`rho(A_32)^2<1561/200`; no approximation to an eigenvalue is part of the
certificate.
