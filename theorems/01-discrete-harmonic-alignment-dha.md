# Toward a Formal Definition of Discrete Harmonic Alignment in Cyclic Structures

**Revision:** 2026-08-08 — pairwise alignment formula corrected and claim boundary tightened.

## Abstract

This work proposes an initial formalization of Discrete Harmonic Alignment (DHA): a framework for analyzing how multiple periodic components interact within finite cyclic structures. The construction connects integer divisibility, cyclic discretization and multi-frequency alignment costs. It is a mathematical research framework, not a validated physical law.

---

## 1. Cyclic domain

Let

\[
\mathbb Z_N=\{0,1,\ldots,N-1\}
\]

with angular embedding

\[
\theta_k=\frac{2\pi k}{N}.
\]

A discrete frequency `f` induces the orbit

\[
\phi_f(t)=ft\pmod N.
\]

The individual return period to phase zero is

\[
T_f=\frac{N}{\gcd(N,f)}.
\]

---

## 2. Two events that must not be conflated

### 2.1 Pairwise phase alignment

Frequencies `f_i` and `f_j` align when

\[
f_it\equiv f_jt\pmod N.
\]

Equivalently,

\[
(f_i-f_j)t\equiv0\pmod N.
\]

If `f_i != f_j (mod N)`, the smallest positive alignment time is

\[
\boxed{
T_{\rm align}(f_i,f_j;N)
=\frac{N}{\gcd(N,|f_i-f_j|)}
}.
\]

If `f_i == f_j (mod N)`, the two phases agree at every step; by convention the smallest positive time is `1`.

### 2.2 Simultaneous return to phase zero

A stronger event is

\[
f_it\equiv0\pmod N,
\qquad
f_jt\equiv0\pmod N.
\]

Its smallest positive time is

\[
\boxed{
T_{\rm origin}(f_i,f_j;N)
=\operatorname{lcm}(T_i,T_j)
}
\]

where

\[
T_i=\frac{N}{\gcd(N,f_i)},
\qquad
T_j=\frac{N}{\gcd(N,f_j)}.
\]

The historical version of this document used `T_origin` while calling it the first pairwise alignment. That was too strong and is corrected here.

### Counterexample that separates the two definitions

For

```text
N=12, fi=1, fj=3
```

we have

\[
T_{\rm align}=\frac{12}{\gcd(12,2)}=6,
\]

but

\[
T_{\rm origin}=\operatorname{lcm}(12,4)=12.
\]

Therefore the two quantities are not interchangeable.

---

## 3. DHA system

Define

\[
S=(N,\{f_1,\ldots,f_k\}).
\]

Two useful cost matrices are now kept separate:

\[
A_{ij}=T_{\rm align}(f_i,f_j;N),
\]

\[
O_{ij}=T_{\rm origin}(f_i,f_j;N).
\]

`A` measures first mutual phase coincidence. `O` measures first simultaneous return to phase zero.

---

## 4. Aggregate metrics

The historical coherence quantity

\[
H_{\rm raw}=\frac{1}{\sum_{i<j}A_{ij}}
\]

is a valid authorial scalar once the intended cost is declared, but it is not automatically comparable across systems with different numbers of frequencies because the number of pairs changes.

For fixed `k`, it can be used as a relative ranking. For comparisons across different `k`, report at least the mean pair cost

\[
\overline A
=\frac{1}{\binom{k}{2}}
\sum_{i<j}A_{ij},
\qquad k\ge2,
\]

or another explicitly normalized statistic.

Claim boundary:

```text
pairwise_alignment_formula = MATH_PASS
joint_origin_formula = MATH_PASS
H_raw = VALID_DEFINITION
cross_k_comparability_of_H_raw = BLOCKED_WITHOUT_NORMALIZATION
```

---

## 5. Divisibility and orbit structure

For one frequency, orbit cardinality is

\[
|\mathcal O_f|=\frac{N}{\gcd(N,f)}.
\]

Composite values of `N` can provide many distinct subgroup/orbit structures, but “higher factorability always maximizes alignment for arbitrary frequency sets” is not a theorem of the current definitions.

It remains a testable optimization question:

```text
high_factorability_global_optimum = HYPOTHESIS
```

---

## 6. Examples

### Example A: `N=12`, frequencies `{3,4,6}`

Pairwise alignment costs are:

\[
A_{3,4}=12,
\quad
A_{3,6}=4,
\quad
A_{4,6}=6.
\]

Thus

\[
\overline A=\frac{12+4+6}{3}=\frac{22}{3}.
\]

### Example B: `N=10`, frequencies `{3,4}`

\[
A_{3,4}=\frac{10}{\gcd(10,1)}=10.
\]

These examples do not by themselves establish that `N=12` is globally more coherent than `N=10`; frequency-set size and composition must be controlled.

---

## 7. Geometric interpretation

The map

\[
k\mapsto e^{2\pi i k/N}
\]

embeds `Z_N` on the unit circle. Under this embedding, frequency orbits become finite cyclic point sets.

Calling `f=3` a triangle, `f=4` a square or `f=6` a hexagon is only exact when the generated orbit has the corresponding cardinality and the embedding is interpreted accordingly. The invariant quantity is the orbit structure determined by `N/gcd(N,f)`.

---

## 8. Relation to signal processing and electrical systems

DHA uses mathematical ingredients familiar from periodic systems, modular arithmetic and Fourier analysis. Resemblance to three-phase engineering or DFT structure is contextual; no engineering efficiency or physical resonance claim is authorized without a system-specific model and measurement.

---

## 9. Open problems

1. Optimal `N` for a declared distribution of frequency sets.
2. Weighted and probabilistic frequency ensembles.
3. Normalized cross-`k` coherence metrics.
4. Continuous-limit constructions with a specified topology/measure.
5. Comparison with standard synchronization and circular-statistics metrics.
6. Empirical usefulness in signal processing after baseline comparison.

---

## 10. Status

```text
finite_cyclic_domain = KNOWN_MATH
individual_period = KNOWN_MATH
pairwise_first_alignment = CORRECTED_MATH_PASS
joint_phase_zero_return = MATH_PASS
DHA_metric = AUTHOR_DEFINITION
factorability_optimality = HYPOTHESIS
physical_efficiency_claim = TOKEN_VAZIO
claim_allowed = false
```

The contribution is therefore a defined research metric and problem family, not a proof of a new universal harmonic law.
