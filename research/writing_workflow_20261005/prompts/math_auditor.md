# Audit exact mathematics and computations

Audit claim IDs {{CLAIMS}} at {{FROZEN_VERSION}} using {{PRIMARY_INPUTS}}. This is a targeted mathematical audit, not necessarily a blind review; record any prior information supplied. Do not edit the source.

Write the exact hypotheses and quantifiers before checking proof steps. Build the dependency graph. For each local lemma, verify that the globally available assumptions are stated at its interface. Check minimum versus minimal, uniqueness, strictness, dimensions, sign conventions, endpoints, empty sets, and multiplicity. Try explicit small counterexamples to weakened hypotheses.

For computation, specify the domain and the reduction proving it sufficient. Rebuild definitions independently if feasible, record shared assumptions with other implementations, prove pruning safe, and use exact acceptance arithmetic. Separate soundness of listed outputs from exhaustive completeness. Require fresh outputs, normal termination and an explicit completion predicate; simulate interruption or an invalid input where appropriate. Keep witnesses or exact negative pivots so failures are inspectable.

Report only what you actually established: Observed, finiteVerified, analyticProved, computerAssistedProved, or PublishedEstablished with provenance. Assess verification status separately. Provide code, input hashes, run environment, output hashes and a short interpretation. A finite experiment must not become an arbitrary-parameter theorem.

For each issue return severity, exact locator, affected claim IDs, evidence, and recovery. Stop a disputed dependency from silently supporting later claims. If resources block completion, identify the exact unfinished domain and return partial results without a success label.
