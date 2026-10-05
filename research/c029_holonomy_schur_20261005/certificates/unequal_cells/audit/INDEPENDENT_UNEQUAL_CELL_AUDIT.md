# Independent audit of unequal-cell Schur assembly

Date: 2026-10-05. Mathematical line audit and independent exact replay: **PASS**.

## Audited conclusions

Let t=(1,1,-1,1,-1,-1,1,-1), and concatenate any positive number r of legal triangle-flux cells w_j=t^j||(1,-1), each of length h=8j+2 with j>=1. Give the signed cycle square either Hamilton holonomy.

The audited argument establishes:

- If every cell length is at least 106, the squared adjacency spectral radius is strictly below 198/25
- If every cell length is at least 202, it is strictly below 790537/100000
- The constants are independent of r, and cell lengths need not be equal

For every k>=6, the negative-holonomy construction with two cells of lengths 8 floor(k/2)+2 and 8 ceil(k/2)+2 gives a signing on n=8k+4 with

    rho(A_n)^2 < 198/25 < rho_tw(n)^2.

For odd k this is a changed, unequal two-cell construction. Its two separations are n/2-4 and n/2+4. The sharper cap 790537/100000 does not hold for all these small graphs: independent exact negative pivots confirm failure at n=60 and n=76.

The proof covers only the specified legal cell words and their concatenations. It is not a theorem for arbitrary defect arrangements or arbitrary signings. It does not determine unrestricted minima, assert a residue-six theorem, or assume a localized-mode multiplicity. No Lean formalization is claimed.

## Dependencies

The fixed-energy Riccati contraction, dual response bounds, positive pivots and normalized six-dimensional seeds are reused from the already audited analytic and strengthening packages. This audit does not treat finite sampling as a replacement for those uniform analytic results.

The new proof reviewed is ../UNEQUAL_CELL_SCHUR_THEOREM.md. The audit independently checks its geometric template, boundary assembly, cell-count-uniform error, all twenty new finite bases, and the sharper-cap obstructions.

## Graph support, retained vertices and seam gauge

With cell starts b_i, retain

    K_i=(b_i,b_i+1,b_i-4,b_i-3,b_i-2,b_i-1)

and eliminate I_i={b_i+2,...,b_i+h_i-5}. The K_i and I_i form a disjoint partition for all legal h_i>=10. Distinct interiors are separated by seven vertices in cyclic distance, and consecutive retained intervals have nearest separation h_i-5>=5. Since A^2 has range four, there are no missing interior-interior or direct retained-retained couplings.

Each cell has the same local beginning and ending triangle word. Direct enumeration of two-edge walks therefore yields the displayed B,D,E_+,E_-,U_0,V blocks at every legal length. Every cell has exactly one quadrilateral-flux gap of length six; all other gaps have length four.

The three sign changes at the global seam are those required to preserve the specified triangle word. Multiplying the tail four coordinates of K_0 by alpha cancels the seam signs in its intrinsic block B and initial coupling U_0. The sole remaining phase is the terminal coupling alpha V of the last chain. This is a literal diagonal sign conjugation; it is not an assumed graph equivalence.

The separate implementation verifies the entire pre-elimination matrix against this block template, rather than checking only reduced determinants or eigenvalues.

## Additive Schur formula and small cell counts

The current left response is U_a=[R_a;W_a^T], and the right coupling is V=[0,E_+]. A chain ending at the even index p_i=2j_i-2 contributes

    L_i=sum_(a=0)^(p_i) U_a X_a^-1 U_a^T,
    P_i=V^T X_(p_i)^-1 V,
    F_i=U_(p_i) X_(p_i)^-1 V.

After eliminating the independent interior chains, the retained matrix has intrinsic diagonal blocks B, subtracts L_i at K_i and P_i at K_(i+1), and subtracts the signed cross block omega_i F_i plus its transpose.

These contributions must be added, not assigned to a single block position. With two cells, the two chains connect the same pair of retained cores and both terms remain. With one cell, left and right endpoints coincide and the correction includes -omega(F+F^T) on the diagonal. Expanding the single terminal Schur form with its combined coupling proves exactly this loop formula.

The independent exact implementation uses a different assembly method from the primary four-by-four recurrence: it constructs each isolated chain with two distinct six-dimensional endpoints, eliminates the chain by scalar Schur steps, then embeds and adds all four endpoint blocks. For r=1 the two endpoint copies map into the same coordinates; for r=2 both chains map into the same pair of coordinates. Its sum agrees exactly with direct elimination of the full signed graph.

## Limiting core and the uniform degree-two estimate

Define

    L_inf=sum_(a>=0) U_a X_a^-1 U_a^T,
    P_inf=V^T X_*^-1 V.

Then B-L_inf-P_inf equals the previously certified S_inf entry by entry. In particular, its upper-right block is C_0-sum R_a X_a^-1 W_a. The series use the actual trajectory, so no inverse-pivot replacement inside them creates an omitted error.

