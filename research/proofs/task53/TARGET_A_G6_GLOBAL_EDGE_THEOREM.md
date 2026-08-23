# The Global Spectral Edge of a Single G6 Interface

Let `H6` be the infinite squared operator with one forward or reflected G6
interface. Let `c6` be the unique root in

```text
[7905369311620327/10^15,7905369311620328/10^15]
```

of the Task 51 irreducible degree-ten polynomial.

## Theorem

```text
sup sigma(H6)=c6.
```

In particular, `sigma(H6) intersect (c6,16]` is empty.

## Proof

Task 50 proves, by an unsquared interval Evans determinant with fixed-sign
derivative, that exactly one simple positive-`A` physical G6 root lies in the
displayed interval. The exact anticommuting symmetry
`(Ku)_i=(-1)^i u_(9-i)` gives `K^2=-I` and `KA=-AK`, so there is one simple
negative partner. After squaring, the `H=A^2` level `c6` has multiplicity
two. This proves membership of `c6` and excludes a second positive root
between `c6` and its rational upper endpoint.

Above that endpoint, the global Grassmann atlas defines the physical
matching condition everywhere. Every physical zero annihilates the exact
stable-branch resultant. Exact factorization and Sturm counting find exactly
two resultant roots in `[c6_upper,16]`:

```text
[8.080985802104273,8.080985802104274],
[8.13985656333926,8.13985656333928].
```

On both intervals, the unsquared G6 determinant in cofactor chart `013` is
strictly negative and every cofactor vector has a certified nonzero pivot.
An independent checker repeats both exclusions in chart `023`. The first
root is the physical gap2 level selected from the common degree-ten
polynomial; changing the defect transfer to G6 makes the matching nonzero.
The second is an elimination branch with no G6 physical match.

The confluent symmetric quotient represents the repeated-multiplier energy.
It is not a resultant candidate, so no zero is lost there. Finally, the
signed adjacency has absolute row sum four, hence `||A||<=4` and
`sigma(A^2)` lies in `[0,16]`. There is no spectrum beyond the checked
interval on the positive branch; anticommutation maps the entire negative
branch to it. Reflection preserves the spectrum by the unitary equivalence
in the physical-branch theorem. This proves the claim.

The exact resultant supplies candidate completeness only. Physical root
selection is entirely unsquared and interval-certified.

Status: `GATE_A3_PASS_G6_GLOBAL_EDGE_PROVED` / COMPUTER_ASSISTED_PROVED.
