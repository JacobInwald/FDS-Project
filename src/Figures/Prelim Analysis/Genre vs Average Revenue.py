import matplotlib.pyplot as plt
from _Data import *

genreRevenues = create_average_revenue_dict("Genre")

fig1, ax1 = plt.subplots(figsize=(10, 10))
ax1.grid(axis="y")
ax1.set_title("Genre vs Average Revenue")
ax1.set_xlabel("Genre")
ax1.set_ylabel("Revenue (Millions)")
ax1.bar(range(len(genreRevenues)), list(genreRevenues.values()),
        tick_label=list(genreRevenues.keys()))
plt.xticks(rotation=90)

save_figure(plt, "Genre vs Average Revenue")
