# 4. Periodic Construction and Floquet Reduction

We now place the order-32 pattern in an arbitrary number of eight-site cells.
Let

```text
tau_*=(+,+,-,+,-,-,+,-)                                         (4.1)
```

and impose either Hamilton holonomy `alpha in {+1,-1}` on a graph of order
`n=8L`.

## 4.1 The eight-site fiber

Write `i=8m+r`, `0<=r<8`, and put `x_(8m+r)=z^m v_r`. Substitution in (2.1)
gives

```text
H(z)=
[ 0  1  1  0  0  0   z^-1   z^-1 ]
[ 1  0  1  1  0  0    0    -z^-1 ]
[ 1  1  0  1 -1  0    0      0   ]
[ 0  1  1  0  1  1    0      0   ]
[ 0  0 -1  1  0  1   -1      0   ]
[ 0  0  0  1  1  0    1     -1   ]
[ z  0  0  0 -1  1    0      1   ]
[ z -z  0  0  0 -1    1      0   ].                              (4.2)
```

On `|z|=1`, replacing `z` by its complex conjugate `z^(-1)` transposes the
matrix, so (4.2) is Hermitian.

**Proposition 4.1 (finite Floquet decomposition).** For `n=8L`,

```text
A_(8L,alpha) ~= direct_sum_(z^L=alpha) H(z).                     (4.3)
```

**Proof.** Let `S` be the unitary shift on the `L` cell coordinates with
twisted boundary `u_(m+L)=alpha u_m`. Its normalized eigenvectors are
`L^(-1/2)(1,z,...,z^(L-1))` with `z^L=alpha`. Distinct roots are orthogonal by
the geometric-sum identity. The signed operator is a finite sum of residue
matrices tensored with powers of `S`, so each eigenspace is invariant and its
restriction is (4.2). There are `L` such eight-dimensional eigenspaces, and
their dimensions sum to `8L`. `square`

Thus the finite problem uses the discrete set `z^L=alpha`, while the infinite
periodic problem uses every `|z|=1`.

## 4.2 Exact determinant

Let `x` be the spectral parameter. Fraction-free elimination of
`xI-H(z)` gives

```text
det(xI-H(z))
 =x^8-16x^6+(80-2(z+z^-1))x^4
   +(-128+16(z+z^-1))x^2
   +(z^2+z^-2)-13(z+z^-1)+40.                                  (4.4)
```

Set

```text
y=x^2,       c=z+z^-1.
```

Since `z^2+z^(-2)=c^2-2`, equation (4.4) becomes

```text
P(y,c)=y^4-16y^3+(80-2c)y^2+(-128+16c)y+c^2-13c+38.             (4.5)
```

For `|z|=1`, `c=2cos(theta)` lies in `[-2,2]`. Hermiticity implies that every
eigenvalue `lambda` is real, and (4.5) shows that `lambda^2` is a nonnegative
root of `P(y,c)`.

## 4.3 A uniform rational bound

Put

```text
B=1561/200,       u=y-B,       t=2-c.
```

Direct substitution in (4.5) gives

```text
P(B+u,2-t)
 =u^4+(761/50)u^3+2u^2t+(1337363/20000)u^2
  +(761/50)ut+(136311081/2000000)u
  +t^2+(119121/20000)t+84332641/1600000000.                     (4.6)
```

Every coefficient in (4.6) is nonnegative and the constant term is positive.
Therefore `P(y,c)>0` whenever `y>=B` and `c<=2`. In particular, no squared
eigenvalue of any unit-circle fiber reaches `B`; hence

```text
rho(H(z))^2<B                                                        (4.7)
```

for every `|z|=1`. Proposition 4.1 now yields

```text
rho(A_(8L,alpha))^2<1561/200                                      (4.8)
```

for both holonomies and every `L>=1`.

## 4.4 Comparison with the conjectured threshold

At `n=32`, the Sturm isolation (3.4)-(3.5) gives

```text
rho_-(32)^2>7809/1000>1561/200.                                  (4.9)
```

For `n>=32`, both angles `2pi/n` and `4pi/n` lie in `(0,pi)` and decrease as
`n` increases. Since cosine decreases with its argument on `(0,pi)`, equation
(2.12) shows that `rho_-(n)^2` increases with `n`. Thus

```text
rho_-(n)^2>=rho_-(32)^2>1561/200.                                (4.10)
```

Combining (4.8) and (4.10) proves Theorem B for `n=8L`, `L>=4`. `square`

The restriction to multiples of eight comes from the construction, not from
the threshold comparison. No conclusion is drawn here for other even orders.
