# Reproduction

All paths below are relative to this directory. Copy the directory before executing programs, because generated certificates are written beside their sources. `PUBLICATION_INVENTORY.json` records the selected inputs; `SHA256SUMS` covers the payload and inventory.

## Build the paper

Use pdfLaTeX with the packages named in `manuscript.tex` (including AMS packages, mathtools, booktabs, lmodern, microtype, TikZ, xurl, and hyperref):

```sh
pdflatex -interaction=nonstopmode -halt-on-error manuscript.tex
pdflatex -interaction=nonstopmode -halt-on-error manuscript.tex
```

The optional `bash build_environment.sh` helper supports the compatible TeX Live filesystem layout using local format/font-map files. It does not change system configuration. The supplied PDF is the frozen 20-page revision; PDF timestamps can make a rebuild differ byte-for-byte.

## Exact computational suite

Use Python 3 with SymPy 1.14.0, as pinned in `supplement/requirements.txt`. NumPy is optional for labeled numerical illustrations; acceptance predicates use exact integers, rationals, or symbolic identities.

```sh
python3 -m pip install -r supplement/requirements.txt
python3 supplement/run_checks.py
```

The runner executes all 13 commands below in dependency order. Alternatively, run them from `supplement/certificates/`:

```sh
python3 analytic/verify_r2_certificate.py
python3 audit/replay_direct_graph_seed.py
python3 audit/replay_local_from_direct_graph.py
python3 new_conjecture/verify_antiperiodic_counterexample.py
python3 audit/replay_antiperiodic.py
python3 strengthening/verify_uniform_cap.py
python3 strengthening/audit/replay_stronger_cap.py
python3 r4_pilot/verify_r4_pilot.py
python3 r4_pilot/audit/replay_r4_phase.py
python3 unequal_cells/verify_unequal_cells.py
python3 unequal_cells/audit/independent_assembly.py
python3 r6_completion/verify_r6_completion.py
python3 r6_completion/audit/replay_r6.py
```

The analytic producer must precede its two direct-graph replays, and the residue-six producer must precede its replay. The four SymPy-importing entry points are `audit/replay_local_from_direct_graph.py`, `audit/replay_antiperiodic.py`, `new_conjecture/verify_antiperiodic_counterexample.py`, and `strengthening/audit/replay_stronger_cap.py`. The unequal-cell producer imports its sibling `assembly.py`.

Inspect complete normal execution and the exact acceptance predicates. In particular, the unequal-cell primary checker requires both the order-60 and order-76 sharper-cap obstructions and stores their complete strict pivot prefixes. The inventory distinguishes this refinement from the archived supplement source.

## Fixed formal checkpoint

Use Lean 4.33.1 and the pinned dependency lockfile in `supplement/formal/`. From that directory:

```sh
lake exe cache get
lake build TargetA.Period8ExactFiniteRadius
lake env lean ExactRadiusAxiomAudit.lean
```

`ExactRadiusAxiomAudit.lean` contains 237 named audit targets. Inspect the resulting axiom dependencies and theorem statements. This snapshot formalizes the exact-radius checkpoint only; it does not formalize the entire article's Schur/finite-completion argument. Later formal additions are separate checkpoints. The inventory records a non-executable introductory-comment normalization in `TargetA/Period8AntiperiodicBridge.lean`; no formal definition, statement, or proof token was changed.
