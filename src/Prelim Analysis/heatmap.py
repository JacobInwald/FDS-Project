import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import math
import _Data as d

data = pd.read_csv("Data Sets/merged_movie_data.csv")
data = data.dropna()
data = data.drop(['Genre', 'Title'], axis=1)

fig = plt.figure(figsize=(8,8))
heatmap = sns.heatmap(data.corr(), vmin=-1, vmax=1, annot=True, cmap='BrBG')
heatmap.set_title('Correlation Heatmap')
heatmap.set_xticklabels(heatmap.get_xticklabels(), 
                        rotation = 45,
                        ha = 'right')
heatmap.set_yticklabels(heatmap.get_yticklabels(), 
                        rotation = 45,
                        va = 'top')

d.save_figure(plt, 'Correlation Heatmap')

data = pd.read_csv("Data Sets/normalised_movie_data.csv")
data = data.dropna()
data = data.drop(['Genre', 'Title'], axis=1)
data = d.to_latex(data)
fig = plt.figure(figsize=(5,5))
heatmap = sns.heatmap(data.corr(), vmin=-1, vmax=1, annot=True, cmap='BrBG', annot_kws={"size": 6})
heatmap.set_title('Normalised Correlation Heatmap')
heatmap.set_xticklabels(heatmap.get_xticklabels(), 
                        rotation = 45,
                        ha = 'right')
heatmap.set_yticklabels(heatmap.get_yticklabels(), 
                        rotation = 45,
                        va = 'top')
d.save_figure(plt, 'Normalised Correlation Heatmap')