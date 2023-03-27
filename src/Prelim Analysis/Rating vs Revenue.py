import matplotlib.pyplot as plt
from _Data import *

fig1, ax1 = plt.subplots(figsize=(10, 10))
ax1.grid()
ax1.set_title("Ratings vs Revenue")
ax1.set_xlabel("Movie Rating")
ax1.set_ylabel("Revenue (Millions)")
ax1.scatter(data["Rating"], data["Revenue (Millions)"], s=5)

save_figure(plt, "Rating vs Revenue")
