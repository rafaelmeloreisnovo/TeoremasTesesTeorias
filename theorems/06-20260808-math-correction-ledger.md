# Mathematical Correction Ledger — DHA / Toroidal Structures / Invariants

**Date:** 2026-08-08  
**Status:** `FAIL_CLOSED_REVIEW`  
**Claim gate:** `claim_allowed=false`

This ledger preserves the historical theorem/prior-art files while recording corrections required before their statements are reused as formal mathematics.

## 1. `01-discrete-harmonic-alignment-dha.md`

Corrected in the same branch.

Historical issue:

```text
fi*t == fj*t (mod N)
```

was paired with a formula for simultaneous return of both phases to zero.

Correct first mutual alignment:

\[
T_{align}=N/\gcd(N,|f_i-f_j|).
\]

Joint phase-zero return:

\[
T_{origin}=\operatorname{lcm}(N/\gcd(N,f_i),N/\gcd(N,f_j)).
\]

These are distinct events.

## 2. `03-discrete-modulated-toroidal-structures.md`

### 2.1 Stable recurrence

The recurrence

\[
s_{t+1}=(1-\alpha)s_t+\alpha x_t,\qquad0<\alpha<1
\]

is a standard exponentially weighted first-order stable filter under bounded input. This is mathematically valid, but the stability mechanism is not novel by itself.

Status:

```text
bounded_input_bounded_state = KNOWN_MATH
novel_universal_invariant = BLOCKED
```

### 2.2 Fibonacci-indexed contraction

The statement that indexing

\[
q^n,\quad0<q<1,
\]

by Fibonacci indices creates a quasi-periodic scaling is false as written.

For

\[
a_k=q^{F_k},
\]

`F_k` grows and `q^n` strictly decreases, so

\[
a_{k+1}<a_k,\qquad a_k\to0.
\]

Correct description:

```text
nonuniform Fibonacci-indexed contraction
```

not quasi-periodicity.

A genuine quasi-periodic construction would require an appropriate phase/dynamical object, for example irrational rotations on a torus, not a positive monotone scalar sequence.

### 2.3 Finite modular orbit is not topologically dense

For

\[
x\mapsto x+k\pmod N
\]

inside fixed finite `Z_N`, the orbit contains

\[
N/\gcd(N,k)
\]

points. It cannot be dense in a continuous circle in the ordinary topological sense.

A continuous-envelope statement requires a declared limit such as `N -> infinity`, a sampling scheme and a topology/metric.

Status:

```text
fixed_finite_orbit_dense = FAIL
continuum_envelope_limit = TOKEN_VAZIO
```

## 3. `04-discrete-continuous-coupling-invariants.md`

### 3.1 Rational simplification and lattice position

The observation that `77/33` and `7/3` represent the same rational number but different integer pairs is correct. The formal object is a quotient/equivalence relation:

\[
(a,b)\sim(c,d)\iff ad=bc,
\qquad b,d\ne0.
\]

The map from integer pairs to rational numbers is many-to-one.

Therefore the lost information is representation/lattice-coordinate information. Calling this “non-commutative arithmetic” is stronger than the demonstrated fact unless explicit operators and domains are defined.

Status:

```text
same_rational_different_integer_pair = MATH_PASS
quotient_map_loses_representation = MATH_PASS
noncommutative_arithmetic_theorem = TOKEN_VAZIO
```

### 3.2 Composite `N` and subcycles

For modular translation by `k`, orbit cardinality is `N/gcd(N,k)`. Composite `N` supports additional subgroup structures, but complex visual interference is an output of a specific connection/plotting rule, not a theorem from compositeness alone.

### 3.3 “Emergent envelopes”

Finite chord diagrams may visually approximate envelopes for families of parameters, but convergence to a curve needs a limiting sequence and error notion. Until then:

```text
envelope_convergence = HYPOTHESIS
```

## 4. Cross-repository boundary

The cleaner 2026 formalization in `rafaelmeloreisnovo/Matem-tica-` should be preferred for claims involving:

- exact `sqrt(3)/2` identities;
- symbolic rewrite theorem 123;
- Ω-CUBE-42 finite cardinality;
- strict-potential DAG/forest proof.

Historical material remains useful as prior art and research origin but must not override later formal corrections.

## 5. Status summary

```text
DHA_first_alignment = CORRECTED_MATH_PASS
DHA_joint_origin_return = MATH_PASS_AFTER_RENAME
q_power_Fibonacci_quasiperiodic = FAIL
finite_ZN_dense_orbit = FAIL
stable_first_order_filter = KNOWN_MATH
rational_pair_representation_loss = MATH_PASS
noncommutative_arithmetic_claim = TOKEN_VAZIO
envelope_limit = TOKEN_VAZIO
physical_toroidal_resonance = TOKEN_VAZIO
```

`F_next`: attach executable counterexamples and normalized metrics before promoting any of these objects to theorem status beyond the precise statements above.
