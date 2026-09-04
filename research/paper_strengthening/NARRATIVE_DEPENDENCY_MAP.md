# Narrative dependency map

| section | mathematical question inherited | answer | question created |
|---|---|---|---|
| 1. Introduction | how small can the signed adjacency radius be on a fixed support? | switching makes cycle flux the relevant variable; the cycle square has local triangles and periodic Fourier structure; period eight is the first rigid sub-eight phase | how are the invariant coordinates and finite fibers constructed? |
| 2. Switching coordinates and periodic fibers | how do local flux, global holonomy, symmetry, and cell phase remain distinct? | Hamilton gauge gives `(tau,alpha)`; finite cell translation gives `z^L=alpha`; lift/dihedral/zone-folding invariance fixes the classification conventions | which coefficient structure can reduce an individual fiber? |
| 3. Half-cell chiral symmetry | when does signed half-translation force zero-symmetric spectrum? | half-antiperiodic `tau` is equivalent to half-periodic `Q` with negative half-cell product and to a monomial chiral involution | chirality already occurs at period two; what extra structure makes a strict crossing solvable? |
| 4. Exact period-eight phase | can the first sub-eight phase be solved on finite rings? | additional centered-quartic symmetry gives four exact bands; two holonomies sample the same law; the positive sector beats twisted | why is eight the first effective period, and is its phase unique? |
| 5. First occurrence, rigidity, and defect constraints | what excludes shorter periods and competing first-period phases? | moments measure density and near clustering; cyclic-gap reduction plus exact certificates gives minimal period and rigidity; the same formulas yield arbitrary-period necessary bounds | does the attained radius equal the unrestricted fixed-graph minimum? |
| 6. Concluding remarks | what remains after the periodic mechanism is closed? | isolate the global minimum and equality-class problem without reopening all-even classification | none |

## Proof dependencies

```text
switching -> (tau, alpha) -> finite Bloch fibers

negative half-cell Q flux
 <-> half-antiperiodic tau
 <-> normalized monomial chiral involution
 -> 2m to m squared reduction

period-eight specialization
 -> explicit UV product
 -> centered quartic
 -> four bands and exact gaps
 -> two finite holonomy radii
 -> twisted comparison

local square
 -> M1, M2, four-class M3 expansion
 -> density/clustering inequalities
 -> cyclic-gap survivor completeness
 -> exact Rayleigh table
 -> smallest primitive period

period-eight two-defect separations
 -> integer recurrence
 -> trichotomy
 -> unique first sub-eight orbit
```

## Deletion decisions

- The independent general-moment section was merged into Section 5 because it
  repeated formulas already needed there.
- The half-cell box diagram was removed because the coefficient identity is
  clearer than the graphic.
- A defect-orbit figure was added because it makes the four period-eight
  geometries and the antipodal survivor immediately visible.
- Related work stays inside the Introduction at the exact point where it
  supports a problem transition.
