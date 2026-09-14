# Final theorem ledger — 2026-09-14 geometry and high-order upgrade

Branch: `paper/circulant-periodic-gap-20260909`

This ledger supersedes the earlier September 14 ledger wherever the two differ. It incorporates the fixed-period geometry theorem, the all-energy characteristic identities, and the hostile-audit correction of the physical antiperiodic phase.

Paper I remains independent of the finite-global-minimization paper: every theorem below concerns explicit periodic phases and their continuous Bloch spectra.

---

# I. New highest-level geometry theorems

## F1. Exact balanced optimizer for every period divisible by eight

Status: **Proved**.

For every integer `r>=1`, in the complete even-separation reflection-chiral two-defect family with coefficient period

\[
p=8r
\]

and

\[
N+m=2r,
\]

the unique full-Bloch gap-maximizing geometry is

\[
\boxed{N=m=r,
\qquad h=p/4.}
\]

Primary file:

`ALL_FIXED_PERIOD_BALANCED_OPTIMALITY.md`.

Proof architecture:

- exact rational certificates for `2<=r<=8`;
- analytic all-phase comparison for every `r>=9`.

This strictly strengthens the earlier eventual fixed-period result.

---

## F2. Exact all-layer minimal `2`-adic quarter-period optimizer

Status: **Proved**.

If

\[
2^k\Vert s,
\qquad k>=2,
\]

then the shortest reflection-chiral two-defect primitive period is

\[
p_{\min}=2^{k+1},
\]

and **for every finite layer** the unique gap-maximizing even defect separation in that minimal period is

\[
\boxed{h=p_{\min}/4=2^{k-1}.}
\]

Primary files:

- `ALL_LAYER_MINIMAL_PERIOD_QUARTER_OPTIMALITY.md`;
- `CANONICAL_QUARTER_PERIOD_2ADIC_PHASE.md`.

There is no remaining large-`k` qualifier.

---

## F3. Exact all-energy scalar characteristic equation

Status: **Proved**.

For arbitrary even defect separation and arbitrary squared energy `y`, the entire growing Bloch determinant reduces to four Chebyshev quantities and the two Bloch coordinates `(d,e)`.

Primary file:

`GENERAL_SEPARATION_ALL_ENERGY_CHARACTERISTIC.md`.

The physical seam coordinate enters only linearly:

\[
P(y;d,e)=\mathcal G(y,d)-e.
\]

---

## F4. All-energy single-square identity

Status: **Proved**.

With

\[
x=\frac{y-d-4}{2},
\qquad
a=\frac{y+d-4}{2},
\]

and

\[
Z=T_N(x)T_m(a)+(ax-3)U_{N-1}(x)U_{m-1}(a),
\]

one has

\[
\boxed{
P(y;d,e)
=4\left[Z^2-1+(d-2)U_{m-1}(a)^2\right]+(2-e).
}
\]

Primary file:

`ALL_ENERGY_SINGLE_SQUARE_IDENTITY.md`.

This is the main algebraic tool behind the finite-period optimization theorem.

---

# II. Exact finite certificates supporting F1

## C1. `r=2`

`EXACT_MINIMAL_PERIOD_OPTIMALITY_K3.md`.

## C2. `r=3,5,6,7`

`EXACT_FIXED_PERIOD_BALANCED_OPTIMALITY_R3_R5_R6_R7.md`.

Reproducibility script:

`verify_residual_fixed_period_balanced_optimality.py`.

## C3. `r=4`

`EXACT_MINIMAL_PERIOD_OPTIMALITY_K4.md`.

## C4. `r=8`

`EXACT_MINIMAL_PERIOD_OPTIMALITY_K5.md`.

## C5. Independent tail audits

- `EXACT_MINIMAL_PERIOD_OPTIMALITY_K6.md` (`r=16`);
- `EXACT_MINIMAL_PERIOD_OPTIMALITY_K7.md` (`r=32`).

These last two are independent checks, not required by the final proof.

---

# III. Analytic tail for fixed-period optimality

## A1. Universal competitor Dirichlet upper bound

Status: **Proved**.

For any geometry,

\[
\Gamma_{N,m,q}
<2-2\cos\frac{\pi}{2\max\{N,m\}}.
\]

Primary file:

`UNIVERSAL_ENDPOINT_DIRICHLET_UPPER_BOUND.md`.

## A2. Balanced endpoint beats the next Dirichlet level

Status: **Proved for `r>=2`**.

\[
e_r^+>D_{r+1}.
\]

The original `r>=1` statement was hostile-audit corrected; `r=1` has no competitor anyway.

Primary file:

`BALANCED_ENDPOINT_BEATS_NEXT_DIRICHLET_LEVEL.md`.

## A3. All-phase analytic tail

Status: **Proved for every `r>=9`**.

\[
\Gamma_{r,r,q}>D_{r+1}.
\]

