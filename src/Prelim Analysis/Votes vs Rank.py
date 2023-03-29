import matplotlib.pyplot as plt
from _Data import *
import seaborn as sns


data = pd.read_csv("Data Sets/merged_movie_data.csv")
data = data.dropna()

fig1, ax1 = plt.subplots(figsize=(8, 8))
ax1.grid(axis="y")
ax1.set_title("Genre vs Rating^2")
ax1.set_xlabel("Genre")
ax1.set_ylabel("Rating^2")
ax1.scatter(data['Rank'], data['Votes'])
plt.xticks(rotation=45, ha='right')

save_figure(plt, "Votes transform vs Rank")