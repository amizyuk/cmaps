import cmaps
import numpy as np
import inspect

import matplotlib.pyplot as plt
import matplotlib
from matplotlib import patheffects
matplotlib.rc('text', usetex=False)


def list_cmaps():
    attributes = inspect.getmembers(cmaps, lambda _: not (inspect.isroutine(_)))
    colors = [_[0] for _ in attributes if
              not (_[0].startswith('__') and _[0].endswith('__'))]
    return colors


if __name__ == '__main__':
    colormaps = list_cmaps()

    gradient = np.linspace(0, 1, 256)
    gradient = np.vstack((gradient, gradient))

    ncols = 8
    nrows = len(colormaps) // ncols + 1
    fig, axs = plt.subplots(figsize=(10, 8),nrows=nrows,ncols=ncols)
    fig.subplots_adjust(top=0.99, bottom=0.01, left=0.01, right=0.99,hspace=0.25,wspace=0.05)
    for (cmap,ax) in zip(colormaps,axs.flat):
        # ax.axis('off')
        ax.imshow(gradient, aspect='auto', cmap=getattr(cmaps, cmap), origin='lower')
        ax.text(.01, 0.5, cmap, va='center', ha='left', fontsize=7,
                transform=ax.transAxes,
                path_effects=[patheffects.withStroke(linewidth=1.1,
                                                        foreground="w")])
    for ax in axs.flat:
        ax.axis('off')
    fig.savefig('colormaps.png', dpi=300)
