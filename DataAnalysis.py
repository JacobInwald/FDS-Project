# Leading streaming services, such as Netflix, Amazon Prime and Disney Plus,
# use recommendation systems to provide suggestions to users of films that they
# predict they will enjoy.

# This is an especially difficult task in the case of movies that haven’t been
# seen by a wide audience yet:

# ? What can we say about the success of a movie before it is released?

# ? Are there certain companies that have found a consistent formula?

# * We would like you to explore what makes a movie popular and/or successful.

# ? From the data available, what factors predict the revenue of a film and how
# ? well (if at all) can we predict the revenue of a film?

# ? Additionally, given that major films costing over millions to produce can
# ? still ‘flop’ in the box office, can we predict which films will be highly
# ? rated by users, regardless of if they are a commercial success?

# * We would also like you to visualise the distribution of ranked position and
# * number of votes, and comment on the relationship between them.

# The extra questions should extend the basic findings.
# Examples of questions are:
# ? Does the year of release or current trends in genre have any influence on a
# ? movie’s preceding popularity rating or revenue?

# ? You could also choose to take a ‘deep-dive’ into the work of one (or a
# ? collection of) actor(s) / actress(es) or director(s) and examine trends
# ? across their apparent most popular movies.

# ? Any other questions that arise as you explore the data.

import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import math


# HELPER FUNCTIONS

def sort_and_crop_dict(d: dict, n: int = None) -> dict:
    """
    Returns a sorted high->low dictionary which has been cropped to length n
        param d: Dictionary to sort and crop
        param n: Length of resultant dictionary
    """
    if (n == None or n <= 0 or n > len(d)):
        n = len(d)
    keys = list(d.keys())
    values = list(d.values())
    sorted_value_index = np.argsort(values)[::-1]
    sorted_dict = {keys[i]: values[i] for i in sorted_value_index[0:n]}
    return sorted_dict


# Main Code

matplotlib.rcParams["figure.dpi"] = 150

data = pd.read_csv("IMDB-Movie-Data.csv")
# Rank, Title, Genre, Description, Director, Actors, Year, Runtime (Minutes),
# Rating, Votes, Revenue (Millions), Metascore


# Genre vs Average Revenue
allGenres = set(sum([genList.split(",") for genList in list(data.Genre)], []))
genreRevenues = {}
for genre in allGenres:
    genreRevenues[genre] = []
for index in data.index:
    itemRevenue = data["Revenue (Millions)"][index]
    if math.isnan(itemRevenue):
        continue
    itemGenres = data.Genre[index].split(",")
    for genre in itemGenres:
        genreRevenues[genre].append(itemRevenue)
for item in genreRevenues:
    genreRevenues[item] = sum(genreRevenues[item]) / len(genreRevenues[item])


genreRevenues = sort_and_crop_dict(genreRevenues)

fig1, ax1 = plt.subplots(figsize=(20, 20))
ax1.grid()
ax1.set_title("Genre vs Average Revenue")
ax1.set_xlabel("Genre")
ax1.set_ylabel("Revenue (Millions)")
ax1.bar(range(len(genreRevenues)), list(genreRevenues.values()),
        tick_label=list(genreRevenues.keys()))
plt.savefig("Figures/Genre vs Average Revenue.png")



# ? Directors vs Average Revenue

# Generate set of distinct directors from dataframe
allDirectors = set(sum([dirList.split(",") for dirList in list(data.Director)], []))

# Generate a dictionary of empty revenues for each director
dirRevenues = {}
for dir in allDirectors:
    dirRevenues[dir] = []


for index in data.index:
    # Getting revenue for each movie
    itemRevenue = data["Revenue (Millions)"][index]
    if math.isnan(itemRevenue): # Skip nan values
        continue

    # Finds the director for the film and 
    # adds the revenue of that film to the dictionary
    dir = data.Director[index]
    dirRevenues[dir].append(itemRevenue)


delList = []

# Average the revenue for each film
for item in dirRevenues:
    if (len(dirRevenues[item]) == 0):
        delList.append(item)
        continue
    dirRevenues[item] = sum(dirRevenues[item]) / len(dirRevenues[item])

# Remove directors with no data
for item in delList:
    del dirRevenues[item]


# Get Directors with the top 100 average revenues
dirRevenues = sort_and_crop_dict(dirRevenues, 100)

