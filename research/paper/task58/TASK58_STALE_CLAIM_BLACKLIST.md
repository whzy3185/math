# Task 58 Stale-Claim Blacklist

Status: `TASK58_FIRST_SUBMISSION_CONTROL`.

This document is an editorial fail-closed filter for the Task 58 first
submission. It changes no theorem and does not replace the canonical import
rules in
`research/paper/proof_completion/TARGET_A_MANUSCRIPT_IMPORT_SAFETY.md`.
When the two documents differ, the canonical import-safety manifest controls
the mathematics and this blacklist controls first-submission wording.

## 1. Context classes

Every occurrence of a blacklisted expression must be assigned one of the
following contexts before it can survive an editorial scan.

| Context | Meaning | First-submission disposition |
|---|---|---|
| `ACTIVE_POSITIVE` | A theorem, definition, proof step, formula, implication, abstract claim, or conclusion asserted as current mathematics. | Reject whenever the expression is blacklisted below. |
| `EXPLICIT_REJECTION` | A sentence that says a claim is false, unproved, out of scope, or not used. | Permitted in internal control and referee files; in the submitted paper use only when mathematically necessary and phrase the current result positively instead when possible. |
| `HISTORICAL_PROVENANCE` | A clearly dated description of a withdrawn research-stage formulation. | Permitted only in internal audit records. Task 58 does not import research-correction history into the first submission. |
| `FAIL_CLOSED_TEST` | A literal token used by a checker or tamper test to prevent regression. | Permitted only in code, tests, or reproducibility controls, never as manuscript prose. |
| `BOUNDED_TRUE_BUT_OMITTED` | A valid bounded result deliberately excluded from the first-submission story. | May remain in the repository; do not import into the paper, its appendices, figures, tables, or general-purpose supplement. |

Quotation marks, code formatting, a citation, or a parenthetical disclaimer do
not by themselves change an occurrence from `ACTIVE_POSITIVE`. The surrounding
sentence must make the rejection or historical status unambiguous.

## 2. Falsified rank and dimension language

The current rank contract is:

```text
dim ker(H_6-c_6)=2;
r separated G6 interfaces give exactly 2r near-c_6 squared levels
in the proved scope r in {1,2,3}, D>=1040;
the complementary space has codimension 2r;
the problem-specific Feshbach operator is 2r x 2r.
```

The following expressions are forbidden in every `ACTIVE_POSITIVE` context:

| Scan expression | Rejected active meaning | Allowed context |
|---|---|---|
| `rank-one`, `rank one` | One squared G6 mode or a rank-one `c_6` eigenspace. | `EXPLICIT_REJECTION`, `HISTORICAL_PROVENANCE`, or `FAIL_CLOSED_TEST` only. |
| `exact-r`, `exact r` | Exactly `r` near-`c_6` squared levels for `r` separated G6 interfaces. | The three non-active contexts above only. A combinatorial count of `r` interfaces must not be called exact-`r`. |
| `codimension-r`, `codimension r` | A codimension-`r` complement for the G6 cluster. | The three non-active contexts above only. |
| `r x r`, `r-by-r`, `r times r` | The problem-specific G6 Feshbach or effective operator has dimension `r`. | The three non-active contexts above only. An unrelated matrix dimension requires manual review and different notation. |
| `I_r` | The obsolete problem-specific ansatz `H_eff=c_6 I_r+...`. | `EXPLICIT_REJECTION`, `HISTORICAL_PROVENANCE`, or `FAIL_CLOSED_TEST` only. An unrelated identity matrix must be renamed or accompanied by a manual false-positive ruling. |

Do not explain the rank correction in the submitted article. State the
current rank-two and exact-`2r` results directly. The known superseded corpus
and the two exact-path source hazards remain governed by the canonical
import-safety manifest and may not supply current formulas or proof prose.

## 3. Open statements that must not be promoted

These expressions usually signal a theorem whose current unrestricted form
is open. They require manual inspection even when the exact spelling differs.

| Scan family | Prohibited promotion | Safe first-submission treatment |
|---|---|---|
| `common limit`, `common-limit` | A common limit for the nonzero residue classes, or existence of unrestricted residue limits. | State only the proved residue-class `limsup` upper bounds. An explicit sentence saying that no limit is claimed is allowed if needed. |
| `unrestricted liminf`, `common liminf`, `common-liminf` | Equality of an unrestricted liminf with `c_6`. | Omit, or identify it narrowly as an open problem in the conclusion without suggesting evidence is a theorem. |
| `all-period`, `all period`, `arbitrary-period uniqueness`, `all periods` | Uniqueness or optimality of the period-eight reference phase over every period. | State only the exact reference-phase theorem actually used. Do not extrapolate from a bounded periodic frontier. |
| `arbitrary multi-gap optimality`, `universal multi-gap`, `all-interface optimality` | Extension of the single-gap hierarchy to arbitrary finite multi-gap cores. | State the single-gap quantifier exactly; do not infer a universal interface theorem. |
| `interaction coefficient`, `pairwise splitting`, `three-body`, `three body` | Universal nonzero pair interactions, finite-ring simplicity, or a genuine three-body term. | Omit. These are not dependencies of the classification. |

