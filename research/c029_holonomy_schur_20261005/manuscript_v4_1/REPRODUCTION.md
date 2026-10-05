# Manuscript and mathematical inputs

The article is `manuscript.pdf`; its editable sources are `manuscript.tex` and `sections/`. `PUBLICATION_INVENTORY.json` records every input file's hash and any source normalization. Copy this packet into a fresh working directory before building or executing programs: generated outputs must not be mixed with the supplied inputs.

## Paper build

Run `bash build_environment.sh` on a compatible TeX Live installation with the Debian package paths used by the helper, or compile `manuscript.tex` twice using an installed pdflatex with the named packages. The helper creates local font/format files without modifying system configuration and fixes `SOURCE_DATE_EPOCH` to 5 October 2026, 08:00 UTC unless overridden. Exact PDF bytes may still depend on the TeX engine, fonts, and absolute build path; the source and mathematical checks are the reproducibility targets.

## Complete computational suite

Use Python 3 and SymPy 1.14.0. The exact SymPy requirement is also in `supplement/requirements.txt`. NumPy is optional and used only for labeled numerical illustrations. All acceptance tests use exact integers, rational arithmetic, or symbolic identities.

These four entry points import SymPy:

- `audit/replay_local_from_direct_graph.py`
- `audit/replay_antiperiodic.py`
- `new_conjecture/verify_antiperiodic_counterexample.py`
- `strengthening/audit/replay_stronger_cap.py`

The other certificate programs use the standard library; `unequal_cells/verify_unequal_cells.py` imports its sibling `assembly.py`.

From the copied packet root, run `python3 supplement/run_checks.py`. Alternatively, change into `supplement/certificates/` and run the following sequence. The analytic producer must precede its two direct-graph replays; the residue-six producer must precede its replay. All four later audit directories and their raw replay scripts are included.

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

Inspect exact acceptance predicates and complete normal execution rather than relying on output labels. Programs write their new certificates beside their sources. The unequal-cell primary checker in this packet requires both the order-60 and order-76 sharper-cap obstructions and stores their complete pivot prefixes. This small source refinement is not claimed to be byte-identical to the earlier public pin; `PUBLICATION_INVENTORY.json` records the upstream and supplied hashes.

## Formal source snapshot

The sources in `supplement/formal/` represent the fixed exact-radius checkpoint: Lean 4.33.1, pinned dependency lockfile, and 237 named axiom-audit targets. From that directory run:

```sh
lake build TargetA.Period8ExactFiniteRadius
lake env lean ExactRadiusAxiomAudit.lean
```

Inspect the theorem statements, their connection to the article, and actual resulting dependencies. Later formal extensions are excluded. One non-executable comment in `TargetA/Period8AntiperiodicBridge.lean` has a redundant evidential qualifier removed; no formal definition, theorem statement, or proof token was changed. This normalization is disclosed in `PUBLICATION_INVENTORY.json`, including the original and supplied file hashes, rather than asserting byte-for-byte source identity.

## External sources

The manuscript links primary literature and immutable predecessor sources. Those linked sources are not bundled; the packet contains the article and its raw mathematical inputs.
