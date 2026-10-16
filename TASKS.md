# TASKS — GOLDPAN

> **Why this file exists.** Tasks are the *now* — concrete, checkable work items
> for the current milestone. Tick them off as they land. When a milestone
> completes, archive its tasks under "Done" and pull the next milestone's work
> up from `ROADMAP.md`. Keep this short; it is a working list, not a log.

**Active milestone:** M1 — Skeleton stood up.

## In progress

- [ ] **M1.1 Gate 1 — test data**
  - [ ] `config.py`: cell type, frames (14/32/50), band (1440:2160), filter
        list, channel-comparison list.
  - [ ] Extract middle-fifth band of the 3 test frames → cached crops.
  - [ ] Montage: raw RGB crop + V channel per frame → `review/gate1_testdata/`.
  - [ ] STOP for Gate 1 review.

- [ ] **M1.2 Gate 2 — preprocessing sweep**
  - [ ] Channel-comparison bank (R−B, R/B, G/R, max−min, HSV, Lab opponents).
  - [ ] Filters: `gauss_bgsub` σ=75, rolling-ball, black/white tophat, CLAHE.
  - [ ] Montage: methods = rows, channel comparisons = columns, one per frame.
  - [ ] STOP for Gate 2 review.

- [ ] **M1.3 Gate 3 — detection sweep**
  - [ ] Detection methods: Otsu, adaptive threshold, Otsu−offset (Path A),
        local-maxima/blob.
  - [ ] Montage: methods = rows, channels = columns, cyan mask OUTLINES on the
        preprocessed image.
  - [ ] STOP for Gate 3 review.

- [ ] **M1.4 Gate 4 — quantification**
  - [ ] Per-object: count, area, mean intensity per channel, density.
  - [ ] Human-readable CSV + summary plots → `review/gate4_quant/`.

- [ ] **M1.5 Verification**
  - [ ] End-to-end dry run on the test subset; confirm every gate renders and
        the quant table is produced.

## Backlog (pull up when M1 is done)

- Melanophore config + small-scale validation (M2).
- GitHub remote wired up (private, owned by `braedanmc`) once `gh` is installed
  or the remote is created manually.

## Done

- [x] **M1.0** Repo created, `src/` layout scaffold, `pyproject.toml`,
      NORTHSTAR / ROADMAP / TASKS, packaging-best-practices doc. (2026-10-16)

## Conventions reminder (don't re-litigate these)

- Methods-rows × channels-columns for preprocessing montages.
- Cyan outlines, never filled overlays, for detection montages.
- Never clobber; append/upsert. Review images before trusting numbers.
- `laya` conda env is the runtime.
