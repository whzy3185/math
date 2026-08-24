# Proof Overview

The proof replaces physical-root ordering by a compactly supported
variational argument.

## 1. Remove lift and orientation choices

The two `tau` lifts are related after squaring by a diagonal unitary, and
reflection is a unitary equivalence. It is enough to treat the canonical
forward lift.

## 2. Convert a vector into an exact spectral lower bound

For finitely supported integer `v`, compute `A_gv` on the full image window.
Then

```text
<v,H_gv>/<v,v>=||A_gv||^2/||v||^2=N/D.
```

The variational principle gives `sup sigma(H_g)>=N/D`.

## 3. Close the six small gaps

Explicit integer vectors cover `g=1,2,3,5,7,8`. Their exact Rayleigh
quotients all exceed the rational number in equation (3) of the theorem
statement. No decimal comparison is used.

## 4. Close every large gap with one vector

For `g>=9`, one fixed vector has support near the left endpoint. The right
defect affects its image only for `g=9,10`; all `g>=11` share the same local
calculation. The uniform lower bound is

```text
182/23>988671163952541/125000000000000.
```

## 5. Insert the equality case

The global one-G6 theorem supplies `sup sigma(H_6)=c6` and rank two. The
period-eight reference theorem supplies `sup sigma(H_4)=eta<c6`, explaining
why gap four is excluded.

## Proof architecture

```text
local operator formula
  -> seven finite integer Rayleigh calculations
  -> exact rational comparisons
  -> variational consequence for all g
  -> inherited global equality at G6.
```

## Publication placement

- `MAIN_TEXT_REQUIRED`: the complete hierarchy theorem, finite-support
  Rayleigh lemma, rational quotient table, fixed `g>=9` witness, and strict
  uniform `1/250` corollary.
- `APPENDIX_REQUIRED`: full integer vectors, their complete images, and all
  raw cross-multiplication differences.
- `REPRODUCIBILITY_ONLY`: the JSON certificate, independent checker, and
  tamper-test records.
