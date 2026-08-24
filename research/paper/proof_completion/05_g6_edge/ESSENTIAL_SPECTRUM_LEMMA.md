# Essential Spectrum and Tail Matching for the G6 Interface

Let `A_6` and `H_6=A_6^2` be the operators in `THEOREM_STATEMENT.md`.  Let
`H_L` and `H_R` be the two whole-line periodic squared operators obtained by
continuing, respectively, the left and right tails of `H_6` across all of
`Z`.  Both are translated and diagonally switched copies of the reference
period-eight operator `H_ref`.

## Lemma

The operator `H_6` is a bounded self-adjoint finite-range operator and

```text
sigma_ess(H_6)=sigma(H_L) union sigma(H_R)=sigma(H_ref).       (E1)
```

In particular,

```text
sup sigma_ess(H_6)=eta=4+sqrt(10+2sqrt(5)).                    (E2)
```

Every point `y>eta` in `sigma(H_6)` is an isolated eigenvalue of finite
multiplicity.  Its eigenvectors have exponentially decaying tails.  More
precisely, after decomposing an `H_6` eigenvector into its `A_6` eigenparts at
`lambda=+sqrt(y)` and `lambda=-sqrt(y)`, each nonzero part satisfies the
stable/unstable plane matching condition used by the G6 Evans determinant.

## Proof

### 1. Boundedness, self-adjointness, and finite range

The matrix of `A_6` is real and symmetric.  Indeed, the coefficient of
`u_(i+2)` in row `i` is `tau_i`, and the coefficient of `u_i` in row `i+2`
is the same number.  Every row has four entries of absolute value one.
Schur's test therefore gives

```text
||A_6||<=4.
```

Thus `A_6` is a bounded self-adjoint operator of range two.  Consequently
`H_6=A_6^2` is bounded and self-adjoint, has range four, and satisfies
`0<=H_6<=16I`.

### 2. Decoupling the two periodic tails

Choose integers `a<b` beyond the finite interface core, far enough that the
matrix coefficients of `H_6` agree with those of `H_L` on the left of `a`
and with those of `H_R` on the right of `b`.  Write

```text
ell^2(Z)=ell^2((negative infinity,a]) direct_sum ell^2([a+1,b-1])
         direct_sum ell^2([b,positive infinity)).                 (E3)
```

Let `H_L^-` and `H_R^+` be the Dirichlet compressions of `H_L` and `H_R` to
the first and third summands, and let `F` be any self-adjoint operator on the
finite middle summand, for instance the corresponding compression of `H_6`.
Define

```text
H_dec=H_L^- direct_sum F direct_sum H_R^+.                        (E4)
```

Because all three operators have range four, `H_6-H_dec` can have nonzero
matrix entries only in finitely many rows or columns: those meeting the
finite core or one of the two cuts.  Hence `H_6-H_dec` has finite rank.
Compact invariance of the essential spectrum and the direct-sum rule give

```text
sigma_ess(H_6)=sigma_ess(H_L^-) union sigma_ess(H_R^+).            (E5)
```

The finite-dimensional summand `F` contributes no essential spectrum.

### 3. A periodic half-line has the whole-line essential spectrum

We prove the assertion for the right compression `B^+` of an arbitrary
bounded self-adjoint periodic finite-range operator `B` on `ell^2(Z)`.  The
left compression is identical after reversing the lattice.

First let `x in sigma(B)`.  Floquet decomposition supplies a nonzero bounded
Bloch solution `v` of `(B-x)v=0`.  Cut `v` off on `L` consecutive period
cells placed arbitrarily far inside the positive half-line.  Since `B` has
finite range, `(B^+-x)` applied to this cutoff is supported in only a fixed
number of sites at its two ends and has norm bounded independently of `L`.
The cutoff itself has norm comparable to `L^(1/2)`.  After normalization and
translation to infinity, these vectors converge weakly to zero and their
residual norms tend to zero.  Weyl's criterion for the essential spectrum
therefore yields

```text
sigma(B) subset sigma_ess(B^+).                                   (E6)
```

