# NORTHSTAR — GOLDPAN

> **Why this file exists.** The north star is the stable *why/what* of the
> project. It changes rarely. When a decision is unclear, it should be
> resolvable by asking "does this serve the north star?" Roadmap and tasks
> flow from this document, never the other way around.

## Project

**GOLDPAN** — **G**ated **O**bject-**L**ocalization & **D**etection for
**P**igment cell **AN**alysis.

## Goal

GOLDPAN is a reusable, documented workflow for detecting and quantifying
pigment cells in zebrafish imaging data. It extracts a small test subset, then
advances through four human-gated stages — test-data preview, preprocessing
sweep, object-detection sweep, and quantification — pausing at each gate with a
reviewable montage so the method is validated by eye before committing to a
full run. The same skeleton applies across pigment cell types of increasing
difficulty: melanophores (easy), xanthophores (medium), and iridophores (hard).
It is built from the preprocessing filters and channel-comparison components
already proven on this project, and is structured as a versioned Python package
— tracked in a private GitHub repo owned by `braedanmc` — so it can mature into
a maintained tool.

## Success criteria

The project is succeeding when all of these hold:

1. **Gated, reviewable, reproducible.** Every stage stops and emits a montage
   (or table) a human reviews before the next stage runs. Re-running a stage on
   the same inputs produces the same outputs.
2. **Proven components, not reinvented.** Preprocessing and channel-comparison
   building blocks are the recipes already validated on this project
   (`gauss_bgsub` σ=75, rolling-ball, tophat family; opponent/ratio channels
   R−B, R/B, G/R, max−min, HSV/Lab). New methods are added, not substituted,
   and only after a gate review.
3. **Generalizes across cell types.** The same driver runs melanophores,
   xanthophores, and iridophores by changing configuration, not code.
4. **Packaged with best practices.** It is an installable, versioned Python
   package (`src/` layout, `pyproject.toml`, pinned env, tests, semantic
   versioning, a clean public API) — maintainable as it grows, not a pile of
   scripts.
5. **Self-documenting.** The north star, the roadmap, and the current task list
   live in the repo and stay current, so the project is navigable by anyone
   (including future-us) with no external context.

## Non-goals (for now)

- Not a real-time or production inference service — it is an offline analysis
  workflow with human review in the loop.
- Not a replacement for the locked Path A melanophore pipeline — GOLDPAN
  *reuses* its recipes and generalizes them; it does not re-derive them.
- Not a GUI. Review happens through saved montage images and CSVs.

## Fixed facts (the ground truth this project is built on)

- **Test frames:** 14, 32, 50 from the `14str` series.
- **Test band:** the middle fifth of the image width, columns `1440:2160`
  (images are `(1000, 3600, 3)`), matching the existing `BAND = (1440, 2160)`.
- **Montage convention:** preprocessing method = rows, channel comparison =
  columns. Detection montages show cyan mask *outlines* on the preprocessed
  image, never filled overlays.
- **Source environment:** the `laya` conda env
  (`/Users/bmcc/miniforge3/envs/laya`) has cv2, skimage, sklearn, scipy.
