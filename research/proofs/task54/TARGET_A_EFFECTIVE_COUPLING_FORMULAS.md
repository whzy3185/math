# Effective Coupling Formulas

> **Superseded as a one-mode-per-interface application.** These formal
> identities remain correct after replacing `Phi` by a `2r`-column map and
> proving the corresponding complement inverse. The old `r`-column spectral
> application is not proved.

Put the truncated modes in `Phi`, let `S=G^(-1/2)` for `G=Phi^*Phi`, define
the orthonormal column map `U=Phi S`, and write `E=(H-c6)Phi` and
`E_tilde=ES`. Use
`ell=floor((floor(D/4)-12)/8)`. The effective matrix is exactly

```text
H_eff(lambda)-c6 I
=G^(-1/2)Phi^*E G^(-1/2)
 -G^(-1/2)E^*Q(QHQ-lambda)^(-1)QE G^(-1/2).
```

The first term is the direct two-tail interaction. The second propagates the
two residual tails through the complementary Green function. The decay
theorem and `||(QHQ-lambda)^(-1)||<=400` imply, uniformly for fixed `r`,

```text
|<u_i,e_tilde_j>| = O((9/25)^ell),
|<Qe_tilde_i,(QHQ-lambda)^(-1)Qe_tilde_j>|
    = O((9/25)^(2ell)).
```

On a ring the direct term is the sum of the two arc contributions. Their
relative sign records holonomy and orientation; suppressing that sign would
not be invariant under the legal gauge choices.

Current problem-specific status: `OPEN_PENDING_2R_COMPLEMENT`; leading
coefficients remain `OPEN/HIGH_PRECISION`.
