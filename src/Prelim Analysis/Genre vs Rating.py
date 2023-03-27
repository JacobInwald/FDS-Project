import matplotlib.pyplot as plt
from _Data import *
import seaborn as sns

genreRating = create_average_rating_dict("Genre")

genre_data = pd.read_csv("Data Sets/IMDB-Movie-Data.csv")
genre_data = genre_data.drop(['Title', 'Description', 'Director', 'Actors', 'Year', 'Runtime (Minutes)', 'Votes'], axis=1)

genre_data_clean = pd.DataFrame(columns=['Genre', 'Rating', 'Revenue (Millions)', 'Metascore'])
i = 0
for x in range(len(genre_data)):
    r = genre_data.iloc[x]
    for g in r['Genre'].split(','):
        genre_data_clean.loc[i] = [g, r['Rating'], r['Revenue (Millions)'], r['Metascore']]
        i+=1

genre_data = genre_data_clean
print(genre_data[genre_data.Genre == 'Musical'])
fig1, ax1 = plt.subplots(figsize=(10, 10))
ax1.grid(axis="y")
ax1.set_title("Genre vs Rating")
ax1.set_xlabel("Genre")
ax1.set_ylabel("Rating")
plot = sns.boxplot(data=pd.concat([genre_data, genre_data.assign(type='both')]),
            x='Genre', y='Rating',
              order=genre_data['Genre'].unique(),
              notch=True,
              color='lightsalmon')
plt.xticks(rotation=45, ha='right')
save_figure(plt, "Genre vs Rating")
