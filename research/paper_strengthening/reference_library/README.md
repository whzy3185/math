# Canonical reference library for the period-eight paper

This directory is the authoritative reference index for the JGT-first
period-eight manuscript.  It organizes metadata and citation decisions without
moving or deleting the older `research/related_work/` archive.

## Collections

| collection | purpose | may appear in manuscript bibliography? |
|---|---|---|
| `manuscript_core` | sources that support a statement actually made in the paper | yes; currently 15/15 cited |
| `jgt_structure_corpus` | full-text JGT papers used to determine section and proof architecture | no, unless a later mathematical claim independently requires one |
| `reserve` | legitimate, verified sources whose present role is redundant or outside the final scope | not by default |
| `specific_recent_context` | the Suvagiya preprint, isolated from the mature background | yes, once and late in the Introduction |

The complete index is `MASTER_REFERENCE_INDEX.csv`.  The canonical core BibTeX
is `bibliography/manuscript_core.bib`; the manuscript carries a synchronized
copy at `../manuscript_period8_jgt/references.bib` so that its source package
remains self-contained.

## Decision rule

A reference enters `manuscript_core` only if it has all three:

1. verified bibliographic metadata;
2. one nonredundant mathematical role;
3. at least one citation context recorded in `CLAIM_REFERENCE_MAP.md`.

Journal-style exemplars do not count as mathematical evidence.  A paper is not
retained merely because it is recent, highly cited, or topically adjacent.

## Files

- `MASTER_REFERENCE_INDEX.csv`: one row per unique work and its editorial decision.
- `bibliography/manuscript_core.bib`: canonical 15-entry BibTeX file.
- `CLAIM_REFERENCE_MAP.md`: exact claim/function assigned to every cited source.
- `ACCESS_AND_FULLTEXT.md`: local full-text inventory and authoritative landing pages.
- `JGT_STRUCTURE_CORPUS.md`: compact index of the ten full-text architecture exemplars.
- `RESERVE_AND_EXCLUDED.md`: why verified sources are not currently cited.
- `VERIFICATION_LEDGER.md`: metadata and manuscript-sync audit status.
- `verify_reference_library.py`: deterministic uniqueness, scope, path, and sync checks.

## Maintenance workflow

1. Add or change one row in `MASTER_REFERENCE_INDEX.csv`.
2. If promoted to `manuscript_core`, add a fully verified BibTeX entry and a
   claim map row.
3. Synchronize the manuscript copy.
4. Run `python3 verify_reference_library.py`.
5. Run the manuscript integrity check before submission.

Do not edit the old `research/related_work` metadata to force agreement with
this paper.  That directory records earlier scopes and remains a provenance
archive.
