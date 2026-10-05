# Unequal one-G6 cells: a uniform Schur bound and a full R4 family

Date: 2026-10-05. Scope: the original signed cycle-square problem.

## Results and present evidence status

For j≥1 define the legal triangle-flux cell

    w_j=(1,1,−1,1,−1,−1,1,−1)^j || (1,−1),
    h_j=8j+2.

Concatenate r≥1 such cells, with independently chosen positive integers
j_0,…,j_(r−1). Let N be the sum of their lengths. Give the Hamilton cycle
holonomy α∈{−1,+1}: write a_i=1 except a_(N−1)=α, and define

    sign{i,i+1}=a_i,
    sign{i,i+2}=τ_i a_i a_(i+1),

where τ is the concatenated word. This construction has exactly r gaps of
length six between positive quadrilateral fluxes, all other gaps having
length four. The separations may be unequal.

**Unequal-cell theorem.** For either holonomy and every number of cells,

    min h_i≥106  implies  ρ(A_N)²<198/25=7.92,                (1)
    min h_i≥202  implies  ρ(A_N)²<790537/100000=7.90537.       (2)

The constants and minimum cell lengths are independent of r. The proof is
a direct block-cyclic Schur assembly, not a periodic Fourier decomposition.

**Full R4 consequence.** For every integer k≥6, put

    j_0=floor(k/2), j_1=ceil(k/2),
    N=(8j_0+2)+(8j_1+2)=8k+4,
    τ=w_(j_0)||w_(j_1), α=−1.

Then

    ρ(A_N)²<198/25<ρ_−(N)².                                 (3)

For even k this is the earlier balanced two-G6 family. For odd k its two
separations are N/2−4 and N/2+4, rather than N/2. Thus it is an explicitly
changed construction. It completes the residue-four counterexample family
analytically with finitely many exact bases; it does not classify minima.

The choice of 7.92 in (3) is substantive: it is below the inherited R4
target 2679/338 and below the twisted benchmark already at N=52. The
stronger cap 7.90537 fails even for this changed construction at N=60, as
shown by an exact negative-pivot certificate. It cannot simply replace 7.92
throughout (3).

The complete derivation, primary exact verification, and independent
mathematical review all PASS. This is a finite-certificate-assisted analytic
theorem, not Lean formalization or external peer review. No previously
completed package has been modified, and no localized-mode multiplicity
statement is claimed.

## 1. Exact geometric cuts and canonical retained blocks

Put b_0=0 and b_i=sum_(a<i)h_a. All indices are interpreted modulo N.
For each i retain the six vertices

    K_i=(b_i,b_i+1,b_i−4,b_i−3,b_i−2,b_i−1),

in that stated order: first the head pair of cell i, then the tail four of
cell i−1. The interior of cell i is

    I_i={b_i+2,…,b_i+h_i−5}.

These interiors and retained blocks partition the graph for every h_i≥10.
Every interior is a chain of m_i−1 four-site blocks, where m_i=2j_i.

The matrix A² has range four. Consecutive retained six-vertex intervals are
separated by at least four interior vertices; their closest vertices are
at distance h_i−5≥5. Thus there is no direct coupling between distinct
retained cores. Interiors in distinct cells have their closest vertices
at distance seven, so they do not couple to one another either.

Every interior chain couples only to K_i at its left end and to the
four-dimensional tail slot of K_(i+1) at its right end. The relevant
coefficients are independent of h_i because all cells have the same
initial and terminal local triangle-flux patterns. These facts can also be
read directly from the exact formulas

    (A²)_(u,u)=4,
    (A²)_(u,u+1)=τ_(u−1)+τ_u,
    (A²)_(u,u+2)=1,
    (A²)_(u,u+3)=τ_u+τ_(u+1),
    (A²)_(u,u+4)=τ_u τ_(u+2),

with seam factors on paths crossing the global holonomy cut. There is no
unlisted longer-range edge.

For a proposed cap t let M=tI−A². Away from the seam, the intrinsic
retained block and the chain data are

    B=[[G_0,C_0],[C_0ᵀ,D_t]],
    U_0=[R_0;W_0ᵀ],       V=[0_(4×2),E_+],

where

    D_t=[[t−4,0,−1,0],[0,t−4,0,−1],
         [−1,0,t−4,0],[0,−1,0,t−4]],
    E_+=[[-1,0,0,0],[0,1,0,0],[-1,2,1,0],[2,-1,0,-1]],
    E_−=[[-1,0,0,0],[0,1,0,0],[-1,-2,1,0],[-2,-1,0,-1]],
    G_0=(t−4)I_2,
    R_0=[[-1,-2,1,0],[-2,-1,0,-1]],
    C_0=[[-1,0,-1,0],[0,-1,0,-1]],
    W_0=[[0,0,-1,0],[0,0,0,1],[0,0,0,0],[0,0,0,0]].

