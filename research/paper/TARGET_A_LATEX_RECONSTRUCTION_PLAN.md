# Target A Publication LaTeX Reconstruction Plan

Status: `MATHEMATICAL_CONTENT_FROZEN`

## Frozen source

The mathematical source of record is
`manuscript_md/TARGET_A_MANUSCRIPT_V2.md` at SHA-256
`d7b9e35acd57b2ab9916bf82bf8d52359ee30ab13cda09efebf0f93f8e76ce6b`.
The Task 44 tree `manuscript_tex/` is an immutable archive for this task.  The
publication reconstruction is built separately in `manuscript_tex_pub/`.

## Permitted reconstruction

- Replace Markdown and ASCII pseudo-math by semantic LaTeX mathematics.
- Replace hand-numbered statements and displays by theorem, proof, equation,
  table, figure, section, and appendix environments with semantic labels.
- Replace textual structural references by automatic cross-references.
- Repair Markdown list conversion, table floats, line breaking, and typography.
- Compress introductory implementation detail without changing any theorem,
  hypothesis, quantifier, numerical bound, proof dependency, or trust boundary.
- Move engineering detail to appendices and add publication metadata, data and
  code availability, and supplementary-material placeholders.
- Verify bibliographic metadata against primary or publisher sources.
- Share one mathematical body among generic, anonymous, JGT-style, and
  SIDMA-style wrappers.

## Prohibited automatic changes

- Any change to the scope or logical strength of Theorems A--F.
- Any new mathematical result, search, conjectural implication, or proof step.
- Any claim of all-period or all-signings optimality, failure at every even
  order above 32, or an unconditional priority claim.
- Any removal or weakening of the computer-assisted proof disclosure.
- Any guessed author, affiliation, correspondence, ORCID, funding,
  acknowledgment, archive DOI, or reference metadata.
- Any modification of the frozen V2 source or destruction of the Task 44 tree.

If a mathematical defect is discovered, it is recorded and the affected
reconstruction stops.  It is not repaired by silently changing the theorem.

## Baseline and gates

At the frozen baseline, the Task 44 source contains 115 `lstlisting`
environments and 155 hand-number-like patterns.  The Markdown component source
contains 109 mathematical fenced blocks and 6 shell-command fenced blocks.

The publication gate requires:

1. the frozen-source hash and mathematical manuscript checker to pass;
2. zero mathematical listings and zero hand equation numbers;
3. theorem/proof environments, labeled table floats, resolved references, and
   resolved citations;
4. zero overfull boxes, no `\sloppy`, no table of contents, no local absolute
   paths, and no task identifiers in the manuscript;
5. successful generic, anonymous, JGT-style, and SIDMA-style builds;
6. a page-by-page visual audit; and
7. a read-only publication-presentation review with zero blockers and majors.

Passing these gates permits the status `TARGET_A_PUBLICATION_LATEX_READY`.
It does not permit `TARGET_A_SUBMISSION_READY`; author metadata, archive DOI,
and final journal selection remain external decisions.
