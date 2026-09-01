# Exact Certificate Semantics

## Failure witnesses

For an explicit signing `sigma*`, suppose an exact certificate proves

```text
rho(A_sigma*)^2 < t < rho_-(n)^2.
```

Then `m_n<=rho(A_sigma*)<rho_-(n)`, which is the entire failure obligation.
No enumeration of other signings is required.

The implemented LDL form proves the first strict inequality: if

```text
tI-A_sigma*^2 is positive definite,
```

then every eigenvalue of `A_sigma*^2` is strictly below `t`, hence
`rho(A_sigma*)^2<t`. Fraction-free Bareiss/rational LDL accepts only if every
leading pivot is strictly positive. The comparison `t<rho_-(n)^2` is an exact
rational or real-algebraic interval comparison. This is used for `n=32`,
`n=40`, and the 96-row interval `48<=n<240`.

## Equality certificates

For an equality order, the twisted signing gives only `m_n<=rho_-(n)`. The
finite proof must instead establish `rho(A_sigma)>=rho_-(n)` for every
signing. The certified route is:

```text
all signings -> switching representatives -> canonical states -> complete
finite closure -> exact terminal lower certificate.
```

A rejected local window has an integer vector with Rayleigh quotient strictly
above an exact upper enclosure of `rho_-(n)^2`; every completion containing it
is therefore impossible for a counterexample. Each surviving terminal is
checked either by an exact threshold eigenvalue or a full-ring integer
Rayleigh witness, in both holonomy sectors. This is a lower-bound argument,
not the LDL upper-bound argument used for failures.

The independent checker reconstructs the windows, overlaps, parity lift,
cyclic closure, dihedral quotient, holonomy lift, and terminal tests. Its
acceptance implication is precisely

```text
certificate accepted => rho(A_sigma)>=rho_-(n)
```

for every represented signing.
