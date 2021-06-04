# -*- coding: utf-8 -*-
"""Plotting functions."""
from pathlib import Path

import iris

import matplotlib.pyplot as plt

from aeolus.calc import spatial_mean
from aeolus.model import um


# Locations of grid lines on maps
XLOCS = np.arange(-180, 181, 90)
YLOCS = np.arange(-90, 91, 30)


def cube_stats_string(cube, sep=" | ", fmt="auto", model=um):
    """Return min, mean and max of an `iris.cube.Cube` as a string."""
    # Compute the stats
    _min = cube.collapsed([model.y, model.x], iris.analysis.MIN)
    _mean = spatial_mean(cube, model=model)
    _max = cube.collapsed([model.y, model.x], iris.analysis.MAX)
    _min = float(_min.data)
    _mean = float(_mean.data)
    _max = float(_max.data)
    # Assemble a string
    txts = []
    if fmt != "auto":
        txts.append(f"min={_min:{fmt}}")
        txts.append(f"mean={_mean:{fmt}}")
        txts.append(f"max={_max:{fmt}}")
    else:
        if (np.log10(abs(_mean)) < 0) or (np.log10(abs(_mean)) > 5):
            txts.append(f"min={_min:.0e}")
            txts.append(f"mean={_mean:.0e}")
            txts.append(f"max={_max:.0e}")
        else:
            txts.append(f"min={np.round(_min):.0f}")
            txts.append(f"mean={np.round(_mean):.0f}")
            txts.append(f"max={np.round(_max):.0f}")
    return sep.join(txts)


def figsave(fig, imgname, stamp=True, **kw_savefig):
    """Save figure and print relative path to it."""
    if stamp:
        fig.suptitle(
            imgname.name,
            x=0.5,
            y=0.05,
            ha="center",
            fontsize="xx-small",
            color="tab:grey",
            alpha=0.5,
        )
    save_dir = imgname.absolute().parent
    save_dir.mkdir(parents=True, exist_ok=True)
    fig.savefig(imgname, **kw_savefig)
    pth = Path.cwd()
    rel_path = None
    pref = ""
    for par in pth.parents:
        pref += ".." + pth.anchor
        try:
            rel_path = f"{pref}{imgname.relative_to(par)}"
            break
        except ValueError:
            pass
    if rel_path is not None:
        print(f"Saved to {rel_path}.{plt.rcParams['savefig.format']}")


def use_style():
    """Load custom matplotlib style sheet."""
    plt.style.use("simple.mplstyle")