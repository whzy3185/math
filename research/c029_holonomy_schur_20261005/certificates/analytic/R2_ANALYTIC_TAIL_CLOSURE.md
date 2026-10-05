# An explicit analytic closure of the residue-two Schur tail

Date: 2026-10-05. Project: C029, signed even cycle squares, August Target A.

## Result and evidence boundary

Let k ≥ 6, n = 8k+2, and let A_n be the signed adjacency matrix of C_n(1,2)
whose length-one edges have sign +1 and whose length-two edge from i to i+2
has sign τ_i. Indices are taken modulo n. Put

    t = (1,1,−1,1,−1,−1,1,−1),
    τ_i = t_(i mod 8) for 0 ≤ i ≤ n−2,   τ_(n−1) = −1.

Equivalently, τ is k copies of t followed by (1,−1). Its quadrilateral
fluxes τ_i τ_(i+1) have positive positions 0,4,…,n−6, hence exactly one
cyclic gap of length six and all other gaps of length four. Its Hamilton
cycle holonomy is +1.

**Theorem.** For every k ≥ 6,

    (198/25) I_n − A_n² ≻ 0,
    ρ(A_n)² < 198/25 < 4+2 cos(2π/n)+2 cos(4π/n) = ρ_−(n)².

This closes the previously open response-majorant route for this explicit
residue-two family. The infinite tail argument below is analytic; its
finitely many rational premises have been independently checked using the
attached standard-library Fraction verifier. The result is therefore a
finite-certificate-assisted analytic theorem, not a claim of a
computation-free classification of all signings. It does not determine the
global minimum m_n, does not classify minimizing signings, and says nothing
new about residues four or six. The historical all-even truth-value
classification was already computer-assisted; this is a new, shorter proof
of one infinite constituent, not a new truth set.

## 1. Exact normalized block reduction

Throughout this note M_n = (198/25)I_n − A_n². Partition its indices into

    V_0 = {0,1},
    V_j = {2+4(j−1),…,5+4(j−1)},   1 ≤ j ≤ m = 2k.

The diagonal block on every V_j, j ≥ 1, is

    D = [98/25  0      −1      0    ]
        [0      98/25   0     −1    ]
        [−1     0       98/25  0    ]
        [0     −1       0      98/25].

The coupling from V_j to V_(j+1) is E_+ for j odd and E_− for j even,
where

    E_+ = [−1  0  0  0]       E_− = [−1  0  0  0]
          [ 0  1  0  0]             [ 0  1  0  0]
          [−1  2  1  0]             [−1 −2  1  0]
          [ 2 −1  0 −1],            [−2 −1  0 −1].

The exceptional boundary blocks are

    G_0 = (98/25) I_2,    H_0 = D,
    R_0 = [−1 −2 1  0],   C_0 = [−1  0 −1  0],
          [−2 −1 0 −1]          [ 0 −1  0 −1]
    W_0 = [0 0 −1 0]
          [0 0  0 1]
          [0 0  0 0]
          [0 0  0 0].

Here R_0 = M[V_0,V_1], C_0 = M[V_0,V_m], W_0 = M[V_1,V_m].
All remaining non-nearest bulk blocks vanish.

These identities follow directly, for n ≥ 50, from

    (A²)_(i,i) = 4,
    (A²)_(i,i+1) = τ_(i−1)+τ_i,
    (A²)_(i,i+2) = 1,
    (A²)_(i,i+3) = τ_i+τ_(i+1),
    (A²)_(i,i+4) = τ_i τ_(i+2),

their transposes, and zero entries at larger cyclic distances. Substituting
the eight-periodic interior and the two terminal signs gives the displayed
blocks. The verifier additionally reconstructs the signed graph by integer
two-hop walks and compares every entry at n = 50,58,66,410. Those checks
test implementation alignment; the displayed local formulas prove the
all-length identity.

Use zero-based elimination index j. Initially X_0 = D. Let E_j = E_+ for
j even and E_− for j odd. The length-independent open-chain recurrence is

    X_(j+1) = D − E_jᵀ X_j⁻¹ E_j,
    R_(j+1) = −R_j X_j⁻¹ E_j,
    W_(j+1) = −E_jᵀ X_j⁻¹ W_j,
    G_(j+1) = G_j − R_j X_j⁻¹ R_jᵀ,
    H_(j+1) = H_j − W_jᵀ X_j⁻¹ W_j,
    C_(j+1) = C_j − R_j X_j⁻¹ W_j.

