# A sharper uniform bound for every one-G6 cycle square

Date: 2026-10-05. Scope: the explicit residue-two family from August Target A.

## The strengthened theorem

For each integer k≥1 let n=8k+2. Give every length-one edge of C_n(1,2)
sign +1, and give its length-two edges the signs

    τ = (1,1,−1,1,−1,−1,1,−1)^k || (1,−1).

Write A_n for this signed adjacency matrix. Then

    ρ(A_n)² < 790537/100000 = 7.90537       for every k≥1.       (1)

For the particular member n=202,

    ρ(A_202)² > 7905369/1000000 = 7.905369.                    (2)

Consequently the least uniform upper bound for this prescribed family lies
in the interval

    7.905369 < sup_(k≥1) ρ(A_(8k+2))² ≤ 7.90537.              (3)

Its width is 10⁻⁶. The right endpoint in (3) is non-strict: individual strict
inequalities alone do not prove a strict inequality for their supremum.

This strengthens the previous cap 198/25=7.92 and extends its range from
k≥6 to all k≥1. The counterexample comparison with the twisted signing
still follows only in the established range k≥6, since

    7.90537 < 7.92 < ρ_−(8k+2)²               for k≥6.

No assertion is made about the global minimum over all signings, its
minimizers, the existence of a limit as k→∞, monotonicity in k, or the exact
value of the supremum in (3). No two- or three-interface theorem is claimed.

Evidence level: **Proved, finite-certificate-assisted analytic theorem**,
with an independent exact replay and analytic audit. The infinite-length argument
below is analytic; all its rational premises have a fresh exact verifier.
There is no Lean formalization of this strengthened R2 theorem.

## Why the old certificate could not simply be reused

The preliminary small-order spectrum calculation was used only to falsify
candidate bounds. It suggested that the cap holds already at n=10,18,26,34,42.
Exact tests then showed that after lowering the cap to 7.91, the old
two-cell inequalities with factor 2/5 and the residual bound at elimination
index 24 both fail. These failed inequalities are preliminary falsification checks, not premises of the strengthened theorem.

Moving the entrance to index 48 and using center inequalities with factor
1/2 instead gives a valid certificate at the smaller cap 7.90537. Thus the
new result does not extrapolate the previous fixed-energy calculation.
The existing metric matrices P,Q happen to remain suitable; every relevant
inequality was checked again at the new rational center.

## 1. The exact one-parameter block system

For a rational t put M_n(t)=tI_n−A_n². For n≥18 partition the vertices into
V_0={0,1} and m=2k consecutive four-site blocks

    V_j={2+4(j−1),…,5+4(j−1)},   1≤j≤m.

Use the constant matrices

    D_t = [[t−4,0,−1,0],[0,t−4,0,−1],
           [−1,0,t−4,0],[0,−1,0,t−4]],
    E_+ = [[−1,0,0,0],[0,1,0,0],[−1,2,1,0],[2,−1,0,−1]],
    E_− = [[−1,0,0,0],[0,1,0,0],[−1,−2,1,0],[−2,−1,0,−1]],
    G_0=(t−4)I_2,   H_0=D_t,
    R_0=[[-1,-2,1,0],[-2,-1,0,-1]],
    C_0=[[-1,0,-1,0],[0,-1,0,-1]],
    W_0=[[0,0,-1,0],[0,0,0,1],[0,0,0,0],[0,0,0,0]].

The block identity is exactly the one established in
../analytic/R2_ANALYTIC_TAIL_CLOSURE.md, with 98/25 replaced by t−4.
It is valid for every n≥18 by the displayed local A² entry formulas there.
At n=10, the first and last four-site blocks are adjacent, so their
exceptional wrap coupling coincides with the ordinary nearest-block
coupling. We avoid any implicit double counting by checking that full
ten-by-ten matrix directly.

