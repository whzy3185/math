# Task 60 General Squared-Operator Formula

Let `H_s=A_{s,tau,alpha}^2`, with indices interpreted on the cover and
`u_{i+N}=alpha u_i`. Direct enumeration of all ordered length-two paths gives

```text
(H_s u)_i = 4u_i
  + u_{i+2}+u_{i-2}
  + tau_i tau_{i+s} u_{i+2s}
  + tau_{i-s} tau_{i-2s} u_{i-2s}
  + (tau_i+tau_{i+1}) u_{i+s+1}
  + (tau_{i-1}+tau_i) u_{i+s-1}
  + (tau_{i-s}+tau_{i-s+1}) u_{i-s+1}
  + (tau_{i-s-1}+tau_{i-s}) u_{i-s-1}.
```

Writing `P_i=tau_i tau_{i+s}=product_{r=0}^{s-1}Q_{i+r}` expresses the two
pure chord coefficients solely through local flux products.

If two displayed displacements coincide modulo `N`, their contributions are
added. Thus the formula remains valid without a hidden genericity assumption.

## Universal destructive cancellation

The two forward mixed coefficients factor as

```text
tau_i+tau_{i+1}       = tau_i(1+Q_i),
tau_{i-1}+tau_i       = tau_{i-1}(1+Q_{i-1}),
```

and the backward coefficients have the translated factorizations. Therefore

```text
Q_i=-1
```

cancels the associated `s+1` mixed path contribution for every `s`, and the
translated condition cancels the `s-1` contribution. This cancellation is
universal. It does not by itself say that the corresponding finite matrix
entry vanishes: a `2` or `2s` channel can land at the same residue modulo
`N` and survive there.

For a residue `r in {0,...,N-1}`, the seam-safe aggregation rule is

```text
chat_r(i) = sum_{d congruent r (mod N)} alpha^((d-r)/N) c_d(i),
```

where `d` runs through the displayed path channels with multiplicity.

## Proof

There are four first steps, `+1,-1,+s,-s`. Backtracking produces four copies
of `u_i`. Equal step-one directions produce `u_{i+/-2}`. Equal chord
directions produce the two products of chord signs at displacement `+/-2s`.
The two orderings of one step-one and one chord step give each displayed sum
of two chord signs. This exhausts all 16 ordered paths. Quasiperiodic boundary
factors are determined solely by the final displacement, so collided terms
add with the same boundary factor.

## Verification boundary

`verify_target_a_task60_general_model.py` independently constructs the
finite signed matrix, squares it over the integers, and compares it with a
separate path-by-path implementation. The current suite covers `s=2,...,6`,
generic and exceptional small rings, both holonomies, 288 general words, 200
alternating words, and an intentional coefficient tamper.

Two minimal obstructions to an unqualified channel statement are:

- `N=9,s=3,tau=1,alpha=1`, where the pure `+2` and mixed `s-1`
  contributions give `H[0,2]=3`;
- `N=7,s=2,alpha=1` with `tau=(1,-1,1,1,1,1,1)`, where `Q_0=-1` cancels
  the forward mixed paths but `H[0,3]=1` because `+3=-4 (mod 7)`.
