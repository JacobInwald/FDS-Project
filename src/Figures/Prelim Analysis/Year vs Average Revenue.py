import matplotlib.pyplot as plt
import math
from _Data import *

data = pd.read_csv("IMDB-Movie-Data.csv")
data = data.dropna(0)

yearRange = range(min(data.Year), max(data.Year) + 1)

# Create a dictionary with empty revenues for each year
yearRevenues = {}
for year in yearRange:
    yearRevenues[year] = []

for index in data.index:
    # Get the revenue for the movie
    itemRevenue = data["Revenue (Millions)"][index]
    if math.isnan(itemRevenue):  # Skip nan values
        continue

    # Find the movies year and add its revenue
    yearRevenues[data.Year[index]].append(itemRevenue)

# Calculate the average revenue for each year
for item in yearRevenues:
    yearRevenues[item] = sum(yearRevenues[item]) / len(yearRevenues[item])

fig1, ax1 = plt.subplots(figsize=(10, 10))
ax1.grid()
ax1.set_title("Year vs Average Revenue")
ax1.set_xlabel("Year")
ax1.set_ylabel("Revenue (Millions)")
ax1.plot(yearRange, list(yearRevenues.values()))

save_figure(plt, "Year vs Average Revenue")
