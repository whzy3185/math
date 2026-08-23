# Even Residue-class Upper Theorem

Let `m_n` be the minimum spectral radius over legal signings of order `n`.
For each nonzero even residue, use the following cyclic gap word:

```text
n=8k+2: [6,4^(2k-1)],
n=8k+4: [6,4^(k-1),6,4^(k-1)],
n=8k+6: [6,4^a,6,4^b,6,4^c],
```

where

```text
a=floor((2k-3)/3),
b=floor((2k-2)/3),
c=floor((2k-1)/3).
```

The last three exponents sum to `2k-3`. Thus the gap sums are exactly the
displayed orders. Each word contains `2k` positive `Q` defects, so the number
of negative `Q` entries is even and `product Q=1`; the cyclic `tau` lift
exists. Each gap six has charge `+2`. Its sector shift is two modulo four,
and the total shift agrees with `n mod 4`, which is precisely the cyclic
sector-closure condition. Either Hamilton holonomy may be chosen after the
lift.

The numbers of G6 interfaces are one, two, and three. Their minimum cyclic
site separations are respectively `n`, `n/2`, and at least `(n-8)/3`, hence
at least `n/4` for all sufficiently large orders. The fixed-r cap therefore
has an error tending to zero. Since each word supplies an admissible signing,

```text
limsup_(k->infinity) m_(8k+r)^2 <=c6,  r=2,4,6.
```

No lower bound matching `c6` is asserted, so these are limsup statements,
not limits.

Status: all three residue upper theorems PROVED.
