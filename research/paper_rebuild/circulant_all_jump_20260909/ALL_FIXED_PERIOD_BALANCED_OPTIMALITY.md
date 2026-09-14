# Exact balanced-separation optimality for every period divisible by eight

Date: 2026-09-14

Status: **Proved**. This strengthens the minimal-`2`-adic quarter-period theorem to an arithmetic-free fixed-period statement.

## 1. Setup

Let

\[
r\ge1
\]

be an arbitrary integer. Consider the complete reflection-chiral even-separation two-defect family with

\[
N+m=2r.
\]

Then

\[
L=2(N+m)=4r
\]

and the primitive coefficient period is

\[
\boxed{p=2L=8r.}
\]

For any compatible odd multiplier define

\[
\Gamma_{N,m,q}
=8-\max_{|z|=1}\rho(H_{N,m,q}(z))^2.
\]

The balanced geometry is

\[
\boxed{N=m=r}
\]

and its two positive flux defects are separated by

\[
\boxed{h=2r=p/4.}
\]

## Theorem A — exact all-period balanced optimizer

For every integer

\[
\boxed{r\ge1}
\]

and every compatible odd multiplier,

\[
\boxed{
\Gamma_{r,r,q}
>
\Gamma_{N,m,q}
}
\tag{1.1}

for every positive integer pair

\[
N+m=2r,
\qquad
(N,m)\ne(r,r).
\]

Thus in **every coefficient period divisible by eight**, the unique full-Bloch gap-maximizing even-separation reflection-chiral two-defect geometry is the quarter-period geometry

\[
\boxed{h=p/4.}
\tag{1.2}

For `r=1` the statement is vacuous because `(1,1)` is the only geometry; for every `r>=2` the inequality is strict against genuine competitors.

---

## 2. Universal reduction

For every geometry put

\[
M=\max\{N,m\}.
\]

`UNIVERSAL_ENDPOINT_DIRICHLET_UPPER_BOUND.md` gives

\[
\Gamma_{N,m,q}<D_M,
\qquad
D_M=2-2\cos\frac\pi{2M}.
\tag{2.1}
\]

For an unbalanced pair with `N+m=2r`,

\[
M\ge r+1,
\]

and `D_M` is decreasing. Hence

\[
\boxed{
\Gamma_{N,m,q}<D_{r+1}.
}
\tag{2.2}

Therefore it suffices, for each `r`, to prove

\[
\boxed{
\Gamma_{r,r,q}>D_{r+1}.
}
\tag{2.3}

The proof of (2.3) is finite for `r<=8` and analytic for `r>=9`.

---

## 3. Exact finite range `1<=r<=8`

### `r=1`

Only `(N,m)=(1,1)` exists.

### `r=2`

`EXACT_MINIMAL_PERIOD_OPTIMALITY_K3.md` gives an exact rational separator and proves balanced optimality.

### `r=3,5,6,7`

`EXACT_FIXED_PERIOD_BALANCED_OPTIMALITY_R3_R5_R6_R7.md` gives exact rational all-energy Bernstein certificates and endpoint derivative certificates.

### `r=4`

`EXACT_MINIMAL_PERIOD_OPTIMALITY_K4.md` proves the result using a degree-16 exact Bernstein certificate.

### `r=8`

`EXACT_MINIMAL_PERIOD_OPTIMALITY_K5.md` proves the result using a degree-32 exact Bernstein certificate.

Thus (2.3) is proved for every integer `r<=8`.

---

## 4. Analytic tail `r>=9`

`BALANCED_ALL_PHASE_DIRICHLET_COMPARISON_TAIL.md` proves directly, without computation,

\[
\boxed{
\Gamma_{r,r,q}>D_{r+1}
\qquad(r\ge9),
}
\tag{4.1}

uniformly in the odd multiplier.

The proof evaluates the exact all-energy single-square characteristic identity at

\[
y_*=6+2\cos\frac\pi{2(r+1)}
\]

and proves positivity for the complete Bloch phase interval. Its central structure is the strict log-concavity of

\[
R_r(x)=\frac{T_r(x)}{U_{r-1}(x)}
\]

on the relevant hyperbolic domain, derived from the interlacing of the Chebyshev zeros.

Combining (4.1) with the competitor bound (2.2) gives the strict balanced inequality for all `r>=9`.

This completes the proof of Theorem A.

---

## 5. Independent high-period audits

The following exact certificates are no longer logically needed but independently audit the analytic tail:

- `EXACT_MINIMAL_PERIOD_OPTIMALITY_K6.md`: `r=16`;
- `EXACT_MINIMAL_PERIOD_OPTIMALITY_K7.md`: `r=32`.

Their relaxed balanced determinants have degree `64` and `128`, respectively, with all exact Bernstein coefficients strictly positive.

---

## Corollary B — all-layer minimal `2`-adic optimizer

Let

\[
2^k\Vert s,
\qquad k\ge2.
\]

The shortest compatible primitive period is

\[
p_{\min}=2^{k+1}=8\cdot2^{k-2}.
\]

Applying Theorem A with

\[
r=2^{k-2}
\]

gives immediately:

\[
\boxed{
\text{the unique gap-maximizing geometry at }p_{\min}
\text{ has }h=p_{\min}/4.
}
\]

Thus `ALL_LAYER_MINIMAL_PERIOD_QUARTER_OPTIMALITY.md` is a direct arithmetic specialization of the stronger fixed-period theorem.

---

## 7. Variational interpretation

The theorem has a simple geometric content.  At fixed period `8r`, moving one lattice unit away from balance forces one soft arc to have length at least `r+1`.  Its special endpoint already bounds the full Bloch gap by the next Dirichlet level `D_(r+1)`.  The balanced two-well system, despite its periodic Bloch phase slip, remains strictly above that level.

Hence the discrete geometry optimization and the continuous Bloch optimization separate cleanly:

1. **geometry:** exact balance `N=m` is uniquely optimal at every admissible period `8r`;
2. **Bloch phase:** within that geometry, the periodic cusp shifts the maximizing phase by `Theta(r^-2)` and produces the all-orders phase-slip series.

This is the exact finite-period counterpart of the macroscopic balanced-geometry law.
