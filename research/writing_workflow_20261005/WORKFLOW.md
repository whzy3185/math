# An executable workflow for mathematics papers

Version 1.0 • Generic public edition

This operating procedure takes a mathematical question through evidence, exposition, independent review, reproducibility and a human submission decision. It defines sixteen stages, role separation, reusable prompts, typed records and conservative validation. This public edition contains no real manuscript, private source inventory, project identifier, review history or research receipt.

The official publisher and technical guidance in `PRIMARY_SOURCES.md` supports bounded requirements. The stage sequence, two-round context limit, separate-editor rule and record contracts are this toolkit’s recommendations. They are not universal journal policies. `SYNTHETIC_DEMO.md` demonstrates the method using elementary arithmetic and explicitly invented administrative fixtures.

## How to run a paper through the workflow

1. Give the paper an immutable version identifier and copy the templates. Populate the claim ledger before polishing the abstract.
2. Check S00 before target-specific drafting, then work through stages S01–S08. Parallelize literature verification, mathematical attacks, and formalization only after agreeing on the exact statement version.
3. Freeze an allowlisted manuscript and mathematical-input packet. Keep review history and administrative evidence outside it. Run `scripts/workflow_check.py packet`; then inspect the whole packet manually. Passing the scanner alone is insufficient.
4. Create a genuinely new review context for S09 using `prompts/blind_initial.md`. A different editor performs S10. A context can review at most two rounds; a new context starts blind even if the project is on version 17.
5. Re-run affected checks and freeze the new version. Use S11 for re-review and S12–S14 for formalization, PDF, and supplement. These can run in parallel, but the final hashes must agree.
6. Run `scripts/workflow_check.py readiness /path/to/your/record.json` or a completed local record. Exit 2 means at least one gate is blocked; it is not a failed theorem. Resolve or explicitly scope out the blocker before submission readiness.
7. S15 produces a human decision packet. There is no automatic journal submission, author assignment, acceptance claim, merge, or public release.

## Evidence vocabulary

Every substantive claim has a stable ID, exact statement, hypotheses, quantifiers, dependencies, source locator, evidence kind, verification state, and scope exclusions. Do not use a single unqualified word such as “verified” across these categories.

- **Observed**: a numerical, exploratory, empirical, or otherwise unproved pattern. Record precision, sample, seed, and search domain. It may motivate a conjecture; it is not a theorem.
- **finiteVerified**: an exact checked assertion over a specified finite domain. Record the complete domain, acceptance predicate, algorithm, environment, termination, and outputs. A finite witness can prove an existential claim once its encoding and exact predicate are justified; a finite search cannot alone prove an unbounded universal statement.
- **analyticProved**: a complete mathematical argument establishes the stated quantifiers without indispensable finite computational premises. Independent audit state remains separate; a proof's existence and a reviewer having checked it are different facts.
- **computerAssistedProved**: a mathematical reduction plus exact computational premises establishes the stated claim. The reduction, complete domain, safe pruning, arithmetic model, and successful exact run are all necessary. Program agreement alone is insufficient.
- **PublishedEstablished**: a result is attributed to a verified published primary source with a precise theorem/page and matching hypotheses. Publication is provenance, not an infallibility guarantee. A preprint or unpublished project predecessor remains explicitly so and should use its actual evidence kind with publication status `preprint` or `unpublished`.

These are evidence categories, not an automatic maturity ladder. Separate fields record `verification_state` (`unreviewed`, `audited`, `disputed`, `blocked`) and `novelty_status` (`not_assessed`, `inherited`, `bounded_search_no_match`, `overlap_unresolved`, `new_contribution_proposed`). “No match found” never becomes a proof of novelty. A hash establishes byte identity, not correctness; a screenshot establishes appearance, not proof; a Lean compile establishes a formal statement under its dependencies, not its correspondence to the prose.

## Roles and separation

