import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.regression.linear_model import OLS, GLS, WLS
from sklearn.model_selection import train_test_split
# reading the csv file
data = pd.read_csv("Data Sets/normalised_movie_data.csv")
data = data.drop(['Genre', 'Title', 'Votes^{1/3}'], axis=1)
data = data.dropna()
x = data.drop('Revenue^{1/3}', axis=1)
y = data['Revenue^{1/3}']

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3, random_state=101)

# fit simple linear regression model
linear_model = OLS(y_train,x_train).fit()
  
# display model summary
print(linear_model.summary())
fig = plt.figure(figsize=(9,9))
# creating regression plots
sm.graphics.plot_partregress_grid(linear_model, fig=fig)
plt.show()