# CLAIM_LEDGER

Use one row for every claim that could materially affect correctness, novelty, or the paper's headline contribution.

## Evidence states

- `Observed` — exploratory evidence only.
- `Verified` — exact verification for a stated finite range/object.
- `Proved` — complete general mathematical proof.
- `Published/Established` — supported by a reliable source that proves the exact claim.

## Claims

| ID | Claim | Type | Evidence state | Exact scope / hypotheses | Proof, certificate, or source | Depends on | Falsification / audit status | Paper location | Notes |
|---|---|---|---|---|---|---|---|---|---|
| C001 |  | main theorem / lemma / computation / novelty / literature / equality / algorithm |  |  |  |  |  |  |  |

## Main-theorem consistency checks

For each headline theorem verify:

- [ ] statement in theorem environment matches the proved statement;
- [ ] abstract does not claim more;
- [ ] introduction does not silently omit hypotheses;
- [ ] equality/sharpness language is justified;
- [ ] computational range is stated exactly;
- [ ] Lean theorem, if required, has the same mathematical content;
- [ ] cited prior art does not already subsume the theorem;
- [ ] independent audit has checked all dependencies.

## Literature claims

| ID | Paper claim | Primary source | Exact theorem/page/section | What the source establishes | What it does not establish | Last checked |
|---|---|---|---|---|---|---|
| L001 |  |  |  |  |  |  |

## Counterexample / obstruction ledger

| ID | Target statement | Counterexample or obstruction | Exact verification | Consequence | Archived at |
|---|---|---|---|---|---|
| X001 |  |  |  | theorem false / hypothesis necessary / constant non-sharp / proof lemma false |  |

## Strengthening ledger

| Attempt | Starting level | Proposed stronger statement | Outcome | Evidence | Next implication |
|---|---|---|---|---|---|
| S001 | L3 |  | open / proved / false / prior art |  |  |
