# Phase-uniform Schur closure and an equally spaced R4 family

Date: 2026-10-05. Research scope: the original signed cycle-square problem.

## Result and verification status

The argument below extends the verified one-G6 boundary estimate to every
unit complex phase and then assembles any number of identical cells by a
finite unitary Fourier decomposition. It uses the full operators, without
an assumption about the number of localized interface modes.

The mathematical derivation, all stated primary exact checks, and the
independent mathematical audit are complete. **Both exact verification and
independent audit PASS.** This is a finite-certificate-assisted analytic
theorem, not a proof-assistant formalization or external peer review. The
preceding R2 packages remain unchanged.

Put

    t = 790537/100000 = 7.90537,
    w_j = (1,1,−1,1,−1,−1,1,−1)^j || (1,−1),
    h = 8j+2.

For the real signed cycle square on N=rh vertices, repeat the length-two
triangle-flux word w_j exactly r times and choose Hamilton-cycle holonomy
α∈{−1,+1}. More explicitly, put a_i=1 except a_(N−1)=α, and assign
edge signs

    sign{i,i+1}=a_i,
    sign{i,i+2}=τ_i a_i a_(i+1),    τ=w_j^r.

All indices are cyclic. There are exactly r equally spaced gaps of length
six between positive quadrilateral fluxes; every other gap has length four.

**Phase-uniform assembly theorem.** If j≥25, then for every r≥1 and
either holonomy,

    ρ(A_(rh,α))² < t.                                         (1)

The cap and the lower threshold on the cell length do not depend on r.
This is an equally spaced repeated-cell theorem. It is not a theorem for
arbitrary positions or types of r defects.

**R4 consequence.** For every j≥1, the balanced two-G6 signing on
N=16j+4 with holonomy−1 satisfies

    ρ(A_N)² < t.                                               (2)

For j≥3, hence N≥52, it follows that

    ρ(A_N)² < t < ρ_−(N)².

This is the even-k line of the inherited residue-four family N=8k+4,
namely k=2j. The odd-k line is not included. An exact negative-pivot
certificate at N=60 shows that the sharp cap t actually fails for that
balanced odd-k signing, so removing the parity restriction would be false.

The weaker cap 198/25 also admits the same phase-uniform assembly argument
once h≥106, using the earlier R2 certificate. No new decimal optimization
is involved; the new content is uniformity in phase and assembly of cells.

## 1. The Hermitian phased cell

Let τ=w_j, periodically extended to all integer indices. For |z|=1,
consider sequences satisfying f_(i+h)=z f_i. The operator

    (A_h(z)f)_i = f_(i+1)+f_(i−1)
                  +τ_i f_(i+2)+τ_(i−2) f_(i−2)

induces an h-by-h Hermitian matrix on indices 0,…,h−1. Every time an edge
crosses the right boundary it contributes a factor z; crossing the left
boundary contributes z⁻¹=conjugate(z). For z=1 this is the previously
verified one-G6 matrix.

For h≥18 partition the indices into V_0={0,1} and m=2j four-site blocks
V_1,…,V_m, with V_s={2+4(s−1),…,5+4(s−1)}. The diagonal and ordinary
nearest-block matrices of M_h(z)=tI−A_h(z)² are the same D_t,E_± as in
the verified R2 proof:

    D_t=[[t−4,0,−1,0],[0,t−4,0,−1],
         [−1,0,t−4,0],[0,−1,0,t−4]],
    E_+=[[-1,0,0,0],[0,1,0,0],[-1,2,1,0],[2,-1,0,-1]],
    E_−=[[-1,0,0,0],[0,1,0,0],[-1,-2,1,0],[-2,-1,0,-1]].

The unphased boundary data are

    G_0=(t−4)I_2, H_0=D_t,
    R_0=[[-1,-2,1,0],[-2,-1,0,-1]],
    C_0=[[-1,0,-1,0],[0,-1,0,-1]],
    W_0=[[0,0,-1,0],[0,0,0,1],[0,0,0,0],[0,0,0,0]].

Here C_0 couples V_0 to V_m and W_0 couples V_1 to V_m. With phase z,

    C_0(z)=conjugate(z) C_0,
    W_0(z)=conjugate(z) W_0,                                  (3)

and every other initial block is unchanged. Indeed every two-step path in
A² represented by these wrap blocks crosses the cell boundary once in the
negative direction. Ordinary bulk paths do not cross it. Because h>8, no
two-step path winds twice or collides with a distinct cyclic-distance term.

