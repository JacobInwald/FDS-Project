import matplotlib.pyplot as plt
import math
from _Data import *

# Get the range of runtimes in the dataframe
runtimeRange = range(min(data["Runtime (Minutes)"]),
                     max(data["Runtime (Minutes)"]) + 1)

# Create a dictionary with empty revenues for each year
runtimeRevenues = {}
for runtime in runtimeRange:
    runtimeRevenues[runtime] = []

for index in data.index:
    # Get the revenue for the movie
    itemRevenue = data["Revenue (Millions)"][index]
    if math.isnan(itemRevenue):  # Skip nan values
        continue

    # Find the movies runtime and add its revenue
    runtimeRevenues[data["Runtime (Minutes)"][index]].append(itemRevenue)

delList = []

# Calculate the average revenue for each year
for item in runtimeRevenues:
    if len(runtimeRevenues[item]) == 0:
        delList.append(item)
        continue
    runtimeRevenues[item] = sum(
        runtimeRevenues[item]) / len(runtimeRevenues[item])

# Remove runtimes with no data
for item in delList:
    del runtimeRevenues[item]

fig1, ax1 = plt.subplots(figsize=(10, 10))
ax1.grid()
ax1.set_title("Runtime vs Average Revenue")
ax1.set_xlabel("Runtime (Minutes)")
ax1.set_ylabel("Revenue (Millions)")
ax1.scatter(data["Runtime (Minutes)"], data["Revenue (Millions)"], s=5)

save_figure(plt, "Runtime vs Average Revenue")
