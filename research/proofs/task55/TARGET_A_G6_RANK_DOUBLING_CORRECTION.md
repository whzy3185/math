# G6 Rank-Doubling Correction

## Corrected Theorem

For the infinite single-G6 signed adjacency `A_6`, the positive Evans root
`+sqrt(c6)` and its negative partner `-sqrt(c6)` are both simple. Therefore
the squared operator `H_6=A_6^2` has

```text
rank P_(H_6,{c6}) = 2.                                (1)
```

Consequently, the Task 54 statements asserting exactly `r` squared levels
for `r` separated G6 interfaces, a codimension-`r` complement gap, and an
`r x r` Feshbach matrix are false as stated. The corrected construction uses
two localized modes per interface and has dimension `2r`.

This correction does not affect the theorem that every even `n>=48` has an
explicit certified counterexample.

## Exact Anticommuting Symmetry

In the infinite tree gauge,

```text
(A_6 u)_i = u_(i-1)+u_(i+1)+tau_(i-2)u_(i-2)+tau_i u_(i+2).   (2)
```

The G6 word obeys

```text
Q_(6-i)=Q_i,
tau_(7-i)=-tau_i.                                     (3)
```

Define

```text
(Ku)_i=(-1)^i u_(9-i).                                (4)
```

Applying (4) twice gives

```text
(K^2u)_i=(-1)^i(-1)^(9-i)u_i=-u_i.                   (5)
```

For `j=9-i`, equations (2) and (3) give

```text
(KAu)_i=(-1)^i[u_(8-i)+u_(10-i)
                    +tau_(7-i)u_(7-i)+tau_(9-i)u_(11-i)]
        =-(AKu)_i.                                    (6)
```

Hence

```text
K^2=-I,       KA=-AK,       KH=HK.                    (7)
```

The producer and independent checker also construct symmetric open windows
of dimensions 58, 90, and 138 and verify all three integer matrix identities
in (7) entry by entry. These windows are controls; the infinite identity is
the coefficient calculation (6).

## Multiplicity

Task 50 proves one simple physical positive root in the certified `c6`
interval. If `A psi_+=sqrt(c6) psi_+`, then (7) gives

```text
A(K psi_+)=-sqrt(c6)(K psi_+).                         (8)
```

The two vectors belong to distinct eigenvalues of self-adjoint `A`, so they
are orthogonal. Positive-root simplicity and symmetry show that the negative
root is also simple. The `H` eigenspace at `c6` is the direct sum of the `A`
eigenspaces at `+sqrt(c6)` and `-sqrt(c6)`. This proves (1).

The Task 53 global-edge argument classifies the positive branch. Equation
(7) supplies the missing negative-spectrum bridge: any negative level with
larger absolute value would map to an excluded positive level. Thus

```text
sup sigma(H_6)=c6                                      (9)
```

remains valid, now with squared multiplicity two.

## Corrected Separated-Interface Space

For each interface use

```text
phi_(j,+)=chi_j psi_(j,+),
phi_(j,-)=chi_j psi_(j,-),
V_L=span{phi_(j,+),phi_(j,-):1<=j<=r}.                (10)
```

If `x` is orthogonal to `V_L`, then every localized vector `chi_j x` is
orthogonal to the full rank-two G6 eigenspace. The Task 54 cutoff partition
and its IMS error are unchanged. Therefore the corrected complement proof,
once the two-mode certificate is bound, has codimension `2r`, and the
effective matrix is

```text
H_eff(z)=c6 I_(2r)+T_1+R_2(z),
H_eff(z)-z I_(2r).                                    (11)
```

The old coordinate expression `H_eff-zP` was dimensionally wrong.

## Surviving Main Theorem

For `48<=n<240`, every certificate directly proves `tI-A_n^2` positive
definite by exact rational LDL. For `n>=240`, the global IMS argument uses
only the local quadratic-form cap `sup sigma(H_6)=c6`, not its multiplicity.
Together they still prove

```text
every even n>=48 has an explicit rigorously certified counterexample.      (12)
```

Evidence status: rank correction `COMPUTER_ASSISTED_PROVED`; old exact-`r`
claim `FALSIFIED_AS_STATED`; corrected exact-`2r` cluster and Feshbach theorem
`COMPUTER_ASSISTED_PROVED` with `INDEPENDENT_CHECKER_PASS`.
