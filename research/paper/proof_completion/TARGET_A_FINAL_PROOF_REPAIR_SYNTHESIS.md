# Target A Final Proof Repair Synthesis

## 1. Baseline

```text
reference checkpoint: 06316943472d9a1ea22f57b383bd3a0091cd4577
actual integration base: 06316943472d9a1ea22f57b383bd3a0091cd4577
branch: agent/target-a-discovery-snapshot
starting ahead/behind: 0/0
starting working tree: clean
```

Formal manuscript trees remained frozen at:

```text
English  59e3a8f73a152ef06f994e979b7219a3365efeae
Chinese  57ae03fb5b90866f84d0d72b414008678e8f5004
```

## 2. Candidate Attainment

For every even `n>=8`, the candidate has tree-gauge signs

```text
a_i=1 (i<n-1),  a_(n-1)=-1,
b_i=(-1)^i (i<n-2),  b_(n-2)=-1,  b_(n-1)=1.
```

Equivalently, `Q_i=-1` and `alpha=-1`. On the antiperiodic space
`u_(j+n)=-u_j`, the unsquared adjacency has two-dimensional Fourier fibers

```text
2 [[cos theta,  cos 2theta],
   [cos 2theta,-cos theta]],
theta=(2k+1)pi/n.
```

Their squared eigenvalue is
`4(cos^2(theta)+cos^2(2theta))`. Exact convex endpoint comparison gives the
maximum at `theta=pi/n`, hence

```text
rho(A_(sigma_n^-))=rho_-(n).
```

Scope: every even `n>=8`. Claim ID: `T8.0`. Machine dependency: none. The
structural verifier checks the symbolic fiber identity but is corroborative,
not the proof source. Status: `PURE_ANALYTIC_PROVED`.

## 3. Complete Classification Logic

Failure means

```text
m_n<rho_-(n),
```

equivalently `m_n^2<theta_n` for `theta_n=rho_-(n)^2`. On the validity set,
finite exhaustion gives `m_n>=rho_-(n)` while `T8.0` gives
`m_n<=rho_-(n)`, so `m_n=rho_-(n)`. On the failure set, exact strict
witnesses give the strict inequality.

```text
validity set: {8,10,...,30,34,36,38,42,44,46}
failure set:  32, 40, and every even n>=48.
```

The complete theorem now depends explicitly on both attainment and
lower/strict classification. Status: `PAPER_READY`.

## 4. G6 Essential Spectrum

Let `H_L` and `H_R` be the periodic whole-line continuations of the two G6
tails. Cutting beyond the core gives

```text
H_dec=H_L^- direct_sum F direct_sum H_R^+.
```

The finite range of `H_6` makes `H_6-H_dec` finite rank. Compact invariance,
cutoff Bloch Weyl sequences, and a half-line Fredholm resolvent parametrix
give

```text
sigma_ess(H_6)=sigma(H_L) union sigma(H_R)=sigma(H_ref),
sup sigma_ess(H_6)=eta.
```

Every spectral point above `eta` is isolated of finite multiplicity.
Decomposition through `H_6=A_6^2` gives unsquared branches at
`+/-sqrt(y)`; hyperbolic periodic transfer forces exponentially decaying
stable/unstable tails. Thus the Evans plane-intersection criterion is
necessary and sufficient in the domain where it is used. Claim ID: `T4.0`.
Status: `PURE_ANALYTIC_PROVED`.

## 5. G6 Proof Cleanup

The unnamed “standard cutoff Weyl-sequence argument” is replaced by the
essential-spectrum lemma. The isolating interval is now named `J_6`; every
former ambiguous reference to “interval (1)” uses `J_6`. Stable/unstable
planes are parameterized consistently by the unsquared variable `lambda`.
Status: `PASS`.

## 6. Exact-2r Patch Identification

For each marked G6 core, the cutoff and its range-four enlarged support are
defined explicitly. At `D>=1040`, `S=floor(D/4)>=260`; every coefficient
collar sees exactly one abnormal gap, each pure-bulk plateau has length at
least 16, and the holonomy seam is at least eight sites from every interface
support.

