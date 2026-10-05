# Unique domination in bipartite graphs of order 3 gamma plus 1

This directory contains a complete English research paper, its editable LaTeX source, and a Chinese handoff.

The main theorem determines the maximum edge count as gamma(gamma+7)/2 for all gamma>=2 and classifies the extremal graph uniquely up to isomorphism for gamma>=4. It yields connected counterexamples to the n=3gamma+1 specialization of Koch–Narayan's Conjecture 1. The proof is elementary; finite checks are supplementary.

Files:

- manuscript.pdf — final 7-page paper, compiled and visually checked
- manuscript.tex — complete editable source
- HANDOFF.zh-CN.md — theorem, scope, source comparison, proof mechanism and reproduction notes in Chinese
- SOURCE_STATUS.md — version-fixed citations and bounded current-source check
- QA_REPORT.md — build, visual and mathematical alignment checks
- build.sh — workspace-local TeX build recipe
- PAPER_MANIFEST.json — SHA-256s of delivery files

Run bash build.sh from this directory. On a standard complete TeX Live installation, two runs of pdflatex manuscript.tex also suffice. The build script can recreate its local format and font map from the installed distribution, without changing system configuration.

The proof and independent finite audit are in the parent directory and audit/. The author and affiliation metadata remain unfilled. No journal submission or external author contact has been made.

The manuscript now credits Erlbacher’s earlier public n=13 counterexample package; see SOURCE_STATUS.md and ../extension/prior_work/. Its main result is the sharp all-gamma boundary theorem.
