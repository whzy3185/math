# Math Research Full-Push v5 — skill evaluation

Date: 2026-09-09
Branch: `skill/math-research-full-push-20260909`
Comparison baseline: v4 commit `b9bbadf7b779908a82522b4a7f6b25609233fb71`

## Evaluation method

This report follows the public OpenAI `plugin-eval` skill evaluator logic: frontmatter/trigger checks, progressive disclosure, link integrity, SKILL size, trigger/invoke/deferred token budgets, then benchmark scenarios for real workspace use.

The local environment used for this refactor cannot resolve github.com, so the CLI itself could not be executed here. Static bands below are reconstructed from the evaluator's published rules and conservative GitHub byte-size upper bounds. A real Codex benchmark config is included for later execution.

## Before / after

### v4

- `SKILL.md`: about 860 lines / 33.8 KB.
- Large top-level design/reference docs plus nine templates lived inside the installable skill bundle.
- Expected evaluator findings: `skill-too-large` error, missing progressive disclosure warning, excessive invoke budget error, excessive deferred budget error, weak trigger wording warning.
- Reconstructed score: roughly **45 / F / high risk**.
- Research methodology quality was much stronger than the deployment score; the main problem was instruction/budget architecture.

### v5

Installable bundle now contains only:

- `SKILL.md`
- `references/literature.md`
- `references/proof.md`
- `references/verification.md`
- `references/publication.md`

The full v4 wording remains recoverable from Git at the baseline commit and is pointed to by `V4_ARCHIVE_POINTER.md`.

Current conservative budget bounds from GitHub byte sizes:

- `SKILL.md`: 3515 bytes ⇒ estimated invocation cost is at most `ceil(3515/4)=879` tokens, inside the evaluator's **heavy** band but below the 900-token excessive/error threshold.
- four references: 4704 bytes total ⇒ deferred cost is at most `1176` tokens, inside **heavy** but below the 1200-token excessive/error threshold.
- description explicitly begins with `Use when` and includes negative routing for textbook/factual questions.
- progressive disclosure is present through four resolving relative references.
- main file is far below the evaluator's 500/800-line size warnings/errors.

Expected static result under the published scoring rules:

- invoke heavy warning: −4.5
- deferred heavy warning: −4.5
- coverage-unavailable informational check: about −0.25 if emitted
- no structural/error deduction expected

Reconstructed score: about **91 / B / medium risk**.

This is deliberately not pushed to an artificial A by deleting core research behavior. The next optimization should be driven by observed benchmark usage.

## Real-use benchmark

Config: `research/skill-eval/math-research-full-push/benchmark.json`

Six scenarios:

1. Paper/Remark mining: Seed 0 → literature positioning → proof obligation → concrete repo delta.
2. `继续推进`: recover repository frontier without unnecessary clarification.
3. Theorem strengthening: falsify stronger forms, strengthen, then re-check prior art.
4. JCTA-style escalation: simulated referee objections become mathematical obligations and at least one is advanced/closed.
5. Literature/background: targeted prior-art/open-status chain changes theorem or proof strategy.
6. Routine textbook boundary: do not launch a research campaign for an elementary exercise.

Primary quality signals:

- task completion on disk;
- unnecessary clarification count;
- evidence-state mistakes;
- false/open-status or novelty overclaims;
- theorem-strength delta;
- verifier/formal build status where applicable;
- token/tool-call cost;
- boundary overreach.

## Commands for an environment with plugin-eval/Codex CLI

From repository root:

```bash
plugin-eval analyze skills/math-research-full-push --format markdown
plugin-eval benchmark skills/math-research-full-push --config research/skill-eval/math-research-full-push/benchmark.json
plugin-eval analyze skills/math-research-full-push --observed-usage skills/math-research-full-push/.plugin-eval/benchmark-usage.jsonl --format markdown
plugin-eval measurement-plan skills/math-research-full-push --observed-usage skills/math-research-full-push/.plugin-eval/benchmark-usage.jsonl --format markdown
```

## Decision rule for v5.1

Do not compress further merely to gain static points. Change the skill after observed runs show one of these:

- repeated irrelevant reference loading;
- elementary/boundary over-triggering;
- missing research obligations because compact guidance became too weak;
- excessive clarification instead of autonomous continuation;
- theorem strengthening or literature re-check being skipped;
- measured invocation/deferred cost dominating task cost.

If quality holds while cost remains high, compress further. If quality drops, restore only the smallest missing behavior from the v4 archive.
