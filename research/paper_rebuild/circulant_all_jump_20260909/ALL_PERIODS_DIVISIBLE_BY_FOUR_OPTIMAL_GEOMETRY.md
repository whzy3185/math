# Exact optimal two-defect geometry for every period divisible by four

Date: 2026-09-14

Status: **Proved**. This is the strongest finite-period geometry theorem in Paper I.

## 1. Setup

Consider the complete reflection-chiral even-separation two-defect family.  Write

\[
L=2(N+m),
\qquad
h=2m,
\]

so the primitive coefficient period is

\[
p=2L=4(N+m).
\]

For every compatible odd multiplier define

\[
\Gamma_{N,m,q}
=8-\max_{|z|=1}\rho(H_{N,m,q}(z))^2.
\]

We classify the unique maximizer of `Gamma` at every admissible period.

---

## Theorem A — complete fixed-period geometry classification

Let

\[
\boxed{4\mid p.}
\]

Then the unique gap-maximizing even-separation reflection-chiral two-defect geometry is determined as follows.

### Case I: `p=8r`

For every integer `r>=1`,

\[
\boxed{N=m=r.}
\]

Equivalently,

\[
\boxed{h=p/4.}
\]

Thus every period divisible by eight has a unique exactly balanced quarter-period optimizer.

### Case II: `p=8r+4`, `1<=r<=5`

The unique optimizer is

\[
\boxed{(N,m)=(r+1,r).}
\]

Equivalently,

\[
\boxed{h=2r=\frac{p-4}{4}.}
\]

The defect arc is the shorter of the two nearest-balanced arcs.

### Case III: `p=8r+4`, `r>=6`

The unique optimizer is

\[
\boxed{(N,m)=(r,r+1).}
\]

Equivalently,

\[
\boxed{h=2r+2=\frac{p+4}{4}.}
\]

The defect arc is the longer of the two nearest-balanced arcs.

Hence the only finite orientation transition in the entire fixed-period problem occurs between

\[
\boxed{p=44\quad(r=5)}
\]

and

\[
\boxed{p=52\quad(r=6).}
\]

---

## 2. Proof for `p=8r`

`ALL_FIXED_PERIOD_BALANCED_OPTIMALITY.md` proves that for every integer `r>=1`, the unique optimizer under

\[
N+m=2r
\]

is

\[
N=m=r.
\]

Its proof consists of:

- exact rational certificates for `r<=8`;
- the analytic all-phase theorem `BALANCED_ALL_PHASE_DIRICHLET_COMPARISON_TAIL.md` for every `r>=9`.

This proves Case I.

---

## 3. Proof for `p=8r+4`, `r<=8`

Here

\[
N+m=2r+1,
\]

so exact balance is impossible.

`EXACT_ODD_TOTAL_ORIENTATION_R1_R5.md` proves

\[
(r+1,r)
\]

is uniquely optimal for `r=1,...,5`.

`EXACT_ODD_TOTAL_ORIENTATION_R6_R8.md` proves

\[
(r,r+1)
\]

is uniquely optimal for `r=6,7,8`.

All certificates use exact rational arithmetic.  Their reproducibility script is

`verify_exact_odd_total_orientation_switch.py`.

This proves Case II and the first three layers of Case III.

---

## 4. Proof for `p=8r+4`, `r>=9`

`ODD_TOTAL_EFFECTIVE_TAIL_R9.md` proves a fully explicit analytic tail.

Put

\[
\ell=r+1.
\]

For the periodic-near-balanced orientation

\[
A=(\ell,\ell-1),
\]

and compressed-antiperiodic orientation

\[
B=(\ell-1,\ell),
\]

that theorem gives

\[
\boxed{
e_A^+-\Gamma_A>\frac1{25\ell^4}}
\]

and

\[
\boxed{
0<e_A^+-\Gamma_B<\frac1{100\ell^4}}.
\]

Therefore

\[
\boxed{
\Gamma_B-\Gamma_A>\frac3{100\ell^4}>0.
}
\]

Moreover

\[
e_A^+-D_{\ell+1}>\frac1{8\ell^3}
\]

and hence

\[
\Gamma_B>D_{\ell+1}.
\]

Every geometry other than the two nearest-balanced orientations has

\[
\max\{N,m\}\ge\ell+1
\]

and the universal endpoint Dirichlet bound gives

\[
\Gamma_{N,m,q}<D_{\ell+1}.
\]

Thus `B=(r,r+1)` is uniquely optimal for every `r>=9`, proving the rest of Case III.

---

## 5. Geometric interpretation

The complete fixed-period law has two layers.

### Even half-total

When `p/4=N+m` is even, integer balance exists and is always uniquely optimal:

\[
N=m.
\]

### Odd half-total

When `p/4=N+m` is odd, the two closest integer geometries differ only by orientation.  For small cells the periodic-cusp orientation wins; after the single finite switch at `r=6`, the compressed-antiperiodic orientation wins forever.

At large `r` the orientation splitting is

\[
\boxed{
\Gamma_{r,r+1,q}-\Gamma_{r+1,r,q}
\sim\frac{\pi^2}{32r^4},
}

while moving farther from balance costs `Theta(r^-3)`.

Thus the exact finite theorem is the lattice realization of the macroscopic balanced-geometry principle.

---

## 6. Corollary for minimal `2`-adic periods

If

\[
2^k\Vert s,
\qquad k\ge2,
\]

then the shortest compatible period is

\[
p_{\min}=2^{k+1},
\]

which is divisible by eight.  Case I therefore immediately gives the canonical minimal-period optimizer

\[
\boxed{h=p_{\min}/4.}
\]

Hence the `2`-adic canonical phase is now a direct corollary of the stronger all-period geometry classification.

---

## 7. Paper-level significance

There is no remaining fixed-period geometry problem inside the complete even-separation reflection-chiral two-defect family:

\[
\boxed{
\text{every admissible period }4\mid p
\text{ has a unique explicitly classified spectral optimizer.}
}
\]

The remaining research questions concern enlarging the variational class beyond two defects, not optimizing geometry within this family.