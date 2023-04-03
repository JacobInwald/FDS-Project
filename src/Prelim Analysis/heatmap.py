import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import _Data as d

data = pd.read_csv("Data Sets/normalised_movie_data.csv")
data = data.dropna()
data = data.drop(["Genre", "Title", "Action", "Adventure", "Sci-Fi",
                 "Thriller", "Comedy", "Drama", "Romance", "Crime"], axis=1)
data = d.to_latex(data)
fig = plt.figure(figsize=(5, 5))
heatmap = sns.heatmap(data.corr(), fmt=".3f", vmin=-1, vmax=1,
                      annot=True, cmap="BrBG", annot_kws={"size": 6})
heatmap.set_title("Normalised Correlation Heatmap")
heatmap.set_xticklabels(heatmap.get_xticklabels(),
                        rotation=45,
                        ha="right")
heatmap.set_yticklabels(heatmap.get_yticklabels(),
                        rotation=45,
                        va="top")
d.save_figure(plt, "Normalised Correlation Heatmap")
