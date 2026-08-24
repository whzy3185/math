# Referee Checklist

## Statement and exhaustion

- [x] The domain is exactly the even integers $n\ge8$.
- [x] The failure set is $\{32,40\}\cup\{n\ge48:n\text{ even}\}$.
- [x] Truth classification is distinguished from minimiser classification.
- [x] The proof partitions the domain into $8$ through $30$, $32$, the six
  no-counterexample orders, $40$, $48$ through $238$, and $n\ge240$.
- [x] The six pieces are disjoint and exhaustive.
- [x] The finite bridge has exactly 96 even orders.

## Exactness

- [x] One explicit signing is printed for every even $n\ge8$.
- [x] Its alternating triangle flux and negative holonomy are checked directly.
- [x] A complete $2\times2$ antiperiodic Fourier calculation proves
  $\rho(A_{\sigma_n^-})=\rho_-(n)$ without machine input.
- [x] On the validity set, candidate attainment gives $m_n\le\rho_-(n)$ and
  exhaustion gives $m_n\ge\rho_-(n)$, so equality is explicit.
- [x] On the failure set, a separate witness gives the strict inequality;
  existence of the threshold candidate does not weaken that conclusion.
- [x] No floating-point eigenvalue comparison is an accepting endpoint.
- [x] Lower certificates use exact Rayleigh inequalities or threshold equality.
- [x] Upper certificates use positivity of $pI-qA^2$ and exact comparison.
- [x] Algebraic thresholds use exact polynomials and isolating intervals.
- [x] Infinite-tail propagation uses an explicit monotonicity identity.

## Small finite-state interval

- [x] Local exclusion is proved independently of enumeration.
- [x] Graph soundness, completeness, cyclic closure, and parity closure are proved.
- [x] Both holonomies are represented.
- [x] The authoritative terminal total is 64; the historical 84 typo is corrected.
- [x] The unresolved total is independently reconstructed as zero.

## Reproducibility and scope

- [x] Every essential finite artifact has an independent checker.
- [x] The analytic candidate-attainment lemma is not represented as a producer
  or independent-verification result and has no machine dependency.
- [x] Paths and hashes are isolated in the provenance appendix.
- [x] The mathematical dependency graph has no task-number node.
- [x] The theorem does not claim that all even $n\ge32$ fail.
- [x] The theorem does not call 48 the first failure.
- [x] Exact-$2r$ and $N_{\mathrm{exp}}=3120$ are not dependencies here.
- [x] No unrestricted limit, universal multi-gap, arbitrary-period, or full
  minimiser theorem is inferred.

Disposition: READY FOR MATHEMATICAL COPY-EDIT, subject to successful execution
of the listed independent checkers at the bound reference checkpoint.
