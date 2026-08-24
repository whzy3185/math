# Target A Proof Completion Synthesis

## 1. Baseline

```text
reference checkpoint: e6a01d8bf30088dae1042a237398bee2df138280
actual integration base: e6a01d8bf30088dae1042a237398bee2df138280
branch: agent/target-a-discovery-snapshot
starting ahead/behind: 0/0
starting working tree: clean
```

The formal English and Chinese manuscript trees remained frozen at
`59e3a8f73a152ef06f994e979b7219a3365efeae` and
`57ae03fb5b90866f84d0d72b414008678e8f5004`. Task 57 creates a separate
canonical-current proof layer; it does not rewrite either manuscript.

The Lane D import-safety audit is based on the Task 57 integration checkpoint
`06316943472d9a1ea22f57b383bd3a0091cd4577`. It changes no theorem and does
not treat its producer-side scan as independent mathematical verification.

## 2. Canonical Main Theorems

- **T1: Complete Even-Order Classification.** For every even `n>=8`, the
  conjectured lower bound fails exactly at `n=32`, `n=40`, and every even
  `n>=48`.
- **T2: Reference-Phase Theorem.** The period-eight reference phase has exact
  squared edge `eta=4+sqrt(10+2sqrt(5))<8`.
- **T3: Sector-Shift Theorem.** A gap charge `q=g-4` changes the translated
  reference sector by `q modulo 4`, and shifts compose additively.
- **T4: Elementary Phase-Slip Theorem.** The G6 interface has global squared
  spectral edge `c6` and `dim ker(H6-c6)=2`.
- **T5: Single-Gap Optimality Theorem.** G6 uniquely minimizes the spectral
  edge among abnormal single gaps, and every other abnormal gap lies strictly
  above `c6+1/250`.
- **T6: Separated Phase-Slip Theorem.** For `r in {1,2,3}` and certified
  separation, exactly `2r` squared levels lie in the fixed near-`c6` window,
  with explicit exponential control.
- **T7: Residue-Class Upper-Constructions Theorem.** Legal one-, two-, and
  three-G6 words give the residue `limsup` bounds and the explicit large-order
  counterexample tail.

These are exactly seven main theorem families. T6 and T7 may share a
manuscript section, but they are not one theorem family.

## 3. Complete Even-Order Classification

The final proof uses an exhaustive disjoint partition:

```text
8<=n<=30;  n=32;  34<=n<=46;  48<=n<240;  n>=240.
```

Within `34<=n<=46`, the exact finite-state theorem proves validity at
`34,36,38,42,44,46`, while a separate exact LDL certificate proves failure at
40. The finite-state closure has exactly 64 terminal `(Q,alpha)` records,
consisting of six threshold equalities and 58 strict Rayleigh records; all are
resolved. The earlier number 84 was a documentation sum error, not a
certificate or coverage gap. The first range is closed by complete
switching-class certificates, 32
by an explicit exact counterexample, `48<=n<240` by 96 full-matrix rational
LDL certificates, and `n>=240` by the global IMS construction. This proves a
truth-value classification, not a classification of minimizers or exact
values of `m_n`.

The canonical convention is

```text
theta_n:=rho_-(n)^2,
failure at n iff m_n<rho_-(n) iff m_n^2<theta_n.
```

The exhaustive lower-bound argument proves `m_n>=rho_-(n)` at every order
outside the failure set. Claim `T8.0` now supplies one explicit antibalanced
signing with `Q_i=-1`, `alpha=-1`, and spectral radius exactly `rho_-(n)` for
every even `n>=8`. Thus `m_n<=rho_-(n)`, and the two inequalities give
`m_n=rho_-(n)` on the validity set. The absence of a strict counterexample is
not used as a substitute for attainment.

Status: `PAPER_READY` subject only to importing the proof package into LaTeX.

## 4. Reference Phase

One canonical tau convention, Bloch parameter, and fiber matrix are fixed in
`03_reference_phase`. The Floquet characteristic is maximized exactly at the
identified band parameter, giving

