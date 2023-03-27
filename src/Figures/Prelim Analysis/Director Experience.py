import matplotlib.pyplot as plt
from _Data import *

director_counts = pd.read_csv("director_counts.csv")
dirRevenues = create_average_revenue_dict("Director")
dirRatings = create_average_rating_dict("Director")
d = {}
dRatings = {}
for director in dirRevenues.keys():
    a = director.strip()
    if len(director_counts[director_counts.name == director]) != 1:
        continue
    num_movies = director_counts[director_counts.name ==
                                 director]['num_films'].values[0]
    if num_movies not in d.keys():
        d[num_movies] = [dirRevenues[director]]
    else:
        d[num_movies].append(dirRevenues[director])

    if num_movies not in dRatings.keys():
        dRatings[num_movies] = [dirRatings[director]]
    else:
        dRatings[num_movies].append(dirRatings[director])

for a in d.keys():
    d[a] = sum(d[a]) / len(d[a])
for b in dRatings.keys():
    dRatings[b] = sum(dRatings[b]) / len(dRatings[b])

fig1, ax1 = plt.subplots(figsize=(10, 10))
ax1.set_title(
    "Director Experience (Number of Appearances) vs Mean Revenue of Movie")
ax1.set_xlabel("Director Experience (Number of Appearances")
ax1.set_ylabel("Mean Revenue of Movie (Millions)")
ax1.scatter(d.keys(), d.values())

save_figure(
    plt, "Director Experience (Number of Appearances) vs Mean Revenue of Movie")

fig1, ax1 = plt.subplots(figsize=(10, 10))
ax1.set_title(
    "Director Experience (Number of Appearances) vs Mean Rating of Movie")
ax1.set_xlabel("Director Experience (Number of Appearances")
ax1.set_ylabel("Mean Rating")
ax1.scatter(dRatings.keys(), dRatings.values())

save_figure(
    plt, "Director Experience (Number of Appearances) vs Mean Rating of Movie")
