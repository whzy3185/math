# Explicit Exponential Constants: Open Status

The repository currently certifies the complement constants

```text
delta_comp=1/200,
counting window radius=1/400,
||(QHQ-lambda)^(-1)||<=400,
```

and the period-eight-cell multiplier bound `q=9/25`. It does not store a
normalized algebraic G6 matching vector or a certified tail prefactor.
Consequently it does not yet provide reproducible numerical values for
`C_1,C_2,C_3` or their onset distances.

A complete extraction must certify the normalized stable-mode coefficients,
tail norm, Gram conditioning, quasimode residuals, and `QHP` for every
orientation and holonomy. If

```text
||PHP-c6P||<=A_r q^ell,
||QHP||<=B_r q^ell,
```

then the existing inverse bound yields

```text
C_r=A_r+400 B_r^2.
```

No decimal fit is accepted in place of those bounds.

Status: OPEN.