Translation, optional reflection, and diagonal switching identify forward
and reflected patches, both tau lifts, both holonomies, and cyclic wraparound
with the canonical line G6 model. Noninterface patches are exact translated
period-eight bulk sections. The transported normalized pair
`psi_(j,+/-)` is orthogonal before truncation, and
`phi_(j,+/-)=chi_j psi_(j,+/-)` is exactly the pair in the Gram matrix.
Therefore the complement-gap orthogonality is applied to the same local model
and same rank-two eigenspace.

Claim ID: `T6.0`. Scope remains `r in {1,2,3}`, `D>=1040`; constants 1040,
3505, and `9/25` are unchanged. Status: `PURE_ANALYTIC_PROVED`.

## 7. Canonical Consistency

The hierarchy has exactly seven main theorem families, Theorems 1.1--1.7.
Canonical notation fixes

```text
theta_n:=rho_-(n)^2,
```

compares `m_n` only with `rho_-(n)`, and compares `m_n^2` only with
`theta_n`. Claims `T8.0`, `T4.0`, and `T6.0` were added without renumbering
existing claims. Status: `PASS`.

## 8. Manuscript Import Safety

`TARGET_A_MANUSCRIPT_IMPORT_SAFETY.md` defines the categories
`CANONICAL_IMPORT`, `IMPORT_WITH_CAUTION`,
`DO_NOT_IMPORT_CURRENT_CLAIMS`, and `HISTORICAL_ONLY`. The exact hazards

```text
research/proofs/task52/TARGET_A_MULTI_SLIP_INTERACTION_ASYMPTOTICS.md
research/proofs/task54/TARGET_A_COMMON_RESIDUE_LIMIT_SCOPE.md
```

are blacklisted for current claims, and the superseded exact-`r` corpus is
listed path by path as historical only. Canonical import root:
`research/paper/proof_completion/`. Status: `PASS`.

## 9. Stale-rank Audit

Active positive rank-one claims: 0. Active positive exact-`r` claims: 0.
Active positive `r x r` problem-specific claims: 0. Historical rejection and
tamper occurrences remain deliberately visible. Status: `PASS`.

## 10. Evidence Boundary

| Theorem family | Final evidence boundary |
|---|---|
| Complete classification | `COMPUTER_ASSISTED_PROVED`; candidate attainment is analytic, finite lower/strict pieces are certified |
| Orders 34--46 | `COMPUTER_ASSISTED_PROVED`; 64 exact terminals, zero unresolved |
| G6 global edge | `COMPUTER_ASSISTED_PROVED`; essential-spectrum bridge is analytic, physical candidate completeness is certified |
| Single-gap hierarchy | analytic variational proof using certified `c6` input and exact integer witnesses |
| Exact-`2r` | `COMPUTER_ASSISTED_PROVED`; patch identification is analytic, one-interface/Floquet constants are certified |
| Residue limsup | analytic upper-construction corollary of certified local edge inputs; no liminf |
| Periodic frontier | bounded `COMPUTER_ASSISTED_PROVED` appendix theorem for `p<=24` only |

## 11. Verification

```text
Task 57.5 unified referee gate: PASS (13 inherited checkers + 1 repair gate)
Task 57.5 structural/tamper tests: 15 passed
full research/scripts regression: 736 passed, 3 skipped, 20 subtests passed
git diff --check: PASS
formal manuscript hashes: PASS
```

## 12. Readiness

```text
READY_FOR_TASK58_MANUSCRIPT_REFRAME
```

The independent hostile review finds no necessary implication still implicit
in Theorems 1.1, 1.4, or 1.6.

## 13. Git

Starting HEAD: `06316943472d9a1ea22f57b383bd3a0091cd4577`.
The final repair commit is the commit containing this synthesis. Its exact
local/remote SHA, ahead/behind, clean-tree state, and push result are recorded
in the final integration response. PR: none.