For m even the terminal elimination index is p = m−2, which is even.
At this elimination only, replace W_p by W_p+E_+. Thus the retained
six-by-six core S_m on V_0 ∪ V_m is

    S_m = [ G_p − R_p X_p⁻¹ R_pᵀ,
            C_p − R_p X_p⁻¹ (W_p+E_+) ;
            transpose,
            H_p − (W_p+E_+)ᵀ X_p⁻¹ (W_p+E_+) ].

Repeated Schur congruence proves that M_n ≻ 0 exactly when its eliminated
four-by-four pivots and S_m are positive. The core dimension is six and the
normalization is fixed throughout. Below, S_26 corresponds to n = 106;
subscripts on S denote block counts, not graph orders.

## 2. Finite rational premises

Put F_±(X)=D−E_±ᵀX⁻¹E_± and Φ=F_−∘F_+. Let B=Φ¹²(D)=X_24 and
Y=F_+(B). Define

    P = (1/10000) [10766    87    19    974]
                  [   87 12664   148  −2418]
                  [   19   148 10093    −25]
                  [  974 −2418   −25  14009],

    Q = (1/10000) [11503   614   990  −1101]
                  [  614 10470    15    113]
                  [  990    15 12299  −2632]
                  [−1101   113 −2632  13260].

Let r=10⁻¹⁰ and L_B=B⁻¹E_+Y⁻¹E_−. The exact verifier proves:

1. Every pivot X_0,…,X_24 is positive; B,Y ≻ I_4/2
2. (9/10)I_4 ≺ P,Q ≺ 2I_4
3. L_Bᵀ P L_B ≺ (2/5)P and L_B Q L_Bᵀ ≺ (2/5)Q
4. ||Φ(B)−B||_F < r/40
5. R_24 Q R_24ᵀ ≺ 10⁻¹⁰ I_2 and W_24ᵀ Q W_24 ≺ 10⁻¹⁰ I_4
6. S_26 − (1/50)I_6 ≻ 0
7. S_m ≻ 0 at m = 12,14,16,18,20,22,24

All matrices in these premises are explicitly rational. Positive-definiteness
tests use exact LDL pivots, and the residual test compares the sum of entry
squares with (r/40)². No floating eigenvalue, approximate convergence or
solver tolerance is used. Full rational seed and center matrices, including
the six positive LDL pivots for item 6, are in r2_exact_certificate.json.

## 3. A transparent local Riccati contraction

For symmetric H define the P order-unit norm

    |H|_P = inf{a ≥ 0 : −aP ≼ H ≼ aP}
          = ||P⁻¹ᐟ² H P⁻¹ᐟ²||_2.

Consider the closed ball K={X=Xᵀ : |X−B|_P ≤ r}. Since P ≼ 2I,

    ||X−B||_2 ≤ 2r =: e.

The exact lower bounds B,Y ≻ I/2 imply X ≻ I/3 and ||X⁻¹||_2 ≤ 3.
The inverse identity and ||B⁻¹||_2 ≤ 2 give

    ||X⁻¹−B⁻¹||_2 ≤ 6e.

Because ||E_±||_F²=14, writing Y_X=F_+(X) yields

    ||Y_X−Y||_2 ≤ 84e < 1/6.

Consequently Y_X ≻ I/3, ||Y_X⁻¹||_2 ≤ 3 and

    ||Y_X⁻¹−Y⁻¹||_2 ≤ 504e.

Define L(X)=X⁻¹E_+Y_X⁻¹E_−. Splitting the product difference at one
factor at a time proves

    ||L(X)−L_B||_2 ≤ 14(6·3+2·504)e = 14364e.

The P-column norm and Q-row norm both differ from the Euclidean operator
norm by a factor at most sqrt(20/9)<3/2. Their conventions are

    ||L||_(P,col)=||P¹ᐟ² L P⁻¹ᐟ²||_2,
    ||L||_(Q,row)=||Q⁻¹ᐟ² L Q¹ᐟ²||_2.

