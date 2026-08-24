# The Elementary G6 Spectral Edge

## Operator and algebraic constant

Let `Q^(6)` have positive sites `4Z` on the left through zero and
`6+4Z` on the right from six onward. Fix either lift by
`tau_(i+1)=Q_i tau_i`, and define on `ell^2(Z)`

```text
(A_6 u)_i=u_(i-1)+u_(i+1)+tau_(i-2)u_(i-2)+tau_i u_(i+2),
H_6=A_6^2.
```

Let `p_6` be

```text
16y^10-520y^9+6913y^8-48448y^7+191768y^6
-423904y^5+484528y^4-270464y^3+137856y^2
-19968y+256.
```

There is a unique root `c6` of `p_6` in

```text
7905369311620327/10^15 < c6
                       < 7905369311620328/10^15.       (1)
```

The plain-text symbol `c6` is typeset as `c_6`; thus the first publication
formula below reads `sup sigma(H_6)=c_6`.

## Theorem

For either orientation of the elementary G6 interface and either `tau` lift,

```text
sup sigma(H_6)=c6,                                    (2)
dim ker(H_6-c6)=2.                                    (3)
```

Equivalently, `A_6` has one simple physical eigenvalue `+sqrt(c6)`, one
simple physical eigenvalue `-sqrt(c6)`, and no spectral point of larger
absolute value. Both eigenvectors are exponentially localized at the phase
slip.

The essential squared bulk edge is

```text
eta=4+sqrt(10+2sqrt(5))<c6.
```

Thus `c6` is an isolated rank-two squared eigenvalue above the period-eight
bulk bands.

## Symmetry statement

In the forward tree gauge,

```text
(K u)_i=(-1)^i u_(9-i)
```

satisfies

```text
K^2=-I,   K A_6=-A_6 K,   K H_6=H_6 K.               (4)
```

This is an explicit real-linear orthogonal symmetry. No appeal to informal
Kramers terminology is needed.
