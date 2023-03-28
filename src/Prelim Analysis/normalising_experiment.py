import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import math
import _Data as d
from scipy.stats import kstest
import scipy
from scipy import stats

data = pd.read_csv("Data Sets/merged_movie_data.csv")
data = data.dropna()

data = data[data['Revenue (Millions)']>0]
print(data.skew().sort_values(ascending=False))
# Transform Data
# Right-Skewed Data
data['Revenue^{1/3}'] = np.cbrt(data['Revenue (Millions)'])
data['Votes^{1/3}'] = np.cbrt(data['Votes'])
data['ln(Runtime)'] = np.log(data['Runtime (Minutes)'])
data['ln(Director Exp)'] = np.log(data['Director Exp.'])
# Left-skewed data
data['Rating^2'] = np.square(data['Rating'])

data = data.drop(['Revenue (Millions)', 'Votes',
           'Runtime (Minutes)', 'Director Exp.',
            'Rating'], axis=1)

# P-Value testing for normal distribution
p = {}
label = {}
for c in data.columns:
    if c in ['Genre', 'Title', 'Rank', 'Year']:
        continue
    data[c] = (data[c] - np.mean(data[c])) / np.std(data[c])
    s, p[c] = kstest(data[c], 'norm')
    print(p[c])
    label[c] = f'${c}$ : p = %.3f ∴ X~N(0,1)'%p[c] if p[c] > 0.05 else \
                f'${c}$ : p <0.05, ∴ X≁N(0,1)'




# Plot data

fig, axs = plt.subplots(ncols=5, nrows=2, figsize=(10,5), sharey=True)
fig.delaxes(axs[1][2])
fig.delaxes(axs[1][3])
fig.delaxes(axs[1][4])
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
        ax.set_title(f'Distribution of \n ${c}$')

        fig.tight_layout()

        i+=1
fig.legend(loc='lower right')
d.save_figure(plt, "Distribution of Numeric Variables (Transformed)")
for c in data.columns:
    if c in ['Genre', 'Title', 'Rank', 'Year']:
        continue
    data = data[np.abs(stats.zscore(data[c])) < 3]
data.to_csv("Data Sets/normalised_movie_data.csv", index=False)