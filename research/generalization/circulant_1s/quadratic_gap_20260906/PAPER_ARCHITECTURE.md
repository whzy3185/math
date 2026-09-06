# Manuscript architecture: sharp Bloch gaps and arithmetic obstructions

Date: 2026-09-06
Branch: `research/quadratic-gap-upgrade`

## Working title

**Sharp Bloch Gaps and Arithmetic Obstructions in Signed Circulants `C_N(1,s)`**

Alternative:

**Parity, Phase Slip, and Finite Resonance in Signed Circulants**

## Central message

The manuscript now has two complementary theorem packages.

### Package I — periodic/Bloch sharp asymptotics

For an explicit parity-dependent periodic signing for every integer jump
`s>=2`, prove

\[
 Rhat_s<8,
 \qquad
 s^2(8-Rhat_s)\to\pi^2.
\]

Odd and even jumps reach the same leading constant by different mechanisms.
For even `s=2r`, the true edge has a nonzero phase slip with

\[
 \phi_r=
 \frac\pi{4\sqrt2\,r^2}
 -\frac{3\pi}{16r^3}
 +o(r^{-3}),
\]

and

\[
 e_r-g_{2r}
 =\frac{\pi^2}{32r^4}
 -\frac{3\pi^2}{32\sqrt2\,r^5}
 +o(r^{-5}).
\]

### Package II — finite arithmetic obstruction

For the infinite resonance line

\[
 N=3s,\qquad s\ge7\text{ odd},
\]

prove for **every edge signing**

\[
 \boxed{\rho(A)^2\ge8+1/70.}
\]

Thus every jump has a periodic sub-`sqrt(8)` Bloch construction, while an
infinite family of finite rings admits no sub-`sqrt(8)` signing at all.

## Theorem hierarchy

### Theorem A — all-jump explicit Bloch family

Define the parity-dependent construction:

- odd `s`: period-two alternating flux;
- even `s`: primitive period-`4s` antipodal defect word.

Prove `Rhat_s<8` and the common quadratic envelope

`1/(6s(s+2)) <= 8-Rhat_s <= 4 sin^2(pi/(s+2))`.

### Theorem B — odd-jump exact model

Derive the exact Fourier dispersion, prove uniqueness of the odd optimizer,
obtain

`s U_(s-1)(cos(2 theta_s))=1`,

and conclude `s^2(8-M_s)->pi^2`.

### Theorem C — even antipodal determinant theorem

Develop chirality, the reduced threshold matrix and the exact continuant
characteristic determinant for every even `s`.

### Theorem D — even quadratic gap

Use the two-Chebyshev factorization, covariance/mixture inequality,
Pell-square derivative kernel, coefficient convolution and inverse trace to
prove the `Theta(s^-2)` gap.

### Theorem E — phase-zero endpoint asymptotic

Prove the endpoint Robin limit and

`s^2(8-rho(H_s(1))^2)->pi^2`.

### Proposition F — exact phase-zero failure

Give the exact `s=10` Sturm certificate showing that the true even Bloch edge
need not be at zero phase.

### Theorem G — even global sharp limit

Use hyperbolic localization, exclusion of the soft hyperbolic branch and the
oscillatory Robin limit to prove

`s^2(8-R_s)->pi^2` for even `s`.

### Theorem H — second-order phase slip

Prove

`r^2 phi_r -> pi/(4sqrt2)`

and

`r^4(e_r-g_(2r))->pi^2/32`.

Interpret this as a two-soft-mode avoided crossing with effective law

`z^2-(pi/(2sqrt2))z`.

### Theorem I — first finite-`r` correction

Prove

`phi_r = pi/(4sqrt2 r^2) - 3pi/(16r^3) + o(r^-3)`

and the corresponding `r^-5` gain correction.

### Corollary J — parity-free sharp Bloch limit

Combine odd and even subsequences:

`s^2(8-Rhat_s)->pi^2`.

### Theorem K — exact finite base obstruction at `(21,7)`

