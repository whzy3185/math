# Task 59 Hostile Submission Review

## Scope

Three independent read-only audits attacked the revision from distinct
angles: title/scope/literature, proof hierarchy/terminology, and rendered
submission packaging. A final local audit then checked the integrated source,
PDFs, manifest, and complete verifier chain.

## Findings and disposition

| Severity | Finding | Disposition |
|---|---|---|
| MAJOR | Original title suggested a complete determination of `m_n` | Replaced by a title about optimality of the twisted signing; theorem scope now says "conjectured equality" |
| MAJOR | Introduction began with the degree-ten `c_6` polynomial and a 15-digit interval | Removed from the introduction; Section 4 and Appendix A retain the certificate |
| MAJOR | Exact-`2r` appeared as a main-paper theorem although unused in classification | Replaced by a short remark; full theorem/proof remains in the supplement |
| MAJOR | Figure 2 was too small and its first Task 59 redraw overlapped after rendering | Rebuilt as a stable two-panel figure with three fixed-width residue columns; rendered output rechecked |
| MAJOR | Anonymous supplement exposed repository identifiers and unique script names | Added a separately compiled anonymous supplement with those fields suppressed |
| MINOR | Truth set was readable only through prose and a long set | Added a compact two-row truth-pattern table |
| MINOR | Main Appendix A read as a certificate dump | Moved raw rational enclosures to a dedicated supplement section; retained proof implications in Appendix A |
| MINOR | Supplement printed a long path/command manifest | Replaced by seven human-readable certificate families and a SHA-256 machine manifest |
| MINOR | Four LaTeX warnings and a sparse anonymous transition page remained | Corrected math-mode font sizing/bookmark text and removed the forced appendix page break |
| MINOR | Defensive use of `exact` obscured the narrative | Centralized the arithmetic convention and reduced main-source occurrences from 107 to 51 |

## Final verdict

- Open MAJOR findings: 0
- Open MINOR findings: 0
- Mathematical conclusions changed: none
- Submission status: `SUBMISSION_READY_MODULO_SUBMITTER_DESIGNATION_AND_ARCHIVE`

The two remaining blockers require external data rather than manuscript work:
submitting/corresponding-author designation and an immutable archive identifier.
