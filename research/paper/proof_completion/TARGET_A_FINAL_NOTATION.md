# Target A Final Notation

Status: `CANONICAL_CURRENT`.

This file fixes the notation used by the proof-completion package. Historical
documents may use different symbols; those symbols do not override this table.

## Finite Signed Graphs

| Symbol | Meaning |
|---|---|
| `G_n=C_n(1,2)` | The graph on `Z/nZ` with edges at cyclic distances one and two. The paper concerns even `n>=8`. |
| `sigma` | A signing of the edges of `G_n`. |
| `A_sigma` | The real symmetric signed adjacency matrix of `(G_n,sigma)`. |
| `rho(A_sigma)` | The spectral radius of `A_sigma`. |
| `H_sigma=A_sigma^2` | The squared signed adjacency. Its spectral top is `rho(A_sigma)^2`. |
| `m_n` | `min_sigma rho(A_sigma)`, with the minimum over all signings of `G_n`. |
| `rho_-(n)` | The comparison value from the conjecture, with `rho_-(n)^2=4+2cos(2pi/n)+2cos(4pi/n)`. |

Switching by a diagonal matrix with diagonal entries in `{+1,-1}` is denoted
by `A_sigma -> D A_sigma D`. Switching preserves the spectrum. Do not use
`tau` for an arbitrary signing before the Hamilton gauge has been fixed.

## Hamilton Gauge, Flux, And Holonomy

After switching, all step-one signs are placed in the Hamilton-cycle gauge.
On a simply connected arc they are `+1`; the cyclic residual sign is the
Hamilton holonomy

```text
alpha in {+1,-1}.
```

The step-two signs are written

```text
tau=(tau_i),  tau_i in {+1,-1}.
```

The gauge-invariant triangular flux word is

```text
Q_i=tau_i tau_(i+1).
```

On the line, fix `tau_0=1` and lift by

```text
tau_(i+1)=Q_i tau_i.
```

The other lift is `-tau`; its squared operator is unitarily equivalent. On a
ring, `Q` and `alpha` together retain the parity/holonomy information needed
by the finite classifiers.

## Infinite Operator And Squared Operator

For a bilateral `tau` word, use

```text
(A_tau u)_i=u_(i-1)+u_(i+1)
              +tau_(i-2)u_(i-2)+tau_i u_(i+2),
H_tau=A_tau^2.
```

`A_tau` always denotes the unsquared operator and `H_tau` the squared
operator. Avoid the historical ambiguity in which a Bloch matrix was called
`H(z)` while its characteristic polynomial was written in `x`.

For a periodic word, write

```text
A_tau(z)  for the unsquared Bloch fiber,
H_tau(z)=A_tau(z)^2,
c=z+z^(-1) in [-2,2].
```

## Reference Phase

The canonical period-eight word is

```text
tau_ref=(+,+,-,+,-,-,+,-),
Q_ref=(+,-,-,-) repeated.
```

Its squared spectral edge is

```text
eta=4+sqrt(10+2sqrt(5)).
```

Use `eta` only for the squared edge. If the unsquared edge is needed, write
`sqrt(eta)` explicitly.

The four translated reference bulk sectors are

```text
B_s,  s in Z/4Z,
```

where the positive entries of `Q` occur exactly at sites congruent to `s`
modulo four.

## Defects, Gaps, And Charge

Let the positive-`Q` sites on a ring occur cyclically at
`d_1,...,d_d`. Their positive cyclic gaps are

```text
g_j=d_(j+1)-d_j  (cyclically),
sum_j g_j=n.
```

The reference gap is four. Define the local excess charge

```text
q_j=g_j-4,
sum_j q_j=n-4d.
```

The translation-sector shift of a charge is

```text
sigma_sec(q)=q mod 4.
```

Use `sigma_sec` in prose or formulas where confusion with the edge signing
`sigma` is possible. A gap word is displayed as `(g_1,...,g_d)`; exponent
notation such as `4^a` means `a` consecutive reference gaps, not a power.

`G6` denotes the elementary abnormal gap `g=6`, equivalently `q=+2`. The
bilateral one-interface operators are `A_6` and `H_6=A_6^2`.

## The G6 Edge

Write `c6` for the unique root in

```text
(7905369311620327/10^15,
 7905369311620328/10^15)
```

of

```text
16y^10-520y^9+6913y^8-48448y^7+191768y^6
-423904y^5+484528y^4-270464y^3+137856y^2
-19968y+256.
```

`c6` is a squared spectral value. The corresponding unsquared values are
`+sqrt(c6)` and `-sqrt(c6)`. The accepted multiplicity statement is

```text
dim ker(H_6-c6)=2.
```

Never call `c6` a simple eigenvalue of `H_6`.

## Separated Interfaces

| Symbol | Meaning |
|---|---|
| `r` | Number of G6 interfaces; the certified exact-count theorem uses `r in {1,2,3}`. |
| `D` | Minimum cyclic site distance between interface cores; for one interface use `D=n`. |
| `S` | `floor(D/4)` in the exact-`2r` cutoff construction. |
| `L_site` | `S-12`. |
| `ell` | `floor(L_site/8)=floor((floor(D/4)-12)/8)`. |
| `q_F` | The Floquet decay constant `9/25`. Use `q_F`, not `q`, when local charge is also present. |
| `Phi` | Matrix of the `2r` truncated localized columns, ordered by interface and unsquared sign. |
| `G=Phi^*Phi` | Gram matrix of those columns. |
| `P` | Orthogonal projection onto `ran Phi` after Gram orthonormalization. |
| `Q_perp=I-P` | Complementary projection. Do not confuse it with the flux word `Q`. |
| `H_eff(z)` | The `2r x 2r` Feshbach operator in orthonormalized coordinates. |

The canonical cluster estimates are

```text
rank 1_[c6-1/400,c6+1/400](H)=2r,
Q_perp H Q_perp <=c6-1/200,
|lambda_j-c6|<3505r(9/25)^ell.
```

Multiplicity is counted. Individual finite-ring simplicity is not part of
the notation or theorem.

## Evidence And Editorial Terms

Use the following phrases exactly:

```text
mathematical reduction
finite exact object
independent machine verification
mathematical consequence
```

Use `MAIN_TEXT`, `APPENDIX`, and `REPRODUCIBILITY` for placement. Use the
evidence labels defined in
[TARGET_A_FINAL_CLAIM_INVENTORY_V2.md](TARGET_A_FINAL_CLAIM_INVENTORY_V2.md).
Internal research-task numbers are provenance metadata and are not theorem
names or mathematical dependencies.

## Forbidden Or Superseded Notation

Do not use any of the following in the canonical package:

```text
one squared mode per G6,
exact-r squared cluster,
codimension-r complement,
r x r problem-specific Feshbach matrix,
simple c6 eigenvalue of H_6,
sigma(q)=q/2 mod 4.
```

The corrected forms are rank two per G6, exact `2r`, codimension `2r`, a
`2r x 2r` Feshbach matrix, and `sigma_sec(q)=q mod 4`.
