# Residue-Class Upper Theorem

## Setting

Let `A` be a legal signed adjacency matrix of `C_n(1,2)` and put
`H=A^2`. Let `eta` be the squared spectral edge of the period-eight bulk and
let `c6` be the squared spectral edge of the elementary G6 interface. Thus

```text
eta < c6 < 8.
```

A separated G6 ring is a legal cyclic gap word containing `t` gaps equal to
six and only gaps equal to four otherwise. Here `t` is the number of
interfaces, not a residue class. Let `D` be the minimum cyclic site distance
between consecutive interfaces, with `D=n` when `t=1`.

## Theorem A: exact IMS cap

[MAIN_TEXT_REQUIRED]

Assume `t in {1,2,3}`. Choose an integer `R>=4` such that

```text
2(R+4)<D,                 n>2R+4.
```

Then both holonomy sectors and both interface orientations satisfy

```text
rho(A)^2
 <= c6 + (240R-342)/(R(2R^2+1))
 <= c6 + 120/R^2.                                      (1)
```

In particular, taking `R=floor((D-9)/2)` whenever the displayed support
conditions hold gives a fixed-`t` cap converging to `c6` as `D` tends to
infinity.

## Theorem B: explicit exponential refinement

[APPENDIX_REQUIRED]

If, in addition, `D>=1040`, define

```text
ell=floor((floor(D/4)-12)/8),        q=9/25.
```

The independently certified exact-`2t` cluster theorem implies

```text
rho(A)^2 <= c6+3505t q^ell.                            (2)
```

The cluster has dimension `2t`, counted with multiplicity. Formula (2) does
not use or revive the false historical exact-`t` squared-mode count.

## Theorem C: residue-class constructions

[MAIN_TEXT_REQUIRED]

For sufficiently large `k`, the following legal cyclic gap words exist:

```text
n=8k+2:  [6,4^(2k-1)],
n=8k+4:  [6,4^(k-1),6,4^(k-1)],
n=8k+6:  [6,4^a,6,4^b,6,4^c],
```

where

```text
a=floor((2k-3)/3),
b=floor((2k-2)/3),
c=floor((2k-1)/3).
```

If `m_n` denotes the minimum spectral radius over legal signings, then

```text
limsup_(k->infinity) m_(8k+s)^2 <= c6,
s in {2,4,6}.                                           (3)
```

Equation (3) is an upper-construction theorem only. It asserts neither a
matching lower bound, a limit, nor a classification of minimizers.

## Scope

[MAIN_TEXT_REQUIRED]

The theorem applies only to the displayed period-eight/G6 constructions with
one, two, or three interfaces. It does not assert universal multi-gap
optimality, unrestricted common residue limits, or simplicity of the
finite-ring near-`c6` levels.
