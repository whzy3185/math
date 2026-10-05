# Freeze and validate a mathematical release candidate

Paper {{VERSION}}, authorized local output {{DIRECTORY}}, required claims/supplement {{MAP}}. No publication or submission authority is included by this prompt.

Produce two separate bundles: a neutral mathematical review packet, and an administrative evidence bundle. The mathematical packet contains only the final paper/PDF, raw mathematical sources/data, executable producer/checker code, neutral reproduction instructions and identity metadata. Exclude prior conversation, reports, responses, verdicts, saved success outputs and remote-verification statuses, including verified_via. Preserve original inputs and record explicit sanitization transformations outside the packet; never alter mathematical evidence to hide a defect.

Use explicit file allowlists and SHA256 hashes. Run make_packet.py/workflow_check.py, then inspect all filenames, source comments, JSON metadata, PDF text/metadata/links and visible source landing pages for exposure. If a reviewer has already seen status information, regenerate the packet and use a new context; do not reset its label.

Build the paper from frozen source, inspect every page, and replay indispensable computations from freshly unpacked inputs. Check output semantics, exit statuses and interruption behavior. Verify anonymous retrieval only if public release is already authorized and claimed. Record local mathematical readiness, venue-policy compatibility, and publication/submission permission separately.

Return immutable file identities, exact entry-point commands, complete validation evidence, unresolved gates and the next authorized action. Never treat your manifest or validator output as a mathematical proof.
