# C029 manuscript increment

Read manuscript.pdf for the complete English mathematical increment. The canonical editable source is manuscript.tex with sections/*.tex; manuscript.md is a generated reading copy. HANDOFF.zh-CN.md explains the substantive changes and integration boundaries in Chinese. CLAIM_LEDGER.md and PROOF_DEPENDENCY_MAP.md distinguish the inherited exact formula, its application to the September conjecture, the newly closed residue-two proof, and the remaining formal/global-optimality gaps.

This is a review package, not a submitted manuscript. It supplies no new certification of the historical all-even classification and makes no publication-priority claim. The restored files and fresh build are distinguished from the pre-reset artifacts in RECOVERY.md.

## Package layout

The package root has manuscript/ and certificates/ as sibling directories. The certificate subdirectories analytic/, audit/ and new_conjecture/ preserve the relative paths required by their scripts. All paths mentioned in the manuscript's reproducibility paragraph are relative to the package root.

## Reproduce the manuscript

From manuscript/, run pdflatex -interaction=nonstopmode -halt-on-error manuscript.tex twice on a normal TeX Live installation. The optional build_environment.sh fallback uses installed TeX packages when the system's format and font-map databases are missing; it is not a network installer.

## Reproduce exact checks

From the package root run:

- python3 certificates/analytic/verify_r2_certificate.py
- python3 certificates/audit/replay_direct_graph_seed.py
- python3 certificates/audit/replay_local_from_direct_graph.py
- python3 certificates/new_conjecture/verify_antiperiodic_counterexample.py
- python3 certificates/audit/replay_antiperiodic.py

From manuscript/, prefix these certificate paths with ../ instead. The first two scripts use only Python's standard library; the symbolic verifiers require SymPy. Numerical illustrations, where present, are not exact acceptance conditions.

The residue-two proof requires the rational premises in Appendix A, seven bases and the normalized n106 seed. The recovered standard-library verifier freshly reproduced all124 required checks. Both independent graph-based scalar-Schur replays were restored and freshly passed. The antiperiodic verifier freshly checked all64 positive integer principal minors and the exact characteristic identities. See the individual JSON outputs and recovery records for their exact scope.

## Formal verification

Lean validation is separate. Do not infer graph-level formalization from a scalar or fiber theorem. In particular, the raw negative-holonomy graph-to-cell bridge and the residue-two argument are outside the current formalized scope. A verified build report may update the partial-module status without changing these boundaries.

## Sources

The manuscript cites exact current arXiv versions and the frozen inherited period-eight formula in the project repository. Third-party full papers are not redistributed. After a workspace reset, the manuscript was reconstructed from its retained textual copy and rebuilt; the manifest records hashes of actual recovered files.
