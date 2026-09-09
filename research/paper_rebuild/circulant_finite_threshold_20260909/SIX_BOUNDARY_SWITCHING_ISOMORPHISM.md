# Switching-isomorphism orbits at the `sqrt(6)` boundary

`SIX_BOUNDARY_MINIMIZER_RIGIDITY.md` proves that the labelled minimizing switching-class counts at the four equality pairs are

\[
2,32,32,2
\]

for `(12,4),(16,3),(16,5),(20,8)`.  This note determines the coarser orbits after graph automorphisms.

## Theorem 1

The complete switching-isomorphism orbit structure is

\[
\boxed{
\begin{array}{c|c|c}
(N,s)&\#\text{ labelled minimizer classes}&\#\text{ switching-isomorphism orbits}\\ \hline
(12,4)&2&1,\\
(16,3)&32&2,\\
(16,5)&32&2,\\
(20,8)&2&1.
\end{array}}
\tag{1}
\]

For `(16,3)` the two orbits have size `16` and are distinguished by the holonomy `alpha=+-1` of the step-one Hamilton cycle.  The multiplier `x -> 5x` transports the same two-orbit decomposition to `(16,5)`.

### Proof

We first identify the full graph automorphism groups.

#### `(12,4)`

In `C_12(1,4)`, every step-four edge lies in exactly one triangle, namely one of the four chord triangles, while no step-one edge lies in a triangle.  Therefore every graph automorphism preserves the two edge types.  In particular it preserves the step-one Hamilton cycle.  Hence

\[
\operatorname{Aut}(C_{12}(1,4))\le \operatorname{Aut}(C_{12})=D_{24}.
\]

Translations and reflection preserve both step lengths, so equality holds:

\[
\operatorname{Aut}(C_{12}(1,4))=D_{24}.
\tag{2}
\]

The two minimizing labelled switching classes from the exact certificate are interchanged by translation by one vertex.  Hence they form one switching-isomorphism orbit.

#### `(16,3)`

Here neither edge type belongs to a triangle, but the number of four-cycles through an edge separates the types.  By translation it suffices to inspect the edges `01` and `03`.

The step-one edge `01` lies in exactly the five four-cycles

```text
0-1-2-3-0,
0-1-2-15-0,
0-1-4-3-0,
0-1-14-13-0,
0-1-14-15-0,
```

whereas the step-three edge `03` lies in exactly the three four-cycles

```text
0-3-2-1-0,
0-3-2-15-0,
0-3-4-1-0.
```

Thus every automorphism preserves the step-one Hamilton cycle, and exactly as above

\[
\operatorname{Aut}(C_{16}(1,3))=D_{32}.
\tag{3}
\]

The sign of the step-one Hamilton cycle is switching invariant and is preserved by every automorphism in (3).  Hence the 16 minimizers with `alpha=+1` cannot be switching-isomorphic to the 16 minimizers with `alpha=-1`.

Conversely, exact dihedral action on the 32 Hamilton-gauge representatives shows that translation by one vertex has an orbit of size 16 in each holonomy sector.  Since there are exactly 16 representatives in each sector, each sector is one orbit.  Therefore there are exactly two switching-isomorphism orbits.

#### `(16,5)`

Multiplication by `5` gives the graph isomorphism

\[
C_{16}(1,3)\cong C_{16}(1,5),
\]

so the two size-16 orbits transport bijectively.

#### `(20,8)`

In `C_20(1,8)`, a step-eight edge lies in exactly one five-cycle: the chord edges split into four disjoint `C_5` components.  A step-one edge lies in no five-cycle.  Hence automorphisms again preserve the step-one Hamilton cycle, giving

\[
\operatorname{Aut}(C_{20}(1,8))=D_{40}.
\tag{4}
\]

The two equality chord words from the analytic recurrence are interchanged by translation by one vertex, so they form a single switching-isomorphism orbit.  This proves (1). `square`

---

## Exact reproducibility

`verify_six_boundary_orbits.py` applies the dihedral permutations `x -> +-x+b` to the exact Hamilton-gauge minimizer sets and verifies orbit sizes

```text
(12,4): 2;
(16,3): 16,16;
(20,8): 2.
```

The finite action is purely combinatorial.  The companion minimizer script uses floating point only to propose integer negative quadratic-form witnesses; no floating comparison accepts or rejects a theorem branch.

## Consequence

At the parameter level the `sqrt(6)` boundary consists of four isolated pairs, but at the minimizer-moduli level there are two qualitatively different behaviors:

- the duplicate-free pairs `(12,4)` and `(20,8)` each have one switching-isomorphism orbit;
- the repeated-root order-16 pair has two distinct orbits, separated by Hamilton holonomy.

This is the natural rigidity statement to place after the complete equality theorem in the manuscript.
