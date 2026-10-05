# Reproduction and validation

## Toolchain and dependencies

Use official Lean **4.33.1**, commit `819816b2e0a3bf405af45ae5c7af2491d8f5bee6`. Mathlib is pinned to `0df444a360eaa60ab8c11dca51a86af692955474`. Preserve `dependencies/lake-manifest.json`, which pins all transitive repositories. From `dependencies/`, obtain the official packages and cached Mathlib artifacts with the matching Lake installation:

```sh
lake exe cache get
```

This needs network access to the official dependency repositories/cache and sufficient disk/memory. The replay used already available matching third-party caches; downloading these afresh was not tested during publication.

## Fast, fresh structural and typed replay

From this directory, run:

```sh
python3 reproduce/validate_package.py
python3 reproduce/replay_structural.py --lean lean
```

Alternatively, point `--cache-project` at a project whose `.lake/packages` contains the exact pinned revisions. The runner verifies each dependency checkout's revision, ignores all prior project objects, creates one new output root, and compiles in order:

1. `C029OpenSchur`
2. `TargetA/R2TerminalSchur` (import-only overlay)
3. `TargetA/R2RationalRecurrence` (byte-identical original)
4. `TargetA/R2GenericSchurBridge`
5. `C029BoundaryIncidenceEstimate`
6. `C029InnerProductCrossEstimate`
7. `C029AssembledQuadraticPositivity`
8. `C029FlattenedMatrixPosDef`

Each direct Lean invocation uses one compiler thread, a 90-second wall limit, fresh `.olean` and `.ilean` outputs, and complete inline axiom-name validation. The final report is `.repro/structural/replay.json`. The output directory must be new; use `--out` to select another directory for a later attempt. A nonblocking compiler lock prevents overlapping runs. Failed/timed-out runs remain failed, with diagnostics retained in their output directory.

The finite and structural profiles deliberately have distinct `TargetA` roots. Do not mix their project objects. The terminal overlay changes only import lines; `validate_package.py` compares the proof bodies directly to the original finite source, and also checks that the recurrence source is byte-identical.

## Finite chain: cumulative evidence versus a fresh rebuild

The exact sources, pinned dependencies, certificate input, named audit programs, and 607-name cumulative ledger are supplied. The portable direct route is `python3 reproduce/replay_finite.py` (plan only), followed by `python3 reproduce/replay_finite.py --execute --lean lean` when ready for a potentially expensive source rebuild. Add `--audit` only to attempt the monolithic audit after the source build; this aggregate route previously did not complete. The runner compiles the full import closure serially into a new complete namespace, reusing only pinned third-party caches. This clean dependency-first route does not need a compiler setup JSON, but has not been executed for the full finite chain here. During publication, source hashes, import closure, the exact expected name set, standard-axiom restrictions, and the final 3/5/7 inline report groups were checked. **No clean-room numerical-chain rebuild and no fresh monolithic 607-name audit are claimed.**

The previously successful route built the earlier base through `TargetA.R2FourthStepCertificate` with Lake, then compiled the later recurrence certificates sequentially with official Lean's full-artifact argument shape:

```sh
lean SOURCE -o FRESH_OLEAN -i FRESH_ILEAN -c FRESH_C --setup CHECKED_COMPILER_INPUT --json -j 1
```

Use a complete isolated `TargetA` namespace: Lean resolves a namespace using the first matching search-path root, so a partial overlay must not hide older required modules. Preserve the canonical compiler setup's package/options/module mode/plugins/dynlibs and every nonproject import mapping. For each successive module, update the module name, map already checked project imports to their byte-identical isolated artifacts, and add the newly compiled predecessor. Never fabricate a successful Lake build trace. Hash sources, setup and imported project artifacts before and after each run; require clean termination and fresh full outputs.

The measured terminal modules used a 180-second hard limit and a 150-second review threshold, passing in approximately 117.284, 139.786 and 115.609 seconds. The fresh terminal 15-name aggregate import later failed within its separate bound. A complete new numerical rebuild may require substantial memory and time, and must be reported as a new run with its own success/failure evidence. The audit programs alone are not evidence of their successful execution.

The successful 607-name route reconciles prior disjoint 592-name reports with the final inline 3/5/7 reports and verifies every name exactly once. `finite/formal/R2FiniteSeedAxiomAudit.lean` defines the authoritative expected set. `evidence/finite607_coverage.json` preserves the coverage basis and the failed-new15 status. Do not reinterpret its 51 closed equality premises as all finite inequalities or a proof of the full R2 theorem.
