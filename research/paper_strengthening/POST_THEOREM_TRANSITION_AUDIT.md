# Post-theorem transition audit

## Scope

Eight already-collected full-text JGT papers were reread for the prose that
surrounds major theorems.  The audit concerns rhetorical function and
mathematical organization, not sentence imitation.

## Corpus observations

### Li--Feng--Peng

The main result is followed by comparison with the classical edge theorem,
an explanation of why the spectral hypothesis changes the extremal picture,
and a discussion of sharp examples.  The next result is motivated by the
specific phenomenon exposed by that comparison.  The authors spend several
paragraphs around a main theorem, but little prose after routine lemmas.

**Applicable pattern:** exact statement -> classical/benchmark comparison ->
sharpness or extremal mechanism -> new question.

### Albrechtsen--Jacobs--Knappe--Pitz

Negative and positive results are placed next to one another.  Their boundary
is compared explicitly, which exposes a narrow unresolved gap.  That gap,
rather than a roadmap sentence, produces the next structural question.  Short
remarks are used only when a distinction changes the problem.

**Applicable pattern:** obstruction -> surviving positive statement -> exact
boundary -> remaining question.

### Li--Zhao--Zou

After the first extremal theorem, the text records which earlier conjecture or
special case follows and what part of the family remains untreated.  The
second main result is presented as the answer to that residue.  Equality cases
are part of the theorem proof rather than detached commentary.

**Applicable pattern:** theorem -> consequence for prior problem -> residual
case -> second theorem.

### Guo--Spiro

The authors pause after the main bounds to test equality, compare with other
bounds, and give examples in both directions.  The comparison section is
substantive and longer than the organization paragraph.  A more general
theorem is introduced because the proof mechanism naturally extends, not
because another result is needed for volume.

**Applicable pattern:** theorem -> tight examples -> comparison/incomparability
-> precise extension.

### Fang--Lin--Shi

Several headline theorems are stated together in the Introduction, but their
proofs are kept in uninterrupted theorem-specific arcs.  Discussion is
concentrated before and after a full arc rather than inserted after each
technical claim.  The extremal graph and equality analysis carry the
interpretation.

**Applicable pattern:** cluster related headline statements -> one complete
proof arc -> equality meaning.

### Horn--Purcilly--Stevens

A general analytic inequality is followed by graph-theoretic corollaries and
examples showing what the inequality detects.  The transition to applications
comes from the local content of the bound.  No separate generic conclusion is
needed after each corollary.

**Applicable pattern:** general tool -> what its terms measure -> graph
consequences -> examples/limitations.

### Steinerberger--Thomas

General optimization statements are interpreted through symmetry, spectral
embeddings, and exact certificates.  Certificate machinery receives prose
explaining what the certificate means and how it can be checked.  Computation
is persuasive only after the mathematical object and verification condition
are explicit.

**Applicable pattern:** structural theorem -> geometric/algebraic meaning ->
certificate criterion -> exact examples.

### Goedgebeur--Renders--Wiener--Zamfirescu

Finite computation enters only after a structural construction or order
reduction.  Tables close a domain already proved complete.  The text then says
which orders are settled and isolates the few unresolved ones.  Algorithms
and larger certificates are separated from the conceptual proof.

**Applicable pattern:** completeness reduction -> finite table/certificate ->
settled range -> remaining exceptions.

## Frozen transition patterns for this manuscript

### Exact finite radius

```text
exact equality on every positive-holonomy finite ring
 -> attained value, not an asymptotic estimate
 -> strict twisted comparison for L >= 4
 -> exact value alone does not identify the solvable structure
 -> inspect the half-period sign reversal.
```

### General half-cell theorem

```text
alternating sign times half translation
 -> operator anticommutation
 -> equivalent negative half-cell flux condition
 -> chiral symmetry is readable from switching-invariant local cycles
 -> period-two is already chiral but has edge 8
 -> ask when chirality first becomes spectrally effective.
```

### Complete period-eight dispersion

```text
general dimension halving
 -> additional centered-quartic symmetry at period eight
 -> four exact bands and gaps
 -> two holonomies sample one dispersion on different phase grids
 -> solvability still does not explain first occurrence.
```

### Minimal primitive period

```text
moment and exact-certificate exclusion below period eight
 -> chirality predates the strict crossing
 -> period eight is selected by spectral effectiveness
 -> ask whether the first effective period contains more than one phase.
```

### Period-eight rigidity

```text
unique dihedral Q orbit below eight
 -> low moments penalize density and near clustering
 -> the survivor has two maximally separated defects
 -> compatible short-period geometry, not an all-period sufficiency claim
 -> return to the general necessary obstruction.
```

### General moment obstruction

```text
arbitrary-period necessary inequalities
 -> density and clustering interpretation
 -> no general minimizer classification
 -> isolate the true fixed-graph minimum as the concluding problem.
```

## Style consequences

- No paragraph is added after a routine lemma merely to satisfy a template.
- A major theorem receives discussion only when the reader's mathematical
  question changes.
- Remarks are reserved for a genuine distinction such as displayed versus
  primitive period or `Q` orbit versus its two `tau` lifts.
- “The next section” and similar roadmap connectors are replaced by the
  unresolved mathematical fact itself.
- Exact tables appear after a completeness lemma, never as discovery output.

```text
POST_THEOREM_TRANSITION_PATTERNS_FROZEN
```
