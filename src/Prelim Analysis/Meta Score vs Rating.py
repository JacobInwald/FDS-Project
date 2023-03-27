import matplotlib.pyplot as plt
from _Data import *

fig1, ax1 = plt.subplots(figsize=(10, 10))
ax1.grid()
ax1.set_title("Meta Score vs Rating")
ax1.set_ylabel("Meta Score")
ax1.set_xlabel("Rating")
ax1.scatter(data["Rating"], data["Metascore"], s=5)
x = data["Rating"]
y = data["Metascore"]
a, b = np.polyfit(x, y, 1)
r_2 = np.corrcoef(x, y)[0][1]
ax1.plot(x, a * x + b, label=("$R^2=$%.2f: y = %.2f*x + %.2f" % (r_2, a, b)))
ax1.legend()

save_figure(plt, "Meta Score vs Rating")
