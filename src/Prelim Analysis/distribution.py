import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import math
import _Data as d

data = pd.read_csv("Data Sets/merged_movie_data.csv")

fig, axs = plt.subplots(ncols=3, nrows=3, figsize=(8,8), sharey=True)
fig.delaxes(axs[2][1])
fig.delaxes(axs[2][2])
fig.suptitle("Distribution of Numeric Variables (No Transformation)")
fig.supylabel("Count")
fig.tight_layout()
colors = plt.rcParams["axes.prop_cycle"]()

axs[0][0].hist(data['Revenue (Millions)'], 20 , label='Revenue (Millions)', color=next(colors)["color"])
axs[0][0].set_xlabel('Revenue (Millions)')
axs[0][0].set_title('Distribution of Revenue (Millions)')
fig.tight_layout()
axs[0][1].hist(data['Votes'], 20, label='Votes', color=next(colors)["color"])
axs[0][1].set_xlabel('Votes')
axs[0][1].set_title('Distribution of Votes')
fig.tight_layout()
axs[0][2].hist(data['Metascore'], 20, label='Metascore', color=next(colors)["color"])
axs[0][2].set_xlabel('Metascore')
axs[0][2].set_title('Distribution of Metascore')
fig.tight_layout()
axs[1][0].hist(data['Rating'], 20, label='Rating', color=next(colors)["color"])
axs[1][0].set_xlabel('Rating')
axs[1][0].set_title('Distribution of Rating')
fig.tight_layout()
axs[1][1].hist(data['Runtime (Minutes)'], 20, label='Runtime (Minutes)', color=next(colors)["color"])
axs[1][1].set_xlabel('Runtime (Minutes)')
axs[1][1].set_title('Distribution of Runtime')
fig.tight_layout()
axs[1][2].hist(data['Director Exp.'], 20, label='Director Exp.', color=next(colors)["color"])
axs[1][2].set_xlabel('Experience')
axs[1][2].set_title('Distribution of Director Exp.')
fig.tight_layout()
axs[2][0].hist(data['Mean Lead Roles Exp.'], 20, label='Mean Lead Roles Exp.', color=next(colors)["color"])
axs[2][0].set_xlabel('Experience')
axs[2][0].set_title('Distribution of Mean Lead Roles Exp.')
fig.tight_layout()
fig.legend(loc='lower right')
d.save_figure(plt, "Distribution of Numeric Variables (No Transformation)")