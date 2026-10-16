# GOLDPAN

**G**ated **O**bject-**L**ocalization & **D**etection for **P**igment cell
**AN**alysis.

A reusable, documented, human-gated workflow for detecting and quantifying
pigment cells in zebrafish imaging data — melanophores (easy), xanthophores
(medium), and iridophores (hard) — built from preprocessing and
channel-comparison components proven on this project.

## How the project is navigated

Three living documents drive the work, from most stable to most volatile:

| File | What it holds | Changes |
|------|---------------|---------|
| [`NORTHSTAR.md`](NORTHSTAR.md) | The goal and success criteria | rarely |
| [`ROADMAP.md`](ROADMAP.md) | Milestones toward the north star | per milestone |
| [`TASKS.md`](TASKS.md) | The current checklist | continuously |

Packaging standards: [`docs/PACKAGING.md`](docs/PACKAGING.md).

## The four gates

Every run walks four stages, each stopping with a reviewable montage before the
next begins:

1. **Test data** — extract the middle-fifth band of the test frames; montage.
2. **Preprocessing sweep** — filters × channel comparisons; montage
   (methods = rows, channels = columns).
3. **Detection sweep** — detection methods; montage with cyan mask outlines.
4. **Quantification** — count / area / intensity / density → CSV + plots.

## Install (development)

Runtime is the `laya` conda env. For development:

```bash
conda activate laya
pip install -e ".[dev]"   # editable install into the env
```

## Run

```bash
goldpan            # walks the gates for the configured cell type
```

## Layout

```
src/goldpan/
  config.py        # all tunables (cell type, frames, band, filters, channels)
  components/      # pure, reusable transforms (preproc, channels, detectors)
  gates/           # the four stage drivers
  driver.py        # entry point that walks the gates
tests/             # pytest suite (M5)
docs/              # packaging + design docs
review/            # generated artifacts (gitignored)
```

Status: **M1 — skeleton stood up.** See `TASKS.md`.