```text
eta=4+sqrt(10+2sqrt(5)).
```

Gap 4 is proved to be precisely the unperturbed translated reference phase.
Status: `PAPER_READY`.

## 5. Charge / Sector

Positive-Q defect locations define cyclic gaps `g_j` with `sum g_j=n` and
charges `q_j=g_j-4`, hence `sum q_j=n-4d`. The four backgrounds `B_s` are
defined before operator matching. The recurrence `tau_(i+1)=Q_i tau_i`
proves the elementary sector law `sigma(q)=q mod 4`; composition is addition
in `Z/4Z`. No Evans or Grassmann machinery is needed.

Status: `PAPER_READY`.

## 6. G6 Global Edge

Claim `T4.0` first proves that the G6 essential spectrum is exactly the
periodic bulk spectrum with upper edge `eta`, so every higher spectral point
is a discrete finite-multiplicity eigenvalue with exponentially decaying
tails. The remaining proof is distilled into four mathematical reductions:

1. bulk hyperbolicity above `eta` gives two-dimensional stable and unstable
   transfer spaces;
2. an interface eigenvalue is equivalent to geometric stable/unstable
   matching;
3. exact elimination and Sturm isolation give a complete finite candidate
   list, while unsquared physical matching excludes every candidate above
   `c6`;
4. the isolated root `c6` satisfies the genuine physical matching condition.

The computer appendix exposes the chart cover, chart transitions, isolating
intervals, determinant signs, orientation handling, certificate bindings, and
independent reconstruction. The elementary symmetry

```text
K^2=-I,  KA=-AK,  KH=HK
```

supplies the simple negative unsquared partner and gives squared multiplicity
two. Status: `PAPER_READY_COMPUTER_ASSISTED`.

## 7. Single-Gap Hierarchy

Six exact finite vectors cover `g=1,2,3,5,7,8`. One fixed vector covers every
`g>=9` with quotient `182/23`. G6 supplies equality, and gap 4 is reference
bulk. The new direct exact comparison proves

```text
sup sigma(H_g)>c6+1/250,  g not in {4,6}.
```

The smallest margin occurs at `g=8` and equals
`174815250030533/310875000000000000`. A dedicated producer, independent
checker, and 12 fail-closed tests bind the corollary. Status: `PAPER_READY`.

## 8. Exact-2r

Claim `T6.0` first identifies each enlarged finite-ring interface patch with
the certified infinite G6 local model for both orientations, lifts, and
holonomies, with the seam outside all interface collars. The canonical proof
then begins with two orthonormal G6 modes per interface. It
then applies truncation, Gram control, a `2r`-dimensional residual subspace,
the codimension-`2r` complementary gap, min-max, and the corrected
`2r x 2r` Feshbach determinant. This proves exactly `2r` levels counted with
multiplicity and

```text
|lambda_j-c6|<3505r(9/25)^ell.
```

No individual simplicity, interaction coefficient, or genuine three-body
claim is inferred. Status: `PAPER_READY_COMPUTER_ASSISTED`.

## 9. IMS / Residue

The exact discrete IMS identity is separated from the patch classification.
Legal residue constructions use one, two, and three G6 interfaces for
residues 2, 4, and 6. Gap sums, parity, sector closure, holonomy, and minimum
separation are checked before applying localization. The resulting theorem is

```text
limsup_(k->infinity) m_(8k+r)^2<=c6,  r in {2,4,6}.
```

No matching liminf is claimed. The global tent estimate yields the analytic
tail from 240 and joins the exact finite bridge at 48. Status: `PAPER_READY`.

## 10. Periodic / Moments

Only moments with a clear role in defect count, charge, or local obstruction
are retained. Long walk expansions belong in the appendix or are omitted.
The periodic theorem is stated only for primitive legal phases of period
`p<=24`, with all equivalences and primitive normalization explicit. Read-only
period-25/26 work is excluded from theorem dependencies.

Disposition: compact context in main text; finite classification in appendix;
unused exploratory moment material omitted.