Set X_0=D_t and E_j=E_+ for even j and E_j=E_− for odd j. The open
recurrence is

    X_(j+1)=D_t−E_jᵀX_j⁻¹E_j,
    R_(j+1)=−R_jX_j⁻¹E_j,
    W_(j+1)=−E_jᵀX_j⁻¹W_j,
    G_(j+1)=G_j−R_jX_j⁻¹R_jᵀ,
    H_(j+1)=H_j−W_jᵀX_j⁻¹W_j,
    C_(j+1)=C_j−R_jX_j⁻¹W_j.

For even m the terminal elimination is p=m−2, always even. At that step
replace W_p by W_p+E_+. The retained normalized six-by-six core is

    S_m(t) = [ G_p−R_pX_p⁻¹R_pᵀ,
               C_p−R_pX_p⁻¹(W_p+E_+);
               transpose,
               H_p−(W_p+E_+)ᵀX_p⁻¹(W_p+E_+) ].

Schur congruence proves M_n(t)≻0 if and only if all its eliminated bulk
pivots and S_m(t) are positive. As before, m counts blocks, not vertices.

## 2. Fresh finite data at the improved cap

Fix

    t=790537/100000,  J=48,  r=10⁻¹⁸,  η=10⁻²⁰,
    q=3/4,  θ=q²=9/16,
    a=1/9000000000,  b=12a,  ε=10⁻⁸,  γ=10⁻⁶.

Put F_±(X)=D_t−E_±ᵀX⁻¹E_±, Φ=F_−∘F_+, B=Φ²⁴(D_t)=X_48,
Y=F_+(B) and L_B=B⁻¹E_+Y⁻¹E_−. The unchanged rational weights are

    P=(1/10000)[[10766,87,19,974],[87,12664,148,−2418],
               [19,148,10093,−25],[974,−2418,−25,14009]],
    Q=(1/10000)[[11503,614,990,−1101],[614,10470,15,113],
               [990,15,12299,−2632],[−1101,113,−2632,13260]].

The new verifier establishes, using only rational arithmetic:

1. X_0,…,X_48 are positive and B,Y≻I_4/2
2. (9/10)I_4≺P,Q≺2I_4
3. L_BᵀPL_B≺P/2 and L_BQL_Bᵀ≺Q/2
4. ||Φ(B)−B||_F<r/40
5. R_48QR_48ᵀ≺ηI_2 and W_48ᵀQW_48≺ηI_4
6. S_50(t)−γI_6≻0, the seed at graph order 202
7. M_10(t)≻0 directly, and S_m(t)≻0 for m=4,6,…,48

Thus item 7 covers exactly the 24 graph orders 10,18,…,194. No untested
small case or exceptional block overlap is hidden in the recurrence.

The script stores the exact center, both entrance responses, the exact seed
core and all six positive seed LDL pivots in uniform_cap_certificate.json.
Its separate lower-cap calculation is described below.

## 3. The uniform analytic continuation

Use |H|_P=||P⁻¹ᐟ²HP⁻¹ᐟ²||_2 on symmetric matrices. On

    K={X=Xᵀ: |X−B|_P≤r},

we have ||X−B||_2≤2r=e. The exact lower bounds B,Y≻I/2 and
||E_±||_F²=14 give, exactly as in the first proof,

    ||X⁻¹||_2, ||F_+(X)⁻¹||_2≤3,
    ||X⁻¹−B⁻¹||_2≤6e,
    ||F_+(X)−Y||_2≤84e<1/6,
    ||F_+(X)⁻¹−Y⁻¹||_2≤504e,
    ||L(X)−L_B||_2≤14364e.

Both weighted transfer norms cost less than 3/2 in this last conversion, so
their variation is less than 43092r<10⁻⁴. Since

    sqrt(1/2)+10⁻⁴<3/4,

we obtain throughout K

    L(X)ᵀPL(X)≺q²P,    L(X)QL(X)ᵀ≺q²Q.

The identity DΦ_X[H]=L(X)ᵀHL(X) therefore proves θ=9/16 contraction
in |·|_P. The ball is invariant because the center residual is below r/36
in that norm and

    1/36+9/16=85/144<1.