The words `limit`, `period`, `interaction`, and `rank` are not globally
forbidden mathematical vocabulary. The listed compound meanings are the
hazards; every nearby generalized quantifier must be checked manually.

## 4. Valid results excluded from the first submission

The following material is not declared false. It is excluded to preserve the
locked classification-plus-G6 story and the page budget.

| Scan expression or topic | Evidence boundary | First-submission rule |
|---|---|---|
| `p<=24`, `p \le 24`, `periodic frontier` | A bounded computer-assisted theorem through period 24. | `BOUNDED_TRUE_BUT_OMITTED`; do not cite, summarize, tabulate, or place in an appendix. |
| `period 25`, `period-25`, `period 26`, `period-26`, `25/26` | Exact finite read-only recomputation, not a promoted theorem. | Omit completely. It may remain in internal audit records only. |
| `multi-gap`, `multigap`, `31,008`, `(3,3)` obstruction | Bounded or subclass obstruction results; no universal multi-gap theorem follows. | Omit the package from the first submission. The main text may still use several separated G6 interfaces in the proved finite-ring construction; call those separated phase slips, not the multi-gap obstruction program. |
| `reference graph`, `105/164`, `420/656` | Producer-side finite graph evidence. | Omit completely. |
| `full moments`, `moment machinery`, `M_1`, `M_2`, `M_3` | Supporting identities not needed in the locked narrative. | Omit the general machinery. A local identity may appear only if it is independently required by an imported proof and rewritten from its canonical source. |
| `interaction fit`, `interaction asymptotics` | Exploratory or non-promoted interaction work. | Omit completely. |

The bounded `p<=24` theorem must never be rewritten as an all-period theorem.
The period-25/26 computation must never be used to extend the bounded theorem.

## 5. Workflow and authorship-language blacklist

The submitted paper must read as a mathematical article, not as a record of
the research workflow. Scan case-insensitively for:

```text
Task 52
Task 53
Task 54
Task 55
Task 56
Task 57
Task58
script observed
the script found
AI
agent
subagent
Codex
prompt
```

Disposition:

- `Task 52` through `Task 57`, `Task58`, `agent`, `subagent`, `Codex`, and
  `prompt` are forbidden in the manuscript, appendices, captions, tables,
  acknowledgments, and data/code statement.
- `AI` is forbidden as workflow or authorship language. A genuine bibliographic
  title containing the letters `AI` is a manual false positive, not a reason
  to alter the citation.
- `script observed` and equivalent formulations are forbidden as logical
  steps. Use the four-part computer-assisted proof form: mathematical
  reduction, finite exact object, exact verification, and mathematical
  consequence.
- Prefer `independent checker`, `verification program`, or `exact computation`
  in the reproducibility supplement. The bare word `script` should not appear
  in the mathematical narrative.
- Internal control documents, historical audits, checker source, and tests may
  retain these tokens under `HISTORICAL_PROVENANCE` or `FAIL_CLOSED_TEST`.

## 6. Quantifier and conclusion guardrails

The word scan is supplemented by the following semantic checks:

1. The classification is exactly
   `m_n<rho_-(n)` if and only if `n=32`, `n=40`, or even `n>=48`.
2. Equality at the remaining even orders uses both exhaustive lower bounds and
   explicit candidate attainment.
3. G6 explains eventual permanent failure; exact finite verification places
   the beginning of continuous failure at order 48. Do not attribute the
   sharp onset 48 to IMS or to G6 alone.
4. The analytic IMS tail begins at `n>=240`; it is not the final onset.
5. Residue results are `limsup` upper bounds only. Do not silently replace
   `limsup` by `liminf` or `limit`.
6. Single-gap optimality is not arbitrary-interface optimality.
7. Exact-`2r` is a structural refinement, not a premise of the sharp
   classification threshold `N_*=48`.

## 7. Scan disposition

Each scan hit must be recorded as one of:

```text
REJECT_ACTIVE_CLAIM
ALLOW_EXPLICIT_REJECTION
ALLOW_INTERNAL_HISTORY
ALLOW_FAIL_CLOSED_TEST
OMIT_FIRST_SUBMISSION
MANUAL_FALSE_POSITIVE
```

An unexplained hit fails the Task 58 import audit. Passing the lexical scan is
necessary but not sufficient: theorem quantifiers, evidence labels, and source
paths must still be checked against the canonical proof-completion package.
