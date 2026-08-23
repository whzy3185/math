# Single-Gap Hierarchy: Exact Recurrence And Open Physical Tail

## Exact Gap-Plus-Eight Transfer

For a gap `g`, let

```text
R_g       = product on [g,g+8),
N_(g+8)   = inserted product on [g,g+8),
R_(g+8)   = product on [g+8,g+16).
```

The exact transfer update produced by inserting one period-eight cell is

```text
C_g = R_(g+8) N_(g+8) R_g^-1.                         (5)
```

All eight residue representatives have the same characteristic polynomial,
but the matrices themselves form exactly two classes:

```text
C_1=C_3=C_5=C_7,
C_2=C_4=C_6=C_8.                                      (6)
```

This corrects the earlier informal wording that suggested eight distinct
matrices.

## Characteristic Polynomial

With `y=lam^2`, both classes satisfy

```text
chi_C(t) = t^4 + a_C t^3 + b_C t^2 + a_C t + 1,       (7)
a_C = -2y^2+12y-17,
b_C = y^4-16y^3+88y^2-200y+160.
```

Let `W_g=wedge^2 C_g` in the ordered basis

```text
(01,02,03,12,13,23).
```

Its characteristic polynomial is `(t-1)^2 Q_4(t)`, with

```text
Q_4(t)=t^4+A t^3+B t^2+A t+1,
A=-y^4+16y^3-88y^2+200y-158,
B=2y^4-16y^3+36y^2-8y-29.                            (8)
```

Exact symbolic multiplication gives

```text
(W_g-I)Q_4(W_g)=0                                     (9)
```

for both matrix classes. At `lam=3`, the Krylov matrix

```text
[e_0,W_ge_0,W_g^2e_0,W_g^3e_0,W_g^4e_0]
```

has a nonzero minor on rows `(0,1,2,3,5)`:

```text
odd class:  -361233047485886499,
even class:  1134653061164985747.                     (10)
```

Therefore the generic minimal polynomial has degree at least five; (9)
shows it has degree at most five. It is exactly

```text
m_5(t)=(t-1)Q_4(t)
      =t^5-Ut^4+Vt^3-Vt^2+Ut-1,                      (11)
U=(y-3)(y^3-13y^2+49y-53),
V=(y-3)(3y^3-23y^2+55y-43).
```

Consequently every scalar exterior-square observable along a fixed residue
family satisfies the exact order-five recurrence

```text
d_(k+5)=U d_(k+4)-V d_(k+3)+V d_(k+2)-U d_(k+1)+d_k. (12)
```

## Why This Does Not Close The Hierarchy

The reciprocal reduction of `Q_4` has discriminant

```text
(y-8)(y-4)(y-2)^2(y^2-8y+14)^2.                      (13)
```

The certified G6 interval lies strictly inside `4<y<8`, so (13) is negative
there. The relevant recurrence modes occur as complex reciprocal pairs of
equal modulus. A real Perron root, invariant cone, or one-mode eventual-sign
argument is therefore unavailable at `c6`.

Moreover, the gap-2/gap-6 involution exchanges stable and unstable Floquet
sheets. Equations (1) and (12) do not select the physical Evans branch and do
not prove eventual root ordering, monotonicity, or a uniform lower bound for
all single gaps.

## Classification

The exact algebraic result is:

```text
UNSQUARED_QUOTIENT_INVOLUTION_AND_ORDER5_RECURRENCE_PROVED.
```

The target statement

```text
every physical single-gap interface has spectral top at least c6
```

remains `OPEN`. A successful continuation needs a genuinely physical branch
invariant, such as a Weyl phase, a stable-sheet sign rule, or a finite exact
base plus a two-mode tail estimate. The recurrence alone is not such an
invariant.
