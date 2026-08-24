# Complete Abnormal Single-Gap Theorem

## Canonical single-gap operator

For an integer `g>=1`, let

```text
D_g=(-4 Z_(>=0)) union {0,g} union (g+4 Z_(>=0)).
```

Set `Q_i=+1` for `i in D_g` and `Q_i=-1` otherwise. Choose either lift
`tau_(i+1)=Q_i tau_i` and define

```text
(A_g v)_k=v_(k-1)+v_(k+1)+tau_(k-2)v_(k-2)+tau_k v_(k+2),
H_g=A_g^2.
```

Gap `g=4` is the unperturbed reference bulk, not an abnormal interface.
The plain-text symbol `c6` is typeset as `c_6`.

## Theorem

For both lifts and both interface orientations,

```text
sup sigma(H_6)=c6,
dim ker(H_6-c6)=2.                                    (1)
```

For every positive integer `g not in {4,6}`,

```text
sup sigma(H_g)>c6+1/250.                              (2)
```

Thus the publication form of (2) is `sup sigma(H_g)>c_6+1/250`; the
inequality is strict.

In particular, among all abnormal positive single gaps, G6 is the unique
minimizer of the squared spectral edge, and every other abnormal single gap
is separated from it by the same explicit constant.

## Exact comparison threshold

The proof uses the certified upper endpoint

```text
c6<7905369311620328/10^15
```

and therefore compares every witness to

```text
7905369311620328/10^15+1/250
=988671163952541/125000000000000.                    (3)
```

The smallest exact witness margin over (3) occurs at `g=8` and is

```text
174815250030533/310875000000000000>0.                (4)
```

## Scope

The theorem compares single gaps only. It does not assert that G6 minimizes
over arbitrary multi-gap or finite-core interfaces.
