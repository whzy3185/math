# Independent audit of phase-uniform assembly and balanced R4

Date: 2026-10-05. Mathematical line audit and independent exact replay: **PASS**.

## Audited conclusions and limits

Let c=790537/100000 and w_j=(1,1,-1,1,-1,-1,1,-1)^j||(1,-1), of length h=8j+2.

1. For every j>=25, every positive integer r, and either Hamilton-cycle holonomy alpha=+1 or -1, the signed cycle square with triangle word w_j repeated r times satisfies rho(A)^2<c.
2. For the balanced two-G6 signing with negative Hamilton holonomy on n=16j+4, the same strict cap holds for every j>=1. For j>=3, n>=52, this is strictly below the twisted benchmark.
3. The balanced odd-k family is excluded. At n=8k+4=60 with k=7, exact rational elimination proves rho(A)^2>c. Dropping the even-k restriction would be false.

The assembly theorem requires identical equally spaced cells. It does not cover arbitrary defect placement, arbitrary types of interfaces, all residue-four orders, or global minimization over signings. No localized-mode count is assumed, including the erroneous older r count. This is an exact-certificate-assisted analytic result, not a Lean formalization or external peer review.

The sharpened one-G6 premises are a dependency already independently audited in ../strengthening/audit/INDEPENDENT_STRONGER_CAP_AUDIT.md (path relative to the containing r4_pilot directory). This audit checks the new phase and assembly argument and separately replays all its new finite bases. It does not infer phase uniformity merely from the unphased spectral theorem.

## Phase law and finite terminal corrections

Use the quasiperiodic condition u_(i+h)=z u_i, |z|=1. In M_h(z)=cI-A_h(z)^2, the exceptional initial blocks are C_0(z)=z^-1 C_0 and W_0(z)=z^-1 W_0. The remaining blocks are the real unphased ones. For h>=18, the local walk expansion is valid with disjoint block locations and no cyclic-distance collisions.

Before terminal elimination, the Hermitian Schur recurrence gives exactly

    X_p(z)=X_p, R_p(z)=R_p, G_p(z)=G_p, H_p(z)=H_p,
    C_p(z)=z^-1 C_p, W_p(z)=z^-1 W_p.

The invariance of H uses conjugate transpose and |z|=1. It would not follow from an ordinary-transpose recurrence with complex W.

At p=m-2, m=2j, the physical terminal coupling is E=E_+, so it is E+z^-1 W_p, not z^-1(E+W_p). Define

    g=G_p-R_p X_p^-1 R_p^T,
    c_p=C_p-R_p X_p^-1 W_p,
    h_p=H_p-W_p^T X_p^-1 W_p-E^T X_p^-1 E,
    u=R_p X_p^-1 E,
    v=W_p^T X_p^-1 E.

Then the exact retained core is

    S_m(z) = [[g, z^-1 c_p-u],
              [conjugate transpose, h_p-z v-z^-1 v^T]].

For U_z=diag(I_2,z I_4), the correct unitary congruence is

    U_z^* S_m(z) U_z
      = [[g, c_p-z u],
         [conjugate transpose, h_p-z v-z^-1 v^T]].

This is not generally equal to the unphased finite core. The terminal off-diagonal correction and both terminal H cross terms survive with phases. The proof retains all of them.

## Common limiting core and uniform tail

The limiting Schur sums use the actual unphased infinite pivot trajectory, rather than replacing each pivot by its fixed-point limit. After the displayed unitary congruence, the limit is the previously certified real S_infinity. Phase independence follows because u and v decay to zero; the quadratic series and pure fixed-point correction remain unphased.

The inherited response bounds are in ordinary Euclidean operator norm after the verified dual-Q conversion. Consequently multiplication by z does not alter any required bound. The complex Hermitian block norm inequality is the same as the real symmetric one.

With p=48+2s and

    q=3/4, theta=9/16, r_0=10^-18,
    a=1/9000000000, b=12a,