Thus the perturbation in either norm is below 21546e=43092r<1/10000.
Since sqrt(2/5)+1/10000<2/3, on all of K we have

    L(X)ᵀ P L(X) ≺ (4/9)P,
    L(X) Q L(X)ᵀ ≺ (4/9)Q.                 (3.1)

Direct differentiation gives DΦ_X[H]=L(X)ᵀ H L(X). If −aP≼H≼aP,
then (3.1) gives −(4a/9)P≼DΦ_X[H]≼(4a/9)P. Hence the derivative,
and therefore Φ on the convex ball K, is 4/9-Lipschitz in |·|_P.

The residual has |Φ(B)−B|_P < (10/9)(r/40)=r/36, so

    |Φ(X)−B|_P < r/36+(4/9)r = (17/36)r < r.

Banach's theorem supplies a unique X_* in K fixed by Φ. The actual
even orbit starts at B, so for every h ≥ 0,

    ||X_(24+2h)−X_*||_2 ≤ 4r(4/9)^h.      (3.2)

The constant 4r is deliberately loose: the diameter of K suffices. All
these even pivots and their odd partners are ≻ I/3. Combined with the
finite entrance, every required pivot is positive for every chain length.

This proof avoids the previous ten-coordinate derivative estimate entirely.
It uses the four-dimensional positive-map structure of the derivative.

## 4. Response decay with the correct orientation

Two successive updates multiply R on the right by L(X) and W on the left
by L(X)ᵀ. The second inequality in (3.1), together with the entrance
premises, yields for q=2/3

    R_(24+2h) Q R_(24+2h)ᵀ ≺ 10⁻¹⁰ q^(2h) I_2,
    W_(24+2h)ᵀ Q W_(24+2h) ≺ 10⁻¹⁰ q^(2h) I_4.

Since Q≽(9/10)I, both ordinary operator norms are bounded by

    ||R_(24+2h)||_2, ||W_(24+2h)||_2 < a q^h,
    a=1/30000.

Every single-step transfer has norm at most 3||E_±||_F<12. Thus both
even and odd members of the h-th pair obey the common bound

    ||R_j||_2, ||W_j||_2 ≤ b q^h,
    b=12a=1/2500,   j∈{24+2h,25+2h}.     (4.1)

The common Q metric is valid in these two different response orientations
because both quadratic updates involve L Q Lᵀ. A column-only inequality
Lᵀ Q L would not justify these conclusions.

## 5. A term-by-term Schur-tail estimate

Define G_∞, H_∞, C_∞ by summing the actual infinite open-chain trajectory:

    G_∞ = G_0 − Σ_(j≥0) R_j X_j⁻¹ R_jᵀ,
    H_∞ = H_0 − Σ_(j≥0) W_jᵀ X_j⁻¹ W_j,
    C_∞ = C_0 − Σ_(j≥0) R_j X_j⁻¹ W_j.

These series converge absolutely, because of (4.1) and ||X_j⁻¹||_2≤3
after j=24. This definition is important: the series use the actual X_j,
so no replacement of every pivot by X_* and no missing inverse-error
terms inside the sums are needed.

Set

    S_∞ = [G_∞  C_∞; C_∞ᵀ  H_∞−E_+ᵀX_*⁻¹E_+].

For an even m≥26 put p=m−2=24+2h. Each Schur series tail beginning at
p+1 has norm at most the deliberately larger bound beginning at p,

    T_h = 6 b² q^(2h)/(1−q²).             (5.1)

There are two single-block terms per pair, each at most 3b²q^(2h).
That factor two is explicit in (5.1).

Subtracting the exact finite-core formula from S_∞ gives:

    ||ΔG||_2 ≤ T_h,
    ||ΔC||_2 ≤ T_h+12a q^h,
    ||ΔH||_2 ≤ T_h+24a q^h+144δ θ^h,

where δ=4r and θ=4/9. The C correction is the terminal term
R_p X_p⁻¹ E_+, whose norm is at most 12a q^h. The H cross terms are
W_pᵀX_p⁻¹E_+ and its transpose, together at most 24a q^h. Finally

    ||X_p⁻¹−X_*⁻¹||_2 ≤ 9||X_p−X_*||_2 ≤ 9δ θ^h,

so the terminal pure-pivot correction has norm at most
||E_+||_F²9δθ^h ≤144δθ^h. These are all terminal terms.

