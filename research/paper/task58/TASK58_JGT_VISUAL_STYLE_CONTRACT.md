# Task 58 JGT Visual-Style Contract

Status: `TASK58_FIRST_SUBMISSION_CONTROL`.

This contract governs the visual and typographic construction of the Task 58
English first submission. Its aim is a restrained, theorem-driven graph theory
paper compatible with ordinary journal production. It does not reproduce or
imitate proprietary Wiley or JGT page design, logos, branding, running heads,
or house-style assets.

## 1. Design principle

The paper should resemble mature work in four broad traditions:

- complete spectral classification papers;
- signed spectral structure papers;
- structural extremal graph papers;
- computer-assisted classification papers.

These are genre references only. The manuscript must use conventional LaTeX
structure and its own mathematical content, not copied journal typography or
page furniture. Mathematical hierarchy, not decoration, supplies emphasis.

## 2. Typography and fonts

- Use a conventional serif body face with a matched mathematical font.
- Prefer a verified Wiley/JGT-compatible template if one is legitimately
  available; otherwise use a conservative standard LaTeX article setup.
- Retain the document class's ordinary title, author, abstract, heading,
  bibliography, and page-number conventions.
- Use upright roman type for operators and definitions where standard, italic
  mathematical variables, and consistent boldface only for established
  vector or matrix notation.
- Keep body size, leading, margins, and display spacing at normal article
  values. Do not use custom font files, `fontspec` without a technical need,
  sans-serif body copy, presentation fonts, handwritten fonts, decorative
  theorem fonts, or manually forced title typography.
- Do not imitate publisher-owned mastheads, logos, exact page furniture, or
  proprietary production fonts.

Page pressure must be solved by editorial deletion and proof placement, never
by shrinking the global font, tightening line spacing, narrowing margins,
scaling whole pages, or applying negative vertical-space tricks.

## 3. Theorem hierarchy

Use only conventional environments:

```text
Theorem
Proposition
Lemma
Corollary
Definition
Remark
Proof
```

The main classification and the reference/single-gap spectral hierarchy may
have descriptive names inside ordinary theorem environments. Do not create
`Key Result`, `Main Insight`, `Contribution`, `Structural Fact Box`, or
`Computer Certificate Box` environments. Proofs use the standard proof
environment and QED marker.

Theorem numbering must follow a stable section-based or journal-template
scheme. Cross-references use names and numbers, not color-coded labels,
internal claim IDs, research-task numbers, or status badges.

## 4. Mathematical display and prose density

- Write dense but readable mathematical prose in normal paragraphs.
- Avoid one-sentence paragraphs, long bullet inventories, numerous tiny
  subsections, and slide-like exposition.
- Display an equation when its structure benefits from isolation. Keep routine
  algebra inline when readability permits.
- Number only formulas cited later or structurally important to a proof.
- Align multi-line derivations by mathematical relation; do not use displays
  as decorative whitespace.
- Avoid repeated `\boxed{...}`, oversized delimiters without need, and manual
  font-size changes inside mathematics.
- Keep theorem statements concise; definitions and hypotheses must remain
  complete even when the page is dense.
- Keep enough whitespace to distinguish theorem, proof, display, and paragraph
  boundaries. Density must come from disciplined exposition, not compression.

The main narrative should normally occupy about 28--34 pages. The paper with
essential appendices should be at most 45 pages whenever feasible. The
reproducibility supplement is counted separately.

## 5. Figure budget and mathematical purpose

The main paper may contain at most three main figures. Every figure must
perform a specific mathematical function:

1. The signed square of a cycle together with switching and flux coordinates.
2. The period-eight reference phase, the G6 interface, and the legal one-,
   two-, and three-slip residue constructions.
3. Finite-ring localization and its identification with an infinite G6 patch.

The second figure and its caption must visibly distinguish the closure law
`sum q_j congruent to n (mod 8)` from the sector law
`sigma_sec(q)=q (mod 4)`.

Do not include a paper-story flowchart, proof-dependency flowchart, software
pipeline, generator/certificate/checker diagram, task chronology, decorative
numerical plot, or exact-`2r` geometry in the main text. Exact-`2r` geometry
may appear in the supplement only if it materially shortens or clarifies the
proof there.

## 6. Figure execution

- Prefer TikZ or comparable vector line art generated from manuscript source.
- Use black, white, and grayscale only, with thin and visually uniform strokes.
- Encode signed edges by solid/dashed strokes or explicit `+`/`-` labels; no
  mathematical distinction may depend on color.
- Use restrained arrows, vertices, braces, and panel dividers. Avoid gradients,
  shadows, textures, icons, perspective effects, and ornamental backgrounds.
- Keep panel labels short and consistent, ordinarily `(a)`, `(b)`, `(c)`.
- Use the manuscript's mathematical fonts for symbols and minimal internal
  labels. Do not place explanatory paragraphs inside figures.
