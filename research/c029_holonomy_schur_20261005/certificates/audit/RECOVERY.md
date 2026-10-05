# Audit evidence recovery

Date: 2026-10-05 UTC.

All eight original audit files were restored from recorded source text and verified byte-for-byte against their original SHA-256 values. Three neutral editorial substitutions were then made in the reports and an antiperiodic script docstring. No executable instruction or mathematical statement changed. Original and current hashes are distinguished in `recovery_manifest.json`.

All three independent checks were freshly rerun successfully after restoration:

- Direct full-graph scalar Schur elimination at n=50,58,66,74,82,90,98,106, including the normalized n=106 seed margin and exact agreement with the primary recurrence certificate
- Direct-graph entrance extraction after 96 scalar eliminations, followed by all P/Q, residual, and response premise checks
- Algorithmic antiperiodic graph/Bloch construction, exact symbolic identities, and exact Fraction scalar LDL for both 279I+100A and 279I-100A at n=32

All three regenerated certificate JSON files exactly match their original hashes. Fresh stdout files are included separately. The two R2 scripts also retain their original hashes; the antiperiodic script has a new hash solely because of the docstring edit.

Run the scripts with Python 3. `replay_direct_graph_seed.py` uses only the standard library. The other two scripts additionally use SymPy. The R2 scripts expect the sibling `../analytic/r2_exact_certificate.json` file. The independent antiperiodic entry point is `replay_antiperiodic.py` in this directory.

See `SHA256SUMS` for the final delivery hashes. This recovery does not alter or extend the proved mathematical claims.