- **Research owner**: decides scope, interprets the problem, maintains the theorem ledger; remains responsible for content and actual authorship.
- **Literature auditor**: opens closest primary sources, records positive overlaps and inaccessible leads, and verifies bibliographic metadata.
- **Mathematical auditor**: attacks claims, checks local hypotheses and global quantifiers, and independently reconstructs critical examples or computations.
- **Writing reviewer**: recovers the question, result, mechanism, and boundary from the frozen paper before seeing the author's explanation. Can be the same isolated reviewer as the mathematical referee, but must report the two assessments separately.
- **Revision editor**: a DIFFERENT executor/person/context from the reviewer, receives the issues after the report is locked, and produces a new version and response. The reviewer never silently edits the assessed manuscript.
- **Formalization auditor**: checks statement correspondence, exact toolchain and dependencies, clean compilation, and axiom output. This can run early to expose a statement mismatch.
- **Release/QA custodian**: builds the packet, verifies final files and public accessibility, and records immutable identities. Cannot certify a proof by changing a status flag.
- **Human authors/corresponding author**: approve authors, affiliations, disclosures, journal, final text, and submission. No names or consent are invented.

One person can fill some roles for a small project, but the reviewer–editor distinction and genuinely fresh blind contexts are mandatory for this project. Computational independence is also substantive: disclose shared reductions, graph labels, libraries, expected lists, and code. Different prompts to the same code do not create independent implementations.

## Stage contracts

Each stage ends with a recorded artifact and an explicit gate decision. A failed gate routes to the stated recovery; it never disappears because the prose is improved.

### S00 Intended venue and AI use compatibility

**Input:** candidate venue(s), actual research/writing history, intended tools and who will write each section. **Owner:** human research owner and policy-aware editor. **Output:** dated official-policy record and a compatibility decision before target-specific drafting.

**Work:** read the publisher and journal policies at their official URLs. Record permitted research, coding, drafting, editing and figure uses separately, plus disclosures and confidentiality rules. If there is no chosen venue, record that fact and preserve accurate tool-use provenance so later selection is possible. Recheck when the venue or policy changes and before submission.

**Acceptance:** intended and already completed activities fit the target's actual rules; the author can truthfully provide required declarations. For example, Taylor & Francis' live guidance accessed 2026-10-05 prohibits generative-AI first drafts of manuscripts or sections, while allowing specified language refinement and other bounded uses. No displayed update date was found. This differs materially from a disclosure-only requirement. See P8.

**Failure/recovery:** do not begin prohibited target-specific drafting. For an already AI-created draft, keep the historical fact, flag incompatibility, and select a compatible venue or obtain an explicit authorized clarification from the publisher. Do not assume that editing, human review, or disclosure erases a forbidden drafting history. Do not conceal AI use or write a false non-use declaration. **Stop:** a compatible target/workflow is established, or venue-specific preparation pauses while mathematically useful research continues. This policy gate is separate from mathematical correctness and permission to submit.

### S01 Research question and closest prior work

**Input:** problem statement, target class/parameters, preliminary examples, and candidate references. **Owner:** research owner plus literature auditor. **Output:** `question.md`, source ledger, and closest-result comparison with theorem/page/version, hypotheses, conclusion, method, overlap, and the proposed delta.

**Work:** search exact terminology and synonyms; trace cited and citing primary work; open the closest statements and proofs; identify unpublished predecessors separately. Log queries, date, source families covered, inaccessible items, and potentially contradictory results. Specify a bounded search scope appropriate to the proposed contribution.

**Acceptance:** the question has an unambiguous domain; every credited result is supported at the cited location; the proposed delta survives direct comparison with the nearest known results; unresolved leads are visible. A negative search is phrased as a bounded observation.

**Failure/recovery:** a predecessor already proves the claim → credit it and refocus on a genuine extension, alternative proof, or exposition; an inaccessible primary source → try an official author/thesis/archive copy and keep the lead open if unavailable. **Stop:** proceed once the bounded search and claim comparison are documented; pause the affected priority claim if a plausible unresolved overlap could erase it. Do not research indefinitely to manufacture certainty.

### S02 Claim and evidence ledger

**Input:** S01 and all candidate statements. **Owner:** research owner. **Output:** `claims.json` or `claim_matrix.csv`, with stable claim IDs and a claim-to-source/proof/certificate map.

**Work:** atomize compound assertions. Separate an upper construction bound, an attainment witness, a complete census, a limit, and a global optimum. Record strictness, integer ranges, equivalence relations, normalization, and excluded domains. Every abstract and introduction assertion must link to one row.

**Acceptance:** no theorem uses exploratory evidence as proof; every computational claim has a finite domain; inherited claims have actual credit; every dependency refers to an existing row; the dependency graph is acyclic or an intentional simultaneous argument has been collapsed into one documented node.

