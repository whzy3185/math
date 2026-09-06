# F(0,17,1,0): Case 2, r=6 independent audit and proof

Date: 2026-09-06

Branch: `research/q1-discrete-full-push-20260906`

## Evidence status

- **Published/Established:** the Case 2 path-type decomposition (equation (13)) and the general deletion framework are from Anstee–Edens–Sahami–Seok–Sali, *Exact Bounds for Forbidden Configurations and the Extremal Matrices*, arXiv:2601.04084 (2026).
- **Proved (this file):** for the proposed `p=17`, `c=21/2` extension, the Case 2 subcase with shortest undirected path length parameter `r=6` always admits a deletion of nonnegative cost.
- **Verified:** the coefficient identity at the end is independently checked by `research/scripts/case2_p17_r6_certificate.py`.
- No computational optimization is used as a proof. A small LP/MILP search was used only to discover a short certificate; the proof below is explicit.

## 1. Audit of the published Case 2 count

Use the notation of equation (13) of arXiv:2601.04084. On a shortest undirected path

\[
R=(v_1,v_2,\dots,v_r),
\]

let the multiplicities of the nonconstant column types be

\[
a_1^1,\ a_2^0,a_2^1,\ldots,a_{r-1}^0,a_{r-1}^1,\ a_r^0.
\]

For the pair `(v_1,v_{r-1})`, a direct expansion of the types in (13) shows that the number of `[1;0]` columns is

\[
\sum_{s,d}a_s^d-(a_1^1+a_{r-2}^1+a_r^0),
\]

not

\[
\sum_{s,d}a_s^d-(a_1^1+a_r^0).
\]

Thus the first displayed pair-count in the published Case 2 discussion omits the term `a_{r-2}^1`.

However, for `(v_2,v_r)` the exact number of `[1;0]` columns is

\[
\sum_{s,d}a_s^d-(a_2^0+a_2^1+a_{r-1}^1).
\]

By minimality of the chosen Case 2 pair this is at most `2p-2`; the adjacent-edge constraints give

\[
a_2^0+a_2^1\le p-1,\qquad a_{r-1}^1\le p-1.
\]

Hence the published bound

\[
\sum_{s,d}a_s^d\le 4p-4
\]

still follows from the second count alone. Therefore the local typo does **not** invalidate the published `p\le9` theorem.

## 2. Specialize to p=17 and r=6

Set

\[
p=17,\qquad c=\frac{21}{2}.
\]

For `r=6`, abbreviate

\[
\begin{aligned}
x_1&=a_1^1,&x_2&=a_2^0,&x_3&=a_2^1,&x_4&=a_3^0,&x_5&=a_3^1,\\
x_6&=a_4^0,&x_7&=a_4^1,&x_8&=a_5^0,&x_9&=a_5^1,&x_{10}&=a_6^0.
\end{aligned}
\]

The ten nonconstant path types are therefore

```text
x1 : 0 1 0 0 0 0
x2 : 1 0 0 0 0 0
x3 : 1 0 1 0 0 0
x4 : 1 1 0 0 0 0
x5 : 1 1 0 1 0 0
x6 : 1 1 1 0 0 0
x7 : 1 1 1 0 1 0
x8 : 1 1 1 1 0 0
x9 : 1 1 1 1 0 1
x10: 1 1 1 1 1 0
```

Because every adjacent pair on the path is an undirected edge, each directional difference count is at most `p-1=16`. We shall use

\[
\tag{U1}x_2+x_3\le16,
\]

coming from `(v_1,v_2)`, and

\[
\tag{U2}x_3+x_6+x_7\le16,
\]

coming from `(v_3,v_4)`.

The Case 2 pair `(v_1,v_6)` was chosen so that its undirected path is shortest among pairs carrying at least `2p-1=33` columns of type `[1;0]`. Therefore every pair connected by a strictly shorter subpath has at most `2p-2=32` such columns. In particular,

\[
\tag{U3}x_2+x_3+x_4+x_5+x_6+x_8+x_9\le32
\]

for `(v_1,v_5)`, and

\[
\tag{U4}x_1+x_4+x_5+x_6+x_7+x_8+x_{10}\le32
\]

for `(v_2,v_6)`.

## 3. Three safe deletions

The following deletion counts are conservative: they delete entire path-type classes whenever necessary, so they remain valid even if columns with the same `R`-trace have different entries on rows outside `R`.

### Delete v6

After deleting `v6`, the types `x8,x9` have the same remaining trace, while `x10` becomes constant on the remaining path rows. Thus it is sufficient to delete

\[
D_6=x_{10}+\min(x_8,x_9)
\]

columns.

Since one deleted row has budget `c=10.5`, a nonnegative-cost deletion exists whenever `D_6\le10`. If this deletion fails, then

\[
\tag{L1}x_9+x_{10}\ge11,
\]

and

\[
\tag{L2}x_8+x_{10}\ge11.
\]

### Delete {v1,v2}

After deleting `v1,v2`, the types `x1,x2,x4` become constant zero on the remaining path rows, and `x3,x6` have the same remaining trace. It is sufficient to delete

\[
D_{12}=x_1+x_2+x_4+\min(x_3,x_6).
\]

Two deleted rows have budget `2c=21`. If this deletion fails, `D_{12}\ge22`, hence in particular

\[
\tag{L3}x_1+x_2+x_4+x_6\ge22.
\]

### Delete {v3,v4}

After deleting `v3,v4`, the collision classes are

\[
\{x_2,x_3\},\qquad \{x_4,x_5,x_6,x_8\},\qquad \{x_7,x_{10}\}.
\]

Thus it is sufficient to delete all but one type from each collision class. If this two-row deletion fails, its minimum necessary conservative deletion count is at least `22`. Therefore every choice of one retained type in each collision class leaves at least `22` deleted columns. We only need the following three consequences:

\[
\tag{L4}x_3+x_5+x_6+x_7+x_8\ge22,
\]

\[
\tag{L5}x_3+x_4+x_5+x_7+x_8\ge22,
\]

\[
\tag{L6}x_3+x_4+x_5+x_6+x_7\ge22.
\]

Each is obtained by retaining one member of each collision class and deleting all the others.

## 4. Integer certificate: 208 < 209

Assume for contradiction that **all three** deletions above have negative cost. Then (L1)–(L6) all hold.

Take the upper bounds with multipliers

\[
1\cdot(U1)+2\cdot(U2)+2\cdot(U3)+3\cdot(U4).
\]

Their right-hand side is

\[
16+2\cdot16+2\cdot32+3\cdot32=208.
\]

Take the lower bounds with multipliers

\[
2\cdot(L1)+1\cdot(L2)+3\cdot(L3)+3\cdot(L4)+1\cdot(L5)+1\cdot(L6).
\]

Their right-hand side is

\[
2\cdot11+11+3\cdot22+3\cdot22+22+22=209.
\]

The two weighted left-hand sides are **identical**. In the variable order `(x1,...,x10)` both equal

\[
3x_1+3x_2+5x_3+5x_4+5x_5+7x_6+5x_7+5x_8+2x_9+3x_{10}.
\]

Hence the same quantity would have to be simultaneously at most `208` and at least `209`, a contradiction.

Therefore at least one of the three deletions has nonnegative cost.

## 5. Conclusion

For `p=17`, `c=21/2`, in Case 2 with `r=6`, there is always a deletion of nonnegative cost. This closes the `r=6` subcase for the inductive upper-bound strategy.

This proof does **not** use the erroneous `(v_1,v_{r-1})` pair-count and is independent of the old discarded shortcut.

The remaining Case 2 bottleneck is therefore `r=4,5`.
