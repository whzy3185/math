# IMS Constant Audit

Task 53's `576/R^2` bound uses only the absolute row sum 16 and the generic
estimate `S_d<=9d^2/(2R^2)`. It is valid but discards the exact offset
structure of `H=A^2`.

For distinct cyclic offsets at the analytic-tail orders,

```text
|H_(a,a+/-1)|<=2, |H_(a,a+/-2)|<=1,
|H_(a,a+/-3)|<=2, |H_(a,a+/-4)|<=1.
```

Direct summation of the normalized tent gives

```text
S_d(R)=3(2d^2R-d(d^2-1))/(R(2R^2+1)).
```

Therefore the global Schur row bound is exactly

```text
2S_1+S_2+2S_3+S_4
=(240R-342)/(R(2R^2+1)) <=120/R^2.
```

This is a global spectral-cap estimate; it does not use orthogonality to a
localized mode. The separate `320/R^2` sine/cosine number in the early
Task 54 complement argument has different cutoff hypotheses and is not used
as a replacement for this theorem.

Status: PROVED.
