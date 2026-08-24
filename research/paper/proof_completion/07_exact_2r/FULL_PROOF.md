# Full Proof

## 1. Certified one-interface inputs

For either G6 orientation, the infinite squared operator satisfies

```text
ker(H_6-c6)=span{psi_+,psi_-},
dim ker(H_6-c6)=2,                                    (1)
```

where `psi_+` and `psi_-` are orthonormal eigenvectors of the unsquared
operator at `+sqrt(c6)` and `-sqrt(c6)`. On the orthogonal complement of
(1),

```text
H_6<=c6-1/100.                                        (2)
```

For every one of the eight period-eight cuts, both stable multipliers have
modulus below

```text
q_F=9/25,                                             (3)
```

and the selected two-column Floquet bases have condition number below `17`.
These statements are uniform under reflection and the two tail directions.

## 2. Cutoffs and tail bounds

Order the interface centers cyclically. On each intervening arc retain a
plateau of length `S=floor(D/4)` at both ends and join adjacent plateaux by a
sine/cosine partition of unity. For `r=1`, use one interface cutoff and one
bulk cutoff with a zero plateau containing a possible holonomy seam. Range
four then prevents the seam from entering an interface block.

Let

```text
L_site=S-12,
ell=floor(L_site/8).
```

The eight site residues, two tails, condition-number bound, and geometric
series give, for either normalized local mode,

```text
||psi_tail||^2
 <=16*17^2/(1-q_F^2) q_F^(2ell)
 =10625/2 q_F^(2ell)
 <73^2 q_F^(2ell).                                   (4)
```

Let `chi_j` be the cutoff at interface `j` and set

```text
phi_(j,+)=chi_j psi_(j,+),
phi_(j,-)=chi_j psi_(j,-).                            (5)
```

Collect the `m=2r` columns in a map `Phi:C^m->C^n` and put `G=Phi^*Phi`.
The same-interface cross term is not set to zero: by orthogonality of the
full modes,

```text
|<phi_(j,+),phi_(j,-)>|
 <=73^2 q_F^(2ell).                                  (6)
```

The same estimate holds for different-interface overlaps because both
vectors are then in their tails. Hence

```text
||G-I_m||<=m*73^2 q_F^(2ell).                         (7)
```

The hypothesis `D>=1040` gives `S>=260`, `L_site>=248`, and `ell>=31`.
Since `m<=6`, exact arithmetic yields

```text
6*73^2 q_F^62<1/2.                                   (8)
```

Thus the columns in (5) are independent and

```text
||G^(-1)||<=2.                                       (9)
```

## 3. Residual and lower count

The row-sum estimate gives `||H||<=16`, while `c6<8`. Cutting an exact local
mode only in its tails and using (4) yields

```text
||(H-c6)phi_(j,+/-)||
 <=(16+8)*73 q_F^ell
 =1752 q_F^ell.                                     (10)
```

Define the isometry

```text
U=Phi G^(-1/2).                                      (11)
```

Combining (9)-(11) for `2r` columns gives

```text
||(H-c6)U||<3504 r q_F^ell<1/400.                    (12)
```

Let `E_W` be the spectral projection of `H` onto
`W=[c6-1/400,c6+1/400]`. If `rank E_W<2r`, some nonzero vector in `ran U`
would be orthogonal to `ran E_W`. The spectral theorem would then give
`||(H-c6)u||>=(1/400)||u||`, contradicting (12). Therefore

```text
rank E_W>=2r.                                        (13)
```

## 4. Codimension-`2r` complement and upper count

Let `V=ran Phi`. If `x` is orthogonal to `V`, then for every interface and
both signs,

```text
<psi_(j,+/-),chi_j x>=<phi_(j,+/-),x>=0.             (14)
```

Thus each localized interface vector is orthogonal to the entire rank-two
space (1), so the local estimate (2) applies. Any extra local block in the
one-interface partition is pure reference bulk and obeys the stronger edge
bound `eta<c6-1/100`.

The sine/cosine partition satisfies the exact range-four IMS estimate

```text
||E_IMS||<=320/T_min^2.                               (15)
```

For `D>=1040`, every transition width is at least `260`, so

```text
||E_IMS||<=320/260^2=4/845.                           (16)
```

Combining (2), (14), and (16) gives

```text
H|_(V^perp)<=c6-1/100+4/845
              =c6-89/16900
              <c6-1/200.                             (17)
```

By the codimension form of min-max, at most `dim V=2r` eigenvalues lie above
`c6-1/200`. Since the whole window `W` lies above that level, (13) sharpens
to

```text
rank E_W=2r.                                         (18)
```

This count includes multiplicity and gives no individual simplicity claim.

## 5. The `2r`-dimensional Feshbach equation

Let

```text
P=UU^*,   Q_perp=I-P,   E=(H-c6)Phi.                  (19)
```

Equation (17) also holds with the orthogonal complement of `ran U`, since
`ran U=V`. For `|z-c6|<=1/400`, the distance from `z` to the spectrum of
`Q_perp H Q_perp` is at least `1/400`, with the usual complex distance off
the real axis.
Therefore, on `ran Q_perp`,

```text
||(Q_perp H Q_perp-z)^(-1)||<=400.                    (20)
```

Block Gaussian elimination of `H-z` with respect to `P+Q_perp=I` gives the Schur
complement

```text
H_eff(z)=U^*HU-U^*H Q_perp
         (Q_perp H Q_perp-z)^(-1)Q_perp H U,          (21)
det(H_eff(z)-z I_(2r))=0.                             (22)
```

The identity in (22) acts in coordinate space; writing `-zP` there would be
dimensionally incorrect.

Using `U=Phi G^(-1/2)` and
`Q_perp H U=Q_perp E G^(-1/2)`, equation (21) becomes

```text
H_eff(z)-c6 I_(2r)
=G^(-1/2)Phi^*E G^(-1/2)
 -G^(-1/2)E^*Q_perp(Q_perp H Q_perp-z)^(-1)
  Q_perp E G^(-1/2).                                 (23)
```

No orthogonality of the uncorrected columns is assumed.

By (9)-(10),

```text
||E G^(-1/2)||^2
 <=2*(2r)*1752^2 q_F^(2ell)
 =r*3504^2 q_F^(2ell).                               (24)
```

Writing (23) as `c6 I_(2r)+T_1+R_2(z)`, equations (20) and (24) imply

```text
||T_1||<=3504 r q_F^ell,
||R_2(z)||<=400 r*3504^2 q_F^(2ell).                 (25)
```

The exact inequality

```text
400*3504^2*(9/25)^31<1                              (26)
```

and `ell>=31` turn (25) into `||R_2(z)||<r q_F^ell`.
Every root of (22) in the fixed window consequently satisfies

```text
|lambda_j-c6|<3505 r q_F^ell.                        (27)
```

Together, (18) and (27) prove the theorem.

## 6. Exact scope and historical correction

The proof used `r<=3` in the uniform Gram estimate and `D>=1040` in the tail
and IMS bounds. It allows both orientations and both holonomies because the
local inputs are uniform and the seam can be gauged into a zero plateau. It
does not prove the theorem for arbitrary `r` or smaller separation.

Most importantly, (1) supplies two modes at each interface. Replacing the
`2r` columns in (5) by one column per interface would make (14) false on the
missing local mode and would invalidate the upper count. This is why the
historical exact-`r`, codimension-`r`, and `r x r` statements cannot be
recovered from this argument.
