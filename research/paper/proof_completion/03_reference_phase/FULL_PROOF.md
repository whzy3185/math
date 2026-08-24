# Full Proof

## 1. The canonical fiber

Use integer indices and the period-eight word

```text
tau_*=(1,1,-1,1,-1,-1,1,-1).
```

For `i=8m+r`, write `u_i=z^m v_r`. Substitution into

```text
(A_tau u)_i=u_(i-1)+u_(i+1)+tau_(i-2)u_(i-2)+tau_i u_(i+2)
```

gives

```text
A_ref(z)=
[ 0  1  1  0  0  0   z^-1   z^-1 ]
[ 1  0  1  1  0  0   0     -z^-1 ]
[ 1  1  0  1 -1  0   0      0    ]
[ 0  1  1  0  1  1   0      0    ]
[ 0  0 -1  1  0  1  -1      0    ]
[ 0  0  0  1  1  0   1     -1    ]
[ z  0  0  0 -1  1   0      1    ]
[ z -z  0  0  0 -1   1      0    ].
```

Reversing each undirected transition shows
`A_ref(z)^T=A_ref(z^(-1))`. Hence `A_ref(z)` is Hermitian whenever `|z|=1`.

## 2. Exact characteristic equation

Fraction-free elimination of `xI-A_ref(z)` gives

```text
det(xI-A_ref(z))
=x^8-16x^6+(80-2(z+z^-1))x^4
 +(-128+16(z+z^-1))x^2
 +(z^2+z^-2)-13(z+z^-1)+40.
```

Put `y=x^2` and `c=z+z^(-1)`. Since
`z^2+z^(-2)=c^2-2`, the equation is

```text
P(y,c)=y^4-16y^3+(80-2c)y^2
       +(-128+16c)y+c^2-13c+38=0.                (1)
```

On the unit circle `c=2 cos(theta)` lies in `[-2,2]`, and all fiber
eigenvalues `x` are real. Thus every squared fiber eigenvalue is a
nonnegative root of (1).

## 3. The endpoint value

At `c=2`,

```text
P(y,2)=y^4-16y^3+76y^2-96y+16.
```

Writing `y=X+4` gives

```text
P(X+4,2)=X^4-20X^2+80.
```

The equation for `W=X^2` is `W^2-20W+80=0`, with roots
`10+2sqrt(5)` and `10-2sqrt(5)`. Hence the four roots of `P(y,2)` are

```text
4-sqrt(10+2sqrt(5)),  4-sqrt(10-2sqrt(5)),
4+sqrt(10-2sqrt(5)),  4+sqrt(10+2sqrt(5)).
```

The largest is

```text
eta=4+sqrt(10+2sqrt(5)).                              (2)
```

## 4. Global maximality and uniqueness

Set `s=sqrt(10+2sqrt(5))`, `u=y-eta`, and `t=2-c`. Exact substitution into
(1) gives

```text
P(eta+u,2-t)
=u^4+4s u^3+2u^2 t+(40+12sqrt(5))u^2
 +4s u t+8sqrt(5)s u+t^2+(4sqrt(5)-3)t.             (3)
```

Every coefficient in (3) is strictly positive. Therefore, for `u>=0` and
`t>=0`, the right-hand side is nonnegative and it vanishes only when
`u=t=0`.

If a unit-circle fiber had a squared eigenvalue `y>eta`, then `u>0` and
`t=2-c>=0`, contradicting (1) and (3). If `y=eta`, equation (3) forces
`t=0`, so `c=2`. On `|z|=1`, the identity `z+z^(-1)=2` holds only for
`z=1`. Conversely, (2) is a root of `P(y,2)`, so `A_ref(1)` has eigenvalues
`+sqrt(eta)` and `-sqrt(eta)`. This proves

```text
sup_(|z|=1) rho(A_ref(z))^2=eta,
```

with equality only at `z=1`.

Finally, `sqrt(5)<9/4` and `(191/50)^2>29/2` imply
`sqrt(10+2sqrt(5))<191/50`; hence `eta<391/50<8`.

## 5. Finite rings

On `L` cells with Hamilton holonomy `alpha`, the cell shift is unitary and
has eigenvalues `z` satisfying `z^L=alpha`. Its eigenspaces are mutually
orthogonal and each is invariant under the signed adjacency. Therefore

```text
A_(8L,alpha) is unitarily equivalent to direct_sum_(z^L=alpha) A_ref(z). (4)
```

For `alpha=+1`, the Bloch grid contains `z=1`, so (4) attains `eta`. For
`alpha=-1`, it does not contain `1`, and the uniqueness just proved gives a
strict inequality. The negative-holonomy grid contains points tending to
`1` as `L` grows; continuity of eigenvalues of Hermitian matrices then gives
convergence of its edge to `eta`.

## 6. Gap-four identification

From `Q_i=tau_i tau_(i+1)` one computes

```text
Q_*=(1,-1,-1,-1,1,-1,-1,-1).
```

Thus `D(Q_*)=4 Z`. A single gap of length four places the right defect
lattice in the same residue class as the left one, so the resulting word is
the same bulk phase up to translation and the harmless choices of lift and
orientation. Hence `g=4` is the unperturbed reference phase. This completes
the proof.