- Figures must remain legible in grayscale and at 100 percent PDF scale. Line
  weights, label sizes, and dash patterns must survive ordinary print output.
- Use stable dimensions and aspect ratios so later label changes do not disturb
  page layout.

## 7. Captions

Captions are concise, mathematical, and descriptive. They identify the object,
the convention needed to read it, and any panel correspondence. A caption may
define a local symbol but must not become a second proof or advertise novelty.

Preferred form:

```text
The reference phase and the one-, two-, and three-slip constructions.
```

Avoid promotional or tutorial phrasing such as “This figure visually
illustrates our novel framework.” Captions must be understandable in black and
white and must not refer to color alone.

## 8. Tables

- Use at most one or two tables in the main text, only when they improve exact
  comparison or classification.
- The preferred main table records order ranges, conclusions, and proof
  mechanisms for the classification partition.
- Use an ordinary LaTeX table; use restrained `booktabs` rules when compatible
  with the document class.
- Avoid vertical rules, colored or shaded cells, status icons, dashboards,
  oversized headers, and software metadata tables.
- Keep captions short and place detailed certificate metadata in the
  reproducibility supplement.
- Align mathematical quantities consistently and do not reduce table type to
  an abnormally small size to force a fit.

## 9. Prohibited visual devices

The manuscript and mathematical appendices must not use:

- infographic or software-architecture diagrams;
- contribution cards, UI cards, colored banners, or large icons;
- decorative theorem boxes, including `tcolorbox` or `mdframed` result panels;
- gradients, shadows, background ornaments, or full-width promotional panels;
- oversized headings or display-type pull quotes;
- excessive whitespace, slide-style fragments, or one-claim-per-page layouts;
- typography compression, global scaling, negative-spacing hacks, or narrowed
  margins used to meet the page target;
- footnotes.

In scan-contract form: no infographic, no software diagram, no decorative
boxes, and no footnotes.

Necessary qualifications belong in the prose, a remark, or an appendix.
Bibliographic and data/code details belong in their dedicated sections rather
than footnotes.

## 10. Appendices and supplement

The first-submission placement policy is:

| Location | Material |
|---|---|
| Main paper | Complete classification, candidate attainment, reference phase, gap/charge laws, G6 mechanism, single-gap hierarchy, finite-ring IMS/residue constructions, finite completion, and only a statement plus short overview of exact-`2r`. |
| Appendix A | Algebraic certification of the G6 spectral edge. |
| Appendix B | Mathematical completeness and exact finite classification. |
| Optional Appendix C | Separated phase-slip spectral refinement only if the complete paper remains within the page target. |
| Reproducibility supplement | Certificate schemas, manifests, hashes, checker commands and versions, expected outputs, tamper tests, resource notes, and any exact-`2r` details removed from Appendix C. |

The supplement is functional technical documentation, not an excuse to omit a
mathematical reduction or completeness proof from the paper. A reader must be
able to understand why each finite object is exhaustive before consulting
software artifacts.

The following material is outside the first-submission design entirely:
bounded periodic-frontier material through `p<=24`, period-25/26 results,
general moments, the multi-gap obstruction package, the reference graph,
interaction fits, and research-correction history.

## 11. Automatic page-budget response

If the paper with essential appendices exceeds 45 pages, move material in this
order:

1. the complete exact-`2r` Gram, complement-gap, Feshbach, and constant proofs
   to the reproducibility supplement;
2. complete integer-vector tables for the single-gap comparisons to the
   supplement;
3. certificate schemas, hashes, commands, and resource details to the
   supplement;
4. compress the exposition of the G6 algebraic certificate without removing
   its mathematical completeness or exact endpoint logic.

Never shorten by weakening the main classification theorem, candidate
attainment, the reference-phase theorem, the G6 hierarchy, the distinction
between mod-eight closure and mod-four sector shift, the IMS mechanism, the
34--46 completeness argument, the 48--238 exact bridge, or the final exhaustive
partition.

## 12. Visual acceptance checklist

- [ ] Conventional serif text and matched mathematics; no proprietary design imitation.
- [ ] Conventional theorem environments and standard proof endings.
- [ ] Formula numbers are limited to referenced or structurally important displays.
- [ ] Paragraph and page density are mature and readable, without compression.
- [ ] No more than three mathematically necessary main-text figures.
- [ ] Every figure is black-and-white vector art and readable at print scale.
- [ ] Captions are concise and non-promotional.
- [ ] Main-text tables number at most two and use restrained mathematical styling.
- [ ] No infographic, software diagram, decorative box, status badge, or color-dependent encoding.
- [ ] No footnotes.
- [ ] Main narrative is approximately 28--34 pages and paper plus essential appendices is at most 45 pages whenever feasible.
- [ ] Appendix and supplement placement follows the locked first-submission scope.
- [ ] Page limits are met by editorial placement, never typographic compression.
