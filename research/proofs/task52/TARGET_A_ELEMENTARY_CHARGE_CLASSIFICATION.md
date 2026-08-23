# Elementary Charged-Interface Classification

## Certified single-gap comparisons

The common interval-Evans kernel proves unique localized roots in the stored
rational intervals for gaps 2, 3, 8, and 12. Task 50 supplies gaps 6 and 10.
Exact interval ordering yields

```text
c_(-2)>8,
c_(-1)>c6,
c_(+4)>c6,
c_(+6)>c6,
c_(+8)>c6.
```

Thus G6 is rigorously cheaper than every currently competitive single-gap
positive even charge in the requested list.

## Gap-plus-eight recurrence

For fixed `g mod 8`, let `D_g` be the Task 50 defect transfer. Write `A_g`
for the common prefix through the old right endpoint, `R_g` for the old
right-bulk eight-step factor, `N_g` for the eight negative-`Q` steps inserted
when the endpoint moves from `g` to `g+8`, and `R'_g` for the restored right
bulk. Then

```text
D_g       = R_g A_g,
D_(g+8)   = R'_g N_g A_g
          = C_g D_g,
C_g       = R'_g N_g R_g^(-1).
```

Every entry has degree at most 32. The certificate checks each matrix
identity at 33 distinct integer values of `lambda` using arbitrary-precision
integers, which proves the polynomial identity. Each factor is invertible
and `det C_g=1`. Acting on two-planes gives a six-dimensional exterior-square
orbit, so every fixed-residue matching sequence satisfies a
Cayley-Hamilton recurrence of order at most six.

The simpler proposed identity `D_(g+8)=M8 D_g` is false in the fixed cut:
the inserted region consists of eight negative `Q` sites and replaces the
old right-bulk block before the cut is restored. Root ordering along the
new recurrence remains open.

## Primitive multi-gap threat search

A finite interface word is a linear sequence of abnormal gaps. Translation
puts its left endpoint at zero; reflection reverses the word. The bounded
search calls a word decomposable if it contains an internal gap 4 or a
proper contiguous zero-charge subword. It exhausts gaps `1,...,12` other
than 4, word length at most four, and charges `-2,+2,+4,+6`. There are
`42,134,182,248` canonical primitive words in these four classes.

Double-window open-interface checks found no non-G6 word whose largest
localized level is below `c6`. The best words by charge are `[3,3]`, `[6]`,
`[8]`, and `[10]`, respectively. A separate scan of every single gap from
13 through 76 found no cost below `c6`; its best case was gap 14 at about
`8.01794579`.

These searches are deterministic bounded evidence. They do not classify
arbitrary support, arbitrary gap size, or all decompositions. Consequently
neither completeness option in Task 52 is met.

Machine artifacts:

- `certificates/single_gap_exact_comparisons.json`;
- `certificates/charge_recurrence.json`;
- `../../experiments/task52/primitive_interface_search.json`;
- `../../experiments/task52/large_gap_scan.json`.

Status: `PLUS_TWO_UNIQUE_ELEMENTARY_EVEN_CHARGE_STRONGLY_SUPPORTED`.
