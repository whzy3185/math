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

The named [Patch Identification Lemma](PATCH_IDENTIFICATION_LEMMA.md) fixes
the finite-ring geometry. Order the left endpoints `p_j` of the G6 gaps
cyclically, put `S=floor(D/4)` and `a=S-8`, and use one interface cutoff
`chi_j` at each `p_j` and one pure-bulk cutoff `beta_j` on every intervening
arc. Each interface-to-bulk transition is a sine/cosine transition of width
`S`; the middle pure-bulk plateau has length at least 16. Thus

```text
sum_j chi_j^2+sum_j beta_j^2=1.                      (4)
```

The lemma proves, for `r=1,2,3`, both orientations, both `tau` lifts, both
holonomies, and cyclic wraparound, that every range-four interface patch is
exactly a finite section of `H_6` after translation, optional reflection,
and diagonal switching. Every `beta_j` patch is a finite section of the
period-eight reference bulk. A holonomy seam is placed in a bulk plateau at
distance at least eight from every interface support.

Let

```text
L_site=S-12,
ell=floor(L_site/8).
```

Indeed, `chi_j` begins changing at distance `S-8`; subtracting the
propagation range four gives `L_site=S-12`. This is the same cutoff used in
the mode transport and in the local complement estimate.

The eight site residues, two tails, condition-number bound, and geometric
series give, for either normalized local mode,

```text
||psi_tail||^2
 <=16*17^2/(1-q_F^2) q_F^(2ell)
 =10625/2 q_F^(2ell)
 <73^2 q_F^(2ell).                                   (5)
```

Let `chi_j` be the cutoff at interface `j` and set

```text
phi_(j,+)=chi_j psi_(j,+),
phi_(j,-)=chi_j psi_(j,-).                            (6)
```

Collect the `m=2r` columns in a map `Phi:C^m->C^n` and put `G=Phi^*Phi`.
These are precisely the transported-and-truncated vectors defined in the
Patch Identification Lemma. The full transported pair is normalized and
orthogonal before truncation.
The same-interface cross term is not set to zero: by orthogonality of the
full modes,

```text
|<phi_(j,+),phi_(j,-)>|
 <=73^2 q_F^(2ell).                                  (7)
```

The same estimate holds for different-interface overlaps because both
vectors are then in their tails. Hence

```text
||G-I_m||<=m*73^2 q_F^(2ell).                         (8)
```

The hypothesis `D>=1040` gives `S>=260`, `L_site>=248`, and `ell>=31`.
Since `m<=6`, exact arithmetic yields

```text
6*73^2 q_F^62<1/2.                                   (9)
```

Thus the columns in (6) are independent and

```text
||G^(-1)||<=2.                                      (10)
```

## 3. Residual and lower count

The row-sum estimate gives `||H||<=16`, while `c6<8`. Cutting an exact local
mode only in its tails and using (5) yields

```text
||(H-c6)phi_(j,+/-)||
 <=(16+8)*73 q_F^ell
 =1752 q_F^ell.                                     (11)
```

Define the isometry

```text
U=Phi G^(-1/2).                                      (12)
```

Combining (10)-(12) for `2r` columns gives

```text
||(H-c6)U||<3504 r q_F^ell<1/400.                    (13)
```

Let `E_W` be the spectral projection of `H` onto
`W=[c6-1/400,c6+1/400]`. If `rank E_W<2r`, some nonzero vector in `ran U`
would be orthogonal to `ran E_W`. The spectral theorem would then give
`||(H-c6)u||>=(1/400)||u||`, contradicting (13). Therefore

```text
rank E_W>=2r.                                       (14)
```

## 4. Codimension-`2r` complement and upper count

Let `V=ran Phi`. If `x` is orthogonal to `V`, then for every interface and
both signs,

```text
<psi_(j,+/-),chi_j x>=<phi_(j,+/-),x>=0.             (15)
```

