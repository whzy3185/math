# Record formats

The eight JSON Schemas use draft 2020-12. Claims can be maintained as CSV using the provided header, but executable readiness records use the JSON representation embedded in `readiness.schema.json`. CSV list cells should use JSON arrays when exported to JSON, not ambiguous comma splitting.

`workflow_check.py`, `readiness_links.py` and `schema_guard.py` are dependency-free and implement the schemas used here plus consequential cross-record checks (file identity, dependency cycles, review/editor separation, stale versions, context retirement and gate evidence). The fallback schema guard implements only the assertion keywords used in these bundled schemas and rejects unsupported keywords; it is not a general JSON Schema implementation. Optional `jsonschema` provides a second structural check. Separately supplied user records can be checked against the same contracts. Optional `jsonschema` provides an independent structural check.

Evidence paths are relative to the JSON record's directory, stay within it, and contain a SHA256 plus an optional semantic locator. The evidence file can be a manuscript, executable source, exact output, primary-source record, or a signed/sourced human assessment. The program verifies bytes; it cannot verify the truth of the assessment. For a real project, retain source locations and frozen evidence privately or in an explicitly authorized project package. This generic distribution contains only synthetic fixtures.

A `pass` gate needs current version, owner, precise acceptance statement and hash-bound evidence. Missing/not-run work is `pending`; a known obstacle is `blocked`. Only formalization S12 can be `not_applicable`, and only with a reason and named approval. Partial formalization cannot be called not applicable when the paper claims it.

Review context identifiers must identify actual separately created contexts, not an instruction to forget. A contaminated review can retain useful evidence, but cannot satisfy the clean-review gate. After two rounds the context is retired. Response records are separate from neutral input packets.

Templates are intentionally incomplete and cannot pass readiness until populated. Test fixtures exercise an all-pass administrative record, not a real mathematical theorem or journal eligibility.

## Linked readiness contract

Readiness binds a readable input PDF and source files to actual hashes. It also hashes and loads five administrative records: proof obligations, review response, version registry, required inventory and typed receipts. The required inventory freezes claim, obligation and review-issue IDs; missing obligations/issues cannot disappear merely by deleting rows from a response. Treat an inventory change as a new scope/version decision, preserving the old one.

Typed receipts are required for passed policy, computational-audit, mathematical-audit, blind-review, re-review, formal-audit, PDF-QA, archive-replay and authorship-consent gates as applicable. They join to actual context/version IDs, issue closure, the current PDF, and supporting file bytes. Review contexts are unique; historical retirement and round counts cannot reset by relabeling. All nested evidence paths are checked, including symlink parents. False booleans cannot masquerade as zero exit codes.

The program validates the records' internal consistency and byte identities, not the truth or authority of whoever supplied them. It does not authenticate a signature, prove that a reviewer is independent, reread a proof semantically, or establish that a publisher approved anything. A person able to rewrite all records and their hashes can fabricate a coherent story. Preserve an externally pinned version and require actual human signoff. “Ready for human submission decision” means that the required administrative evidence has been consistently recorded; it is not proof, journal acceptance or permission to submit.
