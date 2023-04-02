import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import math
import _Data as d
from scipy.stats import kstest
from sklearn.preprocessing import normalize
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

data = d.to_latex(data, ignore_col=['Title', 'Genre', 'Year', 'Rank'])

# P-Value testing for normal distribution
p = {}
label = {}
for c in data.columns:
    if c in ['Genre', 'Title', 'Rank', 'Year']:
        continue
    data[c] = (data[c] - np.mean(data[c])) / np.std(data[c])
    s, p[c] = kstest(data[c], 'norm')
    print(p[c])
    label[c] = f'{c} : p = %.3f ∴ X~N(0,1)'%p[c] if p[c] > 0.05 else \
                f'{c} : p <0.05, ∴ X≁N(0,1)'


# Plot data

fig, axs = plt.subplots(ncols=5, nrows=2, figsize=(9,5), sharey=True)
fig.delaxes(axs[1][4])
fig.delaxes(axs[1][3])
fig.delaxes(axs[1][2])
fig.suptitle("Distributions of transformed quantitative data")
fig.supylabel("Frequency Density")
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
        
        lim = np.max(np.abs(data[c]))
        x = np.linspace(-lim, lim, 100)
        pdf = scipy.stats.norm.pdf(x, loc=np.mean(data[c]), scale=np.std(data[c]))
        ax.hist(data[c], 20, label=label[c], color=next(colors)["color"], density=True)
        ax.plot(x, pdf)
        ax.set_xlabel('x')
        ax.set_title(f'Distribution of \n {c}')

        fig.tight_layout()

        i+=1
fig.legend(loc='lower right', fontsize=14)
d.save_figure(plt, "Distribution of Numeric Variables (Transformed)")
for c in data.columns:
    if c in ['Genre', 'Title', 'Rank', 'Year']:
        continue
    data = data[np.abs(stats.zscore(data[c])) < 3]
    
data = d.from_latex(data)

# One hot encoding with Genre
genre_data_clean = pd.DataFrame(columns=['Genre'])

i = 0
for x in range(len(data)):
    r = data.iloc[x]
    for g in r['Genre'].split(','):
        genre_data_clean.loc[i] = [g]
        i+=1

genres = genre_data_clean['Genre'].unique()
for g in genres:
    data[g] = [int(g in s) for s in data['Genre']]
    if sum(data[g]) < 100:
        data = data.drop(g, axis=1)

data.to_csv("Data Sets/normalised_movie_data.csv", index=False)