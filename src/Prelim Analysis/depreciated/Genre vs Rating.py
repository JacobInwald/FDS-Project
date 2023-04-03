import matplotlib.pyplot as plt
from _Data import *
import seaborn as sns

genre_data = pd.read_csv("Data Sets/normalised_movie_data.csv")

genre_data_clean = pd.DataFrame(columns=['Genre', 'Rating^2', 'Revenue^{1/3}', 'Metascore'])

i = 0
for x in range(len(genre_data)):
    r = genre_data.iloc[x]
    for g in r['Genre'].split(','):
        genre_data_clean.loc[i] = [g, r['Rating^2'], r['Revenue^{1/3}'], r['Metascore']]
        i+=1

genre_data = genre_data_clean
order_by_mean = {c:np.median(genre_data[genre_data.Genre == c]['Rating^2'])for c in genre_data['Genre'].unique()}
order =  [k for k, v in sorted(order_by_mean.items(), key=lambda item: item[1])]
fig1, ax1 = plt.subplots(figsize=(8, 8))
ax1.grid(axis="y")
ax1.set_title("Genre vs $Rating^2$")
plot = sns.boxplot(data=pd.concat([genre_data, genre_data.assign(type='both')]),
            x='Genre', y='Rating^2',
              order=order,
              notch=True,
              color='lightsalmon',
              showmeans=True)
ax1.set_xlabel("Genre")
ax1.set_ylabel("$Rating^2$")
plt.xticks(rotation=45, ha='right')
n = len(order)
i = 0
for c in order:
    rev_c = genre_data[genre_data.Genre ==c]['Rating^2']
    N = len(rev_c)
    rev_clq = np.quantile(rev_c, 0.25)
    rev_cuq = np.quantile(rev_c, 0.75)
    rev_cm = np.median(rev_c)
    print(N)
    plt.text(i,
             rev_clq-0.16 if i % 2 == 0 else rev_cuq+0.05, 
             f'N={N}',
             ha='center')
    i+=1

save_figure(plt, "Genre vs Rating^2")