Exhaust all switching classes after cyclic `Q`-necklace reduction and prove

`rho(A)^2 >= 1066/131`.

### Lemma L — quantitative nine-column signed-triangle rule

For an open width-three strip of nine arbitrary signed triangles, prove by
exact finite certification that either

`||M||^2 >= 8+1/70`

or the six middle transitions satisfy `B_(j+1)=-B_j`.

The integer witness search leaves exactly 128 final survivors.  The constant
`1/70` is close to the local finite-state boundary: a violating word occurs
numerically near `8.014397`, so `1/69` is already too strong for this lemma.

### Proposition M — exact finite base obstruction at `(27,9)`

After Hamilton gauge there are

`2*8^9 = 268,435,456`

triangle-state/holonomy representatives.  Quantitative exact prefix pruning
at margin `1/70` leaves 1064 length-eight prefixes; their eight extensions in
both holonomy sectors require only

`2*1064*8 = 17,024`

final cyclic checks.  This proves `rho(A)^2>=8+1/70` for every signing of
`C_27(1,9)`.

### Theorem N — infinite `N=3s` all-signing obstruction

For every odd `s>=7`, prove

\[
 m(3s,s)^2\ge8+1/70.
\]

For `s>=11`, apply Lemma L to sliding nine-column windows.  Absence of a
local witness forces all ordinary signed-triangle columns to alternate
`B,-B`.  Across the helical seam this would require an orthogonal similarity
`SBS^T=-B`, impossible because

`tr(B^3)=+/-6`

changes sign under `B -> -B`.

This theorem is the finite-arithmetic counterpart to the Bloch sharp theorem.

## Suggested section plan

1. Introduction: periodic versus finite signed-circulant minimization
2. Gauge and universal squared-operator algebra
3. Odd jumps: exact Fourier model and sharp `pi^2` gap
4. Even jumps: antipodal chirality and exact continuant determinant
5. Positive generating functions and quadratic inverse-trace gap
6. Endpoint Robin asymptotics
7. Exact phase-zero failure
8. Global even sharp `pi^2` theorem
9. Avoided crossing and higher phase-slip asymptotics
10. Width-three representation of the resonance line `N=3s`
11. Quantitative nine-column finite-state lemma
12. Base cases `C_21(1,7)` and `C_27(1,9)`
13. Infinite all-signing `N=3s` obstruction
14. Other finite orders: constructions, resonances and open classification
15. Formal verification and reproducibility boundary
16. Literature comparison and open problems

## Positioning

The block-Jacobi/direct-integral viewpoint is standard periodic-operator
framework and should be cited as such.  The closest direct signed-circulant
comparison is Suvagiya's 2026 `C_n(1,2)` preprint.  The manuscript should
focus novelty claims, if ultimately justified, on the all-jump sharp gap,
even avoided-crossing constants and the all-signing finite arithmetic
obstruction, not on Bloch decomposition itself.

See `LITERATURE_UPDATE_20260906.md` for the current bounded audit.

## Publication-strength boundary

Do not claim:

- a closed formula for `m(N,s)` in general;
- global optimality of the periodic parity-dependent family on arbitrary
  finite orders;
- obstruction for every short odd chord-cycle length;
- phase-zero maximality for even Bloch fibers;
- kernel-checked Lean coverage for uncompiled files;
- publication priority before the broader periodic/magnetic operator audit is
  completed.

## Formalization plan

Keep the new Lean development separate from frozen `formal/TargetA`.
Priority order:

1. odd-jump algebra/trigonometric core;
2. even Chebyshev/Pell/inverse-trace chain;
3. global phase localization;
4. second-order bootstrap and phase-slip constants;
5. signed-triangle identities (`tr(B^3)=6uvw`);
6. finite eight-state local-rule certificate interface;
7. all-`s` Bloch assembly;
8. `N=3s` structural obstruction assembly.

Exact Sturm, Rayleigh and finite-state witnesses should remain reproducible
finite certificates even before full Lean import.
