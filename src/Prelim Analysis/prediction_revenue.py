import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.regression.linear_model import OLS
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from yellowbrick.regressor import residuals_plot
from _Data import *
import matplotlib as mpl

mpl.rcParams['lines.markersize'] = 2

# reading the csv file
data = pd.read_csv("Data Sets/normalised_movie_data.csv")
# data = data[['Family' not in r for r in data['Genre']]]
data = data.drop(['Genre', 'Title', 'Votes^{1/3}'], axis=1)
data = data.dropna()
x = data.drop('Revenue^{1/3}', axis=1)
y = data['Revenue^{1/3}']
x = sm.add_constant(x)
x = to_latex(x)
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3, random_state=101)

# fit simple linear regression 
print(OLS(y,x).fit().summary())
print(re.sub(r'\\\$', '$', OLS(y,x).fit().summary().as_latex()))

fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(4,3))
residuals_plot(LinearRegression(), x_train, y_train, x_test, y_test, ax=ax,
                     title='$Revenue^{\\frac{1}{3}}$ Residuals',
                    show=False)
save_figure(plt, 'Revenue OLS Residuals')