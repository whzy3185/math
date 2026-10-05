# Audit paper to Lean correspondence and trust

Paper version {{VERSION}}, claim map {{MAP}}, formal snapshot {{SOURCE_HASHES}}, Lean toolchain {{TOOLCHAIN}}, mathlib/dependency revisions and patches {{LOCKFILES}}, build command {{BUILD_COMMAND}}, axiom driver {{AXIOM_COMMAND}}.

Independently read the named final declaration types and expand definitions needed to compare them to the paper. Record the exact mathematical objects and definitions, domains, index conventions, constants, bounds, existence/equality/attainment quantifiers, and every extra hypothesis. Identify conditional statements that assume the main result, weaker statements, omitted endpoints or different objects.

Use a clean build environment at the exact pins. Do not infer success from old logs, source scans or declaration counts. Execute the build and named axiom audit; preserve complete exit status and logs. Check transitive axiom dependencies against the declared trust policy, explicitly rejecting sorryAx or unjustified project-specific axioms. Record compiler/native-evaluation trust separately from small-kernel checking. Source grep is supplementary only.

Return a claim-by-claim coverage matrix with declaration, formal type, semantic match or mismatch, actual build result, axioms, and uncovered portions. If a build fails, distinguish environment failure from a proof failure. If sources/definitions change, invalidate corresponding earlier results and replay. Do not describe a partial checkpoint as formalizing the entire paper.