Substituting τ in the local A² entry formulas proves (3) at all lengths
h≥18. The new exact verifier additionally constructs the entire phased
normalized matrix as a rational Laurent polynomial in z and compares every block at
h=18,26,34,106,202. This tests the implementation and phase orientation;
the path argument proves the general identity.

## 2. A common limiting core for every phase

Use zero-based elimination index p, with X_0=D_t and alternating E_p.
All inverses below are Hermitian positive inverses. The recurrence is the
usual block Schur recurrence, replacing transpose by conjugate transpose
where necessary.

Induction from (3) gives, before the terminal elimination,

    X_p(z)=X_p,   R_p(z)=R_p,
    G_p(z)=G_p,   H_p(z)=H_p,
    W_p(z)=conjugate(z) W_p,
    C_p(z)=conjugate(z) C_p.                                  (4)

For example, W_p(z)* X_p⁻¹ W_p(z)=W_pᵀX_p⁻¹W_p because |z|=1,
while the mixed correction R_pX_p⁻¹W_p(z) carries the same conjugate(z)
as C_p(z). Thus no numerical phase sampling is being used.

The terminal index is p=m−2, always even. Its physical nearest-block
coupling remains E=E_+, so the last response is

    W_p(z)+E=conjugate(z)W_p+E.

Write

    g_p=G_p−R_pX_p⁻¹R_pᵀ,
    c_p=C_p−R_pX_p⁻¹W_p,
    h_p=H_p−W_pᵀX_p⁻¹W_p−EᵀX_p⁻¹E,
    u_p=R_pX_p⁻¹E,
    v_p=W_pᵀX_p⁻¹E.

The exact six-dimensional phased core is therefore

    S_m(z) = [ g_p, conjugate(z)c_p−u_p;
               transpose-conjugate,
               h_p−z v_p−conjugate(z)v_pᵀ ].                 (5)

Conjugate by the unitary U_z=diag(I_2,zI_4). Then

    U_z* S_m(z) U_z
      = [ g_p, c_p−z u_p;
          transpose-conjugate,
          h_p−z v_p−conjugate(z)v_pᵀ ].                      (6)

Define S_∞ using the actual infinite unphased Schur trajectory, including
the fixed terminal correction EᵀX_*⁻¹E, exactly as in the verified R2
proof. The phase disappears from the limit in (6), because u_p,v_p tend
to zero. Thus the same S_∞ serves all |z|=1 after unitary conjugation.

More importantly, every estimate is uniform before taking the limit.
Multiplication by z does not change ||u_p|| or ||v_p||. Consequently the
already proved all-term tail bound applies without changing any constant:

    ||U_z* S_m(z) U_z−S_∞||_2
      ≤ 24b² q^(2s)/(1−q²)+48a q^s+576r_0 θ^s,              (7)

where p=48+2s and

    r_0=10⁻¹⁸, q=3/4, θ=9/16,
    a=1/9000000000, b=12a.

The notation r_0 here denotes the Riccati radius, not the number of cells.
The right side is at most

    583333407/109375000000000000 < 10⁻⁸.

These are the identical constants already independently verified in the
strengthened R2 certificate. All bulk pivots are also unchanged by z.

The unphased seed at cell order 202, block count50, satisfies
S_50(1)≻10⁻⁶I_6. Comparing it to S_∞ and then to (6) costs two errors,
giving for every even m≥50 and every |z|=1,

    U_z* S_m(z) U_z ≻ (49/50000000)I_6.

Schur congruence now proves

    tI_h−A_h(z)²≻0          for h=8j+2≥202, |z|=1.           (8)

This phase extension requires no new limiting-core certificate. It reuses
the exact positive seed because the limit in (6) is genuinely phase-free.

## 3. Exact assembly of any number of cells

Fix an integer r≥1 and α∈{−1,+1}, and let N=rh. The full signed
operator defined above is the same periodic difference operator with
boundary condition f_(i+N)=α f_i.

For every root z of z^r=α, define F_z:C^h→C^N by

    (F_z v)_(ch+s)=r^(−1/2) z^c v_s,
    0≤c<r, 0≤s<h.

The r values of z are distinct and have modulus one. The finite geometric
sum proves that the ranges of F_z are pairwise orthogonal, and together
they span C^N. Direct substitution in the difference operator gives

    A_(N,α) F_z = F_z A_h(z).                                (9)