Conversely, take `x notin sigma(B)` and put `R=(B-x)^(-1)`.  Let `P` be the
orthogonal projection onto the positive half-line and regard `B^+=PBP` as an
operator on `ran(P)`.  The operator `S=PRP` is a two-sided inverse modulo
finite-rank operators (with `I` below denoting the identity on `ran(P)`):

```text
(B^+-x)S=I-P(B-x)(I-P)RP,
S(B^+-x)=I-PR(I-P)(B-x)P.                                         (E7)
```

Both error terms have finite rank because the cross-boundary operators
`PB(I-P)` and `(I-P)BP` have finite rank.  Hence `B^+-x` is Fredholm, so
`x notin sigma_ess(B^+)`.  Together with (E6), this proves

```text
sigma_ess(B^+)=sigma(B).                                          (E8)
```

Applying (E8) to the two tails in (E5) gives

```text
sigma_ess(H_6)=sigma(H_L) union sigma(H_R).
```

Translation and diagonal switching are unitary conjugacies, so
there are unitaries `U_L,U_R` with

```text
H_L=U_L H_ref U_L^*,       H_R=U_R H_ref U_R^*.
```

Thus `sigma(H_L)=sigma(H_R)=sigma(H_ref)`, which proves (E1).  The exact
Floquet calculation for the reference period-eight operator gives
`sup sigma(H_ref)=eta`, proving (E2).

### 4. Discreteness above the bulk edge

For a bounded self-adjoint operator, every spectral point outside the
essential spectrum is an isolated eigenvalue of finite multiplicity; the
only possible finite accumulation points of such eigenvalues belong to the
essential spectrum.  Equations (E1)-(E2) therefore imply that every
`y in sigma(H_6)` with `y>eta` is discrete and has finite multiplicity.

### 5. Exponential tails and the matching condition

Let `H_6 u=yu`, where `u!=0` and `y>eta`, and set `lambda=sqrt(y)>0`.  Define

```text
u_+=(u+lambda^(-1)A_6u)/2,
u_-=(u-lambda^(-1)A_6u)/2.                                      (E9)
```

Then `u=u_++u_-` and

```text
A_6u_+=lambda u_+,       A_6u_-=-lambda u_-.                    (E10)
```

At least one component is nonzero.  Thus it is enough to consider an
`ell^2` solution of `A_6v=mu v`, where `mu` is either sign of `sqrt(y)`.

On either periodic tail, group the fourth-order recurrence into blocks of
eight sites.  Its monodromy has the reciprocal characteristic polynomial
displayed in `FULL_PROOF.md`; it depends on `mu` through `y=mu^2`.  Since
`y>eta`, no Floquet multiplier lies on the unit circle.  The monodromy
therefore has a two-dimensional stable subspace and a two-dimensional
unstable subspace.

On the right tail, an `ell^2` solution must have zero unstable component:
otherwise inverse iteration on the unstable subspace, whose inverse has
spectral radius less than one, shows that the forward states cannot tend to
zero.  Its right-tail state consequently lies in the stable plane and decays
exponentially.  The same argument under backward iteration shows that the
left-tail state lies in the unstable plane and decays exponentially toward
negative infinity.  Possible Jordan blocks cause only polynomial factors,
which are absorbed by any exponential rate chosen strictly above the stable
spectral radius.  Thus there are constants `C<infinity` and `0<q<1`,
depending on the fixed eigenvalue, such that

```text
|v_i|<=C q^|i|                                                     (E11)
```

outside a fixed finite core.  Equation (E9) then gives the same conclusion
for every `H_6` eigenvector above `eta`.

Finally, the fourth-order transfer recurrence is invertible.  If `U_L(mu)`
is the plane decaying toward negative infinity, `S_R(mu)` is the plane
decaying toward positive infinity, and `D_6(mu)` transports data across the
finite core, the preceding paragraph proves

```text
D_6(mu)U_L(mu) intersect S_R(mu) != {0}.                          (E12)
```

Conversely, a nonzero vector in the intersection extends uniquely to a
bilateral solution with the exponential bounds (E11), hence to an `ell^2`
eigenvector.  Therefore (E12), equivalently the vanishing of the intrinsic
exterior determinant, is necessary and sufficient for every spectral point
above the essential edge.  This completes the proof.
