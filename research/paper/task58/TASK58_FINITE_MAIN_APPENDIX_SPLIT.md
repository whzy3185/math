# Task 58 Finite Main-Appendix-Supplement Split

## 1. Purpose and governing rule

This document fixes the publication split for the exact finite completion of
the even-order classification. It is subordinate to the locked Task 58
manuscript blueprint and to the canonical packages

```text
research/paper/proof_completion/01_even_order_classification/
research/paper/proof_completion/02_small_order_34_46/
```

The main paper must make the classification proof readable and logically
complete. Section 7 states the exact finite lemmas, records the mathematical
consequences needed at each order, and performs the final disjoint synthesis.
Appendix B proves that every finite object used there is exhaustive and that
each accepted exact decision has the asserted spectral consequence. The
separate reproducibility supplement stores the removable machine-readable
payload.

The governing computation contract has four stages:

```text
mathematical reduction
  -> explicitly finite exact object
  -> independent exact verification
  -> mathematical consequence.
```

All four stages must be identified whenever computation enters the proof. A
producer search may discover a witness, vector, quotient representative, or
finite-state candidate. Its output is not a proof. A claim becomes usable only
after the finite object has been defined mathematically, independently rebuilt
or checked in exact arithmetic, and connected to the theorem by a written
implication.

## 2. Section 7: material that stays in the main text

### 2.1 Exact-computation protocol

Section 7 begins with the four-stage contract. It explains that switching,
cyclic lift, dihedral reduction, local compression, positive definiteness,
and Rayleigh comparison are mathematical reductions. It states that every
accepting comparison uses integer, rational, or exact algebraic arithmetic and
that every verification path is fail-closed.

This subsection may cite methodological precedents for exhaustive
computer-assisted proofs. It does not describe implementation internals. In
particular, no JSON field, schema, manifest, hash, command line, software
version, test count, resource measurement, or literal `PASS` marker appears in
Section 7 or elsewhere in the main paper.

### 2.2 Even orders 8 through 30

Section 7 states the finite exhaustion lemma for every even order from 8
through 30. The statement must identify the covered mathematical space:
switching classes at the smallest orders and the equivalent flux-holonomy
quotient, with complete fixed-weight and dihedral coverage, at the larger
orders. It states that every noncandidate class has an exact integral Rayleigh
certificate at or above the threshold and that the remaining candidate class
has exact threshold equality.

The main text gives the consequence

```text
rho(A)^2 >= theta_n for every signing and every even 8 <= n <= 30.
```

It then combines this universal lower bound with the analytic attainment of
`rho_-(n)` by the distinguished signing to obtain

```text
m_n=rho_-(n) for every even 8 <= n <= 30.
```

The main text does not print represented-space totals, cursor records, chunk
records, full witness vectors, or per-class decision tables.

### 2.3 The exact order-32 witness

Order 32 is separated from the exhaustion lemma. Section 7 prints enough data
to define the explicit signing unambiguously, states the exact matrix
inequality

```text
1561 I_32 - 200 A_32^2 > 0,
```

and gives the exact comparison

```text
1561/200 < theta_32.
```

It explains why positive definiteness implies
`rho(A_32)^2<1561/200<theta_32`, and hence strict failure. The main text need
not print the full matrix, pivot stream, Bareiss minors, or algebraic
root-isolation trace.

### 2.4 The six equality-recovery orders

For

```text
n in {34,36,38,42,44,46},
```

Section 7 states a finite-state closure theorem, not a search report. Its proof
in the main text retains the definitions and core implications:

1. a local `Q`-window determines the exact compression
   `M_Q=P A^2 P`;
2. an exact local Rayleigh quotient above the threshold excludes every cyclic
   signing containing that window;
3. surviving windows form an overlap graph;
4. parity-lifted closed walks are sound and complete for legal cyclic
   `Q`-words;
5. dihedral reduction loses no spectral-radius case; and
6. both Hamilton holonomies are retained.

The main text reports the final finite boundary: the six orders reduce to
exactly 64 terminal `(Q,alpha)` records, every terminal is decided by exact
threshold equality or an exact strict Rayleigh inequality, and none remains
unresolved. The consequence is

```text
rho(A)^2 >= theta_n for every signing
```

at all six orders. Candidate attainment then yields equality for precisely
these six recovery orders. The historical total 84 is not admissible; the
proved terminal total is 64.

### 2.5 The exact order-40 witness

Order 40 is kept distinct from the six-order universal closure. Section 7
prints the explicit cyclic `Q`-word and holonomy, states

