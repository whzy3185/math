# Application to the three current manuscripts

These are editorial judgments after the source analysis, based on the current manuscript text. They are not claims made by the sampled authors, and they do not establish mathematical novelty or correctness. The editing task is to implement the useful changes in new manuscript copies, preserve theorem content unless separately corrected, and return a before/after record. None of the source manuscripts was changed by this study.

## Domination manuscript

Baseline: paper_v3_provenance_rev1/manuscript.tex, “Sharp boundary bounds and edit instability in uniquely dominated bipartite graphs.”

### What already works

The abstract states exact maxima and equality classes, then the edit-distance scale. The introduction credits Erlbacher's earlier examples and Koch–Narayan's small equality case. The metric minimizes over arbitrary relabellings. The last sections distinguish absolute deficit from relative deficit and do not claim a theorem for three or more residual vertices. Preserve all of these features.

### Organizing question

The natural central question is how much extremal edge information determines the graph near the smallest feasible orders. The two levels are exact equality and near equality. The strongest narrative is the coexistence of complete equality classifications with an obstruction to dense edit stability. This is an organizing interpretation of the present statements, not a priority claim.

### Paragraph and theorem plan

1. Define unique minimum domination and explain the intrinsic order threshold
2. Give the nearest predecessor and the already-known counterexamples with their exact provenance
3. State the boundary-class question, then the two exact-bound/equality theorems
4. Define the unlabelled edit metric and state the upper/lower stability scale
5. Explain immediately why absolute deficit and relative deficit behave differently
6. Place the recovered conjecture counterexamples as consequences, with the existing attribution
7. Finish the introduction with a causal roadmap rather than another claim list

Keep the two exact maxima before stability, because the deficit and reference extremizer depend on them. Do not let the recovered thirteen-vertex counterexample become the headline again. Construction-first exposition can mean a schematic and a short description before the proof, without requiring all graph notation before the first theorem.

### Suggested original insertion after the current stability discussion

“The equality statements determine the extremal graphs completely, but the amount of edge information needed to force edit-distance closeness is more delicate. Our upper estimate uses the absolute deficit t. The connected examples show that a deficit negligible compared with the extremal edge count can still permit a positive proportion of all possible edits, even after the best relabelling.”

This restates the displayed results without introducing a new stability theorem. Preserve the current explicit normalization and limit in the proof section.

### Suggested original proof roadmap

“Choose two exterior private neighbours for every vertex of the unique minimum dominating set. At the two boundary orders, only one or two residual vertices remain. Local replacement arguments limit the edges between the resulting small cells; equality forces their choices to agree. For near equality at the first boundary, an exact deficit decomposition controls missing incidences, deficient cells, and the imbalance of the two center classes. Repair gives the upper edit bound, while switching whole rows after losing a residual incidence gives the matching order of obstruction.”

Use this only after checking that the local constraints retained in the final proof justify each sentence. The roadmap does not replace those constraints.

### Equality proof signposting

Before the first rigidity proof, say which inequalities must all be tight. Distinguish the local equality pattern from the global coherence condition; the latter is what selects one template rather than independent choices in every cell. Before the two-residual proof, identify the placement split and explain why the small domination-number exceptions require their own treatment. Existing section headings can be retained while adding these bridges.

### Visual candidate and acceptance checks

A schematic should display a center pair x_i,y_j, their private pairs U_i,V_j, and the residual vertex or vertices. Use the same labels as Definition H_r and state whether a line represents one edge or a complete family of edges. A second small panel may show the row modification; list deleted and added edge types rather than relying only on color.

Do not alter the maxima, the three/one/two equality-class regimes, the arbitrary-bijection metric, the range of the obstruction, or any provenance statement. The word “sharp” must remain qualified: the edit bound has the right order, not the best constant 12. The supplementary finite checks remain supplementary to analytic arguments.

Editorial sources: S7 (equality mechanism and proof dependencies), S3 (stability question, explicit examples, separately scoped sharpness), and S2 (explain which structural information a theorem controls). Exact locations are in the reading notes.

## Mycielski manuscript

Baseline: mycielski_paper_v3/mycielski_hall_v3.tex, “Hall bounds under the Mycielski construction and the extremizers of the sixth Mycielski graph.”

### What already works

The manuscript separates the general two-step upper bound, an analytic sharp specialization, and a computer-assisted complete census. It distinguishes ambient D_5-orbits from abstract isomorphism classes. The twenty-vertex witness is proved by explicit independence arguments. The fractional-coloring certificate is sufficient without importing a more complicated exact value. These are strengths to keep.

### Present narrative weakness

The introduction is titled “Statements and scope” and reaches the general theorem before explaining the local question in relation to the familiar Mycielski sequence. The reader can parse the result yet still miss why this is the useful level of generality. The late literature paragraph supplies the boundary, but little affirmative motivation. The solution is a brief mathematical question, not stronger novelty adjectives.

### Suggested original opening after the basic definitions

“The Hall ratio measures the largest vertex-to-independence ratio among induced subgraphs. For the Mycielski construction, we ask what a fractional coloring of the base graph already forces after one or two steps. Our result is a local implication: under the stated hypothesis on the base, it gives upper bounds independent of its order. We then ask whether the two-step value is attained and how the attaining subsets sit inside the sixth Mycielski graph.”

The first sentence follows the definition; it is not intended as a new characterization. Keep the separate statement that the result does not settle the asymptotic ratio problem. If the editor adds the standard inequalities relating Hall, fractional chromatic, and chromatic number, give their short justification or a suitable existing reference.

### Suggested original proof roadmap

“Deleting the distinguished apex vertices leaves a graph that maps to the base, so its fractional coloring bounds the size of every induced subset in terms of its independence number. Integrality then handles large independence numbers, and the layer structure controls the remaining small cases. Tightness forces a twenty-vertex configuration with fixed layer totals. An explicit configuration attains the bound; only the enumeration of all attaining configurations requires the later census.”

### Theorem hierarchy and witness presentation

Keep the general theorem first, the sharp M_6 specialization second, and the census third. The equality restrictions belong with the general theorem because they explain why the later finite search is manageable. Explain that the witness proves attainment independently of census completeness. A four-layer diagram with z,z',w and selected cardinalities can replace some verbal reconstruction, but it must include the special adjacencies used by the proof. The complete integer vertex list can remain as a reproducibility description after the structural definition.

The exact coloring table should retain its coverage explanation. The census section should retain the mathematical membership criterion before implementation details. Record what each independent algorithm checks rather than implying that agreement between outputs alone proves exhaustive search.

### Boundary update rule

The baseline says that chi_f(G)<3 is a sufficient condition and does not claim necessity. Another editor has reported a possible endpoint example based on K_{2,2,2}; that mathematical claim has not been verified in this study. If a separate check proves that replacing <3 by ≤3 fails, the editor may add that precise endpoint obstruction. It would not imply that every graph with fractional chromatic number at least three fails the inequalities, nor prove necessity of the hypothesis for each individual graph. This update must be identified as new mathematical evidence, not as a conclusion of this writing study.

Do not turn “we prove” into “first,” remove the census evidence boundary, rename 199 ambient orbits as 199 nonisomorphic graphs, or confuse the finite specialization with the unbounded-sequence problem.

Editorial sources: S2 (strongest intelligible theorem and dependency order), S6 (qualitative result followed by exact witnesses and explicit limitations), and S1 (framework versus consequences). Exact locations are in the reading notes.

## Signed cycle-square manuscript C029

Baseline: manuscript_integrated/manuscript.tex and sections/01_introduction.tex through 08_verification.tex, “Uniform Schur bounds and holonomy in signed cycle squares.”

### What already works

The abstract leads with the Schur mechanism and a bound uniform in the number of unequal cells. The introduction states the allowed sign words and both holonomies, preserves the earlier witness range's provenance, and separates explicit upper competitors from global minimization. It distinguishes the old withdrawn target from the revised conjecture. The verification section separates analytic extension from exact finite inputs and states a limited formalization scope. Keep these boundaries intact.

### Present narrative weakness

The opening moves quickly from the benchmark into word definitions, gauge formulas, two caps, and a theorem. A reader must infer why arbitrary unequal cells are the key obstacle and why a four-dimensional recurrence answers it. The complete proof architecture exists in the body but should be visible before the first matrix calculations.

### Suggested original bridge before the cell-word definitions

“We seek a bound for an explicit family that survives two changes at once: the cells may have different lengths, and their number is unrestricted. A fixed-period calculation alone does not cover this setting. The useful reduction is to eliminate each cell interior while retaining its boundary coordinates, then control the resulting cyclic boundary matrix with an error independent of the number of cells.”

This describes the stated construction and proof. It makes no claim about arbitrary defects, arbitrary sign words, or a new general theorem for all signed graphs.

### Suggested original roadmap after the main results

“The argument separates local elimination from global assembly. Squaring the signed adjacency matrix turns the spectral-radius bound into positivity of cI−A². Four-site interior blocks obey a fixed rational recurrence; six boundary coordinates retain the effect of each eliminated chain. Exact finite premises and contraction estimates compare long chains with a common positive limiting boundary matrix. In the assembled cycle every boundary meets two chains, so the error is controlled independently of the cell count. The remaining bounded ranges are completed by exact rational checks.”

Retain the explanation that coincident contributions at one or two cells are added, not overwritten. The separate period-eight holonomy proof should be introduced as an exact complementary calculation with its own provenance and application.

### Result hierarchy

The unequal-cell theorem is the organizing mechanism. The all-size one-cell statement is a sharper specialization with finite completion. The competitor theorem translates the family bounds into comparison with the twisted benchmark. The exact holonomy result addresses a revised target but must retain its inherited-formula status. The final extremal problem remains open in the manuscript's stated scope. No formatting choice should blur these roles.

### Visual candidate and acceptance checks

Use a simple diagram with a four-site interior chain and six retained coordinates at each boundary. Show one seam sign and explain that it encodes the Hamilton holonomy. A second diagram may show the cyclic assembly, with explicit treatment of one-cell loops and two-cell parallel contributions. Do not borrow figures from signed Turán papers: their forbidden-subgraph model is different.

Preserve squared-versus-unsquared quantities, strict versus non-strict bounds, the exact minimum cell lengths 106 and 202, the one-cell sign choice, the width-10^{-6} enclosure rather than an exact supremum, and the distinction between all allowed cell counts and all signings. Revalidate formalization claims against the final current build; this study merely observed the baseline statement and did not rerun Lean or certificate computations.

Editorial sources: S1 (common mechanism and differentiated consequences), S3 (causal roadmap and sharpness scope), S4–S5 (signed conventions and comparison candidates), and S6 (attainment versus limit versus method boundary). Exact locations are in the reading notes.

## Required record from the revision editors

For each implemented change, record the old location, new location, a short before/after passage, the reader problem it fixes, and the study note or rubric item that motivated it. Separate editorial changes from new mathematical results, referee-driven corrections, and fresh provenance findings. List omitted suggestions with a reason when they materially affect the plan. Compile and visually inspect the resulting manuscript. A study-only commit is not completion of the user's manuscript-revision request.
