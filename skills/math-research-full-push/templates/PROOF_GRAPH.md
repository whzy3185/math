# PROOF_GRAPH

Use this file as the dependency DAG for the current headline theorem. Do not hide a missing lemma inside prose.

## Main theorem

- ID: `T0`
- Exact statement:
- Evidence state:
- Paper location:
- Lean theorem:

## Dependency DAG

```text
T0 Main theorem
├── O1 Structural reduction — [open/proved/established/false]
│   ├── O1.1 Local lemma — [status]
│   └── E1 External theorem — [source + hypothesis check]
├── O2 Extremal/classification step — [status]
└── O3 Equality/sharpness step — [status]
```

## Obligation registry

| ID | Exact statement | Status | Needed by | Dependencies | Evidence / proof location | Falsification status | Lean status | Risk |
|---|---|---|---|---|---|---|---|---|
| O1 |  | open | T0 |  |  |  |  | high |

Allowed status values:

- `open`
- `observed`
- `verified-finite`
- `proved`
- `published`
- `false`
- `superseded`

## External theorem registry

| ID | External result | Source | Exact hypotheses | Hypotheses matched? | Where used | Notes |
|---|---|---|---|---|---|---|
| E1 |  |  |  | yes/no |  |  |

Never cite a theorem by name alone when a subtle hypothesis matters.

## Bottleneck analysis

### Current highest-leverage obligation

- ID:
- Why it blocks the headline theorem:
- Current attack:
- Cheapest falsification test:
- Alternate route if it fails:

## Hidden-assumption checklist

For the current proof, explicitly check:

- [ ] object exists under the stated hypotheses;
- [ ] denominators/nonzero choices are justified;
- [ ] sign/order/domain assumptions are recorded;
- [ ] compactness/minimality/extremality arguments attain their objects when needed;
- [ ] induction/reduction measure strictly decreases;
- [ ] transformations are invertible when claimed;
- [ ] cases are exhaustive;
- [ ] quantifier order is preserved;
- [ ] no implication has silently been reversed;
- [ ] no finite computation is being used as an infinite proof;
- [ ] no theorem is used before the hypothesis needed to invoke it has been established;
- [ ] equality/sharpness is proved separately from the main inequality/existence statement.

## Adversarial tests

| Target | Test | Result | Consequence |
|---|---|---|---|
| T0/O1/... | exhaustive small cases / boundary case / symbolic check / alternate derivation |  |  |

## Failed proof routes

Archive failed routes so future continuation does not repeat them without a new idea.

### F1 —

- Target obligation:
- Attempt:
- Exact failure point:
- Counterexample/obstruction if any:
- What remains reusable:

## Proof-to-Lean mapping

| Human ID | Lean declaration/file | Status | Mismatch / missing library input |
|---|---|---|---|
| O1 |  |  |  |

## Proof-to-paper mapping

| Human ID | Paper section/theorem | Claim ledger ID | Alignment checked? |
|---|---|---|---|
| T0 |  |  |  |