At the global seam, the equality uses exactly z^r=α. This proves the
unitary direct-sum identity

    A_(N,α) ≅ direct_sum_(z^r=α) A_h(z).

Equation (8) bounds every fiber, proving (1). This is a full spectral
decomposition. It makes no claim of r squared edge modes and is unaffected
by the historical correction from r to 2r localized squared modes.

## 4. The balanced R4 application and exact finite completion

Take r=2 and α=−1. The two fibers have z=i and z=−i. The repeated-cell
word has N=2h=16j+4 and exactly two G6 gaps, separated by h=N/2 sites.
Its cyclic gap word is a rotation of

    [6,4^(2j−1),6,4^(2j−1)].

This is precisely the inherited balanced residue-four construction with
k=2j. The global sign convention agrees with the inherited choice α=−1.

For j≥25, (2) follows from (1). The remaining 24 cases j=1,…,24 are
verified directly on the full real signed graphs at

    N=20,36,52,…,388.

The exact verifier builds each adjacency by its edge signs, forms the
integer matrix 790537I−100000A², and performs sparse rational scalar LDL
in an interior-first ordering. Every pivot is positive. It saves the order,
pivot count and a pivot-list digest for every case. No floating spectrum
or unclosed solver gap enters these checks.

As an additional structural test, the verifier checks (9) at r=2,z=±i
for h=10,18,26,34 using exact Gaussian-integer arithmetic. These checks
also cover the smallest R4 member N=20, whose h=10 fiber has overlapping
ordinary and wrap block locations. No inappropriate disjoint-block formula
is used for that finite base.

Finally t<198/25 and the established benchmark estimate
ρ_−(N)²>8−200/N²≥198/25 for N≥50 prove the strict comparison for
N≥52 in this residue class.

## 5. Exact obstruction to the overbroad odd-k statement

The balanced family at k=7,N=60 has gap word

    [6,4^6,6,4^6]

and holonomy−1. Its half-length is 30, not a cell of the form 8j+2 with a
periodic τ=w_j. Thus the preceding Fourier assembly does not apply.

Direct rational LDL of 790537I−100000A_60² produces 58 positive
predecessor pivots followed by a strictly negative pivot. The exact pivot
and its complete positive prefix are stored in r4_pilot_certificate.json.
By Schur congruence this proves

    ρ(A_60)² > 7.90537.

Therefore the cap in (2) cannot be asserted for the whole balanced
N=8k+4 family by deleting the even-k hypothesis. This does not refute a
weaker cap, the inherited computer-assisted classification, or the goal of
an analytic odd-k residue-four theorem.

## Files, checks, and remaining work

verify_r4_pilot.py is new self-contained Python-standard-library code.
Its current run passes 20 exact checks: Laurent-polynomial block identities,
Gaussian-integer fiber embeddings, direct-graph identification with the
balanced even-k word, complete 24-case finite coverage, and the strict odd-k
obstruction. r4_pilot_certificate.json and verification_output.json contain
the generated certificate and actual execution output.

The complete proof chain uses the frozen strengthened R2 proof and exact
certificate in ../strengthening/, rather than any historical G6 physical
edge or IMS estimate. The older 2r correction remains in force.

An independent audit has verified the new phase argument, full spectral
assembly, and finite base certificates. Its 72 exact checks include symbolic
Laurent scalar elimination, quotient-ring embeddings for r=1,…,5 with both
holonomies, and a different full-graph scalar LDL ordering for all 24 bases
and the N=60 obstruction. See audit/INDEPENDENT_R4_PHASE_AUDIT.md and the
separate replay code and output in that directory.

The next mathematical boundary is the odd-k R4 line, where the half-cell coefficient
word changes sign rather than being periodic. It requires a different
gluing statement or a larger fixed core; it is not included in this result.

Construction provenance:
[residue_gap_word at 44ff33a](https://github.com/whzy3185/math/blob/44ff33a89294056907d0b909d68a8db27371c4f0/research/scripts/target_a_task53_global.py),
[finite-tail holonomy convention](https://github.com/whzy3185/math/blob/44ff33a89294056907d0b909d68a8db27371c4f0/research/proofs/task54/TARGET_A_FINITE_STRUCTURED_COUNTEREXAMPLE_TAIL.md).
