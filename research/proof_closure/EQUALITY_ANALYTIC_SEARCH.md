# Equality Analytic Search

## E1: trace and moment route

For `n>=9`, write `d(Q)=#{i:Q_i=+1}`. The exact row formula for `A^2` gives

```text
tr(A^4)=20n+16d(Q).
```

Indeed, the diagonal, distance-two, and distance-four entries contribute 20
per row; each positive `Q_i` activates four oriented odd-distance entries of
squared magnitude 4. Therefore

```text
rho(A)^4 >= tr(A^4)/n = 20+16d(Q)/n,
rho(A)^2 >= sqrt(20+16d(Q)/n) <= 6.
```

The target `rho_-(n)^2` is already close to 8. Thus the fourth moment cannot
prove the desired universal lower bound. More generally, a fixed trace power
cannot settle the large-order reference family: its normalized fixed-
power moment converges to the integral of a nonconstant bulk symbol, which is
strictly below `8^k`, whereas `rho_-(n)^(2k)` tends to `8^k`. A successful
moment proof would need growing moments or additional structural information,
so E1 is not pursued as a standalone equality proof.

## E2/E3: local obstruction and forbidden-pattern rigidity

The existing certified local-window language was analyzed separately from its
terminal enumeration. For `n=34` and `n=36`, the only recurrent components
are the reference loop `0` and a four-state cycle with output word `1000`.
Consequently:

* at `n=34`, the nonreference cycle cannot close because 4 does not divide 34;
* at `n=36`, it closes as `1000` repeated nine times, but has odd `Q` parity
  and so has no cyclic `tau` lift.

This explains the striking one-terminal outcome at these two orders. It is
not yet an analytic proof: producing the current local language requires
testing all 13- or 14-bit windows with stored exact Rayleigh vectors. The
reduction is valuable reconnaissance, not a replacement theorem.

At `n=38,42,44,46`, the recurrent nonreference component has respectively
18, 28, 28, and 28 states. Its terminal words are structured gap words over
`{4,6,8}`, but it is not a short periodic list. The present local language
therefore does not yield the requested symbolic-dynamics rigidity theorem.

## E4: transfer lower bound

The exact single-interface closure has an order-nine exterior-power
recurrence. After shifting the energy, its coefficients alternate in sign and
the natural positivity cone is not invariant. No trace/discriminant/
projective monotonicity theorem has yet been found. This blocks a uniform
transfer lower bound for equality orders.

## E5/E6/E7/E8 status

No equitable quotient, universal Rayleigh formula, minimal-counterexample
surgery, or sign-flip stationarity condition has yet produced a theorem that
dominates the existing exact finite proof. Those routes remain open rather
than being replaced by conjectural prose.

## Reusable partial result

The 34/36 recurrent-core fact and the fourth-moment obstruction are recorded
in `equality_analytic_search.json`. They guide the next search toward a small
family of stronger local quadratic forms or a direct transfer proof; neither
permits deletion of the finite equality certificates today.
