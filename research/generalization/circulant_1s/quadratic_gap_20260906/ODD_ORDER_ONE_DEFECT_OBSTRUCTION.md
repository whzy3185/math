# Odd-order obstruction: one alternating defect is not enough

Date: 2026-09-06.

The all-`s` theorem covers every odd jump `s` on every admissible **even**
order `N`, because the alternating chord word has period two.  A natural
first attempt for odd `N` is to use the same list on `0,...,N-1` and accept
the single parity defect at the cyclic seam.  This note records an exact
counterexample to that naive extension.

## 1. One-defect family

Let `N` be odd and define the two anchor words

\[
 \tau_i^{\pm}=\pm(-1)^i,\qquad 0\le i<N,
\]

read cyclically.  Then

\[
 Q_i=\tau_i\tau_{i+1}=-1\quad(0\le i<N-1),
 \qquad Q_{N-1}=+1.
\]

Thus this is the closest cyclic analogue of the even-order alternating word:
exactly one local `Q` defect is forced by odd parity.

For Hamilton holonomy `alpha in {+1,-1}`, let `T_alpha` be the signed cyclic
shift with `T_alpha^N=alpha I`, and set

\[
 A_{N,s,\alpha,\tau}
 =T_\alpha+T_\alpha^{-1}
   +M_\tau T_\alpha^s+T_\alpha^{-s}M_\tau.
\tag{1}
\]

This is the same Hamilton-gauge finite operator used in Task 60.

## 2. Exact counterexample at `(N,s)=(21,7)`

Take `N=21`, `s=7`.  For each of the four pairs
`(alpha,anchor) in {+1,-1}^2`, the corresponding one-defect signing has
squared spectral radius strictly larger than `8`.

It is enough to provide an integer vector `v` with

\[
 v^T(A^2-8I)v>0.
\]

The following four certificates do so.  In every row the displayed
`excess` is exactly `v^T(A^2-8I)v`.

### `alpha=+1`, anchor `+`

```text
v = [-1,0,-1,0,-1,0,-1, 1,0,1,0,1,0,1, 1,0,1,0,1,0,1]
v^T v = 12
excess = 2
```

Hence

\[
 \rho(A)^2\ge\frac{8\cdot12+2}{12}
 =\frac{49}{6}>8.
\]

### `alpha=+1`, anchor `-`

```text
v = [-3,-1,-1,0,1,1,3, 3,1,1,0,-1,0,-1, 1,0,1,0,-1,-1,-3]
v^T v = 48
excess = 2
```

Thus

\[
 \rho(A)^2\ge\frac{8\cdot48+2}{48}
 =\frac{193}{24}>8.
\]

### `alpha=-1`, anchor `+`

```text
v = [1,0,1,0,1,0,1, 1,0,1,0,1,0,1, -1,0,-1,0,-1,0,-1]
v^T v = 12
excess = 2
```

Again `rho(A)^2>=49/6>8`.

### `alpha=-1`, anchor `-`

```text
v = [-3,1,-1,0,1,-1,3, -3,1,-1,0,1,0,1, 1,0,1,0,-1,1,-3]
v^T v = 48
excess = 2
```

Again `rho(A)^2>=193/24>8`.

All arithmetic in these certificates is integral.

## 3. Why this rules out every translated single defect

For fixed holonomy, conjugation by a power of the cyclic shift translates
`tau` and preserves the spectrum.  A cyclic `±1` word with exactly one
positive `Q_i=tau_i tau_(i+1)` is determined, after translating its unique
defect to the seam, by exactly one of the two anchors above.  Therefore the
four certificates rule out the entire one-`Q`-defect near-alternating family
at `(N,s)=(21,7)`, in both holonomy sectors.

## 4. Consequence for the finite-order program

The odd-jump continuous theorem is not the obstacle: its period-two Bloch
edge has a sharp positive gap.  The obstruction is the topology of an odd
cycle, which forces a defect, and a single concentrated defect can create a
finite-ring state above the threshold `8`.

Therefore an odd-`N` extension should try one of the following instead:

1. spread the parity mismatch over several defects rather than one;
2. optimize a defect lattice whose spacing grows with `s`;
3. derive a transfer-matrix/scattering description of the defect states and
   impose a cancellation condition;
4. search for a genuinely odd primitive period rather than perturbing the
   period-two word.

This note is an obstruction to one natural strategy, not a claim that no
sub-eight signing exists for odd `N`.  Small exact/numerical enumerations in
the project in fact show sub-eight signings for several odd orders, so the
correct conclusion is that a more structured finite construction is needed.
