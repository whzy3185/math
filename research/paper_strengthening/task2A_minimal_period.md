# Task 2A: minimal period below the eight barrier

**Verdict:** PASS.  
**New theorem class:** Tier A.  
**Proof status:** analytic reduction plus nine finite exact orbit certificates;
independent verifier passed.  
**Lean status:** not pursued under the frozen-kernel instruction.

## Theorem (primitive-period form)

Eight is the smallest primitive period of a legal Hamilton-gauge signing with
squared Bloch edge below eight.

Equivalently, in the earlier displayed-cell language: if `tau` is displayed
with period `p<8` and `R_p(tau)` denotes the supremum of its squared Bloch
spectral radius, then

```text
R_p(tau) >= 8.
```

Equality is attained by the alternating period-two phase and its even-cell
repetitions. In contrast, period eight admits the antipodal two-defect phase
with squared edge

```text
eta=4+sqrt(10+2sqrt(5))<8.
```

Cell repetition does not change the full Bloch edge: a `p=kq` fiber decomposes
into the `q`-cell fibers with phases `w^k=z`.  The target word has primitive
period eight.  Thus the displayed-period theorem is exactly the stated
primitive-period result.  Together with the period-eight trichotomy,
the antipodal two-defect class is the unique first-period sub-eight phase,
modulo translation, reflection, lift ambiguity, and cell repetition.

Lift invariance and the cyclic/reflection conjugacies used for this orbit
reduction are proved in `symmetry_invariance_lemmas.md`.

## Proof architecture

For the local flux word `Q_i=tau_i tau_(i+1)`, legality is
`prod_i Q_i=1`. Let d be the number of positive Q-sites, and let a,b count
positive pairs at cyclic distances one and two. If `R_p(tau)<=8`, the first
three moments imply

```text
16d-12p <= 0,
40d+96a+48b-42p <= 0.
```

For `p=1,...,7`, these two inequalities reduce all legal Q-words to the
following dihedral representatives:

| p | survivors after M1--M3 |
|---:|---|
| 1 | none |
| 2 | `--` |
| 3 | `--+` |
| 4 | `----` |
| 5 | `----+` |
| 6 | `------`, `----++`, `---+-+`, `--+--+` |
| 7 | `------+`, `---+-++`, `--+--++`, `--+-+-+` |

The all-negative representatives are the alternating period-two phase in a
repeated cell and have edge exactly eight.

For the p=3 survivor choose `z=exp(pi i/3)`. The corresponding Hermitian
fiber satisfies

```text
det(8I-H(z)^2)=-1.
```

Since all eigenvalues of `8I-H(z)^2` are real, a negative determinant forces
at least one negative eigenvalue and therefore a squared fiber eigenvalue
greater than eight.

Each remaining survivor has a simple phase `z in {1,-1,i}` and a small
integer or Gaussian-integer vector v with

```text
v*(8I-H(z)^2)v < 0.
```

The exact values are:

| p | Q representative | z | exact quadratic value |
|---:|---|---|---:|
| 5 | `----+` | 1 | -4 |
| 6 | `----++` | 1 | -12 |
| 6 | `---+-+` | -1 | -4 |
| 6 | `--+--+` | i | -4 |
| 7 | `------+` | 1 | -2 |
| 7 | `---+-++` | 1 | -4 |
| 7 | `--+--++` | 1 | -8 |
| 7 | `--+-+-+` | -1 | -8 |

The vectors themselves are short and recorded in the verifier. For a paper
proof, they can be placed in a compact supplementary table or replaced by
the displayed row calculations if the venue requires every coordinate in
the main source.

## Why this is not a brute-force signing classification

The finite step concerns local flux words only for seven fixed cell lengths.
There are at most `2^7` words before the legality and dihedral reductions.
The moment theorem performs the conceptual reduction; the final nine rows are
exact certificates, not numerical spectral searches or a statement about
finite-graph minimizers.

## Independent audit

Run

```text
uv run --with sympy python research/paper_strengthening/verifiers/verify_minimal_period.py
```

The verifier reconstructs all legal Q-words, moment inequalities, dihedral
orbits, tau lifts, fibers, Hermitian checks, and exact determinant/Rayleigh
certificates.
