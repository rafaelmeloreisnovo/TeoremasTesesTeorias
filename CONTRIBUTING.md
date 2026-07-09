# Contributing to TeoremasTesesTeorias

## Scope

Contributions must relate to formal mathematical content:

- Theorems in discrete mathematics, number theory, or topology (`theorems/`)
- Extended research theses (`theses/`)
- Computational verification scripts (`src/`)
- Supporting analysis (`docs/`)

## Prior Art Standards

Documents in `theorems/` serve as **prior art records**. They must:

1. Include a dated abstract
2. Explicitly state what is new vs. what builds on existing work
3. Cite all prior work (group theory, harmonic analysis, cyclic group literature)
4. Be submitted as Markdown with proper LaTeX notation

## Branch Naming

| Type | Pattern |
|---|---|
| New theorem | `theorem/<name>` |
| New thesis | `thesis/<name>` |
| Script | `feat/src-<name>` |
| Fix | `fix/<document>` |

## Commit Convention

```
theorem: add DHA extension to continuous domains
thesis: add structural invariance program chapter 2
fix: correct T7 state vector definition in theorem-03
docs: expand 9papers-structure with paper 10 skeleton
```

## Mathematical Document Format

```yaml
---
title: "Full Document Title"
type: "theorem | prior-art | thesis | analysis"
date: YYYY-MM-DD
version: "1.0"
---
```

Followed by: Abstract → Background → Formalization → Implications → References.

## Pull Request Checklist

- [ ] Document placed in correct directory (`theorems/`, `theses/`, `src/`, `docs/`)
- [ ] YAML front matter included
- [ ] Prior work properly cited
- [ ] LaTeX notation renders correctly in Markdown
- [ ] README theorems table updated if adding new theorem
- [ ] CHANGELOG.md updated under `[Unreleased]`