**Failure/recovery:** split ambiguous rows, weaken an unsupported statement, or route a missing proof to S03/S04. **Stop:** ledger covers all headline claims and remaining open conjectures are labeled. Acceptance here means correctly recorded, not mathematically proved.

### S03 Theorem dependencies and proof obligations

**Input:** exact ledger statements. **Owner:** research owner with mathematical auditor. **Output:** dependency DAG, obligation table, and proof skeleton with local interfaces.

**Work:** for every inference write the hypotheses it consumes, the object it constructs, and the conclusion it exports. Inspect vacuous and degenerate cases; distinguish local from global hypotheses; check existence versus uniqueness, minimum versus minimal, labelled versus unlabelled, and strict versus non-strict statements. Identify every indispensable finite premise and every use of a limiting argument.

**Acceptance:** each main claim has a finite chain of discharged obligations ending in definitions, proved lemmas, precisely cited results, or explicitly listed exact computational inputs. No circular invocation; no locally omitted hypothesis; all endpoints and multiplicities accounted for.

**Failure/recovery:** produce a smallest counterexample to the literal wording if possible, repair the exact lemma, and invalidate dependent proofs until rechecked. **Stop:** no unresolved obligation remains on a claimed theorem path; otherwise retain a conjecture or conditional theorem. A locally missing hypothesis must be repaired even when later applications happen to satisfy it.

### S04 Counterexamples and exact experiments

**Input:** S03 obligations, boundary hypotheses, constructions, and finite domains. **Owner:** computational/mathematical auditor. **Output:** executable checks, exact witnesses, domain manifest, run log, expected outputs, and mathematical interpretations.

**Work:** test removed hypotheses and equality cases; distinguish universal endpoint failure from pointwise necessity. Rebuild definitions independently where valuable. Prove each pruning step preserves all solutions. Use integers/rationals or a rigorously justified interval method for acceptance; floating point only explores. Start each run in a fresh output directory, check exit codes and explicit completion, and atomically publish success only at the end.

**Acceptance:** every finite result identifies inputs, code version, arithmetic, complete domain, termination, predicate, and newly generated output; independent checker verifies certificates; completeness rests on exhaustive reduction and safe enumeration, not just checking a final list. Deliberate failure/interruption cannot leave a stale success accepted.

**Failure/recovery:** a counterexample returns to S02/S03; incomplete runs remain incomplete; stale output is discarded; numerical uncertainty invokes exact arithmetic. **Stop:** the planned domain and specified adversarial cases are completed, or a bounded resource blocker is honestly recorded. No finite run upgrades an unbounded conjecture by extrapolation.

### S05 Main story abstract and introduction

**Input:** stable S01–S04 ledger and target audience. **Owner:** revision/editorial author. **Output:** one-paragraph story, claim-linked abstract, and introduction outline/draft.

**Work:** articulate question → closest known result → exact contribution → proof mechanism → boundary. Put the strongest intelligible general theorem before its specialization and optional census when dependencies permit. Explain why the question matters mathematically without inventing importance. Attribute inherited tools when first needed; put project history outside the research narrative.

**Acceptance:** an independent reader can state the main theorem and its scope; each abstract sentence maps to a ledger row; no “first,” “optimal,” “complete,” or “sharp” exceeds the evidence. The abstract distinguishes analytic and computer-assisted parts where necessary. Exact journal word limits are checked only against the chosen journal's current instructions.

**Failure/recovery:** if the contribution is invisible, fix the hierarchy and motivation; if it is too weak or duplicated, return to S01 instead of marketing it harder. **Stop:** the story is accurate, specific, and recoverable without the author's chat history.

### S06 Proof architecture and notation

**Input:** verified skeleton and narrative. **Owner:** author/editor, with proof auditor for mathematical changes. **Output:** complete source, notation dictionary, lemma-purpose map, and cross-reference map.

**Work:** place definitions before first essential use; introduce a lemma by the obstacle it removes; give the global proof roadmap before technical matrices or case splits. Keep the theorem's hypothesis in the lemma that actually consumes it. Make exact-versus-asymptotic quantities and dimensions visible. Separate analytic continuation from finite completion.

**Acceptance:** a reader can follow dependencies without reverse-engineering the source; every symbol is defined, scoped, and consistently used; every exceptional case has a location; prose bridges explain why the next computation matters. The pre/post theorem and proof diff is reviewed.

