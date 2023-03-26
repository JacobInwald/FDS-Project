import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import math

data_unrefined = pd.read_csv('credits.csv')
actors = []
directors = []
n = len(data_unrefined)

# parse the actors out
for i in range(n):
    a_strings = data_unrefined['cast'].iloc[i].split(',')
    for s in a_strings:
        if 'name' in s:
            a = s.split(': ')[1]
            a = a[1:-1]
            actors.append(a)
actor_count = {}
for a in actors:
    if a in actor_count.keys():
        actor_count[a] += 1
    else:
        actor_count[a] = 1

actor_count = pd.DataFrame.from_dict(actor_count, orient='index')
actor_count.to_csv("actor_counts.csv")


for i in range(n):
    d_strings = data_unrefined['crew'].iloc[i].split(', {')
    
    for s in d_strings:
        if "Director'" in s:
            s = s.split(',')
            for x in s:
                #print(x)
                if 'name' in x:
                    d = x.split(': ')[1]
                    d = d[1:-1]
                    directors.append(d)

director_count = {}
for d in directors:
    if d in director_count.keys():
        director_count[d] += 1
    else:
        director_count[d] = 1

director_count = pd.DataFrame.from_dict(director_count, orient='index')
director_count.to_csv("director_counts.csv")