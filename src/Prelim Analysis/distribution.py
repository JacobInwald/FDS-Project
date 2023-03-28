import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import math
import _Data as d
import scipy

data = pd.read_csv("Data Sets/merged_movie_data.csv")

fig, axs = plt.subplots(ncols=4, nrows=2, figsize=(8,5), sharey=True)
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
            i+= 1
        c = cs[i]
        
        ax.hist(data[c], 20, label=f'{c}', color=next(colors)["color"])
        ax.set_xlabel(f'{c}')
        ax.set_title(f'Distribution of \n {c}')
        fig.tight_layout()

        i+=1

fig.legend(loc='lower right')
d.save_figure(plt, "Distribution of Numeric Variables (No Transformation)")