**Failure/recovery:** split overloaded lemmas, add a missing argument, or name a reusable local principle. Route actual mathematical changes back through S03/S04; an “editorial” label does not exempt them. **Stop:** full proof is present and navigable, not merely sketched by an outline.

### S07 Figures tables and mathematical interfaces

**Input:** exact construction/adjacency/block definitions and notation. **Owner:** editor with mathematical checker. **Output:** original vector figures where suitable, machine-derived tables, captions, and figure-validation evidence.

**Work:** distinguish an individual edge from a complete edge family or matrix block coupling. Label seams, layers, retained coordinates, multiplicities, and repeated cells. Make diagrams readable in grayscale and at final size. Derive every numeric table from named data or a printed proof.

**Acceptance:** figure semantics agree exactly with definitions; captions state any schematic omissions; degenerate cases such as coincident indices or exceptional small dimensions are checked; symbols match the text; no illustration replaces a definition or proof. All data sources and plotting transformations are reproducible.

**Failure/recovery:** correct the diagram and re-render; remove a decorative or misleading diagram rather than preserving it. **Stop:** each retained visual reduces a real reconstruction burden and is mathematically accurate.

### S08 Independent mathematical audits

**Input:** frozen statements, full proofs, and required computational source. **Owner:** auditor distinct from the proof's producer where feasible. **Output:** issue ledger with severity, exact location, reproduction/counterexample, impact, and suggested repair; coverage log.

**Work:** reconstruct the delicate local and global steps without relying on old verdicts; trace all hypotheses; verify closest-prior-work credits; independently generate finite witnesses or checks at high-risk boundaries. Separate a demonstrated error from an unverified concern and an optional stylistic change.

**Acceptance:** every headline theorem and indispensable computational premise has recorded coverage or an explicit blocker; reported issues contain checkable evidence. A successful finite test is not substituted for an arbitrary-parameter proof. Independent algorithm inputs/shared assumptions are disclosed.

**Failure/recovery:** stop affected claims, repair and rerun dependencies, or downgrade scope. **Stop:** specified proof obligations have been audited; unknowns remain explicit. A clean audit does not imply journal acceptance or globally exhaustive novelty clearance.

### S09 Fresh blind mathematical and writing review

**Input:** ONLY an allowlisted frozen manuscript/PDF, neutral build instructions, cited primary mathematical sources, proof code and exact data. **Owner:** a genuinely new review context; custodian prepares packet. **Output:** locked report, input hashes, exposure log, and context/round record.

**Work:** run packet lint, inspect all visible filenames/metadata/text manually, and start with no inherited conversation, prior report, response, saved verdict, or status manifest. Read the paper before the author explains it. Assess mathematics, contribution, exposition, citations, reproducibility, and formal scope separately. Reviewers do not edit source. The initial blind packet excludes even favorable remote-validation status text.

**Acceptance:** new context identity is recorded; round is 1; editor differs; packet hashes match; exposure disposition is clean; the reviewer reports strengths, exact problems, uncertainty, and actionable requirements. One context may handle at most two rounds in total.

**Failure/recovery:** if filenames, metadata, a source page, or messages leak status/old conclusions, immediately record exact exposure and timing, stop calling the review pristine, preserve useful mathematical work as disclosed evidence, regenerate the packet, and start a NEW context. Do not pretend an instruction to forget resets a context. **Stop:** the frozen report and exposure log are complete, or the context is replaced.

### S10 Different editor new version and response

**Input:** locked review, old version, ledger, and allowed editing scope. **Owner:** a different editor. **Output:** new immutable manuscript version, issue-by-issue response, semantic/math diff, updated claim ledger, rerun logs, and new PDF.

**Work:** handle each issue as accepted, partially accepted, rebutted with evidence, or deferred with reason. Identify old/new locations and exact changed statements. Mark editorial versus mathematical changes. Keep baseline untouched. Recompile and rerun the checks invalidated by the diff; newly added results get normal proof obligations.

**Acceptance:** every required issue has a specific disposition and evidence; no theorem changes silently; all newly affected dependencies are checked; the new version has a unique hash. The editor's assertion that an issue is fixed is not the reviewer closing it.

**Failure/recovery:** incomplete responses return to editing; changes that weaken or invalidate a main claim return to S02/S03. **Stop:** a complete reviewable revision and response are frozen, not when the editor self-approves the paper.

