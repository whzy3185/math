# Target A Reviewer Three Major-Revision Report

Date: 2026-08-21

Role: independent spectral graph theory referee

Recommendation: **MAJOR REVISION**

Severity counts: **BLOCKER 0 / MAJOR 1 / MODERATE 4 / MINOR 2**

## Overall Assessment

The mathematical core is strong and, on the evidence reviewed, internally
coherent. I found no error in the order-32 exact witness, the finite/infinite
Floquet interface, the sharp period-eight edge, the one-way moment argument,
the period-eight trichotomy, or the bounded period-16 classification. The new
large-order computation also materially closes the earlier trust gap: exact
representative-set equality and a separately implemented spectral-decision
route now cover `n=24,26,28,30`.

The paper is nevertheless not yet a publication-ready Major Revision. Its
current reproducibility claim points to an old immutable snapshot that does not
contain the strengthened evidence described in the manuscript. The theorem
core appears sound, but the submitted-artifact claim is presently false as a
matter of repository provenance.

## Findings

### MAJOR 1: The cited immutable proof artifact does not contain the revised evidence

The computational section calls `c81be34...` the submitted proof artifact
(`sections/10_computational_verification.tex`, lines 132--149), and the
computational appendix and Data and Code Availability section repeat that URL
(`appendices/14_appendix_computation.tex`, lines 5--20;
`sections/12_data_code_availability.tex`, lines 3--10). That commit predates the
new C scanner, independent spectral audit, four-order evidence, strengthened
gate, revised manuscript, and high-period experiment.

The old submission manifest is also semantically incompatible with the revised
paper: it still limits recordwise independent generation to `n=24` and labels
`n=26,28,30` aggregate-only
(`target_a_submission_artifact_manifest.json`, lines 19--28 and 144--147).
Meanwhile, the strengthened manifest records HEAD `98f9815...`, but the files it
authenticates are currently uncommitted and therefore are not retrievable from
that commit (`target_a_computational_evidence_manifest.json`, lines 1--13).

Required resolution:

1. Commit the reviewed code, evidence, manifests, reports, and synchronized manuscripts.
2. Rebuild the submission manifest so its semantic claims and file inventory include record-level and independent spectral checks through `n=30`.
3. Pin both manuscripts to a commit that actually contains all named artifacts.
4. Make the submission-manifest verifier reject the obsolete `n=24` limitation.
5. Rerun the two manifest verifiers, top-level minimality gate, LaTeX gates, and independent reviews against that exact commit.

### MODERATE 1: The proof prose says vectors are stored although the artifact regenerates them

The finite-exclusion proof says that the enumeration "stores a nonzero rational
vector" for every nonoptimizer (`sections/04_smallest_counterexample.tex`,
lines 130--140). The computational disclosure correctly says that the
large-order vectors are not archived individually and are instead regenerated
by two routes (`sections/10_computational_verification.tex`, lines 163--173).

Required resolution: replace "stores" by "constructs" or "generates and
verifies", then state exactly what is persisted: counts, ordered decision
digests, checkpoint chains, and the zero-uncertified summaries. This removes a
material ambiguity about the proof object without changing the theorem.

### MODERATE 2: The exact coverage claim for the period-17--24 experiment has only a same-route check

The experiment labels the orbit and moment counts exact, but its coverage test
only checks that orbit sizes emitted by the same FKM-style generator sum to
`2^(p-1)` (`target_a_high_period_exploration.py`, lines 165--189 and 243--248).
Its regression test exercises only period 8
(`test_target_a_high_period_exploration.py`, lines 10--18). An implementation
error could, in principle, exchange omitted and duplicated orbits while
preserving the weighted total.

This does not threaten any theorem because the section is explicitly
non-theorem. It does affect the claim that all displayed exact counts at
`p=17,...,24` are certified.

Required resolution: compare the eight orbit counts with an independent
Burnside implementation, and preferably compare canonical sets by a direct
visited-orbit route through at least `p=23` while reusing the existing C
record-level result at `p=24`. Add a regression test covering the archived
eight-period table.

### MODERATE 3: The novelty language is more categorical than the literature audit

The Introduction calls the result "the first counterexample"
(`sections/02_introduction.tex`, lines 54--64), while its public-status section
and literature audit correctly disclaim absolute priority. A refreshed narrow
search again found the source preprint and no direct public resolution, but that
does not prove priority.

