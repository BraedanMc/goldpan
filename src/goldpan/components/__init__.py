"""Pure, reusable transforms: preprocessing filters, channel comparisons,
and detection methods. No I/O, no side effects — components take arrays and
return arrays, so they are testable in isolation and reused across cell types.

Each submodule exposes a registry (name -> callable) that the gate sweeps
iterate over. Adding a method means registering a function, not editing a gate.
"""
