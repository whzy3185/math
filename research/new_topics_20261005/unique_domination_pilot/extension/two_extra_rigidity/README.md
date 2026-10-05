# Addendum on equality at the second boundary

This addendum completes the equality classification for the sharp edge bound at n=3γ+2. It is a separately reviewed addition to the ten-page paper_v2; that published manuscript is preserved unchanged.

For finite simple bipartite graphs without isolated vertices, with a unique minimum-cardinality dominating set of size γ≥2 and exactly ceil(γ²/2)+5γ edges, the full graph-isomorphism class counts are:

- γ=2: three classes, H₂(1,1) and two explicitly described balanced eight-vertex exceptions F₀,F₁
- Odd γ=2k+1≥3: exactly H₂(k+1,k)
- Even γ=2k≥4: exactly H₂(k,k) and H₂(k+1,k−1)

All are connected. RIGIDITY_THEOREM.md supplies the complete elementary proof and graph definitions. The independent proof and exact-isomorphism audit passed; see audit/PROOF_AUDIT.md. Finite checks supplement the proof and are not unrestricted graph censuses. The prior examples and q=1 construction retain their existing attribution. No broad publication-priority claim is made.

Run python check_rigidity.py for the primary certificate and python audit/independent_rigidity.py for the independent check. The audit additionally includes a complete small private-pair skeleton census. Its C++ source is included; the platform-specific executable is unnecessary for publication.
