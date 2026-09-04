# Period-eight manuscript dependency map

## Main theorem

For every integer `L >= 4`, the explicit alpha = +1 period-eight signing on
`C_(8L)(1,2)` has every squared Hermitian eigenvalue strictly below

`4 + 2 cos(pi/(4L)) + 2 cos(pi/(2L))`,

the squared twisted benchmark.  Hence its spectral radius is strictly smaller
than that benchmark in the standard Hermitian spectral interpretation.

## Human-readable chain

```text
Hamilton gauge + period-eight word
  -> finite cell decomposition
  -> H(z), z^L = alpha
  -> chiral 8x8 -> 4x4 -> 2x2 reduction
  -> P(lambda^2, z + z^{-1}) = 0
  -> P(y,c) > 0 for y >= 1561/200 and c <= 2
  -> lambda^2 < 1561/200
  -> 1561/200 < twisted benchmark squared
  -> strict comparison.
```

## Lean coverage

`alpha = +1` is the frozen formal scope.  The kernel includes finite matrix
reindexing, finite cells, ZMod DFT, nonzero fiber extraction, the fiber bound,
Hermitian eigenbasis, and the final all-eigenvalue comparison.  The formal
entry point is `TargetA.period8_alpha_plus_main_theorem`.

## Excluded from the manuscript kernel

- alpha = -1 formal wrapping;
- R2, R4, R6, and G6 cases;
- old exhaustive enumerations and certificate narratives;
- any all-even classification or assertion about all minimizers.

## Structural sections outside the Lean kernel

The period-eight trichotomy and the general moment obstruction are retained as
analytic results.  They are not described as Lean-verified.
