import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn import preprocessing

data = pd.read_csv("Data Sets/normalised_movie_data.csv")
data = data.drop(['Genre', 'Title', 'Rank'], axis=1)
data = data.dropna()
x = data.drop('Revenue^{1/3}', axis=1)
y = data['Revenue^{1/3}']
print(x,y)
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2, random_state=101)

model = LinearRegression()
model.fit(x_train, y_train)
predictions = model.predict(x_test)
print(
  'mean_squared_error : ', mean_squared_error(y_test, predictions))
print(
  'mean_absolute_error : ', mean_absolute_error(y_test, predictions))

print(model.score(x_test, y_test))
print(cross_val_score(model, x_test, y_test))
