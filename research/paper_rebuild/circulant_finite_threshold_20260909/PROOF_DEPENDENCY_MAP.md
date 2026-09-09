# Proof dependency map

This paper is self-contained with respect to the separate branch `paper/circulant-periodic-gap-20260909`: no theorem, notation, construction, or asymptotic statement from that project is used.

The only substantial external classification theorem used below is Greaves--Koolen--Munemasa--Sano--Taniguchi (JCTB 110 (2015)) in the strict sub-`sqrt(6)` section.

## A. Finite signed-graph preliminaries

`switching invariance`
→ Hamilton-path gauge for `C_N(1,s)`
→ every labelled switching class has one normalized representative described by Hamilton holonomy `alpha` and the remaining chord signs.

`tr(A^2)=4N`
→ `rho(A)>=2`
→ equality iff `A^2=4I`.

Define throughout

`B=A^2-4I`,

so

`rho(A)^2=4+lambda_max(B)`.

## B. Parity-defect engine

Over `F_2[Z_N]`,

`(x+x^-1+x^s+x^-s)^2=x^2+x^-2+x^(2s)+x^(-2s)`.

Hence

```text
supp(B mod 2) = empty                         if N=2s+2,
                 Cay(Z_N,{+-2})               if N=4s,
                 Cay(Z_N,{+-2,+-2s})          otherwise.
```

This single identity drives the complete low-end classification.

### B1. Flat line

`B=0`
→ parity support empty
→ `N=2s+2`.

Explicit alternating signing
→ `B=0`
→ `m(N,s)=2`.

Mixed channel
→ two labelled equality switching classes except `(8,3)`.

`(8,3)=K4,4`
→ Hadamard block condition
→ six labelled switching classes, one switching-isomorphism orbit.

### B2. First gaps

Outside flat line, `B` is a nonzero integral symmetric zero-diagonal matrix.

nonzero `2x2` block
→ `lambda_max(B)>=1`
→ `rho(A)^2>=5`.

Equality `lambda_max(B)=1`
→ `I-B>=0`
→ support components are negative cliques up to switching
→ parity support forces `N=5,10`
→ exact liftability
→ `m=sqrt(5)` exactly at `(5,2),(10,3)`.

Integral defect below `sqrt(2)`
→ induced `P3` obstruction
→ negative-clique support
→ no value strictly between `1` and `sqrt(2)`.

Equality at `sqrt(2)` plus parity support
→ unique pair `(8,2)`.

### B3. Exact `N=4s` family

On `N=4s`, if defect index is below `2`, parity forces `B` to be exactly two signed cycles of length `2s`.

signed-cycle spectrum
→ lower bound `2 cos(pi/(2s))` for defect index.

anti-periodic signed shift `T^(4s)=-I`
+ alternating diagonal `D`, `DT=-TD`
→ `A^2=4I+T^2+T^-2`
→ finite roots `z^(4s)=-1`
→ exact attainment.

Therefore

`m(4s,s)^2=4+2 cos(pi/(2s))`.

Vanishing mixed and `2s` channels
→ exactly two labelled minimizing switching classes.

## C. Complete strict sub-`sqrt(6)` classification

Assume a generic pair (`N!=2s+2,4s`) has `rho(A)^2<6`.

`lambda_max(B)<2`
+ `2x2` interlacing
+ integrality
→ every entry of `B` is `0,+-1`
→ parity fixes the support exactly:

`B` is a signing of `P_Ns=Cay(Z_N,{+-2,+-2s})`.

Let `d=gcd(N,2)` and `q=N/d`.

`P_Ns`
→ `d` connected 4-regular circulant components, each of order `q`.

For a signed component `C`:

`lambda_max(C)<2`
→ signed graph `-C` has smallest eigenvalue `>-2`.

### C1. External structural reduction

Greaves--Koolen--Munemasa--Sano--Taniguchi:

- Theorem 19: exceptional signed graphs with smallest eigenvalue `>-2` have orders only `6,7,8`;
- Theorem 6: every integral case has a tree, unicyclic, or one-double-edge representation graph.

Internal 4-regular degree audit:

- simple tree line graph: degree sums `6` → only `K_1,5` → `K5`;
- unicyclic representation: no 4-regular case;
- doubled edge `ab`: parallel-edge line-graph degree is `d(a)+d(b)-3`; 4-regularity gives `d(a)+d(b)=7`; leaf propagation again forces the five-edge multistar whose line graph is `K5`.

Therefore a strict sub-2 4-regular signed component has order at most `8`, except the already order-5 `K5` case. Hence

`q<=8`.

### C2. Exact small components

`q=5`: `K5`
→ unique sub-2 class, all-negative up to switching, index `1`.

`q=6`: `C6(1,2)`
→ sub-2 would force all eight triangles negative
→ unique tree-gauge solution has charpoly `x^3(x-2)^2(x+4)`
→ index exactly `2`
→ impossible strictly below 2.

`q=7`: `C7(1,2)cong overline(C7)`
→ all seven triangles negative
→ exactly two tree-gauge classes:

`(x+4)(x^3-2x^2-x+1)^2`,

`x(x^3-7x+7)^2`.

Only second class is sub-2. Put `beta=maxroot(x^3-7x+7)`.
→ exact component minimum `beta` and unique labelled sub-2 switching class.

`q=8`:
- `C8(1,2)`: two all-negative-triangle classes have index `>2` and `=2`;
- `C8(1,3)=K4,4`: Frobenius/singular-value bound gives index `>=2`.

Therefore only component orders `5` and `7` lift.

### C3. Parameter lifting

`q=5`
→ `N=5,10`
→ prior first-gap lift analysis
→ only `(5,2),(10,3)`, both with `m^2=5`.

`q=7`, `N=7`
→ one mixed off-support two-walk channel must vanish
→ multiply the resulting sign recurrence around the odd cycle
→ `1=(-1)^7`
→ impossible.

`q=7`, `N=14`
→ sub-six mixed-channel vanishing forces `DT=-TD`
→ `D=epsilon diag((-1)^i)`
→ finite identity

`B=T^2+T^-2+(-1)^s(T^(2s)+T^(-2s))`, `T^14=alpha I`.

Exact finite shift factorization
→ defect polynomial `x^2(x^3-7x+7)^4` exactly for

`(s,alpha)=(3,-1),(4,-1),(5,+1)`.

Thus

`m(14,s)^2=4+beta`, `s=3,4,5`,

with exactly two labelled minimizers (`epsilon=+-1`), and `m(14,2)^2>=6`.

### C4. Complete theorem and odd-order corollary

Combining B1--B3 and C1--C3:

```text
m(N,s)^2<6 iff
  N=2s+2; or
  (N,s)=(5,2),(10,3); or
  N=4s; or
  N=14 and s in {3,4,5}.
```

Exact values are `4`, `5`, `4+2cos(pi/(2s))`, `4+beta` respectively.

Hence

`N odd, N>=7 => m(N,s)>=sqrt(6)` for every admissible `s`.

In particular

`k,s odd, k>=3, s>=3 => m(ks,s)>=sqrt(6)`.

### C5. Independent elementary route retained

There is also a self-contained weaker route avoiding Greaves:

`tr X=tr X^3=0`
→ cubic-moment inequality
→ a triangle-free forced parity support cannot occur below defect index `2`.

Classifying triangles in the reduced component yields, among other consequences,

`k odd>=5, s>=3 => m(ks,s)>=sqrt(6)`.

This proof is retained because it explains the arithmetic triangle mechanism even though C4 is globally stronger.

## D. All-even-order sub-`sqrt(8)` theorem

For `N` even choose anti-periodic signed shift `T^N=-I` and alternating diagonal `D`.

`DT=-TD`
→ finite square identity
→ finite Fourier on `z^N=-1`
→

`rho(A)^2<=6+2 cos(2pi/N)<8`.

Thus every even-order two-step circulant has a finite signing below `sqrt(8)`.

## E. Exact `N=3s` transition at `sqrt(8)`

### E1. Positive side

`s even`
→ `N=3s` even
→ Section D.

`s=3,5`
→ explicit finite signings
→ exact Sylvester positivity of `8I-A^2`.

### E2. Odd obstruction

Hamilton gauge + reorder `i=j+as`
→ width-three cyclic strip of signed triangle states.

Exact nine-column finite lemma at excess `2/139`
→ complete integer certificate and local alternation rule.

Base cases:
- `s=7`: exact exhaustive certificate, stronger excess `18/131`;
- `s=9`: exact cyclic prefix certificate at `2/139`.

Odd `s>=11`:
local rule on all windows
→ global alternation
→ seam would force `S B_0 S^T=-B_0`
→ contradiction because `tr(B_0^3)=+-6`.

Therefore

`m(3s,s)^2>=8+2/139` for odd `s>=7`.

Combine E1/E2:

`m(3s,s)<sqrt8 iff s is even or s in {3,5}`.

## F. Computational trust boundary

Exact finite computations are used for:

- small characteristic-polynomial checks in the strict sub-six theorem;
- `s=3,5` Sylvester certificates;
- nine-column and `s=7,9` obstruction certificates.

Small sub-six computations use exact symbolic algebra. The `N=3s` Rayleigh programs may use floating eigensolvers only to propose integer witnesses; branch acceptance is always an exact integer inequality. Floating error can therefore cause a failed search but not a false proof.

## G. Remaining frontier

Current resonance picture:

```text
all odd orders N>=7:   global floor m>=sqrt(6).
k=3:                   complete sqrt(8) transition; odd s>=7 above 8+2/139.
k=4:                   exact global formula for every s.
all even orders:       explicit finite construction below sqrt(8).
odd k>=5, odd s:       sqrt(6) floor known; general sqrt(8) classification open.
```

The highest-value unresolved structural problem is now the equality boundary `m(N,s)^2=6` and, beyond it, the `sqrt(8)` behavior for odd `k>=5`.