# Proof Overview

The proof has four short stages.

## 1. Fix one Floquet convention

Use the canonical lift `tau_*` and the ansatz `u_(8m+r)=z^m v_r`. This gives
one explicit Hermitian unsquared `8 x 8` fiber `A_ref(z)` on `|z|=1`; no alternative cell ordering
or reciprocal Bloch convention is used.

## 2. Reduce the determinant

Writing `x` for an eigenvalue, direct fraction-free elimination gives a
Laurent determinant depending on `z` only through `z+z^(-1)` and
`z^2+z^(-2)`. Put

```text
y=x^2,   c=z+z^(-1).
```

The squared characteristic equation becomes

```text
P(y,c)=y^4-16y^3+(80-2c)y^2+(-128+16c)y+c^2-13c+38=0.
```

For `|z|=1`, one has `c in [-2,2]`.

## 3. Prove the sharp edge

At `c=2`, translating `y=x+4` reduces `P(y,2)` to
`x^4-20x^2+80`; its largest root is
`eta=4+sqrt(10+2sqrt(5))`. For `u=y-eta` and `t=2-c`, an exact expansion of
`P(eta+u,2-t)` has positive coefficients and vanishes for `u,t>=0` only at
`u=t=0`. Thus no unit-circle fiber has a squared eigenvalue above `eta`, and
equality forces `c=2`, hence `z=1`.

## 4. Interpret the reference gap

The positive sites of `Q_*` are `4 Z`. Two consecutive defects are therefore
four sites apart. Thus `g=4` is the reference bulk itself; the charge
coordinate `q=g-4` vanishes there.

## Evidence pattern

This theorem follows the publication pattern

```text
Floquet reduction -> exact quartic -> positive identity -> band-edge theorem.
```

No logically essential machine verification remains in the proof.

## Publication placement

- `MAIN_TEXT_REQUIRED`: the canonical fiber convention, polynomial
  `P(y,c)`, exact value of `eta`, positive identity, and identification of
  gap four.
- `APPENDIX_REQUIRED`: the displayed determinant calculation and finite
  holonomy refinement if space is limited.
- `REPRODUCIBILITY_ONLY`: the independent symbolic determinant audit.
