# Proof Overview

This package isolates the combinatorics that sit between the period-eight
bulk and the operator-theoretic interface analysis.

## 1. Gaps partition the cycle

Successive positive `Q` sites divide the cyclic index set into disjoint arcs.
Their lengths sum to `n`. Subtracting the reference length four from each arc
gives the total-charge identity.

## 2. Periodicity imposes parity

The recurrence `tau_(i+1)=Q_i tau_i` closes cyclically exactly when
`product_i Q_i=1`. For even `n`, this forces the number `d` of positive `Q`
sites to be even. Consequently `4d` is divisible by eight, giving the
modulo-eight charge law.

## 3. Endpoints determine the sector

If a gap begins at a positive site congruent to `s mod 4`, its endpoint is
congruent to `s+g mod 4`. The right reference bulk therefore is `B_(s+g)`.
Since `g` and `q=g-4` have the same residue modulo four, the sector shift is
`q mod 4`.

## 4. Concatenation is addition

Successive endpoint displacements add. Reducing the sum modulo four proves
the composition law without transfer matrices, Evans functions, or a choice
of gauge.

## Important distinction

The total charge controls order modulo eight, while the translation sector
is only a modulo-four invariant. They are compatible but not identical. In
particular the false rule `q/2 mod 4` is not used.

## Publication placement

- `MAIN_TEXT_REQUIRED`: gap coordinates, total charge, four sectors, the
  sector-shift theorem, and composition.
- `APPENDIX_REQUIRED`: cyclic-lift parity bookkeeping if it is not kept with
  the main proposition.
- `REPRODUCIBILITY_ONLY`: the optional finite JSON audit of representative
  sector shifts.
