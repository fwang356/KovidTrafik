import numpy as np
import pandas.plotting as pd
from matplotlib import pyplot
from statsmodels.tsa.arima_model import ARIMA
# import statsmodels.tsa.statespace.sarimax.SARIMAX as SARIMAX
from sklearn.metrics import mean_squared_error
from statsmodels.graphics.tsaplots import plot_acf

import preprocessing as pp

series = pp.get_data()
X = series.values
size = int(len(X) * 0.66)
train, test = X[0:size], X[size:len(X)]
history = [x for x in train]
predictions = list()
"""
mini_series = series[0:24]
diff = list()
for i in range(len(series)):
	value = series[i] - series[i-24]
	diff.append(value)
mini_diff = diff[0:120]
# pdiff = pd.Series(diff)
mean = series.rolling(window=24).mean()
# diffmean = pdiff.rolling(window=24).mean()
# print(mean)
std = series.rolling(window=24).std()
# diffstd = pdiff.rolling(window=24).std()
# print(std)
"""

for t in range(len(test)):
	model = SARIMAX(history, order=(24,1,0), seasonal_order=())
	model_fit = model.fit(disp=0)
	output = model_fit.forecast()
	yhat = output[0]
	predictions.append(yhat)
	obs = test[t]
	history.append(obs)
	print('predicted=%f, expected=%f' % (yhat, obs))
error = mean_squared_error(test, predictions)
print('Test MSE: %.3f' % error)

"""
# plot
pyplot.plot(test)
pyplot.plot(predictions, color='red')
pd.autocorrelation_plot(mini_series)
#pyplot.plot(diffmean, color = "green")
#pyplot.plot(diffstd, color = "red")
plot_acf(series)
pyplot.show()
