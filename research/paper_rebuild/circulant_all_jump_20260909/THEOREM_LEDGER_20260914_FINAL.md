# Final theorem ledger — 2026-09-14

Branch: `paper/circulant-periodic-gap-20260909`

This ledger supersedes all earlier Paper I ledgers.

---

# I. Exact finite geometry

## F1. Exact sub-eight phase diagram

\[
\boxed{R_{N,m,q}<8\iff 2m<T_N(3).}
\]

Primary file: `EXACT_GENERAL_SEPARATION_PHASE_DIAGRAM.md`.

The largest safe defect parameter is

\[
M_N=\frac{T_N(3)-1}{2}=1,8,49,288,1681,9800,\ldots
\]

and

\[
\frac{M_N(M_N+1)}2=U_{N-1}(3)^2.
\]

Primary file: `PELL_SQUARE_TRIANGULAR_PHASE_BOUNDARY.md`.

## F2. Every period `p=8r`: exact balanced optimizer

For every integer `r>=1`, among all even-separation reflection-chiral two-defect geometries with `N+m=2r`, the unique full-Bloch gap maximizer is

\[
\boxed{N=m=r,\qquad h=p/4.}
\]

Primary file: `ALL_FIXED_PERIOD_BALANCED_OPTIMALITY.md`.

Exact finite certificates cover `r<=8`; `BALANCED_ALL_PHASE_DIRICHLET_COMPARISON_TAIL.md` proves the analytic tail `r>=9`.

## F3. Minimal `2`-adic period: canonical optimizer in every layer

If `2^k || s`, `k>=2`, the shortest compatible period is

\[
p_{min}=2^{k+1},
\]

and the unique optimizer at that period has

\[
\boxed{h=p_{min}/4.}
\]

Primary files:

- `ALL_LAYER_MINIMAL_PERIOD_QUARTER_OPTIMALITY.md`;
- `CANONICAL_QUARTER_PERIOD_2ADIC_PHASE.md`.

## F4. Periods `p=8r+4`: exact finite orientation switch through `r=8`

For `N+m=2r+1`:

\[
\boxed{1\le r\le5:\ (r+1,r)\text{ uniquely optimal},}
\]

\[
\boxed{6\le r\le8:\ (r,r+1)\text{ uniquely optimal}.}
\]

Primary files:

- `EXACT_ODD_TOTAL_ORIENTATION_R1_R5.md`;
- `EXACT_ODD_TOTAL_ORIENTATION_R6_R8.md`;
- `verify_exact_odd_total_orientation_switch.py`.

The eventual theorem proves `(r,r+1)` for sufficiently large `r`.  Current main finite-tail target: make it effective from `r>=9`.

---

# II. Exact all-energy algebra

## A1. General all-energy formula

`GENERAL_SEPARATION_ALL_ENERGY_CHARACTERISTIC.md` reduces the entire Bloch characteristic to scalar Chebyshev data and

\[
P(y;d,e)=\mathcal G(y,d)-e.
\]

## A2. Single-square identity

With

\[
x=\frac{y-d-4}{2},\qquad a=\frac{y+d-4}{2},
\]

\[
Z=T_N(x)T_m(a)+(ax-3)U_{N-1}(x)U_{m-1}(a),
\]

\[
\boxed{
P(y;d,e)=4[Z^2-1+(d-2)U_{m-1}(a)^2]+(2-e).
}
\]

Primary file: `ALL_ENERGY_SINGLE_SQUARE_IDENTITY.md`.

## A3. Orientation-duality identity

\[
\boxed{
P_{N,m}(y;d,e)-P_{m,N}(y;-d,e)
=4[(d+2)U_{N-1}(x)^2-(2-d)U_{m-1}(a)^2].
}
\]

Primary file: `ORIENTATION_DUALITY_CHARACTERISTIC_IDENTITY.md`.

---

# III. Macroscopic and all-orders theory

## M1. Leading full-Bloch law

If `h/L -> alpha in (0,1)`,

\[
\boxed{
L^2\Gamma\to\frac{\pi^2}{\max\{\alpha,1-\alpha\}^2}.
}
\]

Balanced geometry uniquely maximizes the leading constant, with

