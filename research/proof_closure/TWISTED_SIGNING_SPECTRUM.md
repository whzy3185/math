# Twisted Signing Spectrum

Let `n>=8` be even. In the Hamilton gauge used by Suvagiya, let `R` be the cyclic shift, `D=diag((-1)^j)`, and `phi=pi/n`. The anti-periodic twisted class has a Hermitian representative

```text
A(phi)=exp(i phi)R + exp(-i phi)R^*
     + exp(2i phi)D R^2 + exp(-2i phi)R^(-2)D.
```

It has alternating triangle flux and step-one holonomy `-1`; equality of all cycle holonomies implies diagonal-unitary equivalence to the real signed adjacency representative. Thus it suffices to compute this Hermitian matrix.

For Fourier vectors `f_k(j)=n^(-1/2)exp(2pi i k j/n)`, the plane spanned by `f_k,f_(k+n/2)` is invariant. On it the matrix is

```text
[ 2 cos(theta_k+phi)       2 cos(2theta_k+2phi) ]
[ 2 cos(2theta_k+2phi)    -2 cos(theta_k+phi)   ],
```

where `theta_k=2pi k/n`. Hence its two eigenvalues are

```text
+- 2 sqrt(g(theta_k+phi)),
g(theta)=cos^2(theta)+cos^2(2theta).
```

The sampled angles are `(2k+1)pi/n`. Put `u=cos^2(theta)`. Then `g(theta)=4u^2-3u+1`. On `[0,pi/2]`, this decreases until `cos^2(theta)=1/4` and then increases; the symmetry `g(pi-theta)=g(theta)` reduces the maximum on the shifted grid to the smallest positive angle, provided `g(pi/n)>1`. For even `n>=8`, `pi/n<=pi/8`, and

```text
g(pi/n)>=g(pi/8)=(4+sqrt(2))/4>1.
```

Therefore

```text
rho_-(n)^2=4g(pi/n)
          =4+2cos(2pi/n)+2cos(4pi/n).
```

The evenness of `n` is used in pairing `k` with `k+n/2` and in the shifted anti-periodic Fourier lattice. This is an analytic proof; no matrix diagonalization or floating-point optimization is used.
