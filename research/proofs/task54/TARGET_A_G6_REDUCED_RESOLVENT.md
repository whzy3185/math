# Single-G6 Reduced Resolvent

Use the contour `Gamma: |z-c6|=1/300`. On the orthogonal complement of the
normalized G6 state, the spectral distance is at least

```text
1/100-1/300=1/150.
```

Thus the spectral theorem gives

```text
||Q6(H6-z)^(-1)Q6|| <=150.
```

For the spatial estimate, `H6` has range four and absolute row sum at most
16. Conjugation by `exp(theta X)`, with `theta=1/40000`, changes the operator
by at most

```text
16(exp(4theta)-1) <=16/9999 <1/600.
```

The weighted full resolvent is therefore bounded by 600. Contour integration
gives `|P6(i,j)|<=2 exp(-|i-j|/40000)`. Subtracting the rank-one pole from the
full resolvent yields the uniform reduced-kernel estimate

```text
|R6_red(z;i,j)| <=1200 exp(-|i-j|/40000).
```

All constants are deliberately conservative and exact.

Status: `G6_REDUCED_RESOLVENT_AND_DECAY_PROVED` /
COMPUTER_ASSISTED_PROVED after the certified isolation input; the resolvent
and decay estimates are analytic consequences.
