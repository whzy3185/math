# Target A Specification — Signed Circulants

Target：C029

Source：[Vaibhav Suvagiya, *Signed circulants at the Ramanujan bound*, arXiv:2607.18334](https://arxiv.org/abs/2607.18334), Conjecture 3
规格状态：FORMALIZED；尚未执行大规模搜索。

## Definition

### Underlying graph

For an integer `n≥8`, let

`V_n = Z/nZ`,

and let `G_n=C_n(1,2)` be the undirected simple graph with edge set

`E_n = {{i,i+1}:i∈V_n} ∪ {{i,i+2}:i∈V_n}`,

where all indices are modulo `n`. For `n≥8`, the two displayed edge families are disjoint and `|E_n|=2n`.

### Signing and signed adjacency matrix

A signing is a function `σ:E_n→{−1,+1}`. Its signed adjacency matrix `A_σ∈Z^{n×n}` is

`(A_σ)_{ij}=σ({i,j})` if `{i,j}∈E_n`, and `0` otherwise.

It is real symmetric. Define

`ρ(A_σ)=max{|λ|: λ is an eigenvalue of A_σ}`.

### Switching

For `d:V_n→{−1,+1}`, switching by `d` sends

`σ({i,j}) ↦ d(i)σ({i,j})d(j)`.

If `D=diag(d(0),…,d(n−1))`, the new matrix is `DA_σD`, so its spectrum and spectral radius are unchanged. Since `G_n` is connected and has `2n` edges, it has exactly `2^{2n-n+1}=2^{n+1}` switching classes.

### Distinguished threshold

For even `n≥8`, define the exact algebraic number

`ρ_−(n)=2 sqrt(cos²(π/n)+cos²(2π/n))`.

This is the spectral radius of either twisted class with alternating triangle flux and step-1 Hamilton-cycle holonomy `α=−1`.

## Domain

- `n` is an even integer with `n≥8`.
- `σ` ranges over every signing of `E_n`, equivalently every switching class.
- No quadrilateral-flux restriction is imposed on the competitor `σ`; that restriction only describes the distinguished four-class family containing the conjectured optimizer.

## Hypotheses

For an instance `(n,σ)`:

1. `n` is even and `n≥8`.
2. `σ` assigns exactly one value in `{−1,+1}` to every undirected edge of `G_n`.
3. `A_σ` is constructed from that signing without dropping the wrap-around edges.

## Claimed conclusion

For every even `n≥8` and every signing `σ:E_n→{−1,+1}`,

`ρ(A_σ) ≥ ρ_−(n)`.

Equivalently,

`min_{σ:E_n→{−1,+1}} ρ(A_σ)=ρ_−(n)`.

The upper bound/equality witness is already established in the source; the unproved part is the global lower bound over all switching classes.

## Counterexample condition

`Counterexample(n,σ) :=`

`Even(n) AND n≥8`

`AND σ∈{−1,+1}^{E_n}`

`AND ρ(A_σ) < ρ_−(n)`.

Equality is not a counterexample. A floating approximation below the threshold is only a candidate until the strict algebraic inequality is certified.

## Equivalent formulations

### Switching-class formulation

It suffices to test one representative of each switching class. A representative can be fixed by choosing a spanning tree and switching all tree-edge signs to `+1`; the remaining `n+1` chord signs encode a class.

### Cycle-flux formulation

Let `T_i=(i,i+1,i+2)` and let `H` be the step-1 Hamilton cycle. The signs of the `n` triangles together with the sign `α` of `H` form coordinates on the `n+1`-dimensional cycle space. Therefore every switching class can be encoded by

`(τ_0,…,τ_{n−1},α)∈{−1,+1}^{n+1}`.

The conjectured optimizing classes have `τ_{i+1}=−τ_i` and `α=−1`.

### Squared formulation

Because both sides are nonnegative,

`ρ(A_σ)<ρ_−(n)` iff

`λ_max(A_σ²) < 4(cos²(π/n)+cos²(2π/n))`.

This can be useful for exact algebraic comparison, but `A_σ²` must still be handled exactly.

### Characteristic-polynomial certificate

Let `p_σ(x)=det(xI−A_σ)∈Z[x]`. A counterexample certificate may consist of `σ`, `p_σ`, isolating intervals for every extreme real root of `p_σ`, and an exact isolating representation of `ρ_−(n)` proving both extreme roots lie strictly inside `(-ρ_−(n),ρ_−(n))`.

## Invariants

For every candidate record:

- `n` and the ordered signs of all step-1 and step-2 edges;
- the canonical switching representative;
- triangle flux vector `(τ_i)`;
- Hamilton holonomy `α`;
- dihedral orbit representative and orbit size;
- `trace(A_σ^{2k})` for selected small `k` as cheap exact filters;
- characteristic polynomial and determinant;
- exact spectral radius;
- exact comparison sign of `ρ(A_σ)−ρ_−(n)`.

## Degenerate cases

- `n` odd is outside the conjecture; the alternating quadrilateral system is inconsistent there.
- `n<8` is outside the stated domain and has edge coincidences/small-cycle degeneracies.
- At `n=8`, `C_8(1,2)` has two additional step-2 quadrilaterals. The conjecture remains stated and verified there, but a verifier must not confuse system (1)'s eight `Q_i` constraints with the stronger all-ten-quadrilateral system.
- A signing in the four-class quadrilateral family is not automatically the global optimizer; only its `α=−1` classes attain `ρ_−(n)` within that family.
- Global negation `σ↦−σ` negates `A_σ` and preserves spectral radius, but its action on cycle flux depends on cycle parity.

## Symmetries

Safe reductions, each of which must be tested independently:

1. vertex switching (`A↦DAD`);
2. rotations and reflections of `Z/nZ` (dihedral automorphisms);
3. global sign negation (`A↦−A`);
4. compositions of the above.

No other edge permutation is allowed unless proved to be an automorphism of `C_n(1,2)`. Canonicalization must preserve at least one representative of every switching class.

## Known theorems and verified range

From the source paper:

1. for even `n≥10`, the all-`Q_i`-unbalanced system has exactly four switching classes;
2. its classes are parametrized by `(τ_0,α)`, and spectral radius depends only on `α`;
3. `α=+1` gives `2√2`, while `α=−1` gives `ρ_−(n)<2√2`;
4. the same spectral conclusions hold at `n=8` with the paper's stated convention;
5. the global conjecture was exhaustively checked numerically for `n∈{8,10,12,14,16,18}` with agreement to `10^-9`.

The final item is **Observed/Reported**, not yet independently reproduced by this project and not an exact proof of the strict comparisons.

## Exact verifier specification

Define `verify_counterexample(candidate)` with candidate fields `n` and a complete edge-sign map.

The verifier must:

1. reject unless `n` is even and `n≥8`;
2. construct `E_n` independently and reject missing, duplicate or non-`±1` signs;
3. build the integer symmetric matrix `A_σ` independently of the searcher's matrix code;
4. compute `ρ(A_σ)` as an exact real algebraic number (for example Sage `AA`, or characteristic polynomial + Sturm/root-isolation certificate);
5. construct `ρ_−(n)` as an exact real algebraic number, not from binary floating cosine;
6. compare the two algebraic numbers exactly;
7. return `True` only when the strict inequality `ρ(A_σ)<ρ_−(n)` is certified;
8. output the canonical signing, flux invariants, characteristic polynomial, exact isolating data and a SHA-256 checksum of the serialized candidate.

Pseudocode:

```text
verify_counterexample(c):
    require even(c.n) and c.n >= 8
    E := exact_edges_Cn12(c.n)
    require keys(c.signs) == E
    require every sign is exactly +1 or -1
    A := exact_integer_signed_adjacency(E, c.signs)
    rho := exact_max_abs_real_root(charpoly(A))
    threshold := exact_algebraic(2*sqrt(cos(pi/c.n)^2 + cos(2*pi/c.n)^2))
    result := exact_compare(rho, threshold) < 0
    emit certificate and invariants
    return result
```

Any implementation that silently falls back to floating-point eigenvalues is non-conforming.

## Search boundary for the next stages

Prompt 6 must first reproduce the paper's four-class formulas and reported global minima for `n=8,10,…,18`. Only after an exact `PASS` may Prompt 7 design the `n=20` search. No large-scale search has been run in the present stage.
