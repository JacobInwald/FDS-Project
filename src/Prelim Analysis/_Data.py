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

import math
import numpy as np
import pandas as pd

data = pd.read_csv("Data Sets/IMDB-Movie-Data.csv")
data = data.dropna(0)


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


def create_average_revenue_dict(colname: str, n: int = None) -> dict:
    # Generate set of distinct genres from dataframe
    if (type(list(data[colname])[0]) == type("")):
        all = set(sum([allcol.split(",")
                  for allcol in list(data[colname])], []))
    else:
        all = set([allcol for allcol in list(data[colname])])

    # Generate a dictionary of empty revenues for each genre
    cRevenues = {}
    for c in all:
        cRevenues[c] = []

    for index in data.index:
        # Getting revenue for each movie
        itemRevenue = data["Revenue (Millions)"][index]
        if math.isnan(itemRevenue):  # Skip nan values
            continue

        # Find each genre for the film
        if (type(list(data[colname])[0]) == type("")):
            itemCol = data[colname][index].split(",")
        else:
            itemCol = [data[colname][index]]
        # Adds the film's revenue to each genre
        for col in itemCol:
            cRevenues[col].append(itemRevenue)

    # Delete List for nan values
    delList = []

    # Calculate the average revenue for each genre
    for item in cRevenues:
        if (len(cRevenues[item]) == 0):
            delList.append(item)
            continue
        cRevenues[item] = sum(cRevenues[item]) / len(cRevenues[item])

    for i in delList:
        del cRevenues[i]

    # Sort the revenues from highest to lowest
    return sort_and_crop_dict(cRevenues, n)


def create_average_rating_dict(colname: str, n: int = None) -> dict:
    # Generate set of distinct genres from dataframe
    if (type(list(data[colname])[0]) == type("")):
        all = set(sum([allcol.split(",")
                  for allcol in list(data[colname])], []))
    else:
        all = set([allcol for allcol in list(data[colname])])

    # Generate a dictionary of empty revenues for each genre
    cRatings = {}
    for c in all:
        cRatings[c] = []

    for index in data.index:
        # Getting revenue for each movie
        itemRating = data["Rating"][index]
        if math.isnan(itemRating):  # Skip nan values
            continue

        # Find each genre for the film
        if (type(list(data[colname])[0]) == type("")):
            itemCol = data[colname][index].split(",")
        else:
            itemCol = [data[colname][index]]
        # Adds the film's revenue to each genre
        for col in itemCol:
            cRatings[col].append(itemRating)

    # Delete List for nan values
    delList = []

    # Calculate the average revenue for each genre
    for item in cRatings:
        if (len(cRatings[item]) == 0):
            delList.append(item)
            continue
        cRatings[item] = sum(cRatings[item]) / len(cRatings[item])

    for i in delList:
        del cRatings[i]

    # Sort the revenues from highest to lowest
    return sort_and_crop_dict(cRatings, n)


def save_figure(plot, fileName):
    plot.rcParams.update({
        "font.size": 11,
        "figure.figsize": (6, 6)
    })
    plot.savefig(
        f"Report/Figures/Prelim Analysis/{fileName}.png", bbox_inches="tight")