## 11. Computer-Assisted Boundary

Every machine-assisted theorem is presented as

```text
mathematical reduction
-> finite exact object
-> independent reconstruction
-> mathematical consequence.
```

Accepted arithmetic types are integer/rational quadratic forms, exact LDL,
Sturm/root isolation, outward interval arithmetic, symbolic determinant
identities, finite graph reachability, and certificate hash checks.
Floating-point calculations propose vectors or root locations only. The
minimal referee entry point is

```text
python3 research/scripts/verify_target_a_task57.py.
```

Final integration verification on the Task 57 working tree produced:

```text
unified referee entry: 13/13 checkers PASS
focused Task 53--57 regression: 290 passed
full research/scripts regression: 727 passed, 3 skipped, 20 subtests passed
Task 57 structural/tamper tests: 18 passed
git diff --check: PASS
```

The canonical registry contains 46 accepted claims. Twelve T-series claims
are directly labeled `COMPUTER_ASSISTED_PROVED`; the total is 26 after
including supporting appendix claims and explicit finite lemmas. This count
does not mean that 26 independent black-box computations are used: many rows
are mathematical consequences sharing the same checked finite object.

## 12. Stale Claims

The canonical package uses rank two at one G6 interface, exact `2r` for `r`
interfaces, a codimension-`2r` complement, and a `2r x 2r` effective matrix.
Historical exact-`r`, rank-one, and `r x r` statements remain only as labeled
provenance or retraction records. The fixed-string audit found 111 relevant
lines in 46 tracked files: 51 current-correct, 52 historical-superseded, two
source-import hazards marked `MUST_UPDATE_BEFORE_MANUSCRIPT`, and six safe
internal retraction/tamper occurrences. Neither frozen manuscript contains a
stale rank claim. The full classification is recorded in
`TARGET_A_STALE_RANK_CLAIM_AUDIT.md`.

For manuscript reconstruction, the operative categories are now
`CANONICAL_IMPORT`, `IMPORT_WITH_CAUTION`,
`DO_NOT_IMPORT_CURRENT_CLAIMS`, and `HISTORICAL_ONLY`. Exact-path overrides,
including the two known hazards and the superseded exact-`r` corpus, are in
`TARGET_A_MANUSCRIPT_IMPORT_SAFETY.md`.

## 13. Referee Audit

The graph-theory audit checks that switching/flux and finite-state arguments
are visible before operator machinery. The spectral audit attacks candidate
completeness and physical matching. The computer-assisted audit checks finite
coverage and exact endpoints. The operator audit checks exact-`2r`, IMS, and
Feshbach dimensions. The editorial audit checks theorem order, proof length,
and appendix isolation. All open future-work statements remain outside the
main theorem hierarchy.

## 14. JGT Paper Architecture

Recommended working title:

```text
Signed Spectral-Radius Minimization on the Square of a Cycle:
Phase Slips and a Complete Even-Order Classification
```

Recommended order:

1. problem, switching, and flux;
2. reference phase and charge sectors;
3. elementary G6 phase slip;
4. complete single-gap optimality;
5. separated phase slips;
6. residue-class upper constructions;
7. complete even-order classification;
8. concise discussion and bounded periodic context;
9. computer-assisted appendices for G6, small orders, exact LDL, and
   exact-`2r`.

## 15. Readiness

```text
READY_FOR_MANUSCRIPT_REFRAME
```

The proof corpus is organized for direct manuscript import. The formal LaTeX
trees remain intentionally unchanged in Task 57. Direct import must follow
`TARGET_A_MANUSCRIPT_IMPORT_SAFETY.md`; equality wording must not be imported
without its candidate-attainment dependency.

## 16. Git

Starting HEAD: `e6a01d8bf30088dae1042a237398bee2df138280`.

The Task 57 proof-completion commit is the commit containing this synthesis.
Its exact SHA, final ahead/behind, remote equality, and clean working-tree
state are recorded in the final integration response after push. PR: none.
