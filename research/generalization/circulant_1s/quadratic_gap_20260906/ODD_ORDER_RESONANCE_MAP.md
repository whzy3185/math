# Odd finite orders: seam-safe resonance map

Date: 2026-09-06.

This note records **exploratory** finite-order evidence after the exact global
obstruction at `C_21(1,7)`.  Except where an exact proof note is cited, the
statements here are numerical and should not be promoted to theorems.

All computations use the quasiperiodic Hamilton model

\[
 A=T+T^{-1}+M_\tau T^s+T^{-s}M_\tau,
 \qquad T^N=\alpha I,
\]

so every step-one or chord crossing of the Hamilton seam receives the correct
holonomy factor.  This corrects an earlier temporary scratch implementation
that wrapped chord edges without the seam factor; no result from that scratch
calculation is used here.

## 1. Exact anchor point

`C21_S7_GLOBAL_OBSTRUCTION.md` proves exhaustively that

\[
 m(21,7)^2\ge\frac{1066}{131}>8,
\]

where here the notation means the minimum squared spectral radius over all
edge signings.  Thus `(21,7)` is a genuine finite obstruction, not merely a
failure of the alternating or one-defect family.

## 2. One-defect family

For odd `N`, the finite alternating word

\[
 \tau_i=\epsilon(-1)^i
\]

has one cyclic positive `Q` defect.  It is the simplest repair of the
period-two odd-jump Bloch signing.

Seam-safe scans show that this family is often below `8`, but develops strong
resonances when the chord subgraph has a short odd cycle.  If

\[
 L=\frac{N}{\gcd(N,s)},
\]

then the `s`-chord subgraph consists of `gcd(N,s)` cycles of length `L`.
The largest observed one-defect failures cluster at small odd `L`.

In particular, along `N=Ls` with odd `s`, the one-defect value eventually
crosses above `8` for each tested short odd `L=3,5,7,9,11`.  The `L=3`
resonance is strongest: its one-defect squared radius rapidly approaches a
limit near `8.384` as `s` grows.

These limiting values are numerical observations only.

## 3. Multi-defect repair is sometimes possible

A one-defect failure does **not** by itself imply a global obstruction.
Exhaustive small-`k` scans over cyclic `Q` words show, for example,

- `(N,s)=(19,9)`: one defect is above `8`, but a five-defect word reaches
  approximately `7.9423`;
- `(N,s)=(23,11)`: one defect is above `8`, but a five-defect word reaches
  approximately `7.9822`.

By contrast,

- `(21,7)`: the exact all-signing theorem proves no repair exists at all;
- `(27,9)`: one-, three-, and five-defect scans remain above `8`, but no
  exhaustive all-signing theorem has yet been proved for this pair.

Thus defect count and chord-cycle resonance interact nontrivially.

## 4. Structural interpretation of `N=3s`

When `N=3s`, reordering vertices by

\[
 i=j+a s,
 \qquad 0\le j<s,\quad a\in\{0,1,2\},
\]

organizes the graph as a width-three cyclic strip:

- each column `j` is a signed triangle formed by the `s`-chords;
- neighboring columns are joined by the step-one matching;
- the final matching carries the helical/holonomy wrap.

For the one-defect alternating word, the signed triangle blocks alternate as

\[
 B,-B,B,-B,\ldots
\]

through the bulk.  Since `s` is odd, the cyclic closure forces a defect in
that alternation.  The open perfectly alternating strip has squared edge
approaching `8` from below, while the cyclic defect numerically creates a
localized state above `8` for `s>=7` in the tested `L=3` family.

This gives a plausible analytic mechanism for a systematic `N=3s`
obstruction theorem, but it is not yet a proof for arbitrary signings.

## 5. Research targets

The next finite-order tasks are:

1. prove or disprove a structural theorem
   `m(3s,s)^2>8` for all sufficiently large odd `s`;
2. derive the exact width-three block/transfer determinant for the
   one-defect family and identify its large-`s` localized-state limit;
3. determine whether `(27,9)` is a second all-signing obstruction by an
   exact reduced enumeration or a structural certificate;
4. classify which short odd chord-cycle lengths `L` can be repaired by a
   bounded number of `Q` defects;
5. separate arithmetic obstructions from mere incompatibility of a chosen
   periodic word.

The companion explorer is `explore_odd_order_resonances.py`.
