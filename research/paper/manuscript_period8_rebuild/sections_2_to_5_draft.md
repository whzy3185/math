# Draft text for Sections 2--5

## 2. Gauge coordinates and finite Bloch decomposition

Switching by a diagonal sign matrix preserves the adjacency spectrum. We use
Hamilton gauge: every step-one edge has sign +1, the step-two edge beginning
at i has sign tau_i, and the residual sign around the step-one Hamilton cycle
is alpha in {+1,-1}. The periodic lift acts by

    (A_tau x)_i = x_(i-1)+x_(i+1)+tau_(i-2)x_(i-2)+tau_i x_(i+2).

If tau has period p and n=pL, write i=pm+r. The finite boundary condition is
x_(i+n)=alpha x_i. The cell ansatz x_(pm+r)=z^m v_r has z^L=alpha and gives a
p by p Hermitian fiber H_tau(z). Thus the finite matrix is the orthogonal
direct sum of the fibers indexed by the finite root set z^L=alpha. This must
not be confused with the infinite-volume family indexed by the full unit
circle.

## 3. The chiral period-eight fiber

Fix tau=(1,1,-1,1,-1,-1,1,-1). In the ordered eight-site cell basis the
fiber has the entries recorded in the theorem dependency map. Choose xi with
xi^2=z. The signed translation by four sites, normalized by xi^(-1), gives an
involution J_z with J_z^2=I and J_z H(z)=-H(z)J_z. Hence the fiber is
off-diagonal in the plus/minus eigenspace splitting of J_z.

Writing H(z)=[[0,B],[C,0]], the squared eigenvalues are eigenvalues of BC.
With s=xi+xi^(-1), a second block decomposition reduces det(yI-BC) to a
two-by-two determinant with

    Q=[[1+xi^(-1),2],[2,1-xi^(-1)]],
    R=[[1+xi,2],[2,1-xi]].

Expansion yields

    P(y,c)=y^4-16y^3+(80-2c)y^2+(-128+16c)y+c^2-13c+38,

where c=z+z^(-1). At c=2, P factors into the two quadratic factors giving
the exact infinite-volume squared edge eta=4+sqrt(10+2sqrt(5)).

## 4. Uniform polynomial certificate

Put B0=1561/200. For y at least B0 and -2 at most c at most 2, direct
differentiation gives partial_c P(y,c)<0. Thus P(y,c) is at least P(y,2).
Writing y=B0+u gives

    P(B0+u,2)
      =u^4+(761/50)u^3+(1337363/20000)u^2
       +(136311081/2000000)u+84332641/1600000000.

Every displayed coefficient is positive. Therefore no squared fiber
eigenvalue can be at least B0. This is the uniform analytic certificate; it
does not use a numerical root search.

## 5. Infinite counterexample family

For the anti-periodic twisted signing, the shifted Fourier grid gives

    rho_minus(8L)^2
      =4+2 cos(pi/(4L))+2 cos(pi/(2L)).

The relevant two-by-two blocks have squared eigenvalues four times
g(t)=cos(t)^2+cos(2t)^2. Symmetry reduces the grid to [pi/(8L),pi/2]. On the
initial interval g decreases; on the remaining interval it is at most one.
The maximum is therefore at the first shifted-grid point. Exact radical
evaluation at L=4 gives B0<rho_minus(32)^2, and monotonicity extends the
strict inequality to every L at least 4. Together with Section 4 this proves
the main theorem.

## Formal-verification note

The alpha=+1 finite theorem kernel for Sections 2--5 is checked in Lean.
The Lean statement is expressed through the Hermitian finite eigenvalue list:
each squared eigenvalue is strictly below the twisted squared benchmark. The
statement does not claim formal alpha=-1 packaging or formal coverage of the
structural results in Sections 6--7.