Let p_i=J+2s_i and s=min s_i. The verified separate response estimates imply

    ||U_(J+2v)|| <= sqrt(2)a q^v,
    ||U_(J+2v+1)|| <= sqrt(2)b q^v.

Thus each quadratic increment is at most 6b^2 q^(2v). Counting both members of each pair gives

    ||L_inf-L_i|| <= 12b^2 q^(2s_i)/(1-q^2).

The inverse identity gives

    ||P_i-P_inf|| <= 576 r_0 theta^(s_i).

This is conservative: ||V||^2<=14 and the inverse bounds already yield a smaller constant. The stated 576 is valid.

For the cross block,

    ||F_i|| <= sqrt(2)a q^(s_i) * 3 sqrt(14)
              =3 sqrt(28)a q^(s_i) <16a q^(s_i).

For arbitrary retained vectors v_i, the total cross-term quadratic form is bounded by

    sum_i 2||F_i|| ||v_i|| ||v_(i+1)||
      <=sum_i ||F_i|| (||v_i||^2+||v_(i+1)||^2)
      <=2 max_i||F_i|| sum_i||v_i||^2.

Each core has two chain-end incidences, counting loops twice and parallel edges separately. The last inequality is consequently valid for every r>=1. No error grows with r.

Combining the diagonal and cross bounds gives the claimed estimate

    ||S-I_r tensor S_inf|| <= E_s,
    E_s=12b^2 q^(2s)/(1-q^2)+576r_0 theta^s+32a q^s.

No boundary term, parallel contribution or multiplicity factor is omitted.

## Constants and transfer from the finite seeds

At cap 198/25, the inherited constants are J=24, r_0=10^-10, q=2/3, theta=4/9, a=1/30000, b=1/2500, gamma=1/50 and epsilon=1/500. Exact arithmetic gives

    E_0=501647/468750000 <1/500.

The previously checked unphased seed is gamma-positive and lies within epsilon of S_inf. The new retained matrix is within epsilon of the direct sum of S_inf. Both errors are included, giving the core margin gamma-2epsilon=2/125.

At cap 790537/100000, the corresponding constants are J=48, r_0=10^-18, q=3/4, theta=9/16, a=1/9000000000, b=1/750000000, gamma=10^-6 and epsilon=10^-8. Exact arithmetic gives

    E_0=700000123/196875000000000000 <10^-8,

and the two-error core margin is 49/50000000.

The condition p_i>=J is equivalent to h_i>=4(J+2)+2, namely 106 or 202. All eliminated pivots are positive by the inherited open-chain result. Schur congruence therefore proves positivity of cap I-A^2. The reduced-core margins are not asserted to be Euclidean eigenvalue lower bounds for the full original matrix.

## Full residue-four coverage and its limits

For k>=26, both selected j_i are at least thirteen, so both cells have length at least 106 and the first uniform theorem applies. The remaining k=6,...,25 correspond exactly to n=52,60,...,204. A separate natural-vertex-order rational LDL verifies every one of these twenty full signed graphs. The first analytic order is n=212, with no missing admissible order.

For n>=52,

    rho_tw(n)^2 > 8-200/n^2 >= 2679/338 >198/25,

where the last gap is exactly 51/8450. This verifies the claimed strict benchmark separation throughout the stated range.

The new odd-k graph at n=60 uses cells (26,34), and at n=76 uses (34,42). Independent exact LDL at cap 790537/100000 produces positive predecessors and a strictly negative pivot in each case. A negative quadratic direction, not merely failure of a numerical positive-definiteness routine, proves the sharp cap is false there. The complete rational pivot prefixes are stored in the audit output.

## Independent finite evidence

The standalone script independent_assembly.py imports no primary verifier or earlier audit code. It performs:

- Entire graph-versus-canonical-template comparisons for twelve cell configurations at both caps and both holonomies
- Independent direct full-graph scalar Schur elimination versus the sum of isolated-chain scalar Schur responses in all 48 cases
- Cases with one cell, two cells, three genuinely unequal cells and four genuinely unequal cells, including threshold-scale lengths
- Natural-order exact LDL for all twenty new residue-four bases
- Strict negative-pivot certificates for the changed n=60 and n=76 graphs at the sharper cap
- Exact rational checks of both error constants, positive seed-transfer margins, threshold conversion and benchmark comparison
- Direct quadrilateral-flux gap counts for every tested configuration

The two matrix comparisons yield 96 exact equalities. With the remaining checks, the final run passes 119 checks. The finite tests check the implementation; the local template argument, Schur identity and quadratic-form estimate prove the unbounded length and cell-count assertions.

## Reproduction

Run with Python 3:

    python independent_assembly.py

Only the standard library is required. Results are in independent_replay.json and verification_stdout.txt. The exact upstream assumptions remain in the frozen analytic and strengthening packages. Source hashes and artifact checksums accompany this report.

No blocking mathematical correction was required. The distinction between the changed odd-k construction, the uniform long-cell sharp cap, and the full finite-range 7.92 cap is essential and is preserved in the reviewed proof.
