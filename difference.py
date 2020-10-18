from pandas import Series
from statsmodels.tsa.stattools import adfuller
from matplotlib import pyplot
import preprocessing as pp

# create a differenced series
def difference(dataset, interval=1):
    diff = list()
    for i in range(interval, len(dataset)):
        value = dataset[i] - dataset[i - interval]
        diff.append(value)
    return Series(diff)


series = pp.get_data()
X = series.values
X = X.astype('float32')
# difference data
hours_in_week = 168
stationary = difference(X, hours_in_week)
stationary.index = series.index[hours_in_week:]
# check if stationary
result = adfuller(stationary)
print('ADF Statistic: %f' % result[0])
print('p-value: %f' % result[1])
print('Critical Values:')
for key, value in result[4].items():
    print('\t%s: %.3f' % (key, value))
# save
stationary.to_csv('stationary.csv', header=False)
# plot
stationary.plot()
pyplot.show()