fig1, ax1 = plt.subplots(figsize=(20, 20))
ax1.grid()
ax1.set_title("Top 100 Director vs Average Revenue")
ax1.set_xlabel("Top 100 Directors")
ax1.set_ylabel("Revenue (Millions)")
ax1.bar(range(len(dirRevenues)), list(dirRevenues.values()),
        tick_label=list(dirRevenues.keys()))
plt.xticks(rotation=90)
plt.savefig("Figures/Directors vs Average Revenue.png")

# ? Actors vs Average Revenue

# Generate set of distinct actors from dataframe
allActors = set(sum([actList.split(",") for actList in list(data.Actors)], []))

# Generate a dictionary of empty revenues for each actor
actRevenues = {}
for act in allActors:
    actRevenues[act] = []


for index in data.index:
    # Getting revenue for each movie
    itemRevenue = data["Revenue (Millions)"][index]
    if math.isnan(itemRevenue): # Skip nan values
        continue

    itemActors = data.Actors[index].split(",")
    for act in itemActors:
        actRevenues[act].append(itemRevenue)

delList = []

# Average the revenue for each film
for item in actRevenues:
    if (len(actRevenues[item]) == 0):
        delList.append(item)
        continue
    actRevenues[item] = sum(actRevenues[item]) / len(actRevenues[item])

# Remove actors with no data
for item in delList:
    del actRevenues[item]


# Get Actors with the top 100 average revenues
actRevenues = sort_and_crop_dict(actRevenues, 100)

fig1, ax1 = plt.subplots(figsize=(20, 20))
ax1.grid()
ax1.set_title("Top 100 Actor vs Average Revenue")
ax1.set_xlabel("Top 100 Actors")
ax1.set_ylabel("Revenue (Millions)")
ax1.bar(range(len(actRevenues)), list(actRevenues.values()),
        tick_label=list(actRevenues.keys()))
plt.xticks(rotation=90)
plt.savefig("Figures/Actors vs Average Revenue.png")


# ? Year vs Average Revenue
yearRange = range(min(data.Year), max(data.Year) + 1)
yearRevenues = {}
for year in yearRange:
    yearRevenues[year] = []
for index in data.index:
    itemRevenue = data["Revenue (Millions)"][index]
    if math.isnan(itemRevenue):
        continue
    yearRevenues[data.Year[index]].append(itemRevenue)
for item in yearRevenues:
    if len(yearRevenues[item]) == 0:
        print(item)
        del yearRevenues[item]
    yearRevenues[item] = sum(yearRevenues[item]) / len(yearRevenues[item])

fig4, ax4 = plt.subplots(figsize=(20, 20))
ax4.grid()
ax4.set_title("Year vs Average Revenue")
ax4.set_xlabel("Year")
ax4.set_ylabel("Revenue (Millions)")
ax4.plot(yearRange, list(yearRevenues.values()))
plt.savefig("Figures/Year vs Average Revenue.png")

# Runtime vs Average Revenue

# ? Rating vs Average Revenue


# Scatter plot



# Generate set of the distinct ratings from dataframe
allRatings = set(data.Rating)

# Generate a dictionary of empty revenues for each rating
rateRevenues = {}
for rate in allRatings:
    rateRevenues[rate] = []

for index in data.index:
    # Getting revenue for each movie
    itemRevenue = data["Revenue (Millions)"][index]
    if math.isnan(itemRevenue): # Skip nan values
        continue

    rate = data.Rating[index]
    rateRevenues[rate].append(itemRevenue)

delList = []

# Average the revenue for each film
for item in rateRevenues:
    if (len(rateRevenues[item]) == 0):
        delList.append(item)
        continue
    rateRevenues[item] = sum(rateRevenues[item]) / len(rateRevenues[item])

# Remove ratings with no data
for item in delList:
    del rateRevenues[item]


# sort ratings
rateRevenues = sort_and_crop_dict(rateRevenues)

fig1, ax1 = plt.subplots(figsize=(20, 20))
ax1.grid()
ax1.set_title("Ratings vs Average Revenue")
ax1.set_xlabel("Movie Rating")
ax1.set_ylabel("Average Revenue (Millions)")
ax1.scatter(list(rateRevenues.keys()), list(rateRevenues.values()))

plt.savefig("Figures/Rating vs Average Revenue.png")

fig1, ax1 = plt.subplots(figsize=(20, 20))
ax1.grid()
ax1.set_title("Ratings vs Revenue")
ax1.set_xlabel("Movie Rating")
ax1.set_ylabel("Revenue (Millions)")
ax1.scatter(data["Rating"], data["Revenue (Millions)"])

plt.savefig("Figures/Rating vs Revenue.png")
