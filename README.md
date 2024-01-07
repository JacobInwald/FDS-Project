# FDS Project
A team-project for Foundations of Data Science, for which we achieved a 2:1 grade.
This was an investigation into movie ratings given on the movie site IMDb.com.
We aimed to answer the question of whether critics where better than the general public at predicting film success. 

## Abstract
This report analyses the impact of critics on the success of movies within the ﬁlm industry. 
We carried out this analysis using data from IMDb which provided statistics on one thousand movies released between 2006 and 2016. 
A least squares multiple regression model was used to determine which factors of a movie can be used to predict their box ofﬁce success, while another least squares multiple regression model was used to determine if critics were able to predict success based on a metric which combines the revenue and viewer rating of that movie.
We found that a movie’s revenue is correlated by the number of votes it has on IMDb, its runtime and the experience of actors in its leading roles. 
We further found that critics ratings cannot be used to predict the box ofﬁce success of a movie, but can predict how the public
will recieve it, even though they tend to be less lenient than the general public. 
Moreover, we discovered that actor experience is a better prediction of box ofﬁce success than director experience

## Dependencies:
We use the following python libraries to perform analysis, so make sure you have these installed before running any code:
- scikit
- scipy
- statsmodels
- yellowbrick
- numpy
- matplotlib
- pandas

## Data
For out analysis we use two datasets, to download use the links and follow instructions:
- IMDb data: 
    - Download: https://www.kaggle.com/datasets/gan2gan/1000-imdb-movies-20062016
    - To parse use the create_merged_dataset function in the _Data.py library
- TMD data:
    - Dowload: https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset?resource=download
    - We only used the credits CSV file
    - To parse use credits_analysis.py
