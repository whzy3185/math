# Translation-Sector Charge Theorem

## Canonical sectors

Let `B_s`, `s in Z/4Z`, be the period-four bulk `Q` word whose positive
sites are exactly `i congruent to s (mod 4)`. Its other three entries are
negative. Fixing `tau_0=1` and using `tau_(i+1)=Q_i tau_i` gives an
antiperiodic lift over four sites and a periodic lift over eight sites. The
four `Q` sectors are independent of the two Hamilton-cycle holonomies
`alpha=+1,-1`.

## Theorem

An oriented gap of length `g` beginning at a positive site in `B_s` ends at
a positive site in

```text
B_(s+g mod 4).
```

If its local charge is `q=g-4`, its translation-sector charge is therefore

```text
sigma(q)=q mod 4.
```

For concatenated interface words `P,Q`,

```text
sigma(PQ)=sigma(P)+sigma(Q) mod 4.
```

## Proof

Translate the initial positive site to zero. The right period-four bulk has
positive sites `g+4Z`, so its residue is `g mod 4`. Since subtracting four
does not change a residue modulo four, this is also `q mod 4`. For a word of
gaps, the endpoint is displaced by the sum of the gaps. Applying the
one-gap statement and reducing modulo four proves additivity. No switching
or holonomy choice enters this argument.

The proposed rule `q/2 mod 4` is false: a G6 interface has `q=2`, while its
right positive sites lie in residue class two, not one. Even charges thus
occupy only the subgroup `{0,2}` of the full `Z4` sector group. Calling the
even charge itself a full `Z4` invariant would be inaccurate.

Machine artifact: `certificates/translation_charge.json`.

Status: `TRANSLATION_CHARGE_PROVED_CORRECTED_RULE`.
