"""The four stage drivers. Each gate orchestrates components, writes its review
artifacts to review/, and returns a result the driver uses to decide whether to
stop for human review.

Gate contract (filled in M1.1-M1.4):
  gate1_testdata   -> extract band, montage raw+V
  gate2_preprocess -> filters x channels montage (methods=rows, channels=cols)
  gate3_detect     -> detector x channels montage with cyan outlines
  gate4_quantify   -> per-object count/area/intensity/density -> CSV + plots
"""
