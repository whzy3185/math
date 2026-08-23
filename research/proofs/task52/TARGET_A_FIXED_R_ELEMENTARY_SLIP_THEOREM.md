# Fixed-r Elementary-Slip Theorem

Let `H=A^2`. The exact G6 theorem gives a normalized infinite-interface
eigenvector `psi` with `H psi=c6 psi` and cellwise decay bounded by
`C_psi (9/25)^|j|`.

## Theorem: fixed-r cluster existence

Fix `r>=1`. Construct a legal even ring with `r` G6 interfaces and minimum
bulk-cell separation `L`. Both holonomies and reflected orientations are
allowed. There are constants `C_r,L_r`, independent of the ring lengths,
such that for `L>=L_r`, `H` has at least `r` eigenvalues, counted with
multiplicity, in

```text
[c6-C_r(9/25)^L, c6+C_r(9/25)^L].
```

In particular this holds for the required cases `r=2` and `r=3`.

## Proof

Around each interface choose a radius less than half the nearest separation.
Transfer the exact isolated G6 mode into the local gauge and truncate it
before the neighboring interface and before the holonomy cut. Reflection is
a unitary coordinate reversal, and changing holonomy alters only a cut
outside every chosen core.

The finite propagation range of `H` and the exact decay estimate imply

```text
||(H-c6)phi_i|| <= C (9/25)^L,
|<phi_i,phi_j>| <= C (9/25)^L  (i != j).
```

After Gram orthonormalization, the span `V_L` has dimension `r` and

```text
||(H-c6)|_(V_L)|| <= C'_r (9/25)^L.
```

If the spectral projection of `H` onto the interval of radius
`2C'_r(9/25)^L` had rank below `r`, a nonzero vector in `V_L` would be
orthogonal to that projection. The spectral theorem would then give a
residual larger than the displayed upper bound, a contradiction. Absorbing
the factor two proves the theorem.

## What is not proved

The argument gives at least `r` levels, not exactly `r`. It does not exclude
other upper-gap eigenvalues and does not prove

```text
rho(A)^2 <= c6+C_r(9/25)^L.
```

Thus neither the strong target nor the sufficient global-cap target is
achieved. Deterministic full spectra for 40 rings (`r=1,...,4`, both
holonomies, five sizes) found the expected cluster and no hidden positive
upper-gap branch in the large-separation rows. Representative `r=2,3`
levels were independently refined with 80, 120, and 160 digit finite-ring
transfer Evans solves. These are HIGH_PRECISION/EXPERIMENTAL checks, not the
missing uniform count.

The `r=4` numerical stress test also retains four cluster levels, so the
formalism scales, but no `r=4` exact-count theorem is asserted.

Artifacts:

- `../../experiments/task52/fixed_r_full_spectrum_scan.json`;
- `../../experiments/task52/fixed_r_high_precision_evans.json`.

Status: `FIXED_R_R23_CLUSTER_PROVED_GLOBAL_CAP_PARTIAL`.
