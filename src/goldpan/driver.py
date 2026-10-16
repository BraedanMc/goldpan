"""GOLDPAN entry point — walks the four gates, pausing for review at each.

This is the single documented way to run the workflow (`goldpan` on the CLI).
Gate bodies are filled in across M1.1-M1.4; this skeleton defines the order and
the stop-for-review contract so the structure is fixed from the start.
"""
from __future__ import annotations

import argparse

from goldpan import __version__
from goldpan.config import DEFAULT, GoldpanConfig

GATES = ["testdata", "preprocess", "detect", "quantify"]


def run(cfg: GoldpanConfig, start: str = "testdata", stop_after: str | None = None) -> None:
    """Walk the gates in order. Each gate writes review artifacts and stops for
    human review before the next runs (unless driven non-interactively).

    Not yet implemented — M1.1 wires in gate1, etc. This stub establishes the
    order and is importable so the package scaffold is valid.
    """
    raise NotImplementedError(
        "GOLDPAN gates are implemented in M1.1-M1.4; see TASKS.md."
    )


def main() -> None:
    p = argparse.ArgumentParser(prog="goldpan", description=__doc__)
    p.add_argument("--version", action="version", version=f"goldpan {__version__}")
    p.add_argument("--cell-type", default=DEFAULT.cell_type,
                   choices=["melanophore", "xanthophore", "iridophore"])
    p.add_argument("--start", default="testdata", choices=GATES)
    p.add_argument("--stop-after", default=None, choices=GATES)
    args = p.parse_args()
    cfg = GoldpanConfig(cell_type=args.cell_type)
    run(cfg, start=args.start, stop_after=args.stop_after)


if __name__ == "__main__":
    main()
