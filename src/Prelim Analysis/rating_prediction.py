import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.regression.linear_model import OLS
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from yellowbrick.regressor import residuals_plot
from _Data import *

# reading the csv file
data = pd.read_csv("Data Sets/normalised_movie_data.csv")
data = data.drop(['Genre', 'Title'], axis=1)
data = data.dropna()
x = data.drop('Rating^2', axis=1)
y = data['Rating^2']
x = sm.add_constant(x)

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3, random_state=101)

# fit simple linear regression model
print(OLS(y_train,x_train).fit().summary().as_latex())

fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(8,6))
viz = residuals_plot(LinearRegression(), x_train, y_train, x_test, y_test, ax=ax,
                     title='Linear Regression Residuals when target column is $Rating^2$')
plt.show()