```text
15541 I_40 - 2000 A_40^2 > 0,
```

and gives the exact comparison

```text
15541/2000 < 63/8 < theta_40.
```

It spells out the positive-definiteness implication and concludes strict
failure at 40. The complete rational elimination record remains outside the
main text.

### 2.6 The 96-order exact bridge

For every even `48 <= n < 240`, Section 7 states the deterministic residue
family used to construct the signing and records that the interval consists
of exactly 96 even orders. It states the exact finite lemma:

```text
for each such n there is a rational t_n with
t_n I-A_n^2 > 0 and t_n < 8-200/n^2.
```

The written proof then uses

```text
theta_n > 8-200/n^2
```

to conclude strict failure at every order in the bridge. Section 7 does not
list 96 matrices, 96 pivot streams, or 96 certificate rows. It must state
interval coverage explicitly; a sample of representative orders is not a
proof of the bridge.

### 2.7 Final disjoint synthesis

Section 7 ends with the final classification theorem and a proof by the
following disjoint, exhaustive partition of all even `n>=8`:

```text
8--30 even                       equality
32                               strict failure
34,36,38,42,44,46               equality
40                               strict failure
48--238 even                     strict failure
all even n>=240                  strict failure.
```

The first and third parts use universal exact lower bounds together with the
distinguished candidate's analytic attainment. The second, fourth, and fifth
parts use explicit exact strict witnesses. The sixth part uses the analytic
G6/IMS tail from Section 6. These mechanisms jointly prove

```text
m_n < rho_-(n)
if and only if n=32, n=40, or n is even and n>=48.
```

This synthesis classifies the truth of the proposed equality. It does not
classify all minimizing signings and does not determine the exact value of
`m_n` at a failing order. The G6/IMS argument explains eventual failure from
240 onward; only its combination with the 96-order bridge places the
continuous onset at 48.

## 3. Appendix B: complete mathematical detail

Appendix B contains the proof-level detail omitted from Section 7. It remains
a mathematical appendix: a reader must be able to verify the reductions,
exhaustiveness statements, and exact implications without treating a machine
log as an argument.

### 3.1 Switching and quotient coverage for 8 through 30

Appendix B proves the switching normal form, the cyclic lift condition, the
role of both holonomies, and the equivalence used to pass to the finite
`(Q,alpha)` quotient. It proves that the enumeration method at each order
covers the full intended quotient, including fixed-weight decomposition,
dihedral canonicalization, and terminal completion.

It defines the exact terminal decision types and proves that an integral
Rayleigh certificate excludes a counterexample while exact characteristic
factorization identifies threshold equality. Concise exact count tables may
be printed when they are needed to establish coverage, but raw class streams
and witness payloads remain supplemental.

### 3.2 Exact strict witnesses at 32 and 40

Appendix B gives the complete reconstruction of each signing from its stated
flux and holonomy data. It proves, in exact arithmetic, positive definiteness
of the two displayed matrices and supplies the exact threshold comparisons.
It explains why Bareiss and rational `LDL^T` certificates are valid
positive-definiteness proofs. Full machine pivot payloads may be moved to the
supplement, but the appendix must include enough exact mathematical data to
make the certificate type and its conclusion auditable.

### 3.3 Local exclusion for the six recovery orders

Appendix B derives the local range-four compression from the squared operator,
specifies the required window length, and proves the local exclusion lemma by
the Rayleigh principle. It gives the exact algebraic definition and rational
isolation of each `theta_n` used in the comparison. No decimal threshold is an
accepting value.

### 3.4 Parity-lifted finite-state completeness

Appendix B constructs the overlap graph and its parity lift. It proves both
directions:

```text
closed parity-even walk -> legal cyclic Q-word,
legal cyclic Q-word with no excluded window -> closed parity-even walk.
```

The proof includes wraparound overlap, cyclic lift parity, dihedral orbit
coverage, reconstruction of the two lifts at the squared-spectrum level, and
separate treatment of both Hamilton holonomies. It then gives the exact
canonical-class and terminal counts whose sum is 64.

### 3.5 Terminal resolution and termination

Appendix B defines the two accepted terminal outcomes: exact threshold
equality and exact strict Rayleigh exclusion. It proves that all 64 terminal
records fall into one of these outcomes and that the finite-state procedure
terminates with no unresolved mathematical case. The conclusion must be tied
back through local exclusion, soundness, and completeness to every signing at
the six orders.

### 3.6 Complete proof of the 96-order bridge

