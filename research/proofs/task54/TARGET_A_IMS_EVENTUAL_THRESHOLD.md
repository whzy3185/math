# IMS Eventual Threshold

For `n=8k+r`, use the explicit Task 53 constructions. Their exact minimum
site separations are

```text
D_2(n)=n,
D_4(n)=n/2,
D_6(n)=6+4 floor((2k-3)/3).
```

In residue zero, the period-eight construction has spectral edge at most
`eta<1561/200`. In the other classes use the optimized global IMS cap with
`R=floor((D_r(n)-9)/2)`. Exact rational comparison against

```text
rho_-(n)^2 > 8-200/n^2
```

passes at `n=240,242,244,246`. Along each residue subsequence, `D` and `R`
are nondecreasing, the exact IMS error is nonincreasing, and the threshold
lower bound is strictly increasing. Hence every even `n>=240` is a
counterexample.

The last orders where this analytic criterion fails are respectively
`32,90,164,238` in residues `0,2,4,6`. Thus the threshold for this exact IMS
criterion is

```text
N_IMS=240.
```

Status: PROVED.