This is where the Patch Identification Lemma is required before the
single-G6 complement gap can be invoked. It proves that `chi_j x` is a
vector in the same canonical infinite G6 finite section as the transported
pair in (15). Thus each localized interface vector is orthogonal to the
entire rank-two space (1), so the local estimate (2) applies. The lemma also
identifies every noninterface vector `beta_j x` with a period-eight
reference-bulk vector, giving the stronger bound `eta<c6-1/100`.

The sine/cosine partition has transition width `S>=260` and satisfies the
exact range-four IMS estimate

```text
||E_IMS||<=320/S^2.                                  (16)
```

For `D>=1040`,

```text
||E_IMS||<=320/260^2=4/845.                          (17)
```

Combining (2), (15), and (17) gives

```text
H|_(V^perp)<=c6-1/100+4/845
              =c6-89/16900
              <c6-1/200.                            (18)
```

By the codimension form of min-max, at most `dim V=2r` eigenvalues lie above
`c6-1/200`. Since the whole window `W` lies above that level, (14) sharpens
to

```text
rank E_W=2r.                                        (19)
```

This count includes multiplicity and gives no individual simplicity claim.

## 5. The `2r`-dimensional Feshbach equation

Let

```text
P=UU^*,   Q_perp=I-P,   E=(H-c6)Phi.                 (20)
```

Equation (18) also holds with the orthogonal complement of `ran U`, since
`ran U=V`. For `|z-c6|<=1/400`, the distance from `z` to the spectrum of
`Q_perp H Q_perp` is at least `1/400`, with the usual complex distance off
the real axis.
Therefore, on `ran Q_perp`,

```text
||(Q_perp H Q_perp-z)^(-1)||<=400.                   (21)
```

Block Gaussian elimination of `H-z` with respect to `P+Q_perp=I` gives the Schur
complement

```text
H_eff(z)=U^*HU-U^*H Q_perp
         (Q_perp H Q_perp-z)^(-1)Q_perp H U,         (22)
det(H_eff(z)-z I_(2r))=0.                            (23)
```

The identity in (23) acts in coordinate space; writing `-zP` there would be
dimensionally incorrect.

Using `U=Phi G^(-1/2)` and
`Q_perp H U=Q_perp E G^(-1/2)`, equation (22) becomes

```text
H_eff(z)-c6 I_(2r)
=G^(-1/2)Phi^*E G^(-1/2)
 -G^(-1/2)E^*Q_perp(Q_perp H Q_perp-z)^(-1)
  Q_perp E G^(-1/2).                                (24)
```

No orthogonality of the uncorrected columns is assumed.

By (10)-(11),

```text
||E G^(-1/2)||^2
 <=2*(2r)*1752^2 q_F^(2ell)
 =r*3504^2 q_F^(2ell).                              (25)
```

Writing (24) as `c6 I_(2r)+T_1+R_2(z)`, equations
(13), (21), and (25) imply

```text
||T_1||<=3504 r q_F^ell,
||R_2(z)||<=400 r*3504^2 q_F^(2ell).                (26)
```

The exact inequality

```text
400*3504^2*(9/25)^31<1                             (27)
```

and `ell>=31` turn (26) into `||R_2(z)||<r q_F^ell`.
Every root of (23) in the fixed window consequently satisfies

```text
|lambda_j-c6|<3505 r q_F^ell.                       (28)
```

Together, (19) and (28) prove the theorem.

## 6. Exact scope and historical correction

The proof used `r<=3` in the uniform Gram estimate and `D>=1040` in the tail,
seam-clearance, and IMS bounds. The Patch Identification Lemma treats both
orientations, both `tau` lifts, both holonomies, and wraparound coefficient by
coefficient. It does not prove the theorem for arbitrary `r` or smaller
separation.

Most importantly, (1) supplies two modes at each interface. Replacing the
`2r` columns in (6) by one column per interface would make (15) false on the
missing local mode and would invalidate the upper count. This is why the
historical exact-`r`, codimension-`r`, and `r x r` statements cannot be
recovered from this argument.
