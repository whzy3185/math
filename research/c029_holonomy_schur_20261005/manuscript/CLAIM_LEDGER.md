# Claim ledger for the 5 October 2026 manuscript increment

This ledger records the scope and evidence of this increment. It does not certify all historical C029 claims. This copy was reconstructed after an executor restart. The recovery record distinguishes fresh checks from earlier retained reports.

## C1 Fixed triangle word and its two holonomies

Statement: on C_(8m)(1,2), m≥1, with labeled triangle signs t=(+,+,−,+,−,−,+,−) repeated, there are two switching classes. Their radii are R(2) and R(2cos(π/m)), where R(s)=sqrt(4+sqrt(8+s+sqrt(26−3s))). The negative-holonomy class is the unique minimizing switching class within this prescribed-word class.

Evidence: Proved. Explicit seam gauge, orthogonal finite Fourier decomposition, exact symbolic determinant, ordering of all eight real roots, and monotonicity are written in Sections 2–3. Before the restart, two independent fresh exact determinant and n32 graph checks agreed. The recovered antiperiodic verifier has also been freshly rerun successfully.

Provenance: inherited construction and exact finite formula, freshly rederived and independently checked. The exact radical and negative-holonomy formula already appear in the project repository at commit 085ea698475b7b32e0ae57457ec903a922248f69, file research/paper_strengthening/manuscript_period8_jgt/sections_en/04_period8_exact.tex, blob a550c50c079fde48759a5aa2b18895339e22ecd5. Earlier August work already used both holonomies. This round does not establish first discovery, public-release priority, or independent historical discovery.

Exact source: https://github.com/whzy3185/math/blob/085ea698475b7b32e0ae57457ec903a922248f69/research/paper_strengthening/manuscript_period8_jgt/sections_en/04_period8_exact.tex

## C2 Refutation of the September revised conjecture

Statement: for every m≥4, μ_(8m)≤R(2cos(π/m))<r_*=R(2), contradicting Conjecture 28 in arXiv:2607.17343v2 (22 September 2026).

Evidence: Proved by C1 and direct matching of graph, real-signing domain, two-sided spectral-radius objective, and unrestricted minimization quantifier to the primary source. The source's Remark 27 states that the opposite Hamilton holonomy is omitted from its search. The direct n32 rational certificate independently gives ρ<2.79<r_*.

Delta: new application of an inherited, freshly verified formula to a newly checked literature claim. The earlier paper arXiv:2607.18334 has been withdrawn and merged; it must not be treated as the latest open conjecture.

Primary source: https://arxiv.org/html/2607.17343v2#S12.SS3

Does not establish: the value of μ_(8m), global optimality of the negative-holonomy word, all minimizing signings, or first-counterexample publication priority.

## C3 Finite-size asymptotic

Statement: r_*−ρ(A_m^−)=c m^(−2)+O(m^(−4)), where c=π²(1−3/(4sqrt5))/(4r_*sqrt(10+2sqrt5))>0.

Evidence: Proved by the displayed exact derivative of R and Taylor's theorem, Corollary 3.2. This is an immediate quantitative consequence, not a claimed independent discovery or a claim that a literature search proves novelty.

## C4 Residue-two explicit-family theorem

Statement: for k≥6, n=8k+2, all step-one signs positive and step-two word t^k||(1,−1), the signed adjacency B_n obeys (198/25)I−B_n²≻0 and ρ(B_n)²<198/25<ρ_tw(n)².

Evidence: Proved, finite-certificate-assisted analytic theorem. Appendix A includes the all-length exact block identity, order-unit Riccati contraction 4/9, correctly oriented response contraction 2/3, actual-trajectory limiting Schur core, complete terminal terms, both increments per pair, and two-error seed transfer. All finite premises were exactly checked by the new standard-library rational verifier and independently from graph-based scalar Schur elimination before the restart. The standard-library verifier and certificate have now been restored and the 124 required checks freshly reproduced. The two independent scalar-Schur scripts and their JSON outputs have also been restored byte-identically and freshly rerun successfully.

Seven bases have graph orders 50,58,66,74,82,90,98; the normalized six-dimensional seed is at graph order106, which is block count26.

Delta: new analytic closure and proof repair of one existing infinite constituent. The inherited analytic-tail route was open. This proof supplies explicit constants and a new correct seed, not a new all-even truth set.

Source baseline: analytic-proof-first@7b6a351cc5f8f83f5527b7fc547f0a865ea50cf2.

The old 9/20 seed cannot be imported: it referred to a different unnormalized eight-dimensional core and is false for the normalized six-dimensional core. Use 1/50 at n106. The resulting 2/125 lower bound applies to reduced cores only, not directly to the least eigenvalue of the original n-dimensional matrix.

