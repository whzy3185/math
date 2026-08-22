# Exact Charge and Higher-Moment Results

## Charge conservation

If the positive `Q` sites cut a periodic word into gaps `g_1,...,g_d`, then

```text
sum_i g_i=n,
sum_i (g_i-4)=n-4d.
```

For even `n`, the periodic `tau` lift condition is
`product_i Q_i=(-1)^(n-d)=1`, so `d` is even and total charge is congruent to
`n mod 8`.  The two Hamilton-cycle holonomies `alpha=+1,-1` remain available;
they do not alter this charge law.

## Exact M4-M6 expansions

Closed step words over `{-2,-1,1,2}` were enumerated and every even `tau`
monomial was rewritten exactly as a `Q` interval.  In the notation
`S[I]=sum_j product_(i in I) Q_(j+i)`, the new fourth moment is

```text
M4 = 2244 S[const] + 2336 S[0] + 640 S[0,1]
   + 96 S[0,1,2] + 32 S[0,1,2,3] + 32 S[0,1,3]
   + 336 S[0,2] + 32 S[0,2,3] + 16 S[0,2,4]
   + 32 S[0,3].
```

Thus spacing four first appears explicitly through `S[0,2,4]`.  The analogous
exact expansions for `M5` and `M6` have 27 and 76 translation classes.  They
were independently checked against exact closed-walk dynamic programming on
36 legal words.  Growth beyond `M6` was stopped because no local positivity
decomposition had emerged.

Status: `EXACT_CHARGE_CONSERVATION_PROVED` and
`M4_M5_M6_EXACT_LOCAL_MOTIF_EXPANSIONS_PROVED`.
