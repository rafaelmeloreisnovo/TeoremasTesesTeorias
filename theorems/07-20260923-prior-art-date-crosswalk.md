# Prior-Art and Date Crosswalk — DHA / Toroidal / Structural Records

**Audit date:** 2026-09-23  
**State:** `PRIOR_ART_REVIEWED_PARTIAL / NOVELTY_UNPROVEN`

This document supplements the historical prior-art records without deleting or rewriting their chronology.

## Internal chronology

| Record | First recovered commit date | Commit |
|---|---:|---|
| DHA initial formalization | 2026-04-17T10:06:12Z | `6a554bc216c6a8c766645d1dd2cfb208d8467645` |
| DHA prior-art record | 2026-04-17T10:15:58Z | `4a7056830d58acfbd40973bf392fac09514919fc` |
| Discrete-modulated toroidal structures | 2026-04-17T10:32:52Z | `d709987ae1fd965b42707e111e081551b9acee41` |
| Discrete–continuous coupling | 2026-04-17T10:36:21Z | `91b19590eff8aebbb74f80ae42a37872c577b9cd` |
| DHA mathematical correction | 2026-08-08T17:19:23Z | `a69edcee1b7ed7e312fa82475732bf3126eefbbb` |

The April 2026 timestamp documents the research framework. The August 2026 timestamp documents the corrected first-alignment mathematics. They are not interchangeable priority dates.

## DHA boundary after literature comparison

Established components:
- finite cyclic group `Z_N`;
- orbit period `N/gcd(N,f)`;
- first mutual alignment from `(fi-fj)t == 0 mod N`, giving `N/gcd(N,abs(fi-fj))`;
- simultaneous origin return by LCM of individual periods.

Project-defined component:
- the specific aggregate coherence/cost functional called DHA, including `H_DHA = 1/sum A_ij` and its normalization policy.

Targeted alphaXiv search on 2026-09-23 found related synchronization literature including:
- arXiv:2211.00596, *Algebra of N-event synchronization* (2022-11-01);
- arXiv:2403.13440, extended Kuramoto phase/frequency synchronization (2024-03-20);
- arXiv:2503.19781, synchronization-definition equivalence in Kuramoto flow (2025-03-25).

No exact match to the declared DHA aggregate functional was established in that targeted search. Correct state:

```text
DHA_COMPONENT_MATH = KNOWN_MATH
DHA_EXACT_AGGREGATE_METRIC = PROJECT_DEFINED
DHA_GLOBAL_NOVELTY = NOVELTY_UNPROVEN
```

## Toroidal records

`T^n=(R/Z)^n` is classical. Choosing `n=7`, assigning named axes, linking a finite 42-state policy, or implementing Q16 transitions are project bindings unless a stronger theorem is separately proved.

The 2026 correction ledger remains authoritative for these boundaries:
- first-order stable recurrence = known mathematics;
- Fibonacci-indexed positive contraction is not quasi-periodic as originally written;
- fixed finite `Z_N` orbit is not topologically dense in a continuous circle;
- representation loss under rational simplification is valid, while “non-commutative arithmetic” remains unproved without explicit operators/domains.

## Correct citation language

Use:

> This repository records the DHA research framework as of 2026-04-17 and its corrected pairwise-alignment formula as of 2026-08-08. Its modular ingredients are established mathematics. The project-specific DHA aggregate functional is documented as an author-defined research metric; a targeted literature search dated 2026-09-23 found related synchronization work but did not establish an exact antecedent. This is not a claim of global novelty.

Do not equate:
```text
timestamped project record == worldwide novelty proof
```

## Cross-repository authority

The full dated matrix is maintained in:
`rafaelmeloreisnovo/Matem-tica-/docs/audits/2026-09-23_PRIOR_ART_DATE_MATRIX_MATHEMATICS_CHIPQUANTUM_V1.md`.

## R3

`F_ok`: original records preserved; April/August DHA chronology disambiguated; related literature and claim boundary attached.  
`F_gap`: exhaustive bibliographic search for the exact DHA functional and formal comparison against standard circular/synchronization metrics.  
`F_next`: define a normalized DHA baseline suite and compare it numerically against established synchronization/order-parameter metrics.