Does not establish: global minimizing signings, residues4 or6, a computation-free proof, or Lean formalization of the R2 theorem.

## C5 Historical all-even classification

Status: not reverified in this increment. No theorem in the manuscript relies on that historical result. Keep its existing correction history, including the G6 r-to-2r multiplicity correction. Do not promote a label, README, old clean build, or prior chat summary into fresh proof evidence.

## Formal proof status

The raw negative-holonomy matrix bridge is now verified by `TargetA.period8_alpha_minus_main_theorem`: for every L>0 and every Hermitian eigenvalue of the explicit raw matrix on8L vertices, the eigenvalue square is strictly below period8Edge. Its assumptions no longer contain an unproved seam equivalence or a Fourier bridge. See [the current formal report](../lean/raw_graph_extension/RAW_GRAPH_VERIFICATION_REPORT.md).

The two bridge modules add31 theorems, for47 new theorems beyond baseline; all196 baseline-plus-extension declarations have a successful axiom audit with only propext, Classical.choice and Quot.sound. This supersedes the raw-graph gap recorded in the earlier165-declaration report, which remains an unchanged historical checkpoint.

This extension does not formalize the exact attained finite-size radical formula, integer n32 certificate, R2/R4 analytic tail arguments, unrestricted global minimum or publication novelty. The final declaration uses the Hermitian eigenvalue list, without a separate spectral-radius wrapper.

## Literature boundary

The current-source audit checked the withdrawal/merger, September v2, the author's current source snapshot, and targeted follow-up searches. No later correction was found in that bounded search. This does not prove absence of later work or establish absolute novelty. The general holonomy/character method is prior art; the two external comparison sources are Luo–Roy and Chen–van Dam–Bu, with hypotheses and scope stated in the introduction.


## C6 Subsequent uniform one-G6 strengthening

Statement: for the same explicit positive-Hamilton-holonomy signing with step-two word t^k||(1,−1), rho(A_(8k+2))²<790537/100000=7.90537 for every k≥1. At n=202, rho(A_202)²>7905369/1000000=7.905369. Thus the supremum over this prescribed family lies in (7.905369,7.90537], with a non-strict upper endpoint.

Evidence: Proved, finite-certificate-assisted analytic theorem. The separate supplement uses a fresh entrance at index48, radius10⁻¹⁸, metric bound1/2, response contraction3/4, Riccati contraction9/16, normalized seed margin10⁻⁶ at n202, and tail error below10⁻⁸. Twenty-four smaller bases n10,18,…,194 plus the seed cover all k≥1. The n10 graph is checked directly to handle coincident block couplings. The primary verifier passes79 exact checks; independent full-graph scalar-Schur extraction verifies every local premise and the exact lower-obstruction pivot. Both implementations freshly pass in the assembled package.

Source: [complete stronger proof](../certificates/strengthening/UNIFORM_ONE_G6_CAP.md) and [independent audit](../certificates/strengthening/audit/INDEPENDENT_STRONGER_CAP_AUDIT.md). This supplement strengthens C4 without changing the earlier 11-page PDF.

Does not establish: the unrestricted minimum over all signings, global minimizing classes, exact family supremum, convergence or monotonicity in k, a new twisted-benchmark counterexample below n50, residues4 or6, or a Lean proof of this theorem.


## C7 Phase-uniform assembly and the balanced even-k R4 family

Proved, finite-certificate-assisted analytic theorem and independent audit PASS: a one-G6 cell of length h=8j+2>=202 has squared spectral radius below7.90537 at every unit complex phase. Any positive number of identical equally spaced cells, with either real Hamilton holonomy, has the same cap by the complete finite Fourier decomposition.

For the balanced negative-holonomy family N=16j+4, all j>=1 satisfy this cap: 24 exact real-graph bases N20,36,…,388 join the analytic range beginning at N404. The twisted comparison follows for j>=3 (N>=52). A strictly negative LDL pivot at the balanced odd-k case N60 proves the same sharp cap fails there.

Evidence: complete phase law and Hermitian terminal-core proof; unchanged R2 exact premises; 20 primary exact checks and72 independent checks, including quotient-ring fiber embeddings and a distinct full-graph LDL ordering. See [proof](../certificates/r4_pilot/PHASE_UNIFORM_R4_ASSEMBLY.md) and [audit](../certificates/r4_pilot/audit/INDEPENDENT_R4_PHASE_AUDIT.md).

Does not establish: arbitrary placements/types of interfaces, all residue-four orders, an odd-k theorem, a global minimum or any R4 Lean formalization. The historical r-to-2r correction is respected; no localized-mode count supplies the argument. The original manuscript PDF is unchanged and this is a separate supplement.
