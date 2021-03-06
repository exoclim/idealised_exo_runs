# -*- coding: utf-8 -*-
"""Paths to data."""
from pathlib import Path

# Top-level directory containing code and data (one level up)
topdir = Path(__file__).absolute().parent.parent

# Modelling results
datadir = topdir.parent / "modelling" / "um" / "results"

sadir = datadir / "sa"  # standalone suites directory

# Plotting output
plotdir = topdir / "plots"
plotdir.mkdir(parents=True, exist_ok=True)