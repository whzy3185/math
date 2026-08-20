# 1. Introduction

Signed adjacency matrices provide a concrete meeting point of spectral graph
theory, switching theory, and discrete magnetic or flux-phase ideas. If `G` is
a graph and every edge receives a sign in `{+1,-1}`, switching the signs at a
vertex conjugates the signed adjacency matrix by a diagonal sign matrix.
Consequently the spectrum depends on cycle fluxes rather than on the chosen
edge gauge. The optimization problem of minimizing spectral radius over all
signings can therefore be viewed as a finite flux-phase problem.

We study this problem for the four-regular circulant

```text
G_n=C_n(1,2),
```

whose vertices are the residues modulo `n` and whose edges join vertices at
cyclic distances one and two. Suvagiya identified a distinguished family in
which the triangle fluxes alternate. For even `n`, the two members of that
family with negative step-one Hamilton-cycle holonomy have spectral radius

```text
rho_-(n)=2 sqrt(cos^2(pi/n)+cos^2(2pi/n)).
```

The source conjecture states that no signing of `G_n` has smaller spectral
radius. The source paper verified the assertion for `n=8,10,...,18` and left
the general lower bound open.

The conjecture is false. Its failure is nevertheless delayed: every admissible
order below 32 satisfies the proposed lower bound. The first counterexample is
an order-32 signing whose triangle-flux word is the fourfold repetition of

```text
(+,+,-,+,-,-,+,-).
```

The same word defines an eight-periodic operator. Its Floquet polynomial can be
computed exactly, and a uniform positivity argument turns the isolated witness
into an infinite family for all multiples of eight at least 32. The resulting
analysis does more than refute the conjecture: it reveals a sharp period-eight
spectral edge and a structural cancellation mechanism.

## 1.1 Main results

Our first result combines an exact witness with exhaustive finite exclusion.

**Theorem A (smallest counterexample).**  The conjectured lower bound holds for
every even `n` with `8<=n<=30`. It fails at `n=32`. Hence 32 is the smallest
counterexample order.

The exclusion through 30 is a finite computer-assisted theorem. Its proof
enumerates a complete quotient of the switching classes and certifies every
nonoptimizer by exact rational inequalities. The order-32 witness itself has a
short exact positive-definiteness certificate.

The witness extends periodically.

**Theorem B (infinite counterexample family).**  For every `n=8L` with `L>=4`
and either Hamilton holonomy, the period-eight signing defined in Section 4
satisfies

```text
rho(A)^2 < 1561/200 < rho_-(n)^2.
```

Thus the conjecture fails at every multiple of eight at least 32. We do not
claim that it fails at every even order above 32.

The Floquet analysis is sharp at infinite volume.

**Theorem C (exact period-eight edge).**  For the target period-eight phase,
the squared infinite-volume spectral radius is

```text
eta=4+sqrt(10+2sqrt(5)),
```

and the top band reaches `eta` only at Bloch parameter `z=1`.

The local mechanism is described by a complete phase classification. For a
legal eight-periodic flux word `Q`, let `D(Q)` be the set of positive entries
and let `R(Q)` denote the squared infinite-volume spectral radius.

**Theorem D (eight-barrier trichotomy).**  Exactly one of the following occurs:

```text
D(Q)=emptyset:                 R(Q)=8;
D(Q)={j,j+4}:                 R(Q)=eta<8;
all other legal period-8 Q:    R(Q)>8.
```

In particular the target is the unique period-eight minimizer up to
translation, reflection, and global gauge negation, and the all-negative phase
is the unique runner-up.

The same squared-operator calculation gives information at every period. Put
`d=|D(Q)|`, let `a` count adjacent positive pairs, and let `b` count positive
pairs at cyclic distance two.

**Theorem E (general-period moment obstruction).**  For every legal
`p`-periodic phase,

```text
M_1=4p,
M_2=20p+16d,
M_3=118p+168d+96a+48b.
```

If `R(Q)<=8`, then necessarily

```text
d<=3p/4,
40d+96a+48b<=42p.
```

These are necessary conditions only.

Finally we classify a bounded but nontrivial periodic domain.

**Theorem F (low-period frontier).**  Among all periodic Hamilton-gauge phases
of primitive period at most 16, the target phase is the unique minimizer up to
translation, reflection, global negation, and repetition of the unit cell.

This theorem is also computer-assisted. The proof enumerates 2,626 legal
flux/dihedral orbit representatives. A closed-walk hierarchy excludes 2,611
representations above the eight-barrier, one cancellation lemma treats eight
repeated all-negative cells, five exact endpoint certificates handle the
remaining competitors, and two displayed target rows are one phase related by
zone folding.

## 1.2 Proof strategy

The first organizing device is Hamilton gauge. After switching all step-one
edges to `+1` except for a single holonomy cut, a signing is encoded by a
periodic word `tau` of triangle fluxes. Its adjacent products

```text
Q_i=tau_i tau_(i+1)
```

are the quadrilateral fluxes. Periodicity permits a Floquet decomposition into
finite Hermitian Laurent matrices `H_Q(z)`. For the target word, the
characteristic determinant is even in the eigenvalue and reduces to a quartic
`P(y,c)` in `y=lambda^2` and `c=z+z^(-1)`. An exact positive-coefficient
expansion at the candidate edge proves the sharp bound and its equality case.

The second device is to square the infinite operator. In `A_tau^2`, every
odd-displacement coefficient contains a factor `1+Q_i`. Negative flux
therefore cancels that coupling exactly, while positive flux activates an
amplitude of absolute value two. Constant terms of even Bloch traces count
signed closed walks. If all squared band values were at most eight, their
successive moments would satisfy `M_(k+1)<=8M_k`. A positive excess therefore
forces the spectrum above eight. This one-way implication, combined with
defect geometry, proves the period-eight trichotomy and supplies the general
period obstructions.

## 1.3 Scope and public status

The results distinguish three optimization domains. Theorem D concerns
infinite-volume phases of displayed period eight. Theorem F concerns periodic
phases of primitive Hamilton-gauge period at most 16. Theorem A concerns all
finite signings only at the enumerated orders through 32. None of these results
proves global optimality over all periods, all nonperiodic signings, or every
finite order.

As of 20 August 2026, we found no direct public resolution of Conjecture 3 in
the source paper, the author's listed follow-up materials, or the narrow
direct-result searches recorded for this draft. This is a dated and bounded
search statement, not an absolute priority claim.

## 1.4 Organization

Section 2 fixes switching, flux, Floquet, moment, and equivalence notation.
Section 3 proves Theorem A. Sections 4 and 5 prove the periodic family and its
sharp edge. Section 6 proves the eight-barrier trichotomy and explains the
chiral symmetry. Section 7 derives the general-period moments and necessary
conditions. Section 8 proves the bounded low-period frontier. Section 9 states
the computer-assisted proof boundary and reproducibility model. Section 10
collects consequences and open problems. The appendices give the orbit-counting
arguments, exact finite certificates, and computational protocol needed to
audit the computer-assisted parts.
