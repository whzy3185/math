# Exact-r Min-Max and Riesz Count

For `r in {1,2,3}`, the corrected sine/cosine truncated modes and the spectral
projection argument supply at least `r` eigenvalues in an exponentially
shrinking neighborhood of `c6`. The complement estimate shows by min-max
that at most `r` eigenvalues can exceed `c6-1/200`.

For sufficiently large minimum separation the cluster lies inside

```text
[c6-1/400,c6+1/400].
```

The interval is above the complementary spectral cap. It therefore contains
exactly `r` eigenvalues counted with multiplicity. Equivalently, a contour
surrounding this interval has a Riesz projection of rank `r`. This does not
assert simplicity.

Status: `EXACT_R_R123_MINMAX_COUNT_PROVED` / COMPUTER_ASSISTED_PROVED. The
min-max/Riesz implication is analytic, while its G6 isolation input is
computer assisted. No independent geometric resolvent proof is claimed.
