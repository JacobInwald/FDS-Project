import matplotlib.pyplot as plt
from _Data import *

# Get directors with the top 100 average revenues
dirRevenues = create_average_revenue_dict("Director", 100)

fig1, ax1 = plt.subplots(figsize=(20, 20))
ax1.grid()
ax1.set_title("Top 100 Director vs Average Revenue")
ax1.set_xlabel("Top 100 Directors")
ax1.set_ylabel("Revenue (Millions)")
ax1.bar(range(len(dirRevenues)), list(dirRevenues.values()),
        tick_label=list(dirRevenues.keys()))
plt.xticks(rotation=90)

save_figure(plt, "Directors vs Average Revenue")
