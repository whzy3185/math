# Stale Rank-Claim Scan Method

## Frozen scan base

The scan was run against the tracked repository at

```text
e6a01d8bf30088dae1042a237398bee2df138280
```

using `git grep`, so untracked proof-completion work was not mistaken for
historical source material. The formal English and Chinese manuscript trees
were included in the scan.

## Concepts

The case-insensitive fixed-string scan covered:

```text
rank one / rank-one / rank-r / rank-`r`
exact-r / exact-`r` / exactly `r`
r-dimensional / `r`-dimensional
r x r / r times r / I_r
codimension-r / codimension-`r`
one-mode-per-interface / one localized mode
unique simple H6 / simple c6 eigenvalue
```

Generic phrases such as "exact rational" and unrelated phrases such as
"four-dimensional transfer" were excluded from the relevant set.

## Classification rule

- `CURRENT_CORRECT`: the occurrence states the corrected rank-two/exact-`2r`
  theorem, rejects the old claim, or uses `r` for a non-spectral count.
- `HISTORICAL_SUPERSEDED`: the file preserves an old proof attempt or review
  and is explicitly superseded/withdrawn in the canonical layer.
- `MUST_UPDATE_BEFORE_MANUSCRIPT`: the line could be imported as current
  mathematics and still contains a dimensionally stale formulation.
- `SAFE_INTERNAL_ARCHIVE`: the occurrence is inside a retraction artifact,
  tamper test, or fail-closed forbidden-token check.

## Result

```text
tracked files scanned:              2,486
relevant files:                        46
relevant line occurrences:            111

CURRENT_CORRECT:                        51
HISTORICAL_SUPERSEDED:                  52
MUST_UPDATE_BEFORE_MANUSCRIPT:           2
SAFE_INTERNAL_ARCHIVE:                   6
```

No positive exact-`r`, codimension-`r`, rank-one G6, or `r x r` Feshbach
claim occurs in either frozen formal manuscript. Historical files were not
rewritten.
