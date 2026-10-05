# Uniform Schur bounds for unequal cells in signed cycle squares

Research manuscript, revision 3, 5 October 2026. The article is `manuscript.pdf` (20 pages), with editable TeX and TikZ sources in `manuscript.tex` and `sections/`.

## Contents

- `manuscript.pdf`, `manuscript.tex`, `sections/`: article and figure sources
- `build_environment.sh`: optional workspace-only TeX setup/build helper
- `supplement/certificates/`: 14 raw Python sources for the 13 exact computational checks, including independent replays
- `supplement/run_checks.py`, `supplement/requirements.txt`: dependency-ordered runner and pinned Python dependency
- `supplement/formal/`: the paper's fixed 237-declaration exact-radius checkpoint, audit targets, and pinned Lean build configuration
- `REPRODUCTION.md`: commands and precise formal scope
- `PUBLICATION_INVENTORY.json`, `SHA256SUMS`: relative-path inventory and content hashes

## Scope

The paper proves explicit signed-cycle-square bounds for unequal prescribed cells and related exact finite constructions. It does not determine unrestricted spectral-radius minima or minimizing signings.

Its formal verification claim remains the fixed 237-declaration exact-radius checkpoint. The full Schur/finite-completion proof is not claimed to be Lean verified. Later R2 formalization increments are separate research checkpoints and do not change the paper's verification claim.

The article's frozen supplement citation remains commit `12e3389c07cc5a632023a1f6b972f9baf450a6a0`. The included unequal-cell checker explicitly requires both the order-60 and order-76 strict obstructions and records their complete pivot prefixes. Its exact difference from the archived source, and one non-executable formal-source comment normalization, are recorded in the inventory.

No author name has been added. This research-branch deposit is not a journal submission.

See `REPRODUCTION.md` to build and reproduce from a fresh copy.
