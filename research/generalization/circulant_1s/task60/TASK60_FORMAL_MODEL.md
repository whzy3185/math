# Task 60 Formal Model

## Graph and nondegenerate regime

Let `V=Z/NZ` and let `C_N(1,s)` have connection set
`{+/-1,+/-s}`. The working hypotheses

```text
2 <= s < N/2
```

exclude `s=0`, `s=+/-1`, and `2s=0 (mod N)`. Thus the graph is simple and
4-regular. Cases outside this range require a separate model because degree
or edge multiplicity changes.

## Explicit cyclic multiplier isomorphisms

Multiplication by a unit `a in (Z/NZ)^*` sends the connection set to
`{+/-a,+/-as}`. Two normalizations are immediate:

1. `a=+/-1` gives `s <-> N-s`.
2. If `gcd(s,N)=1`, choosing `a=+/-s^{-1}` makes the old `s`-edge the new
   step-one edge and gives `s <-> +/-s^{-1} (mod N)`.

Hence the proved multiplier orbit of a normalized chord is

```text
{+/-s}                         if gcd(s,N)>1,
{+/-s,+/-s^{-1}}               if gcd(s,N)=1.
```

A canonical representative is the smallest number in `[2,N/2)` obtained by
replacing every residue `r` in this orbit by `min(r,N-r)`. This is a proved
reduction under cyclic-group automorphisms. It is not asserted to classify
all abstract graph isomorphisms for every cyclic order.

## Hamilton gauge without seam ambiguity

Write the original step-one signs as `a_i`. Switching recursively along the
Hamilton path makes `a_0,...,a_{N-2}` positive. The remaining sign is

```text
alpha = product_i a_i in {+1,-1},
```

the Hamilton-cycle holonomy. If the original chord sign on `{i,i+s}` is
`b_i`, the seam-safe chord coordinate is

```text
tau_i = b_i product_{k=0}^{s-1} a_{i+k},
```

where the product follows the forward Hamilton path from `i` to `i+s`.
This coordinate is switching invariant. In tree gauge, the raw chord sign is
`alpha^chi_i tau_i`, where `chi_i` records whether the path crosses the seam;
calling the raw seam-gauge chord sign `tau_i` would make the flux formula
below false at wraparound indices.

A convenient equivalent description removes the displayed seam on the
universal cover: vectors satisfy

```text
u_{i+N}=alpha u_i,
```

the step-one coefficients are all `+1`, and the transformed chord word
`tau_i` is `N`-periodic. The operator is

```text
(A_{s,tau,alpha}u)_i
 = u_{i-1}+u_{i+1}+tau_{i-s}u_{i-s}+tau_i u_{i+s}.
```

The recursive switching construction proves existence. Any two switchings
that preserve all uniform step-one coefficients differ by a constant sign,
which changes no edge sign; therefore `(alpha,tau)` is a complete and unique
Hamilton-gauge coordinate for a switching class. There are `2^(N+1)` such
classes, agreeing with the cycle-space dimension `2N-N+1=N+1`.

## Four-cycle flux and its limitation

The four-cycle

```text
i -> i+s -> i+s+1 -> i+1 -> i
```

has switching-invariant sign

```text
Q_i=tau_i tau_{i+1}.
```

Consequently `product_i Q_i=1`. Conversely, a cyclic `+/-1` word `Q` lifts
to a chord word precisely when its product is `+1`. Fixing `tau_0` and using
`tau_{i+1}=Q_i tau_i` gives the lift, and the two choices of `tau_0` give
exactly the two lifts `tau` and `-tau`.

This produces an important negative conclusion:

```text
(Q,alpha) does not generally encode the switching class completely.
```

Hamilton gauge has no residual nonconstant switching, so the two chord lifts
are distinct switching classes unless an additional graph automorphism
identifies them. A complete coordinate is `(Q,alpha,tau_0)`, or equivalently
`(alpha,tau)`. For arbitrary `Q`, equal spectral radii of the two lifts must
not be assumed: alternating vertex conjugation followed by global matrix
negation relates

```text
(tau,alpha) -> ((-1)^(s+1) tau, (-1)^N alpha).
```

Thus this symmetry identifies the two lifts at fixed holonomy only when both
`N` and `s` are even. The alternating `Q=-1` family in Task 60.1 has an
additional squared-operator simplification.

## Theorem 60.0A

For every nondegenerate signed `C_N(1,s)`, Hamilton gauge gives the unique
operator above. Its local four-cycle flux is `Q_i=tau_i tau_{i+1}`; cyclic
flux words are exactly the product-`+1` words and have exactly two chord
lifts. These statements are independent of `s`.
