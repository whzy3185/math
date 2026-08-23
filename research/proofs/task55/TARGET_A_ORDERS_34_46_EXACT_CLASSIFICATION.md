# Target A orders 34--46: exact partial classification

> **Supersession notice.**  This document preserves the exact order-40 LDL
> proof and the evidence boundary of the earlier bounded-search lane.  Its
> partial-classification status has been superseded by
> `TARGET_A_SMALL_ORDER_EXACT_THEOREM.md`, whose independent checker gives
> final status `COMPUTER_ASSISTED_PROVED` and proves nonexistence of a
> counterexample at \(n=34,36,38,42,44,46\).  The order-40 proposition and all
> provenance recorded here remain valid.

## 1. Certified statement

**Proposition (order 40).**  There is an admissible cyclic signing at order
\(n=40\) for which

\[
 \rho(A)^2 < \frac{15541}{2000}
              < \frac{63}{8}.
\]

Consequently the conjectured lower bound at order 40 fails.  This proposition
has evidence status `COMPUTER_ASSISTED_PROVED`.

This legacy certificate asserts no corresponding theorem for

\[
 n\in\{34,36,38,42,44,46\}.
\]

Within its own evidence boundary, each of those six rows has status
`OPEN_BOUNDED_SEARCH_ONLY`.  Those are historical lane labels rather than the
current project status: the later exact classifier proves the conjectured
lower bound at all six orders.

## 2. Exact input

The certified cyclic word is

\[
 Q=1000100010001000100010001000100010001000,
 \qquad \alpha=-1.
\]

Its canonical dihedral code is \(73300775185\), and its gap word is
\((4,4,4,4,4,4,4,4,4,4)\).  Starting from \(\tau_0=1\), the checker rebuilds
the remaining signing data from

\[
 \tau_{i+1}=Q_i\tau_i.
\]

It then constructs the real symmetric order-40 adjacency matrix \(A\) using
the stored cyclic lift \(\alpha=-1\).  Neither the matrix nor its LDL factors
are trusted as opaque numerical data.

## 3. Exact positive-definiteness proof

Define the integer symmetric matrix

\[
 M=15541 I_{40}-2000 A^2.
\]

Natural-order fraction-free input followed by exact rational LDL elimination
produces 40 strictly positive pivots.  Hence \(M\) is positive definite.  For
every nonzero vector \(v\),

\[
 0<v^{\mathsf T}Mv
  =15541\lVert v\rVert^2-2000\lVert Av\rVert^2.
\]

It follows that

\[
 \frac{\lVert Av\rVert^2}{\lVert v\rVert^2}
 <\frac{15541}{2000}
\]

for every nonzero \(v\), and therefore

\[
 \rho(A)^2=\lambda_{\max}(A^2)<\frac{15541}{2000}.
\]

The second comparison is elementary and exact:

\[
 \frac{63}{8}-\frac{15541}{2000}
 =\frac{209}{2000}>0.
\]

This proves the proposition without relying on floating-point eigenvalues.

## 4. Independent reconstruction and binding

The independent checker performs all of the following:

1. requires the ordered list of orders to be exactly
   \((34,36,38,40,42,44,46)\);
2. requires order 40 to be the only `CERTIFIED_COUNTEREXAMPLE` row and every
   other row to remain `OPEN_BOUNDED_SEARCH_ONLY`;
3. reconstructs the canonical code, cyclic signing matrix, integer matrix
   \(M\), and all 40 exact rational LDL pivots;
4. verifies the strict rational spectral sandwich;
5. recomputes the matrix and pivot SHA-256 digests;
6. binds the result to the preserved order-40 legacy candidate and certificate
   by their independently recomputed SHA-256 digests;
7. rejects the statement that all even orders \(n\ge 32\) fail.

The certificate also carries search provenance for the orders unresolved by
this legacy lane.  No part of the exact order-40 proof converts that provenance
into an exhaustion proof.

## 5. Historical lane table and current classification

| order | historical lane evidence class | conclusion available from this artifact alone |
|---:|---|---|
| 34 | `OPEN_BOUNDED_SEARCH_ONLY` | no counterexample found in the recorded bounded searches; nonexistence not proved |
| 36 | `OPEN_BOUNDED_SEARCH_ONLY` | no counterexample found in the recorded bounded searches; nonexistence not proved |
| 38 | `OPEN_BOUNDED_SEARCH_ONLY` | no counterexample found in the recorded bounded searches; nonexistence not proved |
| 40 | `COMPUTER_ASSISTED_PROVED` | explicit counterexample certified by exact rational LDL |
| 42 | `OPEN_BOUNDED_SEARCH_ONLY` | no counterexample found in the recorded bounded searches; nonexistence not proved |
| 44 | `OPEN_BOUNDED_SEARCH_ONLY` | no counterexample found in the recorded bounded searches; nonexistence not proved |
| 46 | `OPEN_BOUNDED_SEARCH_ONLY` | no counterexample found in the recorded bounded searches; nonexistence not proved |

Thus the exact Task 55 conclusion for this interval is a partial
classification with one positive certificate **within this legacy artifact**.
Its `OPEN_BOUNDED_SEARCH_ONLY` rows remain accurate descriptions of the stored
bounded searches and are retained for provenance.

The superseding exact local-interlacing certificate and independent checker
close all six rows as `COMPUTER_ASSISTED_PROVED` non-counterexample results.
Together, the two artifacts give the current interval classification:

| order | current conclusion |
|---:|---|
| 34, 36, 38 | no counterexample exists |
| 40 | explicit counterexample, certified by the exact rational LDL proof in this document |
| 42, 44, 46 | no counterexample exists |

Consequently this interval does not support the statement that all even
\(n\ge32\) fail.
