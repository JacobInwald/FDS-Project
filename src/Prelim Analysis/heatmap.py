import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import math
import _Data as d

data = pd.read_csv("Data Sets/numeric_IMDB_movie_data.csv")
plt.figure(figsize=(8,8))
heatmap = sns.heatmap(data.corr(), vmin=-1, vmax=1, annot=True, cmap='BrBG')
heatmap.set_title('Correlation Heatmap')
heatmap.set_xticklabels(heatmap.get_xticklabels(), 
                        rotation = 45,
                        ha = 'right')
heatmap.set_yticklabels(heatmap.get_yticklabels(), 
                        rotation = 45,
                        va = 'top')

d.save_figure(plt, 'Correlation Heatmap')