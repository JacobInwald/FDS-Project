# FDS Project
# Dependencies:
We use the following python libraries to perform analysis, so make sure you have these installed before running any code:
- scikit
- scipy
- statsmodels
- yellowbrick
- numpy
- matplotlib
- pandas
# Data
For out analysis we use two datasets, to download use the links and follow instructions:
- IMDb data: 
    - Download: https://www.kaggle.com/datasets/gan2gan/1000-imdb-movies-20062016
    - To parse use the create_merged_dataset function in the _Data.py library
- TMD data:
    - Dowload: https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset?resource=download
    - We only used the credits CSV file
    - To parse use credits_analysis.py