The global seam initially multiplies C_0 and the lower part of U_0 in
K_0 by α. Conjugating the tail four coordinates of K_0 by α restores
the displayed B and U_0. It moves the seam sign onto the terminal
coupling of cell r−1. Hence the canonical system has terminal factors

    ω_i=1 for i<r−1,  ω_(r−1)=α.

This is an explicit diagonal conjugacy and permutation, not an assumed
canonical relabeling.

## 2. The exact block-cyclic Schur assembly

Use the length-independent open-chain sequences

    X_0=D_t,
    X_(a+1)=D_t−E_aᵀX_a⁻¹E_a,
    U_(a+1)=−U_aX_a⁻¹E_a,

where E_a=E_+ for even a and E_a=E_− for odd a. In the old notation,

    U_a=[R_a;W_aᵀ].

The last interior pivot of cell i has index

    p_i=m_i−2=2j_i−2,

which is even. Define its exact endpoint quantities

    L_i=sum_(a=0)^(p_i) U_aX_a⁻¹U_aᵀ,
    P_i=VᵀX_(p_i)⁻¹V,
    F_i=U_(p_i)X_(p_i)⁻¹V.                                  (4)

Let E_i denote the coordinate embedding of a six-vector into retained
block K_i; it is unrelated to the bulk matrices E_±. Eliminating every
interior chain gives the 6r-dimensional matrix

    S = I_r⊗B
        −sum_i E_i L_i E_iᵀ
        −sum_i E_(i+1) P_i E_(i+1)ᵀ
        −sum_i (ω_i E_i F_i E_(i+1)ᵀ
                +ω_i E_(i+1) F_iᵀ E_iᵀ).                   (5)

Indices on retained blocks are cyclic. Formula (5) is an additive formula.
When r=2, two different chains join the same two cores and their cross
blocks must both be added. When r=1, the cross terms are diagonal loop
contributions −ω_0(F_0+F_0ᵀ). No edge is discarded in either case.

To prove (5), eliminate the first block of one chain. Its current coupling
to K_i is U_a, so it subtracts U_aX_a⁻¹U_aᵀ from K_i and propagates
the coupling as −U_aX_a⁻¹E_a. Only the terminal pivot also sees the next
retained core, with coupling ω_iV. Its Schur complement subtracts the
two self-energies and the displayed cross block. Different interiors do
not couple, so their contributions add. The same calculation includes a
coincident left and right retained core by adding both couplings before
the Schur complement, which gives exactly the r=1 loop terms in (5).

The primary checker compares (5) with direct scalar elimination of the full
signed graph for cells (10,18),(18,26),(10,18,26),(10,10),(10), and (18),
each with both holonomies. All 12 exact identities pass. Thus both unequal
minimal examples, the parallel-edge case and the loop case are explicitly
covered by the implementation check.

## 3. The common limit and an error independent of the cell count

The previously proved fixed-energy Riccati estimates apply to every cell,
since the open-chain data are unchanged. At an even entrance index J,
write

    p_i=J+2s_i, s_i≥0, s=min_i s_i.

For the constants of either verified R2 package,

    ||X_a⁻¹||_2≤3 after J,
    ||R_(J+2v)||_2,||W_(J+2v)||_2≤a q^v,
    ||R_(J+2v+1)||_2,||W_(J+2v+1)||_2≤b q^v,
    ||X_(J+2v)−X_*||_2≤4r_0 θ^v,

where b=12a and θ=q². Here r_0 is a Riccati radius, not a cell count.

Let

    L_∞=sum_(a≥0) U_aX_a⁻¹U_aᵀ,
    P_∞=VᵀX_*⁻¹V,
    S_∞=B−L_∞−P_∞.

This S_∞ is exactly the previously verified six-dimensional limiting
core, because U_a=[R_a;W_aᵀ]. In particular no new positive-limit
assumption is introduced.

The stacked response satisfies

    ||U_(J+2v)||_2≤sqrt(2)a q^v,
    ||U_(J+2v+1)||_2≤sqrt(2)b q^v.

Every quadratic increment in L_∞ therefore has norm at most 6b²q^(2v)
in pair v. Counting both single-block increments per pair gives

    ||L_∞−L_i||_2 ≤ 12b²q^(2s_i)/(1−q²).                   (6)

This harmlessly includes the term at p_i although the actual suffix starts
at p_i+1. The inverse identity and ||V||_2≤sqrt(14) give

    ||P_i−P_∞||_2≤576r_0 θ^(s_i).                           (7)

Finally

    ||F_i||_2≤sqrt(2)a q^(s_i)·3sqrt(14)
             =3sqrt(28)a q^(s_i)<16a q^(s_i).                (8)

The diagonal error in (5), relative to I_r⊗S_∞, combines an outgoing
tail (6) with an incoming error (7), and is bounded by their maxima.

For the cross terms, take arbitrary retained vectors v_0,…,v_(r−1).
Their quadratic form has absolute value at most

    sum_i 2||F_i|| ||v_i|| ||v_(i+1)||
      ≤sum_i ||F_i|| (||v_i||²+||v_(i+1)||²)
      ≤2 max_i||F_i|| sum_i||v_i||².

Every core is incident to exactly two chain ends, counting multiplicity.
The displayed inequality remains valid for r=1 loops and r=2 parallel
edges. It proves a degree-two operator bound, with no factor growing in r.
Together, (6)–(8) yield

    ||S−I_r⊗S_∞||_2≤E_s,
    E_s=12b²q^(2s)/(1−q²)+576r_0θ^s+32a q^s.                (9)

This is the required length- and cell-count-uniform Schur estimate. It uses
the actual 6r-dimensional boundary matrix and does not infer any r- or 2r-
dimensional localized-mode model.

## 4. Two verified parameter choices

At t=198/25, use the original closure data

    J=24, r_0=10⁻¹⁰, q=2/3, θ=4/9,
    a=1/30000, b=1/2500,
    γ=1/50, ε=1/500.

The unphased seed has margin γ and its distance to S_∞ is below ε,
so S_∞≻(γ−ε)I_6. The new error satisfies

    E_0=501647/468750000 < ε.

If every h_i≥4(J+2)+2=106, (9) implies

    S≻(γ−2ε)I_(6r)=(2/125)I_(6r).

All interior pivots are positive by the old open-chain theorem. Schur
congruence proves (1).

At t=790537/100000, use the sharpened closure data

    J=48, r_0=10⁻¹⁸, q=3/4, θ=9/16,
    a=1/9000000000, b=1/750000000,
    γ=10⁻⁶, ε=10⁻⁸.

Here

    E_0=700000123/196875000000000000 < ε.

For every h_i≥202, the retained core is therefore

    S≻(49/50000000)I_(6r),

and Schur congruence proves (2). As always, these are boundary-core margins;
they are not claimed as the same Euclidean eigenvalue gaps for the entire
original matrix.

## 5. Completion of the full residue-four counterexample family

Choose the two cells with j_0=floor(k/2),j_1=ceil(k/2), k≥6, and
holonomy−1. When k≥26, both j_i≥13, hence both h_i≥106. The first
parameter choice proves the cap 7.92 for all those lengths.

The remaining 20 cases k=6,…,25, N=52,60,…,204, are verified directly
on their full signed graphs by sparse rational scalar LDL. Every pivot
is positive. This checks the changed odd-k construction rather than silently
reusing a certificate for the earlier balanced word.

The elementary twisted benchmark bound gives, for N≥52,

    ρ_−(N)²>8−200/N²≥8−200/52²=2679/338>198/25.

The endpoint separation is 2679/338−198/25=51/8450>0. This proves (3)
for every k≥6, a uniform analytic R4 witness family with 20 finite bases.

The sharper cap cannot be substituted throughout that finite range. The
new construction at N=60 uses cells (26,34). At cap 790537/100000 its
exact LDL has positive predecessors and a strictly negative next pivot.
The same obstruction occurs at cells (34,42), N=76. These are direct
falsifications of an overstrong sharp-cap extension, and explain why (3)
uses the already established 7.92 cap with a strict benchmark comparison.

## Verification and dependence boundary

Run `python verify_unequal_cells.py` with its sibling `assembly.py`.
Both are newly authored standard-library Python. The current output contains
22 passing required checks, 12 exact graph-to-assembly identities, 20 complete
finite R4 bases, both rational error estimates and the strict sharp-cap
obstruction at the changed N=60 construction. The exact certificate and
actual stdout are unequal_cells_certificate.json and verification_output.json.

The fixed-energy Riccati/response premises and seed margins are reused from
the frozen ../analytic/ and ../strengthening/ proof packages. This new
verifier checks the new assembly, arithmetic and finite graph statements;
it does not claim to re-prove those upstream analytic premises by sampling.

The proof requires legal cells h_i≡2 modulo 8 with the displayed words. It
does not apply to arbitrary gap arrangements or to arbitrary signings.
Nevertheless their lengths need not be equal or nearly equal, and r is
unrestricted. The historical G6 physical edge, IMS estimate and withdrawn
rank-r claim are not dependencies.

Independent review of the new all-r assembly and finite bases has passed 119
exact checks and a complete line audit. It includes 48 full graph/template
and isolated-chain/core comparisons, a different scalar LDL ordering for
all 20 R4 bases, and the two changed-construction sharp-cap obstructions.
See audit/INDEPENDENT_UNEQUAL_CELL_AUDIT.md and its separate exact replay.

The next residue-six issue would be to choose
three legal cell lengths with the desired total and verify the remaining
finite range; no R6 theorem is asserted here.
