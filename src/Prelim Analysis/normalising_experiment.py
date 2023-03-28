import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import math
import _Data as d
from scipy.stats import kstest
import scipy

data = pd.read_csv("Data Sets/merged_movie_data.csv")
data = data.dropna()

data = data[data['Revenue (Millions)']>0]
print(data.skew().sort_values(ascending=False))
# Transform Data
# Right-Skewed Data
data['Revenue (Millions)'] = np.cbrt(data['Revenue (Millions)'])
data['Votes'] = np.cbrt(data['Votes'])
data['Runtime (Minutes)'] = np.log(data['Runtime (Minutes)'])
data['Director Exp.'] = np.log(data['Director Exp.'])
# Left-skewed data
data['Rating'] = np.square(data['Rating'])
# P-Value testing for normal distribution
p = {}
label = {}
for c in data.columns:
    if c in ['Genre', 'Title', 'Rank', 'Year']:
        continue
    data[c] = (data[c] - np.mean(data[c])) / np.std(data[c])
    s, p[c] = kstest(data[c], 'norm')
    print(p[c])
    label[c] = f'$H_0$: {c} transform not distributed normally: p = %.3f'%p[c] if p[c] > 0.05 else \
                f'$H_0$: {c} transform not distributed normally: p <0.05'




# Plot data

fig, axs = plt.subplots(ncols=3, nrows=3, figsize=(8,8), sharey=True)
fig.delaxes(axs[2][1])
fig.delaxes(axs[2][2])
fig.suptitle("Distribution of Numeric Variables (Transformed)")
fig.supylabel("Count")
fig.tight_layout()
colors = plt.rcParams["axes.prop_cycle"]()

cs = data.columns
i = 0
for ax_r in axs:
    for ax in ax_r:
        if i == len(cs):
            break
        while cs[i] in ['Genre', 'Title', 'Rank', 'Year']:
            i+= 1
        c = cs[i]
        
        x,loc,scale=  scipy.stats.t.fit(data[c])
        lim = np.max(np.abs(data[c]))
        x = np.linspace(-lim, lim, 100)
        pdf = scipy.stats.norm.pdf(x, loc=loc, scale=scale)
        ax.hist(data[c], 20, label=label[c], color=next(colors)["color"], density=True)
        ax.plot(x, pdf)
        ax.set_xlabel('x')
        ax.set_title(f'Distribution of \n {c}')

        fig.tight_layout()

        i+=1
fig.legend(loc='lower right')
d.save_figure(plt, "Distribution of Numeric Variables (Transformed)")

data = data.rename(columns={'Revenue (Millions)': 'ln(Revenue)',
                             'Votes': 'ln(Votes)',
                             'Director Exp.': 'ln(Director Exp.)'})

data.to_csv("Data Sets/normalised_movie_data.csv", index=False)