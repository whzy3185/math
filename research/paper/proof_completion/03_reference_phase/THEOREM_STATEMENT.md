# The Period-Eight Reference Phase

## Canonical convention

On the signed square of the cycle let

```text
(A_tau u)_i=u_(i-1)+u_(i+1)+tau_(i-2)u_(i-2)+tau_i u_(i+2).
```

Fix the period-eight triangle-flux word

```text
tau_*=(+,+,-,+,-,-,+,-)
```

and define `Q_i=tau_i tau_(i+1)`. Its quadrilateral-flux word is

```text
Q_*=(+,-,-,-,+,-,-,-),
```

so the positive `Q` sites are precisely `4 Z`. For a Bloch multiplier
`z in C\{0}`, use `u_(8m+r)=z^m v_r`, `0<=r<8`, and denote the resulting
unsquared fiber by `A_ref(z)`.

## Theorem

Let

```text
eta=4+sqrt(10+2sqrt(5)).
```

Then

```text
sup_(|z|=1) rho(A_ref(z))^2=eta<8.
```

Equality is attained only at `z=1`. Equivalently, the global squared upper
band edge of the infinite period-eight reference operator is `eta`, and the
unique Bloch phase at that edge is zero.

If the same cell is placed on a ring of order `8L` with Hamilton holonomy
`alpha in {+1,-1}`, then

```text
A_(8L,alpha) is unitarily equivalent to direct_sum_(z^L=alpha) A_ref(z).
```

Consequently the positive-holonomy ring has squared spectral radius `eta`,
whereas the negative-holonomy ring has squared spectral radius strictly below
`eta` and converges to `eta` as `L` tends to infinity.

## Structural proposition

A single-gap configuration with gap `g=4` has positive `Q` sites `4 Z` and
is therefore exactly the unperturbed reference phase, up to translation,
reflection, and the choice of the two `tau` lifts. It is not an interface.

## Graph-theoretic meaning

The period-eight signing is the crystalline background for all later phase
slips. In squared spectral coordinates its edge lies strictly below both the
elementary G6 interface edge `c6` and the limiting threshold `8`:

```text
eta<c6<8.
```