The elementary block norm bound ||[U V;Vᵀ Z]||_2≤||U||_2+2||V||_2+||Z||_2
therefore gives the explicit all-length estimate

    ||S_m−S_∞||_2 ≤ 4T_h+48a q^h+144δ θ^h
                  ≤ 251089/156250000
                  < 1/500.               (5.2)

The geometric powers only decrease for h≥0. The exact rational expression
in (5.2) is its h=0 upper bound.

## 6. Positive cores and the spectral conclusion

The seed S_26≻(1/50)I_6 and (5.2), applied twice, show for every even
m≥26 that

    ||S_m−S_26||_2 < 2/500 = 1/250,
    S_m ≻ (1/50−1/250)I_6 = (2/125)I_6.

Both tail errors are necessary; the seed is not the limit. The seven
remaining even block counts 12≤m<26 are covered by exact six-by-six
LDL positivity. The Schur criterion and the proved bulk positivity now give
M_n≻0 for every n=8k+2, k≥6.

The core lower bound is not being asserted as the same lower bound on
M_n: Schur congruence preserves positivity, not Euclidean eigenvalue
gaps. Positivity alone proves ρ(A_n)²<198/25.

Finally cos x>1−x²/2 for x>0 and π²<10 imply

    ρ_−(n)² > 8−20π²/n² > 8−200/n² ≥ 198/25

for n≥50. This proves the theorem.

## 7. Corrections to the inherited draft and scope

This continuation repairs five distinct issues in the September draft:

1. The old seed verifier retained an unnormalized eight-by-eight core of
   198I−25A², while the response recurrence retained a normalized
   six-by-six core of (198/25)I−A². The 9/20 margin was not transferable.
   The freshly checked six-by-six margin is 1/50. At n410, exact LDL
   actually rejects the purported 9/20 margin and also rejects 1/20
2. A seed-to-limit-to-core argument costs two tail errors
3. There are two Schur increments per complete two-block transfer
4. The terminal C block has a linear correction as well as the H block
5. Summing the actual pivot trajectory removes the unnecessary unresolved
   pivot-inverse-difference comparison inside every Schur-series term

The new P order-unit proof also replaces the fragile ten-coordinate local
derivative estimates with a direct positive-map argument.

No G6 spectral multiplicity, Feshbach rank, all-interface theorem, global
optimality claim, or Lean formalization is used here. In particular, nothing
revives the withdrawn r-dimensional G6 statement; the historical 2r
correction remains in force.

## Reproduction and provenance

Run:

    python verify_r2_certificate.py

This is newly authored audit code using only Python's standard library.
It does not import or execute historical repository modules. It writes
r2_exact_certificate.json; verification_output.json preserves the actual
stdout from the run. Diagnostic tests of excessively large seed margins are
kept separate from required passing checks. The finite expansion through
n410 is an extra audit; the proof only needs the seven bases through n98
and the n106 seed.

Frozen baseline: analytic-proof-first at
7b6a351cc5f8f83f5527b7fc547f0a865ea50cf2. Principal sources:

- [Block template](https://github.com/whzy3185/math/blob/7b6a351cc5f8f83f5527b7fc547f0a865ea50cf2/research/proof_closure/r2_block_riccati_template.json)
- [Response recurrence](https://github.com/whzy3185/math/blob/7b6a351cc5f8f83f5527b7fc547f0a865ea50cf2/research/analytic_inventory/r2_response_recurrence.md)
- [P and Q certificates](https://github.com/whzy3185/math/blob/7b6a351cc5f8f83f5527b7fc547f0a865ea50cf2/research/analytic_inventory/r2_response_transfer.md)
- [Unclosed tail draft](https://github.com/whzy3185/math/blob/7b6a351cc5f8f83f5527b7fc547f0a865ea50cf2/research/analytic_inventory/r2_tail_majorant_lemma.md)
- [Old seed implementation showing different normalization and dimension](https://github.com/whzy3185/math/blob/7b6a351cc5f8f83f5527b7fc547f0a865ea50cf2/research/scripts/verify_target_a_r2_boundary_seed.py)

Historical assertions are not treated as proof. The new all-length estimates
above are self-contained, and the stated finite premises were freshly
recomputed. Independent line audit is recorded in a separate audit report;
this note does not represent external peer review.
