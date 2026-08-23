# Arbitrary-Length Local Lemma For A Consecutive `(3,3)` Motif

## Statement

Complete any finite defect core by the period-four defect sequences on its two
sides.  Suppose three consecutive defects occur at

```text
x, x+3, x+6.
```

Let the preceding defect be `x-a`, where `a>=1`, and let the following defect
be `x+6+b`, where `b>=1`.  For either lift of `tau`, the bilateral operator
`A` has a vector supported on `[x-2,x+8]` such that

```text
||Av||^2/||v||^2 >= 419/53
                    > 7905369311620328/10^15
                    > c_6.                                  (1)
```

Consequently every finite core containing consecutive gaps `(3,3)` satisfies

```text
sup sigma(A^2)>c_6,
```

without any bound on the total core length or on the other gaps.

## Reduction To One `tau` Lift

Translate `x` to zero.  First take `tau_0=1`.  If `D` is the diagonal sign
operator `(Du)_i=(-1)^i u_i`, direct inspection of the nearest- and
next-nearest-neighbor terms gives

```text
A_(-tau) = -D A_tau D.                                      (2)
```

Thus replacing `v` by `Dv` preserves both its norm and the norm of its image.
It suffices to prove (1) for `tau_0=1`.

## Explicit Vectors

Coordinates below are ordered from `x-2` through `x+8`.

| predecessor gap | `v` | `||v||^2` |
|---|---|---:|
| `a=1` | `(1,0,3,4,3,5,4,4,3,1,2)` | 106 |
| `a=2` | `(2,0,0,-3,-2,-2,-2,-2,-1,-1,-1)` | 32 |
| `a>=3` | `(1,0,3,4,3,5,4,4,3,1,2)` | 106 |

The image is evaluated on `[x-4,x+10]`.  Direct substitution into

```text
(Av)_k=v_(k-1)+v_(k+1)+tau_(k-2)v_(k-2)+tau_kv_(k+2)        (3)
```

gives the following minimizing absolute-coordinate lists. They are independent
of `b`; in the `a=1` case an additional defect at `x-2` increases the squared
numerator from `874` to `902`.

| predecessor gap | `(|Av|_{x-4},...,|Av|_{x+10})` | `||Av||^2` |
|---|---|---:|
| `a=1` | `(1,1,3,8,6,11,8,15,9,11,11,1,4,3,2)` | `874` or `902`, hence at least `874` |
| `a=2` | `(2,2,0,5,7,4,3,9,3,4,6,0,2,2,1)` | 258 |
| `a>=3` | `(1,1,3,0,8,11,8,15,9,11,11,1,4,3,2)` | 838 |

Here is the finite case closure behind that substitution. Since `v` is
supported on `[x-2,x+8]`, only `Q` on `[x-4,x+7]` can multiply a nonzero
coordinate in formula (3). The checker inspects the five nearest-predecessor
classes `a=1,2,3,4,a>=5`, every subset of still-earlier defects in
`[x-4,x-1]`, and the two locally distinct successor classes `b=1,b>=2`.
These are 32 finite dependency cases. They give numerator sets `{874,902}`,
`{258}`, and `{838}` for the three rows. More distant defects cannot enter
(3).

It follows that the three Rayleigh quotients are

```text
a=1:   ||Av||^2/106 >=874/106 = 437/53,
a=2:   258/32  = 129/16,
a>=3:  838/106 = 419/53.
```

The last is the minimum.  Its exact margin over the certified upper endpoint
for `c_6` is

```text
419/53 - 7905369311620328/10^15
  = 1928310515327/6625000000000000 > 0.                    (4)
```

Equations (2)--(4) prove the lemma for both lifts.  The variational principle
then gives `sup sigma(A^2)>=||Av||^2/||v||^2>c_6`.

## Scope

Every occurrence of `(3,3)` in a finite core has a predecessor and successor
in the completed bilateral defect sequence; at a core boundary these are
supplied by the period-four tail.  Thus the lemma is genuinely independent of
total core length.

It does not cover motif-free primitive words.  In particular, it does not
prove the universal `B0 -> B2` statement, which remains `OPEN`.