There is a fixed point X_*∈K. For h≥0 the actual orbit satisfies

    ||X_(48+2h)−X_*||_2≤4r θ^h.

All later even and odd pivots are ≻I/3. Together with item 1, this proves
positivity of every bulk pivot for all lengths.

The dual Q inequality controls both responses in their correct
orientations. Since a²>(10/9)η, item 5 gives

    ||R_(48+2h)||_2, ||W_(48+2h)||_2<a q^h.

An intermediate single-block transfer has norm below 12, so either member
of that pair is bounded by b q^h.

Define the limiting Schur series using the actual infinite pivot trajectory,
and subtract E_+ᵀX_*⁻¹E_+ from the terminal H block, as in the first
proof. All series converge absolutely. The same explicit term-by-term
estimate, now with the new constants, gives for even m≥50 and
p=m−2=48+2h,

    ||S_m(t)−S_∞(t)||_2 ≤ B_h,
    B_h = 24b² q^(2h)/(1−q²) + 48a q^h + 576r θ^h.         (4)

The first term counts both single-block increments per pair in the G,H,C
tails. The second includes the terminal R_pX_p⁻¹E_+ correction in C
and both W_p/E_+ cross terms in H. The last bounds
E_+ᵀ(X_p⁻¹−X_*⁻¹)E_+. No inverse-pivot replacement is made within
the Schur sums.

All terms decrease, and exact rational arithmetic gives

    B_0=583333407/109375000000000000 < 10⁻⁸=ε.

Applying this estimate to S_m and the seed S_50 costs two errors:

    S_m(t) ≻ (γ−2ε)I_6 = (49/50000000)I_6,   m≥50 even.

Item 7 handles every shorter admissible length. The Schur criterion proves
(1). The positive core margin is not asserted to be the same Euclidean
eigenvalue gap for the entire n-by-n matrix.

## 4. A finite lower obstruction and the supremum bracket

Set t_−=7905369/1000000 and use the same explicit graph at n=202. The
verifier repeats the rational bulk elimination at t_−. All 49 four-by-four
bulk pivots remain positive. In the resulting six-by-six core, scalar LDL
has positive pivots until its first nonpositive pivot, which is strictly
negative. The exact rational pivot and its positive prefix are recorded in
uniform_cap_certificate.json. A decimal approximation is not used in the
acceptance test.

By Schur congruence, t_−I−A_202² has a vector of strictly negative
quadratic form. Hence λ_max(A_202²)>t_−, proving (2). Combining this
single finite obstruction with the uniform theorem gives (3).

This proves neither monotone convergence nor an exact physical-interface
edge equation. It also does not use the older certified G6 edge or its
multiplicity, and does not revive any of the withdrawn r-mode assertions.

## Reproduction and audit boundaries

Run:

    python verify_uniform_cap.py

The script is self-contained and uses only Python's standard library. Its
current run passes 79 required rational checks and all 25 recorded orders
(24 bases and the seed). The exact certificate and actual stdout are
uniform_cap_certificate.json and uniform_cap_output.json. An independent
direct-graph audit is recorded separately; this is not external peer review.

The preceding validated R2 files under ../analytic/ remain unchanged.
The proof reuses their established block identity and exact response
formula, while supplying and checking new fixed-energy premises. The
complete manuscript can include both proofs or replace the weaker cap
theorem while retaining its correction history.

Inherited multi-interface scope was checked against
[ANALYTIC_GAP_AUDIT_CURRENT.md at 44ff33a](https://github.com/whzy3185/math/blob/44ff33a89294056907d0b909d68a8db27371c4f0/research/proof_closure/ANALYTIC_GAP_AUDIT_CURRENT.md).
That source leaves residues 4,6 at new fixed-core obligations with caps
2679/338 and 5782/729. This bounded round selected the uniform-cap
strengthening instead; neither of those gaps is declared closed.