Primary file:

`BALANCED_ALL_PHASE_DIRICHLET_COMPARISON_TAIL.md`.

Its proof uses strict log-concavity of

\[
T_r(x)/U_{r-1}(x)
\]

from Chebyshev zero interlacing.

---

# IV. Exact defect-geometry phase diagram and Pell structure

## G1. Exact all-parameter sub-eight classification

Status: **Proved**.

Write

\[
L=2(N+m),\qquad h=2m.
\]

Then

\[
\boxed{
R_{N,m,q}<8
\iff
2m<T_N(3).
}
\]

Primary file:

`EXACT_GENERAL_SEPARATION_PHASE_DIAGRAM.md`.

## G2. Pell / square-triangular boundary

Status: **Proved**.

The largest safe `m` at fixed `N` is

\[
M_N=\frac{T_N(3)-1}{2}
=1,8,49,288,1681,9800,\ldots
\]

and

\[
\frac{M_N(M_N+1)}2=U_{N-1}(3)^2.
\]

Primary file:

`PELL_SQUARE_TRIANGULAR_PHASE_BOUNDARY.md`.

---

# V. Macroscopic geometry and all-orders asymptotics

## M1. Full-Bloch macroscopic law

Status: **Proved**.

If

\[
h/L\to\alpha\in(0,1),
\]

then

\[
\boxed{
L^2\Gamma
\to
\frac{\pi^2}{\max\{\alpha,1-\alpha\}^2}.
}
\]

Balanced geometry `alpha=1/2` uniquely maximizes the leading constant, giving `4pi^2` in `L^2` normalization and `16pi^2` in primitive-period normalization.

Primary file:

`MACROSCOPIC_FULL_BLOCH_GAP_LAW.md`.

## M2. All-orders endpoint Robin series

Status: **Proved**.

There is a universal series

\[
A(\ell)=\sum_{j\ge2}a_j\ell^{-j}
\]

governing both periodic and antiperiodic endpoint soft roots to every algebraic order.

Primary file:

`ALL_ORDERS_MACROSCOPIC_ROBIN_EXPANSION.md`.

## M3. All-orders periodic cusp series

Status: **Proved**.

At the periodic soft well there is an all-orders compressed phase expansion and gain series

\[
C(N)=\sum_{j\ge0}c_jN^{-j-4}.
\]

Primary file:

`ALL_ORDERS_PERIODIC_PHASE_SLIP_EXPANSION.md`.

## M4. Correct all-orders global phase diagram

Status: **Proved**.

To every algebraic order,

\[
\boxed{
\Gamma\sim A(N)-C(N),
\qquad m\le N,
}
\]

and

\[
\boxed{
\Gamma\sim A(m),
\qquad m>N.
}
\]

Primary file:

`ALL_ORDERS_GLOBAL_GAP_PHASE_DIAGRAM.md`.

---

# VI. Hostile-audit correction: physical antiperiodic phase

## Correct statement

For `m>N`, the globally selected well is the **compressed antiperiodic well**

\[
d=z^{2q+1}+z^{-(2q+1)}\approx-2.
\]

If `n=2q+1` and `z_0^n=-1`, a maximizing phase satisfies

\[
|\delta|=O((3+2\sqrt2)^{-2N})
\]

in compressed displacement from the best seam representative

\[
z_0=e^{\pm i\pi/n}.
\]

Thus the physical shift is beyond every algebraic order.

Primary corrected file:

`ANTIPERIODIC_EXACT_LOCKING_AND_HIGH_ORDER_GAP.md`.

### Retraction

The earlier statement

> `m>N` implies exact physical `z=-1` locking for arbitrary odd multiplier

is retracted.  It is literally correct only for multiplier one (and related symmetry cases).  The algebraic gap expansions derived from it remain valid because the correction is exponentially small.

Corrected dependent files include:

- `UNIFORM_INTEGER_ORIENTATION_SELECTION.md`;
- `DISCRETE_NEAR_BALANCED_TRANSITION.md`;
- `ALL_ORDERS_GLOBAL_GAP_PHASE_DIAGRAM.md`;
- `MACROSCOPIC_GLOBAL_GAP_HIGH_ORDER_PHASE_DIAGRAM.md`.

---

# VII. Current strongest paper-level thesis

The current manuscript is no longer just a periodic construction paper. Its strongest coherent statement is:

> **Reflection-chiral two-defect phases in signed step circulants form an exactly solvable arithmetic scattering family. Their sub-eight region has an exact Chebyshev/Pell phase diagram; at every period divisible by eight the unique spectral optimizer is the balanced quarter-period geometry; the shortest `2`-adic period therefore has a canonical finite optimizer in every layer; and the Bloch edge admits universal all-orders Robin and avoided-crossing expansions.**

This theorem hierarchy should govern the next manuscript rewrite.