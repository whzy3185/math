# Target A Single Phase-Slip Interface Reconnaissance

## Constants and convergence

The explicit single-slip rings were evaluated to order 1026 for gap 6 and
1022 for gap 10.  Sparse `A^2` iteration was cross-checked against dense
diagonalization at the small orders.  The two-exponential model has the best
BIC for both families, followed by the one-exponential model; the power model
is substantially worse.

- `c6 = 7.905369311620327011976279279804273987486348974350953...`
- `8-c6 = 0.0946306883796729880237207201957260125...`
- `c10 = 7.977104370400546515362821583215693131572428742299712...`
- `8-c10 = 0.0228956295994534846371784167843068684...`

The values are stable under 220-digit Evans-function computation and an
independent transfer boundary shift.  A degree-10 PSLQ candidate was found
for `c6`, with constant-first coefficients

`[-256,19968,-137856,270464,-484528,423904,-191768,48448,-6913,520,-16]`.

It survives the higher-precision numerical validation gate but is only an
`ALGEBRAIC_CANDIDATE`.  The gap-10 training relation fails independent
validation, so `c10` remains a `NUMERICAL_CONSTANT`.

## Localization and Floquet match

At rings near 256, 512, and 1024, the controlling `A^2` eigenvectors are
exponentially localized at the slip.  The fitted cell multipliers are about
`0.35` for G6 and `0.260` for G10, with near-interface log-linear fits mostly
above `R^2=0.998`.  The period-8 bulk transfer matrix gives slow stable
multipliers

- G6: `0.3505061161329224423...`
- G10: `0.2585020646331716963...`

The finite-size correction, eigenvector tail, and bulk multiplier therefore
agree at reconnaissance accuracy.  The classification is
`INTERFACE_FLOQUET_SIGNAL_STRONG` for both families.

## Matching prototype

The fourth-order recurrence yields a four-dimensional exact transfer matrix.
Using the two left-unstable and two right-stable bulk modes gives

`D_g(lambda) = det(P_g(lambda) U_left(lambda), U_right(lambda)) = 0`.

This determinant recovers both constants at high precision.  Stable
subspaces are still evaluated numerically and resultant elimination has not
been completed, so the correct status is `SYMBOLIC_INTERFACE_PROTOTYPE`, not
an exact interface equation.

Overall: `PHASE_SLIP_INTERFACE_THEOREM_SIGNAL = STRONG`.
