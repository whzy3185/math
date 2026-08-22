# Target A Arbitrary-Period Crystallization Program

## Exact moment route

`M4` has ten local translation classes and explicitly detects spacing four;
`M5,M6` have 27 and 76 classes.  This is a useful exact motif expansion, but no
nonnegative local decomposition of a Hankel witness has been found.

## Local Rayleigh route

For support lengths 6 through 10, every tau window was enumerated.  Small
integer vectors give exact Rayleigh exclusions above eta for:

```text
L=6: 160/256 tau windows
L=7: 360/512
L=8: 848/1024
L=9: 1864/2048
L=10: 3880/4096.
```

After global-sign identification, 108 length-11 `Q` windows survive at the
strongest level.  A complete primitive-cycle audit through period 16 leaves 30
cycles, including the target.  Therefore this particular local Rayleigh
relaxation is not sufficient for crystallization.

## Peierls and transparent defects

All neutral charge motifs of length 2-4 over `{-2,-1,+1,+2}` were tested at
orders 128 and 256.  All have positive numerical defect cost; the smallest is
about `0.31000936` for charges `[-1,-1,+2]` at order 128.  No transparent
defect was found in this bounded alphabet/support search.  This is scenario A
evidence only, not a uniform Peierls gap.

## Route status

| Route | Status |
|---|---|
| M4 motif expansion | STRONG |
| M5/M6 | STRONG_EXACT_DATA, WEAK_CERTIFICATE |
| Hankel-local certificate | WEAK |
| Local-window Rayleigh | PROMISING_BUT_INSUFFICIENT |
| de Bruijn survivor graph | WEAK: 30 bounded cycles |
| Motif-frequency/cycle polytope | PROMISING, not built after survivor multiplicity |
| SDP/SOS local certificate | WEAK, stopped before unbounded search |
| Transfer multicone | PROMISING, no exact cone |
| Subadditive optimization | PROMISING_CONCEPTUAL_ONLY |
| Finite-defect Peierls gap | PROMISING_BOUNDED_SIGNAL |
| Transparent-defect search | NO_COUNTEREXAMPLE_IN_BOUNDED_SCOPE |

Overall status: `ARBITRARY_PERIOD_REMAINS_OPEN`.
