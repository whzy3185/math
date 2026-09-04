# Half-period chiral criterion

**Verdict:** PASS, strong version.  Within the explicitly delimited natural
class “alternating diagonal sign times half-period translation,” the criterion
is necessary and sufficient and has an equivalent local-flux formulation.

**Proof status:** analytic proof closed; independent exact matrix audit passed
for every sign word through period twelve.  No Lean formalization was added.

## 1. Operator setting

Let `p=2m` and let `tau` be a `2m`-periodic sign word.  On bi-infinite
sequences define

```text
(A_tau x)_i
 = x_(i-1)+x_(i+1)
   +tau_(i-2)x_(i-2)+tau_i x_(i+2).
```

Let

```text
(D x)_i   = (-1)^i x_i,
(T_m x)_i = x_(i+m),
K_m       = D T_m.
```

This is the natural monomial half-cell class studied here.  The theorem does
not classify arbitrary unitary involutions.

## 2. Direct anticommutator calculation

For every sequence `x`, direct substitution gives

```text
((A_tau K_m+K_m A_tau)x)_i
 =(-1)^i [
    (tau_(i-2)+tau_(i+m-2)) x_(i+m-2)
   +(tau_i+tau_(i+m))         x_(i+m+2)
 ].
```

The displacement-one terms cancel because `D` changes their sign.  The
displacement-two terms cancel exactly when the coefficient word changes sign
under the half-period translation.

### Theorem 2.1 — operator criterion

The following are equivalent:

1. `K_m A_tau=-A_tau K_m`;
2. `tau_(i+m)=-tau_i` for every integer `i`.

### Proof

Condition 2 makes both coefficients in the displayed anticommutator zero, so
it is sufficient.  Conversely, if the anticommutator is zero on all sequences,
the coefficient of `x_(i+m+2)` is zero for every `i`; hence
`tau_(i+m)=-tau_i`.  This also makes the other coefficient zero.  No parity
case split is needed for anticommutation itself.

## 3. Correct Bloch normalization

For `|z|=1`, let `B_z` be the `2m`-dimensional Bloch space

```text
x_(i+2m)=z x_i.
```

Both `D` and `T_m` preserve `B_z`, because the full period is even.  On this
space,

```text
T_m^2=z I,
T_m D=(-1)^m D T_m,
```

and therefore

```text
K_m^2=(-1)^m z I.
```

Choose a unit scalar `gamma_m(z)` satisfying

```text
gamma_m(z)^2=(-1)^m z^(-1).
```

Such a scalar always exists.  If `xi^2=z`, one may take

```text
gamma_m(z)=xi^(-1)     when m is even,
gamma_m(z)=i xi^(-1)   when m is odd.
```

The normalized fiber operator

```text
J_z=gamma_m(z) K_m|_(B_z)
```

is unitary and satisfies `J_z^2=I`.  Hence it is also self-adjoint.  The two
choices of square root replace `J_z` by `-J_z` and only exchange its two
eigenspaces.

### Corollary 3.1 — fiberwise chiral involution

If `tau_(i+m)=-tau_i`, then for every unit Bloch phase `z`,

```text
J_z H_tau(z)=-H_tau(z)J_z.
```

For `m=4`, the normalization is `gamma_4(z)=xi^(-1)`, exactly the scalar in
the frozen period-eight involution.

## 4. Gauge-invariant local-flux formulation

Define the defect/local-square word

```text
Q_i=tau_i tau_(i+1).
```

### Theorem 4.1 — flux criterion

For a `2m`-periodic sign word, the following are equivalent:

1. `tau_(i+m)=-tau_i` for all `i`;
2. `Q_(i+m)=Q_i` for all `i` and
   `prod_(j=0)^(m-1) Q_j=-1`.

Thus a natural monomial half-cell chiral involution exists exactly when the
local defect word is half-periodic and carries negative flux over one
half-cell.

### Proof

If `tau_(i+m)=-tau_i`, then

```text
Q_(i+m)=(-tau_i)(-tau_(i+1))=Q_i.
```

The product telescopes because every interior `tau` occurs twice:

```text
prod_(j=0)^(m-1) Q_j=tau_0 tau_m=-1.
```

Conversely, put `r_i=tau_(i+m)/tau_i`, which lies in `{+1,-1}`.  The identity
`Q_(i+m)=Q_i` gives `r_i r_(i+1)=1`, so all `r_i` are equal to one constant
`r`.  The same telescoping product gives

```text
r=tau_m/tau_0=prod_(j=0)^(m-1)Q_j=-1.
```

Hence `tau_(i+m)=-tau_i` for every `i`.

The criterion uses `Q` only and is therefore independent of the choice of its
lift `tau` or `-tau`.

## 5. General algebraic consequences

The half-shift has no fixed coordinate, so `J_z` has trace zero.  Since it is
an involution on a `2m`-dimensional space, its `+1` and `-1` eigenspaces both
have dimension `m`.  Anticommutation sends each eigenspace of `J_z` to the
other.  In a unitary basis adapted to these eigenspaces,

```text
H_tau(z) ~ [[0, B(z)^*],
            [B(z),   0 ]].
```

It follows immediately that:

- the spectrum is symmetric about zero;
- the characteristic polynomial is even;
- the squared problem is the pair of `m x m` positive semidefinite matrices
  `B(z)^*B(z)` and `B(z)B(z)^*`;
- in particular,

```text
det(lambda I_(2m)-H_tau(z))
 =det(lambda^2 I_m-B(z)^*B(z)).
```

No claim is made that the resulting `m x m` spectrum is explicitly solvable
for general `m`.

## 6. Period eight as the first sub-eight realization

For

```text
tau_*=(1,1,-1,1,-1,-1,1,-1),
```

the second half is the negative of the first.  Its local word is

```text
Q_*=(1,-1,-1,-1,1,-1,-1,-1),
```

which is four-periodic and whose first-half product is `-1`.  The general
criterion therefore produces the known period-eight chiral involution and
explains the `8 x 8 -> 4 x 4` reduction structurally.

Shorter periods can also satisfy the chiral criterion—the alternating
period-two phase is the simplest example—but the minimal-period theorem shows
that none has squared edge below eight.  Thus the period-eight target is the
first **sub-eight spectral realization** of the general half-cell mechanism,
not the first chiral word in an absolute sense.

## 7. Scope and article value

This theorem supplies the missing bridge

```text
negative half-cell flux
 -> monomial chiral involution
 -> even characteristic polynomial
 -> half-dimensional squared problem.
```

It upgrades the period-eight anticommutation from an isolated matrix trick to
a gauge-invariant structural mechanism.  It does not classify all chiral
symmetries, all low-edge periodic words, or any general `m x m` spectrum.

## 8. Independent audit

Run

```text
uv run --with sympy python \
  research/paper_strengthening/verifiers/verify_symmetry_and_chiral.py
```

The verifier constructs the fibers directly from the operator, checks
`K_m^2=(-1)^m z I`, exhaustively confirms the iff and flux equivalence for
every sign word of even displayed period at most twelve, and checks the target
word.  The analytic proof is the coefficient calculation above.
