import numpy as np
import pandas.plotting as pd
from pandas import Series
from matplotlib import pyplot
from statsmodels.tsa.arima_model import ARIMA
import statsmodels.tsa.statespace.sarimax as SARIMAX
from sklearn.metrics import mean_squared_error
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

import preprocessing as pp

# create a differenced series
def difference(dataset, interval=1):
	diff = list()
	for i in range(interval, len(dataset)):
		value = dataset[i] - dataset[i - interval]
		diff.append(value)
	return Series(diff)

# invert differenced value
def inverse_difference(history, yhat, interval=1):
	return yhat + history[-interval]

series = pp.get_data()
X = series.values
size = int(len(X) * 0.66)
train, test = X[0:size], X[size:len(X)]
history = [x for x in train]
predictions = list()

for i in range(len(test)):
	# difference data
	hours_in_week = 168
	diff = difference(history, hours_in_week)
	# predict
	model = ARIMA(diff, order=(2, 1, 1))
	model_fit = model.fit(trend='nc', disp=0)
	yhat = model_fit.forecast()[0]
	yhat = inverse_difference(history, yhat, hours_in_week)
	predictions.append(yhat)
	# observation
	obs = test[i]
	history.append(obs)
	print('Predicted=%d, Expected=%d' % (yhat, obs))
error = mean_squared_error(test, predictions)
print('Test MSE: %.3f' % error)

"""
# plot
pyplot.plot(test)
pyplot.plot(predictions, color='red')
pyplot.show()
"""
