import matplotlib.pyplot as plt
from _Data import *

data = pd.read_csv("Data Sets/normalised_movie_data.csv")
data = data.dropna()
metric = np.add(data['Rating^2'], data['Revenue^{1/3}']) / 2
data['Success'] = metric
fig1, ax1 = plt.subplots(figsize=(8, 8))
ax1.grid(axis="y")
ax1.set_title("Metric vs Metascore")
ax1.set_xlabel("Metascore")
ax1.set_ylabel("Success")
print(data['Metascore'].corr(metric))
ax1.scatter(data['Metascore'], metric)
plt.xticks(rotation=45, ha='right')
save_figure(plt, "Metric vs Metascore")
