import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import re
import _Data as d

data = pd.read_csv("Data Sets/normalised_movie_data.csv")

fig, axs = plt.subplots(2, 2, figsize=(5, 5), sharex=True)
x = data["Revenue^{1/3}"]
ys = ["Votes^{1/3}", "ln(Runtime)", "Mean Lead Roles Exp.", "Rank"]

for i, ax in enumerate(axs.flat):
    y = data[ys[i]]
    ax.scatter(x, y, s=0.1)
    ax.set_xlabel("$Revenue^{\\frac{1}{3}}$")
    ax.set_ylabel("$" + re.sub(r'(\d)/(\d)',
                  '\\\\frac{\\1}{\\2}', ys[i]) + "$")
    a, b = np.polyfit(x, y, 1)
    r_2 = np.corrcoef(x, y)[0][1]
    ax.plot(
        x,
        a * x + b,
        label=("$r=$%.2f" % (r_2)),
        color="red"
    )
    ax.legend()

fig.tight_layout()

d.save_figure(plt, "Revenue Factors")
