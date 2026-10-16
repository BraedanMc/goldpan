# PACKAGING — best practices for building GOLDPAN as a package

> **Use best practices for package building.** GOLDPAN is meant to mature from
> a workflow into a maintained Python package. This checklist is the standard
> we hold it to. Items marked (M5) are hardening we defer to the maturity
> milestone, but the structure is laid down from day one so we never have to
> refactor into it.

## Already in place (day one)

- **`src/` layout.** The importable package lives under `src/goldpan/`, not at
  the repo root. This prevents accidentally importing the in-tree copy instead
  of the installed one and is the modern recommended layout.
- **`pyproject.toml` as the single source of build/metadata config** (PEP 517/
  518/621). No `setup.py`. Build backend: setuptools.
- **Pinned runtime.** The `laya` conda env is the declared runtime; its
  critical packages (cv2, skimage, sklearn, scipy, numpy, matplotlib,
  tifffile) are recorded. `environment.yml` captures it for reproducibility.
- **Clear module boundaries.**
  - `goldpan.config` — all tunables (cell type, frames, band, filters,
    channels); no logic.
  - `goldpan.components` — pure, reusable transforms (preprocessing filters,
    channel comparisons, detection methods). No I/O, no side effects.
  - `goldpan.gates` — the four stage drivers; they orchestrate components and
    write review artifacts.
  - `goldpan.io` / `goldpan.review` — loading images and writing montages/CSVs.
- **A single documented entry point** (`goldpan.driver`) that walks the gates,
  so there is one obvious way to run the workflow.
- **`.gitignore`** excludes generated artifacts, caches, large intermediates,
  and env dirs — the repo tracks code and docs, not outputs.

## Deferred to M5 (package maturity)

- **Tests + coverage** — `tests/` with pytest; components tested in isolation
  with small synthetic inputs. Target meaningful coverage of `components`.
- **Semantic versioning** — `MAJOR.MINOR.PATCH`; version declared once in
  `pyproject.toml` and exposed as `goldpan.__version__`. Tag releases in git.
- **CI** — run the test suite and a lint pass on push (GitHub Actions once the
  remote exists).
- **Lint / format / type-check** — ruff (lint + format) and a type checker;
  config in `pyproject.toml`.
- **Stable public API** — a curated `goldpan/__init__.py` export surface; a
  `CHANGELOG.md`; docstrings on every public function.
- **Editable install for development** — `pip install -e .` into the `laya`
  env so imports resolve to the working tree during development.

## Rules that keep the package clean

- Components stay **pure and I/O-free** so they are testable and reusable
  across cell types. All paths/config come from `goldpan.config`, never
  hardcoded in a component.
- Adding a method (filter, channel, detector) means **adding a function and
  registering it**, not editing the driver — the sweeps iterate over
  registries.
- Generated review artifacts are **never committed**; only the code that
  produces them is.
