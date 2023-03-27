import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import math

def convert_to_numeric():
    data_raw = pd.read_csv("IMDB-Movie-Data.csv")
    data_raw = data_raw.dropna(0)
    data_raw = data_raw.drop('Description', axis=1)
    data_raw = data_raw.drop('Title', axis=1)
    data_raw = data_raw.drop('Genre', axis=1)
    print(data_raw.columns)

    director_count = pd.read_csv("director_counts.csv")
    actor_count = pd.read_csv("actor_counts.csv")

    data_raw['Director Experience'] = [director_count[director_count.name == d.strip()]['num_films'].values[0] 
                                    if len(director_count[director_count.name == d.strip()]) >= 1
                                        else None 
                                        for d in data_raw['Director']]
    data_raw = data_raw.drop('Director', axis=1)

    data_raw['Mean Lead Roles Experience'] = [sum([actor_count[actor_count.name == act]['num_films'].values[0] 
                                    if len(actor_count[actor_count.name == act]) >= 1
                                        else 0
                                        for act in a.split(', ')]) / len(a.split(', ')) for a in data_raw['Actors']]
    data_raw = data_raw.drop('Actors', axis=1)
    print("processing_done")
    data_raw.to_csv("numeric_IMDB_movie_data.csv")

data = pd.read_csv("numeric_IMDB_movie_data.csv").set_index("Rank")
plt.figure(figsize=(10,10))
heatmap = sns.heatmap(data.corr(), vmin=-1, vmax=1, annot=True, cmap='BrBG')
heatmap.set_title('Correlations Heatmap')
plt.show()
