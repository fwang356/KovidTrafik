from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from matplotlib import pyplot
from pandas import read_csv
from statsmodels.tsa.stattools import adfuller
import preprocessing as pp
from arima import difference
"""
series = read_csv("stationary.csv", header=None, index_col=0, parse_dates=True, squeeze=True)
pyplot.figure()
pyplot.subplot(211)
plot_acf(series, ax=pyplot.gca())
pyplot.subplot(212)
plot_pacf(series, ax=pyplot.gca())
pyplot.show()
"""