Required resolution: write "an explicit counterexample" or "to the best of our
knowledge, the first counterexample", with the dated bounded-search qualifier
nearby. The structural contribution, not priority over a very recent preprint,
should remain the central novelty claim.

### MODERATE 4: Review bookkeeping does not yet describe the current state

The Major Revision plan still marks R2--R7 as `PENDING` and R1 as review pending
even though the corresponding prose, figures, experiment, and technical audit
are present (`TARGET_A_MAJOR_REVISION_PLAN.md`, lines 14--22). The latest Compute
Re-review still lists a missing verifier-source binding, although that source,
its test, and its builder are now present in the strengthened manifest and the
verifier is present in the minimality dependency graph.

Required resolution: update the response matrix and Compute Re-review after the
final artifact commit. Each review item should point to the exact committed
evidence and the command that verifies it; do not leave a stale finding as the
formal final review record.

### MINOR 1: The chiral subsection contains three notation/reference defects

In `sections/07_eight_barrier.tex`, line 212 typesets `xi` rather than `\xi`,
line 227 writes `C=B*` rather than `C=B^{\ast}`, and lines 229--231 hard-code
"Section 6.4" instead of using the labeled subsection reference. These do not
affect the argument, but they are visible publication defects.

### MINOR 2: Submission metadata remain placeholders

The nonanonymous front matter, funding, acknowledgments, and archive identifiers
still contain bracketed placeholders. This is acceptable during revision but
must be resolved or intentionally omitted before any journal submission. No
mathematical status should be inferred from the current generic/JGT/SIDMA
wrappers.

## Technical Verification

The following high-risk interfaces passed review:

- **Finite minimality:** the C full-space route checks every canonical `Q` record and orbit size at `n=24,26,28,30`; the second Python route reconstructs both holonomies and exactly excludes every nonoptimizer. The shared quotient and library risks are disclosed.
- **Zone folding:** the identity `H_(mq)(z) ~= direct_sum_(w^m=z) H_q(w)` is proved with multiplicities and used correctly for the repeated period-8 rows.
- **Finite versus infinite fibers:** finite order uses only `z^L=alpha`; infinite periodic radius uses all `|z|=1`. I found no substitution of one domain for the other.
- **Moment logic:** every theorem use is `F_k>0 => R(Q)>8`; nonpositive excesses are never used as upper bounds.
- **Period-eight trichotomy:** defect counts `0,2,4,6,8`, all two-defect separations, and the `d>=4` cases are disjoint and exhaustive. The antipodal case is the target orbit.
- **Theorem scope:** the paper does not claim all-period, nonperiodic, all-signing, or all-even-order optimality beyond the stated finite domains.
- **Related work:** the revised introduction now covers signed spectra, signing/lift problems, circulants, periodic magnetic operators, trace methods, and computer-assisted exhaustion. No direct public conflict was found in the bounded refresh.
- **Periods 17--24:** the manuscript clearly labels the calculation experimental, identifies finite-grid values as numerical only, and recognizes the period-24 repetition by exact zone folding. It does not promote the exploration to a theorem.

## Referee Executions

No full `n=30` enumeration or spectral job was rerun.

| Check | Result |
|:---|:---|
| Targeted independent-computation, zone-folding, period-8, and moment tests | `52 passed` |
| Updated strengthened-evidence and top-level minimality tests | `8 passed` |
| Top-level minimality verifier with checkpoint replay disabled | `SMALLEST_COUNTEREXAMPLE_VERIFIED` |
| Exact `n=32` witness verifier | PASS |
| Sharp period-8 edge and structural-core verifiers | PASS |
| General-period moment verifier | PASS |
| Low-period spectral and structural frontier verifiers | PASS |
| English publication source/build gate | PASS; zero undefined citations/references and zero overfull boxes |
| Public direct-result refresh | no direct conflict found; bounded search only |

## Final Verdict

The mathematical and computational theorem core has **BLOCKER 0**. The former
large-order Compute Review MAJOR findings are substantively resolved. The
current package still has **MAJOR 1** because its advertised immutable artifact
does not contain the evidence on which the revised credibility claim relies.

After that provenance chain is rebuilt and the moderate/minor items are
closed, Reviewer Three should perform a short final re-review against the pinned
commit. No additional full `n=30` run is required for those repairs.
