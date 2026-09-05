# 06 — Relation Calculus: Midpoint Möbius Dynamics, Fold Curvature and Discrete Antiderivatives

**Author:** Rafael Melo Reis / RAFAELIA research route  
**Date:** 2026-09-05  
**State:** `FORMAL_RESULTS + NOVELTY_TOKEN_VAZIO`  
**Rule:** proof status and novelty status are independent.

## Abstract

This note collects exact statements emerging from the current geometric/modular/Fibonacci integration. Some are elementary consequences of classical mathematics; they are included to make the RAFAELIA relation graph explicit. No originality claim is made until prior-art review is complete.

## Definition 1 — Spherical midpoint operator

For `c != -1`, define

\[
T(c)=\frac{1+3c}{2(1+c)}.
\]

For three unit vectors with equal pairwise dot product `c`, this is the pairwise dot product of normalized midpoints of adjacent edges.

## Theorem 1 — Möbius representation and inverse

`T` is the Möbius transformation

\[
T(c)=\frac{3c+1}{2c+2}
\]

represented projectively by

\[
M=\begin{pmatrix}3&1\\2&2\end{pmatrix}.
\]

Its inverse is

\[
\boxed{T^{-1}(y)=\frac{2y-1}{3-2y}}.
\]

### Proof

Solve

\[
y(2+2c)=1+3c
\]

for `c`. This gives

\[
c(2y-3)=1-2y,
\]

hence the stated inverse. ∎

## Theorem 2 — Differential and integral forms