all phases satisfy

    ||U_z^* S_m(z) U_z-S_infinity||
      <= B_s
      = 24b^2 q^(2s)/(1-q^2)+48a q^s+576r_0 theta^s.

The coefficient 24 in the first term includes both increments in every pair and the three matrix-block bounds. The coefficient 48 includes the terminal C correction and both H cross terms. The last term is the pure terminal inverse-limit correction. No phase-dependent contribution is missing.

Exact arithmetic gives

    B_0=583333407/109375000000000000 < 10^-8.

The unphased seed S_50(1)>10^-6 I and two errors through S_infinity give

    U_z^* S_m(z) U_z > (49/50000000) I,  m>=50 even.

All bulk pivots are phase independent and positive, so Hermitian Schur congruence proves cI-A_h(z)^2>0 uniformly on the unit circle for h>=202. The reduced-core margin is not asserted to be a lower eigenvalue bound for the full matrix.

The same argument also applies to the older 198/25 certificate for h>=106, as stated in the primary note.

## Exact finite assembly

For N=rh and z^r=alpha, set (F_z v)_(ch+s)=r^-1/2 z^c v_s. Substitution in the signed difference operator, including the three seam edges, proves A_(N,alpha) F_z=F_z A_h(z). The geometric root-of-unity sum makes the r fiber ranges orthogonal and dimension counting makes the decomposition complete.

This handles r=1 and r=2 as well as larger cell counts. A cell has h>=202 in the general theorem, so step-one and step-two edges are distinct, have exactly the cycle-square support, and do not create small-graph edge identifications. The separate small R4 checks include h=10 without assuming disjoint ordinary and wrap blocks there.

Thus every fiber is controlled, not just selected interface modes. The bound and cell threshold are independent of r.

## Balanced even-k identification and finite coverage

For the inherited balanced word [6,4^(k-1),6,4^(k-1)], the two halves have length 4k+2. The quadrilateral flux has positive entries at 0,4,...,4(k-1) in each half. Its product in one half is (-1)^k.

When k=2j is even, the triangle sequence has period h=8j+2 and equals w_j. With global alpha=-1, its two Floquet phases are exactly i and -i. When k is odd, this half-period triangle sequence changes sign; replacing it by the periodic w_j case is invalid.

The general theorem supplies j>=25. Direct exact full-graph LDL covers precisely j=1,...,24, or n=20,36,...,388. No value is omitted between this list and the analytic range, whose first order is n=404.

## Independent executable replay

The new script replay_r4_phase.py imports no primary verifier. It reconstructs the graphs directly and performs:

- Exact natural-vertex-order rational LDL for all 24 R4 bases, a different ordering from the primary verifier
- Reconstruction from the balanced quadrilateral-flux definition and comparison with the repeated triangle word in all 24 cases
- Exact natural-order LDL at n=60: 58 positive pivots followed by a strictly negative pivot
- Symbolic Laurent-polynomial scalar Schur elimination at h=18,26,34,202, testing the full phase dependence of every entry of the retained ten-dimensional open state; at h=202 this includes 192 positive scalar eliminations
- Exact quotient-ring checks of the full Floquet intertwiner for h=10,18,26,202, r=1,2,3,4,5, and both alpha values; reduction uses z^r=alpha algebraically, with no sampled complex phases
- Exact verification of the tail constant and positive two-error seed margin

All 72 recorded checks pass. The finite tests validate the implementation; the arguments above establish the unbounded h and r quantifiers. The output stores the negative pivot and its complete positive prefix, pivot hashes for all finite bases, and every check result.

Reproduce with Python 3:

    python replay_r4_phase.py

Files: independent_replay.json and verification_stdout.txt. The proof reviewed is ../PHASE_UNIFORM_R4_ASSEMBLY.md. No remote state or earlier certificate was modified.

## Editorial findings

No blocking mathematical correction was required. In the exposition, “integer Laurent polynomial” should be read as applying to A_h(z) and A_h(z)^2, or to the denominator-cleared cap matrix; the normalized matrix cI-A_h(z)^2 has rational Laurent coefficients. This wording does not affect any argument or exact check.