Appendix B defines the four deterministic residue constructions, their
holonomies, and their coverage of every even order from 48 through 238. It
states the exact rational positive-definiteness proposition for all 96
matrices and proves that independent exact reconstruction verifies every
premise. It then gives the uniform threshold implication leading to strict
failure throughout the interval.

The appendix may summarize the 96 rational bounds in a compact mathematical
table if required for auditability. Full matrices, factor streams, and
machine-readable rows remain in the supplement.

### 3.7 Appendix-level exhaustive synthesis

Appendix B closes with a concise dependency audit showing that the finite
pieces cover exactly

```text
8--30, 32, 34--46, and 48--238
```

with order 40 separated from the six recovery orders. It then points to the
analytic `n>=240` theorem in Section 6 and verifies that the six sets used in
Section 7 are pairwise disjoint and exhaustive.

The exact single-gap witness arithmetic supporting Section 5 may occupy a
separate final part of Appendix B under the master blueprint. It must not be
mixed into the finite order-classification synthesis, and its full integer
vectors remain supplemental.

## 4. Separate reproducibility supplement

The supplement contains the raw removable layer:

- machine-readable certificates and full certificate payloads;
- JSON schemas, field definitions, canonical serialization rules, and
  manifests;
- immutable hashes, file sizes, provenance paths, and source bindings;
- producer commands, independent-checker commands, software versions, and
  expected output markers;
- literal `PASS` strings, test counts, tamper tests, negative controls, and
  fail-closed parsing records;
- generator cursors, chunk boundaries, represented-space totals, digests,
  optimiser records, and full class streams for orders 8 through 30;
- the complete matrices, Bareiss minors, rational pivot streams, and exact
  root-isolation traces for orders 32 and 40;
- every local-window row, witness vector, overlap-graph record, rooted walk,
  dihedral representative, holonomy terminal, and decision record for the six
  recovery orders;
- all 96 bridge rows, full reconstructed matrices, rational bounds,
  elimination records, and independent-ordering cross-checks; and
- resource notes and reconstruction logs.

The supplement may explain how to reproduce Appendix B, but it may not carry
an implication needed to prove the theorem. Removing it must leave Section 7
plus Appendix B mathematically complete.

## 5. Mandatory proof boundaries

| Component | Mathematical reduction | Finite exact object | Independent verification | Mathematical consequence |
|---|---|---|---|---|
| Even 8--30 | Switching and quotient coverage | Complete exact terminal decisions | Independent reconstruction of coverage and decisions | Universal lower bound, hence equality by attainment |
| Order 32 | Explicit signing and positive-definiteness criterion | Exact matrix and threshold isolation | Independent Bareiss and rational `LDL^T` checks | Strict failure at 32 |
| Six recovery orders | Local exclusion plus parity-lifted cyclic completeness | All windows, closed walks, 64 terminals | Independent exact rebuild with no unresolved case | Universal lower bound, hence equality by attainment |
| Order 40 | Explicit signing and positive-definiteness criterion | Exact matrix and rational pivots | Independent exact reconstruction | Strict failure at 40 |
| Even 48--238 | Deterministic residue families and interval coverage | 96 exact rational matrix inequalities | Independent full-matrix rational `LDL^T` verification | Strict failure throughout the finite bridge |
| Even at least 240 | G6 patch identification and IMS | Exact endpoint inequalities only | Exact endpoint evaluation | Analytic monotonicity gives the infinite tail |

The following shortcuts are forbidden:

1. Treating a producer search, floating-point scan, or stored candidate as a
   proof.
2. Reporting a successful program run without proving what finite set was
   covered and why its decisions imply the theorem.
3. Calling the six recovery orders sampled evidence rather than a complete
   parity-lifted closure.
4. Replacing the 96-order interval proof by selected representative rows.
5. Merging the order-40 witness into the six-order equality theorem.
6. Claiming that the analytic tail alone proves the onset at 48.
7. Printing JSON, schemas, hashes, command lines, literal `PASS` markers, or
   raw certificate payloads in the main paper.
8. Inferring a classification of minimizers or exact failing values from the
   truth classification.

## 6. Acceptance condition

The split is respected only if a reader can delete the reproducibility
supplement and still recover the complete proof from Sections 2--7 and
Appendix B:

```text
candidate attainment
  + universal exact lower bounds at the equality orders
  + exact strict witnesses at 32 and 40
  + the exact 96-order bridge
  + the analytic n>=240 tail
  -> the complete even-order classification.
```

Appendix B must establish the completeness of every finite reduction used in
this implication. The supplement documents reconstruction and independent
verification; it does not repair a missing proof.
