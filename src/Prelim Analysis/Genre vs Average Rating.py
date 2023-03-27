import matplotlib.pyplot as plt
from _Data import *

genreRating = create_average_rating_dict("Genre")

fig1, ax1 = plt.subplots(figsize=(10, 10))
ax1.grid(axis="y")
ax1.set_title("Genre vs Average Rating")
ax1.set_xlabel("Genre")
ax1.set_ylabel("Rating")
ax1.boxplot(range(len(genreRating)), list(genreRating.values()),
        tick_label=list(genreRating.keys()))
ax1.set_ylim(5.5)
plt.xticks(rotation=90)

save_figure(plt, "Genre vs Average Rating")
