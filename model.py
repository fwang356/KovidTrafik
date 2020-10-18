import warnings
import numpy as np
# import pandas.plotting as pd
import pandas as pd
from matplotlib import pyplot
from statsmodels.tsa.arima_model import ARIMA
from sklearn.metrics import mean_squared_error
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

import preprocessing as pp
from arima import difference, inverse_difference

series = pp.get_data()
X = series.values

hours_in_week = 168
diff = difference(X, hours_in_week)

model = ARIMA(diff, order=(3, 1, 1))
model_fit = model.fit(trend='nc', disp=0)

model_fit.save('model.pkl')
