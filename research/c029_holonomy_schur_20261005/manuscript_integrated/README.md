# Uniform Schur bounds and holonomy in signed cycle squares

This is the integrated English manuscript for the C029 continuation. The earlier manuscript/ version remains a separate frozen checkpoint. The present version puts the common two-energy Schur mechanism, unit-phase bound, unequal-cell assembly and complete finite residue coverage into one self-contained mathematical exposition.

The main claims are explicit witness bounds. They do not determine the unrestricted signed spectral minimum or classify minimizers. The witness range at orders32,40 and all even orders≥48 is inherited; the contribution of this increment is the common analytic mechanism, improved quantitative bounds and directly verified constructions.

## Contents

- manuscript.tex and sections/: canonical editable source
- manuscript.pdf: compiled English paper
- manuscript.md: generated reading copy
- CLAIM_LEDGER.md: exact statements, hypotheses, evidence and provenance
- PROOF_DEPENDENCY_MAP.md: complete proof chain and finite coverage
- HANDOFF.zh-CN.md: Chinese mathematical and editorial handoff
- MANIFEST.json: final file hashes and actual verification status

The paper gives the exact period-eight spectrum and its application to arXiv:2607.17343v2 Conjecture28; a one-cell cap790537/100000 for all positive cell parameters and a10^-6 supremum bracket; two uniform bounds for any number of unequal legal cells; full residue-two, residue-four and residue-six witness constructions; and exact short-cell obstructions to overstrong sharp-cap claims.

## Build

From this directory run pdflatex -interaction=nonstopmode -halt-on-error manuscript.tex twice. The optional build_environment.sh uses installed TeX files to work around missing system format/font-map databases; it does not install software. Final compilation, rendered-page checks and the independent manuscript review are recorded in MANIFEST.json after completion.

## Reproduce exact verification

The package root contains manuscript_integrated/ and certificates/ as siblings. From the package root run:

- python3 certificates/analytic/verify_r2_certificate.py
- python3 certificates/strengthening/verify_uniform_cap.py
- python3 certificates/r4_pilot/verify_r4_pilot.py
- python3 certificates/unequal_cells/verify_unequal_cells.py
- python3 certificates/r6_completion/verify_r6_completion.py

Keep assembly.py next to the unequal-cell verifier. The primary programs use Python integers and Fraction arithmetic for acceptance. Each package preserves its independent replay under audit/; some symbolic replays additionally require SymPy. Their README or audit report supplies exact commands. Use ../certificates/ when running from this manuscript directory.

The analytic certificate supplies the fixed rational premises at cap7.92. The strengthening certificate supplies separately verified premises at cap7.90537. The other packages certify geometric identities, the finite bases and negative-pivot obstructions; they do not replace uniform proofs by finite sampling.

## Formal verification checkpoint

The verified Lean4.33.1 exact-radius extension proves the complete negative-holonomy finite radical formula for every positive cell count on the original raw graph matrix. It proves both the upper bound for every Hermitian eigenvalue modulus and attainment at the positive radical. The seam, raw/reverse operator bridges, maximal phase, determinant root and attainment are included. The completed audit at09:12:30UTC on5October2026 covers237 theorem declarations with only propext, Classical.choice and Quot.sound in their axiom union.

The separate quartic identification naming the conjectured constant, the finite-size asymptotic coefficient, the n32 integer certificate, all Riccati/Schur arguments, and R4/R6 completion are not formalized by this checkpoint. They retain their analytic or exact-certificate evidence. The latest verified formal report supplies theorem names, commands and pinned dependencies.

## Scope and provenance

The exact period-eight formula is inherited project work; its application targets the September22 revised conjecture. The original all-even failure range is not presented as a newly discovered truth set. In residue four at odd k and residue six when3 does not divide k, the legal-cell placements can differ from earlier balanced-gap constructions; the finite graphs used here were rebuilt directly.

The proof uses no historical interface-mode count, physical G6 edge estimate or IMS localization theorem as a black box. It does not certify smaller-order equality cases or supply a universal lower bound over all triangle words. No journal acceptance, publication-priority, or literature-exhaustiveness claim is made.
