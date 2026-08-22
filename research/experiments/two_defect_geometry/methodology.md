# Two-Defect Geometry Methodology

Status: **EXPERIMENTAL NON-THEOREM**

For every even `p` from 8 through 64 and every reflected separation class
`1<=s<=p/2`, the experiment constructs the legal word having `Q_0=Q_s=+1`
and all other entries `-1`. Odd periods are excluded because this word would
have product `-1` and hence no periodic `tau` lift.

The spectral screen starts from a deterministic 128-point Bloch grid and
refines neighborhoods of the eight largest sampled values by golden-section
maximization. This is an adaptive continuous-parameter numerical estimate,
not a rigorous enclosure. Exact closed-walk moments through `F_8` are also
recorded for every case.

Potential minima receive one of two rigorous follow-ups. The period-eight
target is identified by the existing exact theorem. Other cases are tested at
the two Bloch endpoints; a floating eigenvector proposes an integer vector,
but the accepted Rayleigh quotient is computed exactly over the rationals and
compared through the exact chain

```text
R(Q)^2 >= Rayleigh quotient > 1561/200 > eta.
```

The final comparison sign is checked symbolically. Failure of this endpoint
test is recorded as absence of this certificate, never as an upper bound.

All records are deterministically ordered by `(p,s)`. No randomness is used.
The JSON metadata pins the script hash, repository commit, and software
versions used by the run.
