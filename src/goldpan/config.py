"""GOLDPAN configuration — all tunables in one place, no logic.

Every path, frame number, band, filter name and channel name the workflow uses
lives here so a component never hardcodes them. Changing cell type or scale is
a config edit, not a code edit.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

# --- fixed project ground truth (see NORTHSTAR.md) ---------------------------
PROJECT_BASE = Path("/Users/bmcc/Documents/Projects/ML_scRNAseq/ML_cells")
IMAGES_DIR = PROJECT_BASE / "images_training"

# Middle-fifth width band. Images are (1000, 3600, 3); 3600/5 centred = 1440:2160.
BAND: tuple[int, int] = (1440, 2160)

# The three test frames and their actual filenames (frame 32 lacks the "ROI"
# token — confirmed on disk).
TEST_FRAMES: dict[int, str] = {
    14: "14str_5000x2200_0014_14_ROI_180813.tif",
    32: "14str_5000x2200_0032_14_180831.tif",
    50: "14str_5000x2200_0050_14_ROI_180922.tif",
}

# --- review output -----------------------------------------------------------
REVIEW_DIR = Path(__file__).resolve().parents[2] / "review"


@dataclass
class GoldpanConfig:
    """One run's configuration. The driver takes an instance of this."""

    # Which pigment cell type this run targets. Drives channel/filter choices
    # and (later) detection tuning. One of: "melanophore", "xanthophore",
    # "iridophore".
    cell_type: str = "melanophore"

    frames: dict[int, str] = field(default_factory=lambda: dict(TEST_FRAMES))
    band: tuple[int, int] = BAND

    # Preprocessing filters to sweep (registered in components.preprocess).
    filters: list[str] = field(default_factory=lambda: [
        "gauss_bgsub",      # Path A locked recipe, sigma=75
        "rollingball",
        "black_tophat",
        "white_tophat",
        "clahe",
    ])

    # Channel comparisons to sweep (registered in components.channels).
    # These reach beyond dark melanophores to orange xanthophores, etc.
    channels: list[str] = field(default_factory=lambda: [
        "V",                # luminance (mel baseline)
        "R_minus_B",        # orange/xanthophore opponent
        "R_over_B",         # lighting-invariant orange ratio
        "G_over_R",         # second opponent ratio
        "max_minus_min",    # saturation-like
        "Lab_a",            # green-red opponent
        "Lab_b",            # blue-yellow opponent
    ])

    # Detection methods to sweep (registered in components.detect).
    detectors: list[str] = field(default_factory=lambda: [
        "otsu",
        "otsu_offset",      # Path A: Otsu minus an offset
        "adaptive",
        "local_maxima",
    ])


DEFAULT = GoldpanConfig()
