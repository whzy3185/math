# Phase-Slip Interaction: Valid Reduction and Open Coefficients

Status: exact `2r` reduction `COMPUTER_ASSISTED_PROVED`; explicit leading interaction,
finite-ring simplicity, and genuine three-body interaction are `OPEN`.

## 1. Statement

The former one-mode-per-interface, `r x r` problem-specific Feshbach model is
withdrawn. A single G6 interface contributes two squared modes at `c6`, coming
from the simple unsquared levels `+sqrt(c6)` and `-sqrt(c6)`. Therefore an
`r`-interface interaction theory must start with `2r` localized columns.

By the independently verified Task 55 exact-`2r` cluster certificate,
separated G6 interfaces with `r in {1,2,3}` admit the exact
coordinate-space reduction

```text
H_eff(z)
 = U^* H U-U^* H Q(QHQ-z)^(-1)QHU,

det(H_eff(z)-z I_(2r))=0,                             (1)
```

where `U` is the Gram-orthonormalized `2r`-column localized-mode map and
`Q=I-UU^*`. In the fixed cluster window this reduction has the form

```text
H_eff(z)=c6 I_(2r)+T1+R2(z),                          (2)
```

with the explicit norm scale recorded by the candidate Task 55 certificate,

```text
||T1|| <=3504 r (9/25)^ell,
||R2(z)|| <=400 r 3504^2 (9/25)^(2ell).               (3)
```

Equations (1)--(3) are a localization and error theorem. They are not an
asymptotic formula for any individual matrix entry.

## 2. Evidence

The exact algebraic rank correction is

```text
K^2=-I,   KA=-AK,   KH=HK,
rank P_(H6,{c6})=2.
```

Two independent mathematical audits accepted the resulting `2r` dimension,
the codimension-`2r` complement estimate, and the constants in (3). The
producer, implementation-independent checker, and 29 fail-closed tests now
agree, and the certificate records `INDEPENDENT_CHECKER_PASS`. Thus (1)--(3)
are accepted. This acceptance does not add any entrywise asymptotic or
simplicity statement.

The inherited 80/120/160-digit transfer-Evans computations remain useful
discovery evidence for representative two- and three-interface rings. They
resolve roots below ordinary finite-matrix precision and preserve orientation
and holonomy data. They do not certify a universal coefficient or remainder
expansion.

## 3. Exact algebra that is already safe

For a static Hermitian `2 x 2` interaction matrix

```text
M = [ a       t ]
    [ conj(t) b ],
```

the two eigenvalues are distinct exactly when

```text
(a-b)^2+4|t|^2>0.                                    (4)
```

Thus a verified nonzero off-diagonal interaction, or unequal diagonal
corrections, would imply simplicity for that static two-level model. Formula
(4) is an abstract criterion; no present proof identifies the physical
finite-ring reduction with such a static matrix to the precision needed to
apply it.

For a static Hermitian three-site pairwise matrix with zero diagonal and

```text
T_12=a,   T_23=b,   T_31=c,
```

one has

```text
det(lambda I-T)
 =lambda^3-lambda(|a|^2+|b|^2+|c|^2)-2 Re(abc).       (5)
```

The gauge-invariant cycle product `Re(abc)` in (5) is built entirely from the
three pairwise entries. Its appearance is therefore not evidence of a genuine
three-body interaction.

## 4. Exact limitation

No current certificate proves any of the following:

1. a nonzero normalized limit for an entry of `T1`;
2. a universal two-arc coefficient or a universal orientation/holonomy sign;
3. simplicity of the individual `2r` finite-ring levels;
4. a pairwise-additive leading `r=3` Hamiltonian;
5. a nonzero genuine three-body coefficient; or
6. a three-body remainder smaller than the pairwise terms after all Gram and
   energy-dependent corrections are included.

The norm estimate (3) permits cancellations. It cannot distinguish a zero
leading coefficient from a nonzero one, and it cannot by itself separate
cluster levels. High-precision splitting tables do not repair this logical
gap.

## 5. Dependencies

- Verified physical dependency: `certificates/exact_2r_cluster.json` and its
  independent checker both PASS.
- Required single-interface inputs: the exact G6 rank-two symmetry, the global
  edge `sup sigma(H6)=c6`, and the complement gap `1/100`.
- Required analytic inputs: phase-uniform Floquet decay, the `2r` Gram bound,
  and the codimension-`2r` complementary resolvent.
- Not a valid dependency: the withdrawn exact-`r` count or the old `r x r`
  Feshbach application.

## 6. Next lemma

The next theorem-level target is an interval-certified coefficient lemma. For
each orientation, holonomy, and relevant separation residue, it should prove
an expansion of the complete `2r x 2r` first interaction block,

```text
T1=q^ell T_lead+E_ell,
||E_ell|| <=C q^(ell+1),
```

with an exact enclosure for `T_lead`. A nondegeneracy bound on the eigenvalue
gaps of `T_lead` stronger than the certified error would then convert the
abstract simplicity criteria into a physical finite-ring theorem. For
`r=3`, a genuine three-body claim additionally requires a gauge-invariant
definition obtained by subtracting all consistently normalized one- and
two-interface contributions.
