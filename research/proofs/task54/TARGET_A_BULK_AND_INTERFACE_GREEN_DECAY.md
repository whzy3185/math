# Bulk and Interface Green Decay

On `Gamma`, the period-eight bulk spectral distance is larger than `9/100`:

```text
c6_lower-1/300-1561/200 >9/100.
```

The same range-four exponential conjugation costs at most `16/9999`.
Consequently every translated bulk Green kernel satisfies

```text
|G_bulk(z;i,j)| <=12 exp(-|i-j|/40000).
```

For the interface, the full Green function has a rank-two pole at the squared
level `c6`; the old rank-one wording counted only the positive `A` root.
After removing the full pole, the constant is 1200. These estimates are uniform in the
four translated bulk sectors, both interface orientations, and `z in Gamma`.

Status: `BULK_AND_REDUCED_INTERFACE_GREEN_DECAY_PROVED` /
COMPUTER_ASSISTED_PROVED after the certified G6 isolation input; the
Combes--Thomas implication is analytic.
