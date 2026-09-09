# Formal / computational verification mode

Lean is a second proof channel, not decoration. Formalize definitions → central reduction/invariant → structural theorem → main theorem → equality/corollaries. “Lean-verified” requires statement alignment, no sorry/admit/smuggled axiom, and a successful build in the repository toolchain with command/commit recorded. Extra assumptions discovered by Lean trigger a human-proof audit; stronger formal statements feed back into theorem strengthening and literature recheck.

Computer-assisted proof maturity: CAP0 exploratory; CAP1 exact bounded observation; CAP2 proved finite reduction; CAP3 exact endpoint/decision principle; CAP4 independent generator/verifier plus completeness/coverage equality; CAP5 deterministic frozen package with commands, versions, outputs and hashes.

Use exact arithmetic where possible. A smallest-counterexample claim needs complete coverage of all earlier cases. The main paper owns the mathematical reduction; implementation QA belongs in the supplement.