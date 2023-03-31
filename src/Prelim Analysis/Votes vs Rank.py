import matplotlib.pyplot as plt
from _Data import *

data = pd.read_csv("Data Sets/merged_movie_data.csv")
data = data.dropna()

fig1, ax1 = plt.subplots(figsize=(8, 8))
ax1.grid(axis="y")
ax1.set_title("Votes vs Rank")
ax1.set_xlabel("Rank")
ax1.set_ylabel("Votes")
ax1.scatter(data['Rank'], data['Votes'])
plt.xticks(rotation=45, ha='right')

save_figure(plt, "Votes vs Rank")

data = pd.read_csv("Data Sets/normalised_movie_data.csv")
data = data.dropna()

fig1, ax1 = plt.subplots(figsize=(8, 8))
ax1.grid(axis="y")
ax1.set_title("Normalised Votes vs Rank")
ax1.set_xlabel("Rank")
ax1.set_ylabel("$Votes^{\\frac{1}{3}}$")
ax1.scatter(data['Rank'], data['Votes^{1/3}'])
plt.xticks(rotation=45, ha='right')

save_figure(plt, "Normalised Votes vs Rank")
