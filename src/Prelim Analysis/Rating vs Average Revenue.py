import matplotlib.pyplot as plt
from _Data import *

rateRevenues = create_average_revenue_dict("Rating")

fig1, ax1 = plt.subplots(figsize=(10, 10))
ax1.grid()
ax1.set_title("Ratings vs Average Revenue")
ax1.set_xlabel("Movie Rating")
ax1.set_ylabel("Average Revenue (Millions)")
ax1.scatter(list(rateRevenues.keys()), list(rateRevenues.values()), s=5)

save_figure(plt, "Rating vs Average Revenue")
