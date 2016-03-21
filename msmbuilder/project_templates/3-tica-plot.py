from subprocess import run

import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt

from msmbuilder.dataset2 import load_trajs, load_generic

sns.set_style('ticks')
colors = sns.color_palette()

tica = load_generic('tica.pickl')
meta, ttrajs = load_trajs('ttrajs')
txx = np.concatenate(list(ttrajs.values()))


def plot_heatmap(ax):
    ax.hexbin(txx[:, 0], txx[:, 1],
              cmap=sns.cubehelix_palette(as_cmap=True),
              mincnt=1,
              bins='log'
              )
    ax.set_xlabel("tIC 1", fontsize=16)
    ax.set_ylabel("tIC 2", fontsize=16)


def plot_timescales(ax):
    timestep = meta['step_ps'].unique()
    assert len(timestep) == 1, timestep
    timestep = float(timestep[0])  # ps
    to_us = (
        (1.0 / 1000)  # ps -> ns
        * (1.0 / 1000)  # ns -> us
        * (timestep / 1)  # steps -> ps
    )
    ax.hlines(tica.timescales_ * to_us,
              0, 1,
              color=colors[0])
    ax.set_ylabel(r'Timescales / $\mathrm{\mu s}$', fontsize=18)
    ax.set_xticks([])
    ax.set_xlim((0, 1))


fig, ax = plt.subplots(figsize=(7, 5))
plot_heatmap(ax)
fig.tight_layout()
fig.savefig('tica-heatmap.pdf')
run(['xdg-open', 'tica-heatmap.pdf'])

fig, ax = plt.subplots(figsize=(3, 5))
plot_timescales(ax)
fig.tight_layout()
fig.savefig('tica-timescales.pdf')
run(['xdg-open', 'tica-timescales.pdf'])
