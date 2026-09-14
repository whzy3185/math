# All-layer quarter-period optimality in the minimal `2`-adic period

Date: 2026-09-14

Status: **Proved**. This is a headline theorem for Paper I.

This note closes the finite-cell geometry optimization problem inside the shortest reflection-chiral two-defect period for every `2`-adic valuation, not merely asymptotically.

## 1. Setup

Let

\[
s=2^k(2q+1),
\qquad k\ge2,
\qquad q\ge0.
\]

Inside the reflection-chiral even-separation two-defect ansatz, compatibility requires

\[
s=L(2q'+1).
\]

Hence the shortest admissible half-period is

\[
\boxed{L=2^k,}
\]

and the shortest primitive coefficient period is

\[
\boxed{p_{\min}=2L=2^{k+1}.}
\tag{1.1}
\]

Every even two-defect geometry in this minimal cell can be written as

\[
L=2(N+m),
\qquad
N+m=2^{k-1},
\qquad
N,m\ge1,
\]

with defect separation

\[
h=2m.
\]

Let

\[
\Gamma_{N,m,q}
:=8-\max_{|z|=1}\rho(H_{N,m,q}(z))^2
\]

be the full continuous squared Bloch gap.

The balanced quarter-period geometry is

\[
\boxed{
N=m=2^{k-2},
\qquad
h=2^{k-1}=\frac{p_{\min}}4.
}
\tag{1.2}
\]

## Theorem A — all-layer exact quarter-period optimizer

For every integer

\[
\boxed{k\ge2}
\]

and every odd multiplier, the balanced geometry (1.2) is the unique gap-maximizing even-separation reflection-chiral two-defect phase of the minimal primitive period `2^(k+1)`:

\[
\boxed{
\Gamma_{2^{k-2},\,2^{k-2},\,q}
>
\Gamma_{N,m,q}
}
\tag{1.3}
\]

for every integer pair

\[
N+m=2^{k-1},
\qquad
(N,m)\ne(2^{k-2},2^{k-2}).
\]

Equivalently, among all such minimal-period phases the unique optimal defect separation is

\[
\boxed{h=p_{\min}/4.}
\tag{1.4}

Thus the shortest-period construction is completely canonical:

1. the `2`-adic valuation fixes the period;
2. exact spectral optimization fixes the defect geometry;
3. the remaining Bloch optimization produces the periodic cusp/phase-slip correction.

---

## 2. Universal comparison principle

For a general geometry put

\[
M:=\max\{N,m\}.
\]

`UNIVERSAL_ENDPOINT_DIRICHLET_UPPER_BOUND.md` proves the finite, non-asymptotic inequality

\[
\boxed{
\Gamma_{N,m,q}
<D_M,
\qquad
D_M:=2-2\cos\frac{\pi}{2M}.
}
\tag{2.1}
\]

If the geometry is super-eight the inequality is automatic; otherwise it follows by choosing the endpoint whose soft channel has length `M`.

Now fix the balanced total cell

\[
N+m=2r.
\]

Every unbalanced integer pair satisfies

\[
M\ge r+1,
\]

and `D_M` is strictly decreasing in `M`. Therefore

\[
\boxed{
\Gamma_{N,m,q}<D_{r+1}
\qquad((N,m)\ne(r,r)).
}
\tag{2.2}
\]

Thus balanced optimality at a given `r` follows from the single inequality

\[
\boxed{
\Gamma_{r,r,q}>D_{r+1}.
}
\tag{2.3}
\]

The rest of the proof establishes (2.3) for exactly the powers

\[
r=2^{k-2}.
\]

---

## 3. The trivial first layer `k=2`

If `k=2`, then

\[
r=1,
\qquad N+m=2.
\]

The only positive integer pair is

\[
(N,m)=(1,1).
\]

Hence the quarter-period geometry is trivially unique.

---

## 4. Exact finite layers `k=3,4,5`

The first three nontrivial powers are handled by exact rational certificates.

### Layer `k=3`, `r=2`

`EXACT_MINIMAL_PERIOD_OPTIMALITY_K3.md` proves, uniformly in the odd multiplier,

\[
\Gamma_{2,2,q}>\frac15
\]

while every competing geometry has gap below `1/5` or is super-eight. Hence `(2,2)` is unique.

### Layer `k=4`, `r=4`

`EXACT_MINIMAL_PERIOD_OPTIMALITY_K4.md` proves

\[
\Gamma_{4,4,q}>\frac1{10}
\]

using the all-energy relaxed determinant and an exact degree-16 Bernstein certificate. Every unbalanced geometry satisfies

\[
\Gamma<D_5<\frac1{10}.
\]

Hence `(4,4)` is unique.

### Layer `k=5`, `r=8`

`EXACT_MINIMAL_PERIOD_OPTIMALITY_K5.md` proves

\[
\Gamma_{8,8,q}>\frac1{32}
\]

using a degree-32 exact Bernstein certificate, while

\[
D_9<\frac1{32}.
\]

Hence `(8,8)` is unique.

These certificates are exact rational proofs, not floating-point acceptance tests.

---

## 5. Uniform analytic tail `k>=6`

If

\[
k\ge6,
\]

then

\[
r=2^{k-2}\ge16.
\]

`BALANCED_ALL_PHASE_DIRICHLET_COMPARISON_TAIL.md` proves the non-asymptotic all-phase inequality

\[
\boxed{
\Gamma_{r,r,q}>D_{r+1}
\qquad(r\ge16),
}
\tag{5.1}

uniformly in the odd multiplier.

The proof uses the all-energy single-square characteristic identity at the test energy

\[
y_*=6+2\cos\frac\pi{2(r+1)},
\]

reducing the entire Bloch problem to one scalar Chebyshev inequality. Its key ingredients are:

1. strict log-concavity of
   \[
   R_r(x)=\frac{T_r(x)}{U_{r-1}(x)}
   \]
   to the right of its largest zero, obtained from the interlacing of the zeros of `T_r` and `U_(r-1)`;
2. monotonic strengthening of the two-arc scattering factor as the two Chebyshev arguments move toward balance;
3. explicit lower estimates on the endpoint scattering factor;
4. a separate convexity argument on the two halves of the Bloch phase interval.

Consequently (5.1) and the competitor bound (2.2) imply

\[
\Gamma_{r,r,q}>\Gamma_{N,m,q}
\]

for every unbalanced pair with `N+m=2r`.

Since every `k>=6` produces such an `r`, this closes all remaining layers.

---

## 6. Independent exact audits for higher layers

The analytic tail makes additional finite certificates logically unnecessary, but exact independent audits are available:

- `EXACT_MINIMAL_PERIOD_OPTIMALITY_K6.md` proves the `r=16` layer directly;
- `EXACT_MINIMAL_PERIOD_OPTIMALITY_K7.md` proves the `r=32` layer directly.

Their relaxed balanced determinants have respectively degree `64` and `128` and strictly positive exact Bernstein coefficients. These are useful reproducibility checks on the analytic tail theorem.

---

## 7. Canonical minimal-period phase

Combining Theorem A with the previously proved period optimality gives the following canonical construction for every even jump with `v_2(s)>=2`.

### Corollary B — canonical shortest-period optimizer

Let

\[
2^k\Vert s,
\qquad k\ge2.
\]

Within the reflection-chiral two-defect ansatz, the unique phase satisfying **both**

- minimal primitive period, and
- maximal full Bloch gap at that period,

is the quarter-period geometry

\[
\boxed{
\operatorname{per}(\tau)=2^{k+1},
\qquad
h=2^{k-1}.
}
\tag{7.1}

This statement is exact for every `k>=2`; there is no large-valuation qualifier.

---

## 8. Asymptotic spectral strength of the canonical phase

As `k->infinity`, put

\[
r=2^{k-2}.
\]

The all-orders balanced phase-slip theory gives

\[
\Gamma_{r,r,q}
=\frac{\pi^2}{4r^2}
-\frac{\sqrt2\pi^2}{4r^3}
+O(r^{-4}),
\]

with the full all-orders expansion available in `ALL_ORDERS_GLOBAL_GAP_PHASE_DIAGRAM.md`.

Since the primitive period is

\[
p=8r=2^{k+1},
\]

we recover the optimal normalized limit

\[
\boxed{
p^2\Gamma_{r,r,q}\longrightarrow16\pi^2.
}
\tag{8.1}

Thus the same phase is simultaneously:

- period-optimal within the structural ansatz;
- geometry-optimal at that minimal period for every finite layer;
- asymptotically optimal in period-normalized gap;
- governed by the universal periodic phase-slip expansion.

## 9. Paper-level consequence

The even-jump story can now be stated without any eventuality qualifier:

> **The `2`-adic valuation determines the shortest reflection-chiral two-defect period, and in every such minimal cell the unique spectral optimizer places the two flux defects one quarter-period apart.**

This is the finite counterpart of the balanced macroscopic variational law and supplies a canonical arithmetic periodic phase for every `v_2(s)>=2`.
