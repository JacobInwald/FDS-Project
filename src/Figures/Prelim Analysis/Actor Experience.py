import matplotlib.pyplot as plt
from _Data import *

actor_counts = pd.read_csv("actor_counts.csv")
actRevenues = create_average_revenue_dict("Actors")
actRatings = create_average_rating_dict("Actors")
d = {}
dRatings = {}

for actor in actRevenues.keys():
    a = actor.strip()
    if len(actor_counts[actor_counts.name == actor]) != 1:
        continue
    num_movies = actor_counts[actor_counts.name ==
                              actor]['num_films'].values[0]
    if num_movies not in d.keys():
        d[num_movies] = [actRevenues[actor]]
    else:
        d[num_movies].append(actRevenues[actor])

    if num_movies not in dRatings.keys():
        dRatings[num_movies] = [actRatings[actor]]
    else:
        dRatings[num_movies].append(actRatings[actor])

for a in d.keys():
    d[a] = sum(d[a]) / len(d[a])
for b in dRatings.keys():
    dRatings[b] = sum(dRatings[b]) / len(dRatings[b])
fig1, ax1 = plt.subplots(figsize=(10, 10))
ax1.set_title(
    "Actor Experience (Number of Appearances) vs Mean Revenue of Movie")
ax1.set_xlabel("Actor Experience (Number of Appearances")
ax1.set_ylabel("Mean Revenue of Movie (Millions)")
ax1.scatter(d.keys(), d.values())

save_figure(plt,
            "Actor Experience (Number of Appearances) vs Mean Revenue of Movie")

fig1, ax1 = plt.subplots(figsize=(10, 10))
ax1.set_title(
    "Actor Experience (Number of Appearances) vs Mean Rating of Movie")
ax1.set_xlabel("Actor Experience (Number of Appearances")
ax1.set_ylabel("Mean Rating of Movie")
ax1.scatter(dRatings.keys(), dRatings.values())

save_figure(plt,
            "Actor Experience (Number of Appearances) vs Mean Rating of Movie")
