import matplotlib.pyplot as plt
from _Data import *

# Get Actors with the top 100 average revenues
actRevenues = create_average_revenue_dict("Actors", 100)

fig1, ax1 = plt.subplots(figsize=(20, 20))
ax1.grid()
ax1.set_title("Top 100 Actor vs Average Revenue")
ax1.set_xlabel("Top 100 Actors")
ax1.set_ylabel("Revenue (Millions)")
ax1.bar(range(len(actRevenues)), list(actRevenues.values()),
        tick_label=list(actRevenues.keys()))
plt.xticks(rotation=90)

save_figure(plt, "Actors vs Average Revenue")
