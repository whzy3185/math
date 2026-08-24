# General Moments and the Bounded Periodic Frontier

## Periodic setup

Let `tau` be a sign word with period `p>=1` and set

```text
Q_i=tau_i tau_(i+1).
```

A periodic lift exists exactly when `product_(i=0)^(p-1) Q_i=1`. Let
`A_Q(z)` be the exact `p x p` Laurent Bloch fiber on `|z|=1`, and define

```text
R(Q)=sup_(|z|=1) rho(A_Q(z))^2,
M_k(Q)=CT_z tr(A_Q(z)^(2k)).
```

Write

```text
d=#{i:Q_i=+1},
a=#{i:Q_i=Q_(i+1)=+1},
b=#{i:Q_i=Q_(i+2)=+1},
```

with indices taken modulo `p`.

## Theorem A: first three general moments

[APPENDIX_REQUIRED]

For every legal period and flux word,

```text
M_1=4p,
M_2=20p+16d,
M_3=118p+168d+96a+48b.                                (1)
```

Consequently,

```text
R(Q)<=8  =>  d<=3p/4,
R(Q)<=8  =>  40d+96a+48b<=42p.                        (2)
```

The conditions in (2) are necessary, not sufficient.

## Theorem B: bounded periodic frontier

[APPENDIX_REQUIRED]

Consider legal periodic phases whose primitive `tau` period is at most 24.
Identify phases under translation, reflection, global `tau` negation, unit
cell repetition, and the corresponding Bloch zone folding. Then the
period-eight reference phase is the unique phase in this bounded domain with

```text
R(Q)<c6.                                               (3)
```

Its value is

```text
R(Q)=eta=4+sqrt(10+2sqrt(5))<c6.
```

Every genuinely different phase in the stated domain satisfies `R(Q)>c6`.

## Exact scope

[MAIN_TEXT_REQUIRED]

Theorem B stops at primitive period 24. It gives no statement for period 25
or larger, aperiodic phases, finite interfaces, or arbitrary finite signings.
The exact read-only calculations at periods 25 and 26 are not part of the
theorem.

The main phase-slip proof does not require the bounded frontier. Its proper
paper role is a supporting appendix theorem.
