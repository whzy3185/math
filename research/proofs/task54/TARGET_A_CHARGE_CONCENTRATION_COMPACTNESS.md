# Charge Concentration-Compactness

Let `z_j(x)=1` when `Q_j(x)=+1` and zero otherwise. Define the
phase-independent bad-window indicator

```text
b_j(x)=1_{sum_(t=0)^3 z_j(x+t) !=1}.
```

If consecutive bad-window indicators vanish, subtracting adjacent length-four
window sums gives `z_j(x+4)=z_j(x)`. The corresponding interior is therefore
one translated period-eight bulk sector.

For positive-Q sites with cyclic gaps `g_(j,i)`, define the signed charge and
a nonnegative compactness measure by

```text
charge_j=sum_i (g_(j,i)-4) delta_(p_(j,i)),
omega_j=sum_x b_j(x) delta_x + |charge_j|.
```

The total signed charge is `n_j-4d_j`, and legality makes `d_j` even; hence it
is congruent to `n_j` modulo eight. The all-negative Q word, which has no gap
chart, is still detected by the bad-window term.

Normalize `mu_j=omega_j/omega_j(C_(n_j))` when the denominator is nonzero.
The usual concentration function

```text
C_j(R)=sup_x mu_j(B_R(x))
```

and a diagonal subsequence give exactly the standard alternatives:

1. `TIGHT`: after translation, arbitrarily nearly all normalized mass lies
   in a fixed-radius ball;
2. `DICHOTOMY`: two positive mass fractions have supports whose separation
   tends to infinity;
3. `NORMALIZED_VANISHING`: `sup_x mu_j(B_R(x))` tends to zero for every fixed
   `R`.

If the unnormalized integer masses are uniformly bounded, tightness implies
that the entire support eventually lies in one fixed-radius ball. Without
that bound, a tight limit may still be an infinite or semi-infinite
excursion.

Normalized vanishing is not the same as sparse defects: positive-density
configurations also vanish after normalization. A genuine sparse-reference
condition is `sum_x b_j(x)=o(n_j)`, which makes a uniformly rooted fixed
window a pure bulk patch with probability tending to one, while leaving
defect-centered roots uncontrolled.

Status: PROVED as a compactness trichotomy. Spectral exclusion of its three
cases is a separate OPEN problem.
