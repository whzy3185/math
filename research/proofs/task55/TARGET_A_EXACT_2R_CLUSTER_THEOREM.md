# Exact-2r Cluster Theorem for Separated G6 Interfaces

Status: `EXACT_2R_R123_CLUSTER_PROVED` / `COMPUTER_ASSISTED_PROVED`.

Mathematical audit status: `TWO_INDEPENDENT_MATHEMATICAL_AUDITS_PASSED`
(`PASS`, then `PASS_WITH_SHARPENING`). Integration status:
`INDEPENDENT_CHECKER_PASS`. The independent exact-`2r` checker and 29 tamper
tests pass.

## Theorem

Let `H=A^2` be a legal finite-ring squared signed adjacency consisting of
exactly `r in {1,2,3}` G6 interfaces and period-eight bulk elsewhere. Both G6
orientations and both finite-ring holonomies are allowed. If the minimum
cyclic site distance `D` between interfaces satisfies `D>=1040`, set

```text
S=floor(D/4),
L_site=S-12,
ell=floor(L_site/8),
q=9/25.
```

Then

```text
rank 1_[c6-1/400,c6+1/400](H)=2r.                     (1)
```

Writing the eigenvalues in this window with multiplicity as
`lambda_1,...,lambda_(2r)`, one has

```text
|lambda_j-c6| < 3505 r q^ell,   1<=j<=2r.             (2)
```

The theorem counts multiplicity. It does not assert that the finite-ring
levels are individually simple.

## Computer-assisted inputs

The proof uses three certified single-interface facts.

1. The positive unsquared G6 Evans root `+sqrt(c6)` is simple.
2. The global squared spectral edge is `sup sigma(H6)=c6`.
3. On the complement of the complete `c6` eigenspace,

```text
H6 <= c6-1/100.                                       (3)
```

The producer binds these inputs by content hash and contract checks. It also
reconstructs all eight cuts of the period-eight 4x4 bulk monodromy using exact
rational interval arithmetic. Both stable multipliers have modulus below
`q=9/25`. For right stable propagation and left backward propagation, exact
Cauchy--Binet bounds on the selected two-column Floquet bases give condition
number strictly below 17 in every phase.

Everything after these single-interface and Floquet inputs is analytic.

## Rank two at one interface

In the infinite tree gauge,

```text
(Au)_i=u_(i-1)+u_(i+1)+tau_(i-2)u_(i-2)+tau_i u_(i+2).
```

The G6 coefficients satisfy `tau_(7-i)=-tau_i`. Define

```text
(Ku)_i=(-1)^i u_(9-i).
```

Direct substitution gives

```text
K^2=-I,             KA=-AK,             KH=HK.        (4)
```

If `A psi_+=sqrt(c6) psi_+`, put `psi_-=K psi_+`. Then
`A psi_-=-sqrt(c6) psi_-`. Since `A` is self-adjoint, the two vectors are
orthogonal. Simplicity of the positive root and (4) imply simplicity of the
negative root. Consequently

```text
ker(H6-c6)=span{psi_+,psi_-}                           (5)
```

has dimension two. Reflection and local switching transport (4)--(5) by
unitary conjugacy, so both interface orientations have the same conclusion.

## Tail and Gram estimates

The phase-uniform Floquet bounds imply, for either normalized mode,

```text
||psi_(+/-),tail||^2
 <=16*17^2/(1-q^2) q^(2ell)
 =10625/2 q^(2ell)
 <73^2 q^(2ell).                                      (6)
```

Choose the Task 54 sine/cosine partition. For each interface let `chi_j=1`
on its central plateau and put

```text
phi_(j,+)=chi_j psi_(j,+),
phi_(j,-)=chi_j psi_(j,-),
Phi=(phi_(1,+),phi_(1,-),...,phi_(r,+),phi_(r,-)).     (7)
```

The same-interface cross term is not discarded. Orthogonality in (5) gives

```text
|<phi_(j,+),phi_(j,-)>|
 =|<psi_(j,+),(1-chi_j^2)psi_(j,-)>|
 <=73^2 q^(2ell).                                     (8)
```

Different-interface overlap occurs only where both vectors are in their
tails and obeys the same bound. Thus, for `G=Phi^*Phi`, `m=2r<=6`,

```text
||G-I_m|| <=m*73^2 q^(2ell)
 <=6*73^2 q^62 <1/2.                                  (9)
```

Hence the `2r` columns are linearly independent and `||G^(-1)||<=2`.

## Codimension-2r complement

Let `V=ran Phi` and let `Q_V` be the orthogonal projection onto `V^perp`. If
`x in V^perp`, then for both signs and every interface,

```text
<psi_(j,+/-),chi_j x>=<chi_j psi_(j,+/-),x>=0.         (10)
```

The local interface vector is therefore orthogonal to the complete rank-two
space (5), so (3) applies. In the `r=1` partition the second local block is
pure bulk and has spectral top below `c6-1/100`.

For `D>=1040`, `S>=260`, `L_site>=248`, and `ell>=31`. The single-interface
transition width is at least 260; for `r=2,3`, every middle transition has
width at least `D-2S>=520`. The exact range-four IMS estimate is therefore

```text
||E_IMS|| <=320/260^2=4/845.                           (11)
```

A holonomy cut may be placed in an excluded plateau. Range four cannot carry
it into an interface block. Combining (3), (10), and (11) gives

```text
Q_V H Q_V <=c6-1/100+4/845
             =c6-89/16900
             <c6-1/200,                               (12)
```

where the final strict surplus is `9/33800`.

## Exact count

From (6), `||H||<=16`, and `c6<8`, each column in (7) satisfies

```text
||(H-c6)phi_(j,+/-)|| <=24*73 q^ell=1752 q^ell.        (13)
```

After Gram orthonormalization `U=Phi G^(-1/2)`, (9)--(13) yield

```text
||(H-c6)U|| <3504 r q^ell.                             (14)
```

For `r<=3` and `ell>=31`, the right side is strictly below `1/400`. If the
spectral projection onto the window in (1) had rank below `2r`, a nonzero
vector in `ran U` would be orthogonal to that projection. The spectral theorem
would then force its residual to be at least `1/400`, contradicting (14).
Thus the window has rank at least `2r`.

By (12) and the codimension form of min--max, at most `2r` eigenvalues can lie
above `c6-1/200`. The fixed window lies strictly above that number. It follows
that its rank is exactly `2r`, proving (1). The Feshbach estimate in the
companion theorem gives (2).

The `n=100` and `n=102` calculations are not inputs to this proof and are not
used as substitutes for the hypothesis `D>=1040`.

Certificate: `certificates/exact_2r_cluster.json`.
Producer: `../../scripts/target_a_task55_exact_2r.py`.
