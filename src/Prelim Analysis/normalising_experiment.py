import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import math
import _Data as d
from scipy.stats import shapiro

data = pd.read_csv("Data Sets/merged_movie_data.csv")
data = data.dropna()
# Normalise data
data = data[data['Revenue (Millions)']>0]
data['Revenue (Millions)'] = np.log(data['Revenue (Millions)'])
data['Votes'] = np.log(data['Votes'])
data['Director Exp.'] = np.log(data['Director Exp.'])
stat = {}
p = {}
label = {}
for c in data.columns:
    if c in ['Genre', 'Title', 'Rank', 'Year']:
        continue
    data[c] = (data[c] - np.mean(data[c])) / np.std(data[c])
    stat[c], p[c]  = shapiro(data[c])
    label[c] = f'{c} transform distributed normally: p = %.3f'%p[c] if p[c] > 0.01 else \
                f'{c} transform distributed normally: p <0.01'
print(stat, p)
fig, axs = plt.subplots(ncols=3, nrows=3, figsize=(8,8), sharey=True)
fig.delaxes(axs[2][1])
fig.delaxes(axs[2][2])
fig.suptitle("Distribution of Numeric Variables (Transformed)")
fig.supylabel("Count")
fig.tight_layout()
colors = plt.rcParams["axes.prop_cycle"]()

axs[0][0].hist(data['Revenue (Millions)'], 20 , label=label['Revenue (Millions)'], color=next(colors)["color"])
axs[0][0].set_xlabel('x')
axs[0][0].set_title('Distribution of Revenue (Millions)')
fig.tight_layout()
axs[0][1].hist(data['Votes'], 20, label=label['Votes'], color=next(colors)["color"])
axs[0][1].set_xlabel('x')
axs[0][1].set_title('Distribution of Votes')
fig.tight_layout()
axs[0][2].hist(data['Metascore'], 20, label=label['Metascore'], color=next(colors)["color"])
axs[0][2].set_xlabel('x')
axs[0][2].set_title('Distribution of Metascore')
fig.tight_layout()
axs[1][0].hist(data['Rating'], 20, label=label['Rating'], color=next(colors)["color"])
axs[1][0].set_xlabel('x')
axs[1][0].set_title('Distribution of Rating')
fig.tight_layout()
axs[1][1].hist(data['Runtime (Minutes)'], 20, label=label['Runtime (Minutes)'], color=next(colors)["color"])
axs[1][1].set_xlabel('x')
axs[1][1].set_title('Distribution of Runtime')
fig.tight_layout()
axs[1][2].hist(data['Director Exp.'], 20, label=label['Director Exp.'], color=next(colors)["color"])
axs[1][2].set_xlabel('x')
axs[1][2].set_title('Distribution of Director Exp.')
fig.tight_layout()
axs[2][0].hist(data['Mean Lead Roles Exp.'], 20, label=label['Mean Lead Roles Exp.'], color=next(colors)["color"])
axs[2][0].set_xlabel('x')
axs[2][0].set_title('Distribution of Mean Lead Roles Exp.')
fig.tight_layout()
fig.legend(loc='lower right')
fig.legend(loc='lower right')
d.save_figure(plt, "Distribution of Numeric Variables (Transformed)")


data.to_csv("Data Sets/normalised_movie_data.csv", index=False)