### S11 Re-review and context retirement

**Input:** new version plus response for the SAME context's second round, or a newly cleaned packet for a NEW context's first round. **Owner:** reviewer and custodian. **Output:** per-issue closure/reopening, regression review, context-use registry, and unresolved list.

**Work:** verify fixes rather than trusting the response; inspect changed statements and their transitive dependents; test new claims; revisit headline-to-evidence agreement. If using the same context, the response may be read because this is explicitly round 2. If using a new context, withhold old reviews/responses until its initial report is locked; a separate later comparison is non-blind.

**Acceptance:** no correctness-critical or mandatory reproducibility issue remains open; subjective disagreements are documented; reviewer identity/round/packet are unambiguous. After two rounds the context is retired regardless of verdict.

**Failure/recovery:** another revision uses a different editor and, after round 2, a new reviewer context. A newly contaminated context is replaced even before two rounds. **Stop:** the required issues are independently closed, or an explicit unresolved blocker/author decision pauses the paper. Do not rotate contexts until a favorable verdict is obtained; preserve all substantive objections in the coordinator record.

### S12 Lean statement coverage and kernel checks

**Input:** exact paper claims, formal sources, toolchain, dependency lockfiles/patches, named declarations, and intended trust policy. **Owner:** formalization auditor. **Output:** paper-to-declaration map, semantic correspondence report, clean build log, axiom audit, and uncovered-claims list.

**Work:** check types and quantifiers, not declaration counts. Map the exact mathematical objects, indexing, bounds and attainment to prose. Build in a clean directory at the exact Lean/mathlib revisions and patches. Run `#print axioms` for every claimed final declaration and relevant exported theorem. Inspect transitive dependencies; forbid `sorryAx` and undeclared/custom assumptions for a kernel-checked claim. Explicitly disclose native-evaluation/compiler trust if used; it is not the same boundary as a proof checked only by the small kernel.

**Acceptance:** exact version compiles; requested declarations exist; statement correspondence is independently assessed; axiom sets match the declared trust policy; no excluded theorem is described as formalized. When no formalization is claimed or required, record a justified `not_applicable` and the ordinary proof path. Partial formalization is acceptable only with exact boundaries and successful checks of the claimed part.

**Failure/recovery:** compilation failure is a build blocker, not automatically a false theorem; fix environment or proof, then clean-replay. A mismatch in the statement returns to S02/S03. **Stop:** the frozen claimed scope is checked, or its claim is withheld. A moving development checkpoint cannot silently replace a paper's pinned checkpoint.

### S13 Compiled PDF and semantic production QA

**Input:** final TeX, bibliography, figures and exact build environment. **Owner:** QA custodian, with a human visual reader. **Output:** PDF hash, compilation log, text/link extraction, all-page visual inspection log, and corrected source if needed.

**Work:** build from the frozen source in a fresh output directory; resolve citations/references; inspect every page at readable resolution for clipping, glyphs, matrix alignment, tables and proof breaks. Verify minus signs, strict inequalities, subscripts and finite ranges against source. Check actual link annotations and abstract/title metadata. Compare PDF and source versions.

**Acceptance:** no unresolved references or material layout defects; all pages inspected with count/hash bound; figures/tables agree with data; active links point to the intended frozen resources. A successful TeX exit alone is not visual QA.

**Failure/recovery:** fix source/layout, rebuild, rehash, and reinspect affected pages plus all-page sanity. Mathematical edits reopen dependent audits. **Stop:** the final PDF, not an intermediate build, has explicit QA evidence.

### S14 Version pinned reproducible supplement

**Input:** all indispensable proof code/data, experiment tables, formal checkpoint, environment and license/provenance constraints. **Owner:** release custodian with independent replay auditor. **Output:** paper-specific allowlisted bundle, hashes, commands, expected outputs, immutable archive/commit/DOI, and access/replay record.

**Work:** document one clean-directory entry point and theorem-to-file map. Pin compilers, package versions, Lean/mathlib and patches. Include all finite domains, seeds, termination conditions, output predicates, and license/attribution. Separate exploratory material from proof inputs without hiding essential calculations. Reproduce from the downloadable bytes; test anonymous retrieval where public access is claimed. Keep history/review reports in a separate administrative bundle, not the blind packet.

