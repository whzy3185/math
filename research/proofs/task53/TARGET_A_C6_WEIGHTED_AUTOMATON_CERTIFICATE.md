# c6 Weighted-automaton Pilot

The inherited grammar has 105 states and 164 edges and contains the
period-eight reference cycle. With the stated forms
`F_k=M_(k+1)-c6 M_k`, every squared Bloch value on that cycle is at most
`eta<c6`. Hence every `F_k` has strictly negative cycle sum.

For any nonzero coefficients `a_k>=0`, the combined cycle sum remains
strictly negative. A potential coboundary telescopes to zero on every closed
cycle, so it cannot make every edge weight nonnegative. The all-zero vector
is vacuous. Thus the requested LP sign convention is exactly obstructed
before numerical optimization.

No `M7` or `M8` was generated.

Status: `CURRENT_LOCAL_GRAMMAR_INSUFFICIENT`.
