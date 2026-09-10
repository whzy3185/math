# Global width-five obstruction at `s=15,17`

This note closes the two previously open vertical base cases `(75,15)` and `(85,17)`.  The proof is over **all** signings.  It combines the intrinsic width-five flux encoding with the exact local rules already proved on this branch, leaving only six finite cyclic gap patterns; those residual cyclic populations are then exhausted with exact integer Rayleigh certificates.

## Theorem 1

\[
\boxed{m(75,15)\ge\sqrt8,
\qquad
m(85,17)\ge\sqrt8.}
\tag{1}
\]

Consequently the step-fifteen and step-seventeen vertical threshold classifications are complete:

\[
\boxed{
m(15k,15)<\sqrt8
\iff k=4\text{ or }k\ge6,
}
\tag{2}
\]

and

\[
\boxed{
m(17k,17)<\sqrt8
\iff k=4\text{ or }k\ge6.
}
\tag{3}
\]

Here `k>=3` is admissible.  The points `k=3` are above the threshold by the proved horizontal `N=3s` obstruction; every even `k` is below by the all-even-order theorem; and all odd `k>=7` were already constructed explicitly in the vertical step-15/17 notes.  Thus (1) is the only new global input needed for (2)--(3).

---

## 1. Intrinsic transition fluxes

Reorder `C_(5s)(1,s)` into `s` chord-pentagon columns

\[
V_j=\{j,j+s,j+2s,j+3s,j+4s\},
\qquad j\in\mathbb Z_s.
\]

For every boundary between two consecutive columns there are five elementary squares.  Record their fluxes in a five-bit mask `delta_j`, with a bit equal to one when the square flux is negative.  This definition is switching invariant.  A boundary is a **complement transition** exactly when

\[
delta_j=31,
\]

that is, all five square fluxes are negative.  Otherwise it is a **defect transition**.

On any proper open interval of columns one may switch all inter-column matching edges to `+1`.  Then the pentagon edge-state masks `eta_j` satisfy

\[
delta_j=\eta_j\oplus\eta_{j+1},
\]

so the exact open-strip lemmas proved previously apply directly to these intrinsic transition masks.

Let `r` be the number of defect transitions around the cyclic width-five strip.

### No-defect case

Let `p_j` be the signed flux of the chord pentagon in column `j`.  The product of the five square fluxes across the boundary `j` is

\[
p_jp_{j+1};
\tag{4}
\]

the five matching signs occur twice and cancel, including at the helical seam.  If every transition were complement, (4) would give

\[
p_{j+1}=-p_j
\]

at every boundary.  For odd `s` this is impossible after one circuit.  Hence

\[
r\ne0.
\tag{5}
\]

---

## 2. A shorter single-defect exclusion

We need one small strengthening of the previous fifteen-column single-defect lemma.

### Lemma 2.1 (fourteen-column single-defect rule)

A fourteen-column open width-five strip with exactly one defect transition, with five complement transitions on one side and seven on the other, has

\[
\rho(M)^2\ge8.
\tag{6}
\]

#### Exact certificate

Normalize the state immediately before the defect.  The 31 non-complement masks reduce under `D_5` to the seven representatives

\[
0,1,3,5,7,11,15.
\]

For each representative an integer vector `w` gives the following exact Rayleigh excess for `Q=M^2-8I`:

\[
\begin{array}{c|c|c}
d&w^Tw&w^TQw\\ \hline
0&270&660\\
1&258&312\\
3&252&310\\
5&262&120\\
7&226&98\\
11&9295&11\\
15&270&8.
\end{array}
\tag{7}
\]

Thus every class satisfies (6). `square`

If `s=15` or `17` and `r=1`, the unique defect has enough complement transitions around it to contain such a proper fourteen-column interval.  Therefore

\[
r\ne1.
\tag{8}
\]

---

## 3. Gap parity and the local exclusions

Assume now `r>=2`.  List the defect transitions cyclically and let

\[
g_1,\ldots,g_r\ge0
\]

be the numbers of complement transitions between consecutive defects.  Then

\[
s=r+\sum_{i=1}^r g_i.
\tag{9}
\]

The thirteen-column complement rule proves that two defects cannot be adjacent in a sufficiently embedded proper interval.  For `s=15,17` every adjacent pair has such an interval, so

\[
g_i\ge1.
\tag{10}
\]

If every `g_i` were odd, then (9) would imply