**Acceptance:** a reader starting from the PDF can obtain exactly the cited bytes, execute the listed checks, and compare newly produced exact results; interrupted runs cannot pass; all essential files are present. Code availability alone is not a successful replay. A Git commit is immutable identity but an archival snapshot improves durability; use the actual target journal's policy.

**Failure/recovery:** repair missing files, pin dependencies, regenerate a versioned bundle, update PDF citation, and rerun the release build. **Stop:** frozen source, PDF and supplement refer to the same version. Public upload/release needs the user's authorization; preparing the bundle does not authorize publication.

### S15 Submission readiness and human decision

**Input:** all prior gate records including a refreshed S00 compatibility decision, final artifacts, current target-journal instructions, verified author/affiliation/funding/disclosure data. **Owner:** human authors/corresponding author with custodian. **Output:** readiness report and decision packet; no automatic submission.

**Work:** confirm journal fit, scope/length/style, prior publication/overlap, declarations, data statement, AI policy, permissions and authors' consent. Verify references against primary sources and metadata. Confirm all correctness-critical objections have evidence-based closure, the latest version was reviewed, formal scope is honest, and supplement/PDF pins agree.

**Acceptance:** all mandatory gates pass or have legitimate signed not-applicable decisions; no unknown author/consent fields; unresolved priority leads are addressed proportionately and never hidden; the chosen journal's actual requirements are met. This means ready for an authorized human decision, not accepted by a journal.

**Failure/recovery:** pause for missing identity/consent/journal decision or reopen the relevant technical gate. **Stop:** deliver the frozen decision packet. Actual submission, legal agreements, authorship commitments and public sharing remain separate authorized actions.

## Review state machine and exposure control

`draft → evidence_complete → packet_candidate → packet_linted → packet_manually_inspected → blind_review_round1 → different_editor_revision → same_context_round2 OR new_context_round1 → gates_closed → submission_decision`

Any mathematical change invalidates the changed claims and their transitive dependents, abstract references to them, relevant formal correspondence, and impacted computational tests. Any PDF/source change invalidates the PDF hash and visual QA. Any dependency/source change invalidates the associated replay. Status changes alone cannot restore a gate.

Keep two bundles:

- **Mathematical packet:** paper, definitions, cited primary material, algorithms, input data, neutral commands and identities. Expected data are mathematical assertions to test; saved success flags and earlier reviewer conclusions are not inputs.
- **Coordinator record:** reviewer identities, context rounds, old reports, responses, exposure logs, status, access-check results, and readiness decisions. This record is never part of a new blind review's initial context.

Cleanliness is broader than filenames. Inspect PDF metadata/annotations, TeX comments, source headers, JSON keys, README claims, archive members and cited-source landing pages. If a primary source includes historical verdict text, a custodian may prepare a faithfully attributed mathematical excerpt with exact locator/hash and clearly mark omissions outside the mathematics; do not misrepresent it as the complete source. A reviewer who already saw leaked content cannot be made blind by sanitizing the next message.

The validator implements conservative schema, identity, context and gate checks. A readiness record joins a locked claim/obligation/issue inventory, proof obligations, issue responses, a version registry, actual PDF/source bytes and typed stage receipts. Required rows cannot be deleted silently; receipts must identify the current version, context and relevant artifact hashes. Finite computational claims bind to explicit discharged obligations and attributed exact run/reduction evidence. All semantic proof, policy and consent judgments remain human or named-auditor attestations, not facts generated by the validator. It cannot understand every paraphrased verdict, prove independence, decide a proof, verify arbitrary mathematical semantics, or guarantee that an agent never opened another file. Its result is a necessary bookkeeping check plus a list of required human attestations. There is intentionally no “theorem true” output.

## Method demonstration and stopping rule

Use `SYNTHETIC_DEMO.md` and the synthetic fixture generator to practice the interfaces without any real research inputs. The mathematical example distinguishes a finite exact check from an arbitrary-parameter proof. The administrative fixture demonstrates linked records and deliberate failure cases; its invented approvals are not scientific or institutional evidence.

For an actual project, completion means that its exact claims and applicable gates have genuine evidence and required human decisions. A reusable workflow can be complete while a particular paper still has open obligations. Stop when those obligations are discharged or the remaining research, access, policy or human decision is explicitly recorded. Do not manufacture readiness or infer permission to publish from a validator result.