\[
p^2\Gamma\to16\pi^2.
\]

## M2. Universal endpoint Robin series

There is a universal all-orders series

\[
A(\ell)=\sum_{j\ge2}a_j\ell^{-j}.
\]

Primary file: `ALL_ORDERS_MACROSCOPIC_ROBIN_EXPANSION.md`.

## M3. Universal periodic cusp series

There is a universal periodic phase-slip/gain series

\[
C(N)=\sum_{j\ge0}c_jN^{-j-4}.
\]

Primary file: `ALL_ORDERS_PERIODIC_PHASE_SLIP_EXPANSION.md`.

## M4. Correct algebraic global phase diagram

To every algebraic order,

\[
\boxed{\Gamma\sim A(N)-C(N),\qquad m\le N,}
\]

\[
\boxed{\Gamma\sim A(m),\qquad m>N.}
\]

Primary file: `ALL_ORDERS_GLOBAL_GAP_PHASE_DIAGRAM.md`.

---

# IV. Correct hard-channel tunneling sector

For `m>N`, put

\[
n=2q+1,\qquad U_N=U_{N-1}(3).
\]

The globally selected well is compressed-antiperiodic, `d≈-2`.  The best exact roots of `z^n=-1` are `z_0=e^{+-i pi/n}`.

The first odd-multiplier-dependent gap correction is

\[
\boxed{
 e^-_{N,m}-\Gamma_{N,m,q}
=
\frac{(2+2\cos(\pi/n))\pi^2}
{64\sqrt2\,U_Nm^3}
(1+O(m^{-1}))
+O(U_N^{-2}m^{-6}).
}
\]

The maximizing compressed displacement is

\[
\boxed{
\delta_*
=-\frac{\pi^2\sin(\pi/n)}
{64\sqrt2\,n\,U_Nm^3}
(1+O(m^{-1}))
+O(U_N^{-2}m^{-6}).
}
\]

Thus the correct beyond-all-orders scale is

\[
\boxed{U_N^{-1}m^{-3}\asymp(3+2\sqrt2)^{-N}m^{-3}.}
\]

Primary file: `ANTIPERIODIC_SEAM_TUNNELING_ASYMPTOTIC.md`.

Historical claims of exact physical `z=-1` locking for arbitrary odd multiplier, and the intermediate overstrong scale `(3+2sqrt2)^(-2N)`, are retracted.

---

# V. Quantitative stability

## S1. Period `p=8r`

For large `r`, the unique runner-up after balanced `(r,r)` is `(r-1,r+1)`. The first-versus-second stability gap satisfies

\[
\boxed{\Delta_r\sim\frac{\pi^2}{2r^3}=\frac{256\pi^2}{p^3}.}
\]

The first odd-multiplier dependence is the positive tunneling correction of order

\[
U_{r-2}(3)^{-1}(r+1)^{-3}.
\]

Primary file: `SECOND_BEST_GEOMETRY_AND_STABILITY_GAP.md`.

## S2. Period `p=8r+4`

The nearest-orientation splitting is

\[
\Gamma_{r,r+1,q}-\Gamma_{r+1,r,q}
\sim\frac{\pi^2}{32r^4},
\]

while geometries farther from balance lose at order `r^-3`.  The hard-channel tunneling correction is exponentially smaller.

Primary file: `ODD_TOTAL_EVENTUAL_OPTIMAL_ORIENTATION.md`.

---

# VI. Current strongest manuscript thesis

> **Reflection-chiral two-defect phases in signed step circulants form an exactly solvable arithmetic scattering family. Their threshold region has an exact Chebyshev/Pell phase diagram and their arbitrary-energy Bloch determinant collapses to a single-square identity. At every period divisible by eight the unique optimizer is the balanced quarter-period geometry; at periods congruent to four modulo eight an exact finite orientation switch is already located between `r=5` and `r=6`. The shortest `2`-adic period therefore has a canonical optimizer in every layer. The Bloch edge admits universal all-orders Robin and avoided-crossing expansions, and the first odd-multiplier dependence is an explicitly computed hard-channel tunneling correction.**

Next primary target: prove `(r,r+1)` is optimal for every `r>=9` when `p=8r+4`, completing the geometry classification for every period divisible by four.