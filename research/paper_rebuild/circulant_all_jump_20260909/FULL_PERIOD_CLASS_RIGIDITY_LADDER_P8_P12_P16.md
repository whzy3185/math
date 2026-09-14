# Full-period variational rigidity ladder: periods 8, 12, and 16

Date: 2026-09-14

This note records the first three complete fixed-period experiments in which the variational class is enlarged from the reflection-chiral two-defect family to **all legal periodic Hamilton-gauge flux words of the given period**.

The evidence labels follow the project convention strictly.

---

## 1. Period 8, jump 4

Status: **Proved**.

There are `128` legal flux words and `18` dihedral orbits. The exact theorem is

\[
\boxed{
\min_Q R_8(Q)=4+\sqrt{14}<8,
}
\]

with a unique minimizing dihedral orbit represented by

\[
Q_0=Q_2=+1,
\qquad Q_j=-1\ (j\ne0,2).
\]

The all-negative orbit has edge exactly `8`; every other orbit has edge strictly larger than `8`.

Primary proof:

`PERIOD8_FULL_CLASS_JUMP4_VARIATIONAL_THEOREM.md`.

Exact audit:

`verify_period8_full_class_jump4.py`.

Thus at the first `2`-adic layer both statements hold:

1. **optimizer rigidity**: the canonical two-defect phase is the unique optimizer in the complete period-eight class;
2. **sub-eight uniqueness**: it is also the unique orbit below the threshold `8`.

---

## 2. Period 12, jump 6

Status: **Verified** by exact finite computation.

There are

\[
2^{11}=2048
\]

legal flux words and exactly `122` dihedral orbits.

The exact verifier proves:

- the distance-two two-defect orbit is strictly sub-eight for every Bloch phase;
- the all-negative orbit has edge exactly `8`;
- every other orbit violates an exact endpoint even-moment inequality
  \[
  8\operatorname{tr}(H^{2j})-\operatorname{tr}(H^{2j+2})\ge0
  \]
  at `z=1` or `z=-1`, with the latest required certificate occurring at order `44`.

Therefore the exact finite evidence establishes

\[
\boxed{
\text{unique full-class optimizer}=
\text{distance-two two-defect orbit},
}
\]

and again this orbit is the unique sub-eight orbit.

Its full edge is the largest real root of

\[
y^3-14y^2+53y-36=0,
\]

numerically

\[
7.7887152091079\ldots.
\]

The exact evidence source is

`verify_period12_full_class_jump6.py`.

Under the project convention this is **Verified**, not promoted to `Proved`, because the exclusion of the `122` finite orbits is still an exact computational certificate rather than a conceptual human-scale classification.

---

## 3. Period 16, jump 8

Status: **Verified** for the unique optimizer by exact finite computation; additional sub-eight multiplicity currently **Observed** unless separately certified.

There are

\[
2^{15}=32768
\]

legal flux words and exactly `1162` dihedral orbits.

Let the balanced two-defect orbit have positive flux sites at cyclic distance four. The exact rational separator

\[
\boxed{y_0=389/50=7.78}
\]

certifies its full-class optimality:

- the balanced target has full Bloch edge strictly below `389/50`; this follows from an all-energy single-square Bernstein certificate plus a Sylvester inertia check at the reference fiber;
- `1127` of the remaining orbits are excluded above `8` by endpoint moment inequalities through order `14`;
- among the remaining `34` competitors, each has `389I-50H^2` non-positive-definite at `z=1` or `z=-1`, witnessed by a nonpositive leading principal minor of order at most `15`.

Hence

\[
\boxed{
\text{the balanced distance-four two-defect orbit is the unique period-16 full-class optimizer.}
}
\]

Exact audit:

`verify_period16_full_class_jump8.py`.

A separate corrected Hermitian numerical exploration finds the target edge

\[
R_{16}^{\rm opt}\approx7.75282441939334.
\]

It also finds other sub-eight orbits, including four-defect classes with edges approximately

\[
7.8012484453,
\qquad
7.8042260652.
\]

These latter numerical values are currently **Observed**, not theorem statements.

Thus period `16` is the first layer where

\[
\boxed{
\text{optimizer rigidity persists but sub-eight uniqueness breaks.}
}
\]

---

## 4. Emerging conjectural picture

The data through periods `8,12,16` point to a substantially stronger variational principle than the two-defect theorem proved earlier:

> **Full-class optimizer-rigidity conjecture.** For every admissible coefficient period divisible by four, the unique minimizer of the continuous squared Bloch edge over the complete legal periodic flux class is the same two-defect geometry already identified as optimal inside the reflection-chiral two-defect family.

The expected geometry is therefore the one from `ALL_PERIODS_DIVISIBLE_BY_FOUR_OPTIMAL_GEOMETRY.md`:

- for `p=8r`, exact balance / quarter-period separation;
- for `p=8r+4`, the classified nearest-balanced orientation, including the finite switch at `r=5 -> 6`.

This statement is **not yet proved** beyond period eight. Periods twelve and sixteen are exact finite evidence.

A second phenomenon is distinct:

> uniqueness below the threshold `8` holds at periods `8` and `12` but fails by period `16`.

Hence future work should optimize the spectral edge directly rather than try to classify all sub-eight phases.
