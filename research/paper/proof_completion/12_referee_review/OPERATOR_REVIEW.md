# Hostile Operator-Theory Review

## Verdict

`PASS` for the IMS/residue and exact-`2r` statements at their declared
evidence levels.

## IMS

The double-commutator identity has the correct sign and is verified entrywise.
The cyclic cutoff family is an exact partition of unity. The squared operator
has propagation range four, and the exact offset weights yield

```text
||E_IMS||
 <=(240R-342)/(R(2R^2+1))
 <=120/R^2.
```

The support assumptions `R>=4`, `2(R+4)<D`, and `n>2R+4` are stated. The
patch theorem then controls every localized quadratic form by `c6`; taking a
supremum controls the full finite-ring spectrum.

## Exact-2r

The low-energy space contains both squared modes from every G6 interface.
Gram control gives `2r` independent quasimodes; the codimension-`2r`
complement gap gives the upper count; min-max gives exact multiplicity. The
Feshbach map acts on a `2r`-dimensional space. No unproved finite-ring
simplicity or interaction coefficient is inferred.

## Residue theorem

The proof is correctly one-sided. Explicit competitors and a vanishing IMS
error imply only

```text
limsup m_(8k+s)^2<=c6.
```

No lower limit, common limit, or universal interface theorem is smuggled into
the argument.

## Scope warning

The exponential `3505r` estimate and the elementary IMS cap are distinct
tools. The qualitative residue `limsup` needs only the latter and therefore
does not inherit unnecessary exact-`2r` hypotheses.