\[
\boxed{T'(c)=\frac1{(1+c)^2}},
\]

\[
\boxed{T''(c)=-\frac2{(1+c)^3}}.
\]

Moreover

\[
T(c)=\frac32-\frac1{1+c},
\]

so

\[
\boxed{\int T(c)dc=\frac32c-\ln|1+c|+C}.
\]

∎

## Theorem 3 — Fixed points

The only finite fixed points are

\[
\boxed{1\quad\text{and}\quad-1/2}.
\]

### Proof

`T(c)=c` is equivalent to

\[
2c^2-c-1=0=(2c+1)(c-1).
\]

∎

## Theorem 4 — Exact projective contraction

Define

\[
z(c)=\frac{c-1}{c+1/2}.
\]

Then

\[
\boxed{z(T(c))=\frac14z(c)}.
\]

Consequently

\[
\boxed{z(T^n(c))=4^{-n}z(c)}.
\]

Since

\[
z^{-1}(u)=\frac{2+u}{2(1-u)},
\]

one gets the closed iterate

\[
\boxed{
T^n(c)=
\frac{2+4^{-n}z(c)}{2(1-4^{-n}z(c))}
}.
\]

### Proof

Direct rational simplification of `z(T(c))` gives `z(c)/4`; iteration follows by induction. ∎

## Corollary 4.1 — Monotone convergence

For

\[
-1/2<c<1,
\]

\[
T(c)-c=
\frac{(1-c)(2c+1)}{2(1+c)}>0.
\]

The exact projective contraction implies

\[
T^n(c)\to1.
\]

## Theorem 5 — Asymptotic angular halving

Let

\[
c_{n+1}=T(c_n),
\qquad
\theta_n=\arccos c_n,
\]

with `-1/2<c_0<1`. Then

\[
\boxed{
\lim_{n\to\infty}\frac{\theta_{n+1}}{\theta_n}=\frac12
}.
\]

### Proof sketch

The projective coordinate contracts by `1/4`, so near the attracting fixed point `1-c_{n+1}` is asymptotic to `(1-c_n)/4`. Since

\[
1-\cos\theta\sim\theta^2/2,
\]

the angular scale contracts by the square root, giving `1/2`. ∎

## Definition 2 — Arc/chord ratio

\[
Q(\theta)=\frac{\theta}{2\sin(\theta/2)}.
\]

## Theorem 6 — Curvature-excess quartering

For the midpoint-refined sequence of Theorem 5,

\[
\boxed{
\lim_{n\to\infty}
\frac{Q(\theta_{n+1})-1}{Q(\theta_n)-1}
=\frac14
}.
\]

### Proof

Taylor expansion gives

\[
Q(\theta)=1+\theta^2/24+O(\theta^4).
\]

Combine with `theta_{n+1}/theta_n -> 1/2`. ∎

## Corollary 6.1 — Icosahedral special value

For

\[
c_0=1/\sqrt5,
\]

one has

\[
T(c_0)=\phi/2=\cos(\pi/5).
\]

Thus a normalized midpoint side on a unit-radius sphere has chord

\[
1/\phi
\]

and geodesic arc

\[
\pi/5,
\]

so

\[
\boxed{Q=\pi\phi/5}.
\]

This is a special value of the general midpoint operator, not evidence of Fibonacci causation.

## Definition 3 — Fold quotient

For `m>=2`,

\[
q_m(r)=\min(r,m-r),
\qquad
r\in\{0,\ldots,m-1\}.
\]

It is the quotient by the involution

\[
r\sim-r\pmod m.
\]

## Theorem 7 — Inverse classes of the fold

For `0<d<m/2`,

\[
\boxed{q_m^{-1}(d)=\{d,m-d\}}.
\]

Additionally

\[
q_m^{-1}(0)=\{0\},
\]

and for even `m`,

\[
q_m^{-1}(m/2)=\{m/2\}.
\]

Thus every non-fixed folded coordinate has exactly two exclusive inverse branches.

## Definition 4 — Cyclic discrete curvature

\[
\kappa_m(r)=q_m(r+1)-2q_m(r)+q_m(r-1),
\]

with indices modulo `m`.

## Theorem 8 — Fold-curvature localization

If

\[
m=2k+1,
\]

then

\[
\boxed{
\kappa_m(0)=2,
\quad
\kappa_m(k)=\kappa_m(k+1)=-1,
\quad
\kappa_m=0\text{ otherwise}
}.
\]

If

\[
m=2k,
\]

then

\[
\boxed{
\kappa_m(0)=2,
\quad
\kappa_m(k)=-2,
\quad
\kappa_m=0\text{ otherwise}
}.
\]

In both cases

\[
\sum_{r=0}^{m-1}\kappa_m(r)=0.
\]

### Proof

Away from the origin and antipodal fold locus, `q_m` is affine with slope `+1` or `-1`, so the second difference vanishes. Direct substitution at the slope-change points gives the listed masses. The cyclic second-difference sum telescopes to zero. ∎

### Corollary 8.1 — Mod 7

\[
q_7=(0,1,2,3,3,2,1),
\]

\[
\boxed{\kappa_7=(2,0,0,-1,-1,0,0)}.
\]

## Definition 5 — Integer Rafaeliana

\[
R_n=F_{n+3}-1,
\qquad n\ge1.
\]

## Theorem 9 — Rafaeliana is a discrete antiderivative

\[
\boxed{R_n=\sum_{k=0}^{n+1}F_k}.
\]

### Proof

Use the Fibonacci sum identity

\[
\sum_{k=0}^{N}F_k=F_{N+2}-1
\]

with `N=n+1`. ∎

## Corollary 9.1 — First and second differences

\[
\boxed{\Delta R_n=F_{n+1}},
\]

and, on the compatible range,

\[
\boxed{\Delta^2R_n=F_{n-1}}.
\]

## Theorem 10 — Antiderivative of the Rafaeliana

\[
\boxed{
\sum_{k=1}^{n}R_k=F_{n+5}-n-5
}.
\]

### Proof

Substitute `R_k=F_{k+3}-1`, shift the Fibonacci sum, and simplify. ∎

## Theorem 11 — Multi-base 420 embedding

Define

\[
\Pi(n)=
(n\bmod7,n\bmod10,n\bmod12,n\bmod20).
\]

Then the minimum period is

\[
\boxed{\operatorname{lcm}(7,10,12,20)=420}.
\]

The induced map from `Z_420` is injective onto the compatible generalized-CRT tuples.

This is a modular period theorem. It does not imply `420 physical attractors`.

## Theorem 12 — Conditional Poincaré-Hopf 21/21 statement

Assume a smooth vector field on `T^7` has exactly 42 isolated hyperbolic zeros; every zero is either a source or a sink; and their indices are `+1` and `-1` respectively. Then

\[
\boxed{N_{source}=N_{sink}=21}.
\]

### Proof

Poincaré-Hopf gives

\[
N_{source}-N_{sink}=\chi(T^7)=0.
\]

The hypothesis gives

\[
N_{source}+N_{sink}=42.
\]

Solve the two equations. ∎

**Boundary:** without the hypotheses, `42 -> 21+21` is not a theorem.

## Open problems / conjectures

### C1 — Spherical midpoint area renormalization

For

\[
\mathcal A(c)=3\arccos\frac{c}{1+c}-\pi,
\]

study

\[
\rho_A(c)=\frac{\mathcal A(T(c))}{\mathcal A(c)}.
\]

Classify monotonicity, convexity, special values and convergence to `1/4`.

### C2 — Frequency-f icosphere metric classes

Let

\[
N_{classes}(f)
\]

be the number of metric face classes after frequency-`f` subdivision and radial normalization. Determine a closed form or asymptotic classification.

### C3 — Multiscale ruler optimality

Test whether

\[
(F_n,F_{n+1},F_{n+3}-1)
\]

is extremal for a declared navigation/coverage functional relative to uniform, prime, Gray, Hilbert/Morton and random baselines.

## Novelty gate

```text
PROOF_VALIDITY != NOVELTY
ELEMENTARY_DERIVATION != NEW_THEOREM_IN_LITERATURE
APPLICATION_NOVELTY != IDENTITY_NOVELTY
```

All novelty claims remain `TOKEN_VAZIO_PRIOR_ART` until primary-source review.
