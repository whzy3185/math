# F(0,17,1,0): transitivity, clique components, and Case 1

Date: 2026-09-06

Branch: `research/q1-discrete-full-push-20260906`

## Evidence status

- **Published/Established:** Deletion Lemma 3.2, Upper Bound Lemma 3.3, and the transitivity framework are from Anstee–Edens–Sahami–Seok–Sali, *Exact Bounds for Forbidden Configurations and the Extremal Matrices*, arXiv:2601.04084 (2026).
- **Proved (this file):** their algebraic lemmas apply with the proposed `p=17`, `c=21/2`; every clique component has deletion cost at least `0`, with zero cost only for a 6-row copy of `K_6 \setminus \mathbf 1_6`; every non-clique component in Case 1 has strictly positive deletion cost.
- No numerical optimization is used in these arguments.

Throughout set

\[
p=17,\qquad c=\frac{21}{2},\qquad 2p-2=32.
\]

We seek the inductive upper bound

\[
\|A\|\le cm+1.
\]

The cost of deleting `k` rows and `d` columns is `ck-d`.

## 1. Pair graph and transitivity

For two rows `i,j` of an `F(0,17,1,0)`-avoiding simple matrix, write

\[
n_{10}(i,j)=\#\{\text{columns with }(i,j)=(1,0)\},
\]

\[
n_{01}(i,j)=\#\{\text{columns with }(i,j)=(0,1)\}.
\]

Avoidance says that if both directional types occur, then

\[
n_{10}(i,j),n_{01}(i,j)\le16.
\]

Thus every row pair can be represented either by an undirected edge (both directional counts at most 16) or, if one directional type is absent, by a directed edge in the corresponding containment direction.

The proof of the published Transitivity Lemma 3.4 only needs the numerical hypothesis used to pay for the deletion in its three-row obstruction. With `c=21/2`,

\[
2c=21\ge p=17,
\]

so the same proof applies verbatim: unless a deletion of positive cost is already available, directed edges are transitive and the connected components of the undirected-edge graph admit a total transitive ordering. Consequently, a column can be nonconstant on at most one undirected component.

This reduces the global induction to bounding the matrix `B_C` associated to each undirected component `C`: all columns nonconstant on `C`, together with the all-zero column on `C` if it occurs. Such a matrix has no all-one column.

## 2. Upper Bound Lemma specialized to p=17

Suppose a simple `k`-rowed matrix `B` has neither constant column and every pair of rows differs in at most `t=32` columns in total. Published Lemma 3.3 gives

\[
\|B\|\le
\left\lfloor
2k+\frac{(32-4)k(k-1)}{4(k-2)}
\right\rfloor
=
\left\lfloor
2k+\frac{7k(k-1)}{k-2}
\right\rfloor.
\tag{UB}
\]

For a component matrix `B_C`, at most one additional all-zero column may be present.

## 3. Clique components

If `C` is a clique of undirected edges, then every pair of rows has both directional counts at most `16`, so the total number of differing columns on a pair is at most `32`. Hence (UB) applies to the nonconstant columns.

### 3.1. k <= 6

Because `B_C` is simple and has no all-one column,

\[
\|B_C\|\le 2^k-1.
\]

For `k<=5`,

\[
2^k-1<\frac{21}{2}k.
\]

For `k=6`,

\[
\|B_C\|\le63=\frac{21}{2}\cdot6.
\]

Equality forces `B_C` to contain every six-bit column except `111111`; therefore

\[
B_C=K_6\setminus\mathbf1_6
\]

(up to row and column permutation). In particular every row pair has exactly 16 columns of each directional type, so this is indeed a clique component.

### 3.2. k = 7

By (UB), the number of nonconstant columns is at most

\[
\left\lfloor14+\frac{7\cdot7\cdot6}{5}\right\rfloor
=\lfloor72.8\rfloor=72.
\]

Adding the possible zero column gives

\[
\|B_C\|\le73<73.5=\frac{21}{2}\cdot7.
\]

### 3.3. k >= 8

Ignoring the floor in (UB), the component size is at most

\[
1+2k+\frac{7k(k-1)}{k-2}
=1+9k+\frac{7k}{k-2}.
\]

For `k>=8`,

\[
1+9k+\frac{7k}{k-2}<\frac{21}{2}k.
\]

Indeed this is equivalent to

\[
2(k-2)+14k<3k(k-2),
\]

i.e.

\[
3k^2-22k+4>0,
\]

which holds at `k=8` and is increasing thereafter.

Therefore every clique component has nonnegative deletion cost, and the **only zero-cost clique component** is

\[
\boxed{k=6,\quad B_C=K_6\setminus\mathbf1_6.}
\]

## 4. Case 1: non-clique component with no large separated pair

Consider a non-clique undirected component `C` in Case 1 of the published argument: there is no row pair in `C` carrying at least `2p-1=33` columns of one directional type while the reverse type is present in the sense that starts Case 2.

For every pair of rows in `C` we then have at most `32` differing nonconstant columns in total:

- if the pair is undirected, each direction has at most 16, hence total at most 32;
- if the pair is directed, Case 1 bounds the only possible directional difference by at most 32.

Therefore (UB) applies to the nonconstant columns of `B_C`, even though `C` is not a clique.

For `k<=5`, the simple-capacity bound gives

\[
\|B_C\|\le2^k-1<ck.
\]

For `k=6`, simple capacity gives `|B_C|<=63`. Equality would force every column except all-one, which makes every row pair undirected; that would make `C` a clique, contrary to the Case 1 hypothesis. Hence a non-clique six-row component satisfies

\[
\|B_C\|\le62<63=6c.
\]

For `k=7`, (UB) plus the possible zero column gives

\[
\|B_C\|\le73<73.5=7c.
\]

For every `k>=8`, the calculation in Section 3.3 gives

\[
\|B_C\|<ck.
\]

Thus every non-clique component in Case 1 has **strictly positive deletion cost**.

## 5. Reduction of the p=17 theorem

After transitivity, every undirected component falls into exactly one of the following classes:

1. clique component: nonnegative cost, with zero cost only for the 6-row block `K_6\setminus\mathbf1_6`;
2. non-clique Case 1 component: strictly positive cost;
3. non-clique Case 2 component: contains a shortest undirected path `R=(v_1,...,v_r)` associated with a row pair carrying at least 33 columns of one directional type.

The independent file `F017_CASE2_R6_INDEPENDENT_AUDIT.md` closes the Case 2 subcase `r=6` by an explicit integer deletion certificate.

Hence the only currently unresolved local cases needed for the full `p=17` upper bound are

\[
\boxed{r=4\quad\text{and}\quad r=5.}
\]

Once these two cases are closed by nonnegative-cost deletions (or by a component bound of the same strength), induction yields

\[
\operatorname{forb}(m,F(0,17,1,0))\le \left\lfloor\frac{21m}{2}\right\rfloor+1.
\]

For `6|m`, the standard ordered product of `m/6` copies of `K_6\setminus\mathbf1_6` contributes `63(m/6)` nonterminal columns plus the final all-one column, giving

\[
\operatorname{forb}(m,F(0,17,1,0))\ge \frac{21m}{2}+1.
\]

Thus equality for multiples of six will follow immediately after `r=4,5` are closed.
