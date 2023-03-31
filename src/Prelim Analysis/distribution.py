import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import _Data as d

data = pd.read_csv("Data Sets/merged_movie_data.csv")

fig, axs = plt.subplots(ncols=4, nrows=2, figsize=(8, 5), sharey=True)
fig.delaxes(axs[1][3])
fig.suptitle("Distribution of Numeric Variables (No Transformation)")
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

fig1, axs1 = plt.subplots(1, 2, figsize=(10, 5), sharey=True)
fig1.suptitle("Distributions of Votes and Rank")
fig1.supylabel("Count")
axs1[0].hist(data["Votes"], 20, label="Votes", color="lightsalmon")
axs1[0].set_xlabel("Votes")
axs1[0].set_title("Distribution of Votes")
axs1[1].hist(data["Rank"], 20, label="Rank", color="lightsalmon")
axs1[1].set_xlabel("Rank")
axs1[1].set_title("Distribution of Rank")
d.save_figure(plt, "Distributions of Votes and Rank")