\[
s\equiv r+r\equiv0\pmod2,
\]

contrary to odd `s`.  Hence at least one `g_i` is even.

The two exact even-gap lemmas already proved on this branch give:

- `g=2,4` are impossible with two arbitrary context transitions on one side and one on the other;
- `g=6,8,10,12,14` are impossible with one arbitrary context transition on each side.

When the corresponding open interval is a proper subset of the cycle, these rules exclude the even gap immediately.  For `s=15` this eliminates every even gap at most eight; for `s=17` it eliminates every even gap at most ten.

The only cyclic patterns not covered because the long even gap consumes almost the whole cycle are therefore, up to cyclic reversal,

\[
\begin{array}{c|c}
s=15&(12,1),\ (10,3),\ (10,1,1),\\[1mm]
s=17&(14,1),\ (12,3),\ (12,1,1).
\end{array}
\tag{11}
\]

Here the tuples list the complement-gap lengths and have respectively two or three defects.  This elementary list is exhaustive because the positive gaps sum to `s-r`.

---

## 4. Exact cyclic audit of the six residual patterns

The remaining enumeration retains the helical seam exactly; it is not an open-strip approximation.

Choose one complement boundary from the long gap as the cut.  Switch all other inter-column matching edges to `+1`.  The seam matching is a signed 5-cycle permutation.  A common row switching puts its five edge signs into the canonical form

\[
q=(1,1,1,1,\alpha),
\qquad \alpha\in\{\pm1\},
\tag{12}
\]

without changing any transition mask.  The initial chord-pentagon state `eta_0` ranges over all 32 masks.  Once `eta_0` and all internal transition masks are fixed, every column state is determined.  The five seam square fluxes are then computed explicitly and required to equal the complement mask `31`.  Thus the enumeration covers both Hamilton-holonomy sectors and every switching class compatible with the residual gap pattern.

### Two-defect residuals

For each of

\[
(15;12,1),\quad(15;10,3),\quad
(17;14,1),\quad(17;12,3),
\]

we enumerate

\[
\alpha\in\{\pm1\},\qquad
\eta_0\in\{0,\ldots,31\},\qquad
(d,e)\in\{0,\ldots,30\}^2,
\]

and retain only those satisfying the exact seam-complement equations.  In **each** of the four cases exactly

\[
\boxed{1920}
\tag{13}
\]

full cyclic candidates remain.  Every one has an integer vector `w` such that

\[
w^T(A^2-8I)w\ge0.
\tag{14}
\]

Hence no two-defect residual signing is strictly sub-threshold.

### Three-defect residuals

For `(s;G,1,1)`, with `(s,G)=(15,10)` or `(17,12)`, first use the two proper `(s-1)`-column principal strips obtained by deleting one endpoint column.  Exact integer Rayleigh pruning leaves only

\[
10\quad(s=15),
\qquad
2\quad(s=17)
\tag{15}
\]

canonical `D_5` transition triples.  Expanding their dihedral orbits gives respectively

\[
50\quad\text{and}\quad10
\tag{16}
\]

labelled transition triples.  Imposing the two seam holonomies, all 32 initial pentagon states, and the exact seam-complement condition leaves only

\[
\boxed{100\quad(s=15),
\qquad40\quad(s=17)}
\tag{17}
\]

full cyclic candidates.  Every candidate again admits an exact integer witness (14).

The complete reconstruction, including (7), (13), (15)--(17), and every integer branch certificate, is `verify_n5s_15_17_global_obstruction.py`.  Floating eigenvectors are used only to propose integer directions; a candidate is rejected only after the integer inequality (14) is verified exactly.

Thus all cases `r=0`, `r=1`, and `r>=2` are impossible under the assumption `rho(A)^2<8`.  This proves (1), and hence (2)--(3). `square`

---

## Corollary 1.1 (first transition on the horizontal `N=5s` line)

The odd points on the horizontal resonance `N=5s` are now known through step seventeen:

\[
\boxed{
m(5s,s)<\sqrt8\quad\text{for }s=3,5,7,9,11,13,
}
\]

whereas

\[
\boxed{
m(75,15)\ge\sqrt8,
\qquad m(85,17)\ge\sqrt8.
}
\]

This is the first rigorous evidence of a second horizontal threshold beyond the completely classified triangle resonance `N=3s`.  No claim is yet made for all odd `s>=15`; extending the finite gap-parity mechanism uniformly is the next problem.