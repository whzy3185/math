# Maximal independent sets of a Mycielskian and exact Hall certificates

Let G be a finite simple graph with n>=1 vertices. Write μ(G) for its Mycielskian, with original vertices V, clones V', and apex z. Let I(G) be the family of all independent sets, including the empty set. Set i(G)=|I(G)| and let m(G) be the number of maximal independent sets.

This note proves the identities used by the finite certificate workflow. No publication-novelty claim is made for the identities or the underlying Hall-profile formulation.

## Theorem 1: neighborhood-union compression

Define

`D(G)={N_G(I): I in I(G)}` and `d(G)=|D(G)|`.

Then

`m(μ(G))=m(G)+d(G)`.

More precisely, maximal independent sets containing z correspond bijectively to maximal independent sets I of G, through `{z} union I`. Maximal independent sets avoiding z correspond bijectively to neighborhood unions N in D(G), through

`K_N=J_N union (V minus N)'`,

where `J_N={v in V: N_G(v) subseteq N}`.

### Proof

Choose independent I with N=N_G(I). We have I subseteq J_N. Also J_N is disjoint from N: if v belonged to both, v would have a neighbor i in I, and `N(v) subseteq N` would force i into N, contradicting the independence of I. Since every vertex in J_N has all neighbors in N, J_N is independent, and `N(J_N)=N(I)=N`.

It follows that K_N is independent. Every excluded original vertex has a neighbor among the selected clones, by the definition of J_N. Every excluded clone has an original neighbor in I subseteq J_N. There is at least one selected clone: V minus N contains I if I is nonempty, and is all of V otherwise. Thus the apex also has a selected neighbor, so K_N is maximal.

Conversely, let K be maximal independent and avoid z. If I is its original part, all available clones must be selected, so its clone part is `(V minus N(I))'`. Maximality then forces its original part to be J_(N(I)). Hence K=K_N. The clone part determines N uniquely, proving bijectivity.

If z belongs to K, no clone belongs to K; the original part must be a maximal independent set of G. This gives the other bijection and the counting identity.

### Closure interpretation

On independent sets, `cl(I)=J_(N(I))` is an extensive, idempotent operation, and `N(cl(I))=N(I)`. Thus the non-apex maximal independent sets can equivalently be indexed by its closed independent sets. Independent sets with the same open-neighborhood union lead to exactly the same output.

## Corollary 2: generation complexity

There are at most `i(G)+m(G)<=2i(G)` maximal independent sets of μ(G).

Enumerate the independent sets of G, collect their distinct neighborhood unions, and recognize maximal independent sets by `I union N(I)=V`. Construct one K_N for each distinct union and one apex set for each maximal independent set. With adjacency represented by Boolean arrays, this requires `O(n^2 i(G))` elementary Boolean operations and `O(n^2+n i(G))` bits of working/output storage. Bitsets improve these bounds in practice.

This is a bound in the number of independent sets of the base graph, not in the number of all subsets of the doubled graph. It is not a polynomial-time claim in n, nor a polynomial-time claim for solving the resulting integer optimization problem.

For the 23-vertex M5, the exact counts are

`i(M5)=7407`, `d(M5)=778`, `m(M5)=79`,

so `m(M6)=778+79=857`.

## Proposition 3: induced-subset recurrence

For A,B subseteq V and epsilon in {0,1}, write H for the induced graph on originals A, clones B', and the apex when epsilon=1. Then

`alpha(H)=max(epsilon+alpha(G[A]), max_(I independent, I subseteq A) (|I|+|B minus N(I)|))`.

An independent set avoiding the apex selects original part I and can take every available clone. An independent set using the apex selects no clone and can take a maximum independent set of G[A]. For epsilon=0, the first expression is redundant but harmless.

## Proposition 4: independence-polynomial decomposition

Let `Z_G(t)=sum_(I in I(G)) t^|I|`. Then

`Z_(μ(G))(t)=t Z_G(t)+sum_(I in I(G)) t^|I| (1+t)^(n-|N(I)|)`.

The two terms count independent sets using or avoiding the apex. In particular,

`i(μ(G))=i(G)+sum_(I in I(G)) 2^(n-|N(I)|)`.

Applying this to M5 gives `i(M6)=39,473,983`. This quantifies a practical limit of escalating the same parameterized enumeration to the next level; no computation of all those M6 independent sets was needed here.

## The exact-certificate workflow

For H=μ(G), generate its maximal independent sets `K_1,...,K_q` by Theorem 1. For binary vertex-selection variables x, the condition `alpha(H[S])<=k` is equivalent to

`sum_(v in K_j) x_v<=k` for every j.

The forward implication holds because each intersection is independent. The reverse holds because every independent set extends to a maximal one.

To prove an upper bound on |S|, use these inequalities and `0<=x_v<=1`. Numerical LP or MILP software may suggest candidates, branch variables, or rational dual weights. The proof output is separate:

1. A binary split tree specifies fixed-zero and fixed-one assignments
2. Each leaf supplies nonnegative rational combinations of the residual independent-set inequalities and upper bounds `x_v<=1`
3. The combination covers every free objective coefficient by at least one
4. Its exact objective bound is strictly below the excluded integer cardinality

An exact checker verifies these statements using integers and rational numbers. It does not trust solver status or numerical tolerance. Verification is polynomial in the explicit certificate's bit length; there is no promised polynomial bound on the certificate size or its discovery time.

The M6 example in the sibling pilot package illustrates this workflow with 47 binary variables, 857 independent-set rows, and a 273-node proof of Hall ratio 10/3. The strengthening package adds 22 nodes to isolate all equality cases.

## Prior-work scope

The Hall-profile formulation predates this work: Barnett's 2016 dissertation uses the function w(a,G). Whole-graph independence formulas for Mycielskians have also been studied previously. This note presents complete proofs for a reproducible workflow, without claiming these general identities are new.

Sources:

- Barnett, dissertation, Definition 2.1.1 and Chapter 4: https://etd.auburn.edu/bitstream/handle/10415/5316/Final%20Dissertation%20-%20Johnathan%20Barnett.pdf?isAllowed=y&sequence=2
- *The exponential growth of the packing chromatic number of iterated Mycielskians*: https://www.sciencedirect.com/science/article/abs/pii/S0166218X23003098
