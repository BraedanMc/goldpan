# ROADMAP — GOLDPAN

> **Why this file exists.** The roadmap is the *when / in what order*. It
> translates the north star into milestones. It is more stable than `TASKS.md`
> (the day-to-day checklist) but less stable than `NORTHSTAR.md` (the goal).
> Revisit it at the end of each milestone.

## Shape of the work

GOLDPAN has two axes:

- **The gate axis** — the four stages every run walks through:
  `test-data → preprocessing → detection → quantification`, each with a human
  review gate.
- **The difficulty axis** — the pigment cell types the same skeleton is applied
  to, in increasing order of hardness:
  `melanophores (easy) → xanthophores (medium) → iridophores (hard)`.

The roadmap builds the gate axis first (the skeleton), validated on the easy
case, then walks the difficulty axis.

## Milestones

### M1 — Skeleton stood up (current)
Build the four-gate framework end-to-end on the test subset, reusing proven
components. Each gate produces its reviewable montage and stops.

- [x] M1.0 Repo + planning framework (NORTHSTAR / ROADMAP / TASKS) + package
      scaffold with packaging best practices (`src/` layout, `pyproject.toml`).
- [ ] M1.1 Gate 1 — test-data extraction + montage.
- [ ] M1.2 Gate 2 — preprocessing sweep (filters × channel comparisons),
      montage as methods-rows × channels-columns.
- [ ] M1.3 Gate 3 — object-detection sweep, montage with cyan mask outlines.
- [ ] M1.4 Gate 4 — quantification (count/area/intensity/density) → CSV + plots.
- [ ] M1.5 End-to-end dry run on the test subset; every gate renders.

### M2 — Melanophores (easy) validated
Run the full skeleton on melanophores at the test scale, confirm it reproduces
what Path A already established, then scale up. This is the reference case that
proves the framework is correct.

### M3 — Xanthophores (medium)
Apply the same driver with a xanthophore configuration. The channel
comparisons (R−B, R/B, opponent/ratio channels) exist precisely so detection
reaches beyond dark melanophores to the orange xanthophores. Expect to tune
detection methods at Gate 3; the framework itself should not change.

### M4 — Iridophores (hard)
The hard case (reflective/iridescent, not simple pigment absorption). Likely
needs new channel comparisons and/or detection methods — added behind the same
gates, never replacing the skeleton.

### M5 — Package maturity
Harden GOLDPAN into a maintained package: tests with coverage, CI, a tagged
release (semantic versioning), published docs, and a stable public API. See the
packaging-best-practices checklist in `docs/PACKAGING.md`.

## Principles carried from prior work (standing rules)

- **Never clobber results** — append to the system of record; re-running a
  configuration upserts in place.
- **Every key result gets a human-readable form AND a graph** in the review dir.
- **POC / small-N first** before committing to a big run.
- **Review images before trusting numbers** — a montage is the deliverable, not
  just a table.
