import seaborn as sns
from matplotlib import pyplot as plt

sns.set_style('ticks')
colors = sns.color_palette()

from msmbuilder.dataset2 import load
import numpy as np

meta, ktrajs = load("meta.pandas.pickl", "rmsd-ktrajs")
kxx = np.concatenate(list(ktrajs.values()))


def plot_num_per_state(ax):
    num_per_state = np.bincount(kxx)
    ax.scatter(np.arange(len(num_per_state)), num_per_state,
               s=40,
               c=colors[0],
               )
    ax.set_xlabel("State Index", fontsize=16)
    ax.set_ylabel("Count", fontsize=16)


def plot_num_per_state_hist(ax):
    num_per_state = np.bincount(kxx)
    ax.hist(num_per_state)
    ax.set_xlabel("Conformations / State", fontsize=16)
    ax.set_ylabel("Count", fontsize=16)


def plot_dist_histogram(ax):
    # This isn't really possible yet. We need to add something
    # to msmbuilder where we can transform a trajectory into an array
    # of minimum distances
    pass


fig, ax = plt.subplots(figsize=(7, 5))
plot_num_per_state(ax)
fig.tight_layout()
fig.savefig('rmsd-ktrajs-statecount.pdf')

fig, ax = plt.subplots(figsize=(7, 5))
plot_num_per_state_hist(ax)
fig.tight_layout()
fig.savefig('rmsd-ktrajs-statehist.pdf')
