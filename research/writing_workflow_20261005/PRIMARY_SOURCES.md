# Primary sources and adopted decisions

All pages below were opened on 5 October 2026. Live technical documentation can change; its retrieval date is not a software version pin. The actual paper must record its tested Lean/toolchain/mathlib revisions. No recommendation below is presented as a universal journal rule.

## P1 London Mathematical Society computer aided proofs

[Official policy](https://www.lms.ac.uk/publications/policies/computeraidedproofs), updated November 2024.

The policy requires the article to identify the role of computer-assisted calculations, make essential code and supplementary files available, and provide code that a reader can inspect meaningfully, minimizing numerical error. It does not promise line-by-line verification by a referee.

**Adopted decision:** identify every indispensable finite premise; publish surveyable exact checkers and domains; explain safe pruning; distinguish proof inputs from exploratory computation. Independent reconstruction, stale-output tests, and gate IDs are this workflow's implementation choices. Relevant stages: S02–S04, S08, S14.

## P2 London Mathematical Society data access

[Official policy](https://www.lms.ac.uk/publications/policies/dataaccesspolicy), updated November 2024.

Research data includes evidence needed to evaluate or reproduce results, including software and algorithms. Development notes that are not needed for verification are outside this scope. The policy encourages data statements, stable repositories and citable identifiers; essential material should be available for review. It also permits journal supplementary files, with a stated per-file limit.

**Adopted decision:** separate a complete mathematical supplement from development/review history; cite an immutable, readable package in the PDF. This does not excuse withholding an indispensable failed case or assumption. Check the chosen venue's live size and deposit rules before submission. Relevant stages: S09, S14–S15.

## P3 SIAM Journal on Matrix Analysis and Applications author instructions

[Official instructions](https://epubs.siam.org/journal/simax/instructions-for-authors), live page, no revision date displayed; accessed 2026-10-05.

The page asks for a self-contained one-paragraph abstract of at most 250 words relating techniques/conclusions to known results, accurate citations, and useful figures. Its optional code/data badge has explicit availability, README, parameter and durable-copy expectations. A repository-based badge request includes an immutable supplementary snapshot; an ordinary academic webpage is insufficient for that badge.

**Adopted decision:** map abstract claims to evidence and provide paper-specific replay commands. The 250-word limit and badge rules are SIMAX-specific, not universal requirements or a recommendation that any particular paper fits SIMAX. The workflow's technical replay is stronger than a simple availability check and must be reported separately. Relevant stages: S05, S07, S14–S15.

## P4 SIAM contemporary integrity guidance

Tamara G. Kolda, [A Contract of Trust: Artificial Intelligence Usage for SIAM Journal Submissions](https://www.siam.org/publications/siam-news/articles/a-contract-of-trust-artificial-intelligence-usage-for-siam-journal-submissions/), 1 May 2026.

This official discussion stresses human author responsibility, accurate references, disclosure of AI use, and the risks of unattributed ideas, incorrect mathematics/code and misleading figures. It states that SIAM currently prohibits its official referees from using AI because of confidentiality.

**Adopted decision:** this package's “reviewers” are authorized pre-submission internal audits of the user's own work, not journal-appointed referees. Do not upload confidential third-party journal submissions to an AI system or claim these reports are journal peer review. Do not invent authors or affiliations; verify citations at source and prepare the disclosure the selected venue actually requires. Relevant stages: S01, S07–S09, S15.

## P5 Lean reference on axioms

[Official Lean reference, Axioms](https://lean-lang.org/doc/reference/latest/Axioms/), live `latest` documentation accessed 2026-10-05; [Elaboration and Compilation](https://lean-lang.org/doc/reference/latest/Elaboration-and-Compilation/), same retrieval date.

Lean tracks the axioms on which a declaration depends. `sorryAx` can discharge arbitrary goals and is unsuitable in a finished proof. Standard logical dependencies such as choice, propositional extensionality and quotient soundness differ from adding a problem-specific unproved axiom. Proofs using native evaluation can extend the trust boundary to compiled computation. The kernel checks proof terms produced by elaboration.

**Adopted decision:** audit actual `#print axioms` output for named final declarations at the tested revision, rather than grepping source or counting declarations. Record native/compiler trust distinctly and independently inspect statement correspondence. A completed build cannot prove the informal theorem if the formal statement is weaker or differently defined. Relevant stages: S02, S12.

## P6 mathlib documentation and review

[Documentation style](https://leanprover-community.github.io/contribute/doc.html) and [Pull Request Review Guide](https://leanprover-community.github.io/contribute/pr-review.html), live official community documentation accessed 2026-10-05.

The documentation guide requires explanatory module material, docstrings for important definitions/theorems, and references. The review guide asks whether declarations already exist, are documented meaningfully, fit the library, and have understandable proof sketches where needed. These are mathlib contribution conventions, not a paper-acceptance certificate.

**Adopted decision:** maintain a readable paper-to-declaration map and cite original mathematics alongside formal declarations. Review definitions and semantic scope as well as compilation. No mathlib pull request or upstream acceptance is implied; the project continues in its own repository. Relevant stages: S01, S06, S12.

## P7 Terence Tao on writing

[Author's own writing advice](https://terrytao.wordpress.com/advice-on-writing-papers/), long-running page originating in 2007; accessed 2026-10-05. This is deliberately identified as durable advice, not a new 2026 result.

Tao recommends accurately presenting the paper's key points, motivating and organizing the work, choosing notation and detail for the audience, using smaller lemmas where helpful, and proofreading a final draft. He explicitly cautions that rigid rules do not fit every mathematical text.

**Adopted decision:** ask an independent reader to recover the question, mechanism and boundaries; use a causal roadmap and purpose-driven lemmas. The fixed stage sequence, claim ledger, two-round context cap and separate editor are project-specific engineering decisions, not Tao's prescriptions. Relevant stages: S05–S06, S09–S11.

## P8 Taylor & Francis AI use and manuscript preparation

[Official guidance](https://authorservices.taylorandfrancis.com/editorial-policies/using-ai-in-your-research-and-manuscript-preparations/), live page accessed 2026-10-05; no revision date displayed.

The manuscript-text table prohibits generative-AI first drafts of manuscripts or sections. Language refinement is allowed within a narrower scope; it may not create or conclude the argument. The page separately addresses research methods, software assistance, figures, translations and declarations.

**Adopted decision:** assess venue compatibility before drafting, preserve actual tool-use history, and recheck before submission. An existing AI-created manuscript is not automatically made eligible by disclosure or human editing. This is a publisher-specific constraint, not a universal prohibition on AI-assisted mathematical research. Authors must check that their actual research and writing history fits a prospective venue’s policy. Relevant stages: S00, S05, S15.

## Scope of this source analysis

P1–P3 describe publisher requirements or recommendations within their stated scope; P4 is official integrity guidance; P5–P6 are technical/community documentation; P7 is older author advice; P8 is publisher-specific AI guidance. The workflow, schemas and synthetic demonstrations are original generic synthesis. No private research record or unpublished paper identity is included. Recheck live policies before making a real submission decision.
