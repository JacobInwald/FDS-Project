import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import _Data as d

data = pd.read_csv("Data Sets/merged_movie_data.csv")

fig, axs = plt.subplots(ncols=2, nrows=4, figsize=(4.5, 9), sharey=True)
fig.delaxes(axs[3][1])
fig.suptitle("Distributions of quantitative data")
fig.supylabel("Count")
fig.tight_layout()
colors = plt.rcParams["axes.prop_cycle"]()
cs = data.columns
i = 0
print(cs)
for ax_r in axs:
    for ax in ax_r:
        if i == len(cs):
            break
        while cs[i] in ['Genre', 'Title', 'Rank', 'Year']:
            i += 1
        c = cs[i]

        ax.hist(data[c], 20, label=f'{c}', color='lightsalmon')
        ax.set_xlabel(f'{c}')
        ax.set_title(f'Distribution of \n {c}')
        fig.tight_layout()

        i += 1

d.save_figure(plt, "Distribution of Numeric Variables (No Transformation)")

fig, axs = plt.subplots(ncols=2, nrows=1, figsize=(6, 3), sharey=True)
fig.suptitle("Distributions of Rank and Votes")
fig.supylabel("Count")
fig.tight_layout()
cs = data.columns
i = 0
for ax in axs:
    if i == len(cs):
        break
    while cs[i] not in ['Rank', 'Votes']:
        i += 1
    c = cs[i]

    ax.hist(data[c], 20, label=f'{c}', color='lightsalmon')
    ax.set_xlabel(f'{c}')
    ax.set_title(f'Distribution of \n {c}')
    fig.tight_layout()

    i += 1

d.save_figure(plt, "Distributions of Votes and Rank")
