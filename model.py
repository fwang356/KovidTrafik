from statsmodels.tsa.arima_model import ARIMA

import preprocessing as pp
from arima import difference, inverse_difference

series = pp.get_data()
X = series.values

hours_in_week = 168
diff = difference(X, hours_in_week)

model = ARIMA(diff, order=(2, 0, 0))
model_fit = model.fit(trend='nc', disp=0)

model_fit.save('model